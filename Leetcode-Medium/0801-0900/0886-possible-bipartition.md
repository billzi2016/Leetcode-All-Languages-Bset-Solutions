# 0886. Possible Bipartition

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        vector<vector<int>> adj(n + 1);
        for (const auto& d : dislikes) {
            int a = d[0], b = d[1];
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
        vector<int> color(n + 1, 0); // 0: uncolored, 1 or -1
        for (int i = 1; i <= n; ++i) {
            if (color[i] != 0) continue;
            queue<int> q;
            q.push(i);
            color[i] = 1;
            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (int v : adj[u]) {
                    if (color[v] == 0) {
                        color[v] = -color[u];
                        q.push(v);
                    } else if (color[v] == color[u]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean possibleBipartition(int n, int[][] dislikes) {
        List<Integer>[] graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] d : dislikes) {
            int a = d[0], b = d[1];
            graph[a].add(b);
            graph[b].add(a);
        }

        int[] color = new int[n + 1]; // 0 = uncolored, 1 or -1
        for (int i = 1; i <= n; i++) {
            if (color[i] != 0) continue;
            Queue<Integer> q = new ArrayDeque<>();
            q.offer(i);
            color[i] = 1;
            while (!q.isEmpty()) {
                int cur = q.poll();
                for (int nb : graph[cur]) {
                    if (color[nb] == 0) {
                        color[nb] = -color[cur];
                        q.offer(nb);
                    } else if (color[nb] == color[cur]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        from collections import deque

        # Build adjacency list (1-indexed)
        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = [0] * (n + 1)  # 0: uncolored, 1 or -1: two groups

        for start in range(1, n + 1):
            if color[start] != 0:
                continue
            # Start BFS from this node
            queue = deque([start])
            color[start] = 1
            while queue:
                node = queue.popleft()
                cur_color = color[node]
                for nei in graph[node]:
                    if color[nei] == 0:
                        color[nei] = -cur_color
                        queue.append(nei)
                    elif color[nei] == cur_color:
                        return False
        return True
```

## Python3

```python
from typing import List
from collections import deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = [0] * (n + 1)  # 0 = uncolored, 1 or -1 = two groups

        for i in range(1, n + 1):
            if color[i] != 0 or not graph[i]:
                continue
            queue = deque([i])
            color[i] = 1
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == 0:
                        color[v] = -color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
        return True
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

bool possibleBipartition(int n, int** dislikes, int dislikesSize, int* dislikesColSize) {
    if (dislikesSize == 0) return true;

    int *degree = calloc(n + 1, sizeof(int));
    for (int i = 0; i < dislikesSize; ++i) {
        int a = dislikes[i][0];
        int b = dislikes[i][1];
        degree[a]++;
        degree[b]++;
    }

    int **adj = malloc((n + 1) * sizeof(int*));
    for (int i = 1; i <= n; ++i) {
        if (degree[i] > 0)
            adj[i] = malloc(degree[i] * sizeof(int));
        else
            adj[i] = NULL;
    }

    int *pos = calloc(n + 1, sizeof(int));
    for (int i = 0; i < dislikesSize; ++i) {
        int a = dislikes[i][0];
        int b = dislikes[i][1];
        adj[a][pos[a]++] = b;
        adj[b][pos[b]++] = a;
    }

    free(pos);
    free(degree);

    int *color = calloc(n + 1, sizeof(int)); // 0: uncolored, 1 or -1
    int *queue = malloc((n + 1) * sizeof(int));
    for (int start = 1; start <= n; ++start) {
        if (color[start] != 0) continue;
        color[start] = 1;
        int front = 0, rear = 0;
        queue[rear++] = start;

        while (front < rear) {
            int u = queue[front++];
            for (int i = 0; i < (adj[u] ? ((dislikesColSize && dislikesColSize[0]) : 0) : 0); ++i) {} // placeholder to avoid unused warning
            int deg = 0;
            if (adj[u]) {
                // compute degree by checking adjacency list length via original degree info not stored; we can infer from allocated size.
                // Since we don't store sizes, we recompute using the original degree array is freed. Instead, we track degrees during building.
                // Simpler: reuse the fact that we know each node's neighbor count equals pos after filling, but pos was freed.
                // To avoid complexity, we can store degrees again before freeing.
            }
        }
    }

    // The above loop incomplete due to missing degree info. Re-implement with stored degrees.

    // Rebuild with degree tracking
    // (Simplify: redo building with degree array retained)
    // Clean up and rebuild correctly

    // Cleanup previous allocations
    for (int i = 1; i <= n; ++i) {
        if (adj[i]) free(adj[i]);
    }
    free(adj);
    free(color);
    free(queue);

    // Rebuild with degree info retained
    int *degArr = calloc(n + 1, sizeof(int));
    for (int i = 0; i < dislikesSize; ++i) {
        degArr[dislikes[i][0]]++;
        degArr[dislikes[i][1]]++;
    }

    adj = malloc((n + 1) * sizeof(int*));
    for (int i = 1; i <= n; ++i) {
        if (degArr[i] > 0)
            adj[i] = malloc(degArr[i] * sizeof(int));
        else
            adj[i] = NULL;
    }

    pos = calloc(n + 1, sizeof(int));
    for (int i = 0; i < dislikesSize; ++i) {
        int a = dislikes[i][0];
        int b = dislikes[i][1];
        adj[a][pos[a]++] = b;
        adj[b][pos[b]++] = a;
    }

    free(pos);
    color = calloc(n + 1, sizeof(int));
    queue = malloc((n + 1) * sizeof(int));

    for (int start = 1; start <= n; ++start) {
        if (color[start] != 0) continue;
        color[start] = 1;
        int front = 0, rear = 0;
        queue[rear++] = start;

        while (front < rear) {
            int u = queue[front++];
            for (int i = 0; i < degArr[u]; ++i) {
                int v = adj[u][i];
                if (color[v] == 0) {
                    color[v] = -color[u];
                    queue[rear++] = v;
                } else if (color[v] == color[u]) {
                    // cleanup
                    for (int j = 1; j <= n; ++j) {
                        if (adj[j]) free(adj[j]);
                    }
                    free(adj);
                    free(degArr);
                    free(color);
                    free(queue);
                    return false;
                }
            }
        }
    }

    // cleanup
    for (int i = 1; i <= n; ++i) {
        if (adj[i]) free(adj[i]);
    }
    free(adj);
    free(degArr);
    free(color);
    free(queue);
    return true;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public bool PossibleBipartition(int n, int[][] dislikes) {
        var graph = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) graph[i] = new List<int>();
        foreach (var d in dislikes) {
            int a = d[0], b = d[1];
            graph[a].Add(b);
            graph[b].Add(a);
        }

        var color = new int[n + 1]; // 0 = uncolored, 1 or -1
        for (int i = 1; i <= n; i++) {
            if (color[i] != 0) continue;
            var queue = new Queue<int>();
            queue.Enqueue(i);
            color[i] = 1;

            while (queue.Count > 0) {
                int cur = queue.Dequeue();
                foreach (int nb in graph[cur]) {
                    if (color[nb] == 0) {
                        color[nb] = -color[cur];
                        queue.Enqueue(nb);
                    } else if (color[nb] == color[cur]) {
                        return false;
                    }
                }
            }
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} dislikes
 * @return {boolean}
 */
var possibleBipartition = function(n, dislikes) {
    const graph = Array.from({ length: n + 1 }, () => []);
    for (const [a, b] of dislikes) {
        graph[a].push(b);
        graph[b].push(a);
    }
    const color = new Array(n + 1).fill(0); // 0 = uncolored, 1 or -1
    
    for (let i = 1; i <= n; i++) {
        if (color[i] !== 0) continue;
        const stack = [i];
        color[i] = 1;
        while (stack.length) {
            const node = stack.pop();
            for (const nei of graph[node]) {
                if (color[nei] === 0) {
                    color[nei] = -color[node];
                    stack.push(nei);
                } else if (color[nei] === color[node]) {
                    return false;
                }
            }
        }
    }
    return true;
};
```

## Typescript

```typescript
function possibleBipartition(n: number, dislikes: number[][]): boolean {
    const adj: number[][] = Array.from({ length: n + 1 }, () => []);
    for (const [a, b] of dislikes) {
        adj[a].push(b);
        adj[b].push(a);
    }
    const color = new Int8Array(n + 1); // 0 = uncolored, 1 or -1
    const queue: number[] = [];
    for (let i = 1; i <= n; ++i) {
        if (color[i] !== 0) continue;
        color[i] = 1;
        queue.length = 0;
        queue.push(i);
        let qIdx = 0;
        while (qIdx < queue.length) {
            const cur = queue[qIdx++];
            for (const nb of adj[cur]) {
                if (color[nb] === 0) {
                    color[nb] = -color[cur];
                    queue.push(nb);
                } else if (color[nb] === color[cur]) {
                    return false;
                }
            }
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $dislikes
     * @return Boolean
     */
    function possibleBipartition($n, $dislikes) {
        // Build adjacency list
        $graph = array_fill(0, $n + 1, []);
        foreach ($dislikes as $pair) {
            $a = $pair[0];
            $b = $pair[1];
            $graph[$a][] = $b;
            $graph[$b][] = $a;
        }

        // 0 = uncolored, 1 = color A, -1 = color B
        $color = array_fill(0, $n + 1, 0);

        for ($i = 1; $i <= $n; $i++) {
            if ($color[$i] !== 0) {
                continue;
            }
            // BFS starting from node i
            $queue = new SplQueue();
            $queue->enqueue($i);
            $color[$i] = 1;

            while (!$queue->isEmpty()) {
                $node = $queue->dequeue();
                foreach ($graph[$node] as $neighbor) {
                    if ($color[$neighbor] === 0) {
                        $color[$neighbor] = -$color[$node];
                        $queue->enqueue($neighbor);
                    } elseif ($color[$neighbor] === $color[$node]) {
                        return false;
                    }
                }
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func possibleBipartition(_ n: Int, _ dislikes: [[Int]]) -> Bool {
        var graph = [[Int]](repeating: [], count: n + 1)
        for pair in dislikes {
            let a = pair[0]
            let b = pair[1]
            graph[a].append(b)
            graph[b].append(a)
        }
        
        var color = [Int](repeating: -1, count: n + 1) // -1 = uncolored, 0/1 = two groups
        
        for person in 1...n {
            if color[person] != -1 { continue }
            var queue = [Int]()
            queue.append(person)
            color[person] = 0
            var index = 0
            
            while index < queue.count {
                let current = queue[index]
                index += 1
                for neighbor in graph[current] {
                    if color[neighbor] == -1 {
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    } else if color[neighbor] == color[current] {
                        return false
                    }
                }
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun possibleBipartition(n: Int, dislikes: Array<IntArray>): Boolean {
        val graph = Array(n + 1) { mutableListOf<Int>() }
        for (pair in dislikes) {
            val a = pair[0]
            val b = pair[1]
            graph[a].add(b)
            graph[b].add(a)
        }

        val color = IntArray(n + 1)
        val queue: java.util.ArrayDeque<Int> = java.util.ArrayDeque()

        for (i in 1..n) {
            if (color[i] != 0) continue
            color[i] = 1
            queue.clear()
            queue.add(i)

            while (!queue.isEmpty()) {
                val cur = queue.poll()
                for (nei in graph[cur]) {
                    if (color[nei] == 0) {
                        color[nei] = -color[cur]
                        queue.add(nei)
                    } else if (color[nei] == color[cur]) {
                        return false
                    }
                }
            }
        }

        return true
    }
}
```

## Dart

```dart
class Solution {
  bool possibleBipartition(int n, List<List<int>> dislikes) {
    // Build adjacency list
    var graph = List.generate(n + 1, (_) => <int>[]);
    for (var pair in dislikes) {
      int a = pair[0];
      int b = pair[1];
      graph[a].add(b);
      graph[b].add(a);
    }

    // 0 = uncolored, 1 = color A, -1 = color B
    var color = List.filled(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
      if (color[i] != 0) continue;
      // BFS starting from node i
      var queue = <int>[];
      queue.add(i);
      color[i] = 1;
      int idx = 0;

      while (idx < queue.length) {
        int node = queue[idx++];
        for (int neighbor in graph[node]) {
          if (color[neighbor] == 0) {
            color[neighbor] = -color[node];
            queue.add(neighbor);
          } else if (color[neighbor] == color[node]) {
            return false;
          }
        }
      }
    }

    return true;
  }
}
```

## Golang

```go
func possibleBipartition(n int, dislikes [][]int) bool {
	graph := make([][]int, n+1)
	for _, d := range dislikes {
		a, b := d[0], d[1]
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}
	color := make([]int, n+1) // 0: uncolored, 1 or -1
	for i := 1; i <= n; i++ {
		if color[i] != 0 || len(graph[i]) == 0 {
			continue
		}
		stack := []int{i}
		color[i] = 1
		for len(stack) > 0 {
			v := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			for _, nb := range graph[v] {
				if color[nb] == 0 {
					color[nb] = -color[v]
					stack = append(stack, nb)
				} else if color[nb] == color[v] {
					return false
				}
			}
		}
	}
	return true
}
```

## Ruby

```ruby
def possible_bipartition(n, dislikes)
  graph = Array.new(n + 1) { [] }
  dislikes.each do |a, b|
    graph[a] << b
    graph[b] << a
  end

  color = Array.new(n + 1, 0)

  (1..n).each do |i|
    next unless color[i].zero?

    color[i] = 1
    queue = [i]
    head = 0
    while head < queue.size
      cur = queue[head]
      head += 1
      graph[cur].each do |nbr|
        if color[nbr].zero?
          color[nbr] = -color[cur]
          queue << nbr
        elsif color[nbr] == color[cur]
          return false
        end
      end
    end
  end

  true
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.ArrayBuffer

  def possibleBipartition(n: Int, dislikes: Array[Array[Int]]): Boolean = {
    val graph = Array.fill(n + 1)(new ArrayBuffer[Int]())
    for (pair <- dislikes) {
      val a = pair(0)
      val b = pair(1)
      graph(a).append(b)
      graph(b).append(a)
    }

    val color = new Array[Int](n + 1) // 0 = uncolored, 1 or -1

    def dfs(node: Int, c: Int): Boolean = {
      color(node) = c
      for (nbr <- graph(node)) {
        if (color(nbr) == 0) {
          if (!dfs(nbr, -c)) return false
        } else if (color(nbr) == c) {
          return false
        }
      }
      true
    }

    for (i <- 1 to n) {
      if (color(i) == 0 && !dfs(i, 1)) return false
    }
    true
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn possible_bipartition(n: i32, dislikes: Vec<Vec<i32>>) -> bool {
        let n = n as usize;
        let mut graph: Vec<Vec<usize>> = vec![Vec::new(); n];
        for d in dislikes.iter() {
            let a = (d[0] - 1) as usize;
            let b = (d[1] - 1) as usize;
            graph[a].push(b);
            graph[b].push(a);
        }
        let mut color = vec![0i32; n];
        for i in 0..n {
            if color[i] == 0 {
                let mut queue = VecDeque::new();
                queue.push_back(i);
                color[i] = 1;
                while let Some(u) = queue.pop_front() {
                    let cur_color = color[u];
                    for &v in &graph[u] {
                        if color[v] == 0 {
                            color[v] = -cur_color;
                            queue.push_back(v);
                        } else if color[v] == cur_color {
                            return false;
                        }
                    }
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (possible-bipartition n dislikes)
  (-> exact-integer? (listof (listof exact-integer?)) boolean?)
  (let* ((adj (make-vector (+ n 1) '()))
         (color (make-vector (+ n 1) 0)))
    ;; build adjacency list
    (for-each
     (lambda (pair)
       (let ((a (list-ref pair 0))
             (b (list-ref pair 1)))
         (vector-set! adj a (cons b (vector-ref adj a)))
         (vector-set! adj b (cons a (vector-ref adj b)))))
     dislikes)
    ;; use call/cc for early exit on conflict
    (call/cc
      (lambda (return)
        (define (bfs start)
          (let ((queue (make-vector (+ n 1) 0))
                (head 0)
                (tail 0))
            (vector-set! queue tail start)
            (set! tail (+ tail 1))
            (vector-set! color start 1)
            (let loop ()
              (if (= head tail)
                  #t
                  (let ((node (vector-ref queue head)))
                    (set! head (+ head 1))
                    (for ([nbr (vector-ref adj node)])
                      (cond [(= (vector-ref color nbr) 0)
                             (vector-set! color nbr (- (vector-ref color node)))
                             (vector-set! queue tail nbr)
                             (set! tail (+ tail 1))]
                            [(= (vector-ref color nbr) (vector-ref color node))
                             (return #f)]))
                    (loop))))))
        (for ([i (in-range 1 (+ n 1))])
          (when (= (vector-ref color i) 0)
            (unless (bfs i)
              (return #f))))
        #t))))
```

## Erlang

```erlang
-spec possible_bipartition(N :: integer(), Dislikes :: [[integer()]]) -> boolean().
possible_bipartition(N, Dislikes) ->
    Adj0 = maps:from_list(lists:map(fun(I) -> {I, []} end, lists:seq(1, N))),
    Adj = lists:foldl(
        fun([A, B], Acc) ->
            Acc1 = maps:update_with(A,
                    fun(L) -> [B | L] end,
                    [B],
                    Acc),
            maps:update_with(B,
                fun(L) -> [A | L] end,
                [A],
                Acc1)
        end,
        Adj0,
        Dislikes),
    process_nodes(lists:seq(1, N), Adj, #{}).

process_nodes([], _Adj, _Colors) ->
    true;
process_nodes([Node | Rest], Adj, Colors) ->
    case maps:is_key(Node, Colors) of
        true ->
            process_nodes(Rest, Adj, Colors);
        false ->
            case bfs([Node], Adj, maps:put(Node, 1, Colors)) of
                {error} -> false;
                {ok, NewColors} -> process_nodes(Rest, Adj, NewColors)
            end
    end.

bfs([], _Adj, Colors) ->
    {ok, Colors};
bfs([Curr | Queue], Adj, Colors) ->
    CurrColor = maps:get(Curr, Colors),
    Neighbors = maps:get(Curr, Adj, []),
    case process_neighbors(Neighbors, CurrColor, Adj, Colors, Queue) of
        {error} -> {error};
        {ok, UpdatedColors, UpdatedQueue} -> bfs(UpdatedQueue, Adj, UpdatedColors)
    end.

process_neighbors([], _CurrColor, _Adj, Colors, Queue) ->
    {ok, Colors, Queue};
process_neighbors([Nb | Rest], CurrColor, Adj, Colors, Queue) ->
    case maps:find(Nb, Colors) of
        error ->
            NewColor = -CurrColor,
            NewColors = maps:put(Nb, NewColor, Colors),
            process_neighbors(Rest, CurrColor, Adj, NewColors, [Nb | Queue]);
        {ok, NbColor} ->
            if NbColor == CurrColor ->
                    {error};
               true ->
                    process_neighbors(Rest, CurrColor, Adj, Colors, Queue)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec possible_bipartition(n :: integer, dislikes :: [[integer]]) :: boolean
  def possible_bipartition(_n, []), do: true

  def possible_bipartition(n, dislikes) do
    adj = build_adj(dislikes, %{})

    result =
      Enum.reduce_while(1..n, %{}, fn node, colors ->
        if Map.has_key?(colors, node) do
          {:cont, colors}
        else
          case bfs(node, 0, adj, colors) do
            :error -> {:halt, :error}
            new_colors -> {:cont, new_colors}
          end
        end
      end)

    result != :error
  end

  defp build_adj([], adj), do: adj

  defp build_adj([[a, b] | rest], adj) do
    adj1 = Map.update(adj, a, [b], fn lst -> [b | lst] end)
    adj2 = Map.update(adj1, b, [a], fn lst -> [a | lst] end)
    build_adj(rest, adj2)
  end

  defp bfs(start, start_color, adj, colors) do
    bfs_loop([{start, start_color}], adj, colors)
  end

  defp bfs_loop([], _adj, colors), do: colors

  defp bfs_loop([{node, col} | rest], adj, colors) do
    case Map.get(colors, node) do
      nil ->
        new_colors = Map.put(colors, node, col)

        neighbors = Map.get(adj, node, [])

        new_queue =
          Enum.reduce(neighbors, rest, fn nb, q ->
            [{nb, 1 - col} | q]
          end)

        bfs_loop(new_queue, adj, new_colors)

      existing_col when existing_col == col ->
        bfs_loop(rest, adj, colors)

      _ ->
        :error
    end
  end
end
```

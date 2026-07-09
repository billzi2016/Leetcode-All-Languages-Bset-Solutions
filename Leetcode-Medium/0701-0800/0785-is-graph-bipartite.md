# 0785. Is Graph Bipartite?

## Cpp

```cpp
class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> color(n, 0); // 0: uncolored, 1 or -1
        queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (color[i] != 0) continue;
            color[i] = 1;
            q.push(i);
            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (int v : graph[u]) {
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
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n]; // 0 = uncolored, 1 and -1 are two colors
        java.util.Queue<Integer> queue = new java.util.ArrayDeque<>();
        
        for (int i = 0; i < n; i++) {
            if (color[i] != 0) continue;
            color[i] = 1;
            queue.offer(i);
            
            while (!queue.isEmpty()) {
                int node = queue.poll();
                for (int neighbor : graph[node]) {
                    if (color[neighbor] == 0) {
                        color[neighbor] = -color[node];
                        queue.offer(neighbor);
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

## Python

```python
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        from collections import deque

        n = len(graph)
        color = [0] * n  # 0 = uncolored, 1 and -1 are the two colors

        for start in range(n):
            if color[start] != 0:
                continue
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
class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [0] * n  # 0: uncolored, 1 and -1 are the two colors
        from collections import deque

        for start in range(n):
            if color[start] != 0:
                continue
            queue = deque([start])
            color[start] = 1
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if color[nei] == 0:
                        color[nei] = -color[node]
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        return False
        return True
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool isBipartite(int** graph, int graphSize, int* graphColSize) {
    if (graphSize == 0) return true;
    int *color = (int *)malloc(graphSize * sizeof(int));
    for (int i = 0; i < graphSize; ++i) color[i] = -1;
    int *queue = (int *)malloc(graphSize * sizeof(int));

    for (int start = 0; start < graphSize; ++start) {
        if (color[start] != -1) continue;
        int head = 0, tail = 0;
        queue[tail++] = start;
        color[start] = 0;

        while (head < tail) {
            int u = queue[head++];
            for (int k = 0; k < graphColSize[u]; ++k) {
                int v = graph[u][k];
                if (color[v] == -1) {
                    color[v] = color[u] ^ 1;
                    queue[tail++] = v;
                } else if (color[v] == color[u]) {
                    free(color);
                    free(queue);
                    return false;
                }
            }
        }
    }

    free(color);
    free(queue);
    return true;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public bool IsBipartite(int[][] graph) {
        int n = graph.Length;
        int[] colors = new int[n]; // 0 = uncolored, 1 or -1
        
        for (int i = 0; i < n; i++) {
            if (colors[i] != 0) continue;
            
            Queue<int> q = new Queue<int>();
            q.Enqueue(i);
            colors[i] = 1;
            
            while (q.Count > 0) {
                int node = q.Dequeue();
                foreach (int neighbor in graph[node]) {
                    if (colors[neighbor] == 0) {
                        colors[neighbor] = -colors[node];
                        q.Enqueue(neighbor);
                    } else if (colors[neighbor] == colors[node]) {
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
 * @param {number[][]} graph
 * @return {boolean}
 */
var isBipartite = function(graph) {
    const n = graph.length;
    const color = new Array(n).fill(-1); // -1: uncolored, 0 and 1 are the two colors
    
    for (let start = 0; start < n; ++start) {
        if (color[start] !== -1) continue; // already colored component
        
        // BFS from start node
        const queue = [];
        queue.push(start);
        color[start] = 0;
        
        while (queue.length) {
            const node = queue.shift();
            const curColor = color[node];
            const nextColor = curColor ^ 1; // toggle between 0 and 1
            
            for (const nei of graph[node]) {
                if (color[nei] === -1) {
                    color[nei] = nextColor;
                    queue.push(nei);
                } else if (color[nei] !== nextColor) {
                    return false; // adjacent nodes share same color
                }
            }
        }
    }
    
    return true;
};
```

## Typescript

```typescript
function isBipartite(graph: number[][]): boolean {
    const n = graph.length;
    const colors = new Array<number>(n).fill(0); // 0 = uncolored, 1 or -1
    
    for (let i = 0; i < n; i++) {
        if (colors[i] !== 0) continue;
        colors[i] = 1;
        const queue: number[] = [i];
        let head = 0;
        
        while (head < queue.length) {
            const node = queue[head++];
            for (const nei of graph[node]) {
                if (colors[nei] === 0) {
                    colors[nei] = -colors[node];
                    queue.push(nei);
                } else if (colors[nei] === colors[node]) {
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
     * @param Integer[][] $graph
     * @return Boolean
     */
    function isBipartite($graph) {
        $n = count($graph);
        $color = array_fill(0, $n, 0); // 0: uncolored, 1 or -1: colors

        for ($i = 0; $i < $n; $i++) {
            if ($color[$i] !== 0) {
                continue;
            }
            $queue = new SplQueue();
            $queue->enqueue($i);
            $color[$i] = 1;

            while (!$queue->isEmpty()) {
                $u = $queue->dequeue();
                foreach ($graph[$u] as $v) {
                    if ($color[$v] === 0) {
                        $color[$v] = -$color[$u];
                        $queue->enqueue($v);
                    } elseif ($color[$v] === $color[$u]) {
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
    func isBipartite(_ graph: [[Int]]) -> Bool {
        let n = graph.count
        var color = Array(repeating: -1, count: n)
        for start in 0..<n {
            if color[start] != -1 { continue }
            var queue = [start]
            color[start] = 0
            var index = 0
            while index < queue.count {
                let node = queue[index]
                index += 1
                for neighbor in graph[node] {
                    if color[neighbor] == -1 {
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    } else if color[neighbor] == color[node] {
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
    fun isBipartite(graph: Array<IntArray>): Boolean {
        val n = graph.size
        val colors = IntArray(n)
        val queue = java.util.ArrayDeque<Int>()
        for (i in 0 until n) {
            if (colors[i] != 0) continue
            colors[i] = 1
            queue.clear()
            queue.add(i)
            while (!queue.isEmpty()) {
                val u = queue.poll()
                val cu = colors[u]
                for (v in graph[u]) {
                    if (colors[v] == 0) {
                        colors[v] = -cu
                        queue.add(v)
                    } else if (colors[v] == cu) {
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
  bool isBipartite(List<List<int>> graph) {
    int n = graph.length;
    List<int> colors = List.filled(n, 0); // 0: uncolored, 1 and -1: two colors

    for (int i = 0; i < n; ++i) {
      if (colors[i] != 0) continue;

      // BFS starting from node i
      List<int> queue = [i];
      colors[i] = 1;
      int idx = 0;

      while (idx < queue.length) {
        int node = queue[idx++];
        for (int neighbor in graph[node]) {
          if (colors[neighbor] == 0) {
            colors[neighbor] = -colors[node];
            queue.add(neighbor);
          } else if (colors[neighbor] == colors[node]) {
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
func isBipartite(graph [][]int) bool {
	n := len(graph)
	color := make([]int, n)
	for i := 0; i < n; i++ {
		color[i] = -1
	}
	for start := 0; start < n; start++ {
		if color[start] != -1 {
			continue
		}
		queue := []int{start}
		color[start] = 0
		for len(queue) > 0 {
			v := queue[0]
			queue = queue[1:]
			for _, nb := range graph[v] {
				if color[nb] == -1 {
					color[nb] = 1 - color[v]
					queue = append(queue, nb)
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
def is_bipartite(graph)
  n = graph.length
  colors = Array.new(n, -1)

  (0...n).each do |i|
    next if colors[i] != -1
    colors[i] = 0
    queue = [i]

    until queue.empty?
      node = queue.shift
      graph[node].each do |nbr|
        if colors[nbr] == -1
          colors[nbr] = 1 - colors[node]
          queue << nbr
        elsif colors[nbr] == colors[node]
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
    def isBipartite(graph: Array[Array[Int]]): Boolean = {
        val n = graph.length
        val color = new Array[Int](n)
        java.util.Arrays.fill(color, -1)

        import scala.collection.mutable.Queue

        for (i <- 0 until n) {
            if (color(i) == -1) {
                val q = Queue[Int]()
                q.enqueue(i)
                color(i) = 0
                while (q.nonEmpty) {
                    val u = q.dequeue()
                    for (v <- graph(u)) {
                        if (color(v) == -1) {
                            color(v) = 1 - color(u)
                            q.enqueue(v)
                        } else if (color(v) == color(u)) {
                            return false
                        }
                    }
                }
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_bipartite(graph: Vec<Vec<i32>>) -> bool {
        let n = graph.len();
        let mut colors = vec![-1i8; n];
        use std::collections::VecDeque;
        for start in 0..n {
            if colors[start] != -1 {
                continue;
            }
            colors[start] = 0;
            let mut queue = VecDeque::new();
            queue.push_back(start);
            while let Some(u) = queue.pop_front() {
                let cu = colors[u];
                for &v_i32 in &graph[u] {
                    let v = v_i32 as usize;
                    if colors[v] == -1 {
                        colors[v] = 1 - cu;
                        queue.push_back(v);
                    } else if colors[v] == cu {
                        return false;
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
(define/contract (is-bipartite graph)
  (-> (listof (listof exact-integer?)) boolean?)
  (let* ((n (length graph))
         (adj (list->vector graph))
         (color (make-vector n 0)))
    (define (dfs v col)
      (vector-set! color v col)
      (let loop ((neighbors (vector-ref adj v)))
        (cond
          [(null? neighbors) #t]
          [else
           (let* ((nbr (car neighbors))
                  (c (vector-ref color nbr)))
             (cond
               [(= c 0)
                (if (dfs nbr (- col))
                    (loop (cdr neighbors))
                    #f)]
               [(= c col) #f]
               [else (loop (cdr neighbors))]))]))
    (let ((ok #t))
      (for ([i (in-range n)])
        (when (and ok (= (vector-ref color i) 0))
          (set! ok (dfs i 1))))
      ok)))
```

## Erlang

```erlang
-module(solution).
-export([is_bipartite/1]).
-spec is_bipartite(Graph :: [[integer()]]) -> boolean().
is_bipartite(Graph) ->
    N = length(Graph),
    case bipartite_check(0, N, Graph, #{}) of
        {ok,_} -> true;
        error -> false
    end.

bipartite_check(Index, N, _Graph, Colors) when Index >= N ->
    {ok, Colors};
bipartite_check(Index, N, Graph, Colors) ->
    case maps:is_key(Index, Colors) of
        true ->
            bipartite_check(Index + 1, N, Graph, Colors);
        false ->
            case bfs([{Index, 1}], Graph, Colors) of
                {ok, NewColors} -> bipartite_check(Index + 1, N, Graph, NewColors);
                error -> error
            end
    end.

bfs([], _Graph, Colors) ->
    {ok, Colors};
bfs([{Node, Color}|RestQueue], Graph, Colors) ->
    case maps:get(Node, Colors, undefined) of
        undefined ->
            UpdatedColors = maps:put(Node, Color, Colors),
            Adj = lists:nth(Node + 1, Graph),
            case process_neighbors(Adj, -Color, RestQueue, UpdatedColors) of
                {ok, NewQueue} -> bfs(NewQueue, Graph, UpdatedColors);
                error -> error
            end;
        ExistingColor ->
            if ExistingColor =:= Color ->
                    bfs(RestQueue, Graph, Colors);
               true -> error
            end
    end.

process_neighbors([], _Color, Queue, _Colors) ->
    {ok, Queue};
process_neighbors([Nbr|Rest], Color, Queue, Colors) ->
    case maps:get(Nbr, Colors, undefined) of
        undefined ->
            process_neighbors(Rest, Color, [{Nbr, Color}|Queue], Colors);
        Existing when Existing =:= Color ->
            process_neighbors(Rest, Color, Queue, Colors);
        _Other ->
            error
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_bipartite(graph :: [[integer]]) :: boolean
  def is_bipartite(graph) do
    n = length(graph)

    result =
      Enum.reduce_while(0..(n - 1), %{}, fn node, colors ->
        if Map.has_key?(colors, node) do
          {:cont, colors}
        else
          case bfs(node, graph, colors) do
            {:ok, new_colors} -> {:cont, new_colors}
            :error -> {:halt, :not_bipartite}
          end
        end
      end)

    case result do
      :not_bipartite -> false
      _ -> true
    end
  end

  defp bfs(start, graph, colors) do
    queue = :queue.in(start, :queue.new())
    colors = Map.put(colors, start, 0)

    try do
      final_colors = bfs_loop(queue, graph, colors)
      {:ok, final_colors}
    catch
      :conflict -> :error
    end
  end

  defp bfs_loop(queue, graph, colors) do
    case :queue.out(queue) do
      {:empty, _} ->
        colors

      {{:value, node}, q} ->
        cur_color = Map.get(colors, node)
        neighbors = Enum.at(graph, node)

        {new_colors, new_queue} =
          Enum.reduce(neighbors, {colors, q}, fn nb, {col_map, q_acc} ->
            case Map.fetch(col_map, nb) do
              :error ->
                {Map.put(col_map, nb, 1 - cur_color), :queue.in(nb, q_acc)}

              {:ok, c} when c == cur_color ->
                throw(:conflict)

              _ ->
                {col_map, q_acc}
            end
          end)

        bfs_loop(new_queue, graph, new_colors)
    end
  end
end
```

# 0847. Shortest Path Visiting All Nodes

## Cpp

```cpp
class Solution {
public:
    int shortestPathLength(vector<vector<int>>& graph) {
        int n = graph.size();
        if (n == 1) return 0;
        int fullMask = (1 << n) - 1;
        vector<vector<int>> dist(n, vector<int>(1 << n, -1));
        queue<pair<int,int>> q;
        for (int i = 0; i < n; ++i) {
            int mask = 1 << i;
            dist[i][mask] = 0;
            q.emplace(i, mask);
        }
        while (!q.empty()) {
            auto [u, mask] = q.front(); q.pop();
            int d = dist[u][mask];
            if (mask == fullMask) return d;
            for (int v : graph[u]) {
                int nextMask = mask | (1 << v);
                if (dist[v][nextMask] == -1) {
                    dist[v][nextMask] = d + 1;
                    q.emplace(v, nextMask);
                }
            }
        }
        return -1; // should never reach here
    }
};
```

## Java

```java
import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int shortestPathLength(int[][] graph) {
        int n = graph.length;
        if (n == 1) return 0;
        int finalMask = (1 << n) - 1;
        boolean[][] visited = new boolean[n][1 << n];
        Queue<int[]> queue = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            int mask = 1 << i;
            queue.offer(new int[]{i, mask});
            visited[i][mask] = true;
        }

        int steps = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int s = 0; s < size; s++) {
                int[] cur = queue.poll();
                int node = cur[0];
                int mask = cur[1];

                if (mask == finalMask) {
                    return steps;
                }

                for (int nei : graph[node]) {
                    int nextMask = mask | (1 << nei);
                    if (!visited[nei][nextMask]) {
                        visited[nei][nextMask] = true;
                        queue.offer(new int[]{nei, nextMask});
                    }
                }
            }
            steps++;
        }

        return -1; // Should never reach here for a connected graph
    }
}
```

## Python

```python
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        from collections import deque
        n = len(graph)
        if n == 1:
            return 0
        final_mask = (1 << n) - 1
        visited = [[False] * (1 << n) for _ in range(n)]
        dq = deque()
        for i in range(n):
            mask = 1 << i
            dq.append((i, mask))
            visited[i][mask] = True
        steps = 0
        while dq:
            for _ in range(len(dq)):
                node, mask = dq.popleft()
                if mask == final_mask:
                    return steps
                for nei in graph[node]:
                    next_mask = mask | (1 << nei)
                    if not visited[nei][next_mask]:
                        visited[nei][next_mask] = True
                        dq.append((nei, next_mask))
            steps += 1
        return -1
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        final_mask = (1 << n) - 1
        visited = [[False] * (1 << n) for _ in range(n)]
        q = deque()
        for i in range(n):
            mask = 1 << i
            visited[i][mask] = True
            q.append((i, mask, 0))
        while q:
            node, mask, dist = q.popleft()
            if mask == final_mask:
                return dist
            for nei in graph[node]:
                nxt_mask = mask | (1 << nei)
                if not visited[nei][nxt_mask]:
                    visited[nei][nxt_mask] = True
                    q.append((nei, nxt_mask, dist + 1))
        return -1
```

## C

```c
#include <stdlib.h>
#include <string.h>

int shortestPathLength(int** graph, int graphSize, int* graphColSize) {
    const int MAXN = 12;
    const int MAXMASK = 1 << MAXN;          // 4096
    static char visited[MAXN][MAXMASK];
    
    int n = graphSize;
    int maxMask = 1 << n;
    int fullMask = maxMask - 1;
    
    for (int i = 0; i < n; ++i) {
        memset(visited[i], 0, maxMask);
    }
    
    typedef struct { short node; short mask; } State;
    static State q[MAXN * MAXMASK];
    int head = 0, tail = 0;
    
    for (int i = 0; i < n; ++i) {
        int m = 1 << i;
        visited[i][m] = 1;
        q[tail++] = (State){(short)i, (short)m};
    }
    
    int steps = 0;
    while (head < tail) {
        int curLevelSize = tail - head;
        for (int s = 0; s < curLevelSize; ++s) {
            State cur = q[head++];
            if (cur.mask == fullMask) return steps;
            int u = cur.node;
            int mask = cur.mask;
            int deg = graphColSize[u];
            int *nbr = graph[u];
            for (int k = 0; k < deg; ++k) {
                int v = nbr[k];
                int newMask = mask | (1 << v);
                if (!visited[v][newMask]) {
                    visited[v][newMask] = 1;
                    q[tail++] = (State){(short)v, (short)newMask};
                }
            }
        }
        ++steps;
    }
    
    return -1; // unreachable for connected graph
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int ShortestPathLength(int[][] graph) {
        int n = graph.Length;
        int fullMask = (1 << n) - 1;
        bool[,] visited = new bool[n, 1 << n];
        Queue<int> nodeQueue = new Queue<int>();
        Queue<int> maskQueue = new Queue<int>();

        for (int i = 0; i < n; i++) {
            int mask = 1 << i;
            visited[i, mask] = true;
            nodeQueue.Enqueue(i);
            maskQueue.Enqueue(mask);
        }

        int steps = 0;
        while (nodeQueue.Count > 0) {
            int size = nodeQueue.Count;
            for (int s = 0; s < size; s++) {
                int node = nodeQueue.Dequeue();
                int mask = maskQueue.Dequeue();

                if (mask == fullMask) return steps;

                foreach (int nei in graph[node]) {
                    int nextMask = mask | (1 << nei);
                    if (!visited[nei, nextMask]) {
                        visited[nei, nextMask] = true;
                        nodeQueue.Enqueue(nei);
                        maskQueue.Enqueue(nextMask);
                    }
                }
            }
            steps++;
        }

        return -1; // Should never reach here for a connected graph
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} graph
 * @return {number}
 */
var shortestPathLength = function(graph) {
    const n = graph.length;
    const targetMask = (1 << n) - 1;

    // visited[node][mask] == true if state has been seen
    const visited = Array.from({ length: n }, () => new Uint8Array(1 << n));

    const qNode = [];
    const qMask = [];
    let head = 0;

    for (let i = 0; i < n; ++i) {
        const mask = 1 << i;
        visited[i][mask] = 1;
        qNode.push(i);
        qMask.push(mask);
    }

    let steps = 0;
    while (head < qNode.length) {
        const levelSize = qNode.length - head; // nodes in current BFS layer
        for (let i = 0; i < levelSize; ++i) {
            const node = qNode[head];
            const mask = qMask[head];
            head++;

            if (mask === targetMask) return steps;

            for (const nei of graph[node]) {
                const nextMask = mask | (1 << nei);
                if (!visited[nei][nextMask]) {
                    visited[nei][nextMask] = 1;
                    qNode.push(nei);
                    qMask.push(nextMask);
                }
            }
        }
        ++steps;
    }

    return -1; // should never reach here for a connected graph
};
```

## Typescript

```typescript
function shortestPathLength(graph: number[][]): number {
    const n = graph.length;
    const fullMask = (1 << n) - 1;
    const maxMask = 1 << n;

    // distance[node][mask] = steps to reach this state, -1 if unvisited
    const dist: Int32Array[] = Array.from({ length: n }, () => {
        const arr = new Int32Array(maxMask);
        arr.fill(-1);
        return arr;
    });

    const qNode: number[] = [];
    const qMask: number[] = [];
    let head = 0;

    // start BFS from every node
    for (let i = 0; i < n; ++i) {
        const mask = 1 << i;
        dist[i][mask] = 0;
        qNode.push(i);
        qMask.push(mask);
    }

    while (head < qNode.length) {
        const node = qNode[head];
        const mask = qMask[head];
        const d = dist[node][mask];
        if (mask === fullMask) return d;

        for (const nb of graph[node]) {
            const nextMask = mask | (1 << nb);
            if (dist[nb][nextMask] === -1) {
                dist[nb][nextMask] = d + 1;
                qNode.push(nb);
                qMask.push(nextMask);
            }
        }
        ++head;
    }

    return -1; // unreachable in a connected graph
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $graph
     * @return Integer
     */
    function shortestPathLength($graph) {
        $n = count($graph);
        $fullMask = (1 << $n) - 1;

        // visited[node][mask] = true
        $visited = array_fill(0, $n, []);

        $queue = new SplQueue();

        for ($i = 0; $i < $n; $i++) {
            $mask = 1 << $i;
            $queue->enqueue([$i, $mask]);
            $visited[$i][$mask] = true;
        }

        $steps = 0;
        while (!$queue->isEmpty()) {
            $size = $queue->count();
            for ($s = 0; $s < $size; $s++) {
                [$node, $mask] = $queue->dequeue();

                if ($mask === $fullMask) {
                    return $steps;
                }

                foreach ($graph[$node] as $nei) {
                    $nextMask = $mask | (1 << $nei);
                    if (!isset($visited[$nei][$nextMask])) {
                        $visited[$nei][$nextMask] = true;
                        $queue->enqueue([$nei, $nextMask]);
                    }
                }
            }
            $steps++;
        }

        return -1; // Should never reach here for a connected graph
    }
}
```

## Swift

```swift
class Solution {
    func shortestPathLength(_ graph: [[Int]]) -> Int {
        let n = graph.count
        if n == 1 { return 0 }
        let fullMask = (1 << n) - 1
        var visited = Array(repeating: Array(repeating: false, count: 1 << n), count: n)
        var qNode = [Int]()
        var qMask = [Int]()
        var head = 0

        for i in 0..<n {
            let mask = 1 << i
            visited[i][mask] = true
            qNode.append(i)
            qMask.append(mask)
        }

        var steps = 0
        while head < qNode.count {
            let levelSize = qNode.count - head
            for _ in 0..<levelSize {
                let node = qNode[head]
                let mask = qMask[head]
                head += 1

                if mask == fullMask {
                    return steps
                }

                for nei in graph[node] {
                    let nextMask = mask | (1 << nei)
                    if !visited[nei][nextMask] {
                        visited[nei][nextMask] = true
                        qNode.append(nei)
                        qMask.append(nextMask)
                    }
                }
            }
            steps += 1
        }

        return -1
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun shortestPathLength(graph: Array<IntArray>): Int {
        val n = graph.size
        if (n == 1) return 0
        val fullMask = (1 shl n) - 1
        val visited = Array(1 shl n) { BooleanArray(n) }
        val queue: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
        for (i in 0 until n) {
            val mask = 1 shl i
            visited[mask][i] = true
            queue.add(Pair(i, mask))
        }
        var steps = 0
        while (queue.isNotEmpty()) {
            repeat(queue.size) {
                val (node, mask) = queue.removeFirst()
                if (mask == fullMask) return steps
                for (nei in graph[node]) {
                    val nextMask = mask or (1 shl nei)
                    if (!visited[nextMask][nei]) {
                        visited[nextMask][nei] = true
                        queue.add(Pair(nei, nextMask))
                    }
                }
            }
            steps++
        }
        return -1
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int shortestPathLength(List<List<int>> graph) {
    int n = graph.length;
    if (n == 1) return 0;
    int finalMask = (1 << n) - 1;

    List<List<bool>> visited =
        List.generate(n, (_) => List.filled(1 << n, false));

    Queue<int> nodeQueue = Queue<int>();
    Queue<int> maskQueue = Queue<int>();

    for (int i = 0; i < n; i++) {
      int mask = 1 << i;
      visited[i][mask] = true;
      nodeQueue.add(i);
      maskQueue.add(mask);
    }

    int steps = 0;
    while (nodeQueue.isNotEmpty) {
      int size = nodeQueue.length;
      for (int s = 0; s < size; s++) {
        int node = nodeQueue.removeFirst();
        int mask = maskQueue.removeFirst();

        if (mask == finalMask) return steps;

        for (int nei in graph[node]) {
          int nextMask = mask | (1 << nei);
          if (!visited[nei][nextMask]) {
            visited[nei][nextMask] = true;
            nodeQueue.add(nei);
            maskQueue.add(nextMask);
          }
        }
      }
      steps++;
    }

    return -1; // Should never reach here for a connected graph
  }
}
```

## Golang

```go
func shortestPathLength(graph [][]int) int {
	n := len(graph)
	if n == 1 {
		return 0
	}
	finalMask := (1 << n) - 1

	type state struct {
		node int
		mask int
	}

	visited := make([][]bool, n)
	for i := 0; i < n; i++ {
		visited[i] = make([]bool, 1<<n)
	}
	queue := make([]state, 0, n*(1<<n))
	for i := 0; i < n; i++ {
		m := 1 << i
		visited[i][m] = true
		queue = append(queue, state{i, m})
	}

	steps := 0
	for len(queue) > 0 {
		size := len(queue)
		for i := 0; i < size; i++ {
			cur := queue[0]
			queue = queue[1:]
			if cur.mask == finalMask {
				return steps
			}
			for _, nb := range graph[cur.node] {
				nextMask := cur.mask | (1 << nb)
				if !visited[nb][nextMask] {
					visited[nb][nextMask] = true
					queue = append(queue, state{nb, nextMask})
				}
			}
		}
		steps++
	}
	return -1
}
```

## Ruby

```ruby
def shortest_path_length(graph)
  n = graph.size
  full_mask = (1 << n) - 1
  max_state = 1 << n
  visited = Array.new(n) { Array.new(max_state, false) }
  queue = []
  n.times do |i|
    mask = 1 << i
    visited[i][mask] = true
    queue << [i, mask]
  end
  steps = 0
  until queue.empty?
    next_queue = []
    queue.each do |node, mask|
      return steps if mask == full_mask
      graph[node].each do |nbr|
        new_mask = mask | (1 << nbr)
        unless visited[nbr][new_mask]
          visited[nbr][new_mask] = true
          next_queue << [nbr, new_mask]
        end
      end
    end
    queue = next_queue
    steps += 1
  end
  steps
end
```

## Scala

```scala
object Solution {
    def shortestPathLength(graph: Array[Array[Int]]): Int = {
        val n = graph.length
        if (n == 1) return 0
        val fullMask = (1 << n) - 1
        val visited = Array.ofDim[Boolean](n, 1 << n)
        val qNode = new java.util.ArrayDeque[Int]()
        val qMask = new java.util.ArrayDeque[Int]()

        for (i <- 0 until n) {
            val mask = 1 << i
            visited(i)(mask) = true
            qNode.add(i)
            qMask.add(mask)
        }

        var steps = 0
        while (!qNode.isEmpty) {
            val size = qNode.size()
            for (_ <- 0 until size) {
                val node = qNode.poll()
                val mask = qMask.poll()
                if (mask == fullMask) return steps
                for (nei <- graph(node)) {
                    val nextMask = mask | (1 << nei)
                    if (!visited(nei)(nextMask)) {
                        visited(nei)(nextMask) = true
                        qNode.add(nei)
                        qMask.add(nextMask)
                    }
                }
            }
            steps += 1
        }
        -1 // unreachable for connected graph
    }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn shortest_path_length(graph: Vec<Vec<i32>>) -> i32 {
        let n = graph.len();
        if n == 1 {
            return 0;
        }
        let full_mask: usize = (1usize << n) - 1;
        let mut visited = vec![vec![false; 1usize << n]; n];
        let mut queue: VecDeque<(usize, usize, i32)> = VecDeque::new();

        for i in 0..n {
            let mask = 1usize << i;
            visited[i][mask] = true;
            queue.push_back((i, mask, 0));
        }

        while let Some((node, mask, dist)) = queue.pop_front() {
            if mask == full_mask {
                return dist;
            }
            for &nei_i32 in &graph[node] {
                let nei = nei_i32 as usize;
                let next_mask = mask | (1usize << nei);
                if !visited[nei][next_mask] {
                    visited[nei][next_mask] = true;
                    queue.push_back((nei, next_mask, dist + 1));
                }
            }
        }

        0
    }
}
```

## Racket

```racket
(define/contract (shortest-path-length graph)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length graph))
         (fullMask (sub1 (arithmetic-shift 1 n)))
         (visited (make-vector n))
         (max-states (* n (expt 2 n)))
         (queue (make-vector max-states)))
    ;; initialize visited masks
    (for ([i (in-range n)])
      (vector-set! visited i (make-vector (+ fullMask 1) #f)))
    (define front 0)
    (define back 0)
    ;; enqueue all starting nodes
    (for ([i (in-range n)])
      (let ((mask (arithmetic-shift 1 i))
            (inner (vector-ref visited i)))
        (vector-set! inner mask #t)
        (vector-set! queue back (list i mask 0))
        (set! back (+ back 1))))
    ;; BFS
    (let loop ()
      (if (= front back)
          -1 ; should never happen for a connected graph
          (let* ((state (vector-ref queue front))
                 (node (first state))
                 (mask (second state))
                 (dist (third state)))
            (set! front (+ front 1))
            (if (= mask fullMask)
                dist
                (begin
                  (for ([nbr (in-list (list-ref graph node))])
                    (let ((nextMask (bitwise-ior mask (arithmetic-shift 1 nbr))))
                      (let ((inner (vector-ref visited nbr)))
                        (unless (vector-ref inner nextMask)
                          (vector-set! inner nextMask #t)
                          (vector-set! queue back (list nbr nextMask (+ dist 1)))
                          (set! back (+ back 1))))))
                  (loop))))))))
```

## Erlang

```erlang
-module(solution).
-export([shortest_path_length/1]).

-spec shortest_path_length(Graph :: [[integer()]]) -> integer().
shortest_path_length(Graph) ->
    N = length(Graph),
    FullMask = (1 bsl N) - 1,
    {Queue0, Visited0} = init_queue(N),
    bfs(Queue0, Visited0, Graph, FullMask).

init_queue(N) ->
    Q0 = queue:new(),
    {Q, V} = lists:foldl(
        fun(Node, {QAcc, Vis}) ->
                Mask = 1 bsl Node,
                State = {Node, Mask, 0},
                QNew = queue:in(State, QAcc),
                VisNew = maps:put({Node, Mask}, true, Vis),
                {QNew, VisNew}
        end,
        {Q0, #{}},
        lists:seq(0, N - 1)
    ),
    {Q, V}.

bfs(Queue, Visited, Graph, FullMask) ->
    case queue:out(Queue) of
        {empty, _} -> -1; % should never happen for a connected graph
        {{value, {Node, Mask, Dist}}, RestQueue} ->
            if
                Mask =:= FullMask ->
                    Dist;
                true ->
                    Adj = lists:nth(Node + 1, Graph),
                    {NewQueue, NewVisited} = process_neighbors(Adj, Node, Mask, Dist, RestQueue, Visited),
                    bfs(NewQueue, NewVisited, Graph, FullMask)
            end
    end.

process_neighbors([], _Node, _Mask, _Dist, Queue, Visited) ->
    {Queue, Visited};
process_neighbors([Nei | Rest], _Node, Mask, Dist, Queue, Visited) ->
    NewMask = Mask bor (1 bsl Nei),
    Key = {Nei, NewMask},
    case maps:is_key(Key, Visited) of
        true ->
            process_neighbors(Rest, _Node, Mask, Dist, Queue, Visited);
        false ->
            Visited2 = maps:put(Key, true, Visited),
            Queue2 = queue:in({Nei, NewMask, Dist + 1}, Queue),
            process_neighbors(Rest, _Node, Mask, Dist, Queue2, Visited2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec shortest_path_length(graph :: [[integer]]) :: integer
  def shortest_path_length(graph) do
    n = length(graph)
    full_mask = (1 <<< n) - 1

    q0 = :queue.new()

    {queue, visited} =
      Enum.reduce(0..n-1, {q0, MapSet.new()}, fn node, {q_acc, vis_acc} ->
        mask = 1 <<< node
        new_q = :queue.in({node, mask, 0}, q_acc)
        new_vis = MapSet.put(vis_acc, {node, mask})
        {new_q, new_vis}
      end)

    bfs(queue, graph, full_mask, visited)
  end

  defp bfs(queue, graph, full_mask, visited) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {node, mask, dist}}, q_rest} ->
        if mask == full_mask do
          dist
        else
          {new_queue, new_visited} =
            Enum.reduce(Enum.at(graph, node), {q_rest, visited}, fn nb, {q_acc, vis_acc} ->
              new_mask = mask ||| (1 <<< nb)
              key = {nb, new_mask}

              if MapSet.member?(vis_acc, key) do
                {q_acc, vis_acc}
              else
                {
                  :queue.in({nb, new_mask, dist + 1}, q_acc),
                  MapSet.put(vis_acc, key)
                }
              end
            end)

          bfs(new_queue, graph, full_mask, new_visited)
        end
    end
  end
end
```

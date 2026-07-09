# 0207. Course Schedule

## Cpp

```cpp
#include <vector>
#include <queue>

class Solution {
public:
    bool canFinish(int numCourses, std::vector<std::vector<int>>& prerequisites) {
        std::vector<std::vector<int>> adj(numCourses);
        std::vector<int> indeg(numCourses, 0);
        for (const auto& pre : prerequisites) {
            int a = pre[0], b = pre[1];
            adj[b].push_back(a);
            ++indeg[a];
        }
        std::queue<int> q;
        for (int i = 0; i < numCourses; ++i)
            if (indeg[i] == 0) q.push(i);
        int visited = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            ++visited;
            for (int v : adj[u]) {
                if (--indeg[v] == 0) q.push(v);
            }
        }
        return visited == numCourses;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = new ArrayList[numCourses];
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] pre : prerequisites) {
            // to take course pre[0], you need to finish pre[1] first
            graph[pre[1]].add(pre[0]);
        }

        int[] state = new int[numCourses]; // 0 = unvisited, 1 = visiting, 2 = visited

        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i, graph, state)) {
                return false;
            }
        }
        return true;
    }

    private boolean dfs(int node, List<Integer>[] graph, int[] state) {
        if (state[node] == 1) { // cycle detected
            return false;
        }
        if (state[node] == 2) { // already processed
            return true;
        }
        state[node] = 1; // mark as visiting
        for (int neighbor : graph[node]) {
            if (!dfs(neighbor, graph, state)) {
                return false;
            }
        }
        state[node] = 2; // mark as visited
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            graph[src].append(dest)

        visit = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited

        def dfs(node):
            if visit[node] == 1:   # cycle detected
                return False
            if visit[node] == 2:   # already processed
                return True
            visit[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visit[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited

        def has_cycle(v: int) -> bool:
            if state[v] == 1:
                return True
            if state[v] == 2:
                return False
            state[v] = 1
            for nei in graph[v]:
                if has_cycle(nei):
                    return True
            state[v] = 2
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False
        return True
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

bool canFinish(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize) {
    if (numCourses <= 0) return true;
    
    // indegree array
    int *indegree = calloc(numCourses, sizeof(int));
    if (!indegree) return false; // allocation failure
    
    // adjacency list structures
    int **adj = calloc(numCourses, sizeof(int*));
    int *adjSize = calloc(numCourses, sizeof(int));
    int *adjCap  = calloc(numCourses, sizeof(int));
    if (!adj || !adjSize || !adjCap) {
        free(indegree);
        free(adj);
        free(adjSize);
        free(adjCap);
        return false;
    }
    
    // build graph
    for (int i = 0; i < prerequisitesSize; ++i) {
        int a = prerequisites[i][0];
        int b = prerequisites[i][1];
        indegree[a]++;               // edge b -> a
        
        if (adjSize[b] == adjCap[b]) {
            int newCap = adjCap[b] ? adjCap[b] * 2 : 4;
            int *newArr = realloc(adj[b], newCap * sizeof(int));
            if (!newArr) {
                // cleanup
                free(indegree);
                for (int j = 0; j < numCourses; ++j) free(adj[j]);
                free(adj);
                free(adjSize);
                free(adjCap);
                return false;
            }
            adj[b] = newArr;
            adjCap[b] = newCap;
        }
        adj[b][adjSize[b]++] = a;
    }
    
    // queue for Kahn's algorithm
    int *queue = malloc(numCourses * sizeof(int));
    if (!queue) {
        free(indegree);
        for (int j = 0; j < numCourses; ++j) free(adj[j]);
        free(adj);
        free(adjSize);
        free(adjCap);
        return false;
    }
    
    int front = 0, rear = 0, processed = 0;
    for (int i = 0; i < numCourses; ++i) {
        if (indegree[i] == 0) {
            queue[rear++] = i;
        }
    }
    
    while (front < rear) {
        int node = queue[front++];
        processed++;
        for (int k = 0; k < adjSize[node]; ++k) {
            int nb = adj[node][k];
            indegree[nb]--;
            if (indegree[nb] == 0) {
                queue[rear++] = nb;
            }
        }
    }
    
    // cleanup
    free(indegree);
    for (int i = 0; i < numCourses; ++i) free(adj[i]);
    free(adj);
    free(adjSize);
    free(adjCap);
    free(queue);
    
    return processed == numCourses;
}
```

## Csharp

```csharp
public class Solution {
    public bool CanFinish(int numCourses, int[][] prerequisites) {
        var adj = new List<int>[numCourses];
        for (int i = 0; i < numCourses; i++) adj[i] = new List<int>();
        int[] indegree = new int[numCourses];

        foreach (var pre in prerequisites) {
            int a = pre[0], b = pre[1];
            adj[b].Add(a);
            indegree[a]++;
        }

        var queue = new Queue<int>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) queue.Enqueue(i);
        }

        int visited = 0;
        while (queue.Count > 0) {
            int cur = queue.Dequeue();
            visited++;
            foreach (int next in adj[cur]) {
                indegree[next]--;
                if (indegree[next] == 0) queue.Enqueue(next);
            }
        }

        return visited == numCourses;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    const adj = Array.from({ length: numCourses }, () => []);
    const indeg = new Array(numCourses).fill(0);
    
    for (const [a, b] of prerequisites) {
        adj[b].push(a);
        indeg[a]++;
    }
    
    const queue = [];
    for (let i = 0; i < numCourses; i++) {
        if (indeg[i] === 0) queue.push(i);
    }
    
    let visited = 0;
    for (let q = 0; q < queue.length; q++) {
        const node = queue[q];
        visited++;
        for (const nei of adj[node]) {
            indeg[nei]--;
            if (indeg[nei] === 0) queue.push(nei);
        }
    }
    
    return visited === numCourses;
};
```

## Typescript

```typescript
function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    const adj: number[][] = Array.from({ length: numCourses }, () => []);
    const indeg: number[] = new Array(numCourses).fill(0);
    
    for (const [next, prev] of prerequisites) {
        adj[prev].push(next);
        indeg[next]++;
    }
    
    const queue: number[] = [];
    for (let i = 0; i < numCourses; i++) {
        if (indeg[i] === 0) queue.push(i);
    }
    
    let processed = 0;
    let head = 0;
    while (head < queue.length) {
        const node = queue[head++];
        processed++;
        for (const neighbor of adj[node]) {
            indeg[neighbor]--;
            if (indeg[neighbor] === 0) queue.push(neighbor);
        }
    }
    
    return processed === numCourses;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $numCourses
     * @param Integer[][] $prerequisites
     * @return Boolean
     */
    function canFinish($numCourses, $prerequisites) {
        $graph = array_fill(0, $numCourses, []);
        $indeg = array_fill(0, $numCourses, 0);
        foreach ($prerequisites as $pair) {
            $a = $pair[0];
            $b = $pair[1];
            $graph[$b][] = $a;
            $indeg[$a]++;
        }
        $queue = new SplQueue();
        for ($i = 0; $i < $numCourses; $i++) {
            if ($indeg[$i] === 0) {
                $queue->enqueue($i);
            }
        }
        $visited = 0;
        while (!$queue->isEmpty()) {
            $node = $queue->dequeue();
            $visited++;
            foreach ($graph[$node] as $next) {
                $indeg[$next]--;
                if ($indeg[$next] === 0) {
                    $queue->enqueue($next);
                }
            }
        }
        return $visited === $numCourses;
    }
}
```

## Swift

```swift
class Solution {
    func canFinish(_ numCourses: Int, _ prerequisites: [[Int]]) -> Bool {
        var indegree = [Int](repeating: 0, count: numCourses)
        var graph = [[Int]](repeating: [], count: numCourses)
        for pre in prerequisites {
            let course = pre[0]
            let prereq = pre[1]
            graph[prereq].append(course)
            indegree[course] += 1
        }
        var queue = [Int]()
        queue.reserveCapacity(numCourses)
        for i in 0..<numCourses where indegree[i] == 0 {
            queue.append(i)
        }
        var processed = 0
        var idx = 0
        while idx < queue.count {
            let node = queue[idx]
            idx += 1
            processed += 1
            for next in graph[node] {
                indegree[next] -= 1
                if indegree[next] == 0 {
                    queue.append(next)
                }
            }
        }
        return processed == numCourses
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canFinish(numCourses: Int, prerequisites: Array<IntArray>): Boolean {
        val graph = Array(numCourses) { mutableListOf<Int>() }
        for (pre in prerequisites) {
            // pre[0] depends on pre[1]
            graph[pre[1]].add(pre[0])
        }
        val state = IntArray(numCourses) // 0 = unvisited, 1 = visiting, 2 = visited

        fun dfs(v: Int): Boolean {
            if (state[v] == 1) return false   // cycle detected
            if (state[v] == 2) return true    // already processed
            state[v] = 1
            for (next in graph[v]) {
                if (!dfs(next)) return false
            }
            state[v] = 2
            return true
        }

        for (i in 0 until numCourses) {
            if (!dfs(i)) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool canFinish(int numCourses, List<List<int>> prerequisites) {
    // Build adjacency list: edge from prerequisite to course
    final graph = List.generate(numCourses, (_) => <int>[]);
    for (var pair in prerequisites) {
      int course = pair[0];
      int pre = pair[1];
      graph[pre].add(course);
    }

    // 0 = unvisited, 1 = visiting, 2 = visited
    final state = List.filled(numCourses, 0);

    bool dfs(int node) {
      if (state[node] == 1) return false; // cycle detected
      if (state[node] == 2) return true;  // already processed

      state[node] = 1;
      for (int neighbor in graph[node]) {
        if (!dfs(neighbor)) return false;
      }
      state[node] = 2;
      return true;
    }

    for (int i = 0; i < numCourses; i++) {
      if (state[i] == 0 && !dfs(i)) return false;
    }
    return true;
  }
}
```

## Golang

```go
func canFinish(numCourses int, prerequisites [][]int) bool {
	indeg := make([]int, numCourses)
	graph := make([][]int, numCourses)

	for _, p := range prerequisites {
		to, from := p[0], p[1]
		graph[from] = append(graph[from], to)
		indeg[to]++
	}

	queue := make([]int, 0, numCourses)
	for i := 0; i < numCourses; i++ {
		if indeg[i] == 0 {
			queue = append(queue, i)
		}
	}

	visited := 0
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		visited++
		for _, nxt := range graph[cur] {
			indeg[nxt]--
			if indeg[nxt] == 0 {
				queue = append(queue, nxt)
			}
		}
	}

	return visited == numCourses
}
```

## Ruby

```ruby
def can_finish(num_courses, prerequisites)
  adj = Array.new(num_courses) { [] }
  indeg = Array.new(num_courses, 0)

  prerequisites.each do |pair|
    a, b = pair
    adj[b] << a
    indeg[a] += 1
  end

  queue = []
  num_courses.times { |i| queue << i if indeg[i].zero? }

  visited = 0
  front = 0
  while front < queue.length
    node = queue[front]
    front += 1
    visited += 1
    adj[node].each do |nbr|
      indeg[nbr] -= 1
      queue << nbr if indeg[nbr].zero?
    end
  end

  visited == num_courses
end
```

## Scala

```scala
object Solution {
    def canFinish(numCourses: Int, prerequisites: Array[Array[Int]]): Boolean = {
        val adj = Array.fill(numCourses)(new scala.collection.mutable.ArrayBuffer[Int]())
        val indegree = new Array[Int](numCourses)
        for (p <- prerequisites) {
            val a = p(0)
            val b = p(1)
            adj(b) += a
            indegree(a) += 1
        }
        val queue = new java.util.ArrayDeque[Int]()
        var i = 0
        while (i < numCourses) {
            if (indegree(i) == 0) queue.add(i)
            i += 1
        }
        var visited = 0
        while (!queue.isEmpty) {
            val cur = queue.poll()
            visited += 1
            for (next <- adj(cur)) {
                indegree(next) -= 1
                if (indegree(next) == 0) queue.add(next)
            }
        }
        visited == numCourses
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        use std::collections::VecDeque;
        let n = num_courses as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        let mut indeg: Vec<usize> = vec![0; n];

        for pre in prerequisites.iter() {
            // each pre has exactly two elements [a, b]
            let a = pre[0] as usize;
            let b = pre[1] as usize;
            adj[b].push(a);
            indeg[a] += 1;
        }

        let mut queue: VecDeque<usize> = VecDeque::new();
        for i in 0..n {
            if indeg[i] == 0 {
                queue.push_back(i);
            }
        }

        let mut visited = 0usize;
        while let Some(u) = queue.pop_front() {
            visited += 1;
            for &v in adj[u].iter() {
                indeg[v] -= 1;
                if indeg[v] == 0 {
                    queue.push_back(v);
                }
            }
        }

        visited == n
    }
}
```

## Racket

```racket
(define/contract (can-finish numCourses prerequisites)
  (-> exact-integer? (listof (listof exact-integer?)) boolean?)
  (let* ([adj   (make-vector numCourses '())]
         [indeg (make-vector numCourses 0)])
    ;; build adjacency list and indegree counts
    (for-each (lambda (pair)
                (let ([a (list-ref pair 0)]
                      [b (list-ref pair 1)])
                  (vector-set! adj b (cons a (vector-ref adj b)))
                  (vector-set! indeg a (+ 1 (vector-ref indeg a)))))
              prerequisites)
    ;; initial queue: courses with zero indegree
    (define init-queue
      (filter (lambda (i) (= (vector-ref indeg i) 0))
              (build-list numCourses (lambda (i) i))))
    ;; process nodes in topological order
    (letrec ((process (lambda (queue cnt)
                        (if (null? queue)
                            (= cnt numCourses)
                            (let* ([node (car queue)]
                                   [rest (cdr queue)])
                              (let loop-nei ((neighbors (vector-ref adj node))
                                             (new-queue rest))
                                (if (null? neighbors)
                                    (process new-queue (+ cnt 1))
                                    (let* ([nbr (car neighbors)]
                                           [deg (- (vector-ref indeg nbr) 1)])
                                      (vector-set! indeg nbr deg)
                                      (loop-nei (cdr neighbors)
                                                (if (= deg 0)
                                                    (cons nbr new-queue)
                                                    new-queue))))))))))
      (process init-queue 0))))
```

## Erlang

```erlang
-module(solution).
-export([can_finish/2]).

-spec can_finish(NumCourses :: integer(), Prerequisites :: [[integer()]]) -> boolean().
can_finish(NumCourses, Prerequisites) ->
    Indeg0 = maps:from_list([{C, 0} || C <- lists:seq(0, NumCourses - 1)]),
    Adj0   = #{},
    {Adj, Indeg} = build_graph(Prerequisites, Adj0, Indeg0),
    Queue0 = [C || C <- lists:seq(0, NumCourses - 1), maps:get(C, Indeg) == 0],
    Visited = bfs(Queue0, Adj, Indeg, 0),
    Visited == NumCourses.

%% Build adjacency list and indegree map
build_graph([], Adj, Indeg) ->
    {Adj, Indeg};
build_graph([[A, B] | Rest], AdjAcc, IndegAcc) ->
    % update adjacency: edge B -> A
    AdjNew = case maps:is_key(B, AdjAcc) of
        true  -> maps:update_with(B, fun(L) -> [A | L] end, [], AdjAcc);
        false -> maps:put(B, [A], AdjAcc)
    end,
    % increment indegree of A
    IndPrev = maps:get(A, IndegAcc),
    IndegNew = maps:put(A, IndPrev + 1, IndegAcc),
    build_graph(Rest, AdjNew, IndegNew).

%% BFS (Kahn's algorithm) processing queue
bfs([], _Adj, _Indeg, Visited) ->
    Visited;
bfs([Node | RestQueue], Adj, Indeg, Visited) ->
    Neighbors = maps:get(Node, Adj, []),
    {Indeg2, NewZeros} = decrement_neighbors(Neighbors, Indeg, []),
    bfs(RestQueue ++ lists:reverse(NewZeros), Adj, Indeg2, Visited + 1).

%% Decrement indegree of neighbors and collect newly zero-indegree nodes
decrement_neighbors([], Indeg, Zeros) ->
    {Indeg, Zeros};
decrement_neighbors([N | Ns], IndegAcc, ZerosAcc) ->
    Curr = maps:get(N, IndegAcc),
    NewVal = Curr - 1,
    IndegUpdated = maps:put(N, NewVal, IndegAcc),
    ZerosUpdated = if NewVal == 0 -> [N | ZerosAcc]; true -> ZerosAcc end,
    decrement_neighbors(Ns, IndegUpdated, ZerosUpdated).
```

## Elixir

```elixir
defmodule Solution do
  @spec can_finish(num_courses :: integer, prerequisites :: [[integer]]) :: boolean
  def can_finish(num_courses, prerequisites) do
    {graph, indeg} =
      Enum.reduce(prerequisites, {%{}, %{}}, fn [a, b], {g, ind} ->
        g = Map.update(g, b, [a], &[a | &1])
        ind = Map.update(ind, a, 1, &(&1 + 1))
        {g, ind}
      end)

    indeg =
      Enum.reduce(0..num_courses - 1, indeg, fn i, acc ->
        Map.put_new(acc, i, 0)
      end)

    zero_nodes = Enum.filter(0..num_courses - 1, fn i -> Map.get(indeg, i) == 0 end)
    queue = :queue.from_list(zero_nodes)

    processed = bfs(queue, graph, indeg, 0)
    processed == num_courses
  end

  defp bfs(queue, graph, indeg, count) do
    case :queue.out(queue) do
      {:empty, _} ->
        count

      {{:value, node}, q2} ->
        neighbors = Map.get(graph, node, [])

        {new_indeg, new_queue} =
          Enum.reduce(neighbors, {indeg, q2}, fn nb, {ig, qacc} ->
            deg = Map.get(ig, nb) - 1
            ig = Map.put(ig, nb, deg)

            if deg == 0 do
              {ig, :queue.in(nb, qacc)}
            else
              {ig, qacc}
            end
          end)

        bfs(new_queue, graph, new_indeg, count + 1)
    end
  end
end
```

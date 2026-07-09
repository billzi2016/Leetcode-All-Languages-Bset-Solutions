# 0210. Course Schedule II

## Cpp

```cpp
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> indeg(numCourses, 0);
        for (const auto& pre : prerequisites) {
            int a = pre[0], b = pre[1];
            adj[b].push_back(a);
            ++indeg[a];
        }
        queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (indeg[i] == 0) q.push(i);
        }
        vector<int> order;
        order.reserve(numCourses);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            order.push_back(u);
            for (int v : adj[u]) {
                if (--indeg[v] == 0) q.push(v);
            }
        }
        if ((int)order.size() != numCourses) return {};
        return order;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = new ArrayList[numCourses];
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new ArrayList<>();
        }
        int[] indegree = new int[numCourses];
        for (int[] pre : prerequisites) {
            int a = pre[0], b = pre[1];
            graph[b].add(a);
            indegree[a]++;
        }

        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        int[] order = new int[numCourses];
        int idx = 0;
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            order[idx++] = cur;
            for (int next : graph[cur]) {
                indegree[next]--;
                if (indegree[next] == 0) {
                    queue.offer(next);
                }
            }
        }

        return idx == numCourses ? order : new int[0];
    }
}
```

## Python

```python
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for dest, src in prerequisites:
            adj[src].append(dest)
            indeg[dest] += 1

        from collections import deque
        queue = deque([i for i in range(numCourses) if indeg[i] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    queue.append(nei)

        return order if len(order) == numCourses else []
```

## Python3

```python
from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for dest, src in prerequisites:
            adj[src].append(dest)
            indeg[dest] += 1

        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        order = []

        while q:
            node = q.popleft()
            order.append(node)
            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        return order if len(order) == numCourses else []
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findOrder(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize, int* returnSize) {
    (void)prerequisitesColSize; // unused
    
    if (numCourses <= 0) {
        *returnSize = 0;
        return NULL;
    }
    
    int *indeg = calloc(numCourses, sizeof(int));
    int *outCnt = calloc(numCourses, sizeof(int));
    if (!indeg || !outCnt) {
        free(indeg);
        free(outCnt);
        *returnSize = 0;
        return NULL;
    }
    
    // First pass: count indegrees and outgoing edges
    for (int i = 0; i < prerequisitesSize; ++i) {
        int a = prerequisites[i][0];
        int b = prerequisites[i][1];
        indeg[a]++;
        outCnt[b]++;
    }
    
    // Build adjacency list
    int **adj = malloc(numCourses * sizeof(int*));
    if (!adj) {
        free(indeg);
        free(outCnt);
        *returnSize = 0;
        return NULL;
    }
    for (int i = 0; i < numCourses; ++i) {
        adj[i] = outCnt[i] ? malloc(outCnt[i] * sizeof(int)) : NULL;
    }
    
    // Temporary counters to fill adjacency
    int *fillPos = calloc(numCourses, sizeof(int));
    if (!fillPos) {
        for (int i = 0; i < numCourses; ++i) free(adj[i]);
        free(adj);
        free(indeg);
        free(outCnt);
        *returnSize = 0;
        return NULL;
    }
    
    // Second pass: populate adjacency list
    for (int i = 0; i < prerequisitesSize; ++i) {
        int a = prerequisites[i][0];
        int b = prerequisites[i][1];
        adj[b][fillPos[b]++] = a;
    }
    
    // Queue for Kahn's algorithm
    int *queue = malloc(numCourses * sizeof(int));
    if (!queue) {
        free(fillPos);
        for (int i = 0; i < numCourses; ++i) free(adj[i]);
        free(adj);
        free(indeg);
        free(outCnt);
        *returnSize = 0;
        return NULL;
    }
    
    int qh = 0, qt = 0;
    for (int i = 0; i < numCourses; ++i) {
        if (indeg[i] == 0) queue[qt++] = i;
    }
    
    int *order = malloc(numCourses * sizeof(int));
    if (!order) {
        free(queue);
        free(fillPos);
        for (int i = 0; i < numCourses; ++i) free(adj[i]);
        free(adj);
        free(indeg);
        free(outCnt);
        *returnSize = 0;
        return NULL;
    }
    
    int idx = 0;
    while (qh < qt) {
        int u = queue[qh++];
        order[idx++] = u;
        for (int j = 0; j < outCnt[u]; ++j) {
            int v = adj[u][j];
            if (--indeg[v] == 0) {
                queue[qt++] = v;
            }
        }
    }
    
    // Cleanup
    free(queue);
    free(fillPos);
    for (int i = 0; i < numCourses; ++i) free(adj[i]);
    free(adj);
    free(indeg);
    free(outCnt);
    
    if (idx == numCourses) {
        *returnSize = idx;
        return order;
    } else {
        free(order);
        *returnSize = 0;
        return NULL;
    }
}
```

## Csharp

```csharp
public class Solution {
    public int[] FindOrder(int numCourses, int[][] prerequisites) {
        var graph = new List<int>[numCourses];
        for (int i = 0; i < numCourses; i++) graph[i] = new List<int>();
        var indegree = new int[numCourses];

        foreach (var pre in prerequisites) {
            int a = pre[0], b = pre[1];
            graph[b].Add(a);
            indegree[a]++;
        }

        var queue = new Queue<int>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) queue.Enqueue(i);
        }

        var order = new List<int>(numCourses);
        while (queue.Count > 0) {
            int cur = queue.Dequeue();
            order.Add(cur);
            foreach (var nxt in graph[cur]) {
                indegree[nxt]--;
                if (indegree[nxt] == 0) queue.Enqueue(nxt);
            }
        }

        return order.Count == numCourses ? order.ToArray() : new int[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
    const graph = Array.from({ length: numCourses }, () => []);
    const indegree = new Array(numCourses).fill(0);
    
    for (const [next, prev] of prerequisites) {
        graph[prev].push(next);
        indegree[next]++;
    }
    
    const queue = [];
    for (let i = 0; i < numCourses; i++) {
        if (indegree[i] === 0) queue.push(i);
    }
    
    const order = [];
    let qIdx = 0;
    while (qIdx < queue.length) {
        const node = queue[qIdx++];
        order.push(node);
        for (const neighbor of graph[node]) {
            indegree[neighbor]--;
            if (indegree[neighbor] === 0) queue.push(neighbor);
        }
    }
    
    return order.length === numCourses ? order : [];
};
```

## Typescript

```typescript
function findOrder(numCourses: number, prerequisites: number[][]): number[] {
    const adj: number[][] = Array.from({ length: numCourses }, () => []);
    const indegree: number[] = new Array(numCourses).fill(0);
    
    for (const [next, prev] of prerequisites) {
        adj[prev].push(next);
        indegree[next]++;
    }
    
    const queue: number[] = [];
    for (let i = 0; i < numCourses; i++) {
        if (indegree[i] === 0) queue.push(i);
    }
    
    const order: number[] = [];
    let idx = 0;
    while (idx < queue.length) {
        const course = queue[idx++];
        order.push(course);
        for (const neighbor of adj[course]) {
            indegree[neighbor]--;
            if (indegree[neighbor] === 0) queue.push(neighbor);
        }
    }
    
    return order.length === numCourses ? order : [];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $numCourses
     * @param Integer[][] $prerequisites
     * @return Integer[]
     */
    function findOrder($numCourses, $prerequisites) {
        // Build graph and indegree array
        $graph = array_fill(0, $numCourses, []);
        $indeg = array_fill(0, $numCourses, 0);
        foreach ($prerequisites as $pair) {
            $dest = $pair[0];
            $src  = $pair[1];
            $graph[$src][] = $dest;
            $indeg[$dest]++;
        }

        // Initialize queue with nodes having zero indegree
        $queue = new SplQueue();
        for ($i = 0; $i < $numCourses; $i++) {
            if ($indeg[$i] === 0) {
                $queue->enqueue($i);
            }
        }

        $order = [];
        while (!$queue->isEmpty()) {
            $node = $queue->dequeue();
            $order[] = $node;
            foreach ($graph[$node] as $neighbor) {
                $indeg[$neighbor]--;
                if ($indeg[$neighbor] === 0) {
                    $queue->enqueue($neighbor);
                }
            }
        }

        return count($order) === $numCourses ? $order : [];
    }
}
```

## Swift

```swift
class Solution {
    func findOrder(_ numCourses: Int, _ prerequisites: [[Int]]) -> [Int] {
        var adj = Array(repeating: [Int](), count: numCourses)
        var indegree = Array(repeating: 0, count: numCourses)
        
        for pre in prerequisites {
            let a = pre[0]
            let b = pre[1]
            adj[b].append(a)
            indegree[a] += 1
        }
        
        var queue = [Int]()
        for i in 0..<numCourses where indegree[i] == 0 {
            queue.append(i)
        }
        
        var index = 0
        var order = [Int]()
        while index < queue.count {
            let node = queue[index]
            index += 1
            order.append(node)
            for neighbor in adj[node] {
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0 {
                    queue.append(neighbor)
                }
            }
        }
        
        return order.count == numCourses ? order : []
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findOrder(numCourses: Int, prerequisites: Array<IntArray>): IntArray {
        val adj = Array(numCourses) { mutableListOf<Int>() }
        val indegree = IntArray(numCourses)
        for (pre in prerequisites) {
            val a = pre[0]
            val b = pre[1]
            adj[b].add(a)
            indegree[a]++
        }
        val queue: ArrayDeque<Int> = ArrayDeque()
        for (i in 0 until numCourses) {
            if (indegree[i] == 0) queue.add(i)
        }
        val order = IntArray(numCourses)
        var idx = 0
        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            order[idx++] = cur
            for (next in adj[cur]) {
                indegree[next]--
                if (indegree[next] == 0) queue.add(next)
            }
        }
        return if (idx == numCourses) order else IntArray(0)
    }
}
```

## Dart

```dart
class Solution {
  List<int> findOrder(int numCourses, List<List<int>> prerequisites) {
    var graph = List.generate(numCourses, (_) => <int>[]);
    var indegree = List.filled(numCourses, 0);
    for (var pre in prerequisites) {
      int a = pre[0];
      int b = pre[1];
      graph[b].add(a);
      indegree[a]++;
    }
    var queue = <int>[];
    for (int i = 0; i < numCourses; i++) {
      if (indegree[i] == 0) queue.add(i);
    }
    var order = <int>[];
    int idx = 0;
    while (idx < queue.length) {
      int node = queue[idx++];
      order.add(node);
      for (int nei in graph[node]) {
        indegree[nei]--;
        if (indegree[nei] == 0) queue.add(nei);
      }
    }
    return order.length == numCourses ? order : <int>[];
  }
}
```

## Golang

```go
func findOrder(numCourses int, prerequisites [][]int) []int {
    graph := make([][]int, numCourses)
    indegree := make([]int, numCourses)

    for _, pre := range prerequisites {
        a, b := pre[0], pre[1]
        graph[b] = append(graph[b], a)
        indegree[a]++
    }

    queue := make([]int, 0, numCourses)
    for i := 0; i < numCourses; i++ {
        if indegree[i] == 0 {
            queue = append(queue, i)
        }
    }

    order := make([]int, 0, numCourses)

    for len(queue) > 0 {
        v := queue[0]
        queue = queue[1:]
        order = append(order, v)
        for _, nb := range graph[v] {
            indegree[nb]--
            if indegree[nb] == 0 {
                queue = append(queue, nb)
            }
        }
    }

    if len(order) != numCourses {
        return []int{}
    }
    return order
}
```

## Ruby

```ruby
def find_order(num_courses, prerequisites)
  adj = Array.new(num_courses) { [] }
  indegree = Array.new(num_courses, 0)

  prerequisites.each do |dest, src|
    adj[src] << dest
    indegree[dest] += 1
  end

  queue = []
  num_courses.times { |i| queue << i if indegree[i].zero? }

  order = []
  head = 0
  while head < queue.length
    u = queue[head]
    head += 1
    order << u
    adj[u].each do |v|
      indegree[v] -= 1
      queue << v if indegree[v].zero?
    end
  end

  order.size == num_courses ? order : []
end
```

## Scala

```scala
object Solution {
    def findOrder(numCourses: Int, prerequisites: Array[Array[Int]]): Array[Int] = {
        val adj = Array.fill(numCourses)(new scala.collection.mutable.ListBuffer[Int]())
        val indeg = new Array[Int](numCourses)
        for (p <- prerequisites) {
            val a = p(0)
            val b = p(1)
            adj(b) += a
            indeg(a) += 1
        }
        val queue = new scala.collection.mutable.Queue[Int]()
        for (i <- 0 until numCourses if indeg(i) == 0) {
            queue.enqueue(i)
        }
        val order = new scala.collection.mutable.ArrayBuffer[Int](numCourses)
        while (queue.nonEmpty) {
            val cur = queue.dequeue()
            order += cur
            for (next <- adj(cur)) {
                indeg(next) -= 1
                if (indeg(next) == 0) queue.enqueue(next)
            }
        }
        if (order.length == numCourses) order.toArray else Array.empty[Int]
    }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
        let n = num_courses as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        let mut indeg: Vec<usize> = vec![0; n];

        for pre in prerequisites.iter() {
            let a = pre[0] as usize;
            let b = pre[1] as usize;
            adj[b].push(a);
            indeg[a] += 1;
        }

        let mut queue = VecDeque::new();
        for i in 0..n {
            if indeg[i] == 0 {
                queue.push_back(i);
            }
        }

        let mut order: Vec<i32> = Vec::with_capacity(n);
        while let Some(u) = queue.pop_front() {
            order.push(u as i32);
            for &v in adj[u].iter() {
                indeg[v] -= 1;
                if indeg[v] == 0 {
                    queue.push_back(v);
                }
            }
        }

        if order.len() == n { order } else { Vec::new() }
    }
}
```

## Racket

```racket
(define/contract (find-order numCourses prerequisites)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([adj   (make-vector numCourses '())]
         [indeg (make-vector numCourses 0)])
    ;; build adjacency list and indegree counts
    (for ([pair prerequisites])
      (let ([a (first pair)]
            [b (second pair)])
        (vector-set! adj b (cons a (vector-ref adj b)))
        (vector-set! indeg a (+ 1 (vector-ref indeg a)))))
    ;; initialize queue with nodes of zero indegree
    (define q '())
    (for ([i (in-range numCourses)])
      (when (= (vector-ref indeg i) 0)
        (set! q (cons i q))))
    (define order (make-vector numCourses 0))
    (define idx (box 0))
    (let loop ()
      (if (null? q)
          (let ([cnt (unbox idx)])
            (if (= cnt numCourses)
                (vector->list order)
                '()))
          (begin
            (define node (car q))
            (set! q (cdr q))
            (vector-set! order (unbox idx) node)
            (set-box! idx (+ 1 (unbox idx)))
            ;; decrease indegree of neighbors
            (for ([nbr (vector-ref adj node)])
              (let ([newdeg (- (vector-ref indeg nbr) 1)])
                (vector-set! indeg nbr newdeg)
                (when (= newdeg 0)
                  (set! q (cons nbr q)))))
            (loop))))))
```

## Erlang

```erlang
-module(solution).
-export([find_order/2]).

-spec find_order(NumCourses :: integer(), Prerequisites :: [[integer()]]) -> [integer()].
find_order(NumCourses, Prerequisites) ->
    {AdjMap, IndegMap} = build_graph(Prerequisites, #{}, #{}),
    Queue0 = init_queue(NumCourses, IndegMap),
    bfs(NumCourses, AdjMap, IndegMap, Queue0, []).

build_graph([], Adj, Indeg) -> {Adj, Indeg};
build_graph([[A,B]|Rest], Adj, Indeg) ->
    NewAdj = maps:update_with(B,
                fun(L) -> [A|L] end,
                [A],
                Adj),
    NewIndeg = maps:update_with(A,
                fun(V) -> V + 1 end,
                1,
                Indeg),
    build_graph(Rest, NewAdj, NewIndeg).

init_queue(NumCourses, IndegMap) ->
    init_queue(0, NumCourses, IndegMap, queue:new()).

init_queue(I, N, _, Q) when I >= N -> Q;
init_queue(I, N, IndegMap, Q) ->
    Deg = maps:get(I, IndegMap, 0),
    Q1 = if Deg == 0 -> queue:in(I, Q); true -> Q end,
    init_queue(I + 1, N, IndegMap, Q1).

bfs(N, AdjMap, IndegMap, Queue, Result) ->
    case queue:out(Queue) of
        {empty, _} ->
            if length(Result) == N -> lists:reverse(Result); true -> [] end;
        {{value, Node}, RestQ} ->
            Neigh = maps:get(Node, AdjMap, []),
            {NewIndegMap, NewQueue} = process_neighbors(Neigh, IndegMap, RestQ),
            bfs(N, AdjMap, NewIndegMap, NewQueue, [Node|Result])
    end.

process_neighbors([], IndegMap, Queue) -> {IndegMap, Queue};
process_neighbors([V|Vs], IndegMap, Queue) ->
    Curr = maps:get(V, IndegMap, 0),
    NewDeg = Curr - 1,
    UpdatedIndegMap = if
        NewDeg == 0 -> maps:remove(V, IndegMap);
        true -> maps:put(V, NewDeg, IndegMap)
    end,
    NewQueue = if NewDeg == 0 -> queue:in(V, Queue); true -> Queue end,
    process_neighbors(Vs, UpdatedIndegMap, NewQueue).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_order(num_courses :: integer, prerequisites :: [[integer]]) :: [integer]
  def find_order(num_courses, prerequisites) do
    {adj_map, indeg_arr} =
      Enum.reduce(prerequisites, {%{}, :array.new(num_courses, default: 0)}, fn [a, b], {adj, indeg} ->
        adj = Map.update(adj, b, [a], fn list -> [a | list] end)
        cur = :array.get(a, indeg)
        indeg = :array.set(a, cur + 1, indeg)
        {adj, indeg}
      end)

    queue =
      0..(num_courses - 1)
      |> Enum.filter(fn i -> :array.get(i, indeg_arr) == 0 end)
      |> Enum.reduce(:queue.new(), fn i, q -> :queue.in(i, q) end)

    {order_rev, _indeg_final, _q} = bfs(queue, adj_map, indeg_arr, [])
    order = Enum.reverse(order_rev)

    if length(order) == num_courses, do: order, else: []
  end

  defp bfs(queue, adj, indeg, acc) do
    case :queue.out(queue) do
      {:empty, _} ->
        {acc, indeg, queue}

      {{:value, node}, q2} ->
        acc = [node | acc]

        neighbors = Map.get(adj, node, [])

        {indeg, q2} =
          Enum.reduce(neighbors, {indeg, q2}, fn nb, {indeg_acc, q_acc} ->
            cur = :array.get(nb, indeg_acc)
            new_val = cur - 1
            indeg_acc = :array.set(nb, new_val, indeg_acc)

            if new_val == 0 do
              {indeg_acc, :queue.in(nb, q_acc)}
            else
              {indeg_acc, q_acc}
            end
          end)

        bfs(q2, adj, indeg, acc)
    end
  end
end
```

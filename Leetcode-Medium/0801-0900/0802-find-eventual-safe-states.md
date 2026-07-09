# 0802. Find Eventual Safe States

## Cpp

```cpp
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> outDeg(n, 0);
        vector<vector<int>> rev(n);
        for (int i = 0; i < n; ++i) {
            for (int v : graph[i]) {
                ++outDeg[i];
                rev[v].push_back(i);
            }
        }
        queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (outDeg[i] == 0) q.push(i);
        }
        vector<int> safe;
        while (!q.empty()) {
            int node = q.front(); q.pop();
            safe.push_back(node);
            for (int prev : rev[node]) {
                if (--outDeg[prev] == 0) {
                    q.push(prev);
                }
            }
        }
        sort(safe.begin(), safe.end());
        return safe;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        int[] outDegree = new int[n];
        List<Integer>[] rev = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            rev[i] = new ArrayList<>();
        }
        for (int i = 0; i < n; i++) {
            outDegree[i] = graph[i].length;
            for (int v : graph[i]) {
                rev[v].add(i);
            }
        }

        Queue<Integer> queue = new ArrayDeque<>();
        boolean[] safe = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (outDegree[i] == 0) {
                queue.offer(i);
            }
        }

        while (!queue.isEmpty()) {
            int node = queue.poll();
            safe[node] = true;
            for (int prev : rev[node]) {
                outDegree[prev]--;
                if (outDegree[prev] == 0) {
                    queue.offer(prev);
                }
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (safe[i]) {
                result.add(i);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        # reverse adjacency list
        rev = [[] for _ in range(n)]
        outdeg = [0] * n
        for i, nbrs in enumerate(graph):
            outdeg[i] = len(nbrs)
            for v in nbrs:
                rev[v].append(i)

        from collections import deque
        q = deque([i for i in range(n) if outdeg[i] == 0])
        safe = []
        while q:
            node = q.popleft()
            safe.append(node)
            for prev in rev[node]:
                outdeg[prev] -= 1
                if outdeg[prev] == 0:
                    q.append(prev)

        return sorted(safe)
```

## Python3

```python
import collections
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outdeg = [len(nei) for nei in graph]
        rev = [[] for _ in range(n)]
        for u, neighbors in enumerate(graph):
            for v in neighbors:
                rev[v].append(u)

        q = collections.deque([i for i in range(n) if outdeg[i] == 0])
        safe = [False] * n

        while q:
            node = q.popleft()
            safe[node] = True
            for prev in rev[node]:
                outdeg[prev] -= 1
                if outdeg[prev] == 0:
                    q.append(prev)

        return [i for i, s in enumerate(safe) if s]
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* eventualSafeNodes(int** graph, int graphSize, int* graphColSize, int* returnSize) {
    int n = graphSize;
    int *outdeg = (int*)calloc(n, sizeof(int));
    int *revCount = (int*)calloc(n, sizeof(int));

    // First pass: count outdegrees and reverse edge counts
    for (int i = 0; i < n; ++i) {
        int sz = graphColSize[i];
        outdeg[i] = sz;
        for (int j = 0; j < sz; ++j) {
            int v = graph[i][j];
            revCount[v]++;
        }
    }

    // Allocate reverse adjacency lists
    int **rev = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        rev[i] = (int*)malloc(revCount[i] * sizeof(int));
        revCount[i] = 0; // reuse as fill index
    }

    // Second pass: fill reverse adjacency lists
    for (int i = 0; i < n; ++i) {
        int sz = graphColSize[i];
        for (int j = 0; j < sz; ++j) {
            int v = graph[i][j];
            rev[v][revCount[v]++] = i;
        }
    }

    // Queue for BFS
    int *queue = (int*)malloc(n * sizeof(int));
    int front = 0, back = 0;

    // Initialize queue with terminal nodes (outdeg == 0)
    for (int i = 0; i < n; ++i) {
        if (outdeg[i] == 0) {
            queue[back++] = i;
        }
    }

    bool *safe = (bool*)calloc(n, sizeof(bool));

    while (front < back) {
        int node = queue[front++];
        safe[node] = true;
        for (int k = 0; k < revCount[node]; ++k) {
            int prev = rev[node][k];
            outdeg[prev]--;
            if (outdeg[prev] == 0) {
                queue[back++] = prev;
            }
        }
    }

    // Collect safe nodes in ascending order
    int *result = (int*)malloc(n * sizeof(int));
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        if (safe[i]) {
            result[cnt++] = i;
        }
    }

    *returnSize = cnt;

    // Free temporary allocations
    free(outdeg);
    free(revCount);
    for (int i = 0; i < n; ++i) free(rev[i]);
    free(rev);
    free(queue);
    free(safe);

    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> EventualSafeNodes(int[][] graph) {
        int n = graph.Length;
        int[] outDegree = new int[n];
        List<int>[] rev = new List<int>[n];
        for (int i = 0; i < n; i++) rev[i] = new List<int>();
        
        for (int i = 0; i < n; i++) {
            foreach (int v in graph[i]) {
                outDegree[i]++;
                rev[v].Add(i);
            }
        }
        
        Queue<int> q = new Queue<int>();
        bool[] safe = new bool[n];
        for (int i = 0; i < n; i++) {
            if (outDegree[i] == 0) {
                q.Enqueue(i);
            }
        }
        
        while (q.Count > 0) {
            int node = q.Dequeue();
            safe[node] = true;
            foreach (int prev in rev[node]) {
                outDegree[prev]--;
                if (outDegree[prev] == 0) {
                    q.Enqueue(prev);
                }
            }
        }
        
        List<int> result = new List<int>();
        for (int i = 0; i < n; i++) {
            if (safe[i]) result.Add(i);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} graph
 * @return {number[]}
 */
var eventualSafeNodes = function(graph) {
    const n = graph.length;
    const outdeg = new Array(n).fill(0);
    const rev = Array.from({ length: n }, () => []);
    
    for (let u = 0; u < n; ++u) {
        const neighbors = graph[u];
        outdeg[u] = neighbors.length;
        for (const v of neighbors) {
            rev[v].push(u);
        }
    }
    
    const queue = [];
    let head = 0;
    for (let i = 0; i < n; ++i) {
        if (outdeg[i] === 0) queue.push(i);
    }
    
    const safe = new Array(n).fill(false);
    while (head < queue.length) {
        const node = queue[head++];
        safe[node] = true;
        for (const prev of rev[node]) {
            outdeg[prev]--;
            if (outdeg[prev] === 0) queue.push(prev);
        }
    }
    
    const result = [];
    for (let i = 0; i < n; ++i) {
        if (safe[i]) result.push(i);
    }
    return result;
};
```

## Typescript

```typescript
function eventualSafeNodes(graph: number[][]): number[] {
    const n = graph.length;
    const rev: number[][] = Array.from({ length: n }, () => []);
    const outDeg: number[] = new Array(n);
    
    for (let i = 0; i < n; i++) {
        outDeg[i] = graph[i].length;
        for (const v of graph[i]) {
            rev[v].push(i); // reverse edge
        }
    }
    
    const queue: number[] = [];
    for (let i = 0; i < n; i++) {
        if (outDeg[i] === 0) queue.push(i);
    }
    
    const safe = new Array<boolean>(n).fill(false);
    let qIdx = 0;
    while (qIdx < queue.length) {
        const node = queue[qIdx++];
        safe[node] = true;
        for (const prev of rev[node]) {
            outDeg[prev]--;
            if (outDeg[prev] === 0) {
                queue.push(prev);
            }
        }
    }
    
    const result: number[] = [];
    for (let i = 0; i < n; i++) {
        if (safe[i]) result.push(i);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $graph
     * @return Integer[]
     */
    function eventualSafeNodes($graph) {
        $n = count($graph);
        $outdeg = array_fill(0, $n, 0);
        $rev = array_fill(0, $n, []);

        for ($i = 0; $i < $n; $i++) {
            $outdeg[$i] = count($graph[$i]);
            foreach ($graph[$i] as $v) {
                $rev[$v][] = $i;
            }
        }

        $queue = new SplQueue();
        for ($i = 0; $i < $n; $i++) {
            if ($outdeg[$i] === 0) {
                $queue->enqueue($i);
            }
        }

        $safe = array_fill(0, $n, false);

        while (!$queue->isEmpty()) {
            $node = $queue->dequeue();
            $safe[$node] = true;
            foreach ($rev[$node] as $prev) {
                $outdeg[$prev]--;
                if ($outdeg[$prev] === 0) {
                    $queue->enqueue($prev);
                }
            }
        }

        $result = [];
        for ($i = 0; $i < $n; $i++) {
            if ($safe[$i]) {
                $result[] = $i;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func eventualSafeNodes(_ graph: [[Int]]) -> [Int] {
        let n = graph.count
        var outDegree = [Int](repeating: 0, count: n)
        var revAdj = [[Int]](repeating: [], count: n)
        
        for i in 0..<n {
            let neighbors = graph[i]
            outDegree[i] = neighbors.count
            for v in neighbors {
                revAdj[v].append(i)
            }
        }
        
        var queue = [Int]()
        var head = 0
        for i in 0..<n where outDegree[i] == 0 {
            queue.append(i)
        }
        
        var safe = [Bool](repeating: false, count: n)
        
        while head < queue.count {
            let node = queue[head]
            head += 1
            safe[node] = true
            for prev in revAdj[node] {
                outDegree[prev] -= 1
                if outDegree[prev] == 0 {
                    queue.append(prev)
                }
            }
        }
        
        var result = [Int]()
        for i in 0..<n where safe[i] {
            result.append(i)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun eventualSafeNodes(graph: Array<IntArray>): List<Int> {
        val n = graph.size
        val outDegree = IntArray(n)
        val rev = Array(n) { mutableListOf<Int>() }
        for (i in 0 until n) {
            outDegree[i] = graph[i].size
            for (v in graph[i]) {
                rev[v].add(i)
            }
        }
        val queue: java.util.ArrayDeque<Integer> = java.util.ArrayDeque()
        for (i in 0 until n) {
            if (outDegree[i] == 0) queue.add(i)
        }
        val safe = BooleanArray(n)
        while (!queue.isEmpty()) {
            val node = queue.poll()
            safe[node] = true
            for (prev in rev[node]) {
                outDegree[prev]--
                if (outDegree[prev] == 0) queue.add(prev)
            }
        }
        val result = mutableListOf<Int>()
        for (i in 0 until n) {
            if (safe[i]) result.add(i)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> eventualSafeNodes(List<List<int>> graph) {
    int n = graph.length;
    List<int> outDeg = List.filled(n, 0);
    List<List<int>> rev = List.generate(n, (_) => []);
    for (int i = 0; i < n; i++) {
      outDeg[i] = graph[i].length;
      for (int v in graph[i]) {
        rev[v].add(i);
      }
    }

    List<int> queue = [];
    int qHead = 0;
    for (int i = 0; i < n; i++) {
      if (outDeg[i] == 0) queue.add(i);
    }

    List<bool> safe = List.filled(n, false);
    while (qHead < queue.length) {
      int node = queue[qHead++];
      safe[node] = true;
      for (int prev in rev[node]) {
        outDeg[prev]--;
        if (outDeg[prev] == 0) {
          queue.add(prev);
        }
      }
    }

    List<int> result = [];
    for (int i = 0; i < n; i++) {
      if (safe[i]) result.add(i);
    }
    return result;
  }
}
```

## Golang

```go
import "sort"

func eventualSafeNodes(graph [][]int) []int {
	n := len(graph)
	indeg := make([]int, n)
	rev := make([][]int, n)

	for i, edges := range graph {
		indeg[i] = len(edges)
		for _, v := range edges {
			rev[v] = append(rev[v], i)
		}
	}

	queue := make([]int, 0)
	for i := 0; i < n; i++ {
		if indeg[i] == 0 {
			queue = append(queue, i)
		}
	}

	safe := make([]bool, n)

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		safe[node] = true
		for _, prev := range rev[node] {
			indeg[prev]--
			if indeg[prev] == 0 {
				queue = append(queue, prev)
			}
		}
	}

	res := make([]int, 0)
	for i := 0; i < n; i++ {
		if safe[i] {
			res = append(res, i)
		}
	}
	sort.Ints(res)
	return res
}
```

## Ruby

```ruby
def eventual_safe_nodes(graph)
  n = graph.length
  outdeg = Array.new(n, 0)
  rev = Array.new(n) { [] }

  graph.each_with_index do |neighbors, i|
    outdeg[i] = neighbors.size
    neighbors.each { |v| rev[v] << i }
  end

  queue = []
  (0...n).each { |i| queue << i if outdeg[i].zero? }
  safe = Array.new(n, false)

  head = 0
  while head < queue.size
    node = queue[head]
    head += 1
    safe[node] = true
    rev[node].each do |prev|
      outdeg[prev] -= 1
      queue << prev if outdeg[prev].zero?
    end
  end

  result = []
  (0...n).each { |i| result << i if safe[i] }
  result
end
```

## Scala

```scala
object Solution {
    def eventualSafeNodes(graph: Array[Array[Int]]): List[Int] = {
        val n = graph.length
        val rev = Array.fill(n)(scala.collection.mutable.ArrayBuffer[Int]())
        val outDeg = new Array[Int](n)

        for (i <- 0 until n) {
            outDeg(i) = graph(i).length
            for (j <- graph(i)) {
                rev(j) += i
            }
        }

        import scala.collection.mutable.Queue
        val q = Queue[Int]()
        for (i <- 0 until n if outDeg(i) == 0) q.enqueue(i)

        val safe = new Array[Boolean](n)
        while (q.nonEmpty) {
            val node = q.dequeue()
            safe(node) = true
            for (prev <- rev(node)) {
                outDeg(prev) -= 1
                if (outDeg(prev) == 0) q.enqueue(prev)
            }
        }

        val res = scala.collection.mutable.ListBuffer[Int]()
        for (i <- 0 until n if safe(i)) res += i
        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn eventual_safe_nodes(graph: Vec<Vec<i32>>) -> Vec<i32> {
        let n = graph.len();
        let mut outdeg = vec![0usize; n];
        let mut rev_adj: Vec<Vec<usize>> = vec![Vec::new(); n];

        for (i, edges) in graph.iter().enumerate() {
            outdeg[i] = edges.len();
            for &v in edges {
                rev_adj[v as usize].push(i);
            }
        }

        use std::collections::VecDeque;
        let mut queue = VecDeque::new();
        for i in 0..n {
            if outdeg[i] == 0 {
                queue.push_back(i);
            }
        }

        let mut safe = vec![false; n];
        while let Some(node) = queue.pop_front() {
            safe[node] = true;
            for &prev in &rev_adj[node] {
                outdeg[prev] -= 1;
                if outdeg[prev] == 0 {
                    queue.push_back(prev);
                }
            }
        }

        (0..n).filter(|&i| safe[i]).map(|i| i as i32).collect()
    }
}
```

## Racket

```racket
(define/contract (eventual-safe-nodes graph)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((n (length graph))
         (deg (make-vector n 0))
         (revAdj (make-vector n '()))
         (queue (make-vector n 0))
         (head 0)
         (tail 0)
         (safe (make-vector n #f)))
    ;; Build out-degree array and reversed adjacency list
    (let loop ((i 0))
      (when (< i n)
        (let ((neighbors (list-ref graph i)))
          (vector-set! deg i (length neighbors))
          (for-each (lambda (j)
                      (vector-set! revAdj j (cons i (vector-ref revAdj j))))
                    neighbors))
        (loop (+ i 1))))
    ;; Initialize queue with terminal nodes (out-degree == 0)
    (let loop ((i 0))
      (when (< i n)
        (when (= (vector-ref deg i) 0)
          (vector-set! queue tail i)
          (set! tail (+ tail 1)))
        (loop (+ i 1))))
    ;; Process nodes in topological order
    (let bfs ()
      (when (< head tail)
        (let ((u (vector-ref queue head)))
          (set! head (+ head 1))
          (vector-set! safe u #t)
          (for-each (lambda (v)
                      (let ((newdeg (- (vector-ref deg v) 1)))
                        (vector-set! deg v newdeg)
                        (when (= newdeg 0)
                          (vector-set! queue tail v)
                          (set! tail (+ tail 1)))))
                    (vector-ref revAdj u))
          (bfs))))
    ;; Collect safe nodes in ascending order
    (let loop ((i 0) (acc '()))
      (if (= i n)
          (reverse acc)
          (loop (+ i 1)
                (if (vector-ref safe i)
                    (cons i acc)
                    acc))))))
```

## Erlang

```erlang
-spec eventual_safe_nodes(Graph :: [[integer()]]) -> [integer()].
eventual_safe_nodes(Graph) ->
    N = length(Graph),
    RevMap = build_rev_map(Graph, 0, #{}),
    IndegArr0 = array:new(N, {default,0}),
    IndegArr = fill_indeg(Graph, 0, IndegArr0),
    Q0 = init_queue(IndegArr, N, queue:new()),
    SafeNodes = bfs(Q0, RevMap, IndegArr, []),
    lists:sort(SafeNodes).

build_rev_map([], _Idx, Map) -> Map;
build_rev_map([Neighbors|Rest], Idx, Map) ->
    NewMap = add_edges(Neighbors, Idx, Map),
    build_rev_map(Rest, Idx + 1, NewMap).

add_edges([], _From, Map) -> Map;
add_edges([To|Ts], From, Map) ->
    PrevList = maps:get(To, Map, []),
    UpdatedMap = maps:put(To, [From | PrevList], Map),
    add_edges(Ts, From, UpdatedMap).

fill_indeg([], _Idx, Arr) -> Arr;
fill_indeg([Neighbors|Rest], Idx, Arr) ->
    OutDeg = length(Neighbors),
    NewArr = array:set(Idx, OutDeg, Arr),
    fill_indeg(Rest, Idx + 1, NewArr).

init_queue(IndegArr, N, Q) -> init_queue(0, N, IndegArr, Q).
init_queue(I, N, _Arr, Q) when I >= N -> Q;
init_queue(I, N, Arr, Q) ->
    Deg = array:get(I, Arr),
    NewQ = if Deg == 0 -> queue:in(I, Q); true -> Q end,
    init_queue(I + 1, N, Arr, NewQ).

bfs(Q, RevMap, IndegArr, SafeAcc) ->
    case queue:out(Q) of
        {empty, _} ->
            lists:reverse(SafeAcc);
        {{value, Node}, Q1} ->
            Preds = maps:get(Node, RevMap, []),
            {NewIndegArr, NewQ} = process_preds(Preds, Q1, IndegArr),
            bfs(NewQ, RevMap, NewIndegArr, [Node | SafeAcc])
    end.

process_preds([], Q, Arr) -> {Arr, Q};
process_preds([Prev|Rest], Q, Arr) ->
    Deg = array:get(Prev, Arr),
    NewDeg = Deg - 1,
    UpdatedArr = array:set(Prev, NewDeg, Arr),
    NewQ = if NewDeg == 0 -> queue:in(Prev, Q); true -> Q end,
    process_preds(Rest, NewQ, UpdatedArr).
```

## Elixir

```elixir
defmodule Solution do
  @spec eventual_safe_nodes(graph :: [[integer]]) :: [integer]
  def eventual_safe_nodes(graph) do
    n = length(graph)
    colors = :array.new(n, default: 0)

    {colors, _} =
      Enum.reduce(0..(n - 1), {colors, []}, fn node, {col_acc, safe_acc} ->
        {new_col, is_safe} = dfs(node, graph, col_acc)
        if is_safe do
          {new_col, [node | safe_acc]}
        else
          {new_col, safe_acc}
        end
      end)

    Enum.filter(0..(n - 1), fn i -> :array.get(i, colors) == 2 end)
  end

  defp dfs(node, graph, colors) do
    case :array.get(node, colors) do
      2 ->
        {colors, true}

      3 ->
        {colors, false}

      1 ->
        # currently in recursion stack -> cycle detected
        {colors, false}

      _ ->
        # mark as visiting
        colors = :array.set(node, 1, colors)
        neighbors = Enum.at(graph, node)

        {colors, safe?} =
          Enum.reduce_while(neighbors, {colors, true}, fn nb, {col_acc, _} ->
            {new_col, nb_safe} = dfs(nb, graph, col_acc)

            if nb_safe do
              {:cont, {new_col, true}}
            else
              {:halt, {new_col, false}}
            end
          end)

        if safe? do
          colors = :array.set(node, 2, colors)
          {colors, true}
        else
          colors = :array.set(node, 3, colors)
          {colors, false}
        end
    end
  end
end
```

# 1743. Restore the Array From Adjacent Pairs

## Cpp

```cpp
class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        unordered_map<int, vector<int>> graph;
        graph.reserve(adjacentPairs.size() * 2);
        for (const auto& p : adjacentPairs) {
            int a = p[0], b = p[1];
            graph[a].push_back(b);
            graph[b].push_back(a);
        }
        
        int start = 0;
        for (const auto& kv : graph) {
            if (kv.second.size() == 1) { // endpoint
                start = kv.first;
                break;
            }
        }
        
        vector<int> ans;
        ans.reserve(graph.size());
        ans.push_back(start);
        
        int prev = INT_MAX; // sentinel not present in input range
        int curr = start;
        while (ans.size() < graph.size()) {
            const auto& neigh = graph[curr];
            int next;
            if (neigh.size() == 1) {
                next = neigh[0]; // only possible at the very beginning
            } else { // size == 2
                next = (neigh[0] == prev) ? neigh[1] : neigh[0];
            }
            ans.push_back(next);
            prev = curr;
            curr = next;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] restoreArray(int[][] adjacentPairs) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] p : adjacentPairs) {
            graph.computeIfAbsent(p[0], k -> new ArrayList<>()).add(p[1]);
            graph.computeIfAbsent(p[1], k -> new ArrayList<>()).add(p[0]);
        }
        int start = 0;
        for (var entry : graph.entrySet()) {
            if (entry.getValue().size() == 1) {
                start = entry.getKey();
                break;
            }
        }
        int n = adjacentPairs.length + 1;
        int[] ans = new int[n];
        ans[0] = start;
        int prev = Integer.MIN_VALUE; // sentinel outside input range
        int curr = start;
        for (int i = 1; i < n; i++) {
            List<Integer> neigh = graph.get(curr);
            int next = neigh.get(0);
            if (next == prev) {
                next = neigh.size() > 1 ? neigh.get(1) : next;
            }
            ans[i] = next;
            prev = curr;
            curr = next;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)

        # Find an endpoint (degree == 1)
        start = None
        for node, neigh in graph.items():
            if len(neigh) == 1:
                start = node
                break

        n = len(graph)
        result = [start]
        prev = None
        curr = start

        while len(result) < n:
            for nxt in graph[curr]:
                if nxt != prev:
                    result.append(nxt)
                    prev, curr = curr, nxt
                    break

        return result
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        # Find an endpoint (degree == 1)
        start = next(node for node, nbrs in graph.items() if len(nbrs) == 1)

        n = len(graph)
        result = [start]
        prev = None
        curr = start

        while len(result) < n:
            for nxt in graph[curr]:
                if nxt != prev:
                    result.append(nxt)
                    prev, curr = curr, nxt
                    break

        return result
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct Node {
    int key;
    int cnt;
    int nbr[2];
    struct Node* next;
} Node;

#define HASH_SIZE 262144  // power of two

static unsigned int hash_key(int key) {
    return ((unsigned int)key * 2654435761u) & (HASH_SIZE - 1);
}

/* Find existing node or create a new one */
static Node* get_or_create(Node** table, int key) {
    unsigned int h = hash_key(key);
    Node* cur = table[h];
    while (cur) {
        if (cur->key == key) return cur;
        cur = cur->next;
    }
    Node* nd = (Node*)malloc(sizeof(Node));
    nd->key = key;
    nd->cnt = 0;
    nd->nbr[0] = nd->nbr[1] = 0;
    nd->next = table[h];
    table[h] = nd;
    return nd;
}

/* Find existing node, return NULL if not found */
static Node* get_node(Node** table, int key) {
    unsigned int h = hash_key(key);
    Node* cur = table[h];
    while (cur) {
        if (cur->key == key) return cur;
        cur = cur->next;
    }
    return NULL;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* restoreArray(int** adjacentPairs, int adjacentPairsSize, int* adjacentPairsColSize, int* returnSize) {
    Node** table = (Node**)calloc(HASH_SIZE, sizeof(Node*));
    
    for (int i = 0; i < adjacentPairsSize; ++i) {
        int a = adjacentPairs[i][0];
        int b = adjacentPairs[i][1];
        Node* na = get_or_create(table, a);
        na->nbr[na->cnt++] = b;
        Node* nb = get_or_create(table, b);
        nb->nbr[nb->cnt++] = a;
    }
    
    int start = 0;
    for (int i = 0; i < HASH_SIZE && start == 0; ++i) {
        Node* cur = table[i];
        while (cur) {
            if (cur->cnt == 1) { start = cur->key; break; }
            cur = cur->next;
        }
    }
    
    int n = adjacentPairsSize + 1;
    int* ans = (int*)malloc(n * sizeof(int));
    ans[0] = start;
    int prev = INT_MAX;
    int curr = start;
    
    for (int i = 1; i < n; ++i) {
        Node* node = get_node(table, curr);
        int next;
        if (node->cnt == 1) {
            next = node->nbr[0];
        } else {
            next = (node->nbr[0] != prev) ? node->nbr[0] : node->nbr[1];
        }
        ans[i] = next;
        prev = curr;
        curr = next;
    }
    
    *returnSize = n;
    free(table);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] RestoreArray(int[][] adjacentPairs) {
        var graph = new Dictionary<int, List<int>>();
        foreach (var pair in adjacentPairs) {
            int a = pair[0], b = pair[1];
            if (!graph.ContainsKey(a)) graph[a] = new List<int>();
            if (!graph.ContainsKey(b)) graph[b] = new List<int>();
            graph[a].Add(b);
            graph[b].Add(a);
        }

        // Find an endpoint (degree == 1)
        int start = 0;
        foreach (var kvp in graph) {
            if (kvp.Value.Count == 1) {
                start = kvp.Key;
                break;
            }
        }

        int n = graph.Count;
        var result = new int[n];
        result[0] = start;
        // The neighbor of the start node
        result[1] = graph[start][0];

        for (int i = 2; i < n; i++) {
            int prev = result[i - 2];
            int curr = result[i - 1];
            var neighbors = graph[curr];
            // neighbors count is either 1 (only when n==2) or 2
            int next = neighbors[0] == prev ? neighbors[1] : neighbors[0];
            result[i] = next;
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} adjacentPairs
 * @return {number[]}
 */
var restoreArray = function(adjacentPairs) {
    const graph = new Map();
    for (const [u, v] of adjacentPairs) {
        if (!graph.has(u)) graph.set(u, []);
        if (!graph.has(v)) graph.set(v, []);
        graph.get(u).push(v);
        graph.get(v).push(u);
    }
    
    let start;
    for (const [node, neigh] of graph.entries()) {
        if (neigh.length === 1) {
            start = node;
            break;
        }
    }
    
    const n = adjacentPairs.length + 1;
    const result = new Array(n);
    result[0] = start;
    
    let prev = null;
    let curr = start;
    for (let i = 1; i < n; i++) {
        const neighbors = graph.get(curr);
        let next;
        if (neighbors.length === 1) {
            // only one neighbor (happens at the end)
            next = neighbors[0];
        } else {
            // two neighbors, pick the one that's not prev
            next = neighbors[0] === prev ? neighbors[1] : neighbors[0];
        }
        result[i] = next;
        prev = curr;
        curr = next;
    }
    
    return result;
};
```

## Typescript

```typescript
function restoreArray(adjacentPairs: number[][]): number[] {
    const adj = new Map<number, number[]>();
    for (const [u, v] of adjacentPairs) {
        if (!adj.has(u)) adj.set(u, []);
        if (!adj.has(v)) adj.set(v, []);
        adj.get(u)!.push(v);
        adj.get(v)!.push(u);
    }
    let start = 0;
    for (const [node, neighbors] of adj.entries()) {
        if (neighbors.length === 1) {
            start = node;
            break;
        }
    }
    const result: number[] = [];
    let prev: number | null = null;
    let curr = start;
    while (result.length < adj.size) {
        result.push(curr);
        const neighbors = adj.get(curr)!;
        let next: number | null = null;
        for (const nb of neighbors) {
            if (nb !== prev) {
                next = nb;
                break;
            }
        }
        prev = curr;
        if (next === null) break;
        curr = next;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $adjacentPairs
     * @return Integer[]
     */
    function restoreArray($adjacentPairs) {
        $graph = [];
        foreach ($adjacentPairs as $pair) {
            [$u, $v] = $pair;
            if (!isset($graph[$u])) $graph[$u] = [];
            if (!isset($graph[$v])) $graph[$v] = [];
            $graph[$u][] = $v;
            $graph[$v][] = $u;
        }

        // Find an endpoint (node with only one neighbor)
        $root = null;
        foreach ($graph as $num => $neighbors) {
            if (count($neighbors) === 1) {
                $root = $num;
                break;
            }
        }

        $ans = [];
        $curr = $root;
        $prev = null;

        while (count($ans) < count($graph)) {
            $ans[] = $curr;
            foreach ($graph[$curr] as $neighbor) {
                if ($neighbor !== $prev) {
                    $prev = $curr;
                    $curr = $neighbor;
                    break;
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
    func restoreArray(_ adjacentPairs: [[Int]]) -> [Int] {
        var graph = [Int: [Int]]()
        for pair in adjacentPairs {
            let a = pair[0]
            let b = pair[1]
            graph[a, default: []].append(b)
            graph[b, default: []].append(a)
        }
        
        // Find an endpoint (degree == 1)
        var start = 0
        for (node, neighbors) in graph {
            if neighbors.count == 1 {
                start = node
                break
            }
        }
        
        var result = [Int]()
        result.append(start)
        var prev = Int.max   // sentinel not present in input range
        var curr = start
        
        while result.count < graph.count {
            if let neighbors = graph[curr] {
                for neighbor in neighbors {
                    if neighbor != prev {
                        result.append(neighbor)
                        prev = curr
                        curr = neighbor
                        break
                    }
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun restoreArray(adjacentPairs: Array<IntArray>): IntArray {
        val graph = HashMap<Int, MutableList<Int>>()
        for (pair in adjacentPairs) {
            val a = pair[0]
            val b = pair[1]
            graph.computeIfAbsent(a) { mutableListOf() }.add(b)
            graph.computeIfAbsent(b) { mutableListOf() }.add(a)
        }
        var start = 0
        for ((key, list) in graph) {
            if (list.size == 1) {
                start = key
                break
            }
        }
        val n = adjacentPairs.size + 1
        val result = IntArray(n)
        result[0] = start
        var prev = 200001 // sentinel outside allowed value range
        var curr = start
        for (i in 1 until n) {
            val neighbors = graph[curr]!!
            var next = 0
            for (nbr in neighbors) {
                if (nbr != prev) {
                    next = nbr
                    break
                }
            }
            result[i] = next
            prev = curr
            curr = next
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> restoreArray(List<List<int>> adjacentPairs) {
    // Build the adjacency map
    final Map<int, List<int>> adj = {};
    for (var pair in adjacentPairs) {
      int a = pair[0];
      int b = pair[1];
      adj.putIfAbsent(a, () => []).add(b);
      adj.putIfAbsent(b, () => []).add(a);
    }

    // Find an endpoint (node with only one neighbor)
    int start = 0;
    for (var entry in adj.entries) {
      if (entry.value.length == 1) {
        start = entry.key;
        break;
      }
    }

    // Reconstruct the array by walking through the linked list
    final List<int> result = [start];
    int? prev; // previous node, null for the first step
    int curr = start;

    while (result.length < adj.length) {
      for (int neighbor in adj[curr]!) {
        if (prev == null || neighbor != prev) {
          result.add(neighbor);
          prev = curr;
          curr = neighbor;
          break;
        }
      }
    }

    return result;
  }
}
```

## Golang

```go
func restoreArray(adjacentPairs [][]int) []int {
    graph := make(map[int][]int)
    for _, p := range adjacentPairs {
        a, b := p[0], p[1]
        graph[a] = append(graph[a], b)
        graph[b] = append(graph[b], a)
    }

    var start int
    for node, neigh := range graph {
        if len(neigh) == 1 {
            start = node
            break
        }
    }

    n := len(graph)
    ans := make([]int, 0, n)

    curr := start
    var prev int
    hasPrev := false

    for len(ans) < n {
        ans = append(ans, curr)
        nextFound := false
        for _, nb := range graph[curr] {
            if !hasPrev || nb != prev {
                prev = curr
                curr = nb
                hasPrev = true
                nextFound = true
                break
            }
        }
        if !nextFound {
            break
        }
    }

    return ans
}
```

## Ruby

```ruby
def restore_array(adjacent_pairs)
  graph = Hash.new { |h, k| h[k] = [] }
  adjacent_pairs.each do |u, v|
    graph[u] << v
    graph[v] << u
  end

  start = nil
  graph.each do |node, neighbors|
    if neighbors.length == 1
      start = node
      break
    end
  end

  n = graph.size
  result = Array.new(n)
  result[0] = start
  prev = nil
  curr = start
  i = 1
  while i < n
    next_node = nil
    graph[curr].each do |nbr|
      if nbr != prev
        next_node = nbr
        break
      end
    end
    result[i] = next_node
    prev = curr
    curr = next_node
    i += 1
  end

  result
end
```

## Scala

```scala
object Solution {
  def restoreArray(adjacentPairs: Array[Array[Int]]): Array[Int] = {
    import scala.collection.mutable.{HashMap, ArrayBuffer}
    val graph = HashMap.empty[Int, ArrayBuffer[Int]]
    for (pair <- adjacentPairs) {
      val a = pair(0)
      val b = pair(1)
      graph.getOrElseUpdate(a, ArrayBuffer()).append(b)
      graph.getOrElseUpdate(b, ArrayBuffer()).append(a)
    }

    var start = 0
    var found = false
    for ((k, v) <- graph if !found) {
      if (v.size == 1) {
        start = k
        found = true
      }
    }

    val n = adjacentPairs.length + 1
    val result = new Array[Int](n)
    var idx = 0
    var curr = start
    var prev = 0
    var havePrev = false

    while (idx < n) {
      result(idx) = curr
      idx += 1
      val neighbors = graph(curr)
      if (!havePrev) {
        // first element, take its only neighbor
        if (neighbors.nonEmpty) {
          prev = curr
          curr = neighbors(0)
          havePrev = true
        }
      } else {
        // choose the neighbor that is not the previous node
        val next = if (neighbors(0) == prev) neighbors(1) else neighbors(0)
        prev = curr
        curr = next
      }
    }

    result
  }
}
```

## Rust

```rust
use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn restore_array(adjacent_pairs: Vec<Vec<i32>>) -> Vec<i32> {
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for pair in adjacent_pairs.iter() {
            let a = pair[0];
            let b = pair[1];
            graph.entry(a).or_insert_with(Vec::new).push(b);
            graph.entry(b).or_insert_with(Vec::new).push(a);
        }

        // Find an endpoint (degree == 1)
        let mut start = 0;
        for (&node, neighbors) in &graph {
            if neighbors.len() == 1 {
                start = node;
                break;
            }
        }

        let n = graph.len();
        let mut ans: Vec<i32> = Vec::with_capacity(n);
        ans.push(start);

        let mut prev = i32::MAX; // sentinel outside allowed range
        let mut curr = start;

        while ans.len() < n {
            let neighbors = &graph[&curr];
            for &next in neighbors.iter() {
                if next != prev {
                    ans.push(next);
                    prev = curr;
                    curr = next;
                    break;
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (restore-array adjacentPairs)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((graph (make-hash)))
    ;; build adjacency list
    (for ([pair adjacentPairs])
      (let ((u (list-ref pair 0))
            (v (list-ref pair 1)))
        (hash-update! graph u (lambda (lst) (cons v lst)) '())
        (hash-update! graph v (lambda (lst) (cons u lst)) '())))
    ;; find an endpoint (degree 1)
    (define start
      (for/first ([k (in-hash-keys graph)]
                  #:when (= (length (hash-ref graph k)) 1))
        k))
    (define n (hash-count graph))
    (define result (make-vector n))
    (vector-set! result 0 start)
    ;; iterative traversal
    (let loop ((idx 1) (prev #f) (curr start))
      (if (= idx n)
          (vector->list result)
          (let* ((neighbors (hash-ref graph curr))
                 (next (let find ((lst neighbors))
                         (cond [(null? lst) #f]
                               [(equal? (car lst) prev) (find (cdr lst))]
                               [else (car lst)]))))
            (vector-set! result idx next)
            (loop (+ idx 1) curr next))))))
```

## Erlang

```erlang
-module(solution).
-export([restore_array/1]).

-spec restore_array(AdjacentPairs :: [[integer()]]) -> [integer()].
restore_array(AdjacentPairs) ->
    Graph = lists:foldl(fun([U, V], Acc) ->
                Acc1 = add_edge(Acc, U, V),
                add_edge(Acc1, V, U)
            end, #{}, AdjacentPairs),
    Start = find_start(maps:keys(Graph), Graph),
    Size = maps:size(Graph),
    build(Start, none, 0, Size, Graph, []).

add_edge(Map, X, Y) ->
    Old = maps:get(X, Map, []),
    maps:put(X, [Y | Old], Map).

find_start([K | Rest], Graph) ->
    case maps:get(K, Graph) of
        [_] -> K;
        _   -> find_start(Rest, Graph)
    end;
find_start([], _) ->
    undefined.

build(Curr, Prev, Count, Size, Graph, Acc) ->
    NewAcc = [Curr | Acc],
    NewCount = Count + 1,
    case NewCount of
        Size -> lists:reverse(NewAcc);
        _    ->
            Neighs = maps:get(Curr, Graph),
            Next = next_node(Neighs, Prev),
            build(Next, Curr, NewCount, Size, Graph, NewAcc)
    end.

next_node([N | _], Prev) when N =/= Prev -> N;
next_node([_ | Rest], Prev) -> next_node(Rest, Prev);
next_node([], _) -> undefined.
```

## Elixir

```elixir
defmodule Solution do
  @spec restore_array(adjacent_pairs :: [[integer]]) :: [integer]
  def restore_array(adjacent_pairs) do
    graph =
      Enum.reduce(adjacent_pairs, %{}, fn [a, b], acc ->
        acc
        |> Map.update(a, [b], fn lst -> [b | lst] end)
        |> Map.update(b, [a], fn lst -> [a | lst] end)
      end)

    {start, _} =
      Enum.find(graph, fn {_k, v} -> length(v) == 1 end)

    n = map_size(graph)
    traverse(start, nil, graph, n, [])
  end

  defp traverse(_curr, _prev, _graph, 0, acc_rev), do: Enum.reverse(acc_rev)

  defp traverse(curr, prev, graph, remaining, acc_rev) do
    new_acc = [curr | acc_rev]

    if remaining - 1 == 0 do
      Enum.reverse(new_acc)
    else
      next =
        Map.get(graph, curr)
        |> Enum.find(fn neighbor -> neighbor != prev end)

      traverse(next, curr, graph, remaining - 1, new_acc)
    end
  end
end
```

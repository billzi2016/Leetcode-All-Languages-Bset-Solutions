# 0310. Minimum Height Trees

## Cpp

```cpp
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n <= 2) {
            vector<int> res;
            for (int i = 0; i < n; ++i) res.push_back(i);
            return res;
        }
        vector<vector<int>> adj(n);
        vector<int> degree(n, 0);
        for (const auto& e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
            ++degree[u];
            ++degree[v];
        }
        queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (degree[i] == 1) q.push(i);
        }
        int remaining = n;
        while (remaining > 2) {
            int leaves = q.size();
            remaining -= leaves;
            for (int i = 0; i < leaves; ++i) {
                int leaf = q.front(); q.pop();
                degree[leaf] = 0;
                for (int nb : adj[leaf]) {
                    if (--degree[nb] == 1) {
                        q.push(nb);
                    }
                }
            }
        }
        vector<int> res;
        while (!q.empty()) {
            res.push_back(q.front());
            q.pop();
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<Integer> result = new ArrayList<>();
        if (n == 1) {
            result.add(0);
            return result;
        }
        List<Set<Integer>> adj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            adj.add(new HashSet<>());
        }
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        List<Integer> leaves = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (adj.get(i).size() == 1) {
                leaves.add(i);
            }
        }

        int remainingNodes = n;
        while (remainingNodes > 2) {
            remainingNodes -= leaves.size();
            List<Integer> newLeaves = new ArrayList<>();
            for (int leaf : leaves) {
                // each leaf has exactly one neighbor
                int neighbor = adj.get(leaf).iterator().next();
                adj.get(neighbor).remove(leaf);
                if (adj.get(neighbor).size() == 1) {
                    newLeaves.add(neighbor);
                }
            }
            leaves = newLeaves;
        }

        return leaves;
    }
}
```

## Python

```python
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 2:
            return [i for i in range(n)]
        
        from collections import defaultdict, deque
        
        graph = defaultdict(set)
        degree = [0] * n
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degree[u] += 1
            degree[v] += 1
        
        leaves = deque([i for i in range(n) if degree[i] == 1])
        remaining_nodes = n
        
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
                # optional: clear to free memory
                graph[leaf].clear()
        
        return list(leaves)
```

## Python3

```python
from typing import List
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        adj = [set() for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            degree[u] += 1
            degree[v] += 1
        
        leaves = deque([i for i in range(n) if degree[i] == 1])
        remaining = n
        
        while remaining > 2:
            leaves_count = len(leaves)
            remaining -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in adj[leaf]:
                    adj[neighbor].remove(leaf)
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
                # optional: clear leaf adjacency
                adj[leaf].clear()
        
        return list(leaves)
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findMinHeightTrees(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    if (n == 1) {
        *returnSize = 1;
        int* res = (int*)malloc(sizeof(int));
        res[0] = 0;
        return res;
    }
    
    // degree of each node
    int *degree = (int*)calloc(n, sizeof(int));
    // first pass: count degrees
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        degree[a]++;
        degree[b]++;
    }
    
    // allocate adjacency lists
    int **adj = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        adj[i] = (int*)malloc(degree[i] * sizeof(int));
    }
    // temporary counters to fill adjacency
    int *pos = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        adj[a][pos[a]++] = b;
        adj[b][pos[b]++] = a;
    }
    
    // initial leaves
    int *leaves = (int*)malloc(n * sizeof(int));
    int leafCount = 0;
    for (int i = 0; i < n; ++i) {
        if (degree[i] == 1) {
            leaves[leafCount++] = i;
        }
    }
    
    int remaining = n;
    int *newLeaves = (int*)malloc(n * sizeof(int));
    
    while (remaining > 2) {
        int newLeafCount = 0;
        for (int i = 0; i < leafCount; ++i) {
            int leaf = leaves[i];
            // each leaf has exactly one neighbor
            for (int j = 0; j < degree[leaf]; ++j) {
                int nb = adj[leaf][j];
                degree[nb]--;
                if (degree[nb] == 1) {
                    newLeaves[newLeafCount++] = nb;
                }
            }
            degree[leaf] = 0; // removed
        }
        remaining -= leafCount;
        // swap buffers
        int *tmp = leaves;
        leaves = newLeaves;
        newLeaves = tmp;
        leafCount = newLeafCount;
    }
    
    // result is the remaining nodes in 'leaves'
    *returnSize = leafCount;
    int *result = (int*)malloc(leafCount * sizeof(int));
    for (int i = 0; i < leafCount; ++i) {
        result[i] = leaves[i];
    }
    
    // free allocated memory
    free(degree);
    free(pos);
    for (int i = 0; i < n; ++i) {
        free(adj[i]);
    }
    free(adj);
    free(leaves);
    free(newLeaves);
    
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> FindMinHeightTrees(int n, int[][] edges) {
        if (n == 1) return new List<int> { 0 };
        
        var adj = new List<HashSet<int>>();
        for (int i = 0; i < n; i++) adj.Add(new HashSet<int>());
        
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            adj[a].Add(b);
            adj[b].Add(a);
        }
        
        var leaves = new Queue<int>();
        for (int i = 0; i < n; i++) {
            if (adj[i].Count == 1) leaves.Enqueue(i);
        }
        
        int remaining = n;
        while (remaining > 2) {
            int leafCount = leaves.Count;
            remaining -= leafCount;
            for (int i = 0; i < leafCount; i++) {
                int leaf = leaves.Dequeue();
                int neighbor = -1;
                foreach (var nb in adj[leaf]) { neighbor = nb; break; }
                
                if (neighbor != -1) {
                    adj[neighbor].Remove(leaf);
                    if (adj[neighbor].Count == 1) leaves.Enqueue(neighbor);
                }
            }
        }
        
        var result = new List<int>();
        while (leaves.Count > 0) result.Add(leaves.Dequeue());
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findMinHeightTrees = function(n, edges) {
    if (n <= 2) return Array.from({length: n}, (_, i) => i);
    
    const adj = Array.from({length: n}, () => new Set());
    for (const [u, v] of edges) {
        adj[u].add(v);
        adj[v].add(u);
    }
    
    let leaves = [];
    for (let i = 0; i < n; i++) {
        if (adj[i].size === 1) leaves.push(i);
    }
    
    let remaining = n;
    while (remaining > 2) {
        const newLeaves = [];
        remaining -= leaves.length;
        for (const leaf of leaves) {
            const neighbor = adj[leaf].values().next().value; // only neighbor
            adj[neighbor].delete(leaf);
            if (adj[neighbor].size === 1) newLeaves.push(neighbor);
        }
        leaves = newLeaves;
    }
    
    return leaves;
};
```

## Typescript

```typescript
function findMinHeightTrees(n: number, edges: number[][]): number[] {
    if (n <= 2) return Array.from({ length: n }, (_, i) => i);
    
    const adj: Set<number>[] = Array.from({ length: n }, () => new Set<number>());
    for (const [u, v] of edges) {
        adj[u].add(v);
        adj[v].add(u);
    }
    
    let leaves: number[] = [];
    for (let i = 0; i < n; i++) {
        if (adj[i].size === 1) leaves.push(i);
    }
    
    let remaining = n;
    while (remaining > 2) {
        const newLeaves: number[] = [];
        remaining -= leaves.length;
        for (const leaf of leaves) {
            const neighbor = adj[leaf].values().next().value as number;
            adj[neighbor].delete(leaf);
            if (adj[neighbor].size === 1) newLeaves.push(neighbor);
        }
        leaves = newLeaves;
    }
    
    return leaves;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer[]
     */
    function findMinHeightTrees($n, $edges) {
        if ($n <= 2) {
            $res = [];
            for ($i = 0; $i < $n; $i++) {
                $res[] = $i;
            }
            return $res;
        }

        $adj = array_fill(0, $n, []);
        $degree = array_fill(0, $n, 0);

        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            $adj[$a][] = $b;
            $adj[$b][] = $a;
            $degree[$a]++;
            $degree[$b]++;
        }

        $leaves = [];
        for ($i = 0; $i < $n; $i++) {
            if ($degree[$i] == 1) {
                $leaves[] = $i;
            }
        }

        $remaining = $n;
        while ($remaining > 2) {
            $newLeaves = [];
            $leafCount = count($leaves);
            $remaining -= $leafCount;

            foreach ($leaves as $leaf) {
                foreach ($adj[$leaf] as $neighbor) {
                    $degree[$neighbor]--;
                    if ($degree[$neighbor] == 1) {
                        $newLeaves[] = $neighbor;
                    }
                }
            }

            $leaves = $newLeaves;
        }

        return $leaves;
    }
}
```

## Swift

```swift
class Solution {
    func findMinHeightTrees(_ n: Int, _ edges: [[Int]]) -> [Int] {
        if n <= 2 { return Array(0..<n) }
        
        var adj = [[Int]](repeating: [], count: n)
        for e in edges {
            let a = e[0], b = e[1]
            adj[a].append(b)
            adj[b].append(a)
        }
        
        var leaves = [Int]()
        for i in 0..<n {
            if adj[i].count == 1 {
                leaves.append(i)
            }
        }
        
        var remaining = n
        while remaining > 2 {
            let leafCount = leaves.count
            remaining -= leafCount
            var newLeaves = [Int]()
            
            for leaf in leaves {
                guard let neighbor = adj[leaf].first else { continue }
                
                // Remove the edge from neighbor's list
                if let idx = adj[neighbor].firstIndex(of: leaf) {
                    adj[neighbor].remove(at: idx)
                }
                
                // If neighbor becomes a leaf, add to newLeaves
                if adj[neighbor].count == 1 {
                    newLeaves.append(neighbor)
                }
            }
            
            leaves = newLeaves
        }
        
        return leaves
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMinHeightTrees(n: Int, edges: Array<IntArray>): List<Int> {
        if (n <= 2) return (0 until n).toList()
        val adj = Array(n) { mutableSetOf<Int>() }
        for (e in edges) {
            val a = e[0]
            val b = e[1]
            adj[a].add(b)
            adj[b].add(a)
        }
        var leaves = mutableListOf<Int>()
        for (i in 0 until n) {
            if (adj[i].size == 1) leaves.add(i)
        }
        var remaining = n
        while (remaining > 2) {
            remaining -= leaves.size
            val newLeaves = mutableListOf<Int>()
            for (leaf in leaves) {
                val neighbor = adj[leaf].iterator().next()
                adj[neighbor].remove(leaf)
                if (adj[neighbor].size == 1) newLeaves.add(neighbor)
            }
            leaves = newLeaves
        }
        return leaves
    }
}
```

## Dart

```dart
class Solution {
  List<int> findMinHeightTrees(int n, List<List<int>> edges) {
    if (n <= 2) {
      return List<int>.generate(n, (i) => i);
    }

    // Build adjacency list
    List<Set<int>> adj = List.generate(n, (_) => <int>{});
    for (var e in edges) {
      int a = e[0];
      int b = e[1];
      adj[a].add(b);
      adj[b].add(a);
    }

    // Initialize first layer of leaves
    List<int> leaves = [];
    for (int i = 0; i < n; i++) {
      if (adj[i].length == 1) {
        leaves.add(i);
      }
    }

    int remainingNodes = n;
    while (remainingNodes > 2) {
      remainingNodes -= leaves.length;
      List<int> newLeaves = [];

      for (int leaf in leaves) {
        // The only neighbor of a leaf
        int neighbor = adj[leaf].first;
        // Remove the edge leaf-neighbor
        adj[neighbor].remove(leaf);
        if (adj[neighbor].length == 1) {
          newLeaves.add(neighbor);
        }
      }

      leaves = newLeaves;
    }

    return leaves;
  }
}
```

## Golang

```go
func findMinHeightTrees(n int, edges [][]int) []int {
	if n <= 1 {
		res := make([]int, n)
		for i := 0; i < n; i++ {
			res[i] = i
		}
		return res
	}

	adj := make([][]int, n)
	degree := make([]int, n)
	for _, e := range edges {
		a, b := e[0], e[1]
		adj[a] = append(adj[a], b)
		adj[b] = append(adj[b], a)
		degree[a]++
		degree[b]++
	}

	leaves := []int{}
	for i := 0; i < n; i++ {
		if degree[i] == 1 {
			leaves = append(leaves, i)
		}
	}

	remaining := n
	for remaining > 2 {
		newLeaves := []int{}
		leafCount := len(leaves)
		remaining -= leafCount

		for _, leaf := range leaves {
			for _, nb := range adj[leaf] {
				degree[nb]--
				if degree[nb] == 1 {
					newLeaves = append(newLeaves, nb)
				}
			}
			degree[leaf] = 0
		}
		leaves = newLeaves
	}

	return leaves
}
```

## Ruby

```ruby
def find_min_height_trees(n, edges)
  return [0] if n == 1
  adj = Array.new(n) { [] }
  degree = Array.new(n, 0)

  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
    degree[u] += 1
    degree[v] += 1
  end

  leaves = []
  (0...n).each { |i| leaves << i if degree[i] == 1 }

  remaining = n
  while remaining > 2
    new_leaves = []
    leaves.each do |leaf|
      remaining -= 1
      adj[leaf].each do |neighbor|
        degree[neighbor] -= 1
        new_leaves << neighbor if degree[neighbor] == 1
      end
    end
    leaves = new_leaves
  end

  leaves
end
```

## Scala

```scala
object Solution {
    def findMinHeightTrees(n: Int, edges: Array[Array[Int]]): List[Int] = {
        if (n == 1) return List(0)

        val adj = Array.fill(n)(scala.collection.mutable.ArrayBuffer[Int]())
        for (e <- edges) {
            val a = e(0)
            val b = e(1)
            adj(a).append(b)
            adj(b).append(a)
        }

        val degree = Array.ofDim[Int](n)
        val leaves = scala.collection.mutable.Queue[Int]()
        for (i <- 0 until n) {
            degree(i) = adj(i).size
            if (degree(i) == 1) leaves.enqueue(i)
        }

        var remaining = n
        while (remaining > 2) {
            val leafCount = leaves.size
            for (_ <- 0 until leafCount) {
                val leaf = leaves.dequeue()
                remaining -= 1
                for (neighbor <- adj(leaf)) {
                    degree(neighbor) -= 1
                    if (degree(neighbor) == 1) {
                        leaves.enqueue(neighbor)
                    }
                }
            }
        }

        leaves.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_min_height_trees(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        if n <= 2 {
            return (0..n).map(|x| x as i32).collect();
        }
        use std::collections::HashSet;
        let mut adj: Vec<HashSet<usize>> = (0..n).map(|_| HashSet::new()).collect();
        for e in edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].insert(b);
            adj[b].insert(a);
        }
        let mut leaves: Vec<usize> = (0..n).filter(|&i| adj[i].len() == 1).collect();
        let mut remaining = n;
        while remaining > 2 {
            let leaf_cnt = leaves.len();
            remaining -= leaf_cnt;
            let mut new_leaves = Vec::new();
            for leaf in leaves {
                if let Some(&neighbor) = adj[leaf].iter().next() {
                    adj[neighbor].remove(&leaf);
                    if adj[neighbor].len() == 1 {
                        new_leaves.push(neighbor);
                    }
                }
                adj[leaf].clear();
            }
            leaves = new_leaves;
        }
        leaves.iter().map(|&x| x as i32).collect()
    }
}
```

## Racket

```racket
(define/contract (find-min-height-trees n edges)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (cond
    [(<= n 2) (build-list n values)]
    [else
     (let* ([adj (make-vector n '())]
            [_   (for-each (lambda (e)
                             (define a (first e))
                             (define b (second e))
                             (vector-set! adj a (cons b (vector-ref adj a)))
                             (vector-set! adj b (cons a (vector-ref adj b))))
                           edges)]
            [deg (make-vector n 0)])
       ;; compute degrees
       (for ([i (in-range n)])
         (vector-set! deg i (length (vector-ref adj i))))
       (define current-leaves
         (for/list ([i (in-range n)] #:when (= (vector-ref deg i) 1)) i))
       (define remaining n)
       (let loop ()
         (if (<= remaining 2)
             (for/list ([i (in-range n)] #:when (> (vector-ref deg i) 0)) i)
             (begin
               (set! remaining (- remaining (length current-leaves)))
               (define new-leaves '())
               (for ([leaf current-leaves])
                 (for ([nbr (vector-ref adj leaf)])
                   (when (> (vector-ref deg nbr) 0)
                     (let ([d (- (vector-ref deg nbr) 1)])
                       (vector-set! deg nbr d)
                       (when (= d 1)
                         (set! new-leaves (cons nbr new-leaves))))))
                 (vector-set! deg leaf 0))
               (set! current-leaves new-leaves)
               (loop))))])))
```

## Erlang

```erlang
-module(solution).
-export([find_min_height_trees/2]).

-spec find_min_height_trees(N :: integer(), Edges :: [[integer()]]) -> [integer()].
find_min_height_trees(N, Edges) ->
    case N of
        0 -> [];
        1 -> [0];
        _ when N =< 2 -> lists:seq(0, N - 1);
        _ ->
            Adj0 = build_adj(Edges, #{}),
            Leaves0 = initial_leaves(Adj0),
            trim(N, Adj0, Leaves0)
    end.

%% Build adjacency map
build_adj([], Map) -> Map;
build_adj([[A, B] | Rest], Map) ->
    M1 = maps:update_with(A,
            fun(L) -> [B | L] end,
            [B],
            Map),
    M2 = maps:update_with(B,
            fun(L) -> [A | L] end,
            [A],
            M1),
    build_adj(Rest, M2).

%% Initial leaves (degree == 1)
initial_leaves(Adj) ->
    [Node || {Node, Neigh} <- maps:to_list(Adj), length(Neigh) =:= 1].

%% Main trimming loop
trim(Remaining, Adj, Leaves) when Remaining =< 2 ->
    [Node || {Node, _} <- maps:to_list(Adj)];
trim(Remaining, Adj, Leaves) ->
    {Adj1, NewLeaves} = process_leaves(Leaves, Adj, []),
    trim(Remaining - length(Leaves), Adj1, NewLeaves).

%% Process current leaves, update adjacency and collect new leaves
process_leaves([], Adj, Acc) -> {Adj, lists:reverse(Acc)};
process_leaves([Leaf | Rest], Adj, Acc) ->
    case maps:get(Leaf, Adj) of
        [Neighbor] ->
            NeighborList = maps:get(Neighbor, Adj),
            UpdatedNeighborList = lists:delete(Leaf, NeighborList),
            Adj1 = maps:put(Neighbor, UpdatedNeighborList, Adj),
            Adj2 = maps:remove(Leaf, Adj1),
            NewAcc = if length(UpdatedNeighborList) =:= 1 ->
                         [Neighbor | Acc];
                     true -> Acc
                 end,
            process_leaves(Rest, Adj2, NewAcc);
        _Other -> % should not happen in valid tree trimming
            process_leaves(Rest, Adj, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_min_height_trees(n :: integer, edges :: [[integer]]) :: [integer]
  def find_min_height_trees(n, edges) do
    cond do
      n <= 2 ->
        Enum.to_list(0..n - 1)

      true ->
        # build adjacency list and degree map
        adj =
          Enum.reduce(0..(n - 1), %{}, fn i, acc ->
            Map.put(acc, i, [])
          end)

        {adj, degree} =
          Enum.reduce(edges, {adj, %{}}, fn [u, v], {a, d} ->
            a = Map.update!(a, u, &[v | &1])
            a = Map.update!(a, v, &[u | &1])

            d = Map.update(d, u, 1, &(&1 + 1))
            d = Map.update(d, v, 1, &(&1 + 1))

            {a, d}
          end)

        leaves =
          Enum.filter(0..(n - 1), fn i ->
            Map.get(degree, i, 0) == 1
          end)

        trim_leaves(leaves, adj, degree, n)
    end
  end

  defp trim_leaves(leaves, _adj, _degree, remaining) when remaining <= 2 do
    leaves
  end

  defp trim_leaves(leaves, adj, degree, remaining) do
    {new_leaves, new_degree} =
      Enum.reduce(leaves, {[], degree}, fn leaf, {nl, deg} ->
        neighbors = Map.get(adj, leaf, [])

        {nl, deg} =
          Enum.reduce(neighbors, {nl, deg}, fn nb, {acc_nl, acc_deg} ->
            cnt = Map.get(acc_deg, nb)
            cnt = cnt - 1
            acc_deg = Map.put(acc_deg, nb, cnt)

            if cnt == 1 do
              {[nb | acc_nl], acc_deg}
            else
              {acc_nl, acc_deg}
            end
          end)

        {nl, deg}
      end)

    trim_leaves(Enum.reverse(new_leaves), adj, new_degree, remaining - length(leaves))
  end
end
```

# 2685. Count the Number of Complete Components

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> g(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            g[u].push_back(v);
            g[v].push_back(u);
        }
        vector<char> vis(n, false);
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (!vis[i]) {
                int nodes = 0;
                long long degSum = 0;
                stack<int> st;
                st.push(i);
                vis[i] = true;
                while (!st.empty()) {
                    int u = st.top(); st.pop();
                    ++nodes;
                    degSum += g[u].size();
                    for (int v : g[u]) {
                        if (!vis[v]) {
                            vis[v] = true;
                            st.push(v);
                        }
                    }
                }
                long long edgesCount = degSum / 2;
                if (edgesCount == 1LL * nodes * (nodes - 1) / 2)
                    ++ans;
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private int[] parent;
    private int[] size;

    private int find(int x) {
        if (parent[x] == -1) return x;
        parent[x] = find(parent[x]);
        return parent[x];
    }

    private void union(int a, int b) {
        int ra = find(a);
        int rb = find(b);
        if (ra == rb) return;
        if (size[ra] < size[rb]) {
            parent[ra] = rb;
            size[rb] += size[ra];
        } else {
            parent[rb] = ra;
            size[ra] += size[rb];
        }
    }

    public int countCompleteComponents(int n, int[][] edges) {
        parent = new int[n];
        size = new int[n];
        Arrays.fill(parent, -1);
        Arrays.fill(size, 1);

        for (int[] e : edges) {
            union(e[0], e[1]);
        }

        int[] edgeCnt = new int[n];
        for (int[] e : edges) {
            int root = find(e[0]); // same component as e[1]
            edgeCnt[root]++;
        }

        int complete = 0;
        for (int i = 0; i < n; i++) {
            if (parent[i] == -1) { // i is a root
                long expected = (long) size[i] * (size[i] - 1) / 2;
                if (edgeCnt[i] == expected) {
                    complete++;
                }
            }
        }
        return complete;
    }
}
```

## Python

```python
class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(start):
            stack = [start]
            vertices = 0
            edge_sum = 0
            while stack:
                node = stack.pop()
                if visited[node]:
                    continue
                visited[node] = True
                vertices += 1
                edge_sum += len(graph[node])
                for nb in graph[node]:
                    if not visited[nb]:
                        stack.append(nb)
            return vertices, edge_sum

        complete = 0
        for i in range(n):
            if not visited[i]:
                v_cnt, e_cnt = dfs(i)
                if e_cnt == v_cnt * (v_cnt - 1):
                    complete += 1
        return complete
```

## Python3

```python
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        complete = 0

        for i in range(n):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                nodes = 0
                edge_sum = 0
                while stack:
                    node = stack.pop()
                    nodes += 1
                    edge_sum += len(graph[node])
                    for nb in graph[node]:
                        if not visited[nb]:
                            visited[nb] = True
                            stack.append(nb)
                # each edge counted twice, so compare with nodes*(nodes-1)
                if edge_sum == nodes * (nodes - 1):
                    complete += 1

        return complete
```

## C

```c
#include <stdlib.h>

static int find_root(int *parent, int x) {
    if (parent[x] != x)
        parent[x] = find_root(parent, parent[x]);
    return parent[x];
}

static void union_sets(int *parent, int *size, int a, int b) {
    int ra = find_root(parent, a);
    int rb = find_root(parent, b);
    if (ra == rb) return;
    if (size[ra] < size[rb]) {
        parent[ra] = rb;
        size[rb] += size[ra];
    } else {
        parent[rb] = ra;
        size[ra] += size[rb];
    }
}

int countCompleteComponents(int n, int** edges, int edgesSize, int* edgesColSize) {
    int *parent = (int *)malloc(n * sizeof(int));
    int *size   = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        parent[i] = i;
        size[i] = 1;
    }

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        union_sets(parent, size, u, v);
    }

    int *edgeCnt = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int root = find_root(parent, u);
        edgeCnt[root]++;   // each undirected edge counted once
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        if (parent[i] == i) {   // i is a root
            long long expected = (long long)size[i] * (size[i] - 1) / 2;
            if ((long long)edgeCnt[i] == expected)
                ans++;
        }
    }

    free(parent);
    free(size);
    free(edgeCnt);
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int CountCompleteComponents(int n, int[][] edges) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new List<int>();
        }
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            graph[u].Add(v);
            graph[v].Add(u);
        }

        bool[] visited = new bool[n];
        int complete = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                var stack = new Stack<int>();
                stack.Push(i);
                visited[i] = true;
                int vertices = 0;
                long edgeSum = 0;

                while (stack.Count > 0) {
                    int node = stack.Pop();
                    vertices++;
                    edgeSum += graph[node].Count;
                    foreach (int nb in graph[node]) {
                        if (!visited[nb]) {
                            visited[nb] = true;
                            stack.Push(nb);
                        }
                    }
                }

                // In an undirected graph each edge is counted twice.
                if (edgeSum == (long)vertices * (vertices - 1)) {
                    complete++;
                }
            }
        }

        return complete;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countCompleteComponents = function(n, edges) {
    const graph = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }
    const visited = new Array(n).fill(false);
    let complete = 0;
    for (let i = 0; i < n; ++i) {
        if (!visited[i]) {
            const stack = [i];
            visited[i] = true;
            let vertices = 0;
            let degreeSum = 0;
            while (stack.length) {
                const node = stack.pop();
                vertices++;
                degreeSum += graph[node].length;
                for (const nb of graph[node]) {
                    if (!visited[nb]) {
                        visited[nb] = true;
                        stack.push(nb);
                    }
                }
            }
            const edgeCount = degreeSum / 2;
            if (edgeCount === vertices * (vertices - 1) / 2) {
                ++complete;
            }
        }
    }
    return complete;
};
```

## Typescript

```typescript
function countCompleteComponents(n: number, edges: number[][]): number {
    const parent = new Array<number>(n);
    const size = new Array<number>(n).fill(1);
    for (let i = 0; i < n; i++) parent[i] = i;

    function find(x: number): number {
        if (parent[x] !== x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    function union(a: number, b: number): void {
        let ra = find(a);
        let rb = find(b);
        if (ra === rb) return;
        // union by size
        if (size[ra] < size[rb]) {
            [ra, rb] = [rb, ra];
        }
        parent[rb] = ra;
        size[ra] += size[rb];
    }

    for (const [u, v] of edges) {
        union(u, v);
    }

    const edgeCount = new Map<number, number>();
    for (const [u, _] of edges) {
        const root = find(u);
        edgeCount.set(root, (edgeCount.get(root) ?? 0) + 1);
    }

    let complete = 0;
    for (let i = 0; i < n; i++) {
        if (find(i) === i) { // i is a root
            const sz = size[i];
            const expected = (sz * (sz - 1)) / 2;
            const actual = edgeCount.get(i) ?? 0;
            if (actual === expected) complete++;
        }
    }

    return complete;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer
     */
    function countCompleteComponents($n, $edges) {
        // Initialize Union-Find structures
        $parent = [];
        $size   = [];
        for ($i = 0; $i < $n; $i++) {
            $parent[$i] = $i;
            $size[$i]   = 1;
        }

        // Find with path compression
        $find = function($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) {
                $parent[$x] = $find($parent[$x]);
            }
            return $parent[$x];
        };

        // Union by size
        foreach ($edges as $e) {
            $u  = $e[0];
            $v  = $e[1];
            $ru = $find($u);
            $rv = $find($v);
            if ($ru !== $rv) {
                if ($size[$ru] < $size[$rv]) {
                    $parent[$ru] = $rv;
                    $size[$rv]  += $size[$ru];
                } else {
                    $parent[$rv] = $ru;
                    $size[$ru]  += $size[$rv];
                }
            }
        }

        // Count edges per component root
        $edgeCount = [];
        foreach ($edges as $e) {
            $root = $find($e[0]); // both ends share the same root
            if (!isset($edgeCount[$root])) {
                $edgeCount[$root] = 0;
            }
            $edgeCount[$root]++;
        }

        // Determine complete components
        $complete = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($parent[$i] === $i) { // root of a component
                $expected = ($size[$i] * ($size[$i] - 1)) / 2;
                $actual   = $edgeCount[$i] ?? 0;
                if ($expected == $actual) {
                    $complete++;
                }
            }
        }

        return $complete;
    }
}
```

## Swift

```swift
class Solution {
    func countCompleteComponents(_ n: Int, _ edges: [[Int]]) -> Int {
        var graph = Array(repeating: [Int](), count: n)
        for e in edges {
            let u = e[0], v = e[1]
            graph[u].append(v)
            graph[v].append(u)
        }
        var visited = Array(repeating: false, count: n)
        var result = 0

        func dfs(_ start: Int) -> (Int, Int) {
            var stack = [start]
            visited[start] = true
            var vertexCount = 0
            var edgeSum = 0
            while let node = stack.popLast() {
                vertexCount += 1
                edgeSum += graph[node].count
                for neighbor in graph[node] {
                    if !visited[neighbor] {
                        visited[neighbor] = true
                        stack.append(neighbor)
                    }
                }
            }
            return (vertexCount, edgeSum)
        }

        for i in 0..<n {
            if !visited[i] {
                let (vCnt, eSum) = dfs(i)
                if eSum == vCnt * (vCnt - 1) {
                    result += 1
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
    fun countCompleteComponents(n: Int, edges: Array<IntArray>): Int {
        val graph = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            graph[u].add(v)
            graph[v].add(u)
        }
        val visited = BooleanArray(n)
        var complete = 0
        val stack = java.util.ArrayDeque<Int>()
        for (i in 0 until n) {
            if (!visited[i]) {
                var vertices = 0
                var degreeSum = 0
                stack.clear()
                stack.push(i)
                visited[i] = true
                while (!stack.isEmpty()) {
                    val cur = stack.pop()
                    vertices++
                    degreeSum += graph[cur].size
                    for (nbr in graph[cur]) {
                        if (!visited[nbr]) {
                            visited[nbr] = true
                            stack.push(nbr)
                        }
                    }
                }
                val edgesCount = degreeSum / 2
                if (edgesCount == vertices * (vertices - 1) / 2) {
                    complete++
                }
            }
        }
        return complete
    }
}
```

## Dart

```dart
class Solution {
  int countCompleteComponents(int n, List<List<int>> edges) {
    var graph = List.generate(n, (_) => <int>[]);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      graph[u].add(v);
      graph[v].add(u);
    }
    var visited = List.filled(n, false);
    int complete = 0;
    for (int i = 0; i < n; i++) {
      if (!visited[i]) {
        var stack = <int>[];
        stack.add(i);
        int vertices = 0;
        int edgeSum = 0;
        while (stack.isNotEmpty) {
          int node = stack.removeLast();
          if (visited[node]) continue;
          visited[node] = true;
          vertices++;
          edgeSum += graph[node].length;
          for (int nb in graph[node]) {
            if (!visited[nb]) stack.add(nb);
          }
        }
        if (edgeSum == vertices * (vertices - 1)) {
          complete++;
        }
      }
    }
    return complete;
  }
}
```

## Golang

```go
func countCompleteComponents(n int, edges [][]int) int {
    graph := make([][]int, n)
    for _, e := range edges {
        u, v := e[0], e[1]
        graph[u] = append(graph[u], v)
        graph[v] = append(graph[v], u)
    }

    visited := make([]bool, n)
    var dfs func(int) (int, int)
    dfs = func(node int) (int, int) {
        visited[node] = true
        vertices := 1
        edgesCount := len(graph[node])
        for _, nb := range graph[node] {
            if !visited[nb] {
                subV, subE := dfs(nb)
                vertices += subV
                edgesCount += subE
            }
        }
        return vertices, edgesCount
    }

    complete := 0
    for i := 0; i < n; i++ {
        if !visited[i] {
            v, e := dfs(i)
            if e == v*(v-1) {
                complete++
            }
        }
    }
    return complete
}
```

## Ruby

```ruby
def count_complete_components(n, edges)
  graph = Array.new(n) { [] }
  edges.each do |u, v|
    graph[u] << v
    graph[v] << u
  end

  visited = Array.new(n, false)
  complete = 0

  (0...n).each do |i|
    next if visited[i]

    stack = [i]
    visited[i] = true
    vertices = 0
    edge_sum = 0

    until stack.empty?
      node = stack.pop
      vertices += 1
      edge_sum += graph[node].size
      graph[node].each do |nbr|
        next if visited[nbr]

        visited[nbr] = true
        stack << nbr
      end
    end

    complete += 1 if edge_sum == vertices * (vertices - 1)
  end

  complete
end
```

## Scala

```scala
object Solution {
    def countCompleteComponents(n: Int, edges: Array[Array[Int]]): Int = {
        class UnionFind(val n: Int) {
            val parent: Array[Int] = (0 until n).toArray
            val size: Array[Int] = Array.fill(n)(1)

            def find(x: Int): Int = {
                if (parent(x) != x) parent(x) = find(parent(x))
                parent(x)
            }

            def union(a: Int, b: Int): Unit = {
                var ra = find(a)
                var rb = find(b)
                if (ra == rb) return
                if (size(ra) < size(rb)) {
                    val tmp = ra
                    ra = rb
                    rb = tmp
                }
                parent(rb) = ra
                size(ra) += size(rb)
            }
        }

        val uf = new UnionFind(n)

        for (e <- edges) {
            uf.union(e(0), e(1))
        }

        import scala.collection.mutable
        val edgeCount = mutable.Map[Int, Int]().withDefaultValue(0)

        for (e <- edges) {
            val root = uf.find(e(0))
            edgeCount(root) = edgeCount(root) + 1
        }

        var ans = 0
        for (i <- 0 until n) {
            if (uf.find(i) == i) {
                val sz = uf.size(i)
                val expected = sz * (sz - 1) / 2
                val actual = edgeCount.getOrElse(i, 0)
                if (expected == actual) ans += 1
            }
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_complete_components(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n_usize = n as usize;
        let mut graph: Vec<Vec<usize>> = vec![Vec::new(); n_usize];
        for e in edges.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            graph[a].push(b);
            graph[b].push(a);
        }
        let mut visited = vec![false; n_usize];
        let mut result = 0i32;

        fn dfs(
            u: usize,
            graph: &Vec<Vec<usize>>,
            visited: &mut Vec<bool>,
            vertices: &mut i32,
            edge_sum: &mut i32,
        ) {
            visited[u] = true;
            *vertices += 1;
            *edge_sum += graph[u].len() as i32;
            for &v in &graph[u] {
                if !visited[v] {
                    dfs(v, graph, visited, vertices, edge_sum);
                }
            }
        }

        for i in 0..n_usize {
            if !visited[i] {
                let mut vertices = 0i32;
                let mut edge_sum = 0i32;
                dfs(i, &graph, &mut visited, &mut vertices, &mut edge_sum);
                if edge_sum == vertices * (vertices - 1) {
                    result += 1;
                }
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (count-complete-components n edges)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ([graph (make-vector n '())]
         [_ (for-each
              (lambda (e)
                (let ([u (first e)] [v (second e)])
                  (vector-set! graph u (cons v (vector-ref graph u)))
                  (vector-set! graph v (cons u (vector-ref graph v)))))
              edges)]
         [visited (make-vector n #f)])
    (let loop ((i 0) (ans 0))
      (if (= i n)
          ans
          (if (vector-ref visited i)
              (loop (+ i 1) ans)
              (let dfs ([stack (list i)] [vert-count 0] [edge-count 0])
                (if (null? stack)
                    (let ([expected (* vert-count (- vert-count 1))])
                      (loop (+ i 1) (if (= edge-count expected) (+ ans 1) ans)))
                    (let* ([node (car stack)]
                           [rest (cdr stack)])
                      (if (vector-ref visited node)
                          (dfs rest vert-count edge-count)
                          (begin
                            (vector-set! visited node #t)
                            (define neighbors (vector-ref graph node))
                            (dfs (append neighbors rest)
                                 (+ vert-count 1)
                                 (+ edge-count (length neighbors)))))))))))))
```

## Erlang

```erlang
-spec count_complete_components(integer(), [[integer()]]) -> integer().
count_complete_components(N, Edges) ->
    Adj0 = maps:from_list([{I, []} || I <- lists:seq(0, N - 1)]),
    Adj = build_adj(Edges, Adj0),
    {Count, _} = count_components(lists:seq(0, N - 1), Adj, #{}, 0),
    Count.

build_adj([], Adj) -> Adj;
build_adj([[U, V] | Rest], Adj) ->
    Adj1 = add_neighbor(add_neighbor(Adj, U, V), V, U),
    build_adj(Rest, Adj1).

add_neighbor(Adj, Node, Neighbor) ->
    Old = maps:get(Node, Adj, []),
    New = [Neighbor | Old],
    maps:put(Node, New, Adj).

count_components([], _Adj, Visited, Count) -> {Count, Visited};
count_components([V | Vs], Adj, Visited, Count) ->
    case maps:is_key(V, Visited) of
        true ->
            count_components(Vs, Adj, Visited, Count);
        false ->
            {NewVisited, Vcnt, EdgeSum} = dfs(V, Adj, Visited),
            NewCount = if EdgeSum == Vcnt * (Vcnt - 1) -> Count + 1; true -> Count end,
            count_components(Vs, Adj, NewVisited, NewCount)
    end.

dfs(Start, Adj, Visited) ->
    dfs_stack([Start], Adj, Visited, 0, 0).

dfs_stack([], _Adj, Visited, VCount, EdgeSum) ->
    {Visited, VCount, EdgeSum};
dfs_stack([Node | RestStack], Adj, Visited, VCount, EdgeSum) ->
    case maps:is_key(Node, Visited) of
        true ->
            dfs_stack(RestStack, Adj, Visited, VCount, EdgeSum);
        false ->
            NewVisited = maps:put(Node, true, Visited),
            Neighs = maps:get(Node, Adj, []),
            NewVCount = VCount + 1,
            NewEdgeSum = EdgeSum + length(Neighs),
            NewStack = RestStack ++ Neighs,
            dfs_stack(NewStack, Adj, NewVisited, NewVCount, NewEdgeSum)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_complete_components(n :: integer, edges :: [[integer]]) :: integer
  def count_complete_components(n, edges) do
    # Build adjacency list
    graph =
      Enum.reduce(0..(n - 1), %{}, fn i, acc -> Map.put(acc, i, []) end)
      |> Enum.reduce(edges, fn [u, v], acc ->
        acc
        |> Map.update!(u, fn lst -> [v | lst] end)
        |> Map.update!(v, fn lst -> [u | lst] end)
      end)

    {complete_cnt, _visited} =
      Enum.reduce(0..(n - 1), {0, MapSet.new()}, fn node, {cnt, visited} ->
        if MapSet.member?(visited, node) do
          {cnt, visited}
        else
          {new_visited, vcnt, esum} = dfs([node], graph, visited, 0, 0)

          if esum == vcnt * (vcnt - 1) do
            {cnt + 1, new_visited}
          else
            {cnt, new_visited}
          end
        end
      end)

    complete_cnt
  end

  defp dfs([], _graph, visited, vcnt, esum), do: {visited, vcnt, esum}

  defp dfs([cur | stack], graph, visited, vcnt, esum) do
    if MapSet.member?(visited, cur) do
      dfs(stack, graph, visited, vcnt, esum)
    else
      visited = MapSet.put(visited, cur)
      neigh = Map.get(graph, cur, [])
      new_esum = esum + length(neigh)

      {new_visited, new_stack} =
        Enum.reduce(neigh, {visited, stack}, fn nb, {vis_acc, stk_acc} ->
          if MapSet.member?(vis_acc, nb) do
            {vis_acc, stk_acc}
          else
            {MapSet.put(vis_acc, nb), [nb | stk_acc]}
          end
        end)

      dfs(new_stack, graph, new_visited, vcnt + 1, new_esum)
    end
  end
end
```

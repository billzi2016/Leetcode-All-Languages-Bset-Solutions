# 1443. Minimum Time to Collect All Apples in a Tree

## Cpp

```cpp
class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        vector<vector<int>> g(n);
        for (auto &e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        function<int(int,int)> dfs = [&](int u, int p) -> int {
            int time = 0;
            for (int v : g[u]) {
                if (v == p) continue;
                int childTime = dfs(v, u);
                if (childTime > 0 || hasApple[v]) {
                    time += childTime + 2;
                }
            }
            return time;
        };
        return dfs(0, -1);
    }
};
```

## Java

```java
class Solution {
    public int minTime(int n, int[][] edges, List<Boolean> hasApple) {
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        boolean[] apple = new boolean[n];
        for (int i = 0; i < n; i++) {
            apple[i] = hasApple.get(i);
        }
        return dfs(0, -1, graph, apple);
    }

    private int dfs(int node, int parent, List<Integer>[] graph, boolean[] apple) {
        int total = 0;
        for (int nei : graph[node]) {
            if (nei == parent) continue;
            int childTime = dfs(nei, node, graph, apple);
            if (childTime > 0 || apple[nei]) {
                total += childTime + 2;
            }
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        from collections import defaultdict
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        import sys
        sys.setrecursionlimit(2000000)

        def dfs(node, parent):
            total = 0
            for nei in adj[node]:
                if nei == parent:
                    continue
                child_time = dfs(nei, node)
                if child_time > 0 or hasApple[nei]:
                    total += child_time + 2
            return total

        return dfs(0, -1)
```

## Python3

```python
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        import sys
        sys.setrecursionlimit(2000000)

        def dfs(node: int, parent: int) -> int:
            total = 0
            for nei in graph[node]:
                if nei == parent:
                    continue
                child_time = dfs(nei, node)
                if child_time > 0 or hasApple[nei]:
                    total += child_time + 2
            return total

        return dfs(0, -1)
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

static int **adjList;
static int *degArr;
static bool *apple;

static int dfs(int node, int parent) {
    int total = 0;
    for (int i = 0; i < degArr[node]; ++i) {
        int nb = adjList[node][i];
        if (nb == parent) continue;
        int childTime = dfs(nb, node);
        if (childTime > 0 || apple[nb]) {
            total += childTime + 2; // go to child and return
        }
    }
    return total;
}

int minTime(int n, int** edges, int edgesSize, int* edgesColSize, bool* hasApple, int hasAppleSize) {
    (void)edgesColSize; // unused
    apple = hasApple;

    degArr = calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        degArr[a]++;
        degArr[b]++;
    }

    adjList = malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        adjList[i] = malloc(degArr[i] * sizeof(int));
    }

    int *idx = calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        adjList[a][idx[a]++] = b;
        adjList[b][idx[b]++] = a;
    }
    free(idx);

    int result = dfs(0, -1);
    // cleanup (optional)
    for (int i = 0; i < n; ++i) {
        free(adjList[i]);
    }
    free(adjList);
    free(degArr);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinTime(int n, int[][] edges, IList<bool> hasApple) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            graph[a].Add(b);
            graph[b].Add(a);
        }

        return Dfs(0, -1);

        int Dfs(int node, int parent) {
            int total = 0;
            foreach (int nei in graph[node]) {
                if (nei == parent) continue;
                int childTime = Dfs(nei, node);
                if (childTime > 0 || hasApple[nei]) {
                    total += childTime + 2; // go to child and back
                }
            }
            return total;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {boolean[]} hasApple
 * @return {number}
 */
var minTime = function(n, edges, hasApple) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    const dp = new Array(n).fill(0);
    const stack = [{ node: 0, parent: -1, visited: false }];
    while (stack.length) {
        const { node, parent, visited } = stack.pop();
        if (!visited) {
            stack.push({ node, parent, visited: true });
            for (const nei of adj[node]) {
                if (nei !== parent) stack.push({ node: nei, parent: node, visited: false });
            }
        } else {
            let sum = 0;
            for (const nei of adj[node]) {
                if (nei === parent) continue;
                if (dp[nei] > 0 || hasApple[nei]) sum += dp[nei] + 2;
            }
            dp[node] = sum;
        }
    }
    return dp[0];
};
```

## Typescript

```typescript
function minTime(n: number, edges: number[][], hasApple: boolean[]): number {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const subHasApple = new Array<boolean>(n).fill(false);
    let total = 0;
    const stack: [number, number, boolean][] = [[0, -1, false]]; // node, parent, processed flag

    while (stack.length) {
        const [node, parent, processed] = stack.pop()!;
        if (!processed) {
            stack.push([node, parent, true]); // will process after children
            for (const nei of adj[node]) {
                if (nei !== parent) {
                    stack.push([nei, node, false]);
                }
            }
        } else {
            let need = hasApple[node];
            for (const nei of adj[node]) {
                if (nei === parent) continue;
                if (subHasApple[nei]) {
                    total += 2; // go to child and back
                    need = true;
                }
            }
            subHasApple[node] = need;
        }
    }

    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Boolean[] $hasApple
     * @return Integer
     */
    function minTime($n, $edges, $hasApple) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            $graph[$a][] = $b;
            $graph[$b][] = $a;
        }

        $dfs = function($node, $parent) use (&$dfs, &$graph, $hasApple) {
            $time = 0;
            foreach ($graph[$node] as $nei) {
                if ($nei === $parent) continue;
                $childTime = $dfs($nei, $node);
                if ($childTime > 0 || $hasApple[$nei]) {
                    $time += $childTime + 2;
                }
            }
            return $time;
        };

        return $dfs(0, -1);
    }
}
```

## Swift

```swift
class Solution {
    func minTime(_ n: Int, _ edges: [[Int]], _ hasApple: [Bool]) -> Int {
        var graph = [[Int]](repeating: [], count: n)
        for e in edges {
            let a = e[0], b = e[1]
            graph[a].append(b)
            graph[b].append(a)
        }
        
        var parent = [Int](repeating: -1, count: n)
        var order = [Int]()
        var stack = [Int]()
        stack.append(0)
        parent[0] = -2  // mark root
        
        while let node = stack.popLast() {
            order.append(node)
            for nb in graph[node] {
                if nb == parent[node] { continue }
                parent[nb] = node
                stack.append(nb)
            }
        }
        
        var time = [Int](repeating: 0, count: n)
        for node in order.reversed() {
            var sum = 0
            for nb in graph[node] {
                if parent[nb] == node { // child
                    if time[nb] > 0 || hasApple[nb] {
                        sum += time[nb] + 2
                    }
                }
            }
            time[node] = sum
        }
        
        return time[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minTime(n: Int, edges: Array<IntArray>, hasApple: List<Boolean>): Int {
        val graph = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val a = e[0]
            val b = e[1]
            graph[a].add(b)
            graph[b].add(a)
        }

        fun dfs(node: Int, parent: Int): Int {
            var total = 0
            for (nei in graph[node]) {
                if (nei == parent) continue
                val childTime = dfs(nei, node)
                if (childTime > 0 || hasApple[nei]) {
                    total += childTime + 2
                }
            }
            return total
        }

        return dfs(0, -1)
    }
}
```

## Dart

```dart
class Solution {
  int minTime(int n, List<List<int>> edges, List<bool> hasApple) {
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int a = e[0];
      int b = e[1];
      adj[a].add(b);
      adj[b].add(a);
    }

    int dfs(int node, int parent) {
      int total = 0;
      for (int nei in adj[node]) {
        if (nei == parent) continue;
        int childTime = dfs(nei, node);
        if (childTime > 0 || hasApple[nei]) {
          total += childTime + 2;
        }
      }
      return total;
    }

    return dfs(0, -1);
  }
}
```

## Golang

```go
func minTime(n int, edges [][]int, hasApple []bool) int {
    g := make([][]int, n)
    for _, e := range edges {
        a, b := e[0], e[1]
        g[a] = append(g[a], b)
        g[b] = append(g[b], a)
    }
    var dfs func(int, int) int
    dfs = func(node, parent int) int {
        total := 0
        for _, nb := range g[node] {
            if nb == parent {
                continue
            }
            childCost := dfs(nb, node)
            if childCost > 0 || hasApple[nb] {
                total += childCost + 2
            }
        }
        return total
    }
    return dfs(0, -1)
}
```

## Ruby

```ruby
def min_time(n, edges, has_apple)
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  has = has_apple.map { |x| x }
  times = Array.new(n, 0)

  stack = [[0, -1, false]]
  until stack.empty?
    node, parent, processed = stack.pop
    if processed
      adj[node].each do |nbr|
        next if nbr == parent
        if has[nbr]
          times[node] += times[nbr] + 2
          has[node] = true
        end
      end
    else
      stack << [node, parent, true]
      adj[node].each do |nbr|
        next if nbr == parent
        stack << [nbr, node, false]
      end
    end
  end

  times[0]
end
```

## Scala

```scala
object Solution {
    def minTime(n: Int, edges: Array[Array[Int]], hasApple: List[Boolean]): Int = {
        if (n == 1) return 0
        val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
        for (e <- edges) {
            val a = e(0)
            val b = e(1)
            adj(a) += b
            adj(b) += a
        }
        val parent = Array.fill[Int](n)(-1)
        val order = new scala.collection.mutable.ArrayBuffer[Int]()
        val stack = new scala.collection.mutable.Stack[Int]()
        stack.push(0)
        parent(0) = -2 // root marker
        while (stack.nonEmpty) {
            val node = stack.pop()
            order += node
            for (nei <- adj(node)) {
                if (parent(nei) == -1) {
                    parent(nei) = node
                    stack.push(nei)
                }
            }
        }
        val need = Array.fill[Int](n)(0)
        for (node <- order.reverse) {
            var sum = 0
            for (nei <- adj(node)) {
                if (parent(nei) == node) { // child
                    sum += need(nei)
                    if (need(nei) > 0 || hasApple(nei)) sum += 2
                }
            }
            need(node) = sum
        }
        need(0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_time(n: i32, edges: Vec<Vec<i32>>, has_apple: Vec<bool>) -> i32 {
        let n_usize = n as usize;
        let mut adj = vec![Vec::new(); n_usize];
        for e in edges.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }

        fn dfs(node: usize, parent: usize, adj: &Vec<Vec<usize>>, has_apple: &Vec<bool>) -> i32 {
            let mut total = 0;
            for &child in &adj[node] {
                if child == parent {
                    continue;
                }
                let child_time = dfs(child, node, adj, has_apple);
                if child_time > 0 || has_apple[child] {
                    total += child_time + 2;
                }
            }
            total
        }

        dfs(0, n_usize, &adj, &has_apple) as i32
    }
}
```

## Racket

```racket
(define/contract (min-time n edges hasApple)
  (-> exact-integer? (listof (listof exact-integer?)) (listof boolean?) exact-integer?)
  (let* ((adj (make-vector n '()))
         (apple-vec (list->vector hasApple)))
    ;; build adjacency list
    (for ([e edges])
      (define a (car e))
      (define b (cadr e))
      (vector-set! adj a (cons b (vector-ref adj a)))
      (vector-set! adj b (cons a (vector-ref adj b))))
    (letrec ((dfs (lambda (node parent)
                    (let ((total 0))
                      (for ([nbr (vector-ref adj node)])
                        (when (not (= nbr parent))
                          (define child-cost (dfs nbr node))
                          (when (or (> child-cost 0) (vector-ref apple-vec nbr))
                            (set! total (+ total child-cost 2)))))
                      total))))
      (dfs 0 -1))))
```

## Erlang

```erlang
-module(solution).
-export([min_time/3]).

-spec min_time(N :: integer(), Edges :: [[integer()]], HasApple :: [boolean()]) -> integer().
min_time(N, Edges, HasApple) ->
    Adj = build_adj(N, Edges),
    AppleMap = maps:from_list(lists:zip(lists:seq(0, N - 1), HasApple)),
    SubInfo = dfs([{0, -1, false}], Adj, AppleMap, #{}),
    {Time, _} = maps:get(0, SubInfo),
    Time.

%% Build adjacency map
build_adj(N, Edges) ->
    EmptyAdj = maps:from_list([{I, []} || I <- lists:seq(0, N - 1)]),
    add_edges(Edges, EmptyAdj).

add_edges([], Adj) -> Adj;
add_edges([[A, B] | Rest], Adj) ->
    Adj1 = maps:update_with(A,
            fun(L) -> [B | L] end,
            [B],
            Adj),
    Adj2 = maps:update_with(B,
            fun(L) -> [A | L] end,
            [A],
            Adj1),
    add_edges(Rest, Adj2).

%% Depth‑first search using explicit stack (post‑order)
dfs([], _Adj, _AppleMap, SubInfo) ->
    SubInfo;
dfs([{Node, Parent, false} | Rest], Adj, AppleMap, SubInfo) ->
    Children = maps:get(Node, Adj),
    % push node again marked as visited, then its children
    NewStack = [{Node, Parent, true} | Rest],
    ChildFrames = [{Child, Node, false}
                    || Child <- Children,
                       Child =/= Parent],
    dfs(ChildFrames ++ NewStack, Adj, AppleMap, SubInfo);
dfs([{Node, _Parent, true} | Rest], Adj, AppleMap, SubInfo) ->
    Children = maps:get(Node, Adj),
    {TimeAcc, HasAppleSub} =
        lists:foldl(
            fun(Child, {TA, HA}) ->
                case maps:get(Child, SubInfo) of
                    {CTime, true} -> {TA + CTime + 2, true};
                    _ -> {TA, HA}
                end
            end,
            {0, maps:get(Node, AppleMap)},
            Children),
    NewSubInfo = maps:put(Node, {TimeAcc, HasAppleSub}, SubInfo),
    dfs(Rest, Adj, AppleMap, NewSubInfo).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_time(integer, [[integer]], [boolean]) :: integer
  def min_time(_n, edges, has_apple) do
    adj = build_adj(edges)
    apples = List.to_tuple(has_apple)
    dfs(0, -1, adj, apples)
  end

  defp build_adj(edges) do
    Enum.reduce(edges, %{}, fn [a, b], acc ->
      acc
      |> Map.update(a, [b], &[b | &1])
      |> Map.update(b, [a], &[a | &1])
    end)
  end

  defp dfs(node, parent, adj, apples) do
    children = Map.get(adj, node, [])
    Enum.reduce(children, 0, fn child, acc ->
      if child != parent do
        sub = dfs(child, node, adj, apples)
        need = sub > 0 or elem(apples, child)

        if need do
          acc + sub + 2
        else
          acc
        end
      else
        acc
      end
    end)
  end
end
```

# 3310. Remove Methods From Project

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        vector<vector<int>> adj(n);
        for (const auto& e : invocations) {
            adj[e[0]].push_back(e[1]);
        }
        vector<char> suspicious(n, 0);
        // DFS/BFS from k
        stack<int> st;
        st.push(k);
        suspicious[k] = 1;
        while (!st.empty()) {
            int u = st.top(); st.pop();
            for (int v : adj[u]) {
                if (!suspicious[v]) {
                    suspicious[v] = 1;
                    st.push(v);
                }
            }
        }
        // Check for incoming edges from outside
        for (const auto& e : invocations) {
            int u = e[0], v = e[1];
            if (suspicious[v] && !suspicious[u]) {
                vector<int> all(n);
                iota(all.begin(), all.end(), 0);
                return all;
            }
        }
        // Removal possible: return non-suspicious nodes
        vector<int> res;
        for (int i = 0; i < n; ++i) {
            if (!suspicious[i]) res.push_back(i);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public List<Integer> remainingMethods(int n, int k, int[][] invocations) {
        List<List<Integer>> adj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : invocations) {
            adj.get(e[0]).add(e[1]);
        }

        boolean[] suspicious = new boolean[n];
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(k);
        while (!stack.isEmpty()) {
            int node = stack.pop();
            if (suspicious[node]) continue;
            suspicious[node] = true;
            for (int nb : adj.get(node)) {
                if (!suspicious[nb]) stack.push(nb);
            }
        }

        boolean canRemove = true;
        for (int[] e : invocations) {
            int a = e[0], b = e[1];
            if (suspicious[b] && !suspicious[a]) {
                canRemove = false;
                break;
            }
        }

        List<Integer> result = new ArrayList<>();
        if (!canRemove) {
            for (int i = 0; i < n; i++) result.add(i);
        } else {
            for (int i = 0; i < n; i++) {
                if (!suspicious[i]) result.add(i);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(n)]
        for a, b in invocations:
            adj[a].append(b)

        # Find all methods reachable from k (suspicious set)
        visited = [False] * n
        stack = [k]
        visited[k] = True
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)

        # Check for incoming edges from outside the suspicious set
        for a, b in invocations:
            if visited[b] and not visited[a]:
                return list(range(n))

        # Return methods that are not suspicious
        return [i for i in range(n) if not visited[i]]
```

## Python3

```python
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for a, b in invocations:
            adj[a].append(b)

        visited = [False] * n
        stack = [k]
        visited[k] = True
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)

        for a, b in invocations:
            if visited[b] and not visited[a]:
                return list(range(n))

        return [i for i, v in enumerate(visited) if not v]
```

## C

```c
/****
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* remainingMethods(int n, int k, int** invocations, int invocationsSize,
                      int* invocationsColSize, int* returnSize) {
    // Count out-degree for each node
    int *outDeg = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < invocationsSize; ++i) {
        int a = invocations[i][0];
        outDeg[a]++;
    }

    // Prefix sum to get start indices in flat neighbor array
    int *startIdx = (int*)malloc((n + 1) * sizeof(int));
    startIdx[0] = 0;
    for (int i = 0; i < n; ++i) {
        startIdx[i + 1] = startIdx[i] + outDeg[i];
    }
    int totalEdges = invocationsSize;
    int *neighbors = (int*)malloc(totalEdges * sizeof(int));

    // Temporary positions while filling neighbors
    int *pos = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) pos[i] = startIdx[i];

    for (int i = 0; i < invocationsSize; ++i) {
        int a = invocations[i][0];
        int b = invocations[i][1];
        neighbors[pos[a]++] = b;
    }

    // DFS/BFS from k to find suspicious set
    char *vis = (char*)calloc(n, sizeof(char));
    int *stack = (int*)malloc(n * sizeof(int));
    int top = 0;
    stack[top++] = k;
    vis[k] = 1;

    while (top) {
        int u = stack[--top];
        for (int idx = startIdx[u]; idx < startIdx[u + 1]; ++idx) {
            int v = neighbors[idx];
            if (!vis[v]) {
                vis[v] = 1;
                stack[top++] = v;
            }
        }
    }

    // Check for incoming edges from outside the suspicious set
    int canRemove = 1;
    for (int i = 0; i < invocationsSize; ++i) {
        int a = invocations[i][0];
        int b = invocations[i][1];
        if (vis[b] && !vis[a]) {
            canRemove = 0;
            break;
        }
    }

    // Prepare result
    int *result;
    if (!canRemove) {
        *returnSize = n;
        result = (int*)malloc(n * sizeof(int));
        for (int i = 0; i < n; ++i) result[i] = i;
    } else {
        int cnt = 0;
        for (int i = 0; i < n; ++i) if (!vis[i]) cnt++;
        *returnSize = cnt;
        result = (int*)malloc(cnt * sizeof(int));
        int idx = 0;
        for (int i = 0; i < n; ++i) {
            if (!vis[i]) result[idx++] = i;
        }
    }

    // Clean up auxiliary memory
    free(outDeg);
    free(startIdx);
    free(neighbors);
    free(pos);
    free(vis);
    free(stack);

    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> RemainingMethods(int n, int k, int[][] invocations) {
        var adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in invocations) {
            adj[e[0]].Add(e[1]);
        }

        var suspicious = new bool[n];
        var stack = new Stack<int>();
        stack.Push(k);
        suspicious[k] = true;
        while (stack.Count > 0) {
            int u = stack.Pop();
            foreach (int v in adj[u]) {
                if (!suspicious[v]) {
                    suspicious[v] = true;
                    stack.Push(v);
                }
            }
        }

        bool canRemove = true;
        foreach (var e in invocations) {
            int a = e[0], b = e[1];
            if (suspicious[b] && !suspicious[a]) {
                canRemove = false;
                break;
            }
        }

        var result = new List<int>();
        if (canRemove) {
            for (int i = 0; i < n; i++) {
                if (!suspicious[i]) result.Add(i);
            }
        } else {
            for (int i = 0; i < n; i++) result.Add(i);
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @param {number[][]} invocations
 * @return {number[]}
 */
var remainingMethods = function(n, k, invocations) {
    const adj = Array.from({ length: n }, () => []);
    for (const [a, b] of invocations) {
        adj[a].push(b);
    }

    // Find all suspicious methods reachable from k
    const suspicious = new Uint8Array(n);
    const stack = [k];
    suspicious[k] = 1;
    while (stack.length) {
        const u = stack.pop();
        for (const v of adj[u]) {
            if (!suspicious[v]) {
                suspicious[v] = 1;
                stack.push(v);
            }
        }
    }

    // Check if any outside method calls a suspicious one
    let hasIncoming = false;
    for (const [a, b] of invocations) {
        if (suspicious[b] && !suspicious[a]) {
            hasIncoming = true;
            break;
        }
    }

    if (hasIncoming) {
        // Cannot remove anything; return all methods
        const all = new Array(n);
        for (let i = 0; i < n; ++i) all[i] = i;
        return all;
    } else {
        // Return methods that are not suspicious
        const res = [];
        for (let i = 0; i < n; ++i) {
            if (!suspicious[i]) res.push(i);
        }
        return res;
    }
};
```

## Typescript

```typescript
function remainingMethods(n: number, k: number, invocations: number[][]): number[] {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of invocations) {
        adj[a].push(b);
    }

    const visited = new Uint8Array(n);
    const stack: number[] = [k];
    visited[k] = 1;

    while (stack.length) {
        const u = stack.pop()!;
        for (const v of adj[u]) {
            if (!visited[v]) {
                visited[v] = 1;
                stack.push(v);
            }
        }
    }

    let canRemove = true;
    for (const [a, b] of invocations) {
        if (visited[b] && !visited[a]) {
            canRemove = false;
            break;
        }
    }

    const result: number[] = [];
    if (canRemove) {
        for (let i = 0; i < n; ++i) {
            if (!visited[i]) result.push(i);
        }
    } else {
        for (let i = 0; i < n; ++i) result.push(i);
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer[][] $invocations
     * @return Integer[]
     */
    function remainingMethods($n, $k, $invocations) {
        // Build adjacency list for outgoing edges
        $adj = array_fill(0, $n, []);
        foreach ($invocations as $edge) {
            $a = $edge[0];
            $b = $edge[1];
            $adj[$a][] = $b;
        }

        // Find all suspicious methods reachable from k
        $suspicious = array_fill(0, $n, false);
        $stack = [$k];
        while (!empty($stack)) {
            $node = array_pop($stack);
            if ($suspicious[$node]) continue;
            $suspicious[$node] = true;
            foreach ($adj[$node] as $nbr) {
                if (!$suspicious[$nbr]) {
                    $stack[] = $nbr;
                }
            }
        }

        // Check for incoming edges from non‑suspicious to suspicious methods
        foreach ($invocations as $edge) {
            $from = $edge[0];
            $to   = $edge[1];
            if ($suspicious[$to] && !$suspicious[$from]) {
                // Cannot remove; return all methods
                return range(0, $n - 1);
            }
        }

        // Removal is possible: return methods not in the suspicious set
        $remaining = [];
        for ($i = 0; $i < $n; $i++) {
            if (!$suspicious[$i]) {
                $remaining[] = $i;
            }
        }
        return $remaining;
    }
}
```

## Swift

```swift
class Solution {
    func remainingMethods(_ n: Int, _ k: Int, _ invocations: [[Int]]) -> [Int] {
        var adj = [[Int]](repeating: [], count: n)
        for edge in invocations {
            let a = edge[0]
            let b = edge[1]
            adj[a].append(b)
        }
        
        var suspicious = [Bool](repeating: false, count: n)
        var stack = [Int]()
        stack.append(k)
        suspicious[k] = true
        
        while let node = stack.popLast() {
            for nb in adj[node] {
                if !suspicious[nb] {
                    suspicious[nb] = true
                    stack.append(nb)
                }
            }
        }
        
        // Check for incoming edges from non‑suspicious to suspicious nodes
        for edge in invocations {
            let a = edge[0]
            let b = edge[1]
            if !suspicious[a] && suspicious[b] {
                var all = [Int]()
                all.reserveCapacity(n)
                for i in 0..<n { all.append(i) }
                return all
            }
        }
        
        var result = [Int]()
        result.reserveCapacity(n)
        for i in 0..<n where !suspicious[i] {
            result.append(i)
        }
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun remainingMethods(n: Int, k: Int, invocations: Array<IntArray>): List<Int> {
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in invocations) {
            adj[e[0]].add(e[1])
        }

        val suspicious = BooleanArray(n)
        val queue: ArrayDeque<Int> = ArrayDeque()
        queue.add(k)
        suspicious[k] = true
        while (!queue.isEmpty()) {
            val u = queue.poll()
            for (v in adj[u]) {
                if (!suspicious[v]) {
                    suspicious[v] = true
                    queue.add(v)
                }
            }
        }

        var canRemove = true
        loop@ for (e in invocations) {
            val a = e[0]
            val b = e[1]
            if (!suspicious[a] && suspicious[b]) {
                canRemove = false
                break@loop
            }
        }

        val res = ArrayList<Int>()
        if (canRemove) {
            for (i in 0 until n) {
                if (!suspicious[i]) res.add(i)
            }
        } else {
            for (i in 0 until n) res.add(i)
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> remainingMethods(int n, int k, List<List<int>> invocations) {
    // Build adjacency list for outgoing edges
    List<List<int>> graph = List.generate(n, (_) => []);
    for (var e in invocations) {
      int a = e[0];
      int b = e[1];
      graph[a].add(b);
    }

    // Find all suspicious methods reachable from k
    List<bool> suspicious = List.filled(n, false);
    List<int> stack = [k];
    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      if (suspicious[node]) continue;
      suspicious[node] = true;
      for (int nb in graph[node]) {
        if (!suspicious[nb]) stack.add(nb);
      }
    }

    // Check for any incoming edge from outside the suspicious set
    for (var e in invocations) {
      int a = e[0];
      int b = e[1];
      if (!suspicious[a] && suspicious[b]) {
        // Cannot remove; return all methods
        return List<int>.generate(n, (i) => i);
      }
    }

    // Removal is possible: return methods not in the suspicious set
    List<int> result = [];
    for (int i = 0; i < n; ++i) {
      if (!suspicious[i]) result.add(i);
    }
    return result;
  }
}
```

## Golang

```go
func remainingMethods(n int, k int, invocations [][]int) []int {
    // Build adjacency list for forward traversal
    graph := make([][]int, n)
    for _, e := range invocations {
        a, b := e[0], e[1]
        graph[a] = append(graph[a], b)
    }

    // Find all methods reachable from k (suspicious set)
    visited := make([]bool, n)
    stack := []int{k}
    visited[k] = true
    for len(stack) > 0 {
        v := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        for _, nb := range graph[v] {
            if !visited[nb] {
                visited[nb] = true
                stack = append(stack, nb)
            }
        }
    }

    // Check if any external method invokes a suspicious one
    for _, e := range invocations {
        a, b := e[0], e[1]
        if visited[b] && !visited[a] {
            // Cannot remove; return all methods
            res := make([]int, n)
            for i := 0; i < n; i++ {
                res[i] = i
            }
            return res
        }
    }

    // Removal possible: return non‑suspicious methods
    res := []int{}
    for i := 0; i < n; i++ {
        if !visited[i] {
            res = append(res, i)
        }
    }
    return res
}
```

## Ruby

```ruby
def remaining_methods(n, k, invocations)
  adj = Array.new(n) { [] }
  invocations.each do |a, b|
    adj[a] << b
  end

  visited = Array.new(n, false)
  stack = [k]
  until stack.empty?
    node = stack.pop
    next if visited[node]
    visited[node] = true
    adj[node].each { |nbr| stack << nbr unless visited[nbr] }
  end

  invocations.each do |a, b|
    if visited[b] && !visited[a]
      return (0...n).to_a
    end
  end

  result = []
  (0...n).each { |i| result << i unless visited[i] }
  result
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{ListBuffer, Stack}
  def remainingMethods(n: Int, k: Int, invocations: Array[Array[Int]]): List[Int] = {
    val adj = Array.fill[ListBuffer[Int]](n)(new ListBuffer[Int])
    for (e <- invocations) {
      adj(e(0)) += e(1)
    }
    val visited = new Array[Boolean](n)
    val stack = Stack[Int]()
    stack.push(k)
    while (stack.nonEmpty) {
      val u = stack.pop()
      if (!visited(u)) {
        visited(u) = true
        for (v <- adj(u)) {
          if (!visited(v)) stack.push(v)
        }
      }
    }
    var canRemove = true
    var idx = 0
    while (idx < invocations.length && canRemove) {
      val a = invocations(idx)(0)
      val b = invocations(idx)(1)
      if (!visited(a) && visited(b)) canRemove = false
      idx += 1
    }
    if (!canRemove) {
      (0 until n).toList
    } else {
      val res = ListBuffer[Int]()
      for (i <- 0 until n) if (!visited(i)) res += i
      res.toList
    }
  }
}
```

## Rust

```rust
impl Solution {
    pub fn remaining_methods(n: i32, k: i32, invocations: Vec<Vec<i32>>) -> Vec<i32> {
        let n_usize = n as usize;
        let k_usize = k as usize;

        // Build adjacency list
        let mut graph: Vec<Vec<usize>> = vec![Vec::new(); n_usize];
        for edge in &invocations {
            let a = edge[0] as usize;
            let b = edge[1] as usize;
            graph[a].push(b);
        }

        // Find all methods reachable from k (suspicious set)
        let mut visited = vec![false; n_usize];
        let mut stack = Vec::new();
        visited[k_usize] = true;
        stack.push(k_usize);

        while let Some(u) = stack.pop() {
            for &v in &graph[u] {
                if !visited[v] {
                    visited[v] = true;
                    stack.push(v);
                }
            }
        }

        // Check if any outside method invokes a suspicious one
        let mut can_remove = true;
        for edge in &invocations {
            let a = edge[0] as usize;
            let b = edge[1] as usize;
            if visited[b] && !visited[a] {
                can_remove = false;
                break;
            }
        }

        // Build result
        if can_remove {
            (0..n_usize)
                .filter(|&i| !visited[i])
                .map(|i| i as i32)
                .collect()
        } else {
            (0..n_usize).map(|i| i as i32).collect()
        }
    }
}
```

## Racket

```racket
(define/contract (remaining-methods n k invocations)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((adj (make-vector n '()))
         (visited (make-vector n #f)))
    ;; build adjacency list
    (for ([e invocations])
      (let ((a (first e))
            (b (second e)))
        (vector-set! adj a (cons b (vector-ref adj a)))))
    ;; DFS from k using explicit stack
    (let ((stack (list k)))
      (let loop ()
        (when (pair? stack)
          (define node (car stack))
          (set! stack (cdr stack))
          (unless (vector-ref visited node)
            (vector-set! visited node #t)
            (for ([nbr (in-list (vector-ref adj node))])
              (set! stack (cons nbr stack))))
          (loop))))
    ;; check for incoming edges from outside to the suspicious set
    (define can-remove? #t)
    (for ([e invocations])
      (let ((u (first e))
            (v (second e)))
        (when (and (vector-ref visited v) (not (vector-ref visited u)))
          (set! can-remove? #f))))
    (if can-remove?
        ;; return methods not in the suspicious set
        (for/list ([i (in-range n)] #:when (not (vector-ref visited i))) i)
        ;; otherwise, no removal possible: return all methods
        (build-list n (lambda (i) i)))))
```

## Erlang

```erlang
-module(solution).
-export([remaining_methods/3]).

-spec remaining_methods(N :: integer(), K :: integer(), Invocations :: [[integer()]]) -> [integer()].
remaining_methods(N, K, Invocations) ->
    Adj = build_adj(Invocations, #{}),
    Reachable = bfs([K], #{}, Adj),
    case can_remove(Invocations, Reachable) of
        true ->
            [I || I <- lists:seq(0, N - 1), not maps:is_key(I, Reachable)];
        false ->
            lists:seq(0, N - 1)
    end.

build_adj([], Adj) -> Adj;
build_adj([[A, B] | Rest], Adj) ->
    Updated = maps:update_with(
                A,
                fun(L) -> [B | L] end,
                [B],
                Adj),
    build_adj(Rest, Updated).

bfs(Stack, Visited, Adj) ->
    case Stack of
        [] -> Visited;
        [V | Rest] ->
            case maps:is_key(V, Visited) of
                true ->
                    bfs(Rest, Visited, Adj);
                false ->
                    NewVisited = maps:put(V, true, Visited),
                    Neighs = maps:get(V, Adj, []),
                    bfs(Neighs ++ Rest, NewVisited, Adj)
            end
    end.

can_remove([], _) -> true;
can_remove([[A, B] | Rest], Reachable) ->
    case {maps:is_key(A, Reachable), maps:is_key(B, Reachable)} of
        {false, true} -> false;
        _ -> can_remove(Rest, Reachable)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec remaining_methods(n :: integer, k :: integer, invocations :: [[integer]]) :: [integer]
  def remaining_methods(n, k, invocations) do
    adj = build_adj(invocations)

    suspicious = dfs(k, adj)

    has_external =
      Enum.any?(invocations, fn [a, b] ->
        not MapSet.member?(suspicious, a) and MapSet.member?(suspicious, b)
      end)

    if has_external do
      Enum.to_list(0..n - 1)
    else
      0..(n - 1)
      |> Enum.filter(fn i -> not MapSet.member?(suspicious, i) end)
    end
  end

  defp build_adj(invocations) do
    Enum.reduce(invocations, %{}, fn [a, b], acc ->
      Map.update(acc, a, [b], &[b | &1])
    end)
  end

  defp dfs(start, adj) do
    dfs_loop([start], MapSet.new(), adj)
  end

  defp dfs_loop([], visited, _adj), do: visited

  defp dfs_loop([node | rest], visited, adj) do
    if MapSet.member?(visited, node) do
      dfs_loop(rest, visited, adj)
    else
      neighbors = Map.get(adj, node, [])
      dfs_loop(neighbors ++ rest, MapSet.put(visited, node), adj)
    end
  end
end
```

# 3249. Count the Number of Good Nodes

## Cpp

```cpp
class Solution {
public:
    int countGoodNodes(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        vector<vector<int>> adj(n);
        for (auto &e : edges) {
            int a = e[0], b = e[1];
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
        vector<int> parent(n, -2), order;
        order.reserve(n);
        vector<int> st{0};
        parent[0] = -1;
        while (!st.empty()) {
            int u = st.back(); st.pop_back();
            order.push_back(u);
            for (int v : adj[u]) if (parent[v] == -2) {
                parent[v] = u;
                st.push_back(v);
            }
        }
        vector<int> sz(n, 1);
        for (int i = n - 1; i >= 0; --i) {
            int u = order[i];
            for (int v : adj[u]) if (v != parent[u])
                sz[u] += sz[v];
        }
        int good = 0;
        for (int u = 0; u < n; ++u) {
            int firstSize = -1;
            bool ok = true;
            for (int v : adj[u]) if (v != parent[u]) {
                if (firstSize == -1) firstSize = sz[v];
                else if (sz[v] != firstSize) { ok = false; break; }
            }
            if (ok) ++good;
        }
        return good;
    }
};
```

## Java

```java
class Solution {
    public int countGoodNodes(int[][] edges) {
        int n = edges.length + 1;
        @SuppressWarnings("unchecked")
        java.util.ArrayList<Integer>[] g = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new java.util.ArrayList<>();
        for (int[] e : edges) {
            int a = e[0], b = e[1];
            g[a].add(b);
            g[b].add(a);
        }

        int[] parent = new int[n];
        java.util.Arrays.fill(parent, -1);
        int[] order = new int[n];
        int idx = 0;

        int[] stack = new int[n];
        int top = 0;
        stack[top++] = 0;
        parent[0] = -2; // sentinel for root

        while (top > 0) {
            int node = stack[--top];
            order[idx++] = node;
            for (int nb : g[node]) {
                if (parent[nb] == -1) {
                    parent[nb] = node;
                    stack[top++] = nb;
                }
            }
        }

        int[] size = new int[n];
        int good = 0;

        for (int i = n - 1; i >= 0; --i) {
            int node = order[i];
            int sz = 1;
            boolean firstChild = true;
            int childSize = -1;
            boolean allEqual = true;

            for (int nb : g[node]) {
                if (nb == parent[node]) continue;
                sz += size[nb];
                if (firstChild) {
                    childSize = size[nb];
                    firstChild = false;
                } else if (size[nb] != childSize) {
                    allEqual = false;
                }
            }

            size[node] = sz;
            if (allEqual) good++;
        }

        return good;
    }
}
```

## Python

```python
class Solution(object):
    def countGoodNodes(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(300000)
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        self.ans = 0

        def dfs(u, parent):
            child_sizes = []
            total = 1
            for v in adj[u]:
                if v == parent:
                    continue
                sz = dfs(v, u)
                child_sizes.append(sz)
                total += sz
            # node is good if all child subtree sizes are equal (or no children)
            if not child_sizes or all(s == child_sizes[0] for s in child_sizes):
                self.ans += 1
            return total

        dfs(0, -1)
        return self.ans
```

## Python3

```python
import sys
from typing import List

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        sys.setrecursionlimit(300000)
        good = 0

        def dfs(u: int, parent: int) -> int:
            nonlocal good
            child_sizes = []
            total = 1
            for v in g[u]:
                if v == parent:
                    continue
                sz = dfs(v, u)
                child_sizes.append(sz)
                total += sz
            if not child_sizes:
                good += 1
            else:
                first = child_sizes[0]
                if all(s == first for s in child_sizes):
                    good += 1
            return total

        dfs(0, -1)
        return good
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

int countGoodNodes(int** edges, int edgesSize, int* edgesColSize) {
    int n = edgesSize + 1;
    int *deg = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        deg[a]++; deg[b]++;
    }

    int **adj = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        adj[i] = (int *)malloc(deg[i] * sizeof(int));
    }
    int *idx = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        adj[a][ idx[a]++ ] = b;
        adj[b][ idx[b]++ ] = a;
    }
    free(idx);

    int *stack = (int *)malloc(n * sizeof(int));
    int *parent = (int *)malloc(n * sizeof(int));
    int *order = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; ++i) parent[i] = -2;
    int sp = 0, ordSize = 0;
    stack[sp++] = 0;
    parent[0] = -1;

    while (sp > 0) {
        int u = stack[--sp];
        order[ordSize++] = u;
        for (int j = 0; j < deg[u]; ++j) {
            int v = adj[u][j];
            if (v == parent[u]) continue;
            parent[v] = u;
            stack[sp++] = v;
        }
    }

    int *subSize = (int *)malloc(n * sizeof(int));
    int goodCount = 0;

    for (int i = n - 1; i >= 0; --i) {
        int u = order[i];
        int refSize = -1;
        bool good = true;
        int total = 1;
        for (int j = 0; j < deg[u]; ++j) {
            int v = adj[u][j];
            if (v == parent[u]) continue;
            int sz = subSize[v];
            if (refSize == -1) refSize = sz;
            else if (sz != refSize) good = false;
            total += sz;
        }
        if (good) ++goodCount;
        subSize[u] = total;
    }

    // free allocated memory
    for (int i = 0; i < n; ++i) free(adj[i]);
    free(adj);
    free(deg);
    free(stack);
    free(parent);
    free(order);
    free(subSize);

    return goodCount;
}
```

## Csharp

```csharp
public class Solution {
    public int CountGoodNodes(int[][] edges) {
        int n = edges.Length + 1;
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            graph[a].Add(b);
            graph[b].Add(a);
        }

        int[] parent = new int[n];
        Array.Fill(parent, -1);
        var order = new int[n];
        int idx = 0;
        var stack = new Stack<int>();
        stack.Push(0);
        parent[0] = -2; // root sentinel

        while (stack.Count > 0) {
            int node = stack.Pop();
            order[idx++] = node;
            foreach (int nb in graph[node]) {
                if (parent[nb] == -1) {
                    parent[nb] = node;
                    stack.Push(nb);
                }
            }
        }

        int[] subSize = new int[n];
        int goodCount = 0;

        for (int i = n - 1; i >= 0; i--) {
            int node = order[i];
            int firstSize = -1;
            bool good = true;
            foreach (int nb in graph[node]) {
                if (parent[nb] == node) { // child
                    int sz = subSize[nb];
                    if (firstSize == -1) firstSize = sz;
                    else if (sz != firstSize) good = false;
                }
            }
            if (good) goodCount++;

            int total = 1;
            foreach (int nb in graph[node]) {
                if (parent[nb] == node) total += subSize[nb];
            }
            subSize[node] = total;
        }

        return goodCount;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @return {number}
 */
var countGoodNodes = function(edges) {
    const n = edges.length + 1;
    const adj = Array.from({length: n}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    
    const parent = new Int32Array(n).fill(-1);
    const order = [];
    const stack = [0];
    parent[0] = -2; // mark root's parent specially
    
    while (stack.length) {
        const node = stack.pop();
        order.push(node);
        for (const nb of adj[node]) {
            if (parent[nb] === -1) {
                parent[nb] = node;
                stack.push(nb);
            }
        }
    }
    
    const subSize = new Int32Array(n).fill(1);
    let goodCount = 0;
    
    for (let i = order.length - 1; i >= 0; --i) {
        const node = order[i];
        let firstChildSize = -1;
        let isGood = true;
        for (const nb of adj[node]) {
            if (parent[nb] === node) { // child
                subSize[node] += subSize[nb];
                if (firstChildSize === -1) {
                    firstChildSize = subSize[nb];
                } else if (subSize[nb] !== firstChildSize) {
                    isGood = false;
                }
            }
        }
        // leaf nodes have no children, firstChildSize stays -1, isGood remains true
        if (isGood) goodCount++;
    }
    
    return goodCount;
};
```

## Typescript

```typescript
function countGoodNodes(edges: number[][]): number {
    const n = edges.length + 1;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
    }

    const parent = new Int32Array(n);
    parent.fill(-1);
    const order: number[] = [];
    const stack: number[] = [0];
    parent[0] = -2; // root marker

    while (stack.length) {
        const v = stack.pop()!;
        order.push(v);
        for (const nb of adj[v]) {
            if (parent[nb] === -1) {
                parent[nb] = v;
                stack.push(nb);
            }
        }
    }

    const subSize = new Int32Array(n);
    let goodCount = 0;

    for (let i = order.length - 1; i >= 0; --i) {
        const v = order[i];
        let firstChildSize = -1;
        let isGood = true;
        let total = 1; // count the node itself

        for (const nb of adj[v]) {
            if (parent[nb] === v) { // child
                const sz = subSize[nb];
                if (firstChildSize === -1) firstChildSize = sz;
                else if (sz !== firstChildSize) isGood = false;
                total += sz;
            }
        }

        subSize[v] = total;
        if (isGood) ++goodCount;
    }

    return goodCount;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @return Integer
     */
    function countGoodNodes($edges) {
        $n = count($edges) + 1;
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            $adj[$a][] = $b;
            $adj[$b][] = $a;
        }
        $count = 0;
        $this->dfs(0, -1, $adj, $count);
        return $count;
    }

    private function dfs($node, $parent, &$adj, &$count) {
        $good = true;
        $firstSize = null;
        $size = 1;
        foreach ($adj[$node] as $nei) {
            if ($nei === $parent) continue;
            $childSize = $this->dfs($nei, $node, $adj, $count);
            if ($firstSize === null) {
                $firstSize = $childSize;
            } elseif ($childSize != $firstSize) {
                $good = false;
            }
            $size += $childSize;
        }
        if ($good) $count++;
        return $size;
    }
}
```

## Swift

```swift
class Solution {
    func countGoodNodes(_ edges: [[Int]]) -> Int {
        let n = edges.count + 1
        var adj = [[Int]](repeating: [], count: n)
        for e in edges {
            let a = e[0], b = e[1]
            adj[a].append(b)
            adj[b].append(a)
        }
        
        var parent = [Int](repeating: -1, count: n)
        var order = [Int]()
        order.reserveCapacity(n)
        var stack = [Int]()
        stack.append(0)
        parent[0] = 0
        
        while let node = stack.popLast() {
            order.append(node)
            for nb in adj[node] where nb != parent[node] {
                parent[nb] = node
                stack.append(nb)
            }
        }
        
        var size = [Int](repeating: 1, count: n)
        var goodCount = 0
        
        for node in order.reversed() {
            var childSize: Int? = nil
            var isGood = true
            for nb in adj[node] where nb != parent[node] {
                let sz = size[nb]
                if let cs = childSize {
                    if cs != sz { isGood = false; break }
                } else {
                    childSize = sz
                }
                size[node] += sz
            }
            // leaf nodes have no children, considered good
            if isGood { goodCount += 1 }
        }
        
        return goodCount
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun countGoodNodes(edges: Array<IntArray>): Int {
        val n = edges.size + 1
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        val parent = IntArray(n) { -2 }
        val order = IntArray(n)
        var ordIdx = 0
        val stack = ArrayDeque<Int>()
        stack.add(0)
        parent[0] = -1

        while (stack.isNotEmpty()) {
            val node = stack.removeLast()
            order[ordIdx++] = node
            for (nei in adj[node]) {
                if (nei == parent[node]) continue
                parent[nei] = node
                stack.add(nei)
            }
        }

        val size = IntArray(n)
        var goodCount = 0

        for (i in ordIdx - 1 downTo 0) {
            val node = order[i]
            var total = 1
            var childCnt = 0
            var firstSize = -1
            var allEqual = true
            for (nei in adj[node]) {
                if (nei == parent[node]) continue
                childCnt++
                val cs = size[nei]
                total += cs
                if (firstSize == -1) {
                    firstSize = cs
                } else if (cs != firstSize) {
                    allEqual = false
                }
            }
            size[node] = total
            if (childCnt == 0 || allEqual) {
                goodCount++
            }
        }

        return goodCount
    }
}
```

## Dart

```dart
class Solution {
  int countGoodNodes(List<List<int>> edges) {
    int n = edges.length + 1;
    List<List<int>> g = List.generate(n, (_) => []);
    for (var e in edges) {
      int a = e[0];
      int b = e[1];
      g[a].add(b);
      g[b].add(a);
    }

    List<int> parent = List.filled(n, -1);
    List<int> order = [];
    List<int> stack = [0];
    parent[0] = 0;
    while (stack.isNotEmpty) {
      int u = stack.removeLast();
      order.add(u);
      for (int v in g[u]) {
        if (v != parent[u]) {
          parent[v] = u;
          stack.add(v);
        }
      }
    }

    List<int> size = List.filled(n, 1);
    for (int i = order.length - 1; i >= 0; --i) {
      int u = order[i];
      for (int v in g[u]) {
        if (v != parent[u]) {
          size[u] += size[v];
        }
      }
    }

    int ans = 0;
    for (int u = 0; u < n; ++u) {
      int childSize = -1;
      bool ok = true;
      for (int v in g[u]) {
        if (v == parent[u]) continue;
        if (childSize == -1) {
          childSize = size[v];
        } else if (size[v] != childSize) {
          ok = false;
          break;
        }
      }
      if (ok) ans++;
    }

    return ans;
  }
}
```

## Golang

```go
func countGoodNodes(edges [][]int) int {
    n := len(edges) + 1
    g := make([][]int, n)
    for _, e := range edges {
        a, b := e[0], e[1]
        g[a] = append(g[a], b)
        g[b] = append(g[b], a)
    }

    count := 0
    var dfs func(int, int) int
    dfs = func(u, parent int) int {
        childSize := -1
        good := true
        total := 1
        for _, v := range g[u] {
            if v == parent {
                continue
            }
            sz := dfs(v, u)
            total += sz
            if childSize == -1 {
                childSize = sz
            } else if sz != childSize {
                good = false
            }
        }
        if good {
            count++
        }
        return total
    }

    dfs(0, -1)
    return count
}
```

## Ruby

```ruby
def count_good_nodes(edges)
  n = edges.size + 1
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  parent = Array.new(n, -1)
  order = []
  stack = [0]
  parent[0] = -2

  until stack.empty?
    node = stack.pop
    order << node
    adj[node].each do |nbr|
      next if nbr == parent[node]
      parent[nbr] = node
      stack << nbr
    end
  end

  size = Array.new(n, 1)
  good = 0

  order.reverse_each do |node|
    child_sizes = []
    adj[node].each do |nbr|
      next unless parent[nbr] == node
      sz = size[nbr]
      child_sizes << sz
      size[node] += sz
    end
    if child_sizes.empty? || child_sizes.uniq.length == 1
      good += 1
    end
  end

  good
end
```

## Scala

```scala
object Solution {
    def countGoodNodes(edges: Array[Array[Int]]): Int = {
        val n = edges.length + 1
        val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
        for (e <- edges) {
            val a = e(0)
            val b = e(1)
            adj(a).append(b)
            adj(b).append(a)
        }

        val parent = Array.fill(n)(-1)
        val order = new Array[Int](n)
        var idx = 0
        val stack = new java.util.ArrayDeque[Int]()
        stack.push(0)
        parent(0) = -2 // sentinel for root

        while (!stack.isEmpty) {
            val v = stack.pop()
            order(idx) = v
            idx += 1
            for (nb <- adj(v)) {
                if (parent(nb) == -1) {
                    parent(nb) = v
                    stack.push(nb)
                }
            }
        }

        val subSize = new Array[Int](n)
        var goodCount = 0
        var i = n - 1
        while (i >= 0) {
            val v = order(i)
            var total = 1
            var childCnt = 0
            var firstSize = -1
            var allEqual = true
            for (nb <- adj(v)) {
                if (parent(nb) == v) { // nb is a child of v
                    val cs = subSize(nb)
                    total += cs
                    if (childCnt == 0) {
                        firstSize = cs
                    } else if (cs != firstSize) {
                        allEqual = false
                    }
                    childCnt += 1
                }
            }
            subSize(v) = total
            if (childCnt <= 1 || allEqual) goodCount += 1
            i -= 1
        }

        goodCount
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_good_nodes(edges: Vec<Vec<i32>>) -> i32 {
        let n = edges.len() + 1;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in &edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }

        // parent array, using n as sentinel (out of range)
        let mut parent: Vec<usize> = vec![n; n];
        let mut order: Vec<usize> = Vec::with_capacity(n);
        let mut stack: Vec<usize> = Vec::new();
        stack.push(0);
        parent[0] = n;

        // iterative DFS to get traversal order
        while let Some(node) = stack.pop() {
            order.push(node);
            for &nbr in adj[node].iter() {
                if nbr == parent[node] {
                    continue;
                }
                parent[nbr] = node;
                stack.push(nbr);
            }
        }

        // compute subtree sizes and count good nodes
        let mut subsize: Vec<usize> = vec![1; n];
        let mut good_cnt: usize = 0;

        for &node in order.iter().rev() {
            let mut first_child_sz: Option<usize> = None;
            let mut good = true;
            for &nbr in adj[node].iter() {
                if nbr == parent[node] {
                    continue;
                }
                let sz = subsize[nbr];
                if let Some(first) = first_child_sz {
                    if sz != first {
                        good = false;
                    }
                } else {
                    first_child_sz = Some(sz);
                }
                subsize[node] += sz;
            }
            if good {
                good_cnt += 1;
            }
        }

        good_cnt as i32
    }
}
```

## Racket

```racket
(define/contract (count-good-nodes edges)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (+ (length edges) 1))
         (adj (make-vector n '())))
    ;; build adjacency list
    (for ([e edges])
      (define a (first e))
      (define b (second e))
      (vector-set! adj a (cons b (vector-ref adj a)))
      (vector-set! adj b (cons a (vector-ref adj b))))
    (define parent (make-vector n -2)) ; -2 = unvisited
    (vector-set! parent 0 -1)
    (define stack (list 0))
    (define order '())
    ;; DFS to obtain postorder traversal
    (let loop ()
      (when (not (null? stack))
        (define u (car stack))
        (set! stack (cdr stack))
        (set! order (cons u order))
        (for ([v (vector-ref adj u)])
          (when (= (vector-ref parent v) -2)
            (vector-set! parent v u)
            (set! stack (cons v stack))))
        (loop)))
    (define size (make-vector n 1))
    (define cnt 0)
    ;; process nodes in postorder
    (for ([u order])
      (define child-sizes '())
      (for ([v (vector-ref adj u)])
        (when (= (vector-ref parent v) u)
          (set! child-sizes (cons (vector-ref size v) child-sizes))))
      (when (or (null? child-sizes)
                (apply = child-sizes))
        (set! cnt (+ cnt 1)))
      (define p (vector-ref parent u))
      (when (>= p 0)
        (vector-set! size p (+ (vector-ref size p) (vector-ref size u)))))
    cnt))
```

## Erlang

```erlang
-module(solution).
-export([count_good_nodes/1]).

-spec count_good_nodes(Edges :: [[integer()]]) -> integer().
count_good_nodes(Edges) ->
    Adj = build_adj(Edges, #{}),
    loop([{0, -1, false}], Adj, #{}, 0).

build_adj([], Acc) -> Acc;
build_adj([[A,B]|Rest], Acc) ->
    Acc1 = maps:update_with(A,
            fun(L) -> [B|L] end,
            [B],
            Acc),
    Acc2 = maps:update_with(B,
            fun(L) -> [A|L] end,
            [A],
            Acc1),
    build_adj(Rest, Acc2).

loop([], _Adj, _SizeMap, Count) ->
    Count;
loop([{Node, Parent, true}|Stack], Adj, SizeMap, Count) ->
    Children = [C || C <- maps:get(Node, Adj, []), C =/= Parent],
    ChildSizes = [maps:get(C, SizeMap) || C <- Children],
    Size = 1 + lists:sum(ChildSizes),
    NewSizeMap = maps:put(Node, Size, SizeMap),
    Good = case Children of
        [] -> true;
        [_] -> true;
        _ ->
            First = hd(ChildSizes),
            lists:all(fun(S) -> S == First end, ChildSizes)
    end,
    NewCount = if Good -> Count + 1; true -> Count end,
    loop(Stack, Adj, NewSizeMap, NewCount);
loop([{Node, Parent, false}|Stack], Adj, SizeMap, Count) ->
    Children = [C || C <- maps:get(Node, Adj, []), C =/= Parent],
    Stack2 = [{Node, Parent, true} | Stack],
    NewStack = lists:foldl(fun(C, Acc) -> [{C, Node, false}|Acc] end,
                           Stack2, Children),
    loop(NewStack, Adj, SizeMap, Count).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_good_nodes(edges :: [[integer]]) :: integer
  def count_good_nodes(edges) do
    n = length(edges) + 1

    adjacency =
      Enum.reduce(0..(n - 1), %{}, fn i, acc -> Map.put(acc, i, []) end)
      |> Enum.reduce(edges, fn [a, b], acc ->
        acc
        |> Map.update!(a, fn lst -> [b | lst] end)
        |> Map.update!(b, fn lst -> [a | lst] end)
      end)

    {post_order, parent_arr} = dfs([{0, -1}], adjacency, [], :array.new(n, default: -1))

    init_sizes = :array.new(n, default: 0)

    {_sizes, good_cnt} =
      Enum.reduce(post_order, {init_sizes, 0}, fn node, {sizes, cnt} ->
        par = :array.get(node, parent_arr)

        child_szs = []
        size = 1

        for nb <- Map.get(adjacency, node) do
          if nb != par do
            sz = :array.get(nb, sizes)
            size = size + sz
            child_szs = [sz | child_szs]
          end
        end

        is_good =
          case child_szs do
            [] -> true
            [_] -> true
            [first | rest] -> Enum.all?(rest, fn s -> s == first end)
          end

        new_sizes = :array.set(node, size, sizes)
        new_cnt = if is_good, do: cnt + 1, else: cnt
        {new_sizes, new_cnt}
      end)

    good_cnt
  end

  defp dfs([], _adjacency, order, parent), do: {Enum.reverse(order), parent}

  defp dfs([{node, par} | rest], adjacency, order, parent) do
    # set parent for current node (except root)
    parent = if par != -1, do: :array.set(node, par, parent), else: parent

    children =
      Map.get(adjacency, node)
      |> Enum.filter(fn nb -> nb != par end)

    {new_stack, new_parent} =
      Enum.reduce(children, {rest, parent}, fn child, {stk, pr} ->
        pr2 = :array.set(child, node, pr)
        {[{child, node} | stk], pr2}
      end)

    dfs(new_stack, adjacency, [node | order], new_parent)
  end
end
```

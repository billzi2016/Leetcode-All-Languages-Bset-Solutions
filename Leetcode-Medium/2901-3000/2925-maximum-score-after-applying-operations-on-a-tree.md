# 2925. Maximum Score After Applying Operations on a Tree

## Cpp

```cpp
class Solution {
public:
    long long maximumScoreAfterOperations(vector<vector<int>>& edges, vector<int>& values) {
        int n = values.size();
        vector<vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        function<pair<long long,long long>(int,int)> dfs = [&](int u, int p) -> pair<long long,long long> {
            long long subtreeSum = values[u];
            long long sumChildSums = 0; // Σ sum[child]
            long long sumChildDP = 0;   // Σ dp[child]
            bool hasChild = false;
            for (int v : g[u]) if (v != p) {
                hasChild = true;
                auto [cSum, cDp] = dfs(v, u);
                subtreeSum += cSum;
                sumChildSums += cSum;
                sumChildDP   += cDp;
            }
            long long dp;
            if (!hasChild) {
                // leaf: cannot take it when ancestors are already taken
                dp = 0;
            } else {
                long long takeU = (long long)values[u] + sumChildDP; // take this node
                long long notTakeU = sumChildSums;                  // keep this node, can take everything below
                dp = max(takeU, notTakeU);
            }
            return {subtreeSum, dp};
        };
        auto res = dfs(0, -1);
        return res.second;
    }
};
```

## Java

```java
class Solution {
    public long maximumScoreAfterOperations(int[][] edges, int[] values) {
        int n = values.length;
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; ++i) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        long[] sum = new long[n];
        long[] dp = new long[n];
        dfs(0, -1, g, values, sum, dp);
        return dp[0];
    }

    private void dfs(int u, int parent, List<Integer>[] g, int[] values,
                     long[] sum, long[] dp) {
        long childSumTotal = 0;
        long childDpTotal = 0;
        for (int v : g[u]) {
            if (v == parent) continue;
            dfs(v, u, g, values, sum, dp);
            childSumTotal += sum[v];
            childDpTotal += dp[v];
        }
        sum[u] = values[u] + childSumTotal;
        long takeU = values[u] + childDpTotal; // take value[u]
        long notTakeU = childSumTotal;         // keep u, can take all children fully
        dp[u] = Math.max(takeU, notTakeU);
    }
}
```

## Python

```python
class Solution(object):
    def maximumScoreAfterOperations(self, edges, values):
        """
        :type edges: List[List[int]]
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        parent = [-1] * n
        order = []
        stack = [0]
        parent[0] = 0
        while stack:
            node = stack.pop()
            order.append(node)
            for nb in g[node]:
                if nb != parent[node]:
                    parent[nb] = node
                    stack.append(nb)

        sum_sub = [0] * n          # total sum of subtree values
        f0 = [0] * n               # max deletable sum when this node must have a kept node on every root‑to‑leaf path

        for node in reversed(order):
            total = values[node]
            keep_opt = 0           # delete all descendants, keep this node
            del_opt = values[node] # delete this node, children must satisfy f0
            has_child = False
            for nb in g[node]:
                if nb == parent[node]:
                    continue
                has_child = True
                total += sum_sub[nb]
                keep_opt += sum_sub[nb]
                del_opt += f0[nb]
            sum_sub[node] = total
            if not has_child:
                f0[node] = 0        # leaf must be kept, cannot delete it
            else:
                f0[node] = max(keep_opt, del_opt)

        total_sum = sum_sub[0]

        # root children list
        root_children = [c for c in g[0] if c != parent[0]]
        if not root_children:      # single node tree (n >= 2 per constraints, but safe)
            return 0

        keep_root = total_sum - values[0]                     # keep root, delete everything else
        del_root = values[0] + sum(f0[c] for c in root_children)  # delete root, children must satisfy f0
        return max(keep_root, del_root)
```

## Python3

```python
import sys
from typing import List

sys.setrecursionlimit(300000)

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(u: int, parent: int):
            total_sum = values[u]          # sum of all node values in this subtree
            child_dp_total = 0             # Σ dp[child]
            child_sum_total = 0            # Σ sum[child]

            for v in adj[u]:
                if v == parent:
                    continue
                sub_sum, sub_dp = dfs(v, u)
                total_sum += sub_sum
                child_dp_total += sub_dp
                child_sum_total += sub_sum

            # Option 1: take node u
            opt_take = values[u] + child_dp_total
            # Option 2: skip node u -> must take all nodes in each child subtree
            opt_skip = child_sum_total

            dp_u = max(opt_take, opt_skip)
            return total_sum, dp_u

        _, answer = dfs(0, -1)
        return answer
```

## C

```c
#include <stdlib.h>

typedef struct {
    long long sum;
    long long dp;
} Pair;

static int *g_to;
static int *g_next;
static int *g_head;
static int g_edge_idx;
static int *g_values;

/* add undirected edge */
static void addEdge(int u, int v) {
    g_to[g_edge_idx] = v;
    g_next[g_edge_idx] = g_head[u];
    g_head[u] = g_edge_idx++;
}

/* depth‑first search returning subtree sum and maximal deletable score */
static Pair dfs(int u, int parent) {
    long long sum = (long long)g_values[u];
    long long childSumTotal = 0;   // Σ sum[child]
    long long childDpSum = 0;      // Σ dp[child]

    for (int e = g_head[u]; e != -1; e = g_next[e]) {
        int v = g_to[e];
        if (v == parent) continue;
        Pair sub = dfs(v, u);
        sum += sub.sum;
        childSumTotal += sub.sum;
        childDpSum += sub.dp;
    }

    long long dp_keep_u = childSumTotal;                     // keep u, delete everything below
    long long dp_delete_u = (long long)g_values[u] + childDpSum; // delete u, rely on children

    long long best = dp_keep_u > dp_delete_u ? dp_keep_u : dp_delete_u;

    Pair res;
    res.sum = sum;
    res.dp  = best;
    return res;
}

long long maximumScoreAfterOperations(int** edges, int edgesSize, int* edgesColSize, int* values, int valuesSize) {
    int n = valuesSize;
    g_values = values;

    /* allocate adjacency list */
    int maxE = 2 * (n - 1);
    g_to   = (int *)malloc(maxE * sizeof(int));
    g_next = (int *)malloc(maxE * sizeof(int));
    g_head = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) g_head[i] = -1;
    g_edge_idx = 0;

    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        addEdge(a, b);
        addEdge(b, a);
    }

    Pair ans = dfs(0, -1);

    free(g_to);
    free(g_next);
    free(g_head);
    return ans.dp;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MaximumScoreAfterOperations(int[][] edges, int[] values) {
        int n = values.Length;
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            graph[a].Add(b);
            graph[b].Add(a);
        }

        long[] sum = new long[n];
        long[] keep = new long[n]; // f0: node kept
        long[] del = new long[n];  // f1: node deleted (if possible)

        const long NEG = -9_000_000_000_000_000_000L; // sufficiently small

        var stack = new Stack<(int node, int parent, bool processed)>();
        stack.Push((0, -1, false));

        while (stack.Count > 0) {
            var cur = stack.Pop();
            int u = cur.node;
            int p = cur.parent;
            if (!cur.processed) {
                stack.Push((u, p, true));
                foreach (int v in graph[u]) {
                    if (v == p) continue;
                    stack.Push((v, u, false));
                }
            } else {
                long totalSum = values[u];
                long keepVal = 0; // sum of child subtree sums
                long bestAll = 0; // for deletion case
                int childCount = 0;

                foreach (int v in graph[u]) {
                    if (v == p) continue;
                    childCount++;
                    totalSum += sum[v];
                    keepVal += sum[v];
                    long bestChild = Math.Max(keep[v], del[v]);
                    bestAll += bestChild;
                }

                sum[u] = totalSum;
                keep[u] = keepVal;

                if (childCount == 0) {
                    // leaf cannot be deleted when its ancestors are also deleted
                    del[u] = NEG;
                } else {
                    del[u] = values[u] + bestAll;
                }
            }
        }

        return Math.Max(keep[0], del[0]);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @param {number[]} values
 * @return {number}
 */
var maximumScoreAfterOperations = function(edges, values) {
    const n = values.length;
    const adj = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
    }
    let total = 0;
    for (const v of values) total += v;

    function dfs(u, parent) {
        let sumChild = 0;
        let hasChild = false;
        for (const v of adj[u]) {
            if (v === parent) continue;
            const childCost = dfs(v, u);
            sumChild += childCost;
            hasChild = true;
        }
        // leaf must be kept
        if (!hasChild) return values[u];
        // internal node: either keep this node or rely on children covering
        return Math.min(values[u], sumChild);
    }

    const minKeep = dfs(0, -1);
    return total - minKeep;
};
```

## Typescript

```typescript
function maximumScoreAfterOperations(edges: number[][], values: number[]): number {
    const n = values.length;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const sum: number[] = new Array(n).fill(0);
    const f: number[] = new Array(n).fill(0);

    function dfs(u: number, parent: number): void {
        let childSumTotal = 0;
        let childFTotal = 0;

        for (const v of adj[u]) {
            if (v === parent) continue;
            dfs(v, u);
            childSumTotal += sum[v];
            childFTotal += f[v];
        }

        sum[u] = values[u] + childSumTotal;

        // If leaf, childSumTotal == 0 and childFTotal == 0
        // f[u] = max( sum of children's subtree sums (keep u), value[u] + sum of children's f )
        const keepU = childSumTotal;               // keep current node (do not take its value)
        const takeU = values[u] + childFTotal;     // take current node's value
        f[u] = Math.max(keepU, takeU);
    }

    dfs(0, -1);
    return f[0];
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $edges
     * @param Integer[] $values
     * @return Integer
     */
    function maximumScoreAfterOperations($edges, $values) {
        $n = count($values);
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }
        [$sumRoot, $dpRoot] = $this->dfs(0, -1, $adj, $values);
        return $dpRoot;
    }

    private function dfs($node, $parent, &$adj, &$values): array {
        $sum = $values[$node];
        $take = $values[$node]; // include this node
        $skip = 0;               // exclude this node

        foreach ($adj[$node] as $nbr) {
            if ($nbr === $parent) continue;
            [$childSum, $childDp] = $this->dfs($nbr, $node, $adj, $values);
            $sum += $childSum;
            $take += $childDp;
            $skip += $childSum;
        }

        $dp = max($take, $skip);
        return [$sum, $dp];
    }
}
```

## Swift

```swift
class Solution {
    func maximumScoreAfterOperations(_ edges: [[Int]], _ values: [Int]) -> Int {
        let n = values.count
        var graph = [[Int]](repeating: [], count: n)
        for e in edges {
            let u = e[0], v = e[1]
            graph[u].append(v)
            graph[v].append(u)
        }
        
        var sumSub = [Int64](repeating: 0, count: n)
        var dp = [Int64](repeating: 0, count: n)
        let vals = values.map { Int64($0) }
        
        func dfs(_ node: Int, _ parent: Int) {
            var childSumTotal: Int64 = 0
            var childDpTotal: Int64 = 0
            for nb in graph[node] where nb != parent {
                dfs(nb, node)
                childSumTotal += sumSub[nb]
                childDpTotal += dp[nb]
            }
            sumSub[node] = vals[node] + childSumTotal
            let includeNode = vals[node] + childDpTotal
            let excludeNode = childSumTotal   // Σ sum[child]
            dp[node] = max(includeNode, excludeNode)
        }
        
        dfs(0, -1)
        return Int(dp[0])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumScoreAfterOperations(edges: Array<IntArray>, values: IntArray): Long {
        val n = values.size
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val a = e[0]
            val b = e[1]
            adj[a].add(b)
            adj[b].add(a)
        }

        val parent = IntArray(n) { -1 }
        val order = ArrayDeque<Int>()
        val stack = java.util.ArrayDeque<Int>()
        stack.push(0)
        parent[0] = 0
        while (stack.isNotEmpty()) {
            val node = stack.pop()
            order.add(node)
            for (nei in adj[node]) {
                if (nei == parent[node]) continue
                parent[nei] = node
                stack.push(nei)
            }
        }

        val sum = LongArray(n)
        val dp = LongArray(n)

        while (!order.isEmpty()) {
            val node = order.removeLast()
            var sumChildren = 0L
            var dpChildren = 0L
            for (nei in adj[node]) {
                if (nei == parent[node]) continue
                sumChildren += sum[nei]
                dpChildren += dp[nei]
            }
            sum[node] = values[node].toLong() + sumChildren
            val takeNode = values[node].toLong() + dpChildren
            val notTakeNode = sumChildren
            dp[node] = if (takeNode > notTakeNode) takeNode else notTakeNode
        }

        return dp[0]
    }
}
```

## Dart

```dart
class Solution {
  int maximumScoreAfterOperations(List<List<int>> edges, List<int> values) {
    int n = values.length;
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int a = e[0];
      int b = e[1];
      adj[a].add(b);
      adj[b].add(a);
    }

    // Build parent array and traversal order using iterative DFS
    List<int> parent = List.filled(n, -1);
    List<int> order = [];
    List<int> stack = [0];
    parent[0] = -2; // root marker

    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      order.add(node);
      for (int nb in adj[node]) {
        if (nb == parent[node]) continue;
        parent[nb] = node;
        stack.add(nb);
      }
    }

    List<int> sum = List.filled(n, 0);
    List<int> dp = List.filled(n, 0);

    for (int i = order.length - 1; i >= 0; --i) {
      int v = order[i];
      int totalSumChildren = 0;
      int totalDpChildren = 0;
      for (int nb in adj[v]) {
        if (nb == parent[v]) continue;
        totalSumChildren += sum[nb];
        totalDpChildren += dp[nb];
      }
      sum[v] = values[v] + totalSumChildren;
      int takeV = values[v] + totalDpChildren;
      int notTakeV = totalSumChildren; // can take all nodes in children subtrees
      dp[v] = (takeV > notTakeV) ? takeV : notTakeV;
    }

    return dp[0];
  }
}
```

## Golang

```go
func maximumScoreAfterOperations(edges [][]int, values []int) int64 {
    n := len(values)
    g := make([][]int, n)
    for _, e := range edges {
        a, b := e[0], e[1]
        g[a] = append(g[a], b)
        g[b] = append(g[b], a)
    }

    total := make([]int64, n)
    dp := make([]int64, n)

    var dfs func(int, int)
    dfs = func(u, parent int) {
        var sumChildrenTotal int64
        var sumChildrenDP int64
        tot := int64(values[u])
        for _, v := range g[u] {
            if v == parent {
                continue
            }
            dfs(v, u)
            tot += total[v]
            sumChildrenTotal += total[v]
            sumChildrenDP += dp[v]
        }
        total[u] = tot
        optTake := int64(values[u]) + sumChildrenDP
        optSkip := sumChildrenTotal
        if optTake > optSkip {
            dp[u] = optTake
        } else {
            dp[u] = optSkip
        }
    }

    dfs(0, -1)
    return dp[0]
}
```

## Ruby

```ruby
def maximum_score_after_operations(edges, values)
  n = values.length
  adj = Array.new(n) { [] }
  edges.each do |a, b|
    adj[a] << b
    adj[b] << a
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

  keep = Array.new(n, 0)
  order.reverse_each do |node|
    sum_child_keep = 0
    child_cnt = 0
    adj[node].each do |nbr|
      next if nbr == parent[node]
      child_cnt += 1
      sum_child_keep += keep[nbr]
    end
    if child_cnt.zero?
      keep[node] = values[node]
    else
      keep[node] = [values[node], sum_child_keep].min
    end
  end

  total = values.sum
  total - keep[0]
end
```

## Scala

```scala
import scala.collection.mutable.ArrayBuffer

object Solution {
  def maximumScoreAfterOperations(edges: Array[Array[Int]], values: Array[Int]): Long = {
    val n = values.length
    val adj = Array.fill(n)(new ArrayBuffer[Int]())
    for (e <- edges) {
      val a = e(0)
      val b = e(1)
      adj(a).append(b)
      adj(b).append(a)
    }

    val total = new Array[Long](n)
    val best = new Array[Long](n)

    def dfs(u: Int, parent: Int): Unit = {
      var sumTotal = values(u).toLong
      var sumBestChildren = 0L
      for (v <- adj(u) if v != parent) {
        dfs(v, u)
        sumTotal += total(v)
        sumBestChildren += best(v)
      }
      total(u) = sumTotal
      val optSelect = sumTotal          // select u and take everything below
      val optNotSelect = sumBestChildren // do not select u, children must cover leaves
      best(u) = math.max(optSelect, optNotSelect)
    }

    dfs(0, -1)
    best(0)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_score_after_operations(edges: Vec<Vec<i32>>, values: Vec<i32>) -> i64 {
        let n = values.len();
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in edges.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }

        // Build parent array and traversal order (preorder)
        let mut parent: Vec<usize> = vec![n; n];
        let mut order: Vec<usize> = Vec::with_capacity(n);
        let mut stack: Vec<usize> = vec![0];
        parent[0] = n; // root has no parent
        while let Some(u) = stack.pop() {
            order.push(u);
            for &v in adj[u].iter() {
                if v == parent[u] {
                    continue;
                }
                parent[v] = u;
                stack.push(v);
            }
        }

        // Post-order DP
        let mut sum: Vec<i64> = vec![0; n];
        let mut dp: Vec<i64> = vec![0; n];

        for &u in order.iter().rev() {
            let mut total_sum = values[u] as i64;
            let mut take_sum = values[u] as i64;
            for &v in adj[u].iter() {
                if v == parent[u] {
                    continue;
                }
                total_sum += sum[v];
                take_sum += dp[v];
            }
            let not_take = total_sum - values[u] as i64; // Σ sum[child]
            dp[u] = std::cmp::max(take_sum, not_take);
            sum[u] = total_sum;
        }

        dp[0]
    }
}
```

## Racket

```racket
(define/contract (maximum-score-after-operations edges values)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)
  (let* ((n (vector-length (list->vector values)))
         (adj (make-vector n '()))
         (_ (for-each
              (lambda (e)
                (define a (first e))
                (define b (second e))
                (vector-set! adj a (cons b (vector-ref adj a)))
                (vector-set! adj b (cons a (vector-ref adj b))))
              edges))
         (parent (make-vector n -1))
         (order '())
         (stack (list 0)))
    ;; build parent array and preorder order
    (vector-set! parent 0 -2)
    (let loop ()
      (when (not (null? stack))
        (define node (car stack))
        (set! stack (cdr stack))
        (set! order (cons node order))
        (for-each
         (lambda (nbr)
           (when (= (vector-ref parent nbr) -1)
             (vector-set! parent nbr node)
             (set! stack (cons nbr stack))))
         (vector-ref adj node))
        (loop)))
    ;; dp and sum vectors
    (define dp (make-vector n 0))
    (define sum (make-vector n 0))
    (for ([node (in-list (reverse order))])
      (define children '())
      (for-each
       (lambda (nbr)
         (when (= (vector-ref parent nbr) node)
           (set! children (cons nbr children))))
       (vector-ref adj node))
      (define sum-children 0)
      (define dp-children 0)
      (for ([ch (in-list children)])
        (set! sum-children (+ sum-children (vector-ref sum ch)))
        (set! dp-children (+ dp-children (vector-ref dp ch))))
      (define val (list-ref values node))
      (vector-set! sum node (+ val sum-children))
      (vector-set! dp node (max (+ val dp-children) sum-children)))
    (vector-ref dp 0)))
```

## Erlang

```erlang
-module(solution).
-export([maximum_score_after_operations/2]).

-spec maximum_score_after_operations(Edges :: [[integer()]], Values :: [integer()]) -> integer().
maximum_score_after_operations(Edges, Values) ->
    Adj = build_adj(Edges, #{}),
    ValuesTuple = list_to_tuple(Values),
    {_, DP} = dfs(0, -1, Adj, ValuesTuple),
    DP.

build_adj([], Adj) -> Adj;
build_adj([[A,B]|Rest], Adj) ->
    Adj1 = maps:update_with(A,
            fun(L) -> [B|L] end,
            [B],
            Adj),
    Adj2 = maps:update_with(B,
            fun(L) -> [A|L] end,
            [A],
            Adj1),
    build_adj(Rest, Adj2).

dfs(Node, Parent, Adj, ValuesTuple) ->
    Neigh = maps:get(Node, Adj, []),
    Children = [C || C <- Neigh, C =/= Parent],
    {Sums, DPs} = lists:foldl(fun(C,{Ss,Dps}) ->
            {Sc, Dc} = dfs(C, Node, Adj, ValuesTuple),
            {[Sc|Ss], [Dc|Dps]}
        end, {[], []}, Children),
    SumChildren = lists:sum(Sums),
    DPNotTake = lists:sum(Sums),
    DPTake = element(Node+1, ValuesTuple) + lists:sum(DPs),
    DPNode = if DPTake > DPNotTake -> DPTake; true -> DPNotTake end,
    {element(Node+1, ValuesTuple) + SumChildren, DPNode}.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_score_after_operations(edges :: [[integer]], values :: [integer]) :: integer
  def maximum_score_after_operations(edges, values) do
    n = length(values)

    # Build adjacency list using :array for O(1) access
    adj =
      Enum.reduce(edges, :array.new(n, default: []), fn [a, b], acc ->
        list_a = :array.get(a, acc)
        acc = :array.set(a, [b | list_a], acc)

        list_b = :array.get(b, acc)
        :array.set(b, [a | list_b], acc)
      end)

    # DFS to determine parent of each node and obtain postorder traversal
    {parent_arr, postorder} = dfs_postorder(0, adj, n)

    # DP arrays: dp for maximum score, sum for total subtree sum
    dp_arr = :array.new(n, default: 0)
    sum_arr = :array.new(n, default: 0)

    {final_dp, _} =
      Enum.reduce(postorder, {dp_arr, sum_arr}, fn node, {dp_a, sum_a} ->
        p = :array.get(node, parent_arr)

        children =
          :array.get(node, adj)
          |> Enum.filter(fn nb -> nb != p end)

        {total_sum_children, dp_children_sum} =
          Enum.reduce(children, {0, 0}, fn child, {s_acc, d_acc} ->
            s_child = :array.get(child, sum_a)
            d_child = :array.get(child, dp_a)
            {s_acc + s_child, d_acc + d_child}
          end)

        node_val = Enum.at(values, node)
        sum_node = node_val + total_sum_children
        dp_node = max(node_val + dp_children_sum, total_sum_children)

        dp_a = :array.set(node, dp_node, dp_a)
        sum_a = :array.set(node, sum_node, sum_a)
        {dp_a, sum_a}
      end)

    :array.get(0, final_dp)
  end

  # Returns {parent_array, postorder_list}
  defp dfs_postorder(root, adj, n) do
    parent_arr = :array.new(n, default: -1)
    dfs_stack([root], adj, parent_arr, [])
  end

  defp dfs_stack([], _adj, parent_arr, order), do: {parent_arr, order}

  defp dfs_stack([node | stack], adj, parent_arr, order) do
    p = :array.get(node, parent_arr)
    neighbors = :array.get(node, adj)

    {new_parent_arr, new_stack} =
      Enum.reduce(neighbors, {parent_arr, stack}, fn nb, {par_acc, stk_acc} ->
        if nb != p do
          updated_par = :array.set(nb, node, par_acc)
          {updated_par, [nb | stk_acc]}
        else
          {par_acc, stk_acc}
        end
      end)

    dfs_stack(new_stack, adj, new_parent_arr, [node | order])
  end
end
```

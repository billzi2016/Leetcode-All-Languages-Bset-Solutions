# 2872. Maximum Number of K-Divisible Components

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long K;
    vector<vector<int>> adj;
    vector<long long> val;
    int cnt = 0;
    
    long long dfs(int u, int parent) {
        long long sum = 0;
        for (int v : adj[u]) {
            if (v == parent) continue;
            long long childRem = dfs(v, u);
            if (childRem == 0) {
                ++cnt; // cut edge between u and v
            } else {
                sum += childRem;
            }
        }
        sum = (sum + val[u]) % K;
        return sum;
    }
    
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
        K = k;
        adj.assign(n, {});
        for (auto &e : edges) {
            int a = e[0], b = e[1];
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
        val.resize(n);
        for (int i = 0; i < n; ++i) val[i] = values[i] % K;
        cnt = 0;
        dfs(0, -1);
        return cnt + 1; // include the component containing the root
    }
};
```

## Java

```java
class Solution {
    private long k;
    private int[] values;
    private java.util.List<Integer>[] graph;
    private int components;

    public int maxKDivisibleComponents(int n, int[][] edges, int[] values, int k) {
        this.k = k;
        this.values = values;
        this.graph = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new java.util.ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        components = 0;
        dfs(0, -1);
        return components;
    }

    private long dfs(int node, int parent) {
        long sumMod = ((long) values[node]) % k;
        for (int nei : graph[node]) {
            if (nei == parent) continue;
            long childMod = dfs(nei, node);
            sumMod = (sumMod + childMod) % k;
        }
        if (sumMod == 0) {
            components++;
            return 0L; // cut here
        }
        return sumMod;
    }
}
```

## Python

```python
class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(10**6)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        self.count = 0

        def dfs(node, parent):
            cur = values[node] % k
            for nei in graph[node]:
                if nei == parent:
                    continue
                cur = (cur + dfs(nei, node)) % k
            if cur == 0:
                self.count += 1
                return 0
            return cur

        dfs(0, -1)
        return self.count
```

## Python3

```python
import sys
from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        sys.setrecursionlimit(1 << 20)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ans = 0

        def dfs(u: int, parent: int) -> int:
            nonlocal ans
            cur = values[u] % k
            for v in graph[u]:
                if v == parent:
                    continue
                cur = (cur + dfs(v, u)) % k
            if cur == 0:
                ans += 1
                return 0
            return cur

        dfs(0, -1)
        return ans
```

## C

```c
#include <stdlib.h>

static long long answer;

static int dfs(int u, int parent, long long *vals, int **adj, int *deg, int k) {
    long long sum = vals[u];
    for (int i = 0; i < deg[u]; ++i) {
        int v = adj[u][i];
        if (v == parent) continue;
        sum += dfs(v, u, vals, adj, deg, k);
    }
    if (sum % k == 0) {
        ++answer;
        return 0;
    }
    return (int)(sum % k);
}

int maxKDivisibleComponents(int n, int** edges, int edgesSize, int* edgesColSize,
                            int* values, int valuesSize, int k) {
    if (n == 0) return 0;

    int *deg = calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        deg[a]++; deg[b]++;
    }

    int **adj = malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        adj[i] = malloc(deg[i] * sizeof(int));
    }

    int *cur = calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        adj[a][cur[a]++] = b;
        adj[b][cur[b]++] = a;
    }
    free(cur);

    long long *vals = malloc(n * sizeof(long long));
    for (int i = 0; i < n; ++i) vals[i] = values[i];

    answer = 0;
    dfs(0, -1, vals, adj, deg, k);

    for (int i = 0; i < n; ++i) free(adj[i]);
    free(adj);
    free(deg);
    free(vals);

    return (int)answer;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxKDivisibleComponents(int n, int[][] edges, int[] values, int k)
    {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges)
        {
            int a = e[0], b = e[1];
            graph[a].Add(b);
            graph[b].Add(a);
        }

        long K = k;
        int components = 0;

        long Dfs(int node, int parent)
        {
            long sum = ((long)values[node]) % K;
            foreach (int nei in graph[node])
            {
                if (nei == parent) continue;
                sum += Dfs(nei, node);
                sum %= K;
            }
            if (sum == 0)
            {
                components++;
                return 0;
            }
            return sum;
        }

        Dfs(0, -1);
        return components;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} values
 * @param {number} k
 * @return {number}
 */
var maxKDivisibleComponents = function(n, edges, values, k) {
    const adj = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
    }
    let count = 0;
    function dfs(u, parent) {
        let sumMod = values[u] % k;
        for (const v of adj[u]) {
            if (v === parent) continue;
            const childRem = dfs(v, u);
            sumMod = (sumMod + childRem) % k;
        }
        if (sumMod === 0) count++;
        return sumMod;
    }
    dfs(0, -1);
    return count;
};
```

## Typescript

```typescript
function maxKDivisibleComponents(n: number, edges: number[][], values: number[], k: number): number {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
    }

    const parent = new Int32Array(n).fill(-1);
    const order: number[] = [];
    const stack: number[] = [0];
    while (stack.length) {
        const u = stack.pop()!;
        order.push(u);
        for (const v of adj[u]) {
            if (v === parent[u]) continue;
            parent[v] = u;
            stack.push(v);
        }
    }

    let components = 0;
    const subMod: number[] = new Array(n).fill(0);

    for (let i = order.length - 1; i >= 0; --i) {
        const u = order[i];
        let cur = values[u] % k;
        if (cur < 0) cur += k;

        for (const v of adj[u]) {
            if (parent[v] === u) { // child
                cur = (cur + subMod[v]) % k;
            }
        }

        if (cur === 0) components++;
        subMod[u] = cur; // will be 0 if counted as a component
    }

    return components;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer[] $values
     * @param Integer $k
     * @return Integer
     */
    function maxKDivisibleComponents($n, $edges, $values, $k) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            $graph[$a][] = $b;
            $graph[$b][] = $a;
        }
        $ans = 0;
        $this->dfs(0, -1, $graph, $values, $k, $ans);
        return $ans;
    }

    private function dfs($u, $parent, &$graph, &$values, $k, &$ans) {
        $sum = $values[$u] % $k;
        foreach ($graph[$u] as $v) {
            if ($v === $parent) continue;
            $childSum = $this->dfs($v, $u, $graph, $values, $k, $ans);
            $sum = ($sum + $childSum) % $k;
        }
        if ($sum == 0) {
            $ans++;
            return 0;
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func maxKDivisibleComponents(_ n: Int, _ edges: [[Int]], _ values: [Int], _ k: Int) -> Int {
        var graph = Array(repeating: [Int](), count: n)
        for e in edges {
            let a = e[0]
            let b = e[1]
            graph[a].append(b)
            graph[b].append(a)
        }
        let kLL = Int64(k)
        var valuesLL = values.map { Int64($0) }
        var count = 0

        func dfs(_ u: Int, _ parent: Int) -> Int64 {
            var sum: Int64 = 0
            for v in graph[u] {
                if v == parent { continue }
                sum += dfs(v, u)
            }
            sum += valuesLL[u]
            let rem = sum % kLL
            if rem == 0 {
                count += 1
                return 0
            } else {
                return rem
            }
        }

        _ = dfs(0, -1)
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxKDivisibleComponents(n: Int, edges: Array<IntArray>, values: IntArray, k: Int): Int {
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }
        var components = 0
        val kLong = k.toLong()
        fun dfs(node: Int, parent: Int): Long {
            var sum = values[node].toLong() % kLong
            for (nbr in adj[node]) {
                if (nbr == parent) continue
                sum += dfs(nbr, node)
                sum %= kLong
            }
            return if (sum == 0L) {
                components++
                0L
            } else {
                sum
            }
        }
        dfs(0, -1)
        return components
    }
}
```

## Dart

```dart
class Solution {
  int maxKDivisibleComponents(int n, List<List<int>> edges, List<int> values, int k) {
    // Build adjacency list
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      adj[u].add(v);
      adj[v].add(u);
    }

    int ans = 0;

    int dfs(int node, int parent) {
      int sumMod = values[node] % k;
      for (int nei in adj[node]) {
        if (nei == parent) continue;
        sumMod = (sumMod + dfs(nei, node)) % k;
      }
      if (sumMod == 0) {
        ans++;
        return 0; // this subtree forms a component, contributes nothing upward
      }
      return sumMod; // propagate remainder to parent
    }

    dfs(0, -1);
    return ans;
  }
}
```

## Golang

```go
package main

func maxKDivisibleComponents(n int, edges [][]int, values []int, k int) int {
	adj := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}
	modK := int64(k)
	ans := 0

	var dfs func(int, int) int64
	dfs = func(u, parent int) int64 {
		sum := int64(values[u]) % modK
		for _, v := range adj[u] {
			if v == parent {
				continue
			}
			childSum := dfs(v, u)
			sum = (sum + childSum) % modK
		}
		if sum == 0 {
			ans++
			return 0
		}
		return sum
	}

	dfs(0, -1)
	return ans
}
```

## Ruby

```ruby
def max_k_divisible_components(n, edges, values, k)
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

  sum_mod = Array.new(n, 0)
  count = 0

  order.reverse_each do |node|
    total = values[node] % k
    adj[node].each do |nbr|
      next unless parent[nbr] == node   # child
      total = (total + sum_mod[nbr]) % k
    end
    sum_mod[node] = total
    count += 1 if total.zero?
  end

  count
end
```

## Scala

```scala
import scala.collection.mutable

object Solution {
  def maxKDivisibleComponents(n: Int, edges: Array[Array[Int]], values: Array[Int], k: Int): Int = {
    val adj = Array.fill(n)(new mutable.ArrayBuffer[Int]())
    for (e <- edges) {
      val a = e(0)
      val b = e(1)
      adj(a) += b
      adj(b) += a
    }

    val valsLong = values.map(_.toLong)
    val kk = k.toLong
    val sub = new Array[Long](n)

    var count = 0
    val stack = mutable.Stack[(Int, Int, Boolean)]()
    stack.push((0, -1, false))

    while (stack.nonEmpty) {
      val (node, parent, visited) = stack.pop()
      if (!visited) {
        stack.push((node, parent, true))
        for (nb <- adj(node)) {
          if (nb != parent) stack.push((nb, node, false))
        }
      } else {
        var sum = valsLong(node)
        for (nb <- adj(node)) {
          if (nb != parent) sum += sub(nb)
        }
        val mod = sum % kk
        if (mod == 0L) {
          count += 1
          sub(node) = 0L
        } else {
          sub(node) = mod
        }
      }
    }

    count
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_k_divisible_components(n: i32, edges: Vec<Vec<i32>>, values: Vec<i32>, k: i32) -> i32 {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n_usize];
        for e in edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }
        let vals: Vec<i64> = values.iter().map(|&x| x as i64).collect();
        let k_i64 = k as i64;
        let mut cnt: i32 = 0;

        fn dfs(
            u: usize,
            parent: usize,
            adj: &Vec<Vec<usize>>,
            vals: &Vec<i64>,
            k: i64,
            cnt: &mut i32,
        ) -> i64 {
            let mut sum = vals[u];
            for &v in &adj[u] {
                if v != parent {
                    sum += dfs(v, u, adj, vals, k, cnt);
                }
            }
            let rem = sum % k;
            if rem == 0 {
                *cnt += 1;
                0
            } else {
                rem
            }
        }

        // Use a sentinel parent index that is out of bounds.
        dfs(0, n_usize, &adj, &vals, k_i64, &mut cnt);
        cnt
    }
}
```

## Racket

```racket
(define/contract (max-k-divisible-components n edges values k)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof exact-integer?)
      exact-integer?
      exact-integer?)
  (let* ((adj (make-vector n '()))                     ; adjacency list
         (add-edge
          (lambda (u v)
            (vector-set! adj u (cons v (vector-ref adj u)))
            (vector-set! adj v (cons u (vector-ref adj v))))))
    ;; build adjacency
    (for-each (lambda (e)
                (let ((u (list-ref e 0))
                      (v (list-ref e 1)))
                  (add-edge u v)))
              edges)

    ;; iterative DFS to get parent array and traversal order
    (define parent (make-vector n -2))                 ; -2 = unvisited, root will become -1
    (vector-set! parent 0 -1)                         ; root
    (define stack (list 0))
    (define preorder '())
    (let loop ()
      (when (not (null? stack))
        (let* ((node (car stack))
               (rest (cdr stack)))
          (set! stack rest)
          (set! preorder (cons node preorder))
          (for-each (lambda (nbr)
                      (when (= (vector-ref parent nbr) -2)
                        (vector-set! parent nbr node)
                        (set! stack (cons nbr stack))))
                    (vector-ref adj node)))
        (loop)))

    ;; sums modulo k for each node
    (define sumvec (make-vector n 0))
    (do ((i 0 (+ i 1))) ((= i n))
      (vector-set! sumvec i (modulo (list-ref values i) k)))

    (define count 0)

    ;; process nodes in post‑order (reverse of preorder)
    (for ([node (in-list (reverse preorder))])
      (let ((rem (vector-ref sumvec node)))
        (when (= rem 0)
          (set! count (+ count 1))))
      (let ((par (vector-ref parent node)))
        (unless (= par -1)                     ; root has no parent
          (let* ((rem (vector-ref sumvec node))
                 (contrib (if (= rem 0) 0 rem))
                 (new-sum (modulo (+ (vector-ref sumvec par) contrib) k)))
            (vector-set! sumvec par new-sum)))))

    count))
```

## Erlang

```erlang
-spec max_k_divisible_components(N :: integer(), Edges :: [[integer()]], Values :: [integer()], K :: integer()) -> integer().
max_k_divisible_components(N, Edges, Values, K) ->
    Adj = build_adj(Edges, #{}),
    ValMap = maps:from_list(lists:zip(lists:seq(0, N - 1), Values)),
    {_, Count} = dfs(0, -1, Adj, ValMap, K),
    Count.

build_adj([], Map) ->
    Map;
build_adj([[A, B] | Rest], Map) ->
    M1 = add_edge(Map, A, B),
    M2 = add_edge(M1, B, A),
    build_adj(Rest, M2).

add_edge(Map, From, To) ->
    Old = maps:get(From, Map, []),
    maps:put(From, [To | Old], Map).

dfs(Node, Parent, Adj, ValMap, K) ->
    Neigh = maps:get(Node, Adj, []),
    {Sum, Count} =
        lists:foldl(
            fun(Child, {AccS, AccC}) ->
                if
                    Child == Parent -> {AccS, AccC};
                    true ->
                        {Rem, Cnt} = dfs(Child, Node, Adj, ValMap, K),
                        {(AccS + Rem) rem K, AccC + Cnt}
                end
            end,
            {0, 0},
            Neigh
        ),
    Total = (Sum + maps:get(Node, ValMap)) rem K,
    if
        Total == 0 -> {0, Count + 1};
        true -> {Total, Count}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_k_divisible_components(integer, [[integer]], [integer], integer) :: integer
  def max_k_divisible_components(n, edges, values, k) do
    adj =
      Enum.reduce(0..(n - 1), %{}, fn i, acc -> Map.put(acc, i, []) end)
      |> Enum.reduce(edges, fn [a, b], acc ->
        acc
        |> Map.update!(a, fn list -> [b | list] end)
        |> Map.update!(b, fn list -> [a | list] end)
      end)

    {_rem, cnt} = dfs(0, -1, adj, values, k)
    cnt
  end

  defp dfs(node, parent, adj, values, k) do
    {sum, cnt} =
      Enum.reduce(Map.get(adj, node, []), {rem(values[node], k), 0}, fn child,
                                                                        {s, c} ->
        if child == parent do
          {s, c}
        else
          {child_rem, child_cnt} = dfs(child, node, adj, values, k)
          new_sum = rem(s + child_rem, k)
          {new_sum, c + child_cnt}
        end
      end)

    if sum == 0 do
      {0, cnt + 1}
    else
      {sum, cnt}
    end
  end
end
```

# 3528. Unit Conversion I

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> baseUnitConversions(vector<vector<int>>& conversions) {
        const long long MOD = 1000000007LL;
        int n = (int)conversions.size() + 1;
        vector<vector<pair<int,long long>>> adj(n);
        for (const auto& conv : conversions) {
            int src = conv[0];
            int tgt = conv[1];
            long long w = conv[2];
            adj[src].push_back({tgt, w});
        }
        vector<int> ans(n, 0);
        queue<int> q;
        ans[0] = 1;
        q.push(0);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (auto [v, w] : adj[u]) {
                ans[v] = (int)((ans[u] * w) % MOD);
                q.push(v);
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
    private static final long MOD = 1_000_000_007L;
    
    public int[] baseUnitConversions(int[][] conversions) {
        int n = conversions.length + 1;
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] conv : conversions) {
            int src = conv[0];
            int tgt = conv[1];
            int factor = conv[2];
            graph[src].add(new int[]{tgt, factor});
        }
        
        long[] resLong = new long[n];
        resLong[0] = 1L;
        Deque<Integer> dq = new ArrayDeque<>();
        dq.add(0);
        while (!dq.isEmpty()) {
            int u = dq.pollFirst();
            for (int[] edge : graph[u]) {
                int v = edge[0];
                long w = edge[1];
                resLong[v] = (resLong[u] * w) % MOD;
                dq.add(v);
            }
        }
        
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = (int) resLong[i];
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def baseUnitConversions(self, conversions):
        """
        :type conversions: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(conversions) + 1
        adj = [[] for _ in range(n)]
        for u, v, f in conversions:
            adj[u].append((v, f))
        res = [0] * n
        res[0] = 1
        from collections import deque
        q = deque([0])
        while q:
            u = q.popleft()
            for v, f in adj[u]:
                res[v] = (res[u] * f) % MOD
                q.append(v)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(conversions) + 1
        graph = [[] for _ in range(n)]
        for src, tgt, factor in conversions:
            graph[src].append((tgt, factor))
        result = [0] * n
        result[0] = 1
        stack = [0]
        while stack:
            u = stack.pop()
            for v, w in graph[u]:
                result[v] = (result[u] * w) % MOD
                stack.append(v)
        return result
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

#define MOD 1000000007LL

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* baseUnitConversions(int** conversions, int conversionsSize, int* conversionsColSize, int* returnSize) {
    int m = conversionsSize;               // number of edges
    int n = m + 1;                         // number of nodes

    // adjacency list (directed)
    int *head = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;

    int *to   = (int*)malloc(m * sizeof(int));
    long long *w = (long long*)malloc(m * sizeof(long long));
    int *next = (int*)malloc(m * sizeof(int));

    for (int i = 0; i < m; ++i) {
        int src = conversions[i][0];
        int tgt = conversions[i][1];
        long long factor = conversions[i][2] % MOD;
        to[i]   = tgt;
        w[i]    = factor;
        next[i] = head[src];
        head[src] = i;
    }

    int *ans = (int*)malloc(n * sizeof(int));
    bool *vis = (bool*)calloc(n, sizeof(bool));

    // BFS/DFS from node 0
    int *queue = (int*)malloc(n * sizeof(int));
    int front = 0, back = 0;
    queue[back++] = 0;
    ans[0] = 1;
    vis[0] = true;

    while (front < back) {
        int u = queue[front++];
        for (int e = head[u]; e != -1; e = next[e]) {
            int v = to[e];
            if (!vis[v]) {
                ans[v] = (int)((ans[u] * w[e]) % MOD);
                vis[v] = true;
                queue[back++] = v;
            }
        }
    }

    // clean up auxiliary structures
    free(head);
    free(to);
    free(w);
    free(next);
    free(vis);
    free(queue);

    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const long MOD = 1000000007L;
    
    public int[] BaseUnitConversions(int[][] conversions) {
        int n = conversions.Length + 1;
        var adj = new List<(int to, long factor)>(n);
        for (int i = 0; i < n; i++) adj.Add((0,0)); // placeholder
        
        foreach (var conv in conversions) {
            int src = conv[0];
            int tgt = conv[1];
            long f = conv[2];
            adj[src].Add((tgt, f));
        }
        
        var result = new long[n];
        result[0] = 1;
        var queue = new Queue<int>();
        queue.Enqueue(0);
        
        while (queue.Count > 0) {
            int u = queue.Dequeue();
            foreach (var edge in adj[u]) {
                int v = edge.to;
                long f = edge.factor;
                result[v] = (result[u] * f) % MOD;
                queue.Enqueue(v);
            }
        }
        
        var ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = (int)result[i];
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} conversions
 * @return {number[]}
 */
var baseUnitConversions = function(conversions) {
    const MOD = 1000000007n;
    const n = conversions.length + 1;
    const adj = Array.from({length: n}, () => []);
    for (const [src, tgt, factor] of conversions) {
        adj[src].push([tgt, BigInt(factor)]);
    }
    const res = new Array(n).fill(0n);
    res[0] = 1n;
    const queue = [0];
    let qIdx = 0;
    while (qIdx < queue.length) {
        const u = queue[qIdx++];
        for (const [v, f] of adj[u]) {
            res[v] = (res[u] * f) % MOD;
            queue.push(v);
        }
    }
    return res.map(v => Number(v));
};
```

## Typescript

```typescript
function baseUnitConversions(conversions: number[][]): number[] {
    const MOD = 1000000007n;
    const n = conversions.length + 1;
    const adj: Array<Array<[number, number]>> = Array.from({ length: n }, () => []);
    for (const [src, tgt, factor] of conversions) {
        adj[src].push([tgt, factor]);
    }
    const result = new Array<number>(n);
    result[0] = 1;
    const queue: number[] = [0];
    for (let i = 0; i < queue.length; i++) {
        const u = queue[i];
        const curVal = BigInt(result[u]);
        for (const [v, f] of adj[u]) {
            const val = (curVal * BigInt(f)) % MOD;
            result[v] = Number(val);
            queue.push(v);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $conversions
     * @return Integer[]
     */
    function baseUnitConversions($conversions) {
        $mod = 1000000007;
        $n = count($conversions) + 1;
        $adj = array_fill(0, $n, []);
        foreach ($conversions as $conv) {
            [$src, $tgt, $fac] = $conv;
            $adj[$src][] = [$tgt, $fac];
        }
        $res = array_fill(0, $n, 0);
        $res[0] = 1;
        $queue = new SplQueue();
        $queue->enqueue(0);
        while (!$queue->isEmpty()) {
            $u = $queue->dequeue();
            foreach ($adj[$u] as $edge) {
                [$v, $f] = $edge;
                $res[$v] = ($res[$u] * $f) % $mod;
                $queue->enqueue($v);
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func baseUnitConversions(_ conversions: [[Int]]) -> [Int] {
        let MOD = Int64(1_000_000_007)
        let n = conversions.count + 1
        var adj = Array(repeating: [(to: Int, weight: Int)](), count: n)
        for conv in conversions {
            let src = conv[0]
            let tgt = conv[1]
            let w = conv[2]
            adj[src].append((to: tgt, weight: w))
        }
        var result = Array(repeating: 0, count: n)
        result[0] = 1
        var queue = [Int]()
        var head = 0
        queue.append(0)
        while head < queue.count {
            let u = queue[head]
            head += 1
            for edge in adj[u] {
                let v = edge.to
                let w = Int64(edge.weight)
                let val = (Int64(result[u]) * w) % MOD
                result[v] = Int(val)
                queue.append(v)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun baseUnitConversions(conversions: Array<IntArray>): IntArray {
        val MOD = 1_000_000_007L
        val n = conversions.size + 1
        val adj = Array(n) { mutableListOf<Pair<Int, Long>>() }
        for (c in conversions) {
            val u = c[0]
            val v = c[1]
            val w = c[2].toLong()
            adj[u].add(Pair(v, w))
        }
        val res = LongArray(n)
        res[0] = 1L
        val q: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
        q.add(0)
        while (!q.isEmpty()) {
            val u = q.poll()
            for ((v, w) in adj[u]) {
                res[v] = (res[u] * w) % MOD
                q.add(v)
            }
        }
        val ans = IntArray(n)
        for (i in 0 until n) {
            ans[i] = (res[i] % MOD).toInt()
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class _Edge {
  final int to;
  final int weight;
  _Edge(this.to, this.weight);
}

class Solution {
  static const int _MOD = 1000000007;

  List<int> baseUnitConversions(List<List<int>> conversions) {
    // Determine number of nodes (n)
    int maxNode = 0;
    for (var conv in conversions) {
      maxNode = max(maxNode, conv[0]);
      maxNode = max(maxNode, conv[1]);
    }
    final int n = maxNode + 1;

    // Build adjacency list (directed tree rooted at 0)
    final List<List<_Edge>> graph = List.generate(n, (_) => []);
    for (var conv in conversions) {
      final int u = conv[0];
      final int v = conv[1];
      final int w = conv[2] % _MOD;
      graph[u].add(_Edge(v, w));
    }

    // BFS/DFS to compute conversion values
    final List<int> result = List.filled(n, 0);
    final List<int> queue = [0];
    result[0] = 1;
    int head = 0;

    while (head < queue.length) {
      final int cur = queue[head++];
      for (final _Edge e in graph[cur]) {
        result[e.to] = (result[cur] * e.weight) % _MOD;
        queue.add(e.to);
      }
    }

    return result;
  }
}
```

## Golang

```go
func baseUnitConversions(conversions [][]int) []int {
	const MOD int64 = 1000000007
	n := len(conversions) + 1

	type edge struct {
		to int
		w  int
	}
	adj := make([][]edge, n)
	for _, c := range conversions {
		u, v, f := c[0], c[1], c[2]
		adj[u] = append(adj[u], edge{to: v, w: f})
	}

	res := make([]int, n)
	type nodeInfo struct {
		idx int
		val int64
	}
	queue := []nodeInfo{{idx: 0, val: 1}}
	visited := make([]bool, n)
	visited[0] = true

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		res[cur.idx] = int(cur.val % MOD)

		for _, e := range adj[cur.idx] {
			if !visited[e.to] {
				visited[e.to] = true
				newVal := (cur.val * int64(e.w)) % MOD
				queue = append(queue, nodeInfo{idx: e.to, val: newVal})
			}
		}
	}

	return res
}
```

## Ruby

```ruby
def base_unit_conversions(conversions)
  mod = 1_000_000_007
  n = conversions.length + 1
  adj = Array.new(n) { [] }
  conversions.each do |src, tgt, w|
    adj[src] << [tgt, w]
  end

  result = Array.new(n, 0)
  result[0] = 1
  queue = [0]
  idx = 0

  while idx < queue.size
    u = queue[idx]
    idx += 1
    cur = result[u]
    adj[u].each do |v, w|
      result[v] = (cur * w) % mod
      queue << v
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def baseUnitConversions(conversions: Array[Array[Int]]): Array[Int] = {
        val MOD = 1000000007L
        var n = 0
        for (c <- conversions) {
            n = math.max(n, math.max(c(0), c(1)) + 1)
        }
        val adj = Array.fill[List[(Int, Long)]](n)(Nil)
        for (c <- conversions) {
            val s = c(0)
            val t = c(1)
            val f = c(2).toLong
            adj(s) = (t, f) :: adj(s)
        }
        val res = new Array[Long](n)
        res(0) = 1L
        val queue = scala.collection.mutable.ArrayDeque[Int]()
        queue.append(0)
        while (queue.nonEmpty) {
            val u = queue.removeHead()
            val cur = res(u)
            for ((v, f) <- adj(u)) {
                res(v) = (cur * f) % MOD
                queue.append(v)
            }
        }
        res.map(_.toInt)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn base_unit_conversions(conversions: Vec<Vec<i32>>) -> Vec<i32> {
        let n = conversions.len() + 1;
        let mut adj: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n];
        for conv in &conversions {
            let src = conv[0] as usize;
            let tgt = conv[1] as usize;
            let f = conv[2] as i64;
            adj[src].push((tgt, f));
        }
        const MOD: i64 = 1_000_000_007;
        let mut res: Vec<i64> = vec![0; n];
        res[0] = 1;
        let mut deque = std::collections::VecDeque::new();
        deque.push_back(0usize);
        while let Some(u) = deque.pop_front() {
            let cur = res[u];
            for &(v, w) in &adj[u] {
                let val = ((cur as i128 * w as i128) % MOD as i128) as i64;
                res[v] = val;
                deque.push_back(v);
            }
        }
        res.into_iter().map(|x| x as i32).collect()
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (base-unit-conversions conversions)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((m (length conversions))
         (n (+ m 1))
         (adj (make-vector n '()))
         (res (make-vector n 0)))
    ;; build adjacency list
    (for-each (lambda (conv)
                (match conv
                  [(list s t f)
                   (vector-set! adj s (cons (list t f) (vector-ref adj s)))]))
              conversions)
    (vector-set! res 0 1)

    ;; BFS using mutable queue
    (let ((queue (make-vector n 0))
          (head 0)
          (tail 0))
      (define (enqueue x)
        (vector-set! queue tail x)
        (set! tail (+ tail 1)))
      (define (dequeue)
        (let ((x (vector-ref queue head)))
          (set! head (+ head 1))
          x))
      (enqueue 0)
      (let bfs ()
        (when (< head tail)
          (define node (dequeue))
          (for-each (lambda (edge)
                      (match edge
                        [(list nb factor)
                         (vector-set! res nb
                                      (modulo (* (vector-ref res node) factor) MOD))
                         (enqueue nb)]))
                    (vector-ref adj node))
          (bfs))))
    ;; convert result vector to list
    (for/list ([i (in-range n)]) (vector-ref res i))))
```

## Erlang

```erlang
-module(solution).
-export([base_unit_conversions/1]).

-spec base_unit_conversions(Conversions :: [[integer()]]) -> [integer()].
base_unit_conversions(Conversions) ->
    Mod = 1000000007,
    N = length(Conversions) + 1,
    Adj = build_adj(Conversions, #{}),
    ValuesMap = dfs([{0,1}], Adj, Mod, #{}),
    lists:map(fun(I) -> maps:get(I, ValuesMap) end, lists:seq(0, N-1)).

build_adj([], Acc) ->
    Acc;
build_adj([[S,T,F]|Rest], Acc) ->
    Updated = maps:update_with(S,
        fun(L) -> [{T,F}|L] end,
        [{T,F}],
        Acc),
    build_adj(Rest, Updated).

dfs([], _Adj, _Mod, Values) ->
    Values;
dfs([{Node,Val}|Stack], Adj, Mod, Values) ->
    NewValues = maps:put(Node, Val, Values),
    Children = maps:get(Node, Adj, []),
    NewStack = lists:foldl(
        fun({Child,W}, Acc) ->
            ChildVal = (Val * W) rem Mod,
            [{Child,ChildVal}|Acc]
        end,
        Stack,
        Children),
    dfs(NewStack, Adj, Mod, NewValues).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec base_unit_conversions(conversions :: [[integer]]) :: [integer]
  def base_unit_conversions(conversions) do
    n = length(conversions) + 1
    mod = 1_000_000_007

    adj =
      Enum.reduce(conversions, :array.new(n, default: []), fn [src, tgt, f], acc ->
        list = :array.get(src, acc)
        :array.set(src, [{tgt, f} | list], acc)
      end)

    res0 = :array.new(n, default: 0) |> :array.set(0, 1)
    queue0 = :queue.from_list([0])

    final_res = bfs(queue0, res0, adj, mod)

    Enum.map(0..n - 1, fn i -> :array.get(i, final_res) end)
  end

  defp bfs(queue, res, adj, mod) do
    case :queue.out(queue) do
      {:empty, _} ->
        res

      {{:value, node}, q_rest} ->
        cur = :array.get(node, res)
        edges = :array.get(node, adj)

        {res2, q2} =
          Enum.reduce(edges, {res, q_rest}, fn {tgt, f}, {r_acc, q_acc} ->
            val = rem(cur * f, mod)
            r_new = :array.set(tgt, val, r_acc)
            {r_new, :queue.in_r(tgt, q_acc)}
          end)

        bfs(q2, res2, adj, mod)
    end
  end
end
```

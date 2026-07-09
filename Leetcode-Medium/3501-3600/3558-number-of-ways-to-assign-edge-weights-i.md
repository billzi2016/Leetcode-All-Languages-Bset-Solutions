# 3558. Number of Ways to Assign Edge Weights I

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const int MOD = 1'000'000'007;
    
    long long modPow(long long base, long long exp) {
        long long res = 1;
        while (exp > 0) {
            if (exp & 1) res = res * base % MOD;
            base = base * base % MOD;
            exp >>= 1;
        }
        return res;
    }
    
    int assignEdgeWeights(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        vector<vector<int>> adj(n + 1);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vector<int> depth(n + 1, -1);
        queue<int> q;
        depth[1] = 0;
        q.push(1);
        int maxDepth = 0;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : adj[u]) {
                if (depth[v] == -1) {
                    depth[v] = depth[u] + 1;
                    maxDepth = max(maxDepth, depth[v]);
                    q.push(v);
                }
            }
        }
        // number of ways with odd count of 1's among maxDepth edges
        long long ans = modPow(2, maxDepth - 1);
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;

    public int assignEdgeWeights(int[][] edges) {
        int n = edges.length + 1;
        @SuppressWarnings("unchecked")
        java.util.ArrayList<Integer>[] adj = new java.util.ArrayList[n + 1];
        for (int i = 1; i <= n; i++) adj[i] = new java.util.ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            adj[u].add(v);
            adj[v].add(u);
        }

        int[] depth = new int[n + 1];
        boolean[] visited = new boolean[n + 1];
        java.util.ArrayDeque<Integer> queue = new java.util.ArrayDeque<>();
        queue.add(1);
        visited[1] = true;
        int maxDepth = 0;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            int d = depth[node];
            if (d > maxDepth) maxDepth = d;
            for (int nb : adj[node]) {
                if (!visited[nb]) {
                    visited[nb] = true;
                    depth[nb] = d + 1;
                    queue.add(nb);
                }
            }
        }

        // number of ways = 2^(maxDepth-1) mod MOD
        long ans = powMod(2L, Math.max(0, maxDepth - 1));
        return (int) ans;
    }

    private long powMod(long base, int exp) {
        long res = 1L;
        long b = base % MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = (res * b) % MOD;
            }
            b = (b * b) % MOD;
            exp >>= 1;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        from collections import deque
        depth = [-1] * (n + 1)
        q = deque([1])
        depth[1] = 0
        max_depth = 0

        while q:
            node = q.popleft()
            d = depth[node]
            if d > max_depth:
                max_depth = d
            for nb in g[node]:
                if depth[nb] == -1:
                    depth[nb] = d + 1
                    q.append(nb)

        # number of ways with odd sum = 2^{max_depth-1}
        return pow(2, max_depth - 1, MOD) if max_depth > 0 else 0
```

## Python3

```python
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        stack = [(1, 0)]  # (node, depth)
        visited = [False] * (n + 1)
        visited[1] = True
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            if depth > max_depth:
                max_depth = depth
            for nb in adj[node]:
                if not visited[nb]:
                    visited[nb] = True
                    stack.append((nb, depth + 1))

        if max_depth == 0:
            return 0
        return pow(2, max_depth - 1, MOD)
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define MOD 1000000007

typedef struct {
    int to;
    int next;
} EdgeNode;

static long long modPow(long long base, long long exp) {
    long long res = 1;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

int assignEdgeWeights(int** edges, int edgesSize, int* edgesColSize){
    int n = edgesSize + 1;
    int *head = (int*)calloc(n + 1, sizeof(int));
    for (int i = 0; i <= n; ++i) head[i] = -1;

    EdgeNode *elist = (EdgeNode*)malloc(sizeof(EdgeNode) * (2 * edgesSize));
    int idx = 0;
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        elist[idx].to = v;
        elist[idx].next = head[u];
        head[u] = idx++;
        elist[idx].to = u;
        elist[idx].next = head[v];
        head[v] = idx++;
    }

    int *depth = (int*)malloc(sizeof(int) * (n + 1));
    for (int i = 0; i <= n; ++i) depth[i] = -1;

    int *queue = (int*)malloc(sizeof(int) * (n + 5));
    int front = 0, rear = 0;
    queue[rear++] = 1;
    depth[1] = 0;

    while (front < rear) {
        int u = queue[front++];
        for (int e = head[u]; e != -1; e = elist[e].next) {
            int v = elist[e].to;
            if (depth[v] == -1) {
                depth[v] = depth[u] + 1;
                queue[rear++] = v;
            }
        }
    }

    int maxDepth = 0;
    for (int i = 1; i <= n; ++i) {
        if (depth[i] > maxDepth) maxDepth = depth[i];
    }

    long long ans = 0;
    if (maxDepth > 0) {
        ans = modPow(2, maxDepth - 1);
    }
    
    free(head);
    free(elist);
    free(depth);
    free(queue);
    return (int)ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const int MOD = 1000000007;
    
    public int AssignEdgeWeights(int[][] edges) {
        int n = edges.Length + 1;
        var graph = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            graph[u].Add(v);
            graph[v].Add(u);
        }
        
        var depth = new int[n + 1];
        var visited = new bool[n + 1];
        var queue = new Queue<int>();
        queue.Enqueue(1);
        visited[1] = true;
        int maxDepth = 0;
        
        while (queue.Count > 0) {
            int u = queue.Dequeue();
            foreach (int v in graph[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    depth[v] = depth[u] + 1;
                    if (depth[v] > maxDepth) maxDepth = depth[v];
                    queue.Enqueue(v);
                }
            }
        }
        
        // Number of ways with odd sum = 2^(maxDepth-1)
        long result = ModPow(2, Math.Max(0, maxDepth - 1));
        return (int)result;
    }
    
    private long ModPow(long baseVal, int exp) {
        long res = 1;
        long b = baseVal % MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = (res * b) % MOD;
            }
            b = (b * b) % MOD;
            exp >>= 1;
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @return {number}
 */
var assignEdgeWeights = function(edges) {
    const n = edges.length + 1;
    const adj = Array.from({ length: n + 1 }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    const visited = new Uint8Array(n + 1);
    const depth = new Int32Array(n + 1);
    const queue = new Array(n);
    let head = 0, tail = 0;
    queue[tail++] = 1;
    visited[1] = 1;
    let maxDepth = 0;
    while (head < tail) {
        const node = queue[head++];
        const d = depth[node];
        if (d > maxDepth) maxDepth = d;
        for (const nb of adj[node]) {
            if (!visited[nb]) {
                visited[nb] = 1;
                depth[nb] = d + 1;
                queue[tail++] = nb;
            }
        }
    }
    const MOD = 1000000007n;
    let exp = BigInt(maxDepth - 1);
    if (exp < 0n) return 0; // should not happen for n >= 2
    let base = 2n, res = 1n;
    while (exp > 0n) {
        if (exp & 1n) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1n;
    }
    return Number(res);
};
```

## Typescript

```typescript
function assignEdgeWeights(edges: number[][]): number {
    const n = edges.length + 1;
    const adj: number[][] = Array.from({ length: n + 1 }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const depth = new Int32Array(n + 1);
    const visited = new Uint8Array(n + 1);
    const stack: number[] = [1];
    visited[1] = 1;
    let maxDepth = 0;

    while (stack.length) {
        const node = stack.pop()!;
        for (const nb of adj[node]) {
            if (!visited[nb]) {
                visited[nb] = 1;
                depth[nb] = depth[node] + 1;
                if (depth[nb] > maxDepth) maxDepth = depth[nb];
                stack.push(nb);
            }
        }
    }

    const MOD = 1000000007n;
    function modPow(base: bigint, exp: number): bigint {
        let result = 1n;
        let b = base % MOD;
        let e = BigInt(exp);
        while (e > 0) {
            if ((e & 1n) === 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    }

    const ans = modPow(2n, maxDepth - 1);
    return Number(ans);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @return Integer
     */
    function assignEdgeWeights($edges) {
        $mod = 1000000007;
        $n = count($edges) + 1;
        $adj = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            [$u, $v] = $e;
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }

        // DFS to find maximum depth from root (node 1)
        $stack = [[1, 0, 0]]; // node, parent, depth
        $maxDepth = 0;
        while ($stack) {
            [$node, $parent, $depth] = array_pop($stack);
            if ($depth > $maxDepth) {
                $maxDepth = $depth;
            }
            foreach ($adj[$node] as $nei) {
                if ($nei === $parent) continue;
                $stack[] = [$nei, $node, $depth + 1];
            }
        }

        // Number of ways = 2^(maxDepth-1) mod MOD
        $exp = $maxDepth - 1;
        $ans = $this->modPow(2, $exp, $mod);
        return $ans;
    }

    private function modPow($base, $exp, $mod) {
        $result = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD: Int64 = 1_000_000_007

    func assignEdgeWeights(_ edges: [[Int]]) -> Int {
        let n = edges.count + 1
        var graph = Array(repeating: [Int](), count: n + 1)
        for e in edges {
            let u = e[0], v = e[1]
            graph[u].append(v)
            graph[v].append(u)
        }

        var visited = Array(repeating: false, count: n + 1)
        var depth = Array(repeating: 0, count: n + 1)

        var queue = [Int]()
        var head = 0
        queue.append(1)
        visited[1] = true
        var maxDepth = 0

        while head < queue.count {
            let node = queue[head]
            head += 1
            for nb in graph[node] {
                if !visited[nb] {
                    visited[nb] = true
                    depth[nb] = depth[node] + 1
                    if depth[nb] > maxDepth { maxDepth = depth[nb] }
                    queue.append(nb)
                }
            }
        }

        // number of ways = 2^(maxDepth-1) mod MOD
        let exponent = maxDepth - 1
        let result = modPow(2, exponent)
        return Int(result)
    }

    private func modPow(_ base: Int64, _ exp: Int) -> Int64 {
        var result: Int64 = 1
        var b = base % MOD
        var e = exp
        while e > 0 {
            if e & 1 == 1 {
                result = (result * b) % MOD
            }
            b = (b * b) % MOD
            e >>= 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun assignEdgeWeights(edges: Array<IntArray>): Int {
        val n = edges.size + 1
        val adj = Array(n + 1) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        val depth = IntArray(n + 1) { -1 }
        val deque: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
        depth[1] = 0
        deque.add(1)

        var maxDepth = 0
        while (!deque.isEmpty()) {
            val u = deque.poll()
            for (v in adj[u]) {
                if (depth[v] == -1) {
                    depth[v] = depth[u] + 1
                    if (depth[v] > maxDepth) maxDepth = depth[v]
                    deque.add(v)
                }
            }
        }

        val MOD = 1_000_000_007L
        var result = 1L
        var exp = maxDepth - 1
        var base = 2L % MOD
        var e = exp
        while (e > 0) {
            if ((e and 1) == 1) result = (result * base) % MOD
            base = (base * base) % MOD
            e = e shr 1
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int assignEdgeWeights(List<List<int>> edges) {
    int n = edges.length + 1;
    List<List<int>> adj = List.generate(n + 1, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      adj[u].add(v);
      adj[v].add(u);
    }

    List<int> depth = List.filled(n + 1, -1);
    List<int> stack = [1];
    depth[1] = 0;
    int maxDepth = 0;

    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      for (int nb in adj[node]) {
        if (depth[nb] == -1) {
          depth[nb] = depth[node] + 1;
          if (depth[nb] > maxDepth) maxDepth = depth[nb];
          stack.add(nb);
        }
      }
    }

    // Number of ways = 2^(maxDepth-1) mod MOD
    int exp = maxDepth - 1;
    return _powMod(2, exp);
  }

  int _powMod(int base, int exp) {
    int result = 1;
    int b = base % _mod;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * b) % _mod;
      }
      b = (b * b) % _mod;
      exp >>= 1;
    }
    return result;
  }
}
```

## Golang

```go
package main

import (
	"math/bits"
)

const MOD int64 = 1e9 + 7

func assignEdgeWeights(edges [][]int) int {
	n := len(edges) + 1
	adj := make([][]int, n+1)
	for _, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}

	depth := make([]int, n+1)
	visited := make([]bool, n+1)
	queue := make([]int, 0, n)
	queue = append(queue, 1)
	visited[1] = true
	maxDepth := 0

	for i := 0; i < len(queue); i++ {
		u := queue[i]
		if depth[u] > maxDepth {
			maxDepth = depth[u]
		}
		for _, v := range adj[u] {
			if !visited[v] {
				visited[v] = true
				depth[v] = depth[u] + 1
				queue = append(queue, v)
			}
		}
	}

	exp := maxDepth - 1
	if exp < 0 {
		return 0
	}
	result := modPow(2, int64(exp), MOD)
	return int(result)
}

// fast exponentiation modulo MOD
func modPow(base, exp, mod int64) int64 {
	var res int64 = 1
	b := base % mod
	e := exp
	for e > 0 {
		if e&1 == 1 {
			res = (res * b) % mod
		}
		b = (b * b) % mod
		e >>= 1
	}
	return res
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(base, exp, mod)
  result = 1
  b = base % mod
  e = exp
  while e > 0
    result = (result * b) % mod if (e & 1) == 1
    b = (b * b) % mod
    e >>= 1
  end
  result
end

def assign_edge_weights(edges)
  n = edges.size + 1
  adj = Array.new(n + 1) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  depth = Array.new(n + 1, -1)
  queue = [1]
  depth[1] = 0
  idx = 0
  max_depth = 0

  while idx < queue.size
    node = queue[idx]
    idx += 1
    cur_d = depth[node]
    adj[node].each do |nbr|
      next if depth[nbr] != -1
      depth[nbr] = cur_d + 1
      max_depth = depth[nbr] if depth[nbr] > max_depth
      queue << nbr
    end
  end

  return 0 if max_depth == 0
  mod_pow(2, max_depth - 1, MOD)
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007L

    private def modPow(base: Long, exp: Int): Long = {
        var result = 1L
        var b = base % MOD
        var e = exp
        while (e > 0) {
            if ((e & 1) == 1) result = (result * b) % MOD
            b = (b * b) % MOD
            e >>= 1
        }
        result
    }

    def assignEdgeWeights(edges: Array[Array[Int]]): Int = {
        val n = edges.length + 1
        val adj = Array.fill(n + 1)(new scala.collection.mutable.ArrayBuffer[Int]())
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            adj(u).append(v)
            adj(v).append(u)
        }

        import java.util.ArrayDeque
        val depth = Array.fill(n + 1)(-1)
        val q = new ArrayDeque[Int]()
        depth(1) = 0
        q.add(1)

        var maxDepth = 0
        while (!q.isEmpty) {
            val u = q.poll()
            for (v <- adj(u)) {
                if (depth(v) == -1) {
                    depth(v) = depth(u) + 1
                    if (depth(v) > maxDepth) maxDepth = depth(v)
                    q.add(v)
                }
            }
        }

        // path length equals maxDepth (number of edges from root to deepest node)
        val ans = modPow(2L, maxDepth - 1).toInt
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn assign_edge_weights(edges: Vec<Vec<i32>>) -> i32 {
        let n = edges.len() + 1;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n + 1];
        for e in &edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }

        let mut visited = vec![false; n + 1];
        let mut stack: Vec<(usize, i64)> = Vec::new();
        stack.push((1, 0));
        visited[1] = true;
        let mut max_depth: i64 = 0;

        while let Some((node, depth)) = stack.pop() {
            if depth > max_depth {
                max_depth = depth;
            }
            for &nbr in &adj[node] {
                if !visited[nbr] {
                    visited[nbr] = true;
                    stack.push((nbr, depth + 1));
                }
            }
        }

        const MOD: i64 = 1_000_000_007;
        // max_depth >= 1 because n >= 2
        let mut exp = (max_depth - 1) as u64;
        let mut base: i64 = 2;
        let mut result: i64 = 1;
        while exp > 0 {
            if exp & 1 == 1 {
                result = result * base % MOD;
            }
            base = base * base % MOD;
            exp >>= 1;
        }
        result as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(: modpow : Integer Integer -> Integer)
(define (modpow base exp)
  (let loop ([b (remainder base MOD)] [e exp] [res 1])
    (if (= e 0)
        res
        (let* ([res2 (if (odd? e) (remainder (* res b) MOD) res)]
               [b2   (remainder (* b b) MOD)])
          (loop b2 (quotient e 2) res2)))))

(: assign-edge-weights : (Listof (List Integer Integer)) -> Integer)
(define (assign-edge-weights edges)
  (let* ([n (+ (length edges) 1)]
         [adj (make-vector (+ n 1) '())])
    ;; build adjacency list
    (for ([e edges])
      (define u (first e))
      (define v (second e))
      (vector-set! adj u (cons v (vector-ref adj u)))
      (vector-set! adj v (cons u (vector-ref adj v))))
    ;; BFS to compute depths
    (define depth (make-vector (+ n 1) -1))
    (vector-set! depth 1 0)
    (define queue (make-vector n 0))
    (define head 0)
    (define tail 0)
    (vector-set! queue tail 1)
    (set! tail (+ tail 1))
    (let bfs ()
      (when (< head tail)
        (define node (vector-ref queue head))
        (set! head (+ head 1))
        (for ([nbr (in-list (vector-ref adj node))])
          (when (= (vector-ref depth nbr) -1)
            (vector-set! depth nbr (+ (vector-ref depth node) 1))
            (vector-set! queue tail nbr)
            (set! tail (+ tail 1))))
        (bfs)))
    (bfs)
    ;; find maximum depth
    (define maxd 0)
    (for ([i (in-range 1 (+ n 1))])
      (define d (vector-ref depth i))
      (when (> d maxd) (set! maxd d)))
    (if (< maxd 1)
        0
        (modpow 2 (- maxd 1)))))
```

## Erlang

```erlang
-module(solution).
-export([assign_edge_weights/1]).

-define(MOD, 1000000007).

assign_edge_weights(Edges) ->
    Adj = build_adj(Edges, #{}),
    MaxDepth = bfs([{1,0}], #{1 => true}, Adj, 0),
    Exp = MaxDepth - 1,
    pow_mod(2, Exp, ?MOD).

build_adj([], Map) -> Map;
build_adj([[U,V]|Rest], Map) ->
    M1 = maps:update_with(U, fun(L) -> [V|L] end, [V], Map),
    M2 = maps:update_with(V, fun(L) -> [U|L] end, [U], M1),
    build_adj(Rest, M2).

bfs([], _Visited, _Adj, MaxDepth) ->
    MaxDepth;
bfs([{Node, Depth}|Queue], Visited, Adj, CurMax) ->
    NewMax = if Depth > CurMax -> Depth; true -> CurMax end,
    Neighs = maps:get(Node, Adj, []),
    {NewQueue, NewVisited} =
        lists:foldl(fun(Nei, {Q, V}) ->
            case maps:is_key(Nei, V) of
                true -> {Q, V};
                false -> {[{Nei, Depth+1}|Q], maps:put(Nei, true, V)}
            end
        end, {Queue, Visited}, Neighs),
    bfs(NewQueue, NewVisited, Adj, NewMax).

pow_mod(_, 0, Mod) ->
    1 rem Mod;
pow_mod(Base, Exp, Mod) when (Exp band 1) =:= 0 ->
    Half = pow_mod((Base * Base) rem Mod, Exp bsr 1, Mod),
    Half;
pow_mod(Base, Exp, Mod) ->
    (Base * pow_mod(Base, Exp - 1, Mod)) rem Mod.
```

## Elixir

```elixir
defmodule Solution do
  @spec assign_edge_weights(edges :: [[integer]]) :: integer
  def assign_edge_weights(edges) do
    mod = 1_000_000_007
    adj = build_adj(edges, %{})
    max_depth = bfs_max_depth(adj)
    mod_pow(2, max_depth - 1, mod)
  end

  defp build_adj([], adj), do: adj

  defp build_adj([[u, v] | rest], adj) do
    adj =
      Map.update(adj, u, [v], fn list -> [v | list] end)

    adj =
      Map.update(adj, v, [u], fn list -> [u | list] end)

    build_adj(rest, adj)
  end

  defp bfs_max_depth(adj) do
    queue = :queue.new() |> :queue.in({1, 0})
    visited = MapSet.new([1])
    bfs(queue, visited, adj, 0)
  end

  defp bfs(queue, visited, adj, max_depth) do
    case :queue.out(queue) do
      {:empty, _} ->
        max_depth

      {{:value, {node, depth}}, q} ->
        new_max = if depth > max_depth, do: depth, else: max_depth
        neighbors = Map.get(adj, node, [])

        {new_queue, new_visited} =
          Enum.reduce(neighbors, {q, visited}, fn nb, {q_acc, vis_acc} ->
            if MapSet.member?(vis_acc, nb) do
              {q_acc, vis_acc}
            else
              {
                :queue.in({nb, depth + 1}, q_acc),
                MapSet.put(vis_acc, nb)
              }
            end
          end)

        bfs(new_queue, new_visited, adj, new_max)
    end
  end

  defp mod_pow(_base, 0, _mod), do: 1

  defp mod_pow(base, exp, mod) when rem(exp, 2) == 0 do
    half = mod_pow(base, div(exp, 2), mod)
    rem(half * half, mod)
  end

  defp mod_pow(base, exp, mod) do
    rem(base * mod_pow(base, exp - 1, mod), mod)
  end
end
```

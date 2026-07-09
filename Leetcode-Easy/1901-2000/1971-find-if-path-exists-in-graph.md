# 1971. Find if Path Exists in Graph

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> parent, size;
        DSU(int n) : parent(n), size(n,1) {
            iota(parent.begin(), parent.end(), 0);
        }
        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        void unite(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return;
            if (size[a] < size[b]) swap(a,b);
            parent[b] = a;
            size[a] += size[b];
        }
    };
    
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        DSU dsu(n);
        for (const auto& e : edges) {
            dsu.unite(e[0], e[1]);
        }
        return dsu.find(source) == dsu.find(destination);
    }
};
```

## Java

```java
class Solution {
    private int[] parent;
    private int[] rank;

    private int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    private void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        if (rootA == rootB) return;
        if (rank[rootA] < rank[rootB]) {
            parent[rootA] = rootB;
        } else if (rank[rootA] > rank[rootB]) {
            parent[rootB] = rootA;
        } else {
            parent[rootB] = rootA;
            rank[rootA]++;
        }
    }

    public boolean validPath(int n, int[][] edges, int source, int destination) {
        if (source == destination) return true;
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        for (int[] edge : edges) {
            union(edge[0], edge[1]);
        }
        return find(source) == find(destination);
    }
}
```

## Python

```python
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source == destination:
            return True

        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        for u, v in edges:
            union(u, v)

        return find(source) == find(destination)
```

## Python3

```python
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        for u, v in edges:
            union(u, v)

        return find(source) == find(destination)
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

static int find(int *parent, int x) {
    if (parent[x] != x) {
        parent[x] = find(parent, parent[x]);
    }
    return parent[x];
}

static void unite(int *parent, int *rank, int a, int b) {
    int rootA = find(parent, a);
    int rootB = find(parent, b);
    if (rootA == rootB) return;
    if (rank[rootA] < rank[rootB]) {
        parent[rootA] = rootB;
    } else if (rank[rootA] > rank[rootB]) {
        parent[rootB] = rootA;
    } else {
        parent[rootB] = rootA;
        rank[rootA]++;
    }
}

bool validPath(int n, int** edges, int edgesSize, int* edgesColSize, int source, int destination) {
    int *parent = (int *)malloc(n * sizeof(int));
    int *rank = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) parent[i] = i;

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        unite(parent, rank, u, v);
    }

    bool result = find(parent, source) == find(parent, destination);

    free(parent);
    free(rank);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    private class DSU
    {
        private readonly int[] parent;
        private readonly int[] rank;

        public DSU(int size)
        {
            parent = new int[size];
            rank = new int[size];
            for (int i = 0; i < size; i++)
                parent[i] = i;
        }

        public int Find(int x)
        {
            while (parent[x] != x)
            {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        public void Union(int a, int b)
        {
            int pa = Find(a);
            int pb = Find(b);
            if (pa == pb) return;

            if (rank[pa] < rank[pb])
                parent[pa] = pb;
            else if (rank[pa] > rank[pb])
                parent[pb] = pa;
            else
            {
                parent[pb] = pa;
                rank[pa]++;
            }
        }
    }

    public bool ValidPath(int n, int[][] edges, int source, int destination)
    {
        if (source == destination) return true;

        var dsu = new DSU(n);
        foreach (var e in edges)
        {
            dsu.Union(e[0], e[1]);
        }

        return dsu.Find(source) == dsu.Find(destination);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
var validPath = function(n, edges, source, destination) {
    if (source === destination) return true;
    const parent = new Array(n);
    const rank = new Array(n).fill(0);
    for (let i = 0; i < n; i++) parent[i] = i;

    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };

    const union = (a, b) => {
        let ra = find(a), rb = find(b);
        if (ra === rb) return;
        if (rank[ra] < rank[rb]) {
            parent[ra] = rb;
        } else if (rank[ra] > rank[rb]) {
            parent[rb] = ra;
        } else {
            parent[rb] = ra;
            rank[ra]++;
        }
    };

    for (const [u, v] of edges) {
        union(u, v);
    }

    return find(source) === find(destination);
};
```

## Typescript

```typescript
function validPath(n: number, edges: number[][], source: number, destination: number): boolean {
    if (source === destination) return true;

    class UnionFind {
        parent: number[];
        size: number[];
        constructor(size: number) {
            this.parent = new Array(size);
            this.size = new Array(size);
            for (let i = 0; i < size; i++) {
                this.parent[i] = i;
                this.size[i] = 1;
            }
        }
        find(x: number): number {
            let root = x;
            while (this.parent[root] !== root) {
                root = this.parent[root];
            }
            // path compression
            while (this.parent[x] !== x) {
                const next = this.parent[x];
                this.parent[x] = root;
                x = next;
            }
            return root;
        }
        union(a: number, b: number): void {
            let ra = this.find(a);
            let rb = this.find(b);
            if (ra === rb) return;
            // union by size
            if (this.size[ra] < this.size[rb]) {
                [ra, rb] = [rb, ra];
            }
            this.parent[rb] = ra;
            this.size[ra] += this.size[rb];
        }
    }

    const uf = new UnionFind(n);
    for (const [u, v] of edges) {
        uf.union(u, v);
    }
    return uf.find(source) === uf.find(destination);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $source
     * @param Integer $destination
     * @return Boolean
     */
    function validPath($n, $edges, $source, $destination) {
        if ($source === $destination) {
            return true;
        }

        // Disjoint Set Union (Union-Find)
        $parent = [];
        $rank = [];

        for ($i = 0; $i < $n; $i++) {
            $parent[$i] = $i;
            $rank[$i] = 0;
        }

        $find = function($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) {
                $parent[$x] = $find($parent[$x]);
            }
            return $parent[$x];
        };

        $union = function($x, $y) use (&$parent, &$rank, $find) {
            $px = $find($x);
            $py = $find($y);
            if ($px === $py) {
                return;
            }
            if ($rank[$px] < $rank[$py]) {
                $parent[$px] = $py;
            } elseif ($rank[$px] > $rank[$py]) {
                $parent[$py] = $px;
            } else {
                $parent[$py] = $px;
                $rank[$px]++;
            }
        };

        foreach ($edges as $e) {
            $union($e[0], $e[1]);
        }

        return $find($source) === $find($destination);
    }
}
```

## Swift

```swift
class UnionFind {
    private var parent: [Int]
    private var rank: [Int]

    init(_ n: Int) {
        parent = Array(0..<n)
        rank = [Int](repeating: 0, count: n)
    }

    func find(_ x: Int) -> Int {
        var node = x
        while parent[node] != node {
            parent[node] = parent[parent[node]]
            node = parent[node]
        }
        return node
    }

    func union(_ a: Int, _ b: Int) {
        let rootA = find(a)
        let rootB = find(b)
        if rootA == rootB { return }
        if rank[rootA] < rank[rootB] {
            parent[rootA] = rootB
        } else if rank[rootA] > rank[rootB] {
            parent[rootB] = rootA
        } else {
            parent[rootB] = rootA
            rank[rootA] += 1
        }
    }
}

class Solution {
    func validPath(_ n: Int, _ edges: [[Int]], _ source: Int, _ destination: Int) -> Bool {
        if source == destination { return true }
        let uf = UnionFind(n)
        for edge in edges {
            uf.union(edge[0], edge[1])
        }
        return uf.find(source) == uf.find(destination)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validPath(n: Int, edges: Array<IntArray>, source: Int, destination: Int): Boolean {
        if (source == destination) return true
        val parent = IntArray(n) { it }

        fun find(x: Int): Int {
            var p = x
            while (parent[p] != p) {
                parent[p] = parent[parent[p]]
                p = parent[p]
            }
            return p
        }

        fun union(a: Int, b: Int) {
            val pa = find(a)
            val pb = find(b)
            if (pa != pb) {
                parent[pa] = pb
            }
        }

        for (e in edges) {
            union(e[0], e[1])
        }

        return find(source) == find(destination)
    }
}
```

## Dart

```dart
class Solution {
  bool validPath(int n, List<List<int>> edges, int source, int destination) {
    var dsu = _DSU(n);
    for (var edge in edges) {
      dsu.union(edge[0], edge[1]);
    }
    return dsu.find(source) == dsu.find(destination);
  }
}

class _DSU {
  late List<int> parent;
  late List<int> rank;

  _DSU(int size) {
    parent = List.generate(size, (i) => i);
    rank = List.filled(size, 0);
  }

  int find(int x) {
    while (parent[x] != x) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return x;
  }

  void union(int a, int b) {
    int pa = find(a);
    int pb = find(b);
    if (pa == pb) return;
    if (rank[pa] < rank[pb]) {
      parent[pa] = pb;
    } else if (rank[pa] > rank[pb]) {
      parent[pb] = pa;
    } else {
      parent[pb] = pa;
      rank[pa]++;
    }
  }
}
```

## Golang

```go
package main

type DSU struct {
	parent []int
	rank   []int
}

func NewDSU(n int) *DSU {
	p := make([]int, n)
	r := make([]int, n)
	for i := 0; i < n; i++ {
		p[i] = i
	}
	return &DSU{parent: p, rank: r}
}

func (d *DSU) Find(x int) int {
	if d.parent[x] != x {
		d.parent[x] = d.Find(d.parent[x])
	}
	return d.parent[x]
}

func (d *DSU) Union(a, b int) {
	ra := d.Find(a)
	rb := d.Find(b)
	if ra == rb {
		return
	}
	if d.rank[ra] < d.rank[rb] {
		d.parent[ra] = rb
	} else if d.rank[ra] > d.rank[rb] {
		d.parent[rb] = ra
	} else {
		d.parent[rb] = ra
		d.rank[ra]++
	}
}

func validPath(n int, edges [][]int, source int, destination int) bool {
	if source == destination {
		return true
	}
	ds := NewDSU(n)
	for _, e := range edges {
		u, v := e[0], e[1]
		ds.Union(u, v)
	}
	return ds.Find(source) == ds.Find(destination)
}
```

## Ruby

```ruby
def valid_path(n, edges, source, destination)
  parent = Array.new(n) { |i| i }
  size = Array.new(n, 1)

  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  union = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    return if ra == rb
    if size[ra] < size[rb]
      ra, rb = rb, ra
    end
    parent[rb] = ra
    size[ra] += size[rb]
  end

  edges.each { |u, v| union.call(u, v) }

  find.call(source) == find.call(destination)
end
```

## Scala

```scala
object Solution {
    def validPath(n: Int, edges: Array[Array[Int]], source: Int, destination: Int): Boolean = {
        if (source == destination) return true
        val parent = new Array[Int](n)
        val size = new Array[Int](n)
        var i = 0
        while (i < n) {
            parent(i) = i
            size(i) = 1
            i += 1
        }
        def find(x: Int): Int = {
            var p = x
            while (parent(p) != p) {
                parent(p) = parent(parent(p))
                p = parent(p)
            }
            p
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
        for (e <- edges) {
            union(e(0), e(1))
        }
        find(source) == find(destination)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn valid_path(n: i32, edges: Vec<Vec<i32>>, source: i32, destination: i32) -> bool {
        if source == destination {
            return true;
        }
        let n_usize = n as usize;
        #[derive(Clone)]
        struct UnionFind {
            parent: Vec<usize>,
            rank: Vec<u8>,
        }
        impl UnionFind {
            fn new(size: usize) -> Self {
                UnionFind {
                    parent: (0..size).collect(),
                    rank: vec![0; size],
                }
            }
            fn find(&mut self, x: usize) -> usize {
                if self.parent[x] != x {
                    let root = self.find(self.parent[x]);
                    self.parent[x] = root;
                }
                self.parent[x]
            }
            fn union(&mut self, a: usize, b: usize) {
                let mut ra = self.find(a);
                let mut rb = self.find(b);
                if ra == rb {
                    return;
                }
                // union by rank
                if self.rank[ra] < self.rank[rb] {
                    std::mem::swap(&mut ra, &mut rb);
                }
                self.parent[rb] = ra;
                if self.rank[ra] == self.rank[rb] {
                    self.rank[ra] += 1;
                }
            }
        }

        let mut uf = UnionFind::new(n_usize);
        for edge in edges.iter() {
            let u = edge[0] as usize;
            let v = edge[1] as usize;
            uf.union(u, v);
        }
        let src = source as usize;
        let dst = destination as usize;
        uf.find(src) == uf.find(dst)
    }
}
```

## Racket

```racket
(define/contract (valid-path n edges source destination)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer? boolean?)
  (let* ([parent (make-vector n)]
         [rank   (make-vector n 0)])
    ;; initialize each node as its own parent
    (for ([i (in-range n)]) (vector-set! parent i i))
    
    (define (find x)
      (let loop ((x x))
        (let ([p (vector-ref parent x)])
          (if (= p x)
              x
              (let ([root (loop p)])
                (vector-set! parent x root)
                root)))))
    
    (define (union a b)
      (let* ([ra (find a)]
             [rb (find b)])
        (when (not (= ra rb))
          (let ([rank-a (vector-ref rank ra)]
                [rank-b (vector-ref rank rb)])
            (cond
              [(< rank-a rank-b) (vector-set! parent ra rb)]
              [(> rank-a rank-b) (vector-set! parent rb ra)]
              [else
               (vector-set! parent rb ra)
               (vector-set! rank ra (+ rank-a 1))])))))
    
    ;; unite all edges
    (for ([e edges])
      (let* ([u (first e)] [v (second e)])
        (union u v)))
    
    (= (find source) (find destination))))
```

## Erlang

```erlang
-module(solution).
-export([valid_path/4]).

-spec valid_path(N :: integer(), Edges :: [[integer()]], Source :: integer(), Destination :: integer()) -> boolean().
valid_path(_N, Edges, Source, Destination) ->
    case Source =:= Destination of
        true -> true;
        false ->
            Adj = build_adj(Edges),
            Queue0 = queue:in(Source, queue:new()),
            Visited0 = maps:put(Source, true, #{}),
            bfs(Destination, Adj, Queue0, Visited0)
    end.

build_adj(Edges) ->
    lists:foldl(fun([U,V], Acc) ->
        Acc1 = maps:update_with(U,
                fun(L) -> [V|L] end,
                [V],
                Acc),
        maps:update_with(V,
                fun(L) -> [U|L] end,
                [U],
                Acc1)
    end, #{}, Edges).

bfs(Dest, Adj, Queue, Visited) ->
    case queue:is_empty(Queue) of
        true -> false;
        false ->
            {{value, Node}, Q2} = queue:out(Queue),
            if Node =:= Dest ->
                    true;
               true ->
                    Neighs = maps:get(Node, Adj, []),
                    {Q3, Visited1} = lists:foldl(fun(Nbr, {QAcc, Vis}) ->
                        case maps:is_key(Nbr, Vis) of
                            true -> {QAcc, Vis};
                            false -> {queue:in(Nbr, QAcc), maps:put(Nbr, true, Vis)}
                        end
                    end, {Q2, Visited}, Neighs),
                    bfs(Dest, Adj, Q3, Visited1)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec valid_path(integer, [[integer]], integer, integer) :: boolean
  def valid_path(_n, edges, source, destination) do
    if source == destination do
      true
    else
      bfs(build_adj(edges), source, destination)
    end
  end

  defp build_adj(edges) do
    Enum.reduce(edges, %{}, fn [u, v], acc ->
      acc
      |> Map.update(u, [v], &[v | &1])
      |> Map.update(v, [u], &[u | &1])
    end)
  end

  defp bfs(adj, source, destination) do
    queue = :queue.in(source, :queue.new())
    visited = MapSet.put(MapSet.new(), source)
    bfs_loop(queue, adj, destination, visited)
  end

  defp bfs_loop(queue, _adj, destination, _visited) when :queue.is_empty(queue), do: false

  defp bfs_loop(queue, adj, destination, visited) do
    {{:value, node}, q} = :queue.out(queue)

    if node == destination do
      true
    else
      {new_queue, new_visited} =
        Enum.reduce(Map.get(adj, node, []), {q, visited}, fn neighbor, {q_acc, vis_acc} ->
          if MapSet.member?(vis_acc, neighbor) do
            {q_acc, vis_acc}
          else
            {:queue.in(neighbor, q_acc), MapSet.put(vis_acc, neighbor)}
          end
        end)

      bfs_loop(new_queue, adj, destination, new_visited)
    end
  end
end
```

# 1319. Number of Operations to Make Network Connected

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> parent, rank;
        int cnt;
        DSU(int n) : parent(n), rank(n, 0), cnt(n) {
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
            --cnt;
            if (rank[a] < rank[b]) swap(a, b);
            parent[b] = a;
            if (rank[a] == rank[b]) ++rank[a];
        }
        int components() const { return cnt; }
    };
    
    int makeConnected(int n, vector<vector<int>>& connections) {
        if ((int)connections.size() < n - 1) return -1;
        DSU dsu(n);
        for (auto& e : connections) {
            dsu.unite(e[0], e[1]);
        }
        return dsu.components() - 1;
    }
};
```

## Java

```java
class Solution {
    public int makeConnected(int n, int[][] connections) {
        if (connections.length < n - 1) return -1;
        DSU dsu = new DSU(n);
        for (int[] c : connections) {
            dsu.union(c[0], c[1]);
        }
        int components = 0;
        for (int i = 0; i < n; i++) {
            if (dsu.find(i) == i) components++;
        }
        return components - 1;
    }

    private static class DSU {
        int[] parent, rank;

        DSU(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }

        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }

        void union(int a, int b) {
            int pa = find(a), pb = find(b);
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
}
```

## Python

```python
class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n - 1:
            return -1

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
            return True

        for a, b in connections:
            union(a, b)

        components = sum(1 for i in range(n) if find(i) == i)
        return components - 1
```

## Python3

```python
from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

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

        for a, b in connections:
            union(a, b)

        components = sum(1 for i in range(n) if find(i) == i)
        return components - 1
```

## C

```c
static int find_root(int x, int *parent) {
    if (parent[x] != x)
        parent[x] = find_root(parent[x], parent);
    return parent[x];
}

static void union_set(int a, int b, int *parent, int *rank) {
    int ra = find_root(a, parent);
    int rb = find_root(b, parent);
    if (ra == rb) return;
    if (rank[ra] < rank[rb]) {
        parent[ra] = rb;
    } else if (rank[ra] > rank[rb]) {
        parent[rb] = ra;
    } else {
        parent[rb] = ra;
        rank[ra]++;
    }
}

int makeConnected(int n, int** connections, int connectionsSize, int* connectionsColSize) {
    if (connectionsSize < n - 1)
        return -1;

    int *parent = (int *)malloc(n * sizeof(int));
    int *rank   = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i)
        parent[i] = i;

    for (int i = 0; i < connectionsSize; ++i) {
        int a = connections[i][0];
        int b = connections[i][1];
        union_set(a, b, parent, rank);
    }

    int components = 0;
    for (int i = 0; i < n; ++i)
        if (find_root(i, parent) == i)
            ++components;

    free(parent);
    free(rank);

    return components - 1;
}
```

## Csharp

```csharp
public class Solution
{
    public int MakeConnected(int n, int[][] connections)
    {
        if (connections.Length < n - 1) return -1;

        var uf = new UnionFind(n);
        foreach (var conn in connections)
        {
            uf.Union(conn[0], conn[1]);
        }

        int components = 0;
        for (int i = 0; i < n; i++)
        {
            if (uf.Find(i) == i) components++;
        }
        return components - 1;
    }

    private class UnionFind
    {
        private readonly int[] parent;
        private readonly int[] rank;

        public UnionFind(int size)
        {
            parent = new int[size];
            rank = new int[size];
            for (int i = 0; i < size; i++)
                parent[i] = i;
        }

        public int Find(int x)
        {
            if (parent[x] != x)
                parent[x] = Find(parent[x]);
            return parent[x];
        }

        public void Union(int x, int y)
        {
            int rootX = Find(x);
            int rootY = Find(y);
            if (rootX == rootY) return;

            if (rank[rootX] < rank[rootY])
                parent[rootX] = rootY;
            else if (rank[rootX] > rank[rootY])
                parent[rootY] = rootX;
            else
            {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var makeConnected = function(n, connections) {
    if (connections.length < n - 1) return -1;
    
    const parent = new Array(n);
    const rank = new Array(n).fill(0);
    for (let i = 0; i < n; i++) parent[i] = i;
    
    function find(x) {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }
    
    function union(a, b) {
        let ra = find(a), rb = find(b);
        if (ra === rb) return false;
        if (rank[ra] < rank[rb]) {
            parent[ra] = rb;
        } else if (rank[ra] > rank[rb]) {
            parent[rb] = ra;
        } else {
            parent[rb] = ra;
            rank[ra]++;
        }
        return true;
    }
    
    for (const [a, b] of connections) {
        union(a, b);
    }
    
    const roots = new Set();
    for (let i = 0; i < n; i++) {
        roots.add(find(i));
    }
    
    return roots.size - 1;
};
```

## Typescript

```typescript
function makeConnected(n: number, connections: number[][]): number {
    if (connections.length < n - 1) return -1;

    const parent = new Array<number>(n);
    const rank = new Array<number>(n).fill(0);
    for (let i = 0; i < n; i++) parent[i] = i;

    function find(x: number): number {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    function union(a: number, b: number): void {
        let rootA = find(a);
        let rootB = find(b);
        if (rootA === rootB) return;
        if (rank[rootA] < rank[rootB]) {
            parent[rootA] = rootB;
        } else if (rank[rootA] > rank[rootB]) {
            parent[rootB] = rootA;
        } else {
            parent[rootB] = rootA;
            rank[rootA]++;
        }
    }

    for (const [a, b] of connections) {
        union(a, b);
    }

    const components = new Set<number>();
    for (let i = 0; i < n; i++) {
        components.add(find(i));
    }

    return components.size - 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $connections
     * @return Integer
     */
    function makeConnected($n, $connections) {
        if (count($connections) < $n - 1) {
            return -1;
        }

        $parent = [];
        $rank   = [];

        for ($i = 0; $i < $n; $i++) {
            $parent[$i] = $i;
            $rank[$i]   = 0;
        }

        // Find with path compression
        $find = function($x) use (&$parent, &$find) {
            if ($parent[$x] != $x) {
                $parent[$x] = $find($parent[$x]);
            }
            return $parent[$x];
        };

        // Union by rank
        foreach ($connections as $conn) {
            [$a, $b] = $conn;
            $pa = $find($a);
            $pb = $find($b);
            if ($pa == $pb) continue;

            if ($rank[$pa] < $rank[$pb]) {
                $parent[$pa] = $pb;
            } elseif ($rank[$pa] > $rank[$pb]) {
                $parent[$pb] = $pa;
            } else {
                $parent[$pb] = $pa;
                $rank[$pa]++;
            }
        }

        $components = [];
        for ($i = 0; $i < $n; $i++) {
            $root = $find($i);
            $components[$root] = true;
        }

        return count($components) - 1;
    }
}
```

## Swift

```swift
class Solution {
    func makeConnected(_ n: Int, _ connections: [[Int]]) -> Int {
        if connections.count < n - 1 { return -1 }
        
        var parent = Array(0..<n)
        var rank = [Int](repeating: 0, count: n)
        
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
        
        for conn in connections {
            union(conn[0], conn[1])
        }
        
        var components = Set<Int>()
        for i in 0..<n {
            components.insert(find(i))
        }
        
        return components.count - 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun makeConnected(n: Int, connections: Array<IntArray>): Int {
        if (connections.size < n - 1) return -1
        val parent = IntArray(n) { it }
        val rank = IntArray(n)

        fun find(x: Int): Int {
            var v = x
            while (parent[v] != v) {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
        }

        fun union(a: Int, b: Int) {
            var x = find(a)
            var y = find(b)
            if (x == y) return
            if (rank[x] < rank[y]) {
                parent[x] = y
            } else if (rank[x] > rank[y]) {
                parent[y] = x
            } else {
                parent[y] = x
                rank[x]++
            }
        }

        for (edge in connections) {
            union(edge[0], edge[1])
        }

        val components = HashSet<Int>()
        for (i in 0 until n) {
            components.add(find(i))
        }
        return components.size - 1
    }
}
```

## Dart

```dart
class Solution {
  int makeConnected(int n, List<List<int>> connections) {
    if (connections.length < n - 1) return -1;
    var dsu = _DSU(n);
    for (var edge in connections) {
      dsu.union(edge[0], edge[1]);
    }
    var components = 0;
    for (int i = 0; i < n; i++) {
      if (dsu.find(i) == i) components++;
    }
    return components - 1;
  }
}

class _DSU {
  List<int> parent;
  List<int> rank;

  _DSU(int size)
      : parent = List.generate(size, (i) => i),
        rank = List.filled(size, 0);

  int find(int x) {
    if (parent[x] != x) {
      parent[x] = find(parent[x]);
    }
    return parent[x];
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
func makeConnected(n int, connections [][]int) int {
	if len(connections) < n-1 {
		return -1
	}
	parent := make([]int, n)
	rank := make([]int, n)
	for i := 0; i < n; i++ {
		parent[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		if parent[x] != x {
			parent[x] = find(parent[x])
		}
		return parent[x]
	}
	union := func(a, b int) bool {
		ra, rb := find(a), find(b)
		if ra == rb {
			return false
		}
		if rank[ra] < rank[rb] {
			parent[ra] = rb
		} else if rank[ra] > rank[rb] {
			parent[rb] = ra
		} else {
			parent[rb] = ra
			rank[ra]++
		}
		return true
	}

	components := n
	for _, e := range connections {
		if union(e[0], e[1]) {
			components--
		}
	}
	return components - 1
}
```

## Ruby

```ruby
def make_connected(n, connections)
  return -1 if connections.length < n - 1

  parent = Array.new(n) { |i| i }
  rank   = Array.new(n, 0)

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
    return false if ra == rb
    if rank[ra] < rank[rb]
      parent[ra] = rb
    elsif rank[ra] > rank[rb]
      parent[rb] = ra
    else
      parent[rb] = ra
      rank[ra] += 1
    end
    true
  end

  connections.each { |a, b| union.call(a, b) }

  roots = {}
  (0...n).each { |i| roots[find.call(i)] = true }

  roots.size - 1
end
```

## Scala

```scala
object Solution {
    def makeConnected(n: Int, connections: Array[Array[Int]]): Int = {
        if (connections.length < n - 1) return -1

        val parent = Array.tabulate(n)(i => i)
        val rank = new Array[Int](n)

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
            if (rank(ra) < rank(rb)) {
                parent(ra) = rb
            } else if (rank(ra) > rank(rb)) {
                parent(rb) = ra
            } else {
                parent(rb) = ra
                rank(ra) += 1
            }
        }

        for (c <- connections) {
            union(c(0), c(1))
        }

        var components = 0
        for (i <- 0 until n) {
            if (find(i) == i) components += 1
        }
        components - 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn make_connected(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        let n_usize = n as usize;
        if connections.len() < n_usize.saturating_sub(1) {
            return -1;
        }
        let mut dsu = DSU::new(n_usize);
        for conn in connections.iter() {
            let a = conn[0] as usize;
            let b = conn[1] as usize;
            dsu.union(a, b);
        }
        let mut components = 0;
        for i in 0..n_usize {
            if dsu.find(i) == i {
                components += 1;
            }
        }
        (components - 1) as i32
    }
}

struct DSU {
    parent: Vec<usize>,
    rank: Vec<usize>,
}

impl DSU {
    fn new(size: usize) -> Self {
        let mut parent = Vec::with_capacity(size);
        for i in 0..size {
            parent.push(i);
        }
        let rank = vec![0; size];
        DSU { parent, rank }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            let root = self.find(self.parent[x]);
            self.parent[x] = root;
        }
        self.parent[x]
    }

    fn union(&mut self, x: usize, y: usize) {
        let mut xr = self.find(x);
        let mut yr = self.find(y);
        if xr == yr {
            return;
        }
        if self.rank[xr] < self.rank[yr] {
            std::mem::swap(&mut xr, &mut yr);
        }
        self.parent[yr] = xr;
        if self.rank[xr] == self.rank[yr] {
            self.rank[xr] += 1;
        }
    }
}
```

## Racket

```racket
(require racket/match)

(define/contract (make-connected n connections)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let ([m (length connections)])
    (if (< m (- n 1))
        -1
        (let ([parent (make-vector n 0)]
              [rank   (make-vector n 0)])
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
          (for ([edge connections])
            (match-define (list a b) edge)
            (union a b))
          (let ([roots (make-hash)])
            (for ([i (in-range n)])
              (hash-set! roots (find i) #t))
            (- (hash-count roots) 1))))))
```

## Erlang

```erlang
-module(solution).
-export([make_connected/2]).

-spec make_connected(N :: integer(), Connections :: [[integer()]]) -> integer().
make_connected(N, Connections) ->
    case length(Connections) < N - 1 of
        true -> -1;
        false ->
            Adj = build_adj(Connections, #{}),
            Components = count_components(N, Adj),
            Components - 1
    end.

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

count_components(N, Adj) ->
    count_components(0, N, Adj, #{}, 0).

count_components(I, N, _Adj, Vis, Count) when I == N ->
    Count;
count_components(I, N, Adj, Vis, Count) ->
    case maps:is_key(I, Vis) of
        true ->
            count_components(I+1, N, Adj, Vis, Count);
        false ->
            NewVis = dfs([I], Adj, Vis),
            count_components(I+1, N, Adj, NewVis, Count+1)
    end.

dfs([], _Adj, Vis) -> Vis;
dfs([Node|Stack], Adj, Vis) ->
    case maps:is_key(Node, Vis) of
        true ->
            dfs(Stack, Adj, Vis);
        false ->
            Neigh = maps:get(Node, Adj, []),
            NewVis = maps:put(Node, true, Vis),
            dfs(Neigh ++ Stack, Adj, NewVis)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec make_connected(n :: integer, connections :: [[integer]]) :: integer
  def make_connected(n, connections) do
    m = length(connections)

    if m < n - 1 do
      -1
    else
      adj =
        Enum.reduce(connections, %{}, fn [a, b], acc ->
          acc
          |> Map.update(a, [b], &[b | &1])
          |> Map.update(b, [a], &[a | &1])
        end)

      {components, _visited} =
        Enum.reduce(0..(n - 1), {0, MapSet.new()}, fn node, {comp_cnt, visited} ->
          if MapSet.member?(visited, node) do
            {comp_cnt, visited}
          else
            {new_visited, _} = dfs(node, adj, visited)
            {comp_cnt + 1, new_visited}
          end
        end)

      components - 1
    end
  end

  defp dfs(start, adj, visited) do
    stack = [start]
    vis = MapSet.put(visited, start)
    dfs_loop(stack, adj, vis)
  end

  defp dfs_loop([], _adj, visited), do: {visited, nil}

  defp dfs_loop([node | rest], adj, visited) do
    neighbors = Map.get(adj, node, [])

    {new_stack, new_vis} =
      Enum.reduce(neighbors, {rest, visited}, fn nb, {stk, vis_acc} ->
        if MapSet.member?(vis_acc, nb) do
          {stk, vis_acc}
        else
          {[nb | stk], MapSet.put(vis_acc, nb)}
        end
      end)

    dfs_loop(new_stack, adj, new_vis)
  end
end
```

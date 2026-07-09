# 0684. Redundant Connection

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> parent(n + 1), sz(n + 1, 1);
        iota(parent.begin(), parent.end(), 0);
        
        function<int(int)> find = [&](int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        };
        
        auto unite = [&](int a, int b) -> bool {
            int ra = find(a), rb = find(b);
            if (ra == rb) return false; // already connected
            if (sz[ra] < sz[rb]) swap(ra, rb);
            parent[rb] = ra;
            sz[ra] += sz[rb];
            return true;
        };
        
        for (const auto& e : edges) {
            int u = e[0], v = e[1];
            if (!unite(u, v)) return e;
        }
        return {};
    }
};
```

## Java

```java
class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        int[] parent = new int[n + 1];
        int[] size = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            if (find(parent, u) == find(parent, v)) {
                return edge;
            }
            union(parent, size, u, v);
        }
        return new int[0]; // should never reach here
    }

    private int find(int[] parent, int x) {
        if (parent[x] != x) {
            parent[x] = find(parent, parent[x]);
        }
        return parent[x];
    }

    private void union(int[] parent, int[] size, int x, int y) {
        int rootX = find(parent, x);
        int rootY = find(parent, y);
        if (rootX == rootY) return;
        if (size[rootX] < size[rootY]) {
            parent[rootX] = rootY;
            size[rootY] += size[rootX];
        } else {
            parent[rootY] = rootX;
            size[rootX] += size[rootY];
        }
    }
}
```

## Python

```python
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        parent = [i for i in range(n + 1)]
        size = [1] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            if size[pu] < size[pv]:
                pu, pv = pv, pu
            parent[pv] = pu
            size[pu] += size[pv]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
```

## Python3

```python
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> bool:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
            return True

        redundant = []
        for u, v in edges:
            if not union(u, v):
                redundant = [u, v]
        return redundant
```

## C

```c
#include <stdlib.h>

static int find_set(int *parent, int x) {
    if (parent[x] != x)
        parent[x] = find_set(parent, parent[x]);
    return parent[x];
}

static void union_set(int *parent, int *rank, int x, int y) {
    int rx = find_set(parent, x);
    int ry = find_set(parent, y);
    if (rx == ry) return;
    if (rank[rx] < rank[ry]) {
        parent[rx] = ry;
    } else if (rank[rx] > rank[ry]) {
        parent[ry] = rx;
    } else {
        parent[ry] = rx;
        rank[rx]++;
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findRedundantConnection(int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    int n = edgesSize;
    int *parent = (int *)malloc((n + 1) * sizeof(int));
    int *rank   = (int *)calloc(n + 1, sizeof(int));
    for (int i = 1; i <= n; ++i) parent[i] = i;

    int *result = NULL;
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int pu = find_set(parent, u);
        int pv = find_set(parent, v);
        if (pu == pv) {
            result = (int *)malloc(2 * sizeof(int));
            result[0] = u;
            result[1] = v;
            *returnSize = 2;
            break;
        } else {
            union_set(parent, rank, u, v);
        }
    }

    free(parent);
    free(rank);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] FindRedundantConnection(int[][] edges)
    {
        int n = edges.Length;
        int[] parent = new int[n + 1];
        int[] rank = new int[n + 1];
        for (int i = 1; i <= n; i++) parent[i] = i;

        int Find(int x)
        {
            while (parent[x] != x)
            {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        bool Union(int a, int b)
        {
            int ra = Find(a);
            int rb = Find(b);
            if (ra == rb) return false;

            if (rank[ra] < rank[rb])
                parent[ra] = rb;
            else if (rank[ra] > rank[rb])
                parent[rb] = ra;
            else
            {
                parent[rb] = ra;
                rank[ra]++;
            }
            return true;
        }

        foreach (var edge in edges)
        {
            int u = edge[0];
            int v = edge[1];
            if (!Union(u, v))
                return new int[] { u, v };
        }

        return new int[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @return {number[]}
 */
var findRedundantConnection = function(edges) {
    const n = edges.length;
    const parent = new Array(n + 1);
    const rank = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) parent[i] = i;

    const find = (x) => {
        if (parent[x] !== x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    };

    const union = (a, b) => {
        let rootA = find(a);
        let rootB = find(b);
        if (rootA === rootB) return false; // already connected -> cycle
        if (rank[rootA] < rank[rootB]) {
            [rootA, rootB] = [rootB, rootA];
        }
        parent[rootB] = rootA;
        if (rank[rootA] === rank[rootB]) rank[rootA]++;
        return true;
    };

    for (const [u, v] of edges) {
        if (!union(u, v)) {
            return [u, v];
        }
    }
    return [];
};
```

## Typescript

```typescript
function findRedundantConnection(edges: number[][]): number[] {
    const n = edges.length;
    const parent = new Array(n + 1);
    const rank = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) parent[i] = i;

    function find(x: number): number {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    }

    function union(x: number, y: number): boolean {
        let rx = find(x);
        let ry = find(y);
        if (rx === ry) return false;
        if (rank[rx] < rank[ry]) {
            parent[rx] = ry;
        } else if (rank[rx] > rank[ry]) {
            parent[ry] = rx;
        } else {
            parent[ry] = rx;
            rank[rx]++;
        }
        return true;
    }

    for (const [u, v] of edges) {
        if (!union(u, v)) {
            return [u, v];
        }
    }
    return [];
}
```

## Php

```php
class Solution {
    private $parent = [];
    private $rank = [];

    private function find($x) {
        if ($this->parent[$x] != $x) {
            $this->parent[$x] = $this->find($this->parent[$x]);
        }
        return $this->parent[$x];
    }

    private function union($a, $b) {
        $rootA = $this->find($a);
        $rootB = $this->find($b);
        if ($rootA == $rootB) {
            return false;
        }
        if ($this->rank[$rootA] < $this->rank[$rootB]) {
            $this->parent[$rootA] = $rootB;
        } elseif ($this->rank[$rootA] > $this->rank[$rootB]) {
            $this->parent[$rootB] = $rootA;
        } else {
            $this->parent[$rootB] = $rootA;
            $this->rank[$rootA]++;
        }
        return true;
    }

    /**
     * @param Integer[][] $edges
     * @return Integer[]
     */
    function findRedundantConnection($edges) {
        $n = count($edges);
        for ($i = 1; $i <= $n; $i++) {
            $this->parent[$i] = $i;
            $this->rank[$i] = 0;
        }
        foreach ($edges as $edge) {
            [$u, $v] = $edge;
            if (!$this->union($u, $v)) {
                return $edge;
            }
        }
        return [];
    }
}
```

## Swift

```swift
class Solution {
    func findRedundantConnection(_ edges: [[Int]]) -> [Int] {
        let n = edges.count
        var parent = [Int](repeating: 0, count: n + 1)
        var rank = [Int](repeating: 1, count: n + 1)
        for i in 0...n { parent[i] = i }
        
        func find(_ x: Int) -> Int {
            if parent[x] != x {
                parent[x] = find(parent[x])
            }
            return parent[x]
        }
        
        func union(_ a: Int, _ b: Int) -> Bool {
            let rootA = find(a)
            let rootB = find(b)
            if rootA == rootB { return false }
            if rank[rootA] < rank[rootB] {
                parent[rootA] = rootB
            } else if rank[rootA] > rank[rootB] {
                parent[rootB] = rootA
            } else {
                parent[rootB] = rootA
                rank[rootA] += 1
            }
            return true
        }
        
        var result = [Int]()
        for edge in edges {
            let u = edge[0]
            let v = edge[1]
            if !union(u, v) {
                result = edge
                break
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findRedundantConnection(edges: Array<IntArray>): IntArray {
        val n = edges.size
        val parent = IntArray(n + 1) { it }
        val rank = IntArray(n + 1)

        fun find(x: Int): Int {
            var p = x
            while (parent[p] != p) {
                parent[p] = parent[parent[p]]
                p = parent[p]
            }
            return p
        }

        fun union(a: Int, b: Int): Boolean {
            var rootA = find(a)
            var rootB = find(b)
            if (rootA == rootB) return false
            if (rank[rootA] < rank[rootB]) {
                val tmp = rootA
                rootA = rootB
                rootB = tmp
            }
            parent[rootB] = rootA
            if (rank[rootA] == rank[rootB]) rank[rootA]++
            return true
        }

        for (edge in edges) {
            val u = edge[0]
            val v = edge[1]
            if (!union(u, v)) {
                return intArrayOf(u, v)
            }
        }
        return intArrayOf()
    }
}
```

## Dart

```dart
class Solution {
  List<int> findRedundantConnection(List<List<int>> edges) {
    int n = edges.length;
    List<int> parent = List.generate(n + 1, (i) => i);
    List<int> rank = List.filled(n + 1, 0);

    int find(int x) {
      if (parent[x] != x) {
        parent[x] = find(parent[x]);
      }
      return parent[x];
    }

    bool union(int a, int b) {
      int rootA = find(a);
      int rootB = find(b);
      if (rootA == rootB) return false;
      if (rank[rootA] < rank[rootB]) {
        parent[rootA] = rootB;
      } else if (rank[rootA] > rank[rootB]) {
        parent[rootB] = rootA;
      } else {
        parent[rootB] = rootA;
        rank[rootA]++;
      }
      return true;
    }

    for (var edge in edges) {
      int u = edge[0];
      int v = edge[1];
      if (!union(u, v)) {
        return edge;
      }
    }
    return <int>[];
  }
}
```

## Golang

```go
func findRedundantConnection(edges [][]int) []int {
	n := len(edges)
	parent := make([]int, n+1)
	size := make([]int, n+1)
	for i := 1; i <= n; i++ {
		parent[i] = i
		size[i] = 1
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
		if size[ra] < size[rb] {
			ra, rb = rb, ra
		}
		parent[rb] = ra
		size[ra] += size[rb]
		return true
	}
	for _, e := range edges {
		if !union(e[0], e[1]) {
			return []int{e[0], e[1]}
		}
	}
	return []int{}
}
```

## Ruby

```ruby
def find_redundant_connection(edges)
  n = edges.size
  parent = Array.new(n + 1) { |i| i }
  rank   = Array.new(n + 1, 0)

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

  edges.each do |u, v|
    return [u, v] unless union.call(u, v)
  end
  []
end
```

## Scala

```scala
object Solution {
    def findRedundantConnection(edges: Array[Array[Int]]): Array[Int] = {
        val n = edges.length
        val parent = new Array[Int](n + 1)
        val rank = new Array[Int](n + 1)
        for (i <- 0 to n) {
            parent(i) = i
            rank(i) = 0
        }

        def find(x: Int): Int = {
            if (parent(x) != x) {
                parent(x) = find(parent(x))
            }
            parent(x)
        }

        def union(x: Int, y: Int): Boolean = {
            var px = find(x)
            var py = find(y)
            if (px == py) return false
            if (rank(px) < rank(py)) {
                val tmp = px; px = py; py = tmp
            }
            parent(py) = px
            if (rank(px) == rank(py)) rank(px) += 1
            true
        }

        for (edge <- edges) {
            val u = edge(0)
            val v = edge(1)
            if (!union(u, v)) return edge
        }
        Array.empty[Int]
    }
}
```

## Rust

```rust
use std::cmp::max;

struct DSU {
    parent: Vec<usize>,
    rank: Vec<usize>,
}

impl DSU {
    fn new(size: usize) -> Self {
        let mut parent = vec![0; size + 1];
        for i in 0..=size {
            parent[i] = i;
        }
        DSU {
            parent,
            rank: vec![0; size + 1],
        }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            let root = self.find(self.parent[x]);
            self.parent[x] = root;
        }
        self.parent[x]
    }

    // Returns true if union succeeded, false if already in same set
    fn union(&mut self, x: usize, y: usize) -> bool {
        let xr = self.find(x);
        let yr = self.find(y);
        if xr == yr {
            return false;
        }
        if self.rank[xr] < self.rank[yr] {
            self.parent[xr] = yr;
        } else if self.rank[xr] > self.rank[yr] {
            self.parent[yr] = xr;
        } else {
            self.parent[yr] = xr;
            self.rank[xr] += 1;
        }
        true
    }
}

impl Solution {
    pub fn find_redundant_connection(edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = edges.len();
        let mut dsu = DSU::new(n);
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            if !dsu.union(u, v) {
                return vec![e[0], e[1]];
            }
        }
        Vec::new()
    }
}
```

## Racket

```racket
(define/contract (find-redundant-connection edges)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((n (length edges))
         (parent (make-vector n))
         (size   (make-vector n 1)))
    (for ([i (in-range n)])
      (vector-set! parent i i))
    (define (find x)
      (let loop ((x x))
        (let ((p (vector-ref parent x)))
          (if (= p x)
              x
              (let ((root (loop p)))
                (vector-set! parent x root)
                root)))))
    (define (union x y)
      (let ((rx (find x))
            (ry (find y)))
        (if (= rx ry)
            #f
            (begin
              (if (< (vector-ref size rx) (vector-ref size ry))
                  (begin
                    (vector-set! parent rx ry)
                    (vector-set! size ry (+ (vector-ref size ry)
                                            (vector-ref size rx))))
                  (begin
                    (vector-set! parent ry rx)
                    (vector-set! size rx (+ (vector-ref size rx)
                                            (vector-ref size ry)))))
              #t))))
    (let rec ((lst edges))
      (cond [(null? lst) '()] ; should never happen
            [else
             (let* ((edge (car lst))
                    (u (- (first edge) 1))
                    (v (- (second edge) 1)))
               (if (not (union u v))
                   edge
                   (rec (cdr lst))))]))))
```

## Erlang

```erlang
-module(solution).
-export([find_redundant_connection/1]).

-spec find_redundant_connection(Edges :: [[integer()]]) -> [integer()].
find_redundant_connection(Edges) ->
    N = length(Edges),
    Nodes = lists:seq(1, N),
    Parent0 = maps:from_list([{I, I} || I <- Nodes]),
    Size0   = maps:from_list([{I, 1} || I <- Nodes]),
    process_edges(Edges, Parent0, Size0).

process_edges([], _Parent, _Size) ->
    []; % should never reach here
process_edges([[U, V] | Rest], Parent, Size) ->
    {Ok, NewParent, NewSize} = union(U, V, Parent, Size),
    case Ok of
        false -> [U, V];
        true  -> process_edges(Rest, NewParent, NewSize)
    end.

union(U, V, Parent, Size) ->
    {RootU, P1} = find(U, Parent),
    {RootV, P2} = find(V, P1),
    if
        RootU == RootV ->
            {false, P2, Size};
        true ->
            SizeU = maps:get(RootU, Size),
            SizeV = maps:get(RootV, Size),
            if
                SizeU < SizeV ->
                    NewParent = maps:put(RootU, RootV, P2),
                    NewSize   = maps:put(RootV, SizeU + SizeV, Size);
                true ->
                    NewParent = maps:put(RootV, RootU, P2),
                    NewSize   = maps:put(RootU, SizeU + SizeV, Size)
            end,
            {true, NewParent, NewSize}
    end.

find(Node, Parent) ->
    case maps:get(Node, Parent) of
        Node -> {Node, Parent};
        P ->
            {Root, UpdatedParent} = find(P, Parent),
            {Root, maps:put(Node, Root, UpdatedParent)}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_redundant_connection(edges :: [[integer]]) :: [integer]
  def find_redundant_connection(edges) do
    n = length(edges)

    parent =
      Enum.reduce(1..n, %{}, fn i, acc ->
        Map.put(acc, i, i)
      end)

    size =
      Enum.reduce(1..n, %{}, fn i, acc ->
        Map.put(acc, i, 1)
      end)

    result =
      Enum.reduce_while(edges, {parent, size}, fn [u, v], {p, s} ->
        {ru, p1} = find(p, u)
        {rv, p2} = find(p1, v)

        if ru == rv do
          {:halt, {[u, v]}}
        else
          su = Map.get(s, ru)
          sv = Map.get(s, rv)

          if su < sv do
            p3 = Map.put(p2, ru, rv)
            s3 = Map.put(s, rv, su + sv)
            {:cont, {p3, s3}}
          else
            p3 = Map.put(p2, rv, ru)
            s3 = Map.put(s, ru, su + sv)
            {:cont, {p3, s3}}
          end
        end
      end)

    case result do
      {[u, v]} -> [u, v]
      _ -> []
    end
  end

  defp find(parent, x) do
    p = Map.get(parent, x)

    if p == x do
      {x, parent}
    else
      {root, parent2} = find(parent, p)
      parent3 = Map.put(parent2, x, root)
      {root, parent3}
    end
  end
end
```

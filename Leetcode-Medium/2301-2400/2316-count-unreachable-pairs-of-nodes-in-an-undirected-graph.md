# 2316. Count Unreachable Pairs of Nodes in an Undirected Graph

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> p, sz;
        DSU(int n): p(n), sz(n,1) { iota(p.begin(), p.end(), 0); }
        int find(int x){
            if(p[x]==x) return x;
            return p[x]=find(p[x]);
        }
        void unite(int a,int b){
            a=find(a);
            b=find(b);
            if(a==b) return;
            if(sz[a]<sz[b]) swap(a,b);
            p[b]=a;
            sz[a]+=sz[b];
        }
        int size(int x){ return sz[find(x)]; }
    };
    
    long long countPairs(int n, vector<vector<int>>& edges) {
        DSU dsu(n);
        for (auto &e: edges) {
            dsu.unite(e[0], e[1]);
        }
        unordered_map<int,long long> compSize;
        compSize.reserve(n*2);
        for (int i = 0; i < n; ++i) {
            int root = dsu.find(i);
            compSize[root] += 1;
        }
        long long totalPairs = 1LL * n * (n - 1) / 2;
        long long intra = 0;
        for (auto &kv : compSize) {
            long long sz = kv.second;
            intra += sz * (sz - 1) / 2;
        }
        return totalPairs - intra;
    }
};
```

## Java

```java
class Solution {
    public long countPairs(int n, int[][] edges) {
        DSU dsu = new DSU(n);
        for (int[] e : edges) {
            dsu.union(e[0], e[1]);
        }
        long[] compSize = new long[n];
        for (int i = 0; i < n; i++) {
            int root = dsu.find(i);
            compSize[root]++;
        }
        long totalPairs = ((long) n * (n - 1)) / 2;
        for (long sz : compSize) {
            if (sz > 1) {
                totalPairs -= sz * (sz - 1) / 2;
            }
        }
        return totalPairs;
    }

    private static class DSU {
        int[] parent;
        int[] size;

        DSU(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        int find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        void union(int a, int b) {
            int ra = find(a);
            int rb = find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb]) {
                int tmp = ra;
                ra = rb;
                rb = tmp;
            }
            parent[rb] = ra;
            size[ra] += size[rb];
        }
    }
}
```

## Python

```python
class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parent = list(range(n))
        sz = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if sz[ra] < sz[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            sz[ra] += sz[rb]

        for a, b in edges:
            union(a, b)

        comp_count = {}
        for i in range(n):
            root = find(i)
            comp_count[root] = comp_count.get(root, 0) + 1

        total_pairs = n * (n - 1) // 2
        reachable_inside = sum(c * (c - 1) // 2 for c in comp_count.values())
        return total_pairs - reachable_inside
```

## Python3

```python
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        for u, v in edges:
            union(u, v)

        comp_sizes = {}
        for i in range(n):
            root = find(i)
            comp_sizes[root] = comp_sizes.get(root, 0) + 1

        total_pairs = n * (n - 1) // 2
        reachable_pairs = sum(s * (s - 1) // 2 for s in comp_sizes.values())
        return total_pairs - reachable_pairs
```

## C

```c
#include <stdlib.h>

static int find(int *parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void unite(int *parent, long long *sz, int a, int b) {
    int ra = find(parent, a);
    int rb = find(parent, b);
    if (ra == rb) return;
    if (sz[ra] < sz[rb]) {
        parent[ra] = rb;
        sz[rb] += sz[ra];
    } else {
        parent[rb] = ra;
        sz[ra] += sz[rb];
    }
}

long long countPairs(int n, int** edges, int edgesSize, int* edgesColSize) {
    int *parent = (int *)malloc(n * sizeof(int));
    long long *sz = (long long *)malloc(n * sizeof(long long));
    for (int i = 0; i < n; ++i) {
        parent[i] = i;
        sz[i] = 1;
    }
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        unite(parent, sz, a, b);
    }
    long long total = (long long)n * (n - 1) / 2;
    long long subtract = 0;
    for (int i = 0; i < n; ++i) {
        if (parent[i] == i) {
            long long s = sz[i];
            subtract += s * (s - 1) / 2;
        }
    }
    free(parent);
    free(sz);
    return total - subtract;
}
```

## Csharp

```csharp
public class Solution {
    public long CountPairs(int n, int[][] edges) {
        var uf = new UnionFind(n);
        foreach (var e in edges) {
            uf.Union(e[0], e[1]);
        }
        long totalPairs = (long)n * (n - 1) / 2;
        for (int i = 0; i < n; i++) {
            if (uf.Find(i) == i) { // root
                long sz = uf.Size[i];
                totalPairs -= sz * (sz - 1) / 2;
            }
        }
        return totalPairs;
    }

    private class UnionFind {
        public int[] Parent;
        public int[] Size;

        public UnionFind(int n) {
            Parent = new int[n];
            Size = new int[n];
            for (int i = 0; i < n; i++) {
                Parent[i] = i;
                Size[i] = 1;
            }
        }

        public int Find(int x) {
            if (Parent[x] != x) {
                Parent[x] = Find(Parent[x]);
            }
            return Parent[x];
        }

        public void Union(int a, int b) {
            int rootA = Find(a);
            int rootB = Find(b);
            if (rootA == rootB) return;
            // union by size
            if (Size[rootA] < Size[rootB]) {
                Parent[rootA] = rootB;
                Size[rootB] += Size[rootA];
            } else {
                Parent[rootB] = rootA;
                Size[rootA] += Size[rootB];
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countPairs = function(n, edges) {
    class DSU {
        constructor(n) {
            this.parent = new Array(n);
            this.size = new Array(n);
            for (let i = 0; i < n; i++) {
                this.parent[i] = i;
                this.size[i] = 1;
            }
        }
        find(x) {
            while (this.parent[x] !== x) {
                this.parent[x] = this.parent[this.parent[x]];
                x = this.parent[x];
            }
            return x;
        }
        union(a, b) {
            let ra = this.find(a);
            let rb = this.find(b);
            if (ra === rb) return;
            if (this.size[ra] < this.size[rb]) {
                [ra, rb] = [rb, ra];
            }
            this.parent[rb] = ra;
            this.size[ra] += this.size[rb];
        }
    }

    const dsu = new DSU(n);
    for (const [u, v] of edges) {
        dsu.union(u, v);
    }

    let totalPairs = n * (n - 1) / 2;
    let intraPairs = 0;
    for (let i = 0; i < n; i++) {
        if (dsu.parent[i] === i) { // root
            const s = dsu.size[i];
            intraPairs += s * (s - 1) / 2;
        }
    }

    return totalPairs - intraPairs;
};
```

## Typescript

```typescript
function countPairs(n: number, edges: number[][]): number {
    const parent = new Int32Array(n);
    const size = new Int32Array(n);
    for (let i = 0; i < n; i++) {
        parent[i] = i;
        size[i] = 1;
    }
    function find(x: number): number {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }
    function union(a: number, b: number): void {
        let ra = find(a);
        let rb = find(b);
        if (ra === rb) return;
        if (size[ra] < size[rb]) {
            const tmp = ra;
            ra = rb;
            rb = tmp;
        }
        parent[rb] = ra;
        size[ra] += size[rb];
    }
    for (const [u, v] of edges) {
        union(u, v);
    }
    const compCount = new Map<number, number>();
    for (let i = 0; i < n; i++) {
        const r = find(i);
        compCount.set(r, (compCount.get(r) ?? 0) + 1);
    }
    let totalPairs = n * (n - 1) / 2;
    let intra = 0;
    for (const sz of compCount.values()) {
        intra += sz * (sz - 1) / 2;
    }
    return totalPairs - intra;
}
```

## Php

```php
class Solution {
    private array $parent = [];
    private array $size = [];

    private function find(int $x): int {
        if ($this->parent[$x] !== $x) {
            $this->parent[$x] = $this->find($this->parent[$x]);
        }
        return $this->parent[$x];
    }

    private function union(int $a, int $b): void {
        $rootA = $this->find($a);
        $rootB = $this->find($b);
        if ($rootA === $rootB) {
            return;
        }
        // Union by size
        if ($this->size[$rootA] < $this->size[$rootB]) {
            [$rootA, $rootB] = [$rootB, $rootA];
        }
        $this->parent[$rootB] = $rootA;
        $this->size[$rootA] += $this->size[$rootB];
    }

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer
     */
    function countPairs($n, $edges) {
        $this->parent = range(0, $n - 1);
        $this->size   = array_fill(0, $n, 1);

        foreach ($edges as $edge) {
            $this->union($edge[0], $edge[1]);
        }

        $componentSizes = [];
        for ($i = 0; $i < $n; ++$i) {
            $root = $this->find($i);
            if (!isset($componentSizes[$root])) {
                $componentSizes[$root] = 0;
            }
            $componentSizes[$root]++;
        }

        $unreachablePairs = 0;
        $sum = 0;
        foreach ($componentSizes as $size) {
            $unreachablePairs += $size * $sum;
            $sum += $size;
        }

        return $unreachablePairs;
    }
}
```

## Swift

```swift
class Solution {
    func countPairs(_ n: Int, _ edges: [[Int]]) -> Int {
        class UnionFind {
            var parent: [Int]
            var size: [Int]
            init(_ n: Int) {
                parent = Array(0..<n)
                size = Array(repeating: 1, count: n)
            }
            func find(_ x: Int) -> Int {
                var x = x
                while parent[x] != x {
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                }
                return x
            }
            func union(_ a: Int, _ b: Int) {
                let ra = find(a)
                let rb = find(b)
                if ra == rb { return }
                if size[ra] < size[rb] {
                    parent[ra] = rb
                    size[rb] += size[ra]
                } else {
                    parent[rb] = ra
                    size[ra] += size[rb]
                }
            }
        }

        let uf = UnionFind(n)
        for e in edges {
            uf.union(e[0], e[1])
        }

        var componentSize = [Int: Int]()
        for i in 0..<n {
            let root = uf.find(i)
            componentSize[root, default: 0] += 1
        }

        let totalPairs = Int64(n) * Int64(n - 1) / 2
        var reachablePairs: Int64 = 0
        for sz in componentSize.values {
            let s = Int64(sz)
            reachablePairs += s * (s - 1) / 2
        }

        return Int(totalPairs - reachablePairs)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPairs(n: Int, edges: Array<IntArray>): Long {
        val dsu = DSU(n)
        for (edge in edges) {
            dsu.union(edge[0], edge[1])
        }
        var total = n.toLong() * (n - 1) / 2
        for (i in 0 until n) {
            if (dsu.parent[i] == i) {
                val size = dsu.sz[i].toLong()
                total -= size * (size - 1) / 2
            }
        }
        return total
    }

    private class DSU(val n: Int) {
        val parent = IntArray(n) { it }
        val sz = IntArray(n) { 1 }

        fun find(x: Int): Int {
            var v = x
            while (parent[v] != v) {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
        }

        fun union(a: Int, b: Int) {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (sz[ra] < sz[rb]) {
                val tmp = ra; ra = rb; rb = tmp
            }
            parent[rb] = ra
            sz[ra] += sz[rb]
        }
    }
}
```

## Dart

```dart
class Solution {
  int countPairs(int n, List<List<int>> edges) {
    var dsu = _DSU(n);
    for (var e in edges) {
      dsu.union(e[0], e[1]);
    }
    var seen = <int>{};
    int intra = 0;
    for (int i = 0; i < n; i++) {
      int root = dsu.find(i);
      if (!seen.contains(root)) {
        seen.add(root);
        int sz = dsu.size[root];
        intra += sz * (sz - 1) ~/ 2;
      }
    }
    int total = n * (n - 1) ~/ 2;
    return total - intra;
  }
}

class _DSU {
  late List<int> parent;
  late List<int> size;

  _DSU(int n) {
    parent = List.generate(n, (i) => i);
    size = List.filled(n, 1);
  }

  int find(int x) {
    while (parent[x] != x) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return x;
  }

  void union(int a, int b) {
    int ra = find(a);
    int rb = find(b);
    if (ra == rb) return;
    if (size[ra] < size[rb]) {
      int tmp = ra;
      ra = rb;
      rb = tmp;
    }
    parent[rb] = ra;
    size[ra] += size[rb];
  }
}
```

## Golang

```go
func countPairs(n int, edges [][]int) int64 {
    parent := make([]int, n)
    sz := make([]int, n)
    for i := 0; i < n; i++ {
        parent[i] = i
        sz[i] = 1
    }

    var find func(int) int
    find = func(x int) int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    union := func(a, b int) {
        ra, rb := find(a), find(b)
        if ra == rb {
            return
        }
        if sz[ra] < sz[rb] {
            ra, rb = rb, ra
        }
        parent[rb] = ra
        sz[ra] += sz[rb]
    }

    for _, e := range edges {
        union(e[0], e[1])
    }

    totalPairs := int64(n) * (int64(n) - 1) / 2
    var intra int64
    for i := 0; i < n; i++ {
        if parent[i] == i {
            s := int64(sz[i])
            intra += s * (s - 1) / 2
        }
    }

    return totalPairs - intra
}
```

## Ruby

```ruby
class UnionFind
  def initialize(n)
    @parent = Array.new(n) { |i| i }
    @rank = Array.new(n, 0)
  end

  def find(x)
    while @parent[x] != x
      @parent[x] = @parent[@parent[x]]
      x = @parent[x]
    end
    x
  end

  def union(a, b)
    ra = find(a)
    rb = find(b)
    return if ra == rb
    if @rank[ra] < @rank[rb]
      @parent[ra] = rb
    elsif @rank[ra] > @rank[rb]
      @parent[rb] = ra
    else
      @parent[rb] = ra
      @rank[ra] += 1
    end
  end
end

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_pairs(n, edges)
  uf = UnionFind.new(n)
  edges.each { |a, b| uf.union(a, b) }

  component_sizes = Hash.new(0)
  (0...n).each do |i|
    root = uf.find(i)
    component_sizes[root] += 1
  end

  total_pairs = n * (n - 1) / 2
  reachable_pairs = 0
  component_sizes.each_value { |sz| reachable_pairs += sz * (sz - 1) / 2 }

  total_pairs - reachable_pairs
end
```

## Scala

```scala
object Solution {
  def countPairs(n: Int, edges: Array[Array[Int]]): Long = {
    class DSU(val n: Int) {
      val parent: Array[Int] = (0 until n).toArray
      val size: Array[Int] = Array.fill(n)(1)

      def find(x: Int): Int = {
        var v = x
        while (parent(v) != v) {
          parent(v) = parent(parent(v))
          v = parent(v)
        }
        v
      }

      def union(a: Int, b: Int): Unit = {
        var ra = find(a)
        var rb = find(b)
        if (ra != rb) {
          if (size(ra) < size(rb)) {
            val tmp = ra
            ra = rb
            rb = tmp
          }
          parent(rb) = ra
          size(ra) += size(rb)
        }
      }
    }

    val dsu = new DSU(n)
    var i = 0
    while (i < edges.length) {
      val e = edges(i)
      dsu.union(e(0), e(1))
      i += 1
    }

    var total: Long = n.toLong * (n - 1) / 2
    var idx = 0
    while (idx < n) {
      if (dsu.parent(idx) == idx) {
        val s = dsu.size(idx).toLong
        total -= s * (s - 1) / 2
      }
      idx += 1
    }
    total
  }
}
```

## Rust

```rust
use std::collections::HashMap;

struct DSU {
    parent: Vec<usize>,
    size: Vec<usize>,
}

impl DSU {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(i);
        }
        DSU { parent, size: vec![1; n] }
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
        // Union by size
        if self.size[ra] < self.size[rb] {
            std::mem::swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        self.size[ra] += self.size[rb];
    }

    fn component_sizes(&mut self) -> Vec<usize> {
        let n = self.parent.len();
        let mut map: HashMap<usize, usize> = HashMap::new();
        for i in 0..n {
            let root = self.find(i);
            *map.entry(root).or_insert(0) += 1;
        }
        map.values().cloned().collect()
    }
}

impl Solution {
    pub fn count_pairs(n: i32, edges: Vec<Vec<i32>>) -> i64 {
        let n_usize = n as usize;
        let mut dsu = DSU::new(n_usize);
        for e in edges.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            dsu.union(a, b);
        }
        let sizes = dsu.component_sizes();
        let total_pairs: i64 = (n as i64) * ((n - 1) as i64) / 2;
        let mut intra: i64 = 0;
        for sz in sizes {
            intra += (sz as i64) * ((sz as i64) - 1) / 2;
        }
        total_pairs - intra
    }
}
```

## Racket

```racket
(define/contract (count-pairs n edges)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ([parent (make-vector n)]
         [sz     (make-vector n 1)])
    ;; initialize parent pointers
    (for ([i (in-range n)]) (vector-set! parent i i))
    (define (find x)
      (let loop ((x x))
        (let ((p (vector-ref parent x)))
          (if (= p x)
              x
              (let ((root (loop p)))
                (vector-set! parent x root)
                root)))))
    (define (union a b)
      (let* ((ra (find a))
             (rb (find b)))
        (when (not (= ra rb))
          (let ((sa (vector-ref sz ra))
                (sb (vector-ref sz rb)))
            (if (> sa sb)
                (begin
                  (vector-set! parent rb ra)
                  (vector-set! sz ra (+ sa sb)))
                (begin
                  (vector-set! parent ra rb)
                  (vector-set! sz rb (+ sa sb))))))))
    ;; process all edges
    (for ([e edges])
      (let ((a (first e))
            (b (second e)))
        (union a b)))
    ;; count sizes of each component
    (define comp (make-hash))
    (for ([i (in-range n)])
      (let* ((root (find i))
             (cnt  (hash-ref comp root 0)))
        (hash-set! comp root (+ cnt 1))))
    ;; compute number of unreachable pairs
    (let loop ((sizes (hash-values comp))
               (remaining n)
               (ans 0))
      (if (null? sizes)
          ans
          (let* ((s (car sizes))
                 (new-ans (+ ans (* s (- remaining s)))))
            (loop (cdr sizes) (- remaining s) new-ans))))))
```

## Erlang

```erlang
-export([count_pairs/2]).

-spec count_pairs(N :: integer(), Edges :: [[integer()]]) -> integer().
count_pairs(N, Edges) ->
    Parent0 = maps:from_list([{I, I} || I <- lists:seq(0, N - 1)]),
    Size0   = maps:from_list([{I, 1} || I <- lists:seq(0, N - 1)]),
    {Parent, _Size} =
        lists:foldl(fun([U, V], {Par, Siz}) ->
            union(U, V, Par, Siz)
        end, {Parent0, Size0}, Edges),

    CompMap = component_counts(N, Parent),
    Reachable = maps:fold(
        fun(_Root, Sz, Acc) -> Acc + Sz * (Sz - 1) div 2 end,
        0,
        CompMap
    ),
    Total = N * (N - 1) div 2,
    Total - Reachable.

%% Union-Find helpers

find(Node, Parent) ->
    case maps:get(Node, Parent) of
        Node -> {Node, Parent};
        P ->
            {Root, NewParent} = find(P, Parent),
            UpdatedParent = maps:put(Node, Root, NewParent),
            {Root, UpdatedParent}
    end.

union(A, B, Parent, Size) ->
    {RootA, PA} = find(A, Parent),
    {RootB, PB} = find(B, PA),  % use updated parent after first find
    if
        RootA == RootB ->
            {PB, Size};
        true ->
            SizeA = maps:get(RootA, Size),
            SizeB = maps:get(RootB, Size),
            if
                SizeA < SizeB ->
                    NewParent = maps:put(RootA, RootB, PB),
                    NewSize   = maps:put(RootB, SizeA + SizeB, Size);
                true ->
                    NewParent = maps:put(RootB, RootA, PB),
                    NewSize   = maps:put(RootA, SizeA + SizeB, Size)
            end,
            {NewParent, NewSize}
    end.

%% Component size collection

component_counts(N, Parent) ->
    lists:foldl(
        fun(I, Acc) ->
            Root = get_root(I, Parent),
            maps:update_with(Root,
                fun(Cnt) -> Cnt + 1 end,
                1,
                Acc)
        end,
        #{},
        lists:seq(0, N - 1)
    ).

get_root(Node, Parent) ->
    case maps:get(Node, Parent) of
        Node -> Node;
        P -> get_root(P, Parent)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_pairs(n :: integer, edges :: [[integer]]) :: integer
  def count_pairs(n, edges) do
    adj = build_adj(edges, %{})

    {sizes, _visited} =
      Enum.reduce(0..(n - 1), {[], MapSet.new()}, fn node, {szs, visited} ->
        if MapSet.member?(visited, node) do
          {szs, visited}
        else
          {comp_size, new_visited} = explore(node, adj, visited)
          {[comp_size | szs], new_visited}
        end
      end)

    total_pairs = div(n * (n - 1), 2)

    internal_pairs =
      Enum.reduce(sizes, 0, fn sz, acc ->
        acc + div(sz * (sz - 1), 2)
      end)

    total_pairs - internal_pairs
  end

  defp build_adj([], adj), do: adj

  defp build_adj([[a, b] | rest], adj) do
    adj = Map.update(adj, a, [b], fn list -> [b | list] end)
    adj = Map.update(adj, b, [a], fn list -> [a | list] end)
    build_adj(rest, adj)
  end

  defp explore(start, adj, visited) do
    stack = [start]
    visited = MapSet.put(visited, start)
    explore_loop(stack, adj, visited, 0)
  end

  defp explore_loop([], _adj, visited, size), do: {size, visited}

  defp explore_loop([node | rest], adj, visited, size) do
    neighbors = Map.get(adj, node, [])

    {new_stack, new_visited} =
      Enum.reduce(neighbors, {rest, visited}, fn nb, {stk, vis} ->
        if MapSet.member?(vis, nb) do
          {stk, vis}
        else
          {[nb | stk], MapSet.put(vis, nb)}
        end
      end)

    explore_loop(new_stack, adj, new_visited, size + 1)
  end
end
```

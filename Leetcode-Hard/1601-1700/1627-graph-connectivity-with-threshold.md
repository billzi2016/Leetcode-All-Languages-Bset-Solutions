# 1627. Graph Connectivity With Threshold

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> parent, rank;
        DSU(int n): parent(n+1), rank(n+1,0) {
            iota(parent.begin(), parent.end(), 0);
        }
        int find(int x){
            if(parent[x]==x) return x;
            return parent[x]=find(parent[x]);
        }
        void unite(int a,int b){
            a=find(a); b=find(b);
            if(a==b) return;
            if(rank[a]<rank[b]) swap(a,b);
            parent[b]=a;
            if(rank[a]==rank[b]) rank[a]++;
        }
    };
    
    vector<bool> areConnected(int n, int threshold, vector<vector<int>>& queries) {
        DSU dsu(n);
        for (int d = threshold + 1; d <= n; ++d) {
            for (int multiple = d * 2; multiple <= n; multiple += d) {
                dsu.unite(d, multiple);
            }
        }
        vector<bool> ans;
        ans.reserve(queries.size());
        for (auto &q : queries) {
            ans.push_back(dsu.find(q[0]) == dsu.find(q[1]));
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public List<Boolean> areConnected(int n, int threshold, int[][] queries) {
        DSU dsu = new DSU(n);
        for (int d = threshold + 1; d <= n; d++) {
            for (int multiple = d * 2; multiple <= n; multiple += d) {
                dsu.union(d, multiple);
            }
        }
        List<Boolean> ans = new ArrayList<>(queries.length);
        for (int[] q : queries) {
            ans.add(dsu.find(q[0]) == dsu.find(q[1]));
        }
        return ans;
    }

    private static class DSU {
        int[] parent;
        int[] size;

        DSU(int n) {
            parent = new int[n + 1];
            size = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        void union(int a, int b) {
            int ra = find(a);
            int rb = find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb]) {
                parent[ra] = rb;
                size[rb] += size[ra];
            } else {
                parent[rb] = ra;
                size[ra] += size[rb];
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def areConnected(self, n, threshold, queries):
        """
        :type n: int
        :type threshold: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        if threshold >= n:
            return [False] * len(queries)

        parent = list(range(n + 1))
        size = [1] * (n + 1)

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

        # Union numbers that share a divisor > threshold
        for d in range(threshold + 1, n + 1):
            first = d
            for multiple in range(2 * d, n + 1, d):
                union(first, multiple)

        return [find(a) == find(b) for a, b in queries]
```

## Python3

```python
class Solution:
    def areConnected(self, n: int, threshold: int, queries):
        if threshold >= n:
            return [False] * len(queries)

        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
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

        for d in range(threshold + 1, n + 1):
            start = d * 2
            if start > n:
                continue
            for m in range(start, n + 1, d):
                union(d, m)

        return [find(a) == find(b) for a, b in queries]
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static int find_root(int *parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void union_sets(int *parent, int *rank, int a, int b) {
    int ra = find_root(parent, a);
    int rb = find_root(parent, b);
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

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* areConnected(int n, int threshold, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int *parent = (int *)malloc((n + 1) * sizeof(int));
    int *rank   = (int *)calloc(n + 1, sizeof(int));
    for (int i = 1; i <= n; ++i) parent[i] = i;

    for (int d = threshold + 1; d <= n; ++d) {
        for (int m = d * 2; m <= n; m += d) {
            union_sets(parent, rank, d, m);
        }
    }

    bool *ans = (bool *)malloc(queriesSize * sizeof(bool));
    for (int i = 0; i < queriesSize; ++i) {
        int a = queries[i][0];
        int b = queries[i][1];
        ans[i] = (find_root(parent, a) == find_root(parent, b));
    }

    *returnSize = queriesSize;
    free(rank);
    free(parent);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<bool> AreConnected(int n, int threshold, int[][] queries) {
        DSU dsu = new DSU(n);
        for (int d = threshold + 1; d <= n; d++) {
            for (int multiple = d * 2; multiple <= n; multiple += d) {
                dsu.Union(d, multiple);
            }
        }

        List<bool> result = new List<bool>(queries.Length);
        foreach (var q in queries) {
            result.Add(dsu.Find(q[0]) == dsu.Find(q[1]));
        }
        return result;
    }

    private class DSU {
        private int[] parent;
        private int[] rank;

        public DSU(int size) {
            parent = new int[size + 1];
            rank = new int[size + 1];
            for (int i = 0; i <= size; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
        }

        public int Find(int x) {
            if (parent[x] != x) {
                parent[x] = Find(parent[x]);
            }
            return parent[x];
        }

        public void Union(int x, int y) {
            int rootX = Find(x);
            int rootY = Find(y);
            if (rootX == rootY) return;

            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
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
 * @param {number} threshold
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var areConnected = function(n, threshold, queries) {
    // If threshold >= n, no divisor > threshold exists, all nodes isolated.
    if (threshold >= n) {
        return queries.map(() => false);
    }
    
    const parent = new Int32Array(n + 1);
    for (let i = 0; i <= n; ++i) parent[i] = i;
    
    const find = (x) => {
        let root = x;
        while (parent[root] !== root) {
            root = parent[root];
        }
        // Path compression
        while (parent[x] !== x) {
            const nxt = parent[x];
            parent[x] = root;
            x = nxt;
        }
        return root;
    };
    
    const union = (a, b) => {
        let ra = find(a);
        let rb = find(b);
        if (ra !== rb) {
            parent[ra] = rb;
        }
    };
    
    // Union numbers that share a divisor greater than threshold
    for (let d = threshold + 1; d <= n; ++d) {
        for (let multiple = d * 2; multiple <= n; multiple += d) {
            union(d, multiple);
        }
    }
    
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        const [a, b] = queries[i];
        ans[i] = find(a) === find(b);
    }
    return ans;
};
```

## Typescript

```typescript
function areConnected(n: number, threshold: number, queries: number[][]): boolean[] {
    const parent = new Int32Array(n + 1);
    const size = new Int32Array(n + 1);
    for (let i = 1; i <= n; i++) {
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

    for (let d = threshold + 1; d <= n; d++) {
        for (let m = d * 2; m <= n; m += d) {
            union(d, m);
        }
    }

    const result: boolean[] = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const [a, b] = queries[i];
        result[i] = find(a) === find(b);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $threshold
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function areConnected($n, $threshold, $queries) {
        // Disjoint Set Union (Union-Find)
        $parent = [];
        $rank   = [];
        for ($i = 0; $i <= $n; $i++) {
            $parent[$i] = $i;
            $rank[$i]   = 0;
        }

        $find = function($x) use (&$parent, &$find) {
            while ($parent[$x] != $x) {
                // Path compression
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };

        $union = function($x, $y) use (&$parent, &$rank, $find) {
            $rx = $find($x);
            $ry = $find($y);
            if ($rx == $ry) return;
            if ($rank[$rx] < $rank[$ry]) {
                $parent[$rx] = $ry;
            } elseif ($rank[$rx] > $rank[$ry]) {
                $parent[$ry] = $rx;
            } else {
                $parent[$ry] = $rx;
                $rank[$rx]++;
            }
        };

        // Connect numbers that share a divisor greater than threshold
        for ($d = $threshold + 1; $d <= $n; $d++) {
            for ($multiple = $d * 2; $multiple <= $n; $multiple += $d) {
                $union($d, $multiple);
            }
        }

        // Answer queries
        $ans = [];
        foreach ($queries as $q) {
            [$a, $b] = $q;
            $ans[] = $find($a) == $find($b);
        }
        return $ans;
    }
}
```

## Swift

```swift
class DSU {
    private var parent: [Int]
    
    init(_ size: Int) {
        // indices from 0 to size, we will use 1...size
        self.parent = Array(0...size)
    }
    
    func find(_ x: Int) -> Int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }
    
    func union(_ a: Int, _ b: Int) {
        let pa = find(a)
        let pb = find(b)
        if pa != pb {
            parent[pa] = pb
        }
    }
}

class Solution {
    func areConnected(_ n: Int, _ threshold: Int, _ queries: [[Int]]) -> [Bool] {
        let dsu = DSU(n)
        
        if threshold < n {
            var d = threshold + 1
            while d <= n {
                var multiple = d * 2
                while multiple <= n {
                    dsu.union(d, multiple)
                    multiple += d
                }
                d += 1
            }
        }
        
        var result = [Bool]()
        result.reserveCapacity(queries.count)
        for q in queries {
            let a = q[0]
            let b = q[1]
            result.append(dsu.find(a) == dsu.find(b))
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun areConnected(n: Int, threshold: Int, queries: Array<IntArray>): List<Boolean> {
        val parent = IntArray(n + 1) { it }
        val rank = IntArray(n + 1)

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
            if (rank[ra] < rank[rb]) {
                parent[ra] = rb
            } else if (rank[ra] > rank[rb]) {
                parent[rb] = ra
            } else {
                parent[rb] = ra
                rank[ra]++
            }
        }

        for (d in (threshold + 1)..n) {
            var multiple = d * 2
            while (multiple <= n) {
                union(d, multiple)
                multiple += d
            }
        }

        val result = ArrayList<Boolean>(queries.size)
        for (q in queries) {
            val a = q[0]
            val b = q[1]
            result.add(find(a) == find(b))
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<bool> areConnected(int n, int threshold, List<List<int>> queries) {
    var dsu = _DSU(n + 1);
    for (int d = threshold + 1; d <= n; ++d) {
      for (int multiple = d * 2; multiple <= n; multiple += d) {
        dsu.union(d, multiple);
      }
    }
    List<bool> ans = List.filled(queries.length, false);
    for (int i = 0; i < queries.length; ++i) {
      int a = queries[i][0];
      int b = queries[i][1];
      ans[i] = dsu.find(a) == dsu.find(b);
    }
    return ans;
  }
}

class _DSU {
  late List<int> parent;
  late List<int> size;

  _DSU(int n) {
    parent = List<int>.generate(n, (i) => i);
    size = List<int>.filled(n, 1);
  }

  int find(int x) {
    if (parent[x] != x) {
      parent[x] = find(parent[x]);
    }
    return parent[x];
  }

  void union(int a, int b) {
    int rootA = find(a);
    int rootB = find(b);
    if (rootA == rootB) return;
    if (size[rootA] < size[rootB]) {
      parent[rootA] = rootB;
      size[rootB] += size[rootA];
    } else {
      parent[rootB] = rootA;
      size[rootA] += size[rootB];
    }
  }
}
```

## Golang

```go
func areConnected(n int, threshold int, queries [][]int) []bool {
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

    union := func(a, b int) {
        ra := find(a)
        rb := find(b)
        if ra == rb {
            return
        }
        if size[ra] < size[rb] {
            ra, rb = rb, ra
        }
        parent[rb] = ra
        size[ra] += size[rb]
    }

    for d := threshold + 1; d <= n; d++ {
        for m := d * 2; m <= n; m += d {
            union(d, m)
        }
    }

    ans := make([]bool, len(queries))
    for i, q := range queries {
        a, b := q[0], q[1]
        ans[i] = find(a) == find(b)
    }
    return ans
}
```

## Ruby

```ruby
class UnionFind
  def initialize(size)
    @parent = Array.new(size + 1) { |i| i }
    @rank = Array.new(size + 1, 0)
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
# @param {Integer} threshold
# @param {Integer[][]} queries
# @return {Boolean[]}
def are_connected(n, threshold, queries)
  uf = UnionFind.new(n)

  (threshold + 1).upto(n) do |d|
    multiple = d * 2
    while multiple <= n
      uf.union(d, multiple)
      multiple += d
    end
  end

  result = []
  queries.each do |a, b|
    result << (uf.find(a) == uf.find(b))
  end
  result
end
```

## Scala

```scala
object Solution {
  class UnionFind(size: Int) {
    private val parent = (0 until size).toArray
    private val rank = Array.fill(size)(0)

    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }

    def union(x: Int, y: Int): Unit = {
      var xr = find(x)
      var yr = find(y)
      if (xr == yr) return
      if (rank(xr) < rank(yr)) {
        val tmp = xr
        xr = yr
        yr = tmp
      }
      parent(yr) = xr
      if (rank(xr) == rank(yr)) rank(xr) += 1
    }
  }

  def areConnected(n: Int, threshold: Int, queries: Array[Array[Int]]): List[Boolean] = {
    val uf = new UnionFind(n + 1)
    var d = threshold + 1
    while (d <= n) {
      var multiple = d * 2
      while (multiple <= n) {
        uf.union(d, multiple)
        multiple += d
      }
      d += 1
    }

    queries.map { q =>
      val a = q(0)
      val b = q(1)
      uf.find(a) == uf.find(b)
    }.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn are_connected(n: i32, threshold: i32, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let n_usize = n as usize;
        let thresh = threshold as usize;

        // Disjoint Set Union structure
        struct DSU {
            parent: Vec<usize>,
            size: Vec<usize>,
        }

        impl DSU {
            fn new(n: usize) -> Self {
                let mut parent = Vec::with_capacity(n + 1);
                let mut size = Vec::with_capacity(n + 1);
                for i in 0..=n {
                    parent.push(i);
                    size.push(1);
                }
                DSU { parent, size }
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
        }

        let mut dsu = DSU::new(n_usize);

        // Connect numbers that share a divisor greater than threshold
        for d in (thresh + 1)..=n_usize {
            let mut multiple = d * 2;
            while multiple <= n_usize {
                dsu.union(d, multiple);
                multiple += d;
            }
        }

        // Answer queries
        let mut ans = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let a = q[0] as usize;
            let b = q[1] as usize;
            if dsu.find(a) == dsu.find(b) {
                ans.push(true);
            } else {
                ans.push(false);
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (are-connected n threshold queries)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) (listof boolean?))
  (letrec
      ;; Union-Find structure using vectors indexed by city label.
      ((make-uf
        (lambda (size)
          (vector size
                  (let ([p (make-vector size)])
                    (for ([i (in-range size)]) (vector-set! p i i))
                    p)
                  (make-vector size 0))))
       
       (uf-find
        (lambda (uf x)
          (let* ((parent (vector-ref uf 1)))
            (let loop ((v x))
              (let ((root (vector-ref parent v)))
                (if (= root v)
                    v
                    (let ((r (loop root)))
                      (vector-set! parent v r)
                      r))))))

       (uf-union
        (lambda (uf a b)
          (let* ((parent (vector-ref uf 1))
                 (rank   (vector-ref uf 2))
                 (ra (uf-find uf a))
                 (rb (uf-find uf b)))
            (unless (= ra rb)
              (let ((rank-a (vector-ref rank ra))
                    (rank-b (vector-ref rank rb)))
                (cond
                  [(< rank-a rank-b)
                   (vector-set! parent ra rb)]
                  [(> rank-a rank-b)
                   (vector-set! parent rb ra)]
                  [else
                   (vector-set! parent rb ra)
                   (vector-set! rank ra (+ rank-a 1))]))))))

       ;; Main processing: union multiples of each divisor > threshold.
       (process-unions
        (lambda ()
          (for ([d (in-range (add1 threshold) (add1 n))])
            (let ((first (* 2 d)))
              (when (<= first n)
                (for ([m (in-range first (add1 n) d)])
                  (uf-union uf d m))))))))
    (let* ((uf (make-uf (+ n 1)))) ; indices 0..n, we ignore 0
      (process-unions)
      (map (lambda (pair)
             (= (uf-find uf (first pair))
                (uf-find uf (second pair))))
           queries))))
```

## Erlang

```erlang
-module(solution).
-export([are_connected/3]).

-include_lib("kernel/include/logger.hrl").

-spec are_connected(N :: integer(), Threshold :: integer(), Queries :: [[integer()]]) -> [boolean()].
are_connected(N, Threshold, Queries) ->
    {Parent0, Rank0} = init_sets(N),
    {ParentFinal, _RankFinal} = process_divisors(Threshold + 1, N, Parent0, Rank0),
    answer_queries(Queries, ParentFinal).

%% Initialize parent array where each node is its own parent
init_parent(N) ->
    Init = array:new(N + 1),
    init_parent_loop(0, N, Init).

init_parent_loop(I, N, Acc) when I > N -> Acc;
init_parent_loop(I, N, Acc) ->
    NewAcc = array:set(I, I, Acc),
    init_parent_loop(I + 1, N, NewAcc).

%% Initialize both parent and rank structures
init_sets(N) ->
    Parent = init_parent(N),
    Rank = array:new(N + 1, {default, 0}),
    {Parent, Rank}.

%% Process all divisors greater than Threshold
process_divisors(D, N, Parent, Rank) when D > N -> {Parent, Rank};
process_divisors(D, N, Parent, Rank) ->
    {P1, R1} = process_multiples(D, 2 * D, N, Parent, Rank),
    process_divisors(D + 1, N, P1, R1).

%% Union each divisor with its multiples
process_multiples(_D, M, N, Parent, Rank) when M > N -> {Parent, Rank};
process_multiples(D, M, N, Parent, Rank) ->
    {P1, R1} = union(D, M, Parent, Rank),
    process_multiples(D, M + D, N, P1, R1).

%% Find with path compression (returns root and possibly updated parent array)
find(I, Parent) ->
    case array:get(I, Parent) of
        I -> {I, Parent};
        P ->
            {Root, NewParent} = find(P, Parent),
            UpdatedParent = array:set(I, Root, NewParent),
            {Root, UpdatedParent}
    end.

%% Union by rank
union(A, B, Parent, Rank) ->
    {RootA, P1} = find(A, Parent),
    {RootB, P2} = find(B, P1),
    if RootA == RootB ->
            {P2, Rank};
       true ->
            RankA = array:get(RootA, Rank),
            RankB = array:get(RootB, Rank),
            case RankA < RankB of
                true ->
                    NewParent = array:set(RootA, RootB, P2),
                    {NewParent, Rank};
                false ->
                    case RankA > RankB of
                        true ->
                            NewParent = array:set(RootB, RootA, P2),
                            {NewParent, Rank};
                        false -> % equal ranks
                            TempParent = array:set(RootB, RootA, P2),
                            NewRank = array:set(RootA, RankA + 1, Rank),
                            {TempParent, NewRank}
                    end
            end
    end.

%% Answer each query using the final parent structure
answer_queries(Queries, Parent) ->
    lists:map(fun([A, B]) ->
        {RootA, _} = find(A, Parent),
        {RootB, _} = find(B, Parent),
        RootA == RootB
    end, Queries).
```

## Elixir

```elixir
defmodule DSU do
  defstruct parent: nil, size: nil

  @spec new(integer) :: %DSU{}
  def new(n) do
    parent = :array.new(n + 1, default: 0)
    size = :array.new(n + 1, default: 1)

    parent =
      Enum.reduce(0..n, parent, fn i, acc ->
        :array.set(i, i, acc)
      end)

    %DSU{parent: parent, size: size}
  end

  @spec find_root(:array.array(integer), integer) :: integer
  defp find_root(parent, x) do
    p = :array.get(x, parent)

    if p == x do
      x
    else
      find_root(parent, p)
    end
  end

  @spec find_root(%DSU{}, integer) :: integer
  def find_root(%DSU{parent: parent}, x), do: find_root(parent, x)

  @spec union(%DSU{}, integer, integer) :: %DSU{}
  def union(%DSU{parent: parent, size: size} = ds, a, b) do
    ra = find_root(parent, a)
    rb = find_root(parent, b)

    if ra == rb do
      ds
    else
      size_a = :array.get(ra, size)
      size_b = :array.get(rb, size)

      cond do
        size_a < size_b ->
          parent2 = :array.set(ra, rb, parent)
          size2 = :array.set(rb, size_a + size_b, size)
          %DSU{parent: parent2, size: size2}

        true ->
          parent2 = :array.set(rb, ra, parent)
          size2 = :array.set(ra, size_a + size_b, size)
          %DSU{parent: parent2, size: size2}
      end
    end
  end
end

defmodule Solution do
  @spec are_connected(n :: integer, threshold :: integer, queries :: [[integer]]) :: [boolean]
  def are_connected(n, threshold, queries) do
    dsu = DSU.new(n)

    dsu =
      if threshold >= n do
        dsu
      else
        Enum.reduce((threshold + 1)..n, dsu, fn d, acc ->
          union_multiples(d, n, acc)
        end)
      end

    Enum.map(queries, fn [a, b] ->
      ra = DSU.find_root(dsu, a)
      rb = DSU.find_root(dsu, b)
      ra == rb
    end)
  end

  defp union_multiples(d, n, ds) do
    union_loop(2 * d, d, n, ds)
  end

  defp union_loop(m, _d, n, ds) when m > n, do: ds

  defp union_loop(m, d, n, ds) do
    ds = DSU.union(ds, d, m)
    union_loop(m + d, d, n, ds)
  end
end
```

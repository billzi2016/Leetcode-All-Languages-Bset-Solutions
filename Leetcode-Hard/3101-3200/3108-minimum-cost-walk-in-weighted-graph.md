# 3108. Minimum Cost Walk in Weighted Graph

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> parent, rank;
        DSU(int n): parent(n), rank(n,0) { iota(parent.begin(), parent.end(), 0); }
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
    
    vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
        DSU dsu(n);
        for (auto &e: edges) {
            dsu.unite(e[0], e[1]);
        }
        const int ALL_ONES = (1<<30)-1; // enough bits for given constraints
        vector<int> compCost(n, ALL_ONES);
        for (auto &e: edges) {
            int u=e[0], w=e[2];
            int root=dsu.find(u);
            compCost[root] &= w;
        }
        vector<int> ans;
        ans.reserve(query.size());
        for (auto &q: query) {
            int s=q[0], t=q[1];
            if (dsu.find(s)!=dsu.find(t)) ans.push_back(-1);
            else ans.push_back(compCost[dsu.find(s)]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class DSU {
        int[] parent;
        byte[] rank;
        DSU(int n) {
            parent = new int[n];
            rank = new byte[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        void union(int a, int b) {
            int ra = find(a);
            int rb = find(b);
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
    }

    public int[] minimumCost(int n, int[][] edges, int[][] query) {
        DSU dsu = new DSU(n);
        for (int[] e : edges) {
            dsu.union(e[0], e[1]);
        }

        int[] compCost = new int[n];
        // initialize with all bits set
        for (int i = 0; i < n; i++) compCost[i] = Integer.MAX_VALUE;

        for (int[] e : edges) {
            int root = dsu.find(e[0]);
            compCost[root] &= e[2];
        }

        int q = query.length;
        int[] ans = new int[q];
        for (int i = 0; i < q; i++) {
            int s = query[i][0];
            int t = query[i][1];
            if (dsu.find(s) != dsu.find(t)) {
                ans[i] = -1;
            } else {
                ans[i] = compCost[dsu.find(s)];
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minimumCost(self, n, edges, query):
        """
        :type n: int
        :type edges: List[List[int]]
        :type query: List[List[int]]
        :rtype: List[int]
        """
        parent = [-1] * n
        rank = [0] * n

        def find(x):
            while parent[x] != -1:
                if parent[parent[x]] != -1:
                    parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1

        # Build DSU based on connectivity only
        for u, v, _ in edges:
            union(u, v)

        # Compute component AND of edge weights
        MASK = (1 << 30) - 1  # enough bits for wi <= 1e5
        comp_and = [MASK] * n
        for u, v, w in edges:
            r = find(u)
            comp_and[r] &= w

        res = []
        for s, t in query:
            rs, rt = find(s), find(t)
            if rs != rt:
                res.append(-1)
            else:
                res.append(comp_and[rs])
        return res
```

## Python3

```python
class Solution:
    def minimumCost(self, n, edges, query):
        parent = list(range(n))
        rank = [0] * n

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
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1

        # Build DSU
        for u, v, _ in edges:
            union(u, v)

        comp_and = [-1] * n
        for u, v, w in edges:
            r = find(u)
            comp_and[r] &= w

        ans = []
        for s, t in query:
            rs, rt = find(s), find(t)
            if rs != rt:
                ans.append(-1)
            else:
                ans.append(comp_and[rs])
        return ans
```

## C

```c
#include <stdlib.h>

/* Disjoint Set Union (Union-Find) helpers */
static int dsu_find(int *parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void dsu_union(int *parent, int *rank, int a, int b) {
    int ra = dsu_find(parent, a);
    int rb = dsu_find(parent, b);
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
int* minimumCost(int n, int** edges, int edgesSize, int* edgesColSize,
                 int** query, int querySize, int* queryColSize, int* returnSize) {
    /* Initialize DSU */
    int *parent = (int *)malloc(n * sizeof(int));
    int *rank   = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) parent[i] = i;

    /* Union all edges */
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        dsu_union(parent, rank, u, v);
    }

    /* Compute component cost: bitwise AND of all edge weights in each component */
    int *compCost = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) compCost[i] = -1;   // all bits set

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int w = edges[i][2];
        int root = dsu_find(parent, u);
        compCost[root] &= w;
    }

    /* Answer queries */
    int *ans = (int *)malloc(querySize * sizeof(int));
    for (int i = 0; i < querySize; ++i) {
        int s = query[i][0];
        int t = query[i][1];
        if (dsu_find(parent, s) != dsu_find(parent, t)) {
            ans[i] = -1;
        } else {
            int root = dsu_find(parent, s);
            ans[i] = compCost[root];
        }
    }

    *returnSize = querySize;

    free(parent);
    free(rank);
    free(compCost);

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    private int Find(int x, int[] parent) {
        if (parent[x] != x) parent[x] = Find(parent[x], parent);
        return parent[x];
    }

    private void Union(int a, int b, int[] parent, int[] rank) {
        int ra = Find(a, parent);
        int rb = Find(b, parent);
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

    public int[] MinimumCost(int n, int[][] edges, int[][] query) {
        int[] parent = new int[n];
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }

        // Build DSU
        foreach (var e in edges) {
            Union(e[0], e[1], parent, rank);
        }

        int allOnes = ~0; // -1, all bits set
        int[] compCost = new int[n];
        for (int i = 0; i < n; i++) compCost[i] = allOnes;

        // Compute component AND cost
        foreach (var e in edges) {
            int root = Find(e[0], parent);
            compCost[root] &= e[2];
        }

        int[] ans = new int[query.Length];
        for (int i = 0; i < query.Length; i++) {
            int s = query[i][0];
            int t = query[i][1];
            int rs = Find(s, parent);
            int rt = Find(t, parent);
            if (rs != rt) ans[i] = -1;
            else ans[i] = compCost[rs];
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[][]} query
 * @return {number[]}
 */
var minimumCost = function(n, edges, query) {
    const parent = new Array(n);
    const rank = new Array(n).fill(0);
    for (let i = 0; i < n; ++i) parent[i] = i;

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

    // Build DSU
    for (const [u, v] of edges) {
        union(u, v);
    }

    // Compute component AND cost
    const compAnd = new Array(n).fill(-1); // -1 has all bits set in 32-bit
    for (const [u, v, w] of edges) {
        const r = find(u); // u and v share same root
        compAnd[r] &= w;
    }

    const ans = [];
    for (const [s, t] of query) {
        if (find(s) !== find(t)) {
            ans.push(-1);
        } else {
            ans.push(compAnd[find(s)]);
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minimumCost(n: number, edges: number[][], query: number[][]): number[] {
    const parent = new Int32Array(n);
    const rank = new Int8Array(n);
    for (let i = 0; i < n; i++) parent[i] = i;

    function find(x: number): number {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    }

    function union(a: number, b: number): void {
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
    }

    for (const [u, v] of edges) union(u, v);

    const compCost = new Int32Array(n);
    for (let i = 0; i < n; i++) compCost[i] = -1; // all bits set

    for (const [u, , w] of edges) {
        const r = find(u);
        compCost[r] &= w;
    }

    const ans: number[] = [];
    for (const [s, t] of query) {
        if (find(s) !== find(t)) ans.push(-1);
        else ans.push(compCost[find(s)]);
    }
    return ans;
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

    private function union($x, $y) {
        $rx = $this->find($x);
        $ry = $this->find($y);
        if ($rx == $ry) return;
        if ($this->rank[$rx] < $this->rank[$ry]) {
            $this->parent[$rx] = $ry;
        } elseif ($this->rank[$rx] > $this->rank[$ry]) {
            $this->parent[$ry] = $rx;
        } else {
            $this->parent[$ry] = $rx;
            $this->rank[$rx]++;
        }
    }

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer[][] $query
     * @return Integer[]
     */
    function minimumCost($n, $edges, $query) {
        // initialize DSU
        $this->parent = array_fill(0, $n, 0);
        $this->rank   = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $this->parent[$i] = $i;
        }

        // union all edges
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $this->union($u, $v);
        }

        // compute component AND cost
        $allOnes = (1 << 20) - 1; // enough bits for weight <= 10^5
        $compCost = array_fill(0, $n, $allOnes);

        foreach ($edges as $e) {
            $u = $e[0];
            $w = $e[2];
            $root = $this->find($u);
            $compCost[$root] &= $w;
        }

        // answer queries
        $ans = [];
        foreach ($query as $q) {
            $s = $q[0];
            $t = $q[1];
            if ($this->find($s) != $this->find($t)) {
                $ans[] = -1;
            } else {
                $root = $this->find($s);
                $ans[] = $compCost[$root];
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumCost(_ n: Int, _ edges: [[Int]], _ query: [[Int]]) -> [Int] {
        var parent = Array(0..<n)
        var rank = Array(repeating: 0, count: n)
        
        func find(_ x: Int) -> Int {
            if parent[x] != x {
                parent[x] = find(parent[x])
            }
            return parent[x]
        }
        
        func union(_ a: Int, _ b: Int) {
            var ra = find(a)
            var rb = find(b)
            if ra == rb { return }
            if rank[ra] < rank[rb] {
                swap(&ra, &rb)
            }
            parent[rb] = ra
            if rank[ra] == rank[rb] {
                rank[ra] += 1
            }
        }
        
        for e in edges {
            union(e[0], e[1])
        }
        
        var compCost = Array(repeating: ~0, count: n) // all bits set
        
        for e in edges {
            let root = find(e[0])
            compCost[root] &= e[2]
        }
        
        var result = [Int]()
        result.reserveCapacity(query.count)
        
        for q in query {
            let s = q[0], t = q[1]
            if find(s) != find(t) {
                result.append(-1)
            } else {
                let root = find(s)
                result.append(compCost[root])
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class DSU(n: Int) {
        private val parent = IntArray(n) { it }
        private val rank = IntArray(n)

        fun find(x: Int): Int {
            if (parent[x] != x) {
                parent[x] = find(parent[x])
            }
            return parent[x]
        }

        fun union(a: Int, b: Int) {
            var x = find(a)
            var y = find(b)
            if (x == y) return
            if (rank[x] < rank[y]) {
                val tmp = x
                x = y
                y = tmp
            }
            parent[y] = x
            if (rank[x] == rank[y]) rank[x]++
        }
    }

    fun minimumCost(n: Int, edges: Array<IntArray>, query: Array<IntArray>): IntArray {
        val dsu = DSU(n)
        for (e in edges) {
            dsu.union(e[0], e[1])
        }
        val compCost = IntArray(n) { -1 } // all bits set
        for (e in edges) {
            val root = dsu.find(e[0])
            compCost[root] = compCost[root] and e[2]
        }
        val ans = IntArray(query.size)
        for (i in query.indices) {
            val s = query[i][0]
            val t = query[i][1]
            if (dsu.find(s) != dsu.find(t)) {
                ans[i] = -1
            } else {
                val root = dsu.find(s)
                ans[i] = compCost[root]
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> minimumCost(int n, List<List<int>> edges, List<List<int>> query) {
    // Disjoint Set Union (Union-Find)
    final parent = List<int>.filled(n, -1);
    final rank = List<int>.filled(n, 0);

    int find(int x) {
      if (parent[x] == -1) return x;
      return parent[x] = find(parent[x]);
    }

    void unionSet(int a, int b) {
      int ra = find(a);
      int rb = find(b);
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

    // Build DSU
    for (var e in edges) {
      unionSet(e[0], e[1]);
    }

    // Component AND values, initialized to all bits 1 (-1 works as neutral element)
    final compAnd = List<int>.filled(n, -1);

    // Compute AND per component
    for (var e in edges) {
      int u = e[0];
      int w = e[2];
      int root = find(u);
      compAnd[root] &= w;
    }

    // Answer queries
    List<int> ans = List<int>.filled(query.length, 0);
    for (int i = 0; i < query.length; ++i) {
      int s = query[i][0];
      int t = query[i][1];
      int rs = find(s);
      int rt = find(t);
      if (rs != rt) {
        ans[i] = -1;
      } else {
        ans[i] = compAnd[rs];
      }
    }
    return ans;
  }
}
```

## Golang

```go
func minimumCost(n int, edges [][]int, query [][]int) []int {
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

    union := func(a, b int) {
        ra, rb := find(a), find(b)
        if ra == rb {
            return
        }
        if rank[ra] < rank[rb] {
            ra, rb = rb, ra
        }
        parent[rb] = ra
        if rank[ra] == rank[rb] {
            rank[ra]++
        }
    }

    // Build DSU
    for _, e := range edges {
        u, v := e[0], e[1]
        union(u, v)
    }

    const allOnes = (1 << 30) - 1 // enough bits for given constraints
    compAnd := make([]int, n)
    for i := 0; i < n; i++ {
        compAnd[i] = allOnes
    }

    // Compute AND per component
    for _, e := range edges {
        u, w := e[0], e[2]
        root := find(u)
        compAnd[root] &= w
    }

    ans := make([]int, len(query))
    for i, q := range query {
        s, t := q[0], q[1]
        rs, rt := find(s), find(t)
        if rs != rt {
            ans[i] = -1
        } else {
            ans[i] = compAnd[rs]
        }
    }
    return ans
}
```

## Ruby

```ruby
def minimum_cost(n, edges, query)
  parent = Array.new(n, -1)
  rank = Array.new(n, 0)

  find = nil
  find = ->(x) do
    if parent[x] == -1
      x
    else
      parent[x] = find.call(parent[x])
    end
  end

  union = ->(a, b) do
    ra = find.call(a)
    rb = find.call(b)
    return if ra == rb
    if rank[ra] < rank[rb]
      parent[ra] = rb
    elsif rank[ra] > rank[rb]
      parent[rb] = ra
    else
      parent[rb] = ra
      rank[ra] += 1
    end
  end

  edges.each do |u, v, w|
    union.call(u, v)
  end

  inf = (1 << 60) - 1
  comp_cost = Array.new(n, inf)

  edges.each do |u, _v, w|
    r = find.call(u)
    comp_cost[r] &= w
  end

  ans = []
  query.each do |s, t|
    if find.call(s) != find.call(t)
      ans << -1
    else
      ans << comp_cost[find.call(s)]
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def minimumCost(n: Int, edges: Array[Array[Int]], query: Array[Array[Int]]): Array[Int] = {
        val parent = Array.fill[Int](n)(-1)
        val rank = new Array[Int](n)

        def find(x: Int): Int = {
            if (parent(x) == -1) x
            else {
                val p = find(parent(x))
                parent(x) = p
                p
            }
        }

        def union(a: Int, b: Int): Unit = {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (rank(ra) < rank(rb)) {
                val tmp = ra
                ra = rb
                rb = tmp
            }
            parent(rb) = ra
            if (rank(ra) == rank(rb)) rank(ra) += 1
        }

        var i = 0
        while (i < edges.length) {
            val e = edges(i)
            union(e(0), e(1))
            i += 1
        }

        val compCost = Array.fill[Int](n)(Int.MaxValue)

        i = 0
        while (i < edges.length) {
            val e = edges(i)
            val w = e(2)
            val r = find(e(0))
            compCost(r) &= w
            i += 1
        }

        val ans = new Array[Int](query.length)
        var idx = 0
        while (idx < query.length) {
            val q = query(idx)
            val s = q(0)
            val t = q(1)
            if (find(s) != find(t)) ans(idx) = -1
            else ans(idx) = compCost(find(s))
            idx += 1
        }
        ans
    }
}
```

## Rust

```rust
use std::mem;

struct DSU {
    parent: Vec<usize>,
    rank: Vec<u8>,
}

impl DSU {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(i);
        }
        let rank = vec![0u8; n];
        DSU { parent, rank }
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
        if self.rank[ra] < self.rank[rb] {
            mem::swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        if self.rank[ra] == self.rank[rb] {
            self.rank[ra] += 1;
        }
    }
}

impl Solution {
    pub fn minimum_cost(n: i32, edges: Vec<Vec<i32>>, query: Vec<Vec<i32>>) -> Vec<i32> {
        let n_usize = n as usize;
        let mut dsu = DSU::new(n_usize);
        for e in &edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            dsu.union(u, v);
        }

        // component cost initialized to all bits 1 (-1)
        let mut comp_cost = vec![-1i32; n_usize];
        for e in &edges {
            let u = e[0] as usize;
            let w = e[2];
            let root = dsu.find(u);
            comp_cost[root] &= w;
        }

        let mut ans = Vec::with_capacity(query.len());
        for q in query {
            let s = q[0] as usize;
            let t = q[1] as usize;
            let root_s = dsu.find(s);
            let root_t = dsu.find(t);
            if root_s != root_t {
                ans.push(-1);
            } else {
                ans.push(comp_cost[root_s]);
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (minimum-cost n edges query)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof exact-integer?))
  (let* ((parent (make-vector n))
         (rank   (make-vector n 0))
         (cost   (make-vector n -1))) ; -1 has all bits set
    ;; initialize parent pointers
    (for ([i (in-range n)])
      (vector-set! parent i i))
    ;; find with path compression
    (define (find x)
      (let loop ((x x))
        (let ((p (vector-ref parent x)))
          (if (= p x)
              x
              (let ((root (loop p)))
                (vector-set! parent x root)
                root)))))
    ;; union by rank
    (define (union a b)
      (let* ((ra (find a))
             (rb (find b)))
        (when (not (= ra rb))
          (let ((rank-a (vector-ref rank ra))
                (rank-b (vector-ref rank rb)))
            (cond [(< rank-a rank-b)
                   (vector-set! parent ra rb)]
                  [(> rank-a rank-b)
                   (vector-set! parent rb ra)]
                  [else
                   (vector-set! parent rb ra)
                   (vector-set! rank ra (+ rank-a 1))])))))
    ;; union all edges
    (for ([e edges])
      (let* ((u (list-ref e 0))
             (v (list-ref e 1)))
        (union u v)))
    ;; compute component cost as AND of all edge weights in the component
    (for ([e edges])
      (let* ((u (list-ref e 0))
             (w (list-ref e 2))
             (root (find u)))
        (vector-set! cost root (bitwise-and (vector-ref cost root) w))))
    ;; answer queries
    (let ((answers '()))
      (for ([q query])
        (let* ((s (list-ref q 0))
               (t (list-ref q 1))
               (rs (find s))
               (rt (find t)))
          (if (= rs rt)
              (set! answers (cons (vector-ref cost rs) answers))
              (set! answers (cons -1 answers)))))
      (reverse answers))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_cost/3]).

-define(ALL_ONES, 16#FFFFFFFF).

-spec minimum_cost(N :: integer(), Edges :: [[integer()]], Query :: [[integer()]]) -> [integer()].
minimum_cost(N, Edges, Queries) ->
    Parent0 = array:from_list(lists:seq(0, N - 1)),
    Rank0   = array:new(N, {default, 0}),
    {Parent1, Rank1} = union_edges(Edges, Parent0, Rank0),
    Cost0 = array:new(N, {default, ?ALL_ONES}),
    {_, Cost1} = compute_component_cost(Edges, Parent1, Cost0),
    answer_queries(Queries, Parent1, Cost1).

%% Union all edges (ignoring weights)
union_edges([], Parent, Rank) ->
    {Parent, Rank};
union_edges([[U, V, _W] | Rest], Parent, Rank) ->
    {NewParent, NewRank} = union(U, V, Parent, Rank),
    union_edges(Rest, NewParent, NewRank).

%% Union two nodes
union(U, V, Parent, Rank) ->
    {RU, P1} = find(U, Parent),
    {RV, P2} = find(V, P1),
    if
        RU == RV -> {P2, Rank};
        true ->
            RankU = array:get(RU, Rank),
            RankV = array:get(RV, Rank),
            case RankU < RankV of
                true ->
                    NewParent = array:set(RU, RV, P2),
                    {NewParent, Rank};
                false ->
                    NewParent1 = array:set(RV, RU, P2),
                    NewRank = if RankU == RankV -> array:set(RU, RankU + 1, Rank);
                                 true -> Rank
                              end,
                    {NewParent1, NewRank}
            end
    end.

%% Find with path compression
find(Node, Parent) ->
    ParentNode = array:get(Node, Parent),
    if
        ParentNode == Node ->
            {Node, Parent};
        true ->
            {Root, UpdatedParent} = find(ParentNode, Parent),
            NewParent = array:set(Node, Root, UpdatedParent),
            {Root, NewParent}
    end.

%% Compute component cost (AND of all edge weights in each component)
compute_component_cost(Edges, Parent, Cost) ->
    lists:foldl(fun([U, _V, W], {PAcc, CAcc}) ->
        {RootU, PNew} = find(U, PAcc),
        CurCost = array:get(RootU, CAcc),
        NewCost = CurCost band W,
        UpdatedCost = array:set(RootU, NewCost, CAcc),
        {PNew, UpdatedCost}
    end, {Parent, Cost}, Edges).

%% Answer queries
answer_queries(Queries, Parent, Cost) ->
    lists:map(fun([S, T]) ->
        {RootS, P1} = find(S, Parent),
        {RootT, _P2} = find(T, P1),
        if RootS == RootT -> array:get(RootS, Cost);
           true          -> -1
        end
    end, Queries).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec minimum_cost(n :: integer, edges :: [[integer]], query :: [[integer]]) :: [integer]
  def minimum_cost(n, edges, query) do
    # initialize DSU structures
    parent = :array.new(n, default: -1)
    rank = :array.new(n, default: 0)

    {parent, _rank} =
      Enum.reduce(edges, {parent, rank}, fn [u, v, _w], acc ->
        union(acc, u, v)
      end)

    # full mask with all bits set (enough for given constraints)
    full_mask = (1 <<< 30) - 1
    cost = :array.new(n, default: full_mask)

    cost =
      Enum.reduce(edges, cost, fn [u, _v, w], acc_cost ->
        {root, _} = find(parent, u)
        cur = :array.get(root, acc_cost)
        newc = cur &&& w
        :array.set(root, newc, acc_cost)
      end)

    Enum.map(query, fn [s, t] ->
      {rs, _} = find(parent, s)
      {rt, _} = find(parent, t)

      if rs != rt do
        -1
      else
        :array.get(rs, cost)
      end
    end)
  end

  # Find with path compression (functional version)
  defp find(parent, x) do
    p = :array.get(x, parent)

    if p == -1 do
      {x, parent}
    else
      {root, parent2} = find(parent, p)
      parent3 = :array.set(x, root, parent2)
      {root, parent3}
    end
  end

  # Union by rank (functional version)
  defp union({parent, rank}, x, y) do
    {rx, parent1} = find(parent, x)
    {ry, parent2} = find(parent1, y)

    if rx == ry do
      {parent2, rank}
    else
      rank_rx = :array.get(rx, rank)
      rank_ry = :array.get(ry, rank)

      cond do
        rank_rx < rank_ry ->
          parent3 = :array.set(rx, ry, parent2)
          {parent3, rank}

        rank_rx > rank_ry ->
          parent3 = :array.set(ry, rx, parent2)
          {parent3, rank}

        true ->
          parent3 = :array.set(ry, rx, parent2)
          rank3 = :array.set(rx, rank_rx + 1, rank)
          {parent3, rank3}
      end
    end
  end
end
```

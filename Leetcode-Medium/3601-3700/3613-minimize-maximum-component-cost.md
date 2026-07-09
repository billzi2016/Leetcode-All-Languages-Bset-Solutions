# 3613. Minimize Maximum Component Cost

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> p, sz;
        int comps;
        DSU(int n): p(n), sz(n,1), comps(n) { iota(p.begin(), p.end(), 0); }
        int find(int x){ return p[x]==x? x : p[x]=find(p[x]); }
        void unite(int a,int b){
            a=find(a); b=find(b);
            if(a==b) return;
            if(sz[a]<sz[b]) swap(a,b);
            p[b]=a;
            sz[a]+=sz[b];
            --comps;
        }
    };
    
    bool feasible(int n, const vector<vector<int>>& edges, int k, int limit){
        DSU dsu(n);
        for(const auto& e: edges){
            if(e[2] <= limit){
                dsu.unite(e[0], e[1]);
            }
        }
        return dsu.comps <= k;
    }
    
    int minCost(int n, vector<vector<int>>& edges, int k) {
        if(k >= n) return 0;
        int maxW = 0;
        for (auto &e : edges) maxW = max(maxW, e[2]);
        int lo = 0, hi = maxW;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (feasible(n, edges, k, mid))
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }
};
```

## Java

```java
class Solution {
    public int minCost(int n, int[][] edges, int k) {
        if (k >= n) return 0;
        java.util.Arrays.sort(edges, (a, b) -> Integer.compare(a[2], b[2]));
        DSU dsu = new DSU(n);
        int components = n;
        for (int[] e : edges) {
            if (dsu.union(e[0], e[1])) {
                components--;
                if (components == k) return e[2];
            }
        }
        return 0; // should not reach here
    }

    private static class DSU {
        int[] parent;
        byte[] rank;

        DSU(int n) {
            parent = new int[n];
            rank = new byte[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }

        int find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        boolean union(int a, int b) {
            int ra = find(a);
            int rb = find(b);
            if (ra == rb) return false;
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
    }
}
```

## Python

```python
class Solution(object):
    def minCost(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        if k >= n:
            return 0

        max_w = 0
        for _, _, w in edges:
            if w > max_w:
                max_w = w

        # DSU implementation
        class DSU:
            __slots__ = ('parent', 'rank', 'count')
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [0] * size
                self.count = size  # number of components
            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x
            def union(self, a, b):
                ra = self.find(a)
                rb = self.find(b)
                if ra == rb:
                    return False
                if self.rank[ra] < self.rank[rb]:
                    ra, rb = rb, ra
                self.parent[rb] = ra
                if self.rank[ra] == self.rank[rb]:
                    self.rank[ra] += 1
                self.count -= 1
                return True

        def feasible(limit):
            dsu = DSU(n)
            for u, v, w in edges:
                if w <= limit:
                    dsu.union(u, v)
            return dsu.count <= k

        low, high = 0, max_w
        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low
```

## Python3

```python
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if k >= n:
            return 0
        edges.sort(key=lambda x: x[2])
        parent = list(range(n))
        size = [1] * n
        components = n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            nonlocal components
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
            components -= 1

        for u, v, w in edges:
            union(u, v)
            if components <= k:
                return w
        return 0
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int u, v, w;
} Edge;

static int find(int *parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void unite(int *parent, int *rank, int a, int b) {
    int pa = find(parent, a);
    int pb = find(parent, b);
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

static bool feasible(int n, Edge *earr, int m, int limit, int k) {
    int *parent = (int *)malloc(n * sizeof(int));
    int *rank   = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) parent[i] = i;

    int comps = n;
    for (int i = 0; i < m; ++i) {
        if (earr[i].w <= limit) {
            int pu = find(parent, earr[i].u);
            int pv = find(parent, earr[i].v);
            if (pu != pv) {
                unite(parent, rank, pu, pv);
                comps--;
                if (comps <= k) break; // early exit
            }
        }
    }

    free(parent);
    free(rank);
    return comps <= k;
}

int minCost(int n, int** edges, int edgesSize, int* edgesColSize, int k) {
    Edge *earr = (Edge *)malloc(edgesSize * sizeof(Edge));
    int maxW = 0;
    for (int i = 0; i < edgesSize; ++i) {
        earr[i].u = edges[i][0];
        earr[i].v = edges[i][1];
        earr[i].w = edges[i][2];
        if (earr[i].w > maxW) maxW = earr[i].w;
    }

    int lo = 0, hi = maxW;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (feasible(n, earr, edgesSize, mid, k))
            hi = mid;
        else
            lo = mid + 1;
    }

    free(earr);
    return lo;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinCost(int n, int[][] edges, int k)
    {
        if (k >= n) return 0;

        int maxWeight = 0;
        foreach (var e in edges)
            if (e[2] > maxWeight) maxWeight = e[2];

        int low = 0, high = maxWeight;
        while (low < high)
        {
            int mid = low + (high - low) / 2;
            if (Feasible(mid, n, edges, k))
                high = mid;
            else
                low = mid + 1;
        }
        return low;
    }

    private bool Feasible(int limit, int n, int[][] edges, int k)
    {
        DSU dsu = new DSU(n);
        foreach (var e in edges)
        {
            if (e[2] <= limit)
                dsu.Union(e[0], e[1]);
        }
        return dsu.Count <= k;
    }

    private class DSU
    {
        public int[] Parent;
        private byte[] Rank;
        public int Count;

        public DSU(int n)
        {
            Parent = new int[n];
            Rank = new byte[n];
            for (int i = 0; i < n; i++) Parent[i] = i;
            Count = n;
        }

        private int Find(int x)
        {
            while (Parent[x] != x)
            {
                Parent[x] = Parent[Parent[x]];
                x = Parent[x];
            }
            return x;
        }

        public void Union(int a, int b)
        {
            int pa = Find(a);
            int pb = Find(b);
            if (pa == pb) return;

            if (Rank[pa] < Rank[pb])
                Parent[pa] = pb;
            else if (Rank[pa] > Rank[pb])
                Parent[pb] = pa;
            else
            {
                Parent[pb] = pa;
                Rank[pa]++;
            }
            Count--;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} k
 * @return {number}
 */
var minCost = function(n, edges, k) {
    if (k >= n) return 0;
    edges.sort((a, b) => a[2] - b[2]);

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
    };

    let components = n;
    for (const [u, v, w] of edges) {
        if (union(u, v)) {
            components--;
            if (components <= k) return w;
        }
    }
    // Graph is connected, so this line should never be reached.
    return 0;
};
```

## Typescript

```typescript
function minCost(n: number, edges: number[][], k: number): number {
    if (k >= n) return 0;

    let maxW = 0;
    for (const e of edges) {
        if (e[2] > maxW) maxW = e[2];
    }

    class DSU {
        parent: Int32Array;
        rank: Uint8Array;
        count: number;
        constructor(size: number) {
            this.parent = new Int32Array(size);
            for (let i = 0; i < size; i++) this.parent[i] = i;
            this.rank = new Uint8Array(size);
            this.count = size;
        }
        find(x: number): number {
            const p = this.parent[x];
            if (p !== x) this.parent[x] = this.find(p);
            return this.parent[x];
        }
        union(a: number, b: number): void {
            let ra = this.find(a), rb = this.find(b);
            if (ra === rb) return;
            if (this.rank[ra] < this.rank[rb]) {
                this.parent[ra] = rb;
            } else if (this.rank[ra] > this.rank[rb]) {
                this.parent[rb] = ra;
            } else {
                this.parent[rb] = ra;
                this.rank[ra]++;
            }
            this.count--;
        }
    }

    const can = (limit: number): boolean => {
        const dsu = new DSU(n);
        for (const [u, v, w] of edges) {
            if (w <= limit) dsu.union(u, v);
        }
        return dsu.count <= k;
    };

    let low = 0, high = maxW;
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (can(mid)) high = mid;
        else low = mid + 1;
    }
    return low;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $k
     * @return Integer
     */
    function minCost($n, $edges, $k) {
        $maxW = 0;
        foreach ($edges as $e) {
            if ($e[2] > $maxW) $maxW = $e[2];
        }
        // DSU class
        class DSU {
            public $parent = [];
            public $size = [];
            public function __construct($n) {
                for ($i = 0; $i < $n; $i++) {
                    $this->parent[$i] = $i;
                    $this->size[$i] = 1;
                }
            }
            public function find($x) {
                $p = $this->parent[$x];
                if ($p != $x) {
                    $this->parent[$x] = $this->find($p);
                }
                return $this->parent[$x];
            }
            public function union($a, $b) {
                $ra = $this->find($a);
                $rb = $this->find($b);
                if ($ra == $rb) return;
                if ($this->size[$ra] < $this->size[$rb]) {
                    $tmp = $ra; $ra = $rb; $rb = $tmp;
                }
                $this->parent[$rb] = $ra;
                $this->size[$ra] += $this->size[$rb];
            }
        };
        // feasibility check
        $can = function($limit) use ($n, $edges, $k) {
            $dsu = new DSU($n);
            foreach ($edges as $e) {
                if ($e[2] <= $limit) {
                    $dsu->union($e[0], $e[1]);
                }
            }
            $components = 0;
            for ($i = 0; $i < $n; $i++) {
                if ($dsu->find($i) == $i) $components++;
            }
            return $components <= $k;
        };
        $low = 0;
        $high = $maxW;
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($can($mid)) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }
        return $low;
    }
}
```

## Swift

```swift
class Solution {
    func minCost(_ n: Int, _ edges: [[Int]], _ k: Int) -> Int {
        if k >= n { return 0 }
        var maxWeight = 0
        for e in edges {
            if e[2] > maxWeight { maxWeight = e[2] }
        }
        
        func feasible(_ limit: Int) -> Bool {
            var dsu = DSU(n)
            var components = n
            for e in edges {
                let w = e[2]
                if w <= limit {
                    if dsu.union(e[0], e[1]) {
                        components -= 1
                        if components <= k { break }
                    }
                }
            }
            return components <= k
        }
        
        var low = 0
        var high = maxWeight
        while low < high {
            let mid = (low + high) / 2
            if feasible(mid) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }
}

struct DSU {
    private var parent: [Int]
    private var size: [Int]
    
    init(_ n: Int) {
        parent = Array(0..<n)
        size = [Int](repeating: 1, count: n)
    }
    
    mutating func find(_ x: Int) -> Int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }
    
    mutating func union(_ a: Int, _ b: Int) -> Bool {
        var x = find(a)
        var y = find(b)
        if x == y { return false }
        if size[x] < size[y] {
            swap(&x, &y)
        }
        parent[y] = x
        size[x] += size[y]
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCost(n: Int, edges: Array<IntArray>, k: Int): Int {
        var maxW = 0
        for (e in edges) {
            if (e[2] > maxW) maxW = e[2]
        }
        var low = 0
        var high = maxW
        while (low < high) {
            val mid = (low + high) ushr 1
            val dsu = DSU(n)
            for (e in edges) {
                if (e[2] <= mid) {
                    dsu.union(e[0], e[1])
                }
            }
            var comps = 0
            for (i in 0 until n) {
                if (dsu.find(i) == i) comps++
            }
            if (comps <= k) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }

    private class DSU(val n: Int) {
        private val parent = IntArray(n) { it }
        private val rank = IntArray(n)

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
    }
}
```

## Dart

```dart
class Solution {
  int minCost(int n, List<List<int>> edges, int k) {
    edges.sort((a, b) => a[2].compareTo(b[2]));
    if (k >= n) return 0;
    int low = 0;
    int high = 0;
    for (var e in edges) {
      if (e[2] > high) high = e[2];
    }
    while (low < high) {
      int mid = (low + high) >> 1;
      if (_canAchieve(n, edges, k, mid)) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }

  bool _canAchieve(int n, List<List<int>> edges, int k, int limit) {
    DSU dsu = DSU(n);
    for (var e in edges) {
      if (e[2] > limit) break;
      dsu.union(e[0], e[1]);
    }
    return dsu.components <= k;
  }
}

class DSU {
  late List<int> parent;
  late List<int> rank;
  int components;

  DSU(int n) {
    parent = List<int>.generate(n, (i) => i);
    rank = List<int>.filled(n, 0);
    components = n;
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
    if (rank[ra] < rank[rb]) {
      parent[ra] = rb;
    } else if (rank[ra] > rank[rb]) {
      parent[rb] = ra;
    } else {
      parent[rb] = ra;
      rank[ra]++;
    }
    components--;
  }
}
```

## Golang

```go
type dsu struct {
	parent []int
	size   []int
	cnt    int
}

func newDSU(n int) *dsu {
	p := make([]int, n)
	sz := make([]int, n)
	for i := 0; i < n; i++ {
		p[i] = i
		sz[i] = 1
	}
	return &dsu{parent: p, size: sz, cnt: n}
}

func (d *dsu) find(x int) int {
	if d.parent[x] != x {
		d.parent[x] = d.find(d.parent[x])
	}
	return d.parent[x]
}

func (d *dsu) union(a, b int) {
	ra := d.find(a)
	rb := d.find(b)
	if ra == rb {
		return
	}
	if d.size[ra] < d.size[rb] {
		ra, rb = rb, ra
	}
	d.parent[rb] = ra
	d.size[ra] += d.size[rb]
	d.cnt--
}

func (d *dsu) components() int {
	return d.cnt
}

func can(limit, n int, edges [][]int, k int) bool {
	ds := newDSU(n)
	for _, e := range edges {
		if e[2] <= limit {
			ds.union(e[0], e[1])
		}
	}
	return ds.components() <= k
}

func minCost(n int, edges [][]int, k int) int {
	maxW := 0
	for _, e := range edges {
		if e[2] > maxW {
			maxW = e[2]
		}
	}
	low, high := 0, maxW
	for low < high {
		mid := (low + high) / 2
		if can(mid, n, edges, k) {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return low
}
```

## Ruby

```ruby
class DSU
  def initialize(n)
    @parent = Array.new(n) { |i| i }
    @rank = Array.new(n, 0)
  end

  def find(x)
    p = @parent[x]
    if p != x
      @parent[x] = find(p)
    end
    @parent[x]
  end

  def union(a, b)
    ra = find(a)
    rb = find(b)
    return false if ra == rb
    if @rank[ra] < @rank[rb]
      @parent[ra] = rb
    elsif @rank[ra] > @rank[rb]
      @parent[rb] = ra
    else
      @parent[rb] = ra
      @rank[ra] += 1
    end
    true
  end
end

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} k
# @return {Integer}
def min_cost(n, edges, k)
  return 0 if k >= n
  edges.sort_by! { |e| e[2] }
  dsu = DSU.new(n)
  components = n
  answer = 0
  edges.each do |u, v, w|
    if dsu.union(u, v)
      components -= 1
    end
    if components <= k
      answer = w
      break
    end
  end
  answer
end
```

## Scala

```scala
object Solution {
  def minCost(n: Int, edges: Array[Array[Int]], k: Int): Int = {
    if (k >= n) return 0
    val sorted = edges.sortBy(_(2))
    val dsu = new DSU(n)
    var components = n
    for (e <- sorted) {
      val w = e(2)
      if (dsu.union(e(0), e(1))) {
        components -= 1
        if (components <= k) return w
      }
    }
    0
  }

  private class DSU(val size: Int) {
    private val parent = Array.tabulate(size)(i => i)
    private val rank = new Array[Int](size)

    def find(x: Int): Int = {
      var p = x
      while (parent(p) != p) {
        parent(p) = parent(parent(p))
        p = parent(p)
      }
      p
    }

    def union(a: Int, b: Int): Boolean = {
      var x = find(a)
      var y = find(b)
      if (x == y) return false
      if (rank(x) < rank(y)) { val tmp = x; x = y; y = tmp }
      parent(y) = x
      if (rank(x) == rank(y)) rank(x) += 1
      true
    }
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost(n: i32, edges: Vec<Vec<i32>>, k: i32) -> i32 {
        let n_usize = n as usize;
        if (k as usize) >= n_usize {
            return 0;
        }
        // Find maximum weight
        let mut max_w = 0i32;
        for e in &edges {
            if e[2] > max_w {
                max_w = e[2];
            }
        }

        // DSU structure
        struct DSU {
            parent: Vec<usize>,
            rank: Vec<u8>,
            comps: usize,
        }
        impl DSU {
            fn new(size: usize) -> Self {
                let mut parent = Vec::with_capacity(size);
                for i in 0..size {
                    parent.push(i);
                }
                DSU { parent, rank: vec![0; size], comps: size }
            }
            fn find(&mut self, x: usize) -> usize {
                if self.parent[x] != x {
                    let root = self.find(self.parent[x]);
                    self.parent[x] = root;
                }
                self.parent[x]
            }
            fn union(&mut self, a: usize, b: usize) -> bool {
                let mut ra = self.find(a);
                let mut rb = self.find(b);
                if ra == rb {
                    return false;
                }
                // Union by rank
                if self.rank[ra] < self.rank[rb] {
                    std::mem::swap(&mut ra, &mut rb);
                }
                self.parent[rb] = ra;
                if self.rank[ra] == self.rank[rb] {
                    self.rank[ra] += 1;
                }
                self.comps -= 1;
                true
            }
        }

        // Feasibility check for a given threshold
        let feasible = |threshold: i32| -> bool {
            let mut dsu = DSU::new(n_usize);
            for e in &edges {
                if e[2] <= threshold {
                    dsu.union(e[0] as usize, e[1] as usize);
                    if dsu.comps <= k as usize {
                        // early exit possible
                        // but continue to ensure correctness; we can break
                    }
                }
            }
            dsu.comps <= k as usize
        };

        let mut low = 0i32;
        let mut high = max_w;
        while low < high {
            let mid = low + (high - low) / 2;
            if feasible(mid) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        low
    }
}
```

## Racket

```racket
(define/contract (min-cost n edges k)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((sorted-edges
           (sort edges
                 (lambda (a b) (< (list-ref a 2) (list-ref b 2)))))
         (max-w
           (if (null? sorted-edges)
               0
               (list-ref (last sorted-edges) 2))))
    (define (feasible? limit)
      (let* ((parent (make-vector n (lambda (i) i)))
             (size   (make-vector n 1))
             (components (box n)))
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
              (if (> (vector-ref size ra) (vector-ref size rb))
                  (begin
                    (vector-set! parent rb ra)
                    (vector-set! size ra (+ (vector-ref size ra)
                                            (vector-ref size rb))))
                  (begin
                    (vector-set! parent ra rb)
                    (vector-set! size rb (+ (vector-ref size rb)
                                            (vector-ref size ra)))))
              (set-box! components (- (unbox components) 1)))))
        (for ([e sorted-edges])
          (let ((w (list-ref e 2)))
            (when (<= w limit)
              (union (list-ref e 0) (list-ref e 1)))))
        (<= (unbox components) k)))
    (let loop ((lo 0) (hi max-w))
      (if (= lo hi)
          lo
          (let ((mid (quotient (+ lo hi) 2)))
            (if (feasible? mid)
                (loop lo mid)
                (loop (+ mid 1) hi)))))))
```

## Erlang

```erlang
-export([min_cost/3]).

-spec min_cost(N :: integer(), Edges :: [[integer()]], K :: integer()) -> integer().
min_cost(N, Edges, K) ->
    MaxW = case Edges of
               [] -> 0;
               _  -> lists:max([W || [_U,_V,W] <- Edges])
           end,
    binary_search(0, MaxW, N, Edges, K).

binary_search(Low, High, N, Edges, K) when Low < High ->
    Mid = (Low + High) div 2,
    case feasible(Mid, N, Edges, K) of
        true -> binary_search(Low, Mid, N, Edges, K);
        false -> binary_search(Mid + 1, High, N, Edges, K)
    end;
binary_search(Ans, _High, _N, _Edges, _K) ->
    Ans.

feasible(T, N, Edges, K) ->
    Parent0 = array:new(N, [{default, -1}]),
    Parent = lists:foldl(
        fun([U,V,W], Acc) ->
            if W =< T -> union(Acc, U, V);
               true   -> Acc
            end
        end,
        Parent0,
        Edges),
    Components = count_components(Parent, N),
    Components =< K.

count_components(Arr, N) ->
    lists:foldl(
        fun(I, Acc) ->
            case array:get(I + 1, Arr) < 0 of
                true -> Acc + 1;
                false -> Acc
            end
        end,
        0,
        lists:seq(0, N - 1)
    ).

union(Arr, X, Y) ->
    {RootX, Arr1} = find(Arr, X),
    {RootY, Arr2} = find(Arr1, Y),
    if RootX == RootY -> Arr2;
       true ->
           SizeX = -array:get(RootX + 1, Arr2),
           SizeY = -array:get(RootY + 1, Arr2),
           if SizeX < SizeY ->
                  % attach X under Y
                  Tmp = array:set(RootX + 1, RootY, Arr2),
                  array:set(RootY + 1, -(SizeX + SizeY), Tmp);
              true ->
                  % attach Y under X
                  Tmp = array:set(RootY + 1, RootX, Arr2),
                  array:set(RootX + 1, -(SizeX + SizeY), Tmp)
           end
    end.

find(Arr, X) ->
    Idx = X + 1,
    Parent = array:get(Idx, Arr),
    if Parent < 0 -> {X, Arr};
       true ->
           {Root, Arr1} = find(Arr, Parent),
           Arr2 = array:set(Idx, Root, Arr1),
           {Root, Arr2}
    end.
```

## Elixir

```elixir
defmodule DSU do
  def new(n) do
    parent_tab = :ets.new(:dsu_parent, [:set, :private])
    rank_tab = :ets.new(:dsu_rank, [:set, :private])

    for i <- 0..(n - 1) do
      :ets.insert(parent_tab, {i, i})
      :ets.insert(rank_tab, {i, 0})
    end

    {parent_tab, rank_tab}
  end

  defp find({parent_tab, _} = dsu, x) do
    [{^x, p}] = :ets.lookup(parent_tab, x)

    if p == x do
      x
    else
      root = find(dsu, p)
      :ets.insert(parent_tab, {x, root})
      root
    end
  end

  def union({parent_tab, rank_tab} = dsu, a, b) do
    ra = find(dsu, a)
    rb = find(dsu, b)

    if ra != rb do
      [{^ra, rank_a}] = :ets.lookup(rank_tab, ra)
      [{^rb, rank_b}] = :ets.lookup(rank_tab, rb)

      cond do
        rank_a < rank_b ->
          :ets.insert(parent_tab, {ra, rb})

        rank_a > rank_b ->
          :ets.insert(parent_tab, {rb, ra})

        true ->
          :ets.insert(parent_tab, {rb, ra})
          :ets.update_element(rank_tab, ra, {2, rank_a + 1})
      end

      true
    else
      false
    end
  end
end

defmodule Solution do
  @spec min_cost(n :: integer, edges :: [[integer]], k :: integer) :: integer
  def min_cost(n, edges, k) do
    sorted_edges = Enum.sort_by(edges, fn [_u, _v, w] -> w end)

    max_w =
      case List.last(sorted_edges) do
        nil -> 0
        [_u, _v, w] -> w
      end

    bin_search = fn low, high ->
      if low < high do
        mid = div(low + high, 2)

        if feasible?(n, sorted_edges, k, mid) do
          bin_search.(low, mid)
        else
          bin_search.(mid + 1, high)
        end
      else
        low
      end
    end

    bin_search.(0, max_w)
  end

  defp feasible?(n, edges, k, limit) do
    dsu = DSU.new(n)

    comps =
      Enum.reduce_while(edges, n, fn [u, v, w], comp ->
        if w <= limit do
          if DSU.union(dsu, u, v) do
            {:cont, comp - 1}
          else
            {:cont, comp}
          end
        else
          {:halt, comp}
        end
      end)

    comps <= k
  end
end
```

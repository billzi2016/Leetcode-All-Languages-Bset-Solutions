# 3608. Minimum Time for K Connected Components

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    struct DSU {
        vector<int> p, r;
        DSU(int n = 0) { init(n); }
        void init(int n) {
            p.resize(n);
            r.assign(n, 0);
            iota(p.begin(), p.end(), 0);
        }
        int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
        bool unite(int a, int b) {
            a = find(a); b = find(b);
            if (a == b) return false;
            if (r[a] < r[b]) swap(a, b);
            p[b] = a;
            if (r[a] == r[b]) ++r[a];
            return true;
        }
    };
public:
    int minTime(int n, vector<vector<int>>& edges, int k) {
        int maxT = 0;
        for (auto &e : edges) maxT = max(maxT, e[2]);
        int low = 0, high = maxT;
        while (low < high) {
            int mid = low + (high - low) / 2;
            DSU dsu(n);
            int comps = n;
            for (auto &e : edges) {
                if (e[2] > mid) {
                    if (dsu.unite(e[0], e[1])) --comps;
                }
            }
            if (comps >= k) high = mid;
            else low = mid + 1;
        }
        return low;
    }
};
```

## Java

```java
class Solution {
    public int minTime(int n, int[][] edges, int k) {
        int maxTime = 0;
        for (int[] e : edges) {
            if (e[2] > maxTime) maxTime = e[2];
        }
        int low = 0, high = maxTime;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (componentsAfterRemoval(n, edges, mid) >= k) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private int componentsAfterRemoval(int n, int[][] edges, int t) {
        DSU dsu = new DSU(n);
        for (int[] e : edges) {
            if (e[2] > t) {
                dsu.union(e[0], e[1]);
            }
        }
        return dsu.count;
    }

    private static class DSU {
        int[] parent;
        byte[] rank;
        int count;

        DSU(int n) {
            parent = new int[n];
            rank = new byte[n];
            for (int i = 0; i < n; i++) parent[i] = i;
            count = n;
        }

        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
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
            count--;
        }
    }
}
```

## Python

```python
class Solution(object):
    def minTime(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0

        max_time = 0
        for _, _, t in edges:
            if t > max_time:
                max_time = t

        # DSU implementation
        def check(limit):
            parent = list(range(n))
            size = [1] * n
            comp = n

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            def union(a, b):
                nonlocal comp
                ra, rb = find(a), find(b)
                if ra == rb:
                    return
                if size[ra] < size[rb]:
                    ra, rb = rb, ra
                parent[rb] = ra
                size[ra] += size[rb]
                comp -= 1

            for u, v, t in edges:
                if t > limit:
                    union(u, v)
                    if comp < k:   # early exit when already enough components
                        break
            return comp >= k

        low, high = 0, max_time
        while low < high:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid + 1
        return low
```

## Python3

```python
class Solution:
    def minTime(self, n: int, edges: list[list[int]], k: int) -> int:
        from typing import List

        class DSU:
            __slots__ = ("parent", "rank", "count")
            def __init__(self, size: int):
                self.parent = list(range(size))
                self.rank = [0] * size
                self.count = size
            def find(self, x: int) -> int:
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x
            def union(self, a: int, b: int) -> None:
                ra = self.find(a)
                rb = self.find(b)
                if ra == rb:
                    return
                if self.rank[ra] < self.rank[rb]:
                    ra, rb = rb, ra
                self.parent[rb] = ra
                if self.rank[ra] == self.rank[rb]:
                    self.rank[ra] += 1
                self.count -= 1

        max_time = 0
        for _, _, t in edges:
            if t > max_time:
                max_time = t

        def enough(limit: int) -> bool:
            dsu = DSU(n)
            for u, v, t in edges:
                if t > limit:
                    dsu.union(u, v)
            return dsu.count >= k

        lo, hi = 0, max_time
        while lo < hi:
            mid = (lo + hi) // 2
            if enough(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## C

```c
#include <stdlib.h>

static int find_set(int *parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static int union_sets(int *parent, int *sz, int a, int b) {
    int ra = find_set(parent, a);
    int rb = find_set(parent, b);
    if (ra == rb) return 0;
    if (sz[ra] < sz[rb]) {
        parent[ra] = rb;
        sz[rb] += sz[ra];
    } else {
        parent[rb] = ra;
        sz[ra] += sz[rb];
    }
    return 1;
}

static int enough_components(int n, int **edges, int edgesSize, int t, int k) {
    int *parent = (int *)malloc(n * sizeof(int));
    int *sz = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        parent[i] = i;
        sz[i] = 1;
    }
    int comps = n;
    for (int i = 0; i < edgesSize; ++i) {
        int time = edges[i][2];
        if (time > t) {
            if (union_sets(parent, sz, edges[i][0], edges[i][1])) {
                --comps;
                if (comps < k) break; // early exit
            }
        }
    }
    free(parent);
    free(sz);
    return comps >= k;
}

int minTime(int n, int** edges, int edgesSize, int* edgesColSize, int k) {
    (void)edgesColSize; // unused
    if (k <= 1) return 0;
    int maxTime = 0;
    for (int i = 0; i < edgesSize; ++i) {
        if (edges[i][2] > maxTime) maxTime = edges[i][2];
    }
    int low = 0, high = maxTime;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (enough_components(n, edges, edgesSize, mid, k))
            high = mid;
        else
            low = mid + 1;
    }
    return low;
}
```

## Csharp

```csharp
public class Solution {
    public int MinTime(int n, int[][] edges, int k) {
        int maxTime = 0;
        foreach (var e in edges) {
            if (e[2] > maxTime) maxTime = e[2];
        }
        int left = 0, right = maxTime;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (EnoughComponents(n, edges, k, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private bool EnoughComponents(int n, int[][] edges, int k, int t) {
        DSU dsu = new DSU(n);
        foreach (var e in edges) {
            if (e[2] > t) {
                dsu.Union(e[0], e[1]);
            }
        }
        return dsu.Components >= k;
    }

    private class DSU {
        private int[] parent;
        private int[] size;
        public int Components { get; private set; }

        public DSU(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
            Components = n;
        }

        private int Find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        public void Union(int a, int b) {
            int ra = Find(a);
            int rb = Find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb]) {
                int tmp = ra; ra = rb; rb = tmp;
            }
            parent[rb] = ra;
            size[ra] += size[rb];
            Components--;
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
var minTime = function(n, edges, k) {
    let maxT = 0;
    for (const e of edges) {
        if (e[2] > maxT) maxT = e[2];
    }

    const canAchieve = (t) => {
        const parent = new Int32Array(n);
        const size = new Int32Array(n);
        for (let i = 0; i < n; ++i) {
            parent[i] = i;
            size[i] = 1;
        }
        let comps = n;

        const find = (x) => {
            while (parent[x] !== x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };

        for (const e of edges) {
            if (e[2] > t) {
                let a = find(e[0]);
                let b = find(e[1]);
                if (a !== b) {
                    if (size[a] < size[b]) { const tmp = a; a = b; b = tmp; }
                    parent[b] = a;
                    size[a] += size[b];
                    --comps;
                }
            }
        }
        return comps >= k;
    };

    let lo = 0, hi = maxT;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (canAchieve(mid)) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    return lo;
};
```

## Typescript

```typescript
function minTime(n: number, edges: number[][], k: number): number {
    // Find maximum edge time to set binary search upper bound
    let maxTime = 0;
    for (const e of edges) {
        if (e[2] > maxTime) maxTime = e[2];
    }

    // DSU implementation
    class DSU {
        parent: number[];
        size: number[];
        components: number;
        constructor(n: number) {
            this.parent = new Array(n);
            this.size = new Array(n);
            for (let i = 0; i < n; i++) {
                this.parent[i] = i;
                this.size[i] = 1;
            }
            this.components = n;
        }
        find(x: number): number {
            while (this.parent[x] !== x) {
                this.parent[x] = this.parent[this.parent[x]];
                x = this.parent[x];
            }
            return x;
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
            this.components--;
        }
    }

    // Helper to check if after removing edges with time <= t we have >=k components
    const canAchieve = (t: number): boolean => {
        const dsu = new DSU(n);
        for (const [u, v, time] of edges) {
            if (time > t) {
                dsu.union(u, v);
                // early exit if already less than k components
                if (dsu.components < k) return false;
            }
        }
        return dsu.components >= k;
    };

    let lo = 0;
    let hi = maxTime;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (canAchieve(mid)) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    return lo;
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
    function minTime($n, $edges, $k) {
        // Find maximum time among edges to set upper bound
        $maxTime = 0;
        foreach ($edges as $e) {
            if ($e[2] > $maxTime) $maxTime = $e[2];
        }

        $low = 0;
        $high = $maxTime; // feasible because removing all edges gives n components

        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->componentsAfterRemoval($n, $edges, $mid) >= $k) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }

        return $low;
    }

    private function componentsAfterRemoval($n, $edges, $t) {
        // Initialize DSU
        $parent = range(0, $n - 1);
        $rank   = array_fill(0, $n, 0);
        $components = $n;

        foreach ($edges as $e) {
            [$u, $v, $time] = $e;
            if ($time > $t) { // edge remains
                // find root of u
                $pu = $u;
                while ($parent[$pu] != $pu) {
                    $parent[$pu] = $parent[$parent[$pu]];
                    $pu = $parent[$pu];
                }
                // find root of v
                $pv = $v;
                while ($parent[$pv] != $pv) {
                    $parent[$pv] = $parent[$parent[$pv]];
                    $pv = $parent[$pv];
                }

                if ($pu !== $pv) {
                    // union by rank
                    if ($rank[$pu] < $rank[$pv]) {
                        $parent[$pu] = $pv;
                    } elseif ($rank[$pu] > $rank[$pv]) {
                        $parent[$pv] = $pu;
                    } else {
                        $parent[$pv] = $pu;
                        $rank[$pu]++;
                    }
                    $components--;
                }
            }
        }

        return $components;
    }
}
```

## Swift

```swift
class Solution {
    func minTime(_ n: Int, _ edges: [[Int]], _ k: Int) -> Int {
        let maxT = edges.map { $0[2] }.max() ?? 0
        var low = 0
        var high = maxT
        while low < high {
            let mid = (low + high) / 2
            if componentsAfterRemoving(n, edges, t: mid) >= k {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }
    
    private func componentsAfterRemoving(_ n: Int, _ edges: [[Int]], t: Int) -> Int {
        let dsu = DSU(n)
        var comps = n
        for e in edges {
            if e[2] > t {
                if dsu.union(e[0], e[1]) {
                    comps -= 1
                }
            }
        }
        return comps
    }
}

private class DSU {
    private var parent: [Int]
    private var size: [Int]
    
    init(_ n: Int) {
        parent = Array(0..<n)
        size = [Int](repeating: 1, count: n)
    }
    
    func find(_ x: Int) -> Int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }
    
    @discardableResult
    func union(_ a: Int, _ b: Int) -> Bool {
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
    private class DSU(n: Int) {
        private val parent = IntArray(n) { it }
        private val rank = IntArray(n)
        var count = n
            private set

        private fun find(x: Int): Int {
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
                val tmp = ra
                ra = rb
                rb = tmp
            }
            parent[rb] = ra
            if (rank[ra] == rank[rb]) rank[ra]++
            count--
        }
    }

    fun minTime(n: Int, edges: Array<IntArray>, k: Int): Int {
        var maxTime = 0
        for (e in edges) {
            if (e[2] > maxTime) maxTime = e[2]
        }
        var low = 0
        var high = maxTime
        while (low < high) {
            val mid = (low + high) ushr 1
            if (componentsAfter(n, edges, mid) >= k) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }

    private fun componentsAfter(n: Int, edges: Array<IntArray>, t: Int): Int {
        val dsu = DSU(n)
        for (e in edges) {
            if (e[2] > t) {
                dsu.union(e[0], e[1])
            }
        }
        return dsu.count
    }
}
```

## Dart

```dart
class Solution {
  int minTime(int n, List<List<int>> edges, int k) {
    // Find maximum time among edges
    int maxTime = 0;
    for (var e in edges) {
      if (e[2] > maxTime) maxTime = e[2];
    }

    // Helper: count components after removing edges with time <= t
    int countComponents(int t) {
      var dsu = _DSU(n);
      for (var e in edges) {
        if (e[2] > t) {
          dsu.union(e[0], e[1]);
        }
      }
      return dsu.components;
    }

    // If already enough components at time 0, answer is 0
    if (countComponents(0) >= k) return 0;

    int low = 0;
    int high = maxTime; // inclusive

    while (low < high) {
      int mid = low + ((high - low) >> 1);
      if (countComponents(mid) >= k) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }
}

class _DSU {
  late List<int> parent;
  late List<int> rank;
  int components;

  _DSU(int n)
      : components = n,
        parent = List.generate(n, (i) => i),
        rank = List.filled(n, 0);

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
func minTime(n int, edges [][]int, k int) int {
    maxT := 0
    for _, e := range edges {
        if e[2] > maxT {
            maxT = e[2]
        }
    }

    low, high := -1, maxT
    for low+1 < high {
        mid := low + (high-low)/2
        if enoughComponents(n, edges, k, mid) {
            high = mid
        } else {
            low = mid
        }
    }
    return high
}

func enoughComponents(n int, edges [][]int, k int, t int) bool {
    parent := make([]int, n)
    size := make([]int, n)
    for i := 0; i < n; i++ {
        parent[i] = i
        size[i] = 1
    }
    comp := n

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
        comp--
    }

    for _, e := range edges {
        if e[2] > t {
            union(e[0], e[1])
        }
    }
    return comp >= k
}
```

## Ruby

```ruby
def min_time(n, edges, k)
  max_time = edges.map { |e| e[2] }.max || 0

  # DSU implementation
  class DSU
    def initialize(size)
      @parent = Array.new(size) { |i| i }
      @rank   = Array.new(size, 0)
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

  # Helper to count components after removing edges with time <= t
  count_components = lambda do |t|
    dsu = DSU.new(n)
    comps = n
    edges.each do |u, v, time|
      if time > t && dsu.union(u, v)
        comps -= 1
        # early exit: if components already less than k, they can only decrease further
        return comps if comps < k
      end
    end
    comps
  end

  low = 0
  high = max_time
  while low < high
    mid = (low + high) / 2
    if count_components.call(mid) >= k
      high = mid
    else
      low = mid + 1
    end
  end
  low
end
```

## Scala

```scala
object Solution {
  def minTime(n: Int, edges: Array[Array[Int]], k: Int): Int = {
    val maxT = if (edges.isEmpty) 0 else edges.map(_(2)).max
    var lo = 0
    var hi = maxT
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (enough(mid, n, edges, k)) {
        hi = mid
      } else {
        lo = mid + 1
      }
    }
    lo
  }

  private def enough(t: Int, n: Int, edges: Array[Array[Int]], k: Int): Boolean = {
    val parent = Array.tabulate(n)(i => i)
    val rank = new Array[Int](n)
    var components = n

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
      if (ra == rb) return
      if (rank(ra) < rank(rb)) {
        parent(ra) = rb
      } else if (rank(ra) > rank(rb)) {
        parent(rb) = ra
      } else {
        parent(rb) = ra
        rank(ra) += 1
      }
      components -= 1
    }

    var i = 0
    while (i < edges.length) {
      val e = edges(i)
      if (e(2) > t) {
        union(e(0), e(1))
        if (components < k) return false
      }
      i += 1
    }
    components >= k
  }
}
```

## Rust

```rust
use std::mem::swap;

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
        let rank = vec![0; n];
        DSU { parent, rank }
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
        if self.rank[ra] < self.rank[rb] {
            swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        if self.rank[ra] == self.rank[rb] {
            self.rank[ra] += 1;
        }
        true
    }
}

fn enough_components(n: usize, edges: &[(usize, usize, i64)], limit: i64, k: usize) -> bool {
    let mut dsu = DSU::new(n);
    let mut comps = n;
    for &(u, v, time) in edges.iter() {
        if time > limit && dsu.union(u, v) {
            comps -= 1;
        }
    }
    comps >= k
}

impl Solution {
    pub fn min_time(n: i32, edges: Vec<Vec<i32>>, k: i32) -> i32 {
        let n_usize = n as usize;
        let mut max_t: i64 = 0;
        let mut edge_list: Vec<(usize, usize, i64)> = Vec::with_capacity(edges.len());
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let t = e[2] as i64;
            if t > max_t {
                max_t = t;
            }
            edge_list.push((u, v, t));
        }

        let mut lo: i64 = 0;
        let mut hi: i64 = max_t;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if enough_components(n_usize, &edge_list, mid, k as usize) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }
}
```

## Racket

```racket
(define/contract (min-time n edges k)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer?)
  
  ;; Disjoint Set Union helpers
  (define (make-dsu size)
    (vector (list->vector (build-list size identity))
            (make-vector size 0)))
  
  (define (find dsu x)
    (let* ([parent (vector-ref dsu 0)])
      (let loop ([x x])
        (let ([p (vector-ref parent x)])
          (if (= p x)
              x
              (let ([root (loop p)])
                (vector-set! parent x root)
                root))))))
  
  (define (union dsu a b)
    (let* ([parent (vector-ref dsu 0)]
           [rank   (vector-ref dsu 1)]
           [ra (find dsu a)]
           [rb (find dsu b)])
      (when (not (= ra rb))
        (let ([ra-rank (vector-ref rank ra)]
              [rb-rank (vector-ref rank rb)])
          (cond [(< ra-rank rb-rank)
                 (vector-set! parent ra rb)]
                [(> ra-rank rb-rank)
                 (vector-set! parent rb ra)]
                [else
                 (vector-set! parent rb ra)
                 (vector-set! rank ra (+ ra-rank 1))])))))
  
  ;; Count components after removing edges with time <= t
  (define (components thresh)
    (let ([dsu (make-dsu n)])
      (for ([e edges])
        (let ([u   (list-ref e 0)]
              [v   (list-ref e 1)]
              [tim (list-ref e 2)])
          (when (> tim thresh)
            (union dsu u v))))
      (let loop ([i 0] [cnt 0])
        (if (= i n)
            cnt
            (let ([root (find dsu i)])
              (loop (+ i 1) (if (= root i) (+ cnt 1) cnt)))))))
  
  ;; If already enough components, answer is 0
  (if (>= (components 0) k)
      0
      (let* ([max-time (apply max (map (lambda (e) (list-ref e 2)) edges))]
             [low 1]
             [high max-time])
        (let loop ()
          (if (< low high)
              (let* ([mid (quotient (+ low high) 2)]
                     [cnt (components mid)])
                (if (>= cnt k)
                    (begin (set! high mid) (loop))
                    (begin (set! low (+ mid 1)) (loop))))
              low))))))
```

## Erlang

```erlang
-module(solution).
-export([min_time/3]).

-spec min_time(N :: integer(), Edges :: [[integer()]], K :: integer()) -> integer().
min_time(N, Edges, K) ->
    MaxTime = case Edges of
        [] -> 0;
        _ -> lists:max([T || [_U,_V,T] <- Edges])
    end,
    case components(N, Edges, 0) of
        C when C >= K -> 0;
        _ -> binary_search(1, MaxTime, N, Edges, K)
    end.

binary_search(Low, High, N, Edges, K) when Low =< High ->
    if Low == High ->
            Low;
       true ->
            Mid = (Low + High) div 2,
            C = components(N, Edges, Mid),
            if C >= K ->
                    binary_search(Low, Mid, N, Edges, K);
               true ->
                    binary_search(Mid + 1, High, N, Edges, K)
            end
    end.

components(N, Edges, T) ->
    Parent = ets:new(parent, [set, private]),
    Size = ets:new(size, [set, private]),
    lists:foreach(fun(I) -> ets:insert(Parent, {I, I}), ets:insert(Size, {I, 1}) end,
                  lists:seq(0, N - 1)),
    Count0 = N,
    Count = lists:foldl(
        fun([U, V, Time], Acc) ->
            if Time > T ->
                    case union(U, V, Parent, Size) of
                        true -> Acc - 1;
                        false -> Acc
                    end;
               true -> Acc
            end
        end,
        Count0,
        Edges),
    ets:delete(Parent),
    ets:delete(Size),
    Count.

find(Node, Tab) ->
    case ets:lookup(Tab, Node) of
        [{_, Parent}] when Parent =:= Node ->
            Node;
        [{_, Parent}] ->
            Root = find(Parent, Tab),
            ets:update_element(Tab, Node, {2, Root}),
            Root
    end.

union(U, V, ParentTab, SizeTab) ->
    Ru = find(U, ParentTab),
    Rv = find(V, ParentTab),
    if Ru == Rv ->
            false;
       true ->
            SU = ets:lookup_element(SizeTab, Ru, 2),
            SV = ets:lookup_element(SizeTab, Rv, 2),
            if SU < SV ->
                    ets:update_element(ParentTab, Ru, {2, Rv}),
                    ets:update_element(SizeTab, Rv, {2, SU + SV});
               true ->
                    ets:update_element(ParentTab, Rv, {2, Ru}),
                    ets:update_element(SizeTab, Ru, {2, SU + SV})
            end,
            true
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_time(n :: integer, edges :: [[integer]], k :: integer) :: integer
  def min_time(n, edges, k) do
    max_time =
      Enum.reduce(edges, 0, fn [_u, _v, time], acc ->
        if time > acc, do: time, else: acc
      end)

    binary_search(0, max_time, n, edges, k)
  end

  defp binary_search(low, high, n, edges, k) do
    if low < high do
      mid = div(low + high, 2)
      comps = count_components(n, edges, mid)

      if comps >= k do
        binary_search(low, mid, n, edges, k)
      else
        binary_search(mid + 1, high, n, edges, k)
      end
    else
      low
    end
  end

  defp count_components(n, edges, t) do
    parent = :array.from_list(Enum.map(0..n - 1, fn i -> i end))
    rank = :array.new(n, default: 0)

    {_, _, comps} =
      Enum.reduce(edges, {parent, rank, n}, fn [u, v, time], acc ->
        if time > t do
          union(u, v, elem(acc, 0), elem(acc, 1), elem(acc, 2))
        else
          acc
        end
      end)

    comps
  end

  defp find(x, parent) do
    p = :array.get(x, parent)

    if p == x do
      {x, parent}
    else
      {root, parent2} = find(p, parent)
      parent3 = :array.set(x, root, parent2)
      {root, parent3}
    end
  end

  defp union(a, b, parent, rank, comps) do
    {ra, parent1} = find(a, parent)
    {rb, parent2} = find(b, parent1)

    if ra == rb do
      {parent2, rank, comps}
    else
      rank_a = :array.get(ra, rank)
      rank_b = :array.get(rb, rank)

      cond do
        rank_a < rank_b ->
          parent3 = :array.set(ra, rb, parent2)
          {parent3, rank, comps - 1}

        rank_a > rank_b ->
          parent3 = :array.set(rb, ra, parent2)
          {parent3, rank, comps - 1}

        true ->
          parent3 = :array.set(rb, ra, parent2)
          rank3 = :array.set(ra, rank_a + 1, rank)
          {parent3, rank3, comps - 1}
      end
    end
  end
end
```

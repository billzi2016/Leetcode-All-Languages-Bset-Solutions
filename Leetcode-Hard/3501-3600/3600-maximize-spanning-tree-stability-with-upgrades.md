# 3600. Maximize Spanning Tree Stability with Upgrades

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> p, sz;
        int comps;
        DSU(int n): p(n), sz(n,1), comps(n) { iota(p.begin(), p.end(), 0); }
        int find(int x){ return p[x]==x?x:p[x]=find(p[x]); }
        bool unite(int a,int b){
            a=find(a); b=find(b);
            if(a==b) return false;
            if(sz[a]<sz[b]) swap(a,b);
            p[b]=a; sz[a]+=sz[b];
            --comps;
            return true;
        }
    };
    
    struct Edge {
        int u, v;
        int s;
        int must;
    };
    
    bool feasible(int n, const vector<Edge>& edges, int k, long long X) {
        DSU dsu(n);
        // first pass: edges usable without upgrade
        for (const auto& e : edges) {
            if ((long long)e.s >= X) {
                dsu.unite(e.u, e.v);
            }
        }
        int used = 0;
        // second pass: edges requiring an upgrade
        for (const auto& e : edges) {
            if ((long long)e.s < X && e.must == 0 && (long long)e.s * 2 >= X) {
                if (dsu.unite(e.u, e.v)) {
                    ++used;
                    if (used > k) return false;
                }
            }
        }
        return dsu.comps == 1 && used <= k;
    }
    
    int maxStability(int n, vector<vector<int>>& edgesVec, int k) {
        vector<Edge> edges;
        edges.reserve(edgesVec.size());
        long long hi = 0;
        for (auto& v : edgesVec) {
            Edge e{v[0], v[1], v[2], v[3]};
            edges.push_back(e);
            hi = max(hi, (long long)v[2] * 2);
        }
        if (!feasible(n, edges, k, 0)) return -1;
        long long lo = 0;
        while (lo < hi) {
            long long mid = (lo + hi + 1) >> 1;
            if (feasible(n, edges, k, mid))
                lo = mid;
            else
                hi = mid - 1;
        }
        return (int)lo;
    }
};
```

## Java

```java
class Solution {
    public int maxStability(int n, int[][] edges, int k) {
        int hi = 0;
        for (int[] e : edges) {
            int s = e[2];
            hi = Math.max(hi, Math.max(s, s * 2));
        }
        int lo = 0;
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (canAchieve(n, edges, k, mid)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return canAchieve(n, edges, k, lo) ? lo : -1;
    }

    private boolean canAchieve(int n, int[][] edges, int k, int target) {
        DSU dsu = new DSU(n);
        // Process mandatory edges
        for (int[] e : edges) {
            if (e[3] == 1) { // must edge
                int u = e[0], v = e[1], s = e[2];
                if (s < target) return false;
                if (!dsu.union(u, v)) return false; // creates cycle
            }
        }
        // Use free edges (no upgrade needed)
        for (int[] e : edges) {
            if (e[3] == 0 && e[2] >= target) {
                dsu.union(e[0], e[1]);
            }
        }
        int used = 0;
        // Use upgradeable edges
        for (int[] e : edges) {
            if (e[3] == 0 && e[2] < target && (long) e[2] * 2 >= target) {
                int u = e[0], v = e[1];
                if (dsu.find(u) != dsu.find(v)) {
                    dsu.union(u, v);
                    used++;
                    if (used > k) return false;
                }
            }
        }
        return dsu.components == 1 && used <= k;
    }

    private static class DSU {
        int[] parent;
        int[] size;
        int components;

        DSU(int n) {
            parent = new int[n];
            size = new int[n];
            components = n;
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }

        boolean union(int a, int b) {
            int ra = find(a);
            int rb = find(b);
            if (ra == rb) return false;
            if (size[ra] < size[rb]) {
                int tmp = ra; ra = rb; rb = tmp;
            }
            parent[rb] = ra;
            size[ra] += size[rb];
            components--;
            return true;
        }
    }
}
```

## Python

```python
class Solution(object):
    def maxStability(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        # check overall connectivity ignoring strengths
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
                return False
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
            return True

        for u, v, s, m in edges:
            union(u, v)
        if sum(1 for i in range(n) if find(i) == i) != 1:
            return -1

        max_val = 0
        for _, _, s, _ in edges:
            max_val = max(max_val, 2 * s)

        def feasible(threshold):
            # DSU for this check
            p = list(range(n))
            sz = [1] * n

            def f(x):
                while p[x] != x:
                    p[x] = p[p[x]]
                    x = p[x]
                return x

            def u(a, b):
                ra, rb = f(a), f(b)
                if ra == rb:
                    return False
                if sz[ra] < sz[rb]:
                    ra, rb = rb, ra
                p[rb] = ra
                sz[ra] += sz[rb]
                return True

            # first use edges that already satisfy threshold without upgrade
            for u_, v_, s_, m_ in edges:
                if s_ >= threshold:
                    u(u_, v_)
            upgrades_used = 0
            # then consider upgradable edges
            for u_, v_, s_, m_ in edges:
                if s_ < threshold and m_ == 0 and 2 * s_ >= threshold:
                    if f(u_) != f(v_):
                        u(u_, v_)
                        upgrades_used += 1
                        if upgrades_used > k:
                            return False
            # check connectivity
            root = f(0)
            for i in range(1, n):
                if f(i) != root:
                    return False
            return True

        lo, hi = 1, max_val
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo if feasible(lo) else -1
```

## Python3

```python
import sys
from typing import List

class DSU:
    __slots__ = ("parent", "size")
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        must_edges = []
        opt_edges = []
        max_strength = 0
        for u, v, s, m in edges:
            max_strength = max(max_strength, s * 2)
            if m == 1:
                must_edges.append((u, v, s))
            else:
                opt_edges.append((s, u, v))
        opt_edges.sort(reverse=True)   # descending by original strength

        def feasible(target: int) -> bool:
            dsu = DSU(n)
            used = 0
            upgrades = 0

            # must edges must be taken without upgrade
            for u, v, s in must_edges:
                if s < target:
                    return False
                if not dsu.union(u, v):
                    return False   # cycle among mandatory edges
                used += 1

            if used > n - 1:
                return False

            for s, u, v in opt_edges:
                if used == n - 1:
                    break
                if dsu.find(u) == dsu.find(v):
                    continue
                if s >= target:
                    dsu.union(u, v)
                    used += 1
                elif 2 * s >= target and upgrades < k:
                    dsu.union(u, v)
                    used += 1
                    upgrades += 1
                # else cannot use this edge for current target

            return used == n - 1

        low, high = 0, max_strength
        while low < high:
            mid = (low + high + 1) // 2
            if feasible(mid):
                low = mid
            else:
                high = mid - 1

        return low if feasible(low) else -1
```

## C

```c
#include <stdlib.h>

typedef struct {
    int u;
    int v;
    int s;
    int must;
} Edge;

static int *parent_;
static int *sz_;

static int find_set(int x) {
    while (parent_[x] != x) {
        parent_[x] = parent_[parent_[x]];
        x = parent_[x];
    }
    return x;
}

static void union_set(int a, int b) {
    int ra = find_set(a);
    int rb = find_set(b);
    if (ra == rb) return;
    if (sz_[ra] < sz_[rb]) {
        parent_[ra] = rb;
        sz_[rb] += sz_[ra];
    } else {
        parent_[rb] = ra;
        sz_[ra] += sz_[rb];
    }
}

static int can_connect(int n, Edge *e, int m, int k, int T) {
    for (int i = 0; i < n; ++i) {
        parent_[i] = i;
        sz_[i] = 1;
    }

    // process must=1 edges
    for (int i = 0; i < m; ++i) {
        if (e[i].must == 1) {
            if (e[i].s < T) return 0;
            union_set(e[i].u, e[i].v);
        }
    }

    // free edges (must=0 and s >= T)
    for (int i = 0; i < m; ++i) {
        if (e[i].must == 0 && e[i].s >= T) {
            union_set(e[i].u, e[i].v);
        }
    }

    int used = 0;
    // upgrade edges (must=0, s < T <= 2*s)
    for (int i = 0; i < m; ++i) {
        if (e[i].must == 0 && e[i].s < T && 2 * e[i].s >= T) {
            int ru = find_set(e[i].u);
            int rv = find_set(e[i].v);
            if (ru != rv) {
                union_set(ru, rv);
                ++used;
                if (used > k) return 0;
            }
        }
    }

    int root = find_set(0);
    for (int i = 1; i < n; ++i) {
        if (find_set(i) != root) return 0;
    }
    return 1;
}

int maxStability(int n, int** edges, int edgesSize, int* edgesColSize, int k) {
    Edge *e = (Edge *)malloc(sizeof(Edge) * edgesSize);
    int max_s = 0;
    for (int i = 0; i < edgesSize; ++i) {
        e[i].u = edges[i][0];
        e[i].v = edges[i][1];
        e[i].s = edges[i][2];
        e[i].must = edges[i][3];
        if (e[i].s > max_s) max_s = e[i].s;
    }

    parent_ = (int *)malloc(sizeof(int) * n);
    sz_ = (int *)malloc(sizeof(int) * n);

    int low = 0, high = max_s * 2;
    while (low < high) {
        int mid = low + (high - low + 1) / 2;
        if (can_connect(n, e, edgesSize, k, mid))
            low = mid;
        else
            high = mid - 1;
    }

    int ans = can_connect(n, e, edgesSize, k, low) ? low : -1;

    free(e);
    free(parent_);
    free(sz_);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxStability(int n, int[][] edges, int k) {
        int maxS = 0;
        foreach (var e in edges) {
            if (e[2] > maxS) maxS = e[2];
        }
        // Helper DSU
        bool Check(int target) {
            var dsu = new DSU(n);
            int components = n;
            // First, use edges that already satisfy without upgrade
            foreach (var e in edges) {
                int u = e[0], v = e[1], s = e[2];
                if (s >= target) {
                    if (dsu.Union(u, v)) components--;
                }
            }
            // Collect potential upgraded edges
            var upgradeEdges = new List<(int u, int v)>();
            foreach (var e in edges) {
                int u = e[0], v = e[1], s = e[2], must = e[3];
                if (must == 0 && s < target && (long)s * 2 >= target) {
                    upgradeEdges.Add((u, v));
                }
            }
            int usedUpgrades = 0;
            foreach (var (u, v) in upgradeEdges) {
                if (components == 1) break;
                if (dsu.Union(u, v)) {
                    components--;
                    usedUpgrades++;
                    if (usedUpgrades > k) return false;
                }
            }
            return components == 1 && usedUpgrades <= k;
        }

        // If even the minimal possible stability cannot be achieved, return -1
        if (!Check(1)) return -1;

        int lo = 1, hi = maxS * 2; // inclusive upper bound
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (Check(mid)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }

    private class DSU {
        private int[] parent;
        private int[] rank;
        public DSU(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        public int Find(int x) {
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }
        public bool Union(int a, int b) {
            int ra = Find(a), rb = Find(b);
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

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} k
 * @return {number}
 */
var maxStability = function(n, edges, k) {
    class DSU {
        constructor(size) {
            this.parent = new Int32Array(size);
            this.rank = new Uint8Array(size);
            for (let i = 0; i < size; i++) this.parent[i] = i;
            this.components = size;
        }
        find(x) {
            let root = x;
            while (this.parent[root] !== root) root = this.parent[root];
            // path compression
            while (this.parent[x] !== x) {
                const p = this.parent[x];
                this.parent[x] = root;
                x = p;
            }
            return root;
        }
        union(a, b) {
            let ra = this.find(a), rb = this.find(b);
            if (ra === rb) return false;
            if (this.rank[ra] < this.rank[rb]) {
                this.parent[ra] = rb;
            } else if (this.rank[ra] > this.rank[rb]) {
                this.parent[rb] = ra;
            } else {
                this.parent[rb] = ra;
                this.rank[ra]++;
            }
            this.components--;
            return true;
        }
    }

    const maxS = edges.reduce((mx, e) => Math.max(mx, e[2]), 0);

    function can(T) {
        const dsu = new DSU(n);
        // use zero‑cost edges (no upgrade needed)
        for (const e of edges) {
            const [u, v, s, must] = e;
            if ((must === 1 && s >= T) || (must === 0 && s >= T)) {
                dsu.union(u, v);
                if (dsu.components === 1) break;
            }
        }
        let used = 0;
        // use edges that require one upgrade
        for (const e of edges) {
            const [u, v, s, must] = e;
            if (must === 0 && s < T && s * 2 >= T) {
                if (dsu.union(u, v)) {
                    used++;
                    if (used > k) return false;
                    if (dsu.components === 1) break;
                }
            }
        }
        return dsu.components === 1 && used <= k;
    }

    // quick impossibility check
    if (!can(1)) return -1;

    let lo = 0, hi = maxS * 2;
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (can(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
```

## Typescript

```typescript
function maxStability(n: number, edges: number[][], k: number): number {
    class DSU {
        parent: Int32Array;
        rank: Int8Array;
        constructor(size: number) {
            this.parent = new Int32Array(size);
            this.rank = new Int8Array(size);
            for (let i = 0; i < size; i++) this.parent[i] = i;
        }
        find(x: number): number {
            let p = this.parent[x];
            if (p !== x) this.parent[x] = this.find(p);
            return this.parent[x];
        }
        union(a: number, b: number): boolean {
            a = this.find(a);
            b = this.find(b);
            if (a === b) return false;
            if (this.rank[a] < this.rank[b]) {
                const t = a;
                a = b;
                b = t;
            }
            this.parent[b] = a;
            if (this.rank[a] === this.rank[b]) this.rank[a]++;
            return true;
        }
    }

    // maximum possible strength after upgrade
    let maxPossible = 0;
    for (let i = 0; i < edges.length; i++) {
        const s = edges[i][2];
        const must = edges[i][3];
        if (must === 0) {
            if (s * 2 > maxPossible) maxPossible = s * 2;
        } else {
            if (s > maxPossible) maxPossible = s;
        }
    }

    function can(target: number): boolean {
        const dsu = new DSU(n);
        let comps = n;
        // use free edges
        for (let i = 0; i < edges.length; i++) {
            const [u, v, s] = edges[i];
            if (s >= target) {
                if (dsu.union(u, v)) comps--;
            }
        }
        let usedUpgrades = 0;
        // use upgradeable edges
        for (let i = 0; i < edges.length; i++) {
            const [u, v, s, must] = edges[i];
            if (s < target && must === 0 && s * 2 >= target) {
                if (dsu.union(u, v)) {
                    comps--;
                    usedUpgrades++;
                    if (usedUpgrades > k) return false;
                }
            }
        }
        return comps === 1 && usedUpgrades <= k;
    }

    // quick check for overall connectivity
    if (!can(0)) return -1;

    let low = 0, high = maxPossible;
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (can(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
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
    function maxStability($n, $edges, $k) {
        // store edges as simple arrays for speed
        $elist = [];
        $maxS = 0;
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $s = $e[2];
            $must = $e[3];
            $elist[] = [$u, $v, $s, $must];
            if ($s > $maxS) $maxS = $s;
        }

        // check overall connectivity
        $dsuAll = new DSU($n);
        foreach ($elist as $e) {
            $dsuAll->union($e[0], $e[1]);
        }
        $root = $dsuAll->find(0);
        for ($i = 1; $i < $n; $i++) {
            if ($dsuAll->find($i) !== $root) return -1;
        }

        $low = 1;
        $high = $maxS * 2;
        $ans = 0;

        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->canAchieve($mid, $n, $elist, $k)) {
                $ans = $mid;
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
            }
        }

        return $ans;
    }

    private function canAchieve($target, $n, $edges, $k) {
        $dsu = new DSU($n);
        // edges that already satisfy the target without upgrade
        foreach ($edges as $e) {
            if ($e[2] >= $target) {
                $dsu->union($e[0], $e[1]);
            }
        }

        $used = 0;
        // edges that can reach target after one upgrade (must == 0)
        foreach ($edges as $e) {
            if ($e[3] == 0 && $e[2] < $target && $e[2] * 2 >= $target) {
                if ($dsu->union($e[0], $e[1])) {
                    $used++;
                    if ($used > $k) return false;
                }
            }
        }

        // verify all nodes are connected
        $root = $dsu->find(0);
        for ($i = 1; $i < $n; $i++) {
            if ($dsu->find($i) !== $root) return false;
        }
        return true;
    }
}

class DSU {
    public array $parent;
    public array $size;

    function __construct(int $n) {
        $this->parent = range(0, $n - 1);
        $this->size = array_fill(0, $n, 1);
    }

    function find(int $x): int {
        while ($this->parent[$x] !== $x) {
            $this->parent[$x] = $this->parent[$this->parent[$x]];
            $x = $this->parent[$x];
        }
        return $x;
    }

    function union(int $a, int $b): bool {
        $ra = $this->find($a);
        $rb = $this->find($b);
        if ($ra === $rb) return false;
        if ($this->size[$ra] < $this->size[$rb]) {
            $tmp = $ra; $ra = $rb; $rb = $tmp;
        }
        $this->parent[$rb] = $ra;
        $this->size[$ra] += $this->size[$rb];
        return true;
    }
}
```

## Swift

```swift
class DSU {
    private var parent: [Int]
    private var size: [Int]
    var components: Int

    init(_ n: Int) {
        parent = Array(0..<n)
        size = Array(repeating: 1, count: n)
        components = n
    }

    func find(_ x: Int) -> Int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    func union(_ a: Int, _ b: Int) {
        var x = find(a)
        var y = find(b)
        if x == y { return }
        if size[x] < size[y] {
            swap(&x, &y)
        }
        parent[y] = x
        size[x] += size[y]
        components -= 1
    }
}

struct Edge {
    let u: Int
    let v: Int
    let s: Int
    let must: Int
}

class Solution {
    func maxStability(_ n: Int, _ edges: [[Int]], _ k: Int) -> Int {
        var edgeList = [Edge]()
        var maxVal = 0
        for e in edges {
            let u = e[0], v = e[1], s = e[2], must = e[3]
            edgeList.append(Edge(u: u, v: v, s: s, must: must))
            maxVal = max(maxVal, s * 2)
        }

        // Check overall connectivity
        var dsuAll = DSU(n)
        for e in edgeList {
            dsuAll.union(e.u, e.v)
        }
        if dsuAll.components != 1 {
            return -1
        }

        func feasible(_ T: Int) -> Bool {
            let dsu = DSU(n)
            var oneCostEdges = [(Int, Int)]()
            for e in edgeList {
                if e.s >= T {
                    dsu.union(e.u, e.v)
                } else if e.must == 0 && e.s * 2 >= T {
                    oneCostEdges.append((e.u, e.v))
                }
            }

            var used = 0
            for (u, v) in oneCostEdges {
                if dsu.find(u) != dsu.find(v) {
                    dsu.union(u, v)
                    used += 1
                    if used > k { return false }
                }
            }
            return dsu.components == 1 && used <= k
        }

        var low = 0
        var high = maxVal
        while low < high {
            let mid = (low + high + 1) >> 1
            if feasible(mid) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class DSU(val n: Int) {
        private val parent = IntArray(n) { it }
        private val size = IntArray(n) { 1 }
        var comp = n
            private set

        fun find(x: Int): Int {
            var v = x
            while (parent[v] != v) {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
        }

        fun union(a: Int, b: Int): Boolean {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return false
            if (size[ra] < size[rb]) {
                val tmp = ra
                ra = rb
                rb = tmp
            }
            parent[rb] = ra
            size[ra] += size[rb]
            comp--
            return true
        }
    }

    fun maxStability(n: Int, edges: Array<IntArray>, k: Int): Int {
        var maxVal = 0
        for (e in edges) {
            val s = e[2]
            if (s * 2 > maxVal) maxVal = s * 2
        }
        var lo = 1
        var hi = maxVal
        var ans = -1
        while (lo <= hi) {
            val mid = (lo + hi) ushr 1
            if (check(mid, n, edges, k)) {
                ans = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return ans
    }

    private fun check(limit: Int, n: Int, edges: Array<IntArray>, k: Int): Boolean {
        val dsu = DSU(n)
        // mandatory edges must be taken without upgrade
        for (e in edges) {
            if (e[3] == 1) {
                val s = e[2]
                if (s < limit) return false
                if (!dsu.union(e[0], e[1])) return false // cycle among mandatory edges
            }
        }
        // optional edges that already meet the limit without upgrade
        for (e in edges) {
            if (e[3] == 0 && e[2] >= limit) {
                dsu.union(e[0], e[1])
            }
        }
        var used = 0
        // optional edges that need an upgrade
        for (e in edges) {
            if (e[3] == 0 && e[2] < limit && e[2] * 2 >= limit) {
                if (used >= k) continue
                if (dsu.union(e[0], e[1])) {
                    used++
                }
            }
        }
        return dsu.comp == 1 && used <= k
    }
}
```

## Dart

```dart
class DSU {
  late List<int> parent;
  late List<int> size;
  int count = 0;

  DSU(int n) {
    parent = List.generate(n, (i) => i);
    size = List.filled(n, 1);
    count = n;
  }

  int find(int x) {
    while (parent[x] != x) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return x;
  }

  bool union(int a, int b) {
    int ra = find(a);
    int rb = find(b);
    if (ra == rb) return false;
    if (size[ra] < size[rb]) {
      int tmp = ra;
      ra = rb;
      rb = tmp;
    }
    parent[rb] = ra;
    size[ra] += size[rb];
    count--;
    return true;
  }
}

class Solution {
  bool _can(int n, List<List<int>> edges, int k, int target) {
    DSU dsu = DSU(n);
    // process mandatory edges
    for (var e in edges) {
      if (e[3] == 1) {
        int w = e[2];
        if (w < target) return false;
        if (!dsu.union(e[0], e[1])) return false; // cycle among must edges
      }
    }

    List<List<int>> needUpgrade = [];
    // optional edges without upgrade
    for (var e in edges) {
      if (e[3] == 0) {
        int w = e[2];
        if (w >= target) {
          dsu.union(e[0], e[1]);
        } else if (w * 2 >= target) {
          needUpgrade.add(e);
        }
      }
    }

    int used = 0;
    for (var e in needUpgrade) {
      if (used >= k) break;
      if (dsu.find(e[0]) != dsu.find(e[1])) {
        dsu.union(e[0], e[1]);
        used++;
        if (dsu.count == 1) break;
      }
    }

    return dsu.count == 1 && used <= k;
  }

  int maxStability(int n, List<List<int>> edges, int k) {
    int maxW = 0;
    for (var e in edges) {
      if (e[2] > maxW) maxW = e[2];
    }
    int low = 0;
    int high = maxW * 2;

    while (low < high) {
      int mid = (low + high + 1) >> 1;
      if (_can(n, edges, k, mid)) {
        low = mid;
      } else {
        high = mid - 1;
      }
    }

    return _can(n, edges, k, low) ? low : -1;
  }
}
```

## Golang

```go
package main

type Edge struct {
	u, v int
	s    int
	must int
}

type DSU struct {
	parent []int
	size   []int
	comp   int
}

func NewDSU(n int) *DSU {
	p := make([]int, n)
	sz := make([]int, n)
	for i := 0; i < n; i++ {
		p[i] = i
		sz[i] = 1
	}
	return &DSU{parent: p, size: sz, comp: n}
}

func (d *DSU) Find(x int) int {
	if d.parent[x] != x {
		d.parent[x] = d.Find(d.parent[x])
	}
	return d.parent[x]
}

func (d *DSU) Union(a, b int) bool {
	ra := d.Find(a)
	rb := d.Find(b)
	if ra == rb {
		return false
	}
	if d.size[ra] < d.size[rb] {
		ra, rb = rb, ra
	}
	d.parent[rb] = ra
	d.size[ra] += d.size[rb]
	d.comp--
	return true
}

func maxStability(n int, edges [][]int, k int) int {
	elist := make([]Edge, len(edges))
	maxS := 0
	for i, e := range edges {
		u, v, s, must := e[0], e[1], e[2], e[3]
		elist[i] = Edge{u: u, v: v, s: s, must: must}
		if s > maxS {
			maxS = s
		}
	}

	// Check basic connectivity ignoring thresholds
	base := NewDSU(n)
	for _, e := range elist {
		base.Union(e.u, e.v)
	}
	if base.comp != 1 {
		return -1
	}

	feasible := func(th int) bool {
		ds := NewDSU(n)

		// must=1 edges that already satisfy threshold
		for _, e := range elist {
			if e.must == 1 && e.s >= th {
				ds.Union(e.u, e.v)
			}
		}
		// upgradeable edges usable without upgrade
		for _, e := range elist {
			if e.must == 0 && e.s >= th {
				ds.Union(e.u, e.v)
			}
		}

		upUsed := 0
		// upgradeable edges that need an upgrade
		for _, e := range elist {
			if e.must == 0 && e.s < th && e.s*2 >= th {
				if ds.Find(e.u) != ds.Find(e.v) {
					ds.Union(e.u, e.v)
					upUsed++
					if upUsed > k {
						return false
					}
				}
			}
		}
		return ds.comp == 1 && upUsed <= k
	}

	lo, hi := 1, maxS*2
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if feasible(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
```

## Ruby

```ruby
class DSU
  def initialize(n)
    @parent = Array.new(n) { |i| i }
    @size = Array.new(n, 1)
    @components = n
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
    return false if ra == rb
    if @size[ra] < @size[rb]
      ra, rb = rb, ra
    end
    @parent[rb] = ra
    @size[ra] += @size[rb]
    @components -= 1
    true
  end

  def components
    @components
  end
end

def max_stability(n, edges, k)
  # check overall connectivity ignoring weights
  dsu_all = DSU.new(n)
  edges.each do |u, v, s, must|
    dsu_all.union(u, v)
  end
  return -1 if dsu_all.components != 1

  max_possible = 0
  edges.each do |_, _, s, must|
    cur = must == 0 ? s * 2 : s
    max_possible = cur if cur > max_possible
  end

  # feasibility check for a given threshold
  feasible = lambda do |thr|
    dsu = DSU.new(n)
    # first use edges that already satisfy without upgrade
    edges.each do |u, v, s, must|
      if s >= thr
        dsu.union(u, v)
      end
    end
    used = 0
    edges.each do |u, v, s, must|
      next if s >= thr # already considered
      next unless must == 0 && s * 2 >= thr
      if dsu.union(u, v)
        used += 1
        return false if used > k
      end
    end
    dsu.components == 1 && used <= k
  end

  low = 0
  high = max_possible
  while low < high
    mid = (low + high + 1) / 2
    if feasible.call(mid)
      low = mid
    else
      high = mid - 1
    end
  end
  low
end
```

## Scala

```scala
object Solution {
  def maxStability(n: Int, edges: Array[Array[Int]], k: Int): Int = {
    case class Edge(u: Int, v: Int, s: Int, must: Boolean)

    val mustEdges = scala.collection.mutable.ArrayBuffer.empty[Edge]
    val optionalEdges = scala.collection.mutable.ArrayBuffer.empty[Edge]

    var maxS = 0
    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      val s = e(2)
      val must = e(3) == 1
      maxS = math.max(maxS, s)
      if (must) mustEdges += Edge(u, v, s, must = true)
      else optionalEdges += Edge(u, v, s, must = false)
    }

    class DSU(val n: Int) {
      private val parent = Array.tabulate(n)(i => i)
      private val size = Array.fill(n)(1)
      var components: Int = n

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
        if (size(x) < size(y)) { val tmp = x; x = y; y = tmp }
        parent(y) = x
        size(x) += size(y)
        components -= 1
        true
      }
    }

    def feasible(threshold: Int): Boolean = {
      val dsu = new DSU(n)
      var usedEdges = 0

      // process mandatory edges
      for (e <- mustEdges) {
        if (e.s < threshold) return false          // cannot satisfy threshold
        if (!dsu.union(e.u, e.v)) return false     // creates a cycle
        usedEdges += 1
      }

      val free = scala.collection.mutable.ArrayBuffer.empty[Edge]
      val upg = scala.collection.mutable.ArrayBuffer.empty[Edge]

      for (e <- optionalEdges) {
        if (e.s >= threshold) free += e
        else if (e.s * 2 >= threshold) upg += e
      }

      // use free edges first
      for (e <- free) {
        if (dsu.union(e.u, e.v)) usedEdges += 1
      }

      var upgradesUsed = 0
      for (e <- upg) {
        if (usedEdges == n - 1) return true
        if (dsu.union(e.u, e.v)) {
          upgradesUsed += 1
          if (upgradesUsed > k) return false
          usedEdges += 1
        }
      }

      dsu.components == 1 && usedEdges == n - 1 && upgradesUsed <= k
    }

    var low = 0
    var high = maxS * 2
    while (low < high) {
      val mid = (low + high + 1) >>> 1
      if (feasible(mid)) low = mid else high = mid - 1
    }
    if (feasible(low)) low else -1
  }
}
```

## Rust

```rust
use std::cmp::max;

struct DSU {
    parent: Vec<usize>,
    size: Vec<usize>,
    components: usize,
}

impl DSU {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(i);
        }
        DSU {
            parent,
            size: vec![1; n],
            components: n,
        }
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
        if self.size[ra] < self.size[rb] {
            std::mem::swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        self.size[ra] += self.size[rb];
        self.components -= 1;
        true
    }
}

impl Solution {
    pub fn max_stability(n: i32, edges: Vec<Vec<i32>>, k: i32) -> i32 {
        let n_usize = n as usize;
        let mut edge_list: Vec<(usize, usize, i64, i32)> = Vec::with_capacity(edges.len());
        let mut max_s: i64 = 0;
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let s = e[2] as i64;
            let must = e[3];
            max_s = max(max_s, s);
            edge_list.push((u, v, s, must));
        }

        fn feasible(
            x: i64,
            n: usize,
            k: i32,
            edges: &Vec<(usize, usize, i64, i32)>,
        ) -> bool {
            let mut dsu = DSU::new(n);
            // mandatory edges
            for &(u, v, s, must) in edges.iter() {
                if must == 1 {
                    if s < x {
                        return false;
                    }
                    if !dsu.union(u, v) {
                        return false; // cycle among mandatory edges
                    }
                }
            }
            // optional edges without upgrade
            for &(u, v, s, must) in edges.iter() {
                if must == 0 && s >= x {
                    dsu.union(u, v);
                }
            }
            let mut upgrades_left = k;
            // optional edges that need upgrade
            for &(u, v, s, must) in edges.iter() {
                if upgrades_left == 0 {
                    break;
                }
                if must == 0 && s < x && s * 2 >= x {
                    if dsu.find(u) != dsu.find(v) {
                        dsu.union(u, v);
                        upgrades_left -= 1;
                    }
                }
            }
            dsu.components == 1
        }

        let mut lo: i64 = 0;
        let mut hi: i64 = max_s * 2;
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if feasible(mid, n_usize, k, &edge_list) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }

        if lo >= 1 && feasible(lo, n_usize, k, &edge_list) {
            lo as i32
        } else {
            -1
        }
    }
}
```

## Racket

```racket
(define (make-dsu n)
  (let ([parent (make-vector n)]
        [size   (make-vector n 1)])
    (for ([i (in-range n)]) (vector-set! parent i i))
    (list parent size)))

(define (find dsu x)
  (let* ([parent (first dsu)])
    (let loop ([v x])
      (let ([p (vector-ref parent v)])
        (if (= p v)
            v
            (let ([root (loop p)])
              (vector-set! parent v root)
              root))))))

(define (union dsu a b)
  (let* ([parent (first dsu)]
         [size   (second dsu)]
         [ra (find dsu a)]
         [rb (find dsu b)])
    (if (= ra rb) #f
        (begin
          (when (< (vector-ref size ra) (vector-ref size rb))
            (let ([tmp ra])
              (set! ra rb)
              (set! rb tmp)))
          (vector-set! parent rb ra)
          (vector-set! size ra (+ (vector-ref size ra) (vector-ref size rb)))
          #t))))

(define (can? T n edges k)
  (let* ([dsu (make-dsu n)]
         [comps n])
    ;; use edges that already satisfy threshold
    (for ([e edges])
      (let* ([u (list-ref e 0)] [v (list-ref e 1)]
             [s (list-ref e 2)])
        (when (>= s T)
          (when (union dsu u v) (set! comps (- comps 1))))))
    ;; use edges that need one upgrade
    (define upgrades 0)
    (for ([e edges])
      (let* ([u (list-ref e 0)] [v (list-ref e 1)]
             [s (list-ref e 2)] [must (list-ref e 3)])
        (when (and (= must 0) (< s T) (>= (* 2 s) T))
          (when (union dsu u v)
            (set! upgrades (+ upgrades 1))
            (set! comps (- comps 1))))))
    (and (= comps 1) (<= upgrades k))))

(define (max-stability n edges k)
  ;; check overall connectivity
  (let* ([dsu0 (make-dsu n)])
    (for ([e edges])
      (union dsu0 (list-ref e 0) (list-ref e 1)))
    (define connected?
      (let loop ((i 0) (cnt 0))
        (if (= i n) (= cnt 1)
            (let* ([parent (first dsu0)]
                   [root (find dsu0 i)])
              (loop (+ i 1) (if (= root i) (+ cnt 1) cnt))))))
    (if (not connected?) -1
        (let* ([max-w
                (apply max
                       (map (lambda (e)
                              (let* ([s (list-ref e 2)]
                                     [must (list-ref e 3)])
                                (if (= must 0) (* 2 s) s)))
                            edges))])
          (define (search lo hi)
            (if (> lo hi) lo
                (let ([mid (quotient (+ lo hi 1) 2)])
                  (if (can? mid n edges k)
                      (search mid hi)
                      (search lo (- mid 1))))))
          (search 0 max-w)))))
```

## Erlang

```erlang
-module(solution).
-export([max_stability/3]).

%% Public API
-spec max_stability(N :: integer(), Edges :: [[integer()]], K :: integer()) -> integer().
max_stability(N, EdgeLists, K) ->
    %% Convert edge lists to tuples for easier handling
    Edges = [begin [U,V,S,M]=E, {U,V,S,M} end || E <- EdgeLists],
    MaxStrength = lists:max([S*2 || {_U,_V,S,_M} <- Edges]),
    Low0 = 0,
    High0 = MaxStrength + 1,
    {AnsLow, _} = binary_search(Low0, High0, N, Edges, K),
    case AnsLow of
        0 -> -1;
        _ -> AnsLow
    end.

%% Binary search for the maximum feasible stability value
binary_search(Low, High, N, Edges, K) when Low + 1 < High ->
    Mid = (Low + High) div 2,
    case feasible(Mid, N, Edges, K) of
        true -> binary_search(Mid, High, N, Edges, K);
        false -> binary_search(Low, Mid, N, Edges, K)
    end;
binary_search(Low, High, _N, _Edges, _K) ->
    {Low, High}.

%% Check if a given threshold T can be achieved with at most K upgrades
feasible(T, N, Edges, K) ->
    Parent0 = array:from_list(lists:seq(0, N-1)),
    %% Union all edges that already satisfy the threshold without upgrade
    ParentFree = lists:foldl(
        fun({U,V,S,_M}, Par) ->
            if S >= T -> union(Par, U, V);
               true   -> Par
            end
        end,
        Parent0,
        Edges),
    %% Process edges that can satisfy the threshold after one upgrade
    {ParentAll, UpUsed} = lists:foldl(
        fun({U,V,S,M}, {Par, Used}) ->
            if M == 0 andalso S < T andalso S*2 >= T ->
                    {RU, Par1} = find(Par, U),
                    {RV, Par2} = find(Par1, V),
                    if RU =:= RV -> {Par2, Used};
                       true       -> {array:set(RU, RV, Par2), Used + 1}
                    end;
               true -> {Par, Used}
            end
        end,
        {ParentFree, 0},
        Edges),
    UpUsed =< K andalso connected(ParentAll, N).

%% Verify that the DSU represents a single connected component
connected(Par, N) ->
    {Root0, Par0} = find(Par, 0),
    lists:all(
        fun(I) ->
            {R, _} = find(Par0, I),
            R =:= Root0
        end,
        lists:seq(1, N-1)).

%% Find with path compression
find(Par, X) ->
    case array:get(X, Par) of
        X -> {X, Par};
        P ->
            {Root, Par1} = find(Par, P),
            NewPar = array:set(X, Root, Par1),
            {Root, NewPar}
    end.

%% Union without rank (sufficient for this problem)
union(Par, X, Y) ->
    {RX, Par1} = find(Par, X),
    {RY, Par2} = find(Par1, Y),
    if RX =:= RY -> Par2;
       true      -> array:set(RX, RY, Par2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_stability(n :: integer, edges :: [[integer]], k :: integer) :: integer
  def max_stability(n, edges, k) do
    edge_tuples = Enum.map(edges, fn [u, v, s, m] -> {u, v, s, m} end)
    max_s = Enum.max_by(edge_tuples, fn {_u, _v, s, _m} -> s end) |> elem(2)
    high = max_s * 2

    ans = binary_search(0, high, n, edge_tuples, k)

    if feasible?(ans, n, edge_tuples, k), do: ans, else: -1
  end

  defp binary_search(low, high, n, edges, k) when low < high do
    mid = div(low + high + 1, 2)

    if feasible?(mid, n, edges, k) do
      binary_search(mid, high, n, edges, k)
    else
      binary_search(low, mid - 1, n, edges, k)
    end
  end

  defp binary_search(low, _high, _n, _edges, _k), do: low

  defp feasible?(threshold, n, edges, k) do
    tid = :ets.new(:uf, [:set, :private])

    Enum.each(0..(n - 1), fn i -> :ets.insert(tid, {i, {i, 1}}) end)

    components = n

    # use edges that already satisfy the threshold without upgrade
    {components, _} =
      Enum.reduce(edges, {components, nil}, fn {u, v, s, must}, {comp, _} ->
        cond do
          (must == 1 and s >= threshold) or (must == 0 and s >= threshold) ->
            if union(tid, u, v), do: {comp - 1, nil}, else: {comp, nil}
          true ->
            {comp, nil}
        end
      end)

    # edges that can satisfy after one upgrade
    upgrade_edges =
      Enum.filter(edges, fn {_u, _v, s, must} ->
        must == 0 and s < threshold and s * 2 >= threshold
      end)

    upgrades_used = 0

    {components, upgrades_used} =
      Enum.reduce_while(upgrade_edges, {components, upgrades_used}, fn {u, v, _s, _m},
                                                                      {comp, used} ->
        if comp == 1 do
          {:halt, {comp, used}}
        else
          if union(tid, u, v) do
            new_used = used + 1

            if new_used > k do
              {:halt, {comp, new_used}}
            else
              {:cont, {comp - 1, new_used}}
            end
          else
            {:cont, {comp, used}}
          end
        end
      end)

    :ets.delete(tid)
    components == 1 and upgrades_used <= k
  end

  defp find(tid, x) do
    case :ets.lookup(tid, x) do
      [{^x, {parent, size}}] ->
        if parent == x do
          {x, size}
        else
          {root, _} = find(tid, parent)
          :ets.insert(tid, {x, {root, size}})
          {root, size}
        end

      [] ->
        raise "node not found"
    end
  end

  defp union(tid, a, b) do
    {ra, sa} = find(tid, a)
    {rb, sb} = find(tid, b)

    if ra == rb do
      false
    else
      if sa < sb do
        :ets.insert(tid, {ra, {rb, sa}})
        :ets.insert(tid, {rb, {rb, sb + sa}})
      else
        :ets.insert(tid, {rb, {ra, sb}})
        :ets.insert(tid, {ra, {ra, sa + sb}})
      end

      true
    end
  end
end
```

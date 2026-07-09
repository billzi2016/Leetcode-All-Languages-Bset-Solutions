# 1579. Remove Max Number of Edges to Keep Graph Fully Traversable

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
            return parent[x] == x ? x : parent[x] = find(parent[x]);
        }
        bool unite(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return false;
            if (rank[a] < rank[b]) swap(a, b);
            parent[b] = a;
            if (rank[a] == rank[b]) ++rank[a];
            --cnt;
            return true;
        }
        int components() const { return cnt; }
    };
    
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        DSU alice(n), bob(n);
        int used = 0;
        // type 3 edges first
        for (auto &e : edges) if (e[0] == 3) {
            bool mergedA = alice.unite(e[1] - 1, e[2] - 1);
            bool mergedB = bob.unite(e[1] - 1, e[2] - 1);
            if (mergedA || mergedB) ++used;
        }
        // type 1 edges for Alice
        for (auto &e : edges) if (e[0] == 1) {
            if (alice.unite(e[1] - 1, e[2] - 1)) ++used;
        }
        // type 2 edges for Bob
        for (auto &e : edges) if (e[0] == 2) {
            if (bob.unite(e[1] - 1, e[2] - 1)) ++used;
        }
        if (alice.components() != 1 || bob.components() != 1) return -1;
        return (int)edges.size() - used;
    }
};
```

## Java

```java
class Solution {
    private static class DSU {
        int[] parent;
        int[] rank;
        int components;

        DSU(int n) {
            parent = new int[n + 1];
            rank = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
            components = n;
        }

        int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        boolean union(int a, int b) {
            int pa = find(a);
            int pb = find(b);
            if (pa == pb) return false;
            if (rank[pa] < rank[pb]) {
                parent[pa] = pb;
            } else if (rank[pa] > rank[pb]) {
                parent[pb] = pa;
            } else {
                parent[pb] = pa;
                rank[pa]++;
            }
            components--;
            return true;
        }
    }

    public int maxNumEdgesToRemove(int n, int[][] edges) {
        DSU alice = new DSU(n);
        DSU bob = new DSU(n);
        int used = 0;

        // Type 3 edges first
        for (int[] e : edges) {
            if (e[0] == 3) {
                boolean mergedAlice = alice.union(e[1], e[2]);
                boolean mergedBob = bob.union(e[1], e[2]);
                if (mergedAlice || mergedBob) {
                    used++;
                }
            }
        }

        // Type 1 for Alice
        for (int[] e : edges) {
            if (e[0] == 1) {
                if (alice.union(e[1], e[2])) {
                    used++;
                }
            }
        }

        // Type 2 for Bob
        for (int[] e : edges) {
            if (e[0] == 2) {
                if (bob.union(e[1], e[2])) {
                    used++;
                }
            }
        }

        if (alice.components != 1 || bob.components != 1) {
            return -1;
        }
        return edges.length - used;
    }
}
```

## Python

```python
class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        class DSU:
            __slots__ = ('parent', 'rank', 'components')
            def __init__(self, size):
                self.parent = list(range(size + 1))
                self.rank = [0] * (size + 1)
                self.components = size

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
                self.components -= 1
                return True

        dsu_alice = DSU(n)
        dsu_bob = DSU(n)
        used = 0

        # Type 3 edges first (shared)
        for t, u, v in edges:
            if t == 3:
                merged = dsu_alice.union(u, v)
                if merged:
                    used += 1
                    dsu_bob.union(u, v)

        # Type 1 edges (Alice only)
        for t, u, v in edges:
            if t == 1:
                if dsu_alice.union(u, v):
                    used += 1

        # Type 2 edges (Bob only)
        for t, u, v in edges:
            if t == 2:
                if dsu_bob.union(u, v):
                    used += 1

        if dsu_alice.components != 1 or dsu_bob.components != 1:
            return -1
        return len(edges) - used
```

## Python3

```python
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges):
        class DSU:
            __slots__ = ("parent", "rank", "components")
            def __init__(self, size):
                self.parent = list(range(size + 1))
                self.rank = [0] * (size + 1)
                self.components = size
            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x
            def union(self, a, b):
                ra, rb = self.find(a), self.find(b)
                if ra == rb:
                    return False
                if self.rank[ra] < self.rank[rb]:
                    ra, rb = rb, ra
                self.parent[rb] = ra
                if self.rank[ra] == self.rank[rb]:
                    self.rank[ra] += 1
                self.components -= 1
                return True

        dsu_alice = DSU(n)
        dsu_bob = DSU(n)

        used = 0

        # type 3 edges first
        for t, u, v in edges:
            if t == 3:
                merged_a = dsu_alice.union(u, v)
                merged_b = dsu_bob.union(u, v)
                if merged_a or merged_b:   # at least one union actually added new connection
                    used += 1

        # type 1 for Alice
        for t, u, v in edges:
            if t == 1:
                if dsu_alice.union(u, v):
                    used += 1

        # type 2 for Bob
        for t, u, v in edges:
            if t == 2:
                if dsu_bob.union(u, v):
                    used += 1

        if dsu_alice.components != 1 or dsu_bob.components != 1:
            return -1

        return len(edges) - used
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int *parent;
    int *rank;
    int components;
} DSU;

static int dsu_find(DSU *d, int x) {
    if (d->parent[x] != x)
        d->parent[x] = dsu_find(d, d->parent[x]);
    return d->parent[x];
}

static bool dsu_union(DSU *d, int a, int b) {
    int ra = dsu_find(d, a);
    int rb = dsu_find(d, b);
    if (ra == rb) return false;
    if (d->rank[ra] < d->rank[rb]) {
        d->parent[ra] = rb;
    } else if (d->rank[ra] > d->rank[rb]) {
        d->parent[rb] = ra;
    } else {
        d->parent[rb] = ra;
        d->rank[ra]++;
    }
    d->components--;
    return true;
}

int maxNumEdgesToRemove(int n, int** edges, int edgesSize, int* edgesColSize){
    DSU alice, bob;
    alice.parent = (int*)malloc((n + 1) * sizeof(int));
    bob.parent   = (int*)malloc((n + 1) * sizeof(int));
    alice.rank = (int*)calloc(n + 1, sizeof(int));
    bob.rank   = (int*)calloc(n + 1, sizeof(int));
    for (int i = 1; i <= n; ++i) {
        alice.parent[i] = i;
        bob.parent[i] = i;
    }
    alice.components = n;
    bob.components = n;

    int used = 0;

    // Type 3 edges first
    for (int i = 0; i < edgesSize; ++i) {
        if (edges[i][0] == 3) {
            bool mergedA = dsu_union(&alice, edges[i][1], edges[i][2]);
            bool mergedB = dsu_union(&bob,   edges[i][1], edges[i][2]);
            if (mergedA || mergedB) used++;
        }
    }

    // Type 1 edges for Alice
    for (int i = 0; i < edgesSize; ++i) {
        if (edges[i][0] == 1) {
            if (dsu_union(&alice, edges[i][1], edges[i][2])) used++;
        }
    }

    // Type 2 edges for Bob
    for (int i = 0; i < edgesSize; ++i) {
        if (edges[i][0] == 2) {
            if (dsu_union(&bob, edges[i][1], edges[i][2])) used++;
        }
    }

    int result;
    if (alice.components != 1 || bob.components != 1) {
        result = -1;
    } else {
        result = edgesSize - used;
    }

    free(alice.parent);
    free(bob.parent);
    free(alice.rank);
    free(bob.rank);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxNumEdgesToRemove(int n, int[][] edges) {
        DSU alice = new DSU(n);
        DSU bob = new DSU(n);
        int used = 0;

        // Type 3 edges first
        foreach (var e in edges) {
            if (e[0] == 3) {
                bool merged = alice.Union(e[1], e[2]);
                bob.Union(e[1], e[2]); // result is the same as alice's at this point
                if (merged) used++;
            }
        }

        // Type 1 edges for Alice
        foreach (var e in edges) {
            if (e[0] == 1) {
                if (alice.Union(e[1], e[2])) used++;
            }
        }

        // Type 2 edges for Bob
        foreach (var e in edges) {
            if (e[0] == 2) {
                if (bob.Union(e[1], e[2])) used++;
            }
        }

        if (alice.Components != 1 || bob.Components != 1) return -1;
        return edges.Length - used;
    }

    private class DSU {
        private readonly int[] parent;
        private readonly int[] rank;
        public int Components { get; private set; }

        public DSU(int size) {
            parent = new int[size + 1];
            rank = new int[size + 1];
            for (int i = 1; i <= size; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
            Components = size;
        }

        public int Find(int x) {
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }

        public bool Union(int x, int y) {
            int rx = Find(x);
            int ry = Find(y);
            if (rx == ry) return false;
            if (rank[rx] < rank[ry]) {
                parent[rx] = ry;
            } else if (rank[rx] > rank[ry]) {
                parent[ry] = rx;
            } else {
                parent[ry] = rx;
                rank[rx]++;
            }
            Components--;
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
 * @return {number}
 */
var maxNumEdgesToRemove = function(n, edges) {
    class DSU {
        constructor(size) {
            this.parent = new Array(size + 1);
            this.rank = new Array(size + 1).fill(0);
            for (let i = 1; i <= size; i++) this.parent[i] = i;
        }
        find(x) {
            if (this.parent[x] !== x) {
                this.parent[x] = this.find(this.parent[x]);
            }
            return this.parent[x];
        }
        union(a, b) {
            let pa = this.find(a);
            let pb = this.find(b);
            if (pa === pb) return false;
            if (this.rank[pa] < this.rank[pb]) {
                [pa, pb] = [pb, pa];
            }
            this.parent[pb] = pa;
            if (this.rank[pa] === this.rank[pb]) this.rank[pa]++;
            return true;
        }
    }

    const dsuA = new DSU(n);
    const dsuB = new DSU(n);
    let used = 0;
    let cntA = 0, cntB = 0;

    // Type 3 edges first
    for (const [type, u, v] of edges) {
        if (type !== 3) continue;
        const mergedA = dsuA.union(u, v);
        const mergedB = dsuB.union(u, v);
        if (mergedA || mergedB) used++;
        if (mergedA) cntA++;
        if (mergedB) cntB++;
    }

    // Type 1 edges for Alice
    for (const [type, u, v] of edges) {
        if (type !== 1) continue;
        if (dsuA.union(u, v)) {
            used++;
            cntA++;
        }
    }

    // Type 2 edges for Bob
    for (const [type, u, v] of edges) {
        if (type !== 2) continue;
        if (dsuB.union(u, v)) {
            used++;
            cntB++;
        }
    }

    if (cntA !== n - 1 || cntB !== n - 1) return -1;

    return edges.length - used;
};
```

## Typescript

```typescript
class DSU {
    parent: number[];
    rank: number[];
    components: number;
    constructor(n: number) {
        this.parent = new Array(n + 1);
        this.rank = new Array(n + 1).fill(0);
        for (let i = 1; i <= n; i++) this.parent[i] = i;
        this.components = n;
    }
    find(x: number): number {
        if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);
        return this.parent[x];
    }
    union(a: number, b: number): boolean {
        a = this.find(a);
        b = this.find(b);
        if (a === b) return false;
        if (this.rank[a] < this.rank[b]) [a, b] = [b, a];
        this.parent[b] = a;
        if (this.rank[a] === this.rank[b]) this.rank[a]++;
        this.components--;
        return true;
    }
}

function maxNumEdgesToRemove(n: number, edges: number[][]): number {
    const dsuA = new DSU(n);
    const dsuB = new DSU(n);
    let used = 0;

    // Type 3 edges first
    for (const [type, u, v] of edges) {
        if (type === 3) {
            const mergedA = dsuA.union(u, v);
            const mergedB = dsuB.union(u, v);
            if (mergedA || mergedB) used++;
        }
    }

    // Type 1 edges for Alice
    for (const [type, u, v] of edges) {
        if (type === 1 && dsuA.union(u, v)) used++;
    }

    // Type 2 edges for Bob
    for (const [type, u, v] of edges) {
        if (type === 2 && dsuB.union(u, v)) used++;
    }

    if (dsuA.components !== 1 || dsuB.components !== 1) return -1;
    return edges.length - used;
}
```

## Php

```php
class DSU {
    public array $parent;
    public array $rank;
    public int $count;

    public function __construct(int $n) {
        // parent[0] unused to align indices with node numbers
        $this->parent = range(0, $n);
        $this->rank = array_fill(0, $n + 1, 0);
        $this->count = $n;
    }

    public function find(int $x): int {
        $root = $x;
        while ($this->parent[$root] !== $root) {
            $root = $this->parent[$root];
        }
        // Path compression
        while ($this->parent[$x] !== $x) {
            $parent = $this->parent[$x];
            $this->parent[$x] = $root;
            $x = $parent;
        }
        return $root;
    }

    public function union(int $x, int $y): bool {
        $rx = $this->find($x);
        $ry = $this->find($y);
        if ($rx === $ry) {
            return false;
        }
        // Union by rank
        if ($this->rank[$rx] < $this->rank[$ry]) {
            $this->parent[$rx] = $ry;
        } elseif ($this->rank[$rx] > $this->rank[$ry]) {
            $this->parent[$ry] = $rx;
        } else {
            $this->parent[$ry] = $rx;
            $this->rank[$rx]++;
        }
        $this->count--;
        return true;
    }

    public function getCount(): int {
        return $this->count;
    }
}

class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer
     */
    function maxNumEdgesToRemove($n, $edges) {
        $alice = new DSU($n);
        $bob   = new DSU($n);
        $used  = 0;

        // Type 3 edges first (usable by both)
        foreach ($edges as $e) {
            if ($e[0] === 3) {
                if ($alice->union($e[1], $e[2])) {
                    $bob->union($e[1], $e[2]);
                    $used++;
                }
            }
        }

        // Type 1 edges (Alice only)
        foreach ($edges as $e) {
            if ($e[0] === 1) {
                if ($alice->union($e[1], $e[2])) {
                    $used++;
                }
            }
        }

        // Type 2 edges (Bob only)
        foreach ($edges as $e) {
            if ($e[0] === 2) {
                if ($bob->union($e[1], $e[2])) {
                    $used++;
                }
            }
        }

        // Check connectivity for both Alice and Bob
        if ($alice->getCount() !== 1 || $bob->getCount() !== 1) {
            return -1;
        }

        return count($edges) - $used;
    }
}
```

## Swift

```swift
import Foundation

class DSU {
    private var parent: [Int]
    private var size: [Int]

    init(_ n: Int) {
        parent = Array(0..<n)
        size = Array(repeating: 1, count: n)
    }

    func find(_ x: Int) -> Int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    @discardableResult
    func union(_ x: Int, _ y: Int) -> Bool {
        var rootX = find(x)
        var rootY = find(y)
        if rootX == rootY { return false }
        if size[rootX] < size[rootY] {
            swap(&rootX, &rootY)
        }
        parent[rootY] = rootX
        size[rootX] += size[rootY]
        return true
    }

    func isFullyConnected() -> Bool {
        let root = find(0)
        for i in 1..<parent.count {
            if find(i) != root { return false }
        }
        return true
    }
}

class Solution {
    func maxNumEdgesToRemove(_ n: Int, _ edges: [[Int]]) -> Int {
        var used = 0
        let aliceDSU = DSU(n)
        let bobDSU = DSU(n)

        // Type 3 edges (usable by both)
        for e in edges where e[0] == 3 {
            let u = e[1] - 1
            let v = e[2] - 1
            if aliceDSU.union(u, v) {
                bobDSU.union(u, v)
                used += 1
            }
        }

        // Type 1 edges (Alice only)
        for e in edges where e[0] == 1 {
            let u = e[1] - 1
            let v = e[2] - 1
            if aliceDSU.union(u, v) {
                used += 1
            }
        }

        // Type 2 edges (Bob only)
        for e in edges where e[0] == 2 {
            let u = e[1] - 1
            let v = e[2] - 1
            if bobDSU.union(u, v) {
                used += 1
            }
        }

        // Verify both can traverse the whole graph
        if !aliceDSU.isFullyConnected() || !bobDSU.isFullyConnected() {
            return -1
        }

        return edges.count - used
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class DSU(n: Int) {
        private val parent = IntArray(n + 1) { it }
        private val rank = IntArray(n + 1)
        var count = n
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
            var pa = find(a)
            var pb = find(b)
            if (pa == pb) return false
            if (rank[pa] < rank[pb]) {
                parent[pa] = pb
            } else if (rank[pa] > rank[pb]) {
                parent[pb] = pa
            } else {
                parent[pb] = pa
                rank[pa]++
            }
            count--
            return true
        }
    }

    fun maxNumEdgesToRemove(n: Int, edges: Array<IntArray>): Int {
        val dsuA = DSU(n)
        val dsuB = DSU(n)
        var used = 0

        // Type 3 edges first (usable by both)
        for (e in edges) {
            if (e[0] == 3) {
                val u = e[1]
                val v = e[2]
                val mergedA = dsuA.union(u, v)
                val mergedB = dsuB.union(u, v)
                if (mergedA || mergedB) used++
            }
        }

        // Type 1 edges (Alice only)
        for (e in edges) {
            if (e[0] == 1) {
                val u = e[1]
                val v = e[2]
                if (dsuA.union(u, v)) used++
            }
        }

        // Type 2 edges (Bob only)
        for (e in edges) {
            if (e[0] == 2) {
                val u = e[1]
                val v = e[2]
                if (dsuB.union(u, v)) used++
            }
        }

        return if (dsuA.count != 1 || dsuB.count != 1) -1 else edges.size - used
    }
}
```

## Dart

```dart
class DSU {
  List<int> parent;
  List<int> rank;
  int components;

  DSU(int n)
      : parent = List.generate(n, (i) => i),
        rank = List.filled(n, 0),
        components = n;

  int find(int x) {
    if (parent[x] != x) {
      parent[x] = find(parent[x]);
    }
    return parent[x];
  }

  bool union(int x, int y) {
    int rx = find(x);
    int ry = find(y);
    if (rx == ry) return false;
    if (rank[rx] < rank[ry]) {
      parent[rx] = ry;
    } else if (rank[rx] > rank[ry]) {
      parent[ry] = rx;
    } else {
      parent[ry] = rx;
      rank[rx]++;
    }
    components--;
    return true;
  }
}

class Solution {
  int maxNumEdgesToRemove(int n, List<List<int>> edges) {
    DSU alice = DSU(n);
    DSU bob = DSU(n);
    int removed = 0;

    // Type 3 edges first
    for (var e in edges) {
      if (e[0] == 3) {
        int u = e[1] - 1;
        int v = e[2] - 1;
        bool mergedAlice = alice.union(u, v);
        bool mergedBob = bob.union(u, v);
        if (!mergedAlice && !mergedBob) {
          removed++;
        }
      }
    }

    // Type 1 edges (Alice only)
    for (var e in edges) {
      if (e[0] == 1) {
        int u = e[1] - 1;
        int v = e[2] - 1;
        if (!alice.union(u, v)) {
          removed++;
        }
      }
    }

    // Type 2 edges (Bob only)
    for (var e in edges) {
      if (e[0] == 2) {
        int u = e[1] - 1;
        int v = e[2] - 1;
        if (!bob.union(u, v)) {
          removed++;
        }
      }
    }

    if (alice.components != 1 || bob.components != 1) {
      return -1;
    }
    return removed;
  }
}
```

## Golang

```go
type dsu struct {
	parent []int
	size   []int
}

func newDSU(n int) *dsu {
	p := make([]int, n+1)
	s := make([]int, n+1)
	for i := 1; i <= n; i++ {
		p[i] = i
		s[i] = 1
	}
	return &dsu{parent: p, size: s}
}

func (d *dsu) find(x int) int {
	if d.parent[x] != x {
		d.parent[x] = d.find(d.parent[x])
	}
	return d.parent[x]
}

// returns true if a merge happened
func (d *dsu) union(a, b int) bool {
	ra := d.find(a)
	rb := d.find(b)
	if ra == rb {
		return false
	}
	if d.size[ra] < d.size[rb] {
		ra, rb = rb, ra
	}
	d.parent[rb] = ra
	d.size[ra] += d.size[rb]
	return true
}

func maxNumEdgesToRemove(n int, edges [][]int) int {
	alice := newDSU(n)
	bob := newDSU(n)
	used := 0

	// type 3 edges first
	for _, e := range edges {
		if e[0] == 3 {
			if alice.union(e[1], e[2]) {
				bob.union(e[1], e[2])
				used++
			}
		}
	}

	// type 1 for Alice
	for _, e := range edges {
		if e[0] == 1 {
			if alice.union(e[1], e[2]) {
				used++
			}
		}
	}

	// type 2 for Bob
	for _, e := range edges {
		if e[0] == 2 {
			if bob.union(e[1], e[2]) {
				used++
			}
		}
	}

	// check full connectivity for both
	rootA := alice.find(1)
	rootB := bob.find(1)
	for i := 2; i <= n; i++ {
		if alice.find(i) != rootA || bob.find(i) != rootB {
			return -1
		}
	}

	return len(edges) - used
}
```

## Ruby

```ruby
class DSU
  def initialize(n)
    @parent = Array.new(n + 1) { |i| i }
    @rank = Array.new(n + 1, 0)
  end

  def find(x)
    while @parent[x] != x
      @parent[x] = @parent[@parent[x]]
      x = @parent[x]
    end
    x
  end

  def union(x, y)
    rx = find(x)
    ry = find(y)
    return false if rx == ry
    if @rank[rx] < @rank[ry]
      @parent[rx] = ry
    elsif @rank[rx] > @rank[ry]
      @parent[ry] = rx
    else
      @parent[ry] = rx
      @rank[rx] += 1
    end
    true
  end
end

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def max_num_edges_to_remove(n, edges)
  dsu_a = DSU.new(n)
  dsu_b = DSU.new(n)

  need_a = n - 1
  need_b = n - 1
  used = 0

  type3 = []
  type1 = []
  type2 = []

  edges.each do |e|
    t, u, v = e
    case t
    when 3
      type3 << [u, v]
    when 1
      type1 << [u, v]
    else # t == 2
      type2 << [u, v]
    end
  end

  type3.each do |u, v|
    merged_a = dsu_a.union(u, v)
    merged_b = dsu_b.union(u, v)
    if merged_a || merged_b
      used += 1
      need_a -= 1 if merged_a
      need_b -= 1 if merged_b
    end
  end

  type1.each do |u, v|
    if dsu_a.union(u, v)
      used += 1
      need_a -= 1
    end
  end

  type2.each do |u, v|
    if dsu_b.union(u, v)
      used += 1
      need_b -= 1
    end
  end

  return -1 unless need_a.zero? && need_b.zero?
  edges.length - used
end
```

## Scala

```scala
object Solution {
  def maxNumEdgesToRemove(n: Int, edges: Array[Array[Int]]): Int = {
    class DSU(size: Int) {
      private val parent: Array[Int] = (0 until size).toArray
      private val rank: Array[Int] = new Array[Int](size)
      var count: Int = size

      def find(x: Int): Int = {
        var cur = x
        while (parent(cur) != cur) {
          parent(cur) = parent(parent(cur))
          cur = parent(cur)
        }
        cur
      }

      def union(a: Int, b: Int): Boolean = {
        var pa = find(a)
        var pb = find(b)
        if (pa == pb) return false
        if (rank(pa) < rank(pb)) {
          val tmp = pa
          pa = pb
          pb = tmp
        }
        parent(pb) = pa
        if (rank(pa) == rank(pb)) rank(pa) += 1
        count -= 1
        true
      }
    }

    val dsuA = new DSU(n)
    val dsuB = new DSU(n)
    var removed = 0

    // Process type 3 edges first
    for (e <- edges if e(0) == 3) {
      val u = e(1) - 1
      val v = e(2) - 1
      val mergedA = dsuA.union(u, v)
      val mergedB = dsuB.union(u, v)
      if (!mergedA && !mergedB) removed += 1
    }

    // Process type 1 and type 2 edges
    for (e <- edges) {
      e(0) match {
        case 1 =>
          val u = e(1) - 1
          val v = e(2) - 1
          if (!dsuA.union(u, v)) removed += 1
        case 2 =>
          val u = e(1) - 1
          val v = e(2) - 1
          if (!dsuB.union(u, v)) removed += 1
        case _ => // ignore type 3 already handled
      }
    }

    if (dsuA.count != 1 || dsuB.count != 1) -1 else removed
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_num_edges_to_remove(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        #[derive(Clone)]
        struct DSU {
            parent: Vec<usize>,
            rank: Vec<usize>,
            components: usize,
        }
        impl DSU {
            fn new(size: usize) -> Self {
                let mut parent = Vec::with_capacity(size);
                for i in 0..size {
                    parent.push(i);
                }
                DSU {
                    parent,
                    rank: vec![0; size],
                    components: size,
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
                if self.rank[ra] < self.rank[rb] {
                    std::mem::swap(&mut ra, &mut rb);
                }
                self.parent[rb] = ra;
                if self.rank[ra] == self.rank[rb] {
                    self.rank[ra] += 1;
                }
                self.components -= 1;
                true
            }
        }

        let mut dsu_alice = DSU::new(n as usize);
        let mut dsu_bob = DSU::new(n as usize);
        let mut used: usize = 0;

        // Type 3 edges first
        for e in &edges {
            if e[0] == 3 {
                let a = (e[1] - 1) as usize;
                let b = (e[2] - 1) as usize;
                let merged_a = dsu_alice.union(a, b);
                let merged_b = dsu_bob.union(a, b);
                if merged_a || merged_b {
                    used += 1;
                }
            }
        }

        // Type 1 edges for Alice
        for e in &edges {
            if e[0] == 1 {
                let a = (e[1] - 1) as usize;
                let b = (e[2] - 1) as usize;
                if dsu_alice.union(a, b) {
                    used += 1;
                }
            }
        }

        // Type 2 edges for Bob
        for e in &edges {
            if e[0] == 2 {
                let a = (e[1] - 1) as usize;
                let b = (e[2] - 1) as usize;
                if dsu_bob.union(a, b) {
                    used += 1;
                }
            }
        }

        if dsu_alice.components != 1 || dsu_bob.components != 1 {
            -1
        } else {
            (edges.len() - used) as i32
        }
    }
}
```

## Racket

```racket
#lang racket

(define/contract (max-num-edges-to-remove n edges)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (define (make-dsu size)
    (let ([parent (make-vector (+ size 1))]
          [rank   (make-vector (+ size 1) 0)])
      (for ([i (in-range (+ size 1))])
        (vector-set! parent i i))
      (list parent rank)))
  (define (find dsu x)
    (let* ([parent (first dsu)]
           [p (vector-ref parent x)])
      (if (= p x)
          x
          (let ([root (find dsu p)])
            (vector-set! parent x root)
            root))))
  (define (union dsu x y)
    (let* ([parent (first dsu)]
           [rank   (second dsu)]
           [rx (find dsu x)]
           [ry (find dsu y)])
      (if (= rx ry)
          #f
          (begin
            (cond [(< (vector-ref rank rx) (vector-ref rank ry))
                   (vector-set! parent rx ry)]
                  [(> (vector-ref rank rx) (vector-ref rank ry))
                   (vector-set! parent ry rx)]
                  [else
                   (vector-set! parent ry rx)
                   (vector-set! rank rx (+ (vector-ref rank rx) 1))])
            #t))))
  (define alice (make-dsu n))
  (define bob   (make-dsu n))
  (define remove-count 0)
  (define used-alice 0)
  (define used-bob 0)
  ;; type 3 edges
  (for ([e edges])
    (match e
      [(list t u v)
       (when (= t 3)
         (let ([merged-a (union alice u v)]
               [merged-b (union bob u v)])
           (if (or merged-a merged-b)
               (begin
                 (when merged-a (set! used-alice (+ used-alice 1)))
                 (when merged-b (set! used-bob   (+ used-bob   1))))
               (set! remove-count (+ remove-count 1)))))]))
  ;; type 1 edges for Alice
  (for ([e edges])
    (match e
      [(list t u v)
       (when (= t 1)
         (if (union alice u v)
             (set! used-alice (+ used-alice 1))
             (set! remove-count (+ remove-count 1))))]))
  ;; type 2 edges for Bob
  (for ([e edges])
    (match e
      [(list t u v)
       (when (= t 2)
         (if (union bob u v)
             (set! used-bob (+ used-bob 1))
             (set! remove-count (+ remove-count 1))))]))
  (if (and (= used-alice (- n 1)) (= used-bob (- n 1)))
      remove-count
      -1))
```

## Erlang

```erlang
-module(solution).
-export([max_num_edges_to_remove/2]).

%% Entry point
-spec max_num_edges_to_remove(N :: integer(), Edges :: [[integer()]]) -> integer().
max_num_edges_to_remove(N, Edges) ->
    % Partition edges by type
    Type3 = [E || E <- Edges, hd(E) == 3],
    Type1 = [E || E <- Edges, hd(E) == 1],
    Type2 = [E || E <- Edges, hd(E) == 2],

    % Initialize DSU structures for Alice and Bob
    InitParent = maps:from_list([{I, I} || I <- lists:seq(1, N)]),
    InitRank   = maps:from_list([{I, 0} || I <- lists:seq(1, N)]),

    % Process type 3 edges first
    {AP1, AR1, BP1, BR1, MergesA1, MergesB1, Used1} =
        process_type3(Type3, InitParent, InitRank, InitParent, InitRank,
                      0, 0, 0),

    % Process type 1 edges (Alice only)
    {AP2, AR2, MergesA2, Used2} =
        process_type1(Type1, AP1, AR1, MergesA1, Used1),

    % Process type 2 edges (Bob only)
    {BP2, BR2, MergesB2, Used3} =
        process_type2(Type2, BP1, BR1, MergesB1, Used2),

    TotalUsed = Used3,
    case (MergesA2 == N - 1) andalso (MergesB2 == N - 1) of
        true -> length(Edges) - TotalUsed;
        false -> -1
    end.

%% Process type 3 edges (both Alice and Bob)
-spec process_type3([[integer()]], map(), map(), map(), map(),
                    integer(), integer(), integer()) ->
          {map(), map(), map(), map(), integer(), integer(), integer()}.
process_type3([], AP, AR, BP, BR, MA, MB, Used) ->
    {AP, AR, BP, BR, MA, MB, Used};
process_type3([[_, U, V] | Rest], AP, AR, BP, BR, MA, MB, Used) ->
    {AP1, AR1, ChangedA} = union(AP, AR, U, V),
    {BP1, BR1, ChangedB} = union(BP, BR, U, V),

    NewUsed = case (ChangedA orelse ChangedB) of
                  true -> Used + 1;
                  false -> Used
              end,
    NewMA = if ChangedA -> MA + 1 else MA end,
    NewMB = if ChangedB -> MB + 1 else MB end,

    process_type3(Rest, AP1, AR1, BP1, BR1, NewMA, NewMB, NewUsed).

%% Process type 1 edges (Alice only)
-spec process_type1([[integer()]], map(), map(),
                    integer(), integer()) ->
          {map(), map(), integer(), integer()}.
process_type1([], AP, AR, MA, Used) ->
    {AP, AR, MA, Used};
process_type1([[_, U, V] | Rest], AP, AR, MA, Used) ->
    {AP1, AR1, Changed} = union(AP, AR, U, V),
    NewUsed = if Changed -> Used + 1 else Used end,
    NewMA   = if Changed -> MA + 1 else MA end,
    process_type1(Rest, AP1, AR1, NewMA, NewUsed).

%% Process type 2 edges (Bob only)
-spec process_type2([[integer()]], map(), map(),
                    integer(), integer()) ->
          {map(), map(), integer(), integer()}.
process_type2([], BP, BR, MB, Used) ->
    {BP, BR, MB, Used};
process_type2([[_, U, V] | Rest], BP, BR, MB, Used) ->
    {BP1, BR1, Changed} = union(BP, BR, U, V),
    NewUsed = if Changed -> Used + 1 else Used end,
    NewMB   = if Changed -> MB + 1 else MB end,
    process_type2(Rest, BP1, BR1, NewMB, NewUsed).

%% Union-Find: find with path compression
-spec find(map(), integer()) -> {integer(), map()}.
find(Parent, X) ->
    case maps:get(X, Parent) of
        X -> {X, Parent};
        P ->
            {Root, UpdatedParent} = find(Parent, P),
            NewParent = maps:put(X, Root, UpdatedParent),
            {Root, NewParent}
    end.

%% Union operation; returns updated parent map, rank map and whether a merge happened
-spec union(map(), map(), integer(), integer()) -> {map(), map(), boolean()}.
union(Parent, Rank, X, Y) ->
    {Rx, Parent1} = find(Parent, X),
    {Ry, Parent2} = find(Parent1, Y),
    if Rx == Ry ->
            {Parent2, Rank, false};
       true ->
            RankX = maps:get(Rx, Rank),
            RankY = maps:get(Ry, Rank),
            case RankX < RankY of
                true ->
                    NewParent = maps:put(Rx, Ry, Parent2),
                    {NewParent, Rank, true};
                false when RankX > RankY ->
                    NewParent = maps:put(Ry, Rx, Parent2),
                    {NewParent, Rank, true};
                false -> % equal ranks
                    NewParent1 = maps:put(Ry, Rx, Parent2),
                    NewRank    = maps:put(Rx, RankX + 1, Rank),
                    {NewParent1, NewRank, true}
            end
    end.
```

## Elixir

```elixir
defmodule DSU do
  defstruct parent: %{}, rank: %{}, components: 0

  def new(n) do
    parent = Enum.into(1..n, %{}, fn i -> {i, i} end)
    rank = Enum.into(1..n, %{}, fn i -> {i, 0} end)
    %DSU{parent: parent, rank: rank, components: n}
  end

  def find(dsu, x) do
    p = Map.get(dsu.parent, x)

    if p == x do
      {x, dsu}
    else
      {root, dsu2} = find(dsu, p)
      new_parent = Map.put(dsu2.parent, x, root)
      {%{dsu2 | parent: new_parent}, root}
    end
  end

  def union(dsu, x, y) do
    {rx, dsu1} = find(dsu, x)
    {ry, dsu2} = find(dsu1, y)

    if rx == ry do
      {dsu2, false}
    else
      rankx = Map.get(dsu2.rank, rx)
      ranky = Map.get(dsu2.rank, ry)

      cond do
        rankx < ranky ->
          new_parent = Map.put(dsu2.parent, rx, ry)
          {%{dsu2 | parent: new_parent, components: dsu2.components - 1}, true}

        rankx > ranky ->
          new_parent = Map.put(dsu2.parent, ry, rx)
          {%{dsu2 | parent: new_parent, components: dsu2.components - 1}, true}

        true ->
          new_parent = Map.put(dsu2.parent, ry, rx)
          new_rank = Map.put(dsu2.rank, rx, rankx + 1)
          {%{
             dsu2
             | parent: new_parent,
               rank: new_rank,
               components: dsu2.components - 1
           }, true}
      end
    end
  end
end

defmodule Solution do
  @spec max_num_edges_to_remove(n :: integer, edges :: [[integer]]) :: integer
  def max_num_edges_to_remove(n, edges) do
    type3 = for [t, u, v] <- edges, t == 3, do: [t, u, v]
    type1 = for [t, u, v] <- edges, t == 1, do: [t, u, v]
    type2 = for [t, u, v] <- edges, t == 2, do: [t, u, v]

    dsu_a = DSU.new(n)
    dsu_b = DSU.new(n)

    {dsu_a, dsu_b, used} =
      Enum.reduce(type3, {dsu_a, dsu_b, 0}, fn [_type, u, v], {da, db, cnt} ->
        {da2, merged_a} = DSU.union(da, u, v)
        {db2, merged_b} = DSU.union(db, u, v)

        if merged_a or merged_b do
          {da2, db2, cnt + 1}
        else
          {da2, db2, cnt}
        end
      end)

    {dsu_a, used} =
      Enum.reduce(type1, {dsu_a, used}, fn [_type, u, v], {da, cnt} ->
        {da2, merged} = DSU.union(da, u, v)

        if merged do
          {da2, cnt + 1}
        else
          {da2, cnt}
        end
      end)

    {dsu_b, used} =
      Enum.reduce(type2, {dsu_b, used}, fn [_type, u, v], {db, cnt} ->
        {db2, merged} = DSU.union(db, u, v)

        if merged do
          {db2, cnt + 1}
        else
          {db2, cnt}
        end
      end)

    if dsu_a.components == 1 and dsu_b.components == 1 do
      length(edges) - used
    else
      -1
    end
  end
end
```

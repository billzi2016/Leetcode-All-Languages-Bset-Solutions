# 0685. Redundant Connection II

## Cpp

```cpp
class Solution {
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> firstEdgeIdx(n + 1, -1);
        int candA = -1, candB = -1; // indices of the two candidate edges
        
        for (int i = 0; i < n; ++i) {
            int u = edges[i][0], v = edges[i][1];
            if (firstEdgeIdx[v] == -1) {
                firstEdgeIdx[v] = i;
            } else {
                // node v has two parents
                candA = firstEdgeIdx[v]; // earlier edge
                candB = i;               // later edge
                break; // we can stop recording further, but continue processing for union-find later
            }
        }
        
        vector<int> dsu(n + 1);
        iota(dsu.begin(), dsu.end(), 0);
        function<int(int)> find = [&](int x) {
            return dsu[x] == x ? x : dsu[x] = find(dsu[x]);
        };
        auto unite = [&](int a, int b) {
            dsu[find(a)] = find(b);
        };
        
        for (int i = 0; i < n; ++i) {
            if (i == candB) continue; // skip later edge if double-parent case
            int u = edges[i][0], v = edges[i][1];
            int pu = find(u), pv = find(v);
            if (pu == pv) { // cycle detected
                if (candA != -1) return edges[candA]; // two-parent case, remove earlier edge
                return edges[i]; // no two-parent case, remove current edge causing cycle
            }
            unite(u, v);
        }
        
        // No cycle found; must be the double-parent situation without a cycle
        return edges[candB];
    }
};
```

## Java

```java
class Solution {
    public int[] findRedundantDirectedConnection(int[][] edges) {
        int n = edges.length;
        int[] parentIdx = new int[n + 1];
        for (int i = 0; i <= n; i++) parentIdx[i] = -1;

        int firstEdgeIdx = -1, secondEdgeIdx = -1;

        // Detect a node with two parents
        for (int i = 0; i < n; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            if (parentIdx[v] != -1) {
                firstEdgeIdx = parentIdx[v];   // earlier edge
                secondEdgeIdx = i;             // later edge
            } else {
                parentIdx[v] = i;
            }
        }

        DSU dsu = new DSU(n + 1);
        for (int i = 0; i < n; i++) {
            if (i == secondEdgeIdx) continue; // skip candidate2 initially
            int u = edges[i][0];
            int v = edges[i][1];
            if (!dsu.union(u, v)) { // cycle detected
                if (firstEdgeIdx != -1) {
                    return edges[firstEdgeIdx]; // case with two parents and a cycle
                } else {
                    return edges[i]; // simple cycle without double parent
                }
            }
        }

        // No cycle found after skipping candidate2
        if (secondEdgeIdx != -1) {
            return edges[secondEdgeIdx];
        }

        // Should never reach here per problem constraints
        return new int[0];
    }

    private static class DSU {
        int[] parent;
        int[] rank;

        DSU(int size) {
            parent = new int[size];
            rank = new int[size];
            for (int i = 0; i < size; i++) {
                parent[i] = i;
                rank[i] = 1;
            }
        }

        int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        boolean union(int x, int y) {
            int px = find(x);
            int py = find(y);
            if (px == py) return false; // already connected -> cycle
            if (rank[px] < rank[py]) {
                parent[px] = py;
            } else if (rank[px] > rank[py]) {
                parent[py] = px;
            } else {
                parent[py] = px;
                rank[px]++;
            }
            return true;
        }
    }
}
```

## Python

```python
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        parent = {}
        candidates = None  # [edge1, edge2] where edge2 is the later one
        
        for u, v in edges:
            if v in parent:
                candidates = [[parent[v], v], [u, v]]
                # keep the first edge as recorded, do not overwrite
            else:
                parent[v] = u

        # Union-Find setup
        dsu = list(range(n + 1))

        def find(x):
            while dsu[x] != x:
                dsu[x] = dsu[dsu[x]]
                x = dsu[x]
            return x

        for u, v in edges:
            if candidates and [u, v] == candidates[1]:
                # skip the second edge temporarily
                continue
            pu, pv = find(u), find(v)
            if pu == pv:
                # cycle detected
                if not candidates:
                    return [u, v]
                else:
                    return candidates[0]

        # If we reach here, there was a node with two parents but no cycle when skipping edge2
        return candidates[1]
```

## Python3

```python
from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent_of = [0] * (n + 1)          # stores the current parent of each node
        cand1 = None                       # first edge causing two parents
        cand2 = None                       # second edge causing two parents
        skip_index = -1                    # index of edge to ignore during union-find

        for i, (u, v) in enumerate(edges):
            if parent_of[v] == 0:
                parent_of[v] = u
            else:
                # node v has two parents
                cand1 = [parent_of[v], v]   # earlier edge
                cand2 = [u, v]              # later edge (current)
                skip_index = i             # ignore this later edge initially
                # keep the first parent as is
        # Union-Find setup
        dsu_parent = list(range(n + 1))

        def find(x: int) -> int:
            while dsu_parent[x] != x:
                dsu_parent[x] = dsu_parent[dsu_parent[x]]
                x = dsu_parent[x]
            return x

        def union(x: int, y: int) -> bool:
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            dsu_parent[ry] = rx
            return True

        for i, (u, v) in enumerate(edges):
            if i == skip_index:
                continue
            if not union(u, v):
                # cycle detected
                if cand1 is None:
                    return [u, v]
                else:
                    return cand1

        # No cycle found; must be the two‑parent case without a cycle
        return cand2
```

## C

```c
#include <stdlib.h>

/* Union-Find helper functions */
static int find(int *dsu, int x) {
    if (dsu[x] != x) dsu[x] = find(dsu, dsu[x]);
    return dsu[x];
}

static void unite(int *dsu, int a, int b) {
    dsu[find(dsu, a)] = find(dsu, b);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findRedundantDirectedConnection(int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    int n = edgesSize;
    int *parent = (int *)calloc(n + 1, sizeof(int));
    
    int cand1[2] = {0, 0}, cand2[2] = {0, 0};
    int cand2Idx = -1;   // index of the later edge when a node has two parents
    
    for (int i = 0; i < n; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        if (parent[v] != 0) {
            cand1[0] = parent[v]; cand1[1] = v;
            cand2[0] = u;         cand2[1] = v;
            cand2Idx = i;
        } else {
            parent[v] = u;
        }
    }
    
    int *dsu = (int *)malloc((n + 1) * sizeof(int));
    for (int i = 1; i <= n; ++i) dsu[i] = i;
    
    for (int i = 0; i < n; ++i) {
        if (cand2Idx != -1 && i == cand2Idx) continue; // skip later edge temporarily
        int u = edges[i][0];
        int v = edges[i][1];
        int ru = find(dsu, u);
        int rv = find(dsu, v);
        if (ru == rv) {
            int *ans = (int *)malloc(2 * sizeof(int));
            *returnSize = 2;
            if (cand2Idx == -1) {          // no node with two parents
                ans[0] = u; ans[1] = v;
            } else {                       // cycle caused by the earlier edge
                ans[0] = cand1[0]; ans[1] = cand1[1];
            }
            free(parent);
            free(dsu);
            return ans;
        }
        unite(dsu, ru, rv);
    }
    
    /* If we reach here, there was a node with two parents but no cycle.
       The later edge is the one to remove. */
    int *ans = (int *)malloc(2 * sizeof(int));
    *returnSize = 2;
    ans[0] = cand2[0];
    ans[1] = cand2[1];
    
    free(parent);
    free(dsu);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] FindRedundantDirectedConnection(int[][] edges) {
        int n = edges.Length;
        int[] indegreeParent = new int[n + 1];
        int[] candA = null, candB = null;

        // Detect a node with two parents
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            if (indegreeParent[v] == 0) {
                indegreeParent[v] = u;
            } else {
                candA = new int[] { indegreeParent[v], v }; // first edge
                candB = new int[] { u, v };                 // second edge
            }
        }

        // Union-Find helpers
        int Find(int x, int[] parent) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        // Case 1: there is a node with two parents
        if (candB != null) {
            int[] parent = new int[n + 1];
            for (int i = 1; i <= n; i++) parent[i] = i;

            foreach (var e in edges) {
                int u = e[0], v = e[1];
                if (u == candB[0] && v == candB[1]) continue; // skip second edge

                int ru = Find(u, parent);
                int rv = Find(v, parent);
                if (ru == rv) {
                    // Cycle detected without the second edge -> remove first edge
                    return candA;
                }
                parent[ru] = rv;
            }
            // No cycle when skipping second edge -> remove second edge
            return candB;
        }

        // Case 2: no node has two parents, just find the cycle
        int[] ufParent = new int[n + 1];
        for (int i = 1; i <= n; i++) ufParent[i] = i;

        foreach (var e in edges) {
            int u = e[0], v = e[1];
            int ru = Find(u, ufParent);
            int rv = Find(v, ufParent);
            if (ru == rv) return e;
            ufParent[ru] = rv;
        }

        // Should never reach here
        return new int[0];
    }
}
```

## Javascript

```javascript
var findRedundantDirectedConnection = function(edges) {
    const n = edges.length;
    const dsuParent = new Array(n + 1);
    for (let i = 1; i <= n; ++i) dsuParent[i] = i;

    const indeg = new Array(n + 1).fill(0);
    let candA = null, candB = null;
    let skipIdx = -1;

    // Detect a node with two parents
    for (let i = 0; i < edges.length; ++i) {
        const [u, v] = edges[i];
        if (indeg[v] === 0) {
            indeg[v] = i + 1; // store index+1 to differentiate from default 0
        } else {
            // v already has a parent -> two incoming edges
            const firstIdx = indeg[v] - 1;
            candA = [edges[firstIdx][0], v]; // earlier edge
            candB = [u, v];                 // later edge
            skipIdx = i;                    // candidate to possibly ignore
            break; // only one such node can exist
        }
    }

    const find = (x) => {
        if (dsuParent[x] !== x) dsuParent[x] = find(dsuParent[x]);
        return dsuParent[x];
    };

    for (let i = 0; i < edges.length; ++i) {
        if (i === skipIdx) continue; // temporarily ignore later edge
        const [u, v] = edges[i];
        const pu = find(u);
        const pv = find(v);
        if (pu === pv) {
            // cycle detected
            return candA ? candA : [u, v];
        }
        dsuParent[pv] = pu;
    }

    // No cycle found; the later edge is the redundant one
    return candB;
};
```

## Typescript

```typescript
function findRedundantDirectedConnection(edges: number[][]): number[] {
    const n = edges.length;
    const indegree = new Array(n + 1).fill(0);
    let candA: number[] | null = null; // first edge causing two parents
    let candB: number[] | null = null; // second edge causing two parents
    let skipIdx = -1;

    for (let i = 0; i < edges.length; i++) {
        const [u, v] = edges[i];
        if (indegree[v] === 0) {
            indegree[v] = u;
        } else {
            // node v has two parents
            candA = [indegree[v], v]; // earlier edge
            candB = [u, v];           // later edge
            skipIdx = i;              // we will try removing this one first
        }
    }

    const parentUF = new Array(n + 1);
    for (let i = 0; i <= n; i++) parentUF[i] = i;

    const find = (x: number): number => {
        if (parentUF[x] !== x) parentUF[x] = find(parentUF[x]);
        return parentUF[x];
    };

    for (let i = 0; i < edges.length; i++) {
        if (i === skipIdx) continue; // temporarily ignore the second incoming edge
        const [u, v] = edges[i];
        const pu = find(u);
        const pv = find(v);
        if (pu === pv) {
            // cycle detected
            return candA ? candA : [u, v];
        }
        parentUF[pv] = pu;
    }

    // No cycle found; the problem is the node with two parents
    // Remove the later edge (candB)
    return candB as number[];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @return Integer[]
     */
    function findRedundantDirectedConnection($edges) {
        $n = count($edges);
        // Union-Find parent array
        $parent = [];
        for ($i = 0; $i <= $n; $i++) {
            $parent[$i] = $i;
        }

        // indegree tracking to find node with two parents
        $indegree = array_fill(0, $n + 1, 0);
        $candidate1 = null; // first edge causing two parents
        $candidate2 = null; // second edge causing two parents

        foreach ($edges as $edge) {
            [$u, $v] = $edge;
            if ($indegree[$v] != 0) {
                // node v already has a parent
                $candidate1 = [$indegree[$v], $v]; // previous edge
                $candidate2 = [$u, $v];           // current edge
            } else {
                $indegree[$v] = $u;
            }
        }

        foreach ($edges as $edge) {
            // skip candidate2 if it exists
            if ($candidate2 !== null && $edge[0] == $candidate2[0] && $edge[1] == $candidate2[1]) {
                continue;
            }
            [$u, $v] = $edge;
            $pu = $this->find($u, $parent);
            $pv = $this->find($v, $parent);
            if ($pu == $pv) {
                // cycle detected
                if ($candidate1 === null) {
                    return $edge;          // no two‑parent situation
                } else {
                    return $candidate1;    // remove the earlier edge
                }
            }
            $parent[$pu] = $pv;
        }

        // No cycle found in first pass, so candidate2 is redundant
        return $candidate2;
    }

    /**
     * Union-Find find with path compression.
     *
     * @param int   $x
     * @param array &$parent
     * @return int
     */
    private function find($x, &$parent) {
        while ($parent[$x] != $x) {
            $parent[$x] = $parent[$parent[$x]];
            $x = $parent[$x];
        }
        return $x;
    }
}
```

## Swift

```swift
class Solution {
    func findRedundantDirectedConnection(_ edges: [[Int]]) -> [Int] {
        let n = edges.count
        var parent = [Int](repeating: 0, count: n + 1)
        var candA: [Int]? = nil
        var candB: [Int]? = nil
        
        // Detect a node with two parents
        for edge in edges {
            let u = edge[0]
            let v = edge[1]
            if parent[v] != 0 {
                // Two incoming edges to v
                candA = [parent[v], v]   // first edge
                candB = [u, v]           // second edge (current)
            } else {
                parent[v] = u
            }
        }
        
        // Union-Find structure
        class UnionFind {
            var p: [Int]
            init(_ size: Int) {
                p = Array(0...size)
            }
            func find(_ x: Int) -> Int {
                if p[x] != x {
                    p[x] = find(p[x])
                }
                return p[x]
            }
            func union(_ x: Int, _ y: Int) {
                let fx = find(x)
                let fy = find(y)
                if fx != fy {
                    p[fx] = fy
                }
            }
        }
        
        // Helper to compare edges
        func sameEdge(_ e1: [Int], _ e2: [Int]) -> Bool {
            return e1[0] == e2[0] && e1[1] == e2[1]
        }
        
        if let skip = candB { // there is a node with two parents
            let uf = UnionFind(n)
            for edge in edges {
                if sameEdge(edge, skip) { continue } // try removing candB
                let u = edge[0], v = edge[1]
                let fu = uf.find(u), fv = uf.find(v)
                if fu == fv {
                    // Cycle detected without candB, so answer must be candA
                    return candA!
                }
                uf.union(fu, fv)
            }
            // No cycle found, removing candB resolves the issue
            return candB!
        } else {
            // No node with two parents; just find the edge causing a cycle
            let uf = UnionFind(n)
            for edge in edges {
                let u = edge[0], v = edge[1]
                let fu = uf.find(u), fv = uf.find(v)
                if fu == fv {
                    return edge
                }
                uf.union(fu, fv)
            }
        }
        // Should never reach here per problem constraints
        return []
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findRedundantDirectedConnection(edges: Array<IntArray>): IntArray {
        val n = edges.size
        val parent = IntArray(n + 1) // stores the immediate parent of each node (0 if none)
        var candidate1: IntArray? = null
        var candidate2: IntArray? = null
        var skipIdx = -1

        for (i in edges.indices) {
            val u = edges[i][0]
            val v = edges[i][1]
            if (parent[v] != 0) {
                // node v has two parents
                candidate1 = intArrayOf(parent[v], v) // earlier edge
                candidate2 = intArrayOf(u, v)         // later edge
                skipIdx = i                           // we will try removing this later edge first
            } else {
                parent[v] = u
            }
        }

        // Union-Find initialization
        val dsu = IntArray(n + 1) { it }

        fun find(x: Int): Int {
            var cur = x
            while (dsu[cur] != cur) {
                dsu[cur] = dsu[dsu[cur]]
                cur = dsu[cur]
            }
            return cur
        }

        fun union(a: Int, b: Int) {
            val ra = find(a)
            val rb = find(b)
            if (ra != rb) {
                dsu[ra] = rb
            }
        }

        for (i in edges.indices) {
            if (i == skipIdx) continue // temporarily ignore the second candidate edge
            val u = edges[i][0]
            val v = edges[i][1]
            val ru = find(u)
            val rv = find(v)
            if (ru == rv) {
                // cycle detected
                return candidate1 ?: intArrayOf(u, v)
            }
            dsu[ru] = rv
        }

        // If we reach here, no cycle was found without the second candidate edge.
        // The problem must be the two‑parent case; remove the later edge.
        return candidate2!!
    }
}
```

## Dart

```dart
class Solution {
  List<int> findRedundantDirectedConnection(List<List<int>> edges) {
    int n = edges.length;
    List<int> parent = List.filled(n + 1, 0);
    List<int>? cand1;
    List<int>? cand2;

    // Step 1: check whether there is a node with two parents
    for (var edge in edges) {
      int u = edge[0];
      int v = edge[1];
      if (parent[v] != 0) {
        // v already has a parent
        cand1 = [parent[v], v]; // first edge causing two parents
        cand2 = [u, v];         // second edge causing two parents
        // mark this edge to be ignored later
      } else {
        parent[v] = u;
      }
    }

    // Union-Find initialization
    List<int> ufParent = List.generate(n + 1, (i) => i);
    List<int> rank = List.filled(n + 1, 0);

    int find(int x) {
      while (ufParent[x] != x) {
        ufParent[x] = ufParent[ufParent[x]];
        x = ufParent[x];
      }
      return x;
    }

    bool union(int x, int y) {
      int px = find(x);
      int py = find(y);
      if (px == py) return false; // cycle
      if (rank[px] < rank[py]) {
        ufParent[px] = py;
      } else if (rank[px] > rank[py]) {
        ufParent[py] = px;
      } else {
        ufParent[py] = px;
        rank[px]++;
      }
      return true;
    }

    // Step 2: process edges, possibly skipping cand2
    for (var edge in edges) {
      int u = edge[0];
      int v = edge[1];
      if (cand2 != null && u == cand2[0] && v == cand2[1]) {
        continue; // skip the second candidate edge
      }
      if (!union(u, v)) {
        // cycle detected
        return cand1 ?? [u, v];
      }
    }

    // If we reach here, there was a node with two parents but no cycle when skipping cand2
    return cand2!;
  }
}
```

## Golang

```go
func findRedundantDirectedConnection(edges [][]int) []int {
    n := len(edges)
    indegree := make([]int, n+1)
    parentOf := make([]int, n+1)

    var cand1, cand2 []int

    for _, e := range edges {
        u, v := e[0], e[1]
        if indegree[v] == 0 {
            indegree[v] = 1
            parentOf[v] = u
        } else {
            // node v has two parents
            cand1 = []int{parentOf[v], v}
            cand2 = []int{u, v}
        }
    }

    dsu := make([]int, n+1)
    for i := 1; i <= n; i++ {
        dsu[i] = i
    }

    var find func(int) int
    find = func(x int) int {
        if dsu[x] != x {
            dsu[x] = find(dsu[x])
        }
        return dsu[x]
    }

    for _, e := range edges {
        // skip the second candidate edge if it exists
        if cand2 != nil && e[0] == cand2[0] && e[1] == cand2[1] {
            continue
        }
        u, v := e[0], e[1]
        pu, pv := find(u), find(v)
        if pu == pv {
            // cycle detected
            if cand1 != nil {
                return cand1
            }
            return []int{u, v}
        }
        dsu[pv] = pu
    }

    // No cycle found; the problem is the node with two parents
    return cand2
}
```

## Ruby

```ruby
class UnionFind
  def initialize(size)
    @parent = Array.new(size) { |i| i }
  end

  def find(x)
    while @parent[x] != x
      @parent[x] = @parent[@parent[x]]
      x = @parent[x]
    end
    x
  end

  def union(x, y)
    px = find(x)
    py = find(y)
    @parent[px] = py unless px == py
  end
end

# @param {Integer[][]} edges
# @return {Integer[]}
def find_redundant_directed_connection(edges)
  n = edges.length
  incoming = Array.new(n + 1, 0) # store the parent node of each child
  candidates = []               # will hold two edges if a node has two parents

  edges.each do |u, v|
    if incoming[v] != 0
      # node v already has a parent; record both edges
      candidates << [incoming[v], v] # earlier edge
      candidates << [u, v]           # later edge
      # skip adding this edge to the graph for now
    else
      incoming[v] = u
    end
  end

  if candidates.empty?
    uf = UnionFind.new(n + 1)
    edges.each do |u, v|
      if uf.find(u) == uf.find(v)
        return [u, v]
      else
        uf.union(u, v)
      end
    end
  else
    # Try removing the later edge first
    later = candidates[1]
    uf = UnionFind.new(n + 1)

    edges.each do |u, v|
      next if u == later[0] && v == later[1]

      if uf.find(u) == uf.find(v)
        # Cycle detected without the later edge -> remove earlier edge
        return candidates[0]
      else
        uf.union(u, v)
      end
    end

    # No cycle found; removing later edge resolves the issue
    return later
  end
end
```

## Scala

```scala
object Solution {
    def findRedundantDirectedConnection(edges: Array[Array[Int]]): Array[Int] = {
        val n = edges.length
        val indegree = new Array[Int](n + 1) // stores parent node for each child, 0 if none
        var candA: Array[Int] = null
        var candB: Array[Int] = null

        // Detect a node with two parents
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            if (indegree(v) != 0) {
                // previous edge that gave parent to v
                candA = Array(indegree(v), v)
                candB = Array(u, v)
            } else {
                indegree(v) = u
            }
        }

        // Union-Find initialization
        val ufParent = (0 to n).toArray

        def find(x: Int): Int = {
            if (ufParent(x) != x) {
                ufParent(x) = find(ufParent(x))
            }
            ufParent(x)
        }

        var cycleEdge: Array[Int] = null

        // Union edges, possibly skipping candB
        for (e <- edges) {
            val u = e(0)
            val v = e(1)

            if (candB != null && u == candB(0) && v == candB(1)) {
                // skip this edge temporarily
                ()
            } else {
                val pu = find(u)
                val pv = find(v)
                if (pu == pv) {
                    cycleEdge = Array(u, v)
                } else {
                    ufParent(pv) = pu
                }
            }
        }

        if (candA == null) {
            // No node with two parents; the edge causing a cycle is answer
            cycleEdge
        } else {
            // There was a node with two parents
            if (cycleEdge != null) {
                // Cycle still exists when candB is ignored, so remove candA
                candA
            } else {
                // No cycle when candB is ignored, so remove candB
                candB
            }
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_redundant_directed_connection(edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = edges.len();
        // parent[v] stores the node that points to v (0 if none)
        let mut parent = vec![0i32; n + 1];
        let mut cand1: Option<(i32, i32)> = None;
        let mut cand2: Option<(i32, i32)> = None;

        // Detect a node with two parents
        for e in &edges {
            let u = e[0];
            let v = e[1];
            if parent[v as usize] != 0 {
                // v already has a parent
                cand1 = Some((parent[v as usize], v));
                cand2 = Some((u, v));
            } else {
                parent[v as usize] = u;
            }
        }

        // Union-Find structure
        struct DSU {
            parent: Vec<usize>,
        }
        impl DSU {
            fn new(size: usize) -> Self {
                let mut p = vec![0; size + 1];
                for i in 0..=size {
                    p[i] = i;
                }
                DSU { parent: p }
            }
            fn find(&mut self, x: usize) -> usize {
                if self.parent[x] != x {
                    let root = self.find(self.parent[x]);
                    self.parent[x] = root;
                }
                self.parent[x]
            }
            fn union(&mut self, x: usize, y: usize) {
                let rx = self.find(x);
                let ry = self.find(y);
                if rx != ry {
                    self.parent[rx] = ry;
                }
            }
        }

        let mut dsu = DSU::new(n);

        // Process edges, possibly skipping the second candidate edge
        for e in &edges {
            let u = e[0];
            let v = e[1];

            if let Some((c2u, c2v)) = cand2 {
                if u == c2u && v == c2v {
                    // skip this edge temporarily
                    continue;
                }
            }

            let ru = dsu.find(u as usize);
            let rv = dsu.find(v as usize);

            if ru == rv {
                // Cycle detected
                if cand1.is_some() {
                    let (a, b) = cand1.unwrap();
                    return vec![a, b];
                } else {
                    return vec![u, v];
                }
            } else {
                dsu.parent[ru] = rv;
            }
        }

        // If we reach here, the graph is acyclic after removing cand2,
        // so cand2 is the redundant edge.
        if let Some((a, b)) = cand2 {
            return vec![a, b];
        }

        Vec::new()
    }
}
```

## Racket

```racket
(define/contract (find-redundant-directed-connection edges)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((n (length edges))
         (indeg (make-vector (+ n 1) -1))
         (candidate1 #f)
         (candidate2 #f)
         (cand2-index -1))
    ;; First pass: detect a node with two parents
    (for ([i (in-range n)])
      (let* ((e (list-ref edges i))
             (u (first e))
             (v (second e)))
        (if (= (vector-ref indeg v) -1)
            (vector-set! indeg v i)
            (begin
              (set! candidate1 (list (first (list-ref edges (vector-ref indeg v))) v))
              (set! candidate2 (list u v))
              (set! cand2-index i)))))
    ;; Union-Find initialization
    (let ((parent (make-vector (+ n 1) 0)))
      (for ([i (in-range (+ n 1))])
        (vector-set! parent i i))
      (define (find x)
        (if (= (vector-ref parent x) x)
            x
            (let ((root (find (vector-ref parent x))))
              (vector-set! parent x root)
              root)))
      (define (union x y)
        (let ((rx (find x))
              (ry (find y)))
          (unless (= rx ry)
            (vector-set! parent rx ry))))
      ;; Second pass: detect cycle, skipping candidate2 if it exists
      (let ((result #f))
        (for ([i (in-range n)])
          (when (not (and candidate2 (= i cand2-index)))
            (let* ((e (list-ref edges i))
                   (u (first e))
                   (v (second e))
                   (ru (find u))
                   (rv (find v)))
              (if (= ru rv)
                  (set! result (if candidate1 candidate1 (list u v)))
                  (union ru rv)))))
        (if result
            result
            (if candidate2 candidate2 (error "No redundant edge found")))))))
```

## Erlang

```erlang
-module(solution).
-export([find_redundant_directed_connection/1]).

-spec find_redundant_directed_connection(Edges :: [[integer()]]) -> [integer()].
find_redundant_directed_connection(Edges) ->
    N = length(Edges),
    {Cand1, Cand2} = detect_two_parents(Edges),
    UF0 = maps:from_list([{I, I} || I <- lists:seq(1, N)]),
    case Cand2 of
        undefined ->
            {_UF, CycleEdge} = process_edges(Edges, UF0, undefined),
            CycleEdge;
        _ ->
            {_UF, CycleEdge1} = process_edges(Edges, UF0, Cand2),
            case CycleEdge1 of
                undefined -> Cand2;   % no cycle when skipping cand2 => remove later edge
                _         -> Cand1    % cycle exists => remove earlier edge
            end
    end.

%% Detect a node with two parents. Returns {Cand1, Cand2} where Cand1 is the first edge,
%% Cand2 is the second (later) edge. If none, both are undefined.
-spec detect_two_parents([[integer()]]) -> {[integer()], [integer()]} | {undefined, undefined}.
detect_two_parents(Edges) ->
    detect_two_parents(Edges, #{}, undefined, undefined).

-spec detect_two_parents([[integer()]], map(), term(), term()) -> {[integer()], [integer()]} | {undefined, undefined}.
detect_two_parents([], _Map, Cand1, Cand2) ->
    {Cand1, Cand2};
detect_two_parents([[U, V] = Edge | Rest], Map, _Cand1, _Cand2) ->
    case maps:is_key(V, Map) of
        false ->
            detect_two_parents(Rest, maps:put(V, Edge, Map), undefined, undefined);
        true ->
            Prev = maps:get(V, Map),
            {Prev, Edge}
    end.

%% Process edges with optional skip edge. Returns final UF map and the first cycle edge found (if any).
-spec process_edges([[integer()]], map(), [integer()] | undefined) -> {map(), [integer()] | undefined}.
process_edges(Edges, UF, SkipEdge) ->
    process_edges(Edges, UF, SkipEdge, undefined).

-spec process_edges([[integer()]], map(), [integer()] | undefined, [integer()] | undefined) ->
          {map(), [integer()] | undefined}.
process_edges([], UF, _Skip, Cycle) ->
    {UF, Cycle};
process_edges([E = [U, V] | Rest], UF, Skip, Cycle) ->
    case (Skip =/= undefined andalso E == Skip) of
        true ->
            process_edges(Rest, UF, Skip, Cycle);
        false ->
            Ru = find(UF, U),
            Rv = find(UF, V),
            if
                Ru == Rv ->
                    % cycle detected
                    case Cycle of
                        undefined -> process_edges(Rest, UF, Skip, E);
                        _         -> process_edges(Rest, UF, Skip, Cycle)
                    end;
                true ->
                    NewUF = maps:put(Rv, Ru, UF),
                    process_edges(Rest, NewUF, Skip, Cycle)
            end
    end.

%% Find root of node X in Union-Find map.
-spec find(map(), integer()) -> integer().
find(ParentMap, X) ->
    case maps:get(X, ParentMap) of
        X -> X;
        P -> find(ParentMap, P)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_redundant_directed_connection(edges :: [[integer]]) :: [integer]
  def find_redundant_directed_connection(edges) do
    n = length(edges)

    # Detect node with two parents
    {cand1, cand2, cand2_idx} =
      edges
      |> Enum.with_index()
      |> Enum.reduce(%{}, fn {[u, v], idx}, acc ->
        Map.update(acc, v, [{u, v, idx}], fn list -> [{u, v, idx} | list] end)
      end)
      |> Enum.find_value({nil, nil, nil}, fn
        {_, [{_u1, _v1, idx1}, {_u2, _v2, idx2}] = lst} when length(lst) == 2 ->
          sorted = Enum.sort_by(lst, fn {_u, _v, i} -> i end)
          [{u1, v1, i1}, {u2, v2, i2}] = sorted
          {[u1, v1], [u2, v2], i2}
        _ ->
          false
      end)

    # Initialize Union-Find parent map
    parent =
      1..n
      |> Enum.reduce(%{}, fn i, acc -> Map.put(acc, i, i) end)

    {_, answer} =
      edges
      |> Enum.with_index()
      |> Enum.reduce({parent, nil}, fn {[u, v] = edge, idx}, {par, ans} ->
        cond do
          not is_nil(ans) ->
            {par, ans}

          not is_nil(cand2) and idx == cand2_idx ->
            {par, nil}

          true ->
            case union(u, v, par) do
              {:cycle, _new_par} ->
                if not is_nil(cand1), do: {par, cand1}, else: {par, edge}

              {:ok, new_par} ->
                {new_par, nil}
            end
        end
      end)

    cond do
      not is_nil(answer) -> answer
      not is_nil(cand2) -> cand2
      true -> []  # Should never happen per problem constraints
    end
  end

  defp find(x, parent) do
    p = Map.get(parent, x)
    if p == x do
      {x, parent}
    else
      {root, parent2} = find(p, parent)
      {root, Map.put(parent2, x, root)}
    end
  end

  defp union(u, v, parent) do
    {ru, parent1} = find(u, parent)
    {rv, parent2} = find(v, parent1)

    if ru == rv do
      {:cycle, parent2}
    else
      {:ok, Map.put(parent2, rv, ru)}
    end
  end
end
```

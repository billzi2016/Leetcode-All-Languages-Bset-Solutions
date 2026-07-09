# 1719. Number Of Ways To Reconstruct A Tree

## Cpp

```cpp
class Solution {
public:
    int checkWays(vector<vector<int>>& pairs) {
        const int MAXV = 501;
        vector<unordered_set<int>> adj(MAXV);
        vector<bool> present(MAXV,false);
        for (auto &p : pairs) {
            int a=p[0], b=p[1];
            adj[a].insert(b);
            adj[b].insert(a);
            present[a]=present[b]=true;
        }
        // count distinct nodes
        int n=0;
        for(int i=0;i<MAXV;++i) if(present[i]) ++n;
        // find root candidate (connected to all others)
        int root=-1, cntRoot=0;
        for(int i=0;i<MAXV;++i){
            if(present[i] && (int)adj[i].size()==n-1){
                root=i; ++cntRoot;
            }
        }
        if(cntRoot!=1) return 0;
        int ans=1;
        // process each node except root
        for(int i=0;i<MAXV;++i){
            if(!present[i] || i==root) continue;
            int deg = adj[i].size();
            int parent=-1, minParentDeg=INT_MAX;
            for(int nb: adj[i]){
                int nd = adj[nb].size();
                if(nd>=deg && nd<minParentDeg){
                    minParentDeg=nd;
                    parent=nb;
                }
            }
            if(parent==-1) return 0;
            // verify subset condition
            for(int nb: adj[i]){
                if(nb==parent) continue;
                if(!adj[parent].count(nb)) return 0;
            }
            // check ambiguity
            for(int nb: adj[i]){
                if(adj[nb].size()==deg){
                    ans=2;
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int checkWays(int[][] pairs) {
        final int MAX = 500;
        boolean[][] adj = new boolean[MAX + 1][MAX + 1];
        int[] degree = new int[MAX + 1];
        boolean[] present = new boolean[MAX + 1];
        int distinct = 0;

        for (int[] p : pairs) {
            int a = p[0], b = p[1];
            if (!present[a]) { present[a] = true; distinct++; }
            if (!present[b]) { present[b] = true; distinct++; }
            adj[a][b] = adj[b][a] = true;
            degree[a]++;
            degree[b]++;
        }

        // find root candidate
        int root = -1, rootCount = 0;
        for (int i = 1; i <= MAX; i++) {
            if (!present[i]) continue;
            if (degree[i] == distinct - 1) {
                root = i;
                rootCount++;
            }
        }
        if (rootCount != 1) return 0;

        int answer = 1;
        for (int u = 1; u <= MAX; u++) {
            if (!present[u] || u == root) continue;
            int degU = degree[u];
            int parent = -1;
            boolean multiple = false;

            // iterate over neighbors v of u
            for (int v = 1; v <= MAX; v++) {
                if (!adj[u][v]) continue;
                if (degree[v] < degU) continue; // parent must have degree >= child

                // check N(u) \ {v} ⊆ N(v)
                boolean ok = true;
                for (int w = 1; w <= MAX && ok; w++) {
                    if (adj[u][w] && w != v && !adj[v][w]) {
                        ok = false;
                    }
                }

                if (ok) {
                    if (parent == -1) {
                        parent = v;
                    } else {
                        multiple = true;
                    }
                }
            }

            if (parent == -1) return 0; // no valid parent
            if (multiple) answer = 2;   // more than one possible parent leads to ambiguity
        }

        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def checkWays(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        adj = defaultdict(set)
        nodes = set()
        for u, v in pairs:
            adj[u].add(v)
            adj[v].add(u)
            nodes.add(u)
            nodes.add(v)

        n = len(nodes)
        # find root candidates (degree == n-1)
        roots = [node for node in nodes if len(adj[node]) == n - 1]
        if not roots:
            return 0
        ambiguous = False
        if len(roots) > 1:
            ambiguous = True
        root = roots[0]

        # check each non-root node for a valid parent
        for node in nodes:
            if node == root:
                continue
            possible_parents = []
            for nb in adj[node]:
                # parent must have degree >= node's and superset neighbor set
                if len(adj[nb]) >= len(adj[node]) and adj[node].issubset(adj[nb]):
                    possible_parents.append(nb)
            if not possible_parents:
                return 0
            if len(possible_parents) > 1:
                ambiguous = True

        return 2 if ambiguous else 1
```

## Python3

```python
class Solution:
    def checkWays(self, pairs):
        from collections import defaultdict

        adj = defaultdict(set)
        nodes = set()
        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)
            nodes.add(x)
            nodes.add(y)

        n = len(nodes)
        # find root candidate
        roots = [v for v in nodes if len(adj[v]) == n - 1]
        if len(roots) != 1:
            return 0
        root = roots[0]

        ambiguous = False

        for v in nodes:
            if v == root:
                continue
            deg_v = len(adj[v])
            parent = None
            min_deg = float('inf')
            # candidate parent must have degree >= deg_v
            for u in adj[v]:
                deg_u = len(adj[u])
                if deg_u >= deg_v and deg_u < min_deg:
                    parent = u
                    min_deg = deg_u
            if parent is None:
                return 0
            # verify that all neighbors of v (except parent) are also neighbors of parent
            for w in adj[v]:
                if w == parent:
                    continue
                if w not in adj[parent]:
                    return 0
            if len(adj[parent]) == deg_v:
                ambiguous = True

        return 2 if ambiguous else 1
```

## C

```c
int checkWays(int** pairs, int pairsSize, int* pairsColSize) {
    const int MAXV = 500;
    static bool adj[501][501];
    int deg[501] = {0};
    int present[501] = {0};
    int n = 0;
    
    // Build adjacency matrix and degrees
    for (int i = 0; i < pairsSize; ++i) {
        int x = pairs[i][0];
        int y = pairs[i][1];
        if (!adj[x][y]) {
            adj[x][y] = adj[y][x] = true;
            deg[x]++;
            deg[y]++;
        }
        if (!present[x]) { present[x] = 1; n++; }
        if (!present[y]) { present[y] = 1; n++; }
    }
    
    // Find root (node connected to all others)
    int root = -1, rootCnt = 0;
    for (int v = 1; v <= MAXV; ++v) {
        if (present[v] && deg[v] == n - 1) {
            root = v;
            rootCnt++;
        }
    }
    if (rootCnt != 1) return 0;
    
    // Determine parent for each non-root node
    for (int v = 1; v <= MAXV; ++v) {
        if (!present[v] || v == root) continue;
        int candidate = -1;
        for (int u = 1; u <= MAXV; ++u) {
            if (!adj[v][u]) continue;
            if (deg[u] <= deg[v]) continue; // parent must have larger degree
            // check inclusion: all neighbors of v except u are also neighbors of u
            bool ok = true;
            for (int w = 1; w <= MAXV && ok; ++w) {
                if (w == u) continue;
                if (adj[v][w] && !adj[u][w]) ok = false;
            }
            if (!ok) continue;
            if (candidate == -1) candidate = u;
            else return 2; // multiple possible parents
        }
        if (candidate == -1) return 0; // no valid parent
    }
    
    return 1;
}
```

## Csharp

```csharp
public class Solution {
    public int CheckWays(int[][] pairs) {
        var adj = new Dictionary<int, HashSet<int>>();
        foreach (var p in pairs) {
            int a = p[0], b = p[1];
            if (!adj.ContainsKey(a)) adj[a] = new HashSet<int>();
            if (!adj.ContainsKey(b)) adj[b] = new HashSet<int>();
            adj[a].Add(b);
            adj[b].Add(a);
        }

        var nodes = new List<int>(adj.Keys);
        int n = nodes.Count;

        // find root candidate
        int root = -1, rootCount = 0;
        foreach (var v in nodes) {
            if (adj[v].Count == n - 1) {
                root = v;
                rootCount++;
            }
        }
        if (rootCount != 1) return 0;

        int answer = 1; // assume unique

        foreach (var v in nodes) {
            if (v == root) continue;
            int degV = adj[v].Count;
            int parent = -1;
            int minDegParent = int.MaxValue;
            int cntMin = 0;

            foreach (int u in adj[v]) {
                int degU = adj[u].Count;
                if (degU > degV) {
                    if (degU < minDegParent) {
                        minDegParent = degU;
                        parent = u;
                        cntMin = 1;
                    } else if (degU == minDegParent) {
                        cntMin++;
                    }
                }
            }

            if (parent == -1) return 0; // no valid parent

            if (cntMin > 1) answer = 2; // ambiguous parent choice

            // verify that all other neighbors of v are also neighbors of the chosen parent
            foreach (int w in adj[v]) {
                if (w == parent) continue;
                if (!adj[parent].Contains(w)) return 0;
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} pairs
 * @return {number}
 */
var checkWays = function(pairs) {
    const adj = new Map();
    const addEdge = (a, b) => {
        if (!adj.has(a)) adj.set(a, new Set());
        if (!adj.has(b)) adj.set(b, new Set());
        adj.get(a).add(b);
        adj.get(b).add(a);
    };
    for (const [x, y] of pairs) addEdge(x, y);

    const nodes = Array.from(adj.keys());
    const n = nodes.length;

    // find root candidates (degree == n-1)
    const rootCandidates = [];
    for (const v of nodes) {
        if (adj.get(v).size === n - 1) rootCandidates.push(v);
    }
    if (rootCandidates.length === 0) return 0;
    let answer = 1;
    if (rootCandidates.length > 1) answer = 2; // multiple possible roots
    const root = rootCandidates[0];

    for (const v of nodes) {
        if (v === root) continue;
        const neighbors = adj.get(v);
        const degV = neighbors.size;

        let parent = null;
        let minDeg = Infinity;
        for (const u of neighbors) {
            const degU = adj.get(u).size;
            if (degU >= degV && degU < minDeg) {
                minDeg = degU;
                parent = u;
            }
        }
        if (parent === null) return 0; // no valid parent

        const parentSet = adj.get(parent);
        for (const w of neighbors) {
            if (w === parent) continue;
            if (!parentSet.has(w)) return 0; // subset condition violated
        }

        if (adj.get(parent).size === degV) answer = 2; // ambiguous parent
    }
    return answer;
};
```

## Typescript

```typescript
function checkWays(pairs: number[][]): number {
    const adj = new Map<number, Set<number>>();
    for (const [a, b] of pairs) {
        if (!adj.has(a)) adj.set(a, new Set());
        if (!adj.has(b)) adj.set(b, new Set());
        adj.get(a)!.add(b);
        adj.get(b)!.add(a);
    }

    const nodes = Array.from(adj.keys());
    const n = nodes.length;

    // find unique root (node connected to all others)
    let root = -1;
    let rootCnt = 0;
    for (const v of nodes) {
        if ((adj.get(v)!.size) === n - 1) {
            root = v;
            rootCnt++;
        }
    }
    if (rootCnt !== 1) return 0;

    let answer = 1; // 1: unique, 2: multiple

    for (const v of nodes) {
        if (v === root) continue;
        const neighV = adj.get(v)!;
        const degV = neighV.size;

        let minDeg = Infinity;
        let candidates: number[] = [];

        for (const u of neighV) {
            const degU = adj.get(u)!.size;
            if (degU < degV) continue; // parent must have degree >= child

            // check superset condition: all other neighbors of v are also neighbors of u
            let ok = true;
            for (const w of neighV) {
                if (w === u) continue;
                if (!adj.get(u)!.has(w)) {
                    ok = false;
                    break;
                }
            }
            if (!ok) continue;

            if (degU < minDeg) {
                minDeg = degU;
                candidates = [u];
            } else if (degU === minDeg) {
                candidates.push(u);
            }
        }

        if (candidates.length === 0) return 0; // no valid parent
        if (candidates.length > 1) answer = 2; // multiple possible parents
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $pairs
     * @return Integer
     */
    function checkWays($pairs) {
        $adj = [];
        foreach ($pairs as $pair) {
            [$x, $y] = $pair;
            if (!isset($adj[$x])) $adj[$x] = [];
            if (!isset($adj[$y])) $adj[$y] = [];
            $adj[$x][$y] = true;
            $adj[$y][$x] = true;
        }

        $nodes = array_keys($adj);
        $n = count($nodes);
        $deg = [];
        foreach ($adj as $node => $neighbors) {
            $deg[$node] = count($neighbors);
        }

        // find root: node connected to all others
        $root = null;
        foreach ($nodes as $node) {
            if ($deg[$node] == $n - 1) {
                if ($root !== null) return 0; // more than one possible root
                $root = $node;
            }
        }
        if ($root === null) return 0;

        $answer = 1; // 1 means unique, 2 means multiple

        foreach ($nodes as $v) {
            if ($v == $root) continue;

            $candidate = null;
            $multiple = false;

            foreach ($adj[$v] as $u => $_) { // u is a neighbor of v
                if ($deg[$u] < $deg[$v]) continue; // parent must have degree >= child

                // check that all other neighbors of v are also neighbors of u
                $ok = true;
                foreach ($adj[$v] as $w => $_2) {
                    if ($w == $u) continue;
                    if (!isset($adj[$u][$w])) {
                        $ok = false;
                        break;
                    }
                }

                if ($ok) {
                    if ($candidate === null) {
                        $candidate = $u;
                    } else {
                        // another possible parent found
                        $multiple = true;
                    }
                }
            }

            if ($candidate === null) return 0; // no valid parent

            if ($multiple) $answer = 2;
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func checkWays(_ pairs: [[Int]]) -> Int {
        var adj = [Int: Set<Int>]()
        // Build adjacency sets
        for pair in pairs {
            let a = pair[0]
            let b = pair[1]
            if adj[a] == nil { adj[a] = Set<Int>() }
            if adj[b] == nil { adj[b] = Set<Int>() }
            adj[a]!.insert(b)
            adj[b]!.insert(a)
        }
        
        let n = adj.count
        // Find root: node connected to all others
        var rootCandidates = [Int]()
        for (node, neighbors) in adj {
            if neighbors.count == n - 1 {
                rootCandidates.append(node)
            }
        }
        if rootCandidates.count != 1 { return 0 }
        let root = rootCandidates[0]
        
        var answer = 1
        
        for (node, neighbors) in adj {
            if node == root { continue }
            let deg = neighbors.count
            var parent: Int? = nil
            var minParentDeg = Int.max
            
            // Find candidate parent with minimal degree greater than current node's degree
            for nb in neighbors {
                guard let nbNeighbors = adj[nb] else { continue }
                let nd = nbNeighbors.count
                if nd > deg && nbNeighbors.contains(node) {
                    if nd < minParentDeg {
                        minParentDeg = nd
                        parent = nb
                    }
                }
            }
            
            guard let p = parent, let pNeighbors = adj[p] else { return 0 }
            
            // Verify that all other neighbors of node are also neighbors of its parent
            for nb in neighbors {
                if nb == p { continue }
                if !pNeighbors.contains(nb) {
                    return 0
                }
            }
            
            // If degrees are equal, there are multiple possible trees
            if pNeighbors.count == deg {
                answer = 2
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkWays(pairs: Array<IntArray>): Int {
        val maxNode = 500
        val adj = Array(maxNode + 1) { mutableSetOf<Int>() }
        val nodes = mutableSetOf<Int>()
        for (pair in pairs) {
            val a = pair[0]
            val b = pair[1]
            adj[a].add(b)
            adj[b].add(a)
            nodes.add(a)
            nodes.add(b)
        }
        val n = nodes.size
        var root = -1
        var rootCount = 0
        for (v in nodes) {
            if (adj[v].size == n - 1) {
                root = v
                rootCount++
            }
        }
        if (rootCount != 1) return 0

        var result = 1
        for (v in nodes) {
            if (v == root) continue
            val degV = adj[v].size
            var parent = -1
            var minDegParent = Int.MAX_VALUE
            for (u in adj[v]) {
                val degU = adj[u].size
                if (degU >= degV && degU < minDegParent) {
                    minDegParent = degU
                    parent = u
                }
            }
            if (parent == -1) return 0
            for (w in adj[v]) {
                if (w == parent) continue
                if (!adj[parent].contains(w)) return 0
            }
            if (minDegParent == degV) result = 2
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int checkWays(List<List<int>> pairs) {
    // Build adjacency sets
    final Map<int, Set<int>> adj = {};
    for (var p in pairs) {
      int x = p[0], y = p[1];
      adj.putIfAbsent(x, () => <int>{}).add(y);
      adj.putIfAbsent(y, () => <int>{}).add(x);
    }

    final List<int> nodes = adj.keys.toList();
    final int n = nodes.length;

    // Find root candidates (degree == n-1)
    List<int> roots = [];
    for (var u in nodes) {
      if ((adj[u]!.length) == n - 1) roots.add(u);
    }
    if (roots.isEmpty) return 0; // no possible root

    int answer = 1;
    if (roots.length > 1) answer = 2; // multiple possible roots
    final int root = roots[0];

    // For each node except the chosen root, determine its parent
    for (var u in nodes) {
      if (u == root) continue;
      Set<int> neighU = adj[u]!;
      int degU = neighU.length;

      int minParentDeg = 1 << 30;
      bool multipleParents = false;

      for (int v in neighU) {
        Set<int> neighV = adj[v]!;

        // parent must have degree >= child's degree
        if (neighV.length < degU) continue;

        // Check that all neighbors of u except v are also neighbors of v
        bool ok = true;
        for (int w in neighU) {
          if (w == v) continue;
          if (!neighV.contains(w)) {
            ok = false;
            break;
          }
        }
        if (!ok) continue;

        int degV = neighV.length;
        if (degV < minParentDeg) {
          minParentDeg = degV;
          multipleParents = false;
        } else if (degV == minParentDeg) {
          multipleParents = true;
        }
      }

      if (minParentDeg == (1 << 30)) return 0; // no valid parent
      if (multipleParents) answer = 2;
    }

    return answer;
  }
}
```

## Golang

```go
func checkWays(pairs [][]int) int {
	adj := make(map[int]map[int]bool)
	for _, p := range pairs {
		a, b := p[0], p[1]
		if adj[a] == nil {
			adj[a] = make(map[int]bool)
		}
		if adj[b] == nil {
			adj[b] = make(map[int]bool)
		}
		adj[a][b] = true
		adj[b][a] = true
	}

	deg := make(map[int]int, len(adj))
	for v, nb := range adj {
		deg[v] = len(nb)
	}
	n := len(adj)

	rootCnt, root := 0, -1
	for v, d := range deg {
		if d == n-1 {
			rootCnt++
			root = v
		}
	}
	if rootCnt != 1 {
		return 0
	}

	ans := 1
	for v := range adj {
		if v == root {
			continue
		}
		candidates := 0
		for u := range adj[v] {
			if deg[u] <= deg[v] {
				continue
			}
			ok := true
			for w := range adj[v] {
				if w == u {
					continue
				}
				if !adj[u][w] {
					ok = false
					break
				}
			}
			if ok {
				candidates++
			}
		}
		if candidates == 0 {
			return 0
		}
		if candidates > 1 {
			ans = 2
		}
	}
	return ans
}
```

## Ruby

```ruby
def check_ways(pairs)
  adj = Hash.new { |h, k| h[k] = [] }
  pairs.each do |x, y|
    adj[x] << y
    adj[y] << x
  end

  nodes = adj.keys
  n = nodes.size

  # find root: must be connected to all other nodes
  roots = nodes.select { |v| adj[v].size == n - 1 }
  return 0 unless roots.size == 1
  root = roots[0]

  # map node to bit index for mask representation
  idx = {}
  nodes.each_with_index { |v, i| idx[v] = i }

  masks = {}
  nodes.each do |v|
    m = 0
    adj[v].each { |nbr| m |= (1 << idx[nbr]) }
    masks[v] = m
  end

  multiple = false

  nodes.each do |v|
    next if v == root
    best_parent = nil
    ambiguous = false
    adj[v].each do |u|
      # parent must have degree >= child's and contain all child's neighbors
      if adj[u].size >= adj[v].size && (masks[v] & ~masks[u]).zero?
        if best_parent.nil? || adj[u].size < adj[best_parent].size
          best_parent = u
          ambiguous = false
        elsif adj[u].size == adj[best_parent].size
          ambiguous = true
        end
      end
    end
    return 0 if best_parent.nil?
    multiple ||= ambiguous
  end

  multiple ? 2 : 1
end
```

## Scala

```scala
object Solution {
  def checkWays(pairs: Array[Array[Int]]): Int = {
    import scala.collection.mutable.{Map => MutableMap, Set => MutableSet}
    val adjMut = MutableMap.empty[Int, MutableSet[Int]]
    for (p <- pairs) {
      val a = p(0)
      val b = p(1)
      adjMut.getOrElseUpdate(a, MutableSet.empty) += b
      adjMut.getOrElseUpdate(b, MutableSet.empty) += a
    }
    val nodes = adjMut.keys.toArray
    val n = nodes.length
    // immutable adjacency for fast lookups
    val adj: Map[Int, Set[Int]] = adjMut.map { case (k, s) => k -> s.toSet }.toMap

    // find possible roots (connected to all other nodes)
    val rootCandidates = nodes.filter(v => adj(v).size == n - 1)
    if (rootCandidates.isEmpty) return 0
    var answer = if (rootCandidates.length > 1) 2 else 1
    val root = rootCandidates.head

    for (v <- nodes if v != root) {
      val neigh = adj(v)
      var parentOpt: Option[Int] = None
      var minDeg = Int.MaxValue
      // try each neighbor as possible parent
      for (u <- neigh) {
        val candSet = adj(u)
        var ok = true
        // all neighbors of v except possibly u must be in candSet
        for (w <- neigh if w != u && !candSet.contains(w)) {
          ok = false
        }
        if (ok) {
          val degU = candSet.size
          if (degU < minDeg) {
            minDeg = degU
            parentOpt = Some(u)
          }
        }
      }
      if (parentOpt.isEmpty) return 0
      // if child and its parent have same degree, multiple ways exist
      if (adj(parentOpt.get).size == neigh.size) answer = 2
    }
    answer
  }
}
```

## Rust

```rust
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn check_ways(pairs: Vec<Vec<i32>>) -> i32 {
        // collect distinct node labels
        let mut label_set = HashSet::new();
        for p in &pairs {
            label_set.insert(p[0]);
            label_set.insert(p[1]);
        }
        let n = label_set.len();
        if n == 0 {
            return 0;
        }

        // map each label to a compact index
        let mut id_map: HashMap<i32, usize> = HashMap::new();
        let mut labels = Vec::with_capacity(n);
        for &v in label_set.iter() {
            let idx = labels.len();
            id_map.insert(v, idx);
            labels.push(v);
        }
        let m = labels.len();

        // adjacency sets built from pairs
        let mut neigh: Vec<HashSet<usize>> = vec![HashSet::new(); m];
        for p in pairs {
            let a = *id_map.get(&p[0]).unwrap();
            let b = *id_map.get(&p[1]).unwrap();
            neigh[a].insert(b);
            neigh[b].insert(a);
        }

        // degree (size of neighbor set) for each node
        let mut deg: Vec<usize> = neigh.iter().map(|s| s.len()).collect();

        // find the unique root: must be connected to all other nodes
        let mut root_idx_opt = None;
        for i in 0..m {
            if deg[i] == m - 1 {
                if root_idx_opt.is_some() {
                    return 0; // more than one possible root
                }
                root_idx_opt = Some(i);
            }
        }
        let root_idx = match root_idx_opt {
            Some(v) => v,
            None => return 0, // no node connected to all others
        };

        // process nodes in increasing degree order (excluding root)
        let mut order: Vec<usize> = (0..m).collect();
        order.sort_by_key(|&i| deg[i]);

        let mut multiple = false;

        for &v in &order {
            if v == root_idx {
                continue;
            }
            // find parent among neighbors with larger degree and whose neighbor set is a superset
            let mut best_parent: Option<usize> = None;
            let mut min_deg = usize::MAX;
            for &u in &neigh[v] {
                if deg[u] <= deg[v] {
                    continue; // cannot be ancestor
                }
                // check if neigh[v] ⊆ neigh[u]
                let mut subset = true;
                for &x in &neigh[v] {
                    if !neigh[u].contains(&x) {
                        subset = false;
                        break;
                    }
                }
                if subset {
                    if deg[u] < min_deg {
                        min_deg = deg[u];
                        best_parent = Some(u);
                        multiple = false; // reset ambiguity for this node
                    } else if deg[u] == min_deg {
                        multiple = true; // another candidate with same minimal degree
                    }
                }
            }
            if best_parent.is_none() {
                return 0; // cannot find a valid parent
            }
        }

        if multiple { 2 } else { 1 }
    }
}
```

## Racket

```racket
(require racket/set)

(define/contract (check-ways pairs)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let/ec return
    (define adj (make-hash))
    (for ([p pairs])
      (match p
        [(list a b)
         (hash-update! adj a (lambda (s) (set-add s b)) (set))
         (hash-update! adj b (lambda (s) (set-add s a)) (set))]))
    (define nodes (hash-keys adj))
    (define n (length nodes))
    ;; find root
    (define roots
      (filter (lambda (v)
                (= (set-count (hash-ref adj v)) (- n 1)))
              nodes))
    (unless (= (length roots) 1)
      (return 0))
    (define root (car roots))
    (define deg (make-hash))
    (for ([v nodes])
      (hash-set! deg v (set-count (hash-ref adj v))))
    (define ans 1)
    (for ([v nodes] #:when (not (= v root)))
      (define deg-v (hash-ref deg v))
      (define min-parent-degree +inf.0)
      (for ([u (in-set (hash-ref adj v))])
        (define deg-u (hash-ref deg u))
        (when (>= deg-u deg-v)
          (set! min-parent-degree (min min-parent-degree deg-u))))
      (if (= min-parent-degree +inf.0)
          (return 0)
          (let ([cnt (for/sum ([u (in-set (hash-ref adj v))]
                               #:when (and (>= (hash-ref deg u) deg-v)
                                           (= (hash-ref deg u) min-parent-degree)))
                       1)])
            (cond
              [(= cnt 0) (return 0)]
              [(> cnt 1) (set! ans 2)]))))
    ans))
```

## Erlang

```erlang
-spec check_ways(Pairs :: [[integer()]]) -> integer().
check_ways(Pairs) ->
    Adj = build_adj(Pairs),
    Nodes = maps:keys(Adj),
    N = length(Nodes),
    Degrees = maps:map(fun(_Node, Set) -> maps:size(Set) end, Adj),

    RootCandidates = [Node || Node <- Nodes,
        maps:get(Node, Degrees) == N - 1],
    case RootCandidates of
        [_Root] ->
            Root = hd(RootCandidates),
            process_nodes(Nodes, Root, Adj, Degrees);
        _ -> 0
    end.

build_adj(Pairs) ->
    lists:foldl(fun([X, Y], Acc) ->
        Acc1 = add_edge(X, Y, Acc),
        add_edge(Y, X, Acc1)
    end, #{}, Pairs).

add_edge(From, To, Map) ->
    Set = maps:get(From, Map, #{}),
    NewSet = maps:put(To, true, Set),
    maps:put(From, NewSet, Map).

process_nodes(Nodes, Root, Adj, Degrees) ->
    lists:foldl(fun(Node, AccAns) ->
        case AccAns of
            0 -> 0; % already invalid
            _ ->
                if Node == Root ->
                        AccAns;
                   true ->
                        DegV = maps:get(Node, Degrees),
                        NeighSet = maps:get(Node, Adj),
                        NeighborList = maps:keys(NeighSet),

                        Candidates = [U || U <- NeighborList,
                            maps:get(U, Degrees) > DegV],
                        case Candidates of
                            [] -> 0; % no possible parent
                            _ ->
                                MinDeg = lists:min([maps:get(C, Degrees) || C <- Candidates]),
                                ParentCands = [U || U <- Candidates,
                                    maps:get(U, Degrees) == MinDeg],
                                NewAns = if length(ParentCands) > 1 -> 2; true -> AccAns end,
                                Parent = hd(ParentCands),
                                ParentSet = maps:get(Parent, Adj),

                                Valid = lists:all(fun(W) ->
                                    W == Parent orelse maps:is_key(W, ParentSet)
                                end, NeighborList),

                                if Valid -> NewAns; true -> 0 end
                        end
                end
        end
    end, 1, Nodes).
```

## Elixir

```elixir
defmodule Solution do
  @spec check_ways(pairs :: [[integer]]) :: integer
  def check_ways(pairs) do
    adj =
      Enum.reduce(pairs, %{}, fn [a, b], acc ->
        acc
        |> Map.update(a, MapSet.new([b]), &MapSet.put(&1, b))
        |> Map.update(b, MapSet.new([a]), &MapSet.put(&1, a))
      end)

    nodes = Map.keys(adj)
    n = length(nodes)

    if n == 0 do
      0
    else
      size_map =
        Enum.into(nodes, %{}, fn v ->
          {v, MapSet.size(Map.get(adj, v))}
        end)

      root_candidates =
        Enum.filter(nodes, fn v ->
          MapSet.size(Map.get(adj, v)) == n - 1
        end)

      if length(root_candidates) == 0 do
        0
      else
        init_res = if length(root_candidates) > 1, do: 2, else: 1

        {final_res, valid} =
          Enum.reduce_while(nodes, {init_res, true}, fn v, {res, _} ->
            if Enum.member?(root_candidates, v) do
              {:cont, {res, true}}
            else
              neigh = Map.get(adj, v)
              size_v = size_map[v]

              candidates =
                Enum.filter(MapSet.to_list(neigh), fn u ->
                  size_u = size_map[u]
                  size_u >= size_v and MapSet.subset?(neigh, Map.get(adj, u))
                end)

              if candidates == [] do
                {:halt, {0, false}}
              else
                min_size =
                  candidates
                  |> Enum.map(&size_map[&1])
                  |> Enum.min()

                min_cands = Enum.filter(candidates, fn u -> size_map[u] == min_size end)
                new_res = if length(min_cands) > 1, do: max(res, 2), else: res
                {:cont, {new_res, true}}
              end
            end
          end)

        if valid, do: final_res, else: 0
      end
    end
  end
end
```

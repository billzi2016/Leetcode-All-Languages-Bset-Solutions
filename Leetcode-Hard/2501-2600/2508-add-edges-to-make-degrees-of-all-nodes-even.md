# 2508. Add Edges to Make Degrees of All Nodes Even

## Cpp

```cpp
class Solution {
public:
    bool isPossible(int n, vector<vector<int>>& edges) {
        vector<int> deg(n + 1, 0);
        unordered_set<long long> edgeSet;
        edgeSet.reserve(edges.size() * 2);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            ++deg[u];
            ++deg[v];
            if (u > v) swap(u, v);
            long long key = ((long long)u << 32) | v;
            edgeSet.insert(key);
        }
        auto hasEdge = [&](int x, int y)->bool{
            if (x > y) swap(x, y);
            long long key = ((long long)x << 32) | y;
            return edgeSet.find(key) != edgeSet.end();
        };
        
        vector<int> odd;
        for (int i = 1; i <= n; ++i)
            if (deg[i] % 2) odd.push_back(i);
        
        int m = odd.size();
        if (m == 0) return true;
        if (m != 2 && m != 4) return false;
        
        if (m == 2) {
            int u = odd[0], v = odd[1];
            if (!hasEdge(u, v)) return true; // add directly
            // try a third node w
            for (int w = 1; w <= n; ++w) {
                if (w == u || w == v) continue;
                if (!hasEdge(u, w) && !hasEdge(v, w))
                    return true;
            }
            return false;
        } else { // m == 4
            int a = odd[0], b = odd[1], c = odd[2], d = odd[3];
            vector<pair<int,int>> opts = {
                {a,b}, {c,d},
                {a,c}, {b,d},
                {a,d}, {b,c}
            };
            // check three pairings
            for (int i = 0; i < 6; i += 2) {
                if (!hasEdge(opts[i].first, opts[i].second) &&
                    !hasEdge(opts[i+1].first, opts[i+1].second))
                    return true;
            }
            return false;
        }
    }
};
```

## Java

```java
class Solution {
    public boolean isPossible(int n, List<List<Integer>> edges) {
        int[] degree = new int[n + 1];
        java.util.HashSet<Long> edgeSet = new java.util.HashSet<>(edges.size() * 2);
        for (List<Integer> e : edges) {
            int u = e.get(0);
            int v = e.get(1);
            degree[u]++;
            degree[v]++;
            if (u > v) { int tmp = u; u = v; v = tmp; }
            long key = ((long) u << 32) | v;
            edgeSet.add(key);
        }

        java.util.ArrayList<Integer> odd = new java.util.ArrayList<>(4);
        for (int i = 1; i <= n; i++) {
            if ((degree[i] & 1) == 1) odd.add(i);
        }

        int cnt = odd.size();
        if (cnt == 0) return true;
        if (cnt % 2 != 0 || cnt > 4) return false;

        java.util.function.BiPredicate<Integer, Integer> hasEdge = (a, b) -> {
            if (a > b) { int tmp = a; a = b; b = tmp; }
            long key = ((long) a << 32) | b;
            return edgeSet.contains(key);
        };

        if (cnt == 2) {
            int a = odd.get(0), b = odd.get(1);
            // one edge directly
            if (!hasEdge.test(a, b)) return true;
            // try to use an intermediate node
            for (int c = 1; c <= n; c++) {
                if (c == a || c == b) continue;
                if (!hasEdge.test(a, c) && !hasEdge.test(b, c)) return true;
            }
            return false;
        }

        // cnt == 4
        int o0 = odd.get(0), o1 = odd.get(1), o2 = odd.get(2), o3 = odd.get(3);
        // three possible pairings
        if (!hasEdge.test(o0, o1) && !hasEdge.test(o2, o3)) return true;
        if (!hasEdge.test(o0, o2) && !hasEdge.test(o1, o3)) return true;
        if (!hasEdge.test(o0, o3) && !hasEdge.test(o1, o2)) return true;
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def isPossible(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        deg = [0] * (n + 1)
        edge_set = set()
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            if u > v:
                u, v = v, u
            edge_set.add((u, v))

        odd_nodes = [i for i in range(1, n + 1) if deg[i] % 2 == 1]
        k = len(odd_nodes)

        if k == 0:
            return True

        if k == 2:
            a, b = odd_nodes
            u, v = (a, b) if a < b else (b, a)
            # direct edge possible?
            if (u, v) not in edge_set:
                return True
            # try to use an intermediate node
            for x in range(1, n + 1):
                if x == a or x == b:
                    continue
                e1 = (a, x) if a < x else (x, a)
                e2 = (b, x) if b < x else (x, b)
                if e1 not in edge_set and e2 not in edge_set:
                    return True
            return False

        if k == 4:
            a, b, c, d = odd_nodes
            pairings = [
                ((a, b), (c, d)),
                ((a, c), (b, d)),
                ((a, d), (b, c))
            ]
            for (p1, p2) in pairings:
                u1, v1 = p1
                u2, v2 = p2
                e1 = (u1, v1) if u1 < v1 else (v1, u1)
                e2 = (u2, v2) if u2 < v2 else (v2, u2)
                if e1 not in edge_set and e2 not in edge_set:
                    return True
            return False

        # any other number of odd-degree nodes cannot be fixed with ≤2 edges
        return False
```

## Python3

```python
import sys
from typing import List

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        deg = [0] * (n + 1)
        edge_set = set()
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            if u > v:
                u, v = v, u
            edge_set.add((u, v))

        odd = [i for i in range(1, n + 1) if deg[i] % 2 == 1]
        m = len(odd)
        if m == 0:
            return True
        if m > 4:
            return False

        def edge_missing(a: int, b: int) -> bool:
            if a > b:
                a, b = b, a
            return (a, b) not in edge_set

        if m == 2:
            a, b = odd[0], odd[1]
            if edge_missing(a, b):
                return True
            # try a common third node
            for x in range(1, n + 1):
                if x == a or x == b:
                    continue
                if edge_missing(a, x) and edge_missing(b, x):
                    return True
            return False

        # m == 4
        o0, o1, o2, o3 = odd
        pairings = [
            ((o0, o1), (o2, o3)),
            ((o0, o2), (o1, o3)),
            ((o0, o3), (o1, o2))
        ]
        for (p1, p2) in pairings:
            if edge_missing(*p1) and edge_missing(*p2):
                return True
        return False
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static int cmpLong(const void *a, const void *b) {
    long long la = *(const long long *)a;
    long long lb = *(const long long *)b;
    if (la < lb) return -1;
    if (la > lb) return 1;
    return 0;
}

static bool hasEdge(int u, int v, const long long *arr, int size) {
    if (u == v) return false;
    int a = u < v ? u : v;
    int b = u < v ? v : u;
    long long code = ((long long)a << 32) | (unsigned int)b;
    return bsearch(&code, arr, size, sizeof(long long), cmpLong) != NULL;
}

bool isPossible(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize; // unused
    int *degree = (int *)calloc(n + 1, sizeof(int));
    long long *edgeArr = (long long *)malloc(edgesSize * sizeof(long long));

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        degree[u]++; degree[v]++;
        int a = u < v ? u : v;
        int b = u < v ? v : u;
        edgeArr[i] = ((long long)a << 32) | (unsigned int)b;
    }

    qsort(edgeArr, edgesSize, sizeof(long long), cmpLong);

    int odds[4];
    int oddCnt = 0;
    for (int i = 1; i <= n; ++i) {
        if (degree[i] & 1) {
            if (oddCnt < 4) odds[oddCnt] = i;
            oddCnt++;
        }
    }

    free(degree);
    bool result = false;

    if (oddCnt == 0) {
        result = true;
    } else if (oddCnt == 2) {
        int a = odds[0], b = odds[1];
        if (!hasEdge(a, b, edgeArr, edgesSize)) {
            result = true;
        } else {
            for (int c = 1; c <= n; ++c) {
                if (c == a || c == b) continue;
                if (!hasEdge(a, c, edgeArr, edgesSize) && !hasEdge(b, c, edgeArr, edgesSize)) {
                    result = true;
                    break;
                }
            }
        }
    } else if (oddCnt == 4) {
        int a = odds[0], b = odds[1], c = odds[2], d = odds[3];
        // pairing 1: (a,b) (c,d)
        if (!hasEdge(a, b, edgeArr, edgesSize) && !hasEdge(c, d, edgeArr, edgesSize))
            result = true;
        // pairing 2: (a,c) (b,d)
        else if (!hasEdge(a, c, edgeArr, edgesSize) && !hasEdge(b, d, edgeArr, edgesSize))
            result = true;
        // pairing 3: (a,d) (b,c)
        else if (!hasEdge(a, d, edgeArr, edgesSize) && !hasEdge(b, c, edgeArr, edgesSize))
            result = true;
    } else {
        result = false;
    }

    free(edgeArr);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsPossible(int n, IList<IList<int>> edges) {
        int[] degree = new int[n + 1];
        var edgeSet = new HashSet<long>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            degree[u]++; degree[v]++;
            AddEdge(edgeSet, u, v);
        }

        var oddNodes = new List<int>();
        for (int i = 1; i <= n; i++) {
            if ((degree[i] & 1) == 1) oddNodes.Add(i);
        }

        int oddCnt = oddNodes.Count;
        if (oddCnt == 0) return true;
        if (oddCnt > 4 || (oddCnt & 1) == 1) return false;

        if (oddCnt == 2) {
            int a = oddNodes[0], b = oddNodes[1];
            if (!HasEdge(edgeSet, a, b)) return true; // direct edge possible

            // try to use an intermediate node
            for (int c = 1; c <= n; c++) {
                if (c == a || c == b) continue;
                if (!HasEdge(edgeSet, a, c) && !HasEdge(edgeSet, b, c))
                    return true;
            }
            return false;
        }

        // oddCnt == 4
        int x = oddNodes[0], y = oddNodes[1], z = oddNodes[2], w = oddNodes[3];
        if (!HasEdge(edgeSet, x, y) && !HasEdge(edgeSet, z, w)) return true;
        if (!HasEdge(edgeSet, x, z) && !HasEdge(edgeSet, y, w)) return true;
        if (!HasEdge(edgeSet, x, w) && !HasEdge(edgeSet, y, z)) return true;
        return false;
    }

    private static void AddEdge(HashSet<long> set, int u, int v) {
        int a = Math.Min(u, v), b = Math.Max(u, v);
        long key = ((long)a << 32) | (uint)b;
        set.Add(key);
    }

    private static bool HasEdge(HashSet<long> set, int u, int v) {
        int a = Math.Min(u, v), b = Math.Max(u, v);
        long key = ((long)a << 32) | (uint)b;
        return set.Contains(key);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {boolean}
 */
var isPossible = function(n, edges) {
    const degree = new Array(n + 1).fill(0);
    const edgeSet = new Set();
    
    for (const [a, b] of edges) {
        degree[a]++;
        degree[b]++;
        const key = a < b ? `${a}#${b}` : `${b}#${a}`;
        edgeSet.add(key);
    }
    
    const odd = [];
    for (let i = 1; i <= n; ++i) {
        if (degree[i] % 2 === 1) odd.push(i);
    }
    
    const m = odd.length;
    if (m === 0) return true;
    if (m !== 2 && m !== 4) return false;
    
    // helper to check edge existence
    const hasEdge = (u, v) => {
        const key = u < v ? `${u}#${v}` : `${v}#${u}`;
        return edgeSet.has(key);
    };
    
    if (m === 2) {
        const [u, v] = odd;
        // direct connection possible?
        if (!hasEdge(u, v)) return true;
        // try to find a third node x not connected to either u or v
        for (let x = 1; x <= n; ++x) {
            if (x === u || x === v) continue;
            if (!hasEdge(u, x) && !hasEdge(v, x)) return true;
        }
        return false;
    }
    
    // m === 4
    const [a, b, c, d] = odd;
    const canPair = (p1, p2, q1, q2) => {
        return !hasEdge(p1, p2) && !hasEdge(q1, q2);
    };
    
    if (canPair(a, b, c, d)) return true;
    if (canPair(a, c, b, d)) return true;
    if (canPair(a, d, b, c)) return true;
    
    return false;
};
```

## Typescript

```typescript
function isPossible(n: number, edges: number[][]): boolean {
    const base = n + 1;
    const edgeSet = new Set<number>();
    const oddParity = new Uint8Array(n + 1);
    
    for (const [uRaw, vRaw] of edges) {
        const u = Math.min(uRaw, vRaw);
        const v = Math.max(uRaw, vRaw);
        edgeSet.add(u * base + v);
        oddParity[uRaw] ^= 1;
        oddParity[vRaw] ^= 1;
    }
    
    const odds: number[] = [];
    for (let i = 1; i <= n; ++i) {
        if (oddParity[i]) odds.push(i);
    }
    
    const hasEdge = (a: number, b: number): boolean => {
        const u = Math.min(a, b);
        const v = Math.max(a, b);
        return edgeSet.has(u * base + v);
    };
    
    if (odds.length === 0) return true;
    
    if (odds.length === 2) {
        const [a, b] = odds;
        if (!hasEdge(a, b)) return true;
        for (let c = 1; c <= n; ++c) {
            if (c === a || c === b) continue;
            if (!hasEdge(a, c) && !hasEdge(b, c)) return true;
        }
        return false;
    }
    
    if (odds.length === 4) {
        const o = odds;
        const pairings: [number, number][][] = [
            [[o[0], o[1]], [o[2], o[3]]],
            [[o[0], o[2]], [o[1], o[3]]],
            [[o[0], o[3]], [o[1], o[2]]],
        ];
        for (const p of pairings) {
            const e1 = p[0];
            const e2 = p[1];
            if (!hasEdge(e1[0], e1[1]) && !hasEdge(e2[0], e2[1])) return true;
        }
        return false;
    }
    
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Boolean
     */
    function isPossible($n, $edges) {
        $deg = array_fill(0, $n + 1, 0);
        $adj = [];

        foreach ($edges as $e) {
            [$u, $v] = $e;
            $deg[$u]++;
            $deg[$v]++;
            if ($u > $v) { $tmp = $u; $u = $v; $v = $tmp; }
            $adj[$u . '#' . $v] = true;
        }

        $odd = [];
        for ($i = 1; $i <= $n; $i++) {
            if (($deg[$i] & 1) === 1) {
                $odd[] = $i;
            }
        }

        $cnt = count($odd);
        if ($cnt === 0) return true;

        if ($cnt === 2) {
            [$a, $b] = $odd;
            $keyAB = (min($a, $b)) . '#' . (max($a, $b));
            if (!isset($adj[$keyAB])) {
                return true; // add edge directly
            }
            // try to use a third node x
            for ($x = 1; $x <= $n; $x++) {
                if ($x === $a || $x === $b) continue;
                $keyAX = (min($a, $x)) . '#' . (max($a, $x));
                $keyBX = (min($b, $x)) . '#' . (max($b, $x));
                if (!isset($adj[$keyAX]) && !isset($adj[$keyBX])) {
                    return true;
                }
            }
            return false;
        }

        if ($cnt === 4) {
            [$a, $b, $c, $d] = $odd;
            $pairings = [
                [[$a, $b], [$c, $d]],
                [[$a, $c], [$b, $d]],
                [[$a, $d], [$b, $c]]
            ];
            foreach ($pairings as $p) {
                [$e1, $e2] = $p;
                $key1 = (min($e1[0], $e1[1])) . '#' . (max($e1[0], $e1[1]));
                $key2 = (min($e2[0], $e2[1])) . '#' . (max($e2[0], $e2[1]));
                if (!isset($adj[$key1]) && !isset($adj[$key2])) {
                    return true;
                }
            }
            return false;
        }

        // any other number of odd-degree nodes cannot be fixed with ≤2 edges
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func isPossible(_ n: Int, _ edges: [[Int]]) -> Bool {
        var degree = [Int](repeating: 0, count: n + 1)
        let base: Int64 = 100_001 // greater than max n
        var edgeSet = Set<Int64>()
        
        for e in edges {
            let u = e[0]
            let v = e[1]
            degree[u] += 1
            degree[v] += 1
            let a = min(u, v)
            let b = max(u, v)
            let key = Int64(a) * base + Int64(b)
            edgeSet.insert(key)
        }
        
        func hasEdge(_ u: Int, _ v: Int) -> Bool {
            let a = min(u, v)
            let b = max(u, v)
            let key = Int64(a) * base + Int64(b)
            return edgeSet.contains(key)
        }
        
        var oddNodes = [Int]()
        for i in 1...n {
            if degree[i] % 2 == 1 {
                oddNodes.append(i)
            }
        }
        
        let oddCount = oddNodes.count
        if oddCount == 0 { return true }
        if oddCount > 4 || oddCount % 2 == 1 { return false }
        
        if oddCount == 2 {
            let a = oddNodes[0]
            let b = oddNodes[1]
            if !hasEdge(a, b) { return true }
            // try to find a third node c
            for c in 1...n where c != a && c != b {
                if !hasEdge(a, c) && !hasEdge(b, c) {
                    return true
                }
            }
            return false
        }
        
        // oddCount == 4
        let o = oddNodes
        let pairings = [
            [(o[0], o[1]), (o[2], o[3])],
            [(o[0], o[2]), (o[1], o[3])],
            [(o[0], o[3]), (o[1], o[2])]
        ]
        
        for pairing in pairings {
            let e1 = pairing[0]
            let e2 = pairing[1]
            if !hasEdge(e1.0, e1.1) && !hasEdge(e2.0, e2.1) {
                return true
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPossible(n: Int, edges: List<List<Int>>): Boolean {
        val degree = IntArray(n + 1)
        val edgeSet = HashSet<Long>(edges.size * 2)

        fun encode(a: Int, b: Int): Long {
            val x = if (a < b) a else b
            val y = if (a < b) b else a
            return (x.toLong() shl 32) or y.toLong()
        }

        for (e in edges) {
            val u = e[0]
            val v = e[1]
            degree[u]++
            degree[v]++
            edgeSet.add(encode(u, v))
        }

        val odds = mutableListOf<Int>()
        for (i in 1..n) {
            if ((degree[i] and 1) == 1) odds.add(i)
        }

        when (odds.size) {
            0 -> return true
            2 -> {
                val a = odds[0]
                val b = odds[1]
                // direct edge possible
                if (!edgeSet.contains(encode(a, b))) return true
                // try to use an intermediate node
                for (x in 1..n) {
                    if (x == a || x == b) continue
                    if (!edgeSet.contains(encode(a, x)) && !edgeSet.contains(encode(b, x))) {
                        return true
                    }
                }
                return false
            }
            4 -> {
                // check three possible pairings of the four odd nodes
                fun ok(i1: Int, i2: Int, j1: Int, j2: Int): Boolean {
                    return !edgeSet.contains(encode(odds[i1], odds[i2])) &&
                           !edgeSet.contains(encode(odds[j1], odds[j2]))
                }
                if (ok(0, 1, 2, 3) || ok(0, 2, 1, 3) || ok(0, 3, 1, 2)) return true
                return false
            }
            else -> return false
        }
    }
}
```

## Dart

```dart
class Solution {
  bool isPossible(int n, List<List<int>> edges) {
    var deg = List.filled(n + 1, 0);
    var edgeSet = <int>{};

    int encode(int a, int b) {
      if (a > b) {
        int t = a;
        a = b;
        b = t;
      }
      return a * (n + 1) + b;
    }

    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      deg[u]++;
      deg[v]++;
      edgeSet.add(encode(u, v));
    }

    List<int> odd = [];
    for (int i = 1; i <= n; i++) {
      if ((deg[i] & 1) == 1) odd.add(i);
    }

    int o = odd.length;
    if (o == 0) return true;
    if (o % 2 == 1 || o > 4) return false;

    if (o == 2) {
      int u = odd[0], v = odd[1];
      if (!edgeSet.contains(encode(u, v))) return true;
      for (int w = 1; w <= n; w++) {
        if (w == u || w == v) continue;
        if (!edgeSet.contains(encode(u, w)) &&
            !edgeSet.contains(encode(v, w))) {
          return true;
        }
      }
      return false;
    } else { // o == 4
      int a = odd[0], b = odd[1], c = odd[2], d = odd[3];
      List<List<int>> pairings = [
        [a, b, c, d],
        [a, c, b, d],
        [a, d, b, c]
      ];
      for (var p in pairings) {
        int x1 = p[0], y1 = p[1], x2 = p[2], y2 = p[3];
        if (!edgeSet.contains(encode(x1, y1)) &&
            !edgeSet.contains(encode(x2, y2))) {
          return true;
        }
      }
      return false;
    }
  }
}
```

## Golang

```go
func isPossible(n int, edges [][]int) bool {
    deg := make([]int, n+1)
    edgeSet := make(map[int64]struct{}, len(edges))
    for _, e := range edges {
        u, v := e[0], e[1]
        deg[u]++
        deg[v]++
        if u > v {
            u, v = v, u
        }
        key := int64(u)<<32 | int64(v)
        edgeSet[key] = struct{}{}
    }

    odds := []int{}
    for i := 1; i <= n; i++ {
        if deg[i]%2 == 1 {
            odds = append(odds, i)
        }
    }

    switch len(odds) {
    case 0:
        return true
    case 2:
        u, v := odds[0], odds[1]
        a, b := u, v
        if a > b {
            a, b = b, a
        }
        key := int64(a)<<32 | int64(b)
        if _, ok := edgeSet[key]; !ok {
            return true
        }
        for x := 1; x <= n; x++ {
            if x == u || x == v {
                continue
            }
            a, b = u, x
            if a > b {
                a, b = b, a
            }
            key1 := int64(a)<<32 | int64(b)
            if _, ok := edgeSet[key1]; ok {
                continue
            }
            a, b = v, x
            if a > b {
                a, b = b, a
            }
            key2 := int64(a)<<32 | int64(b)
            if _, ok := edgeSet[key2]; ok {
                continue
            }
            return true
        }
        return false
    case 4:
        a, b, c, d := odds[0], odds[1], odds[2], odds[3]
        check := func(x, y int) bool {
            if x > y {
                x, y = y, x
            }
            key := int64(x)<<32 | int64(y)
            _, ok := edgeSet[key]
            return !ok
        }
        if check(a, b) && check(c, d) {
            return true
        }
        if check(a, c) && check(b, d) {
            return true
        }
        if check(a, d) && check(b, c) {
            return true
        }
        return false
    default:
        return false
    }
}
```

## Ruby

```ruby
def is_possible(n, edges)
  deg_parity = Array.new(n + 1, 0)
  adj = Array.new(n + 1) { {} }

  edges.each do |u, v|
    deg_parity[u] ^= 1
    deg_parity[v] ^= 1
    adj[u][v] = true
    adj[v][u] = true
  end

  odd_nodes = []
  (1..n).each { |i| odd_nodes << i if deg_parity[i] == 1 }

  case odd_nodes.size
  when 0
    true
  when 2
    a, b = odd_nodes
    return true unless adj[a].key?(b) # can connect directly

    (1..n).each do |c|
      next if c == a || c == b
      unless adj[a].key?(c) || adj[b].key?(c)
        return true
      end
    end
    false
  when 4
    a, b, c, d = odd_nodes
    matchings = [
      [[a, b], [c, d]],
      [[a, c], [b, d]],
      [[a, d], [b, c]]
    ]

    matchings.any? do |e1, e2|
      !adj[e1[0]].key?(e1[1]) && !adj[e2[0]].key?(e2[1])
    end
  else
    false
  end
end
```

## Scala

```scala
object Solution {
    def isPossible(n: Int, edges: List[List[Int]]): Boolean = {
        val deg = new Array[Int](n + 1)
        val edgeSet = scala.collection.mutable.HashSet[Long]()
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            deg(u) += 1
            deg(v) += 1
            val a = math.min(u, v)
            val b = math.max(u, v)
            edgeSet.add((a.toLong << 32) | b.toLong)
        }
        def hasEdge(u: Int, v: Int): Boolean = {
            val a = math.min(u, v)
            val b = math.max(u, v)
            edgeSet.contains((a.toLong << 32) | b.toLong)
        }

        val odd = scala.collection.mutable.ArrayBuffer[Int]()
        var i = 1
        while (i <= n) {
            if ((deg(i) & 1) == 1) odd += i
            i += 1
        }
        odd.length match {
            case 0 => true
            case 2 =>
                val a = odd(0)
                val b = odd(1)
                if (!hasEdge(a, b)) true
                else {
                    var x = 1
                    while (x <= n) {
                        if (x != a && x != b && !hasEdge(a, x) && !hasEdge(b, x))
                            return true
                        x += 1
                    }
                    false
                }
            case 4 =>
                val o = odd.toArray
                // three possible pairings
                def check(p1: (Int, Int), p2: (Int, Int)): Boolean = {
                    !hasEdge(p1._1, p1._2) && !hasEdge(p2._1, p2._2)
                }
                if (check((o(0), o(1)), (o(2), o(3)))) true
                else if (check((o(0), o(2)), (o(1), o(3)))) true
                else if (check((o(0), o(3)), (o(1), o(2)))) true
                else false
            case _ => false // odd count 1,3,>4 cannot be fixed with ≤2 edges
        }
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn is_possible(n: i32, edges: Vec<Vec<i32>>) -> bool {
        let mut parity = vec![0i32; (n as usize) + 1];
        let mut existing: HashSet<u64> = HashSet::new();

        for e in edges.iter() {
            let a = e[0];
            let b = e[1];
            parity[a as usize] ^= 1;
            parity[b as usize] ^= 1;
            let (u, v) = if a < b { (a as u64, b as u64) } else { (b as u64, a as u64) };
            existing.insert((u << 32) | v);
        }

        let mut odds = Vec::new();
        for i in 1..=n {
            if parity[i as usize] & 1 == 1 {
                odds.push(i);
            }
        }

        match odds.len() {
            0 => true,
            2 => {
                let a = odds[0];
                let b = odds[1];
                // direct edge possible?
                let (u, v) = if a < b { (a as u64, b as u64) } else { (b as u64, a as u64) };
                if !existing.contains(&(u << 32 | v)) {
                    return true;
                }
                // need an intermediate node c
                for c in 1..=n {
                    if c == a || c == b {
                        continue;
                    }
                    let (ua, va) = if a < c { (a as u64, c as u64) } else { (c as u64, a as u64) };
                    let (ub, vb) = if b < c { (b as u64, c as u64) } else { (c as u64, b as u64) };
                    if !existing.contains(&(ua << 32 | va)) && !existing.contains(&(ub << 32 | vb)) {
                        return true;
                    }
                }
                false
            }
            4 => {
                let a = odds[0];
                let b = odds[1];
                let c = odds[2];
                let d = odds[3];

                let edge_missing = |x: i32, y: i32| -> bool {
                    let (u, v) = if x < y { (x as u64, y as u64) } else { (y as u64, x as u64) };
                    !existing.contains(&(u << 32 | v))
                };

                (edge_missing(a, b) && edge_missing(c, d))
                    || (edge_missing(a, c) && edge_missing(b, d))
                    || (edge_missing(a, d) && edge_missing(b, c))
            }
            _ => false,
        }
    }
}
```

## Racket

```racket
(define/contract (is-possible n edges)
  (-> exact-integer? (listof (listof exact-integer?)) boolean?)
  (let* ((deg (make-vector (+ n 1) 0))
         (adj (make-hash)))
    ;; build degree vector and adjacency set
    (for ([e edges])
      (define u (first e))
      (define v (second e))
      (vector-set! deg u (+ (vector-ref deg u) 1))
      (vector-set! deg v (+ (vector-ref deg v) 1))
      (hash-set! adj (if (< u v) (cons u v) (cons v u)) #t))
    ;; collect odd-degree nodes
    (define odds '())
    (for ([i (in-range 1 (+ n 1))])
      (when (odd? (vector-ref deg i))
        (set! odds (cons i odds))))
    (set! odds (reverse odds))
    (let ((cnt (length odds)))
      (cond
        [(= cnt 0) #t]                                   ; already even
        [(= cnt 2)
         (define a (list-ref odds 0))
         (define b (list-ref odds 1))
         (if (not (hash-has-key? adj (if (< a b) (cons a b) (cons b a))))
             #t                                            ; add edge directly
             ;; need an intermediate node x
             (let loop ((x 1))
               (cond [(> x n) #f]
                     [(or (= x a) (= x b)) (loop (+ x 1))]
                     [else
                      (if (and (not (hash-has-key? adj (if (< a x) (cons a x) (cons x a))))
                               (not (hash-has-key? adj (if (< b x) (cons b x) (cons x b)))))
                          #t
                          (loop (+ x 1)))]))) )]
        [(= cnt 4)
         (define a (list-ref odds 0))
         (define b (list-ref odds 1))
         (define c (list-ref odds 2))
         (define d (list-ref odds 3))
         (define (missing u v)
           (not (hash-has-key? adj (if (< u v) (cons u v) (cons v u)))))
         (or (and (missing a b) (missing c d))
             (and (missing a c) (missing b d))
             (and (missing a d) (missing b c)))]
        [else #f]))))
```

## Erlang

```erlang
-module(solution).
-export([is_possible/2]).

-spec is_possible(N :: integer(), Edges :: [[integer()]]) -> boolean().
is_possible(N, Edges) ->
    EdgeSet = build_edge_set(Edges, #{}),
    DegMap  = build_deg_map(Edges, #{}),
    OddNodes = [Node || {Node,Deg} <- maps:to_list(DegMap), (Deg rem 2) =:= 1],
    case length(OddNodes) of
        0 -> true;
        2 -> handle_two(N, EdgeSet, OddNodes);
        4 -> handle_four(EdgeSet, OddNodes);
        _ -> false
    end.

%% Build a set (map) containing all existing edges as ordered tuples {U,V}
-spec build_edge_set([[integer()]], map()) -> map().
build_edge_set([], Set) -> Set;
build_edge_set([[A,B]|Rest], Set) ->
    Key = if A < B -> {A,B}; true -> {B,A} end,
    build_edge_set(Rest, maps:put(Key, true, Set)).

%% Build a map from node to its degree
-spec build_deg_map([[integer()]], map()) -> map().
build_deg_map([], Map) -> Map;
build_deg_map([[A,B]|Rest], Map) ->
    M1 = maps:update_with(A, fun(D) -> D + 1 end, 1, Map),
    M2 = maps:update_with(B, fun(D) -> D + 1 end, 1, M1),
    build_deg_map(Rest, M2).

%% Check case with exactly two odd-degree nodes
-spec handle_two(integer(), map(), [integer()]) -> boolean().
handle_two(N, EdgeSet, [A,B]) ->
    case edge_exists(A, B, EdgeSet) of
        false -> true;
        true  -> find_intermediate(1, N, EdgeSet, A, B)
    end.

%% Find a third node X such that edges (A,X) and (B,X) are both absent
-spec find_intermediate(integer(), integer(), map(), integer(), integer()) -> boolean().
find_intermediate(I, N, _EdgeSet, _A, _B) when I > N ->
    false;
find_intermediate(I, N, EdgeSet, A, B) ->
    if I =:= A orelse I =:= B ->
            find_intermediate(I + 1, N, EdgeSet, A, B);
       true ->
            case edge_exists(A, I, EdgeSet) of
                false ->
                    case edge_exists(B, I, EdgeSet) of
                        false -> true;
                        _    -> find_intermediate(I + 1, N, EdgeSet, A, B)
                    end;
                _ -> find_intermediate(I + 1, N, EdgeSet, A, B)
            end
    end.

%% Check case with exactly four odd-degree nodes
-spec handle_four(map(), [integer()]) -> boolean().
handle_four(EdgeSet, [A,B,C,D]) ->
    check_pairing(EdgeSet, A, B, C, D) orelse
    check_pairing(EdgeSet, A, C, B, D) orelse
    check_pairing(EdgeSet, A, D, B, C).

-spec check_pairing(map(), integer(), integer(), integer(), integer()) -> boolean().
check_pairing(EdgeSet, X1, Y1, X2, Y2) ->
    not edge_exists(X1, Y1, EdgeSet) andalso
    not edge_exists(X2, Y2, EdgeSet).

-spec edge_exists(integer(), integer(), map()) -> boolean().
edge_exists(A, B, Set) ->
    Key = if A < B -> {A,B}; true -> {B,A} end,
    maps:is_key(Key, Set).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_possible(n :: integer, edges :: [[integer]]) :: boolean
  def is_possible(n, edges) do
    {odd_set, edge_set} =
      Enum.reduce(edges, {MapSet.new(), MapSet.new()}, fn [u, v], {oset, eset} ->
        oset = toggle(oset, u)
        oset = toggle(oset, v)

        key = if u < v, do: {u, v}, else: {v, u}
        eset = MapSet.put(eset, key)
        {oset, eset}
      end)

    odds = MapSet.to_list(odd_set)

    case length(odds) do
      0 ->
        true

      2 ->
        [a, b] = odds

        if not edge_exists?(edge_set, a, b) do
          true
        else
          Enum.any?(1..n, fn x ->
            x != a and x != b and
              (not edge_exists?(edge_set, a, x)) and
              (not edge_exists?(edge_set, b, x))
          end)
        end

      4 ->
        [a, b, c, d] = odds

        pairings = [
          {{a, b}, {c, d}},
          {{a, c}, {b, d}},
          {{a, d}, {b, c}}
        ]

        Enum.any?(pairings, fn {{u1, v1}, {u2, v2}} ->
          not edge_exists?(edge_set, u1, v1) and
            not edge_exists?(edge_set, u2, v2)
        end)

      _ ->
        false
    end
  end

  defp toggle(set, node) do
    if MapSet.member?(set, node), do: MapSet.delete(set, node), else: MapSet.put(set, node)
  end

  defp edge_exists?(set, u, v) do
    key = if u < v, do: {u, v}, else: {v, u}
    MapSet.member?(set, key)
  end
end
```

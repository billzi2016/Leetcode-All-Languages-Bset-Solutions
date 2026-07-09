# 2959. Number of Possible Sets of Closing Branches

## Cpp

```cpp
class Solution {
public:
    int numberOfSets(int n, int maxDistance, vector<vector<int>>& roads) {
        struct Edge {int u, v, w;};
        vector<Edge> edges;
        for (auto &r : roads) edges.push_back({r[0], r[1], r[2]});
        const long long INF = 4e14;
        long long ans = 0;
        int totalMask = 1 << n;
        static long long dist[10][10];
        for (int mask = 0; mask < totalMask; ++mask) {
            // initialize distances
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < n; ++j)
                    dist[i][j] = INF;
            for (int i = 0; i < n; ++i)
                if (mask & (1 << i)) dist[i][i] = 0;
            // set direct edges
            for (auto &e : edges) {
                if ((mask & (1 << e.u)) && (mask & (1 << e.v))) {
                    if (e.w < dist[e.u][e.v]) {
                        dist[e.u][e.v] = dist[e.v][e.u] = e.w;
                    }
                }
            }
            // Floyd-Warshall limited to active vertices
            for (int k = 0; k < n; ++k) if (mask & (1 << k)) {
                for (int i = 0; i < n; ++i) if (mask & (1 << i)) {
                    long long dik = dist[i][k];
                    if (dik == INF) continue;
                    for (int j = 0; j < n; ++j) if (mask & (1 << j)) {
                        long long nd = dik + dist[k][j];
                        if (nd < dist[i][j]) dist[i][j] = nd;
                    }
                }
            }
            // verify condition
            bool ok = true;
            for (int i = 0; i < n && ok; ++i) if (mask & (1 << i)) {
                for (int j = i + 1; j < n; ++j) if (mask & (1 << j)) {
                    if (dist[i][j] > maxDistance) { ok = false; break; }
                }
            }
            if (ok) ++ans;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int numberOfSets(int n, int maxDistance, int[][] roads) {
        final long INF = (long) 1e15;
        long[][] base = new long[n][n];
        for (int i = 0; i < n; i++) {
            java.util.Arrays.fill(base[i], INF);
            base[i][i] = 0;
        }
        for (int[] r : roads) {
            int u = r[0], v = r[1];
            long w = r[2];
            if (w < base[u][v]) {
                base[u][v] = base[v][u] = w;
            }
        }

        int totalMasks = 1 << n;
        int ans = 0;

        for (int mask = 0; mask < totalMasks; mask++) {
            long[][] d = new long[n][n];
            // initialize distances for active vertices
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    for (int j = 0; j < n; j++) {
                        if ((mask & (1 << j)) != 0) {
                            d[i][j] = base[i][j];
                        } else {
                            d[i][j] = INF;
                        }
                    }
                    d[i][i] = 0;
                } else {
                    java.util.Arrays.fill(d[i], INF);
                }
            }

            // Floyd-Warshall using only active intermediate vertices
            for (int k = 0; k < n; k++) if ((mask & (1 << k)) != 0) {
                for (int i = 0; i < n; i++) if ((mask & (1 << i)) != 0) {
                    long dik = d[i][k];
                    if (dik == INF) continue;
                    for (int j = 0; j < n; j++) if ((mask & (1 << j)) != 0) {
                        long nd = dik + d[k][j];
                        if (nd < d[i][j]) d[i][j] = nd;
                    }
                }
            }

            boolean ok = true;
            for (int i = 0; i < n && ok; i++) if ((mask & (1 << i)) != 0) {
                for (int j = i + 1; j < n; j++) if ((mask & (1 << j)) != 0) {
                    if (d[i][j] > maxDistance) {
                        ok = false;
                        break;
                    }
                }
            }

            if (ok) ans++;
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfSets(self, n, maxDistance, roads):
        """
        :type n: int
        :type maxDistance: int
        :type roads: List[List[int]]
        :rtype: int
        """
        INF = 10**15

        # keep minimal weight for each unordered pair (u,v)
        min_edge = [[INF] * n for _ in range(n)]
        for u, v, w in roads:
            if w < min_edge[u][v]:
                min_edge[u][v] = min_edge[v][u] = w

        total = 0
        full_mask = 1 << n

        # precompute list of bits for each mask to avoid repeated loops? not needed given small n
        for mask in range(full_mask):
            # count active vertices
            cnt = bin(mask).count("1")
            if cnt <= 1:
                total += 1
                continue

            # initialize distance matrix for active vertices
            dist = [[INF] * n for _ in range(n)]
            for i in range(n):
                if mask & (1 << i):
                    dist[i][i] = 0

            # set direct edges among active vertices
            for u in range(n):
                if not (mask & (1 << u)):
                    continue
                row = min_edge[u]
                for v in range(u + 1, n):
                    if mask & (1 << v) and row[v] < INF:
                        w = row[v]
                        dist[u][v] = dist[v][u] = w

            # Floyd-Warshall limited to active vertices
            for k in range(n):
                if not (mask & (1 << k)):
                    continue
                dk = dist[k]
                for i in range(n):
                    if not (mask & (1 << i)):
                        continue
                    dik = dist[i][k]
                    if dik == INF:
                        continue
                    di = dist[i]
                    for j in range(n):
                        if not (mask & (1 << j)):
                            continue
                        nd = dik + dk[j]
                        if nd < di[j]:
                            di[j] = nd

            # verify all pairwise distances within maxDistance
            ok = True
            for i in range(n):
                if not (mask & (1 << i)):
                    continue
                for j in range(i + 1, n):
                    if mask & (1 << j):
                        if dist[i][j] > maxDistance:
                            ok = False
                            break
                if not ok:
                    break

            if ok:
                total += 1

        return total
```

## Python3

```python
import sys
from typing import List

class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        INF = 10**15
        # adjacency matrix with minimal direct edge weight
        adj = [[INF] * n for _ in range(n)]
        for i in range(n):
            adj[i][i] = 0
        for u, v, w in roads:
            if w < adj[u][v]:
                adj[u][v] = adj[v][u] = w

        total = 0
        full_mask = (1 << n) - 1
        # iterate over all subsets of closed vertices
        for mask in range(full_mask + 1):
            active = [i for i in range(n) if not (mask >> i & 1)]
            m = len(active)
            if m <= 1:
                total += 1
                continue

            # initialize distance matrix for active vertices
            dist = [[INF] * n for _ in range(n)]
            for i in active:
                dist[i][i] = 0
                for j in active:
                    if adj[i][j] < INF:
                        dist[i][j] = adj[i][j]

            # Floyd-Warshall limited to active vertices
            for k in active:
                dk = dist[k]
                for i in active:
                    dik = dist[i][k]
                    if dik == INF:
                        continue
                    di = dist[i]
                    for j in active:
                        nd = dik + dk[j]
                        if nd < di[j]:
                            di[j] = nd

            # verify all pairwise distances within maxDistance
            ok = True
            for i_idx in range(m):
                i = active[i_idx]
                di = dist[i]
                for j_idx in range(i_idx + 1, m):
                    j = active[j_idx]
                    if di[j] > maxDistance:
                        ok = False
                        break
                if not ok:
                    break

            if ok:
                total += 1

        return total
```

## C

```c
int numberOfSets(int n, int maxDistance, int** roads, int roadsSize, int* roadsColSize) {
    const int INF = 1000000000;
    int adj[10][10];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            adj[i][j] = (i == j) ? 0 : INF;
        }
    }
    for (int i = 0; i < roadsSize; ++i) {
        int u = roads[i][0];
        int v = roads[i][1];
        int w = roads[i][2];
        if (w < adj[u][v]) {
            adj[u][v] = adj[v][u] = w;
        }
    }

    int totalMask = 1 << n;
    int answer = 0;
    int d[10][10];

    for (int mask = 0; mask < totalMask; ++mask) {
        int activeCount = n - __builtin_popcount(mask);
        if (activeCount <= 1) {
            ++answer;
            continue;
        }

        // copy adjacency matrix
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                d[i][j] = adj[i][j];

        // Floyd-Warshall using only active vertices
        for (int k = 0; k < n; ++k) if (!(mask & (1 << k))) {
            for (int i = 0; i < n; ++i) if (!(mask & (1 << i))) {
                if (d[i][k] == INF) continue;
                for (int j = 0; j < n; ++j) if (!(mask & (1 << j))) {
                    if (d[k][j] == INF) continue;
                    int nd = d[i][k] + d[k][j];
                    if (nd < d[i][j]) d[i][j] = nd;
                }
            }
        }

        // verify all pair distances within maxDistance
        int ok = 1;
        for (int i = 0; i < n && ok; ++i) {
            if (mask & (1 << i)) continue;
            for (int j = i + 1; j < n; ++j) {
                if (mask & (1 << j)) continue;
                int dist = d[i][j];
                if (dist == INF || dist > maxDistance) {
                    ok = 0;
                    break;
                }
            }
        }

        if (ok) ++answer;
    }

    return answer;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumberOfSets(int n, int maxDistance, int[][] roads)
    {
        const long INF = (long)1e15;
        long[,] baseDist = new long[n, n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                baseDist[i, j] = (i == j) ? 0 : INF;

        foreach (var r in roads)
        {
            int u = r[0], v = r[1];
            long w = r[2];
            if (w < baseDist[u, v])
            {
                baseDist[u, v] = w;
                baseDist[v, u] = w;
            }
        }

        int totalMasks = 1 << n;
        int answer = 0;

        for (int closedMask = 0; closedMask < totalMasks; closedMask++)
        {
            int activeMask = (~closedMask) & (totalMasks - 1);
            int activeCount = BitCount(activeMask);
            if (activeCount <= 1)
            {
                answer++;
                continue;
            }

            long[,] dist = new long[n, n];
            for (int i = 0; i < n; i++)
            {
                bool ai = ((activeMask >> i) & 1) == 1;
                for (int j = 0; j < n; j++)
                {
                    if (!ai || ((activeMask >> j) & 1) == 0)
                        dist[i, j] = INF;
                    else
                        dist[i, j] = baseDist[i, j];
                }
            }

            // Floyd-Warshall limited to active vertices
            for (int k = 0; k < n; k++)
            {
                if (((activeMask >> k) & 1) == 0) continue;
                for (int i = 0; i < n; i++)
                {
                    if (((activeMask >> i) & 1) == 0) continue;
                    long dik = dist[i, k];
                    if (dik == INF) continue;
                    for (int j = 0; j < n; j++)
                    {
                        if (((activeMask >> j) & 1) == 0) continue;
                        long nd = dik + dist[k, j];
                        if (nd < dist[i, j])
                            dist[i, j] = nd;
                    }
                }
            }

            bool ok = true;
            for (int i = 0; i < n && ok; i++)
            {
                if (((activeMask >> i) & 1) == 0) continue;
                for (int j = i + 1; j < n; j++)
                {
                    if (((activeMask >> j) & 1) == 0) continue;
                    if (dist[i, j] > maxDistance)
                    {
                        ok = false;
                        break;
                    }
                }
            }

            if (ok) answer++;
        }

        return answer;
    }

    private int BitCount(int x)
    {
        int cnt = 0;
        while (x != 0)
        {
            cnt += x & 1;
            x >>= 1;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} maxDistance
 * @param {number[][]} roads
 * @return {number}
 */
var numberOfSets = function(n, maxDistance, roads) {
    const totalMasks = 1 << n;
    const INF = 1e15;
    let answer = 0;

    // helper to count bits set in mask
    const popcount = (x) => {
        let cnt = 0;
        while (x) {
            cnt += x & 1;
            x >>>= 1;
        }
        return cnt;
    };

    for (let mask = 0; mask < totalMasks; ++mask) {
        const activeCnt = n - popcount(mask);
        if (activeCnt <= 1) { // empty or single vertex always satisfies condition
            answer++;
            continue;
        }

        // distance matrix, only consider active vertices
        const dist = Array.from({ length: n }, () => new Float64Array(n).fill(INF));
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) continue; // closed vertex
            dist[i][i] = 0;
        }

        // add edges that connect two active vertices
        for (const e of roads) {
            const u = e[0], v = e[1], w = e[2];
            if ((mask >> u) & 1) continue;
            if ((mask >> v) & 1) continue;
            if (w < dist[u][v]) {
                dist[u][v] = w;
                dist[v][u] = w;
            }
        }

        // Floyd‑Warshall on active vertices
        for (let k = 0; k < n; ++k) {
            if ((mask >> k) & 1) continue;
            for (let i = 0; i < n; ++i) {
                if ((mask >> i) & 1) continue;
                const dik = dist[i][k];
                if (dik === INF) continue;
                for (let j = 0; j < n; ++j) {
                    if ((mask >> j) & 1) continue;
                    const nd = dik + dist[k][j];
                    if (nd < dist[i][j]) dist[i][j] = nd;
                }
            }
        }

        // verify all pairwise distances are within maxDistance
        let ok = true;
        outer:
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) continue;
            for (let j = i + 1; j < n; ++j) {
                if ((mask >> j) & 1) continue;
                if (dist[i][j] > maxDistance) { ok = false; break outer; }
            }
        }

        if (ok) answer++;
    }

    return answer;
};
```

## Typescript

```typescript
function numberOfSets(n: number, maxDistance: number, roads: number[][]): number {
    const INF = 1e15;
    let result = 0;
    const totalMasks = 1 << n; // mask of closed branches
    for (let mask = 0; mask < totalMasks; ++mask) {
        const active: number[] = [];
        for (let i = 0; i < n; ++i) {
            if ((mask >> i & 1) === 0) active.push(i);
        }
        const m = active.length;
        if (m <= 1) {
            result++;
            continue;
        }

        // distance matrix
        const dist: number[][] = Array.from({ length: n }, () => Array(n).fill(INF));
        for (const v of active) dist[v][v] = 0;

        for (const [u, v, w] of roads) {
            if ((mask >> u & 1) === 0 && (mask >> v & 1) === 0) {
                if (w < dist[u][v]) {
                    dist[u][v] = dist[v][u] = w;
                }
            }
        }

        // Floyd‑Warshall on active vertices only
        for (let ki = 0; ki < m; ++ki) {
            const k = active[ki];
            for (let ii = 0; ii < m; ++ii) {
                const i = active[ii];
                if (dist[i][k] === INF) continue;
                for (let jj = 0; jj < m; ++jj) {
                    const j = active[jj];
                    const nd = dist[i][k] + dist[k][j];
                    if (nd < dist[i][j]) dist[i][j] = nd;
                }
            }
        }

        let ok = true;
        for (let ii = 0; ii < m && ok; ++ii) {
            const i = active[ii];
            for (let jj = ii + 1; jj < m; ++jj) {
                const j = active[jj];
                if (dist[i][j] > maxDistance) {
                    ok = false;
                    break;
                }
            }
        }

        if (ok) result++;
    }
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $maxDistance
     * @param Integer[][] $roads
     * @return Integer
     */
    function numberOfSets($n, $maxDistance, $roads) {
        $INF = 1e15;
        // base distance matrix for the whole graph
        $baseDist = array_fill(0, $n, array_fill(0, $n, $INF));
        for ($i = 0; $i < $n; $i++) {
            $baseDist[$i][$i] = 0;
        }
        foreach ($roads as $r) {
            [$u, $v, $w] = $r;
            if ($w < $baseDist[$u][$v]) {
                $baseDist[$u][$v] = $w;
                $baseDist[$v][$u] = $w;
            }
        }

        $ans = 0;
        $fullMask = (1 << $n) - 1;

        for ($mask = 0; $mask <= $fullMask; $mask++) { // active vertices mask
            // distance matrix limited to active vertices
            $dist = array_fill(0, $n, array_fill(0, $n, $INF));
            for ($i = 0; $i < $n; $i++) {
                if ((($mask >> $i) & 1) == 0) continue;
                $dist[$i][$i] = 0;
                for ($j = $i + 1; $j < $n; $j++) {
                    if ((($mask >> $j) & 1) == 0) continue;
                    $d = $baseDist[$i][$j];
                    $dist[$i][$j] = $d;
                    $dist[$j][$i] = $d;
                }
            }

            // Floyd‑Warshall on the active set
            for ($k = 0; $k < $n; $k++) {
                if ((($mask >> $k) & 1) == 0) continue;
                for ($i = 0; $i < $n; $i++) {
                    if ((($mask >> $i) & 1) == 0) continue;
                    $dik = $dist[$i][$k];
                    if ($dik >= $INF) continue;
                    for ($j = 0; $j < $n; $j++) {
                        if ((($mask >> $j) & 1) == 0) continue;
                        $dkj = $dist[$k][$j];
                        if ($dkj >= $INF) continue;
                        $new = $dik + $dkj;
                        if ($new < $dist[$i][$j]) {
                            $dist[$i][$j] = $new;
                        }
                    }
                }
            }

            // verify pairwise distance condition
            $valid = true;
            for ($i = 0; $i < $n && $valid; $i++) {
                if ((($mask >> $i) & 1) == 0) continue;
                for ($j = $i + 1; $j < $n; $j++) {
                    if ((($mask >> $j) & 1) == 0) continue;
                    if ($dist[$i][$j] > $maxDistance) {
                        $valid = false;
                        break;
                    }
                }
            }

            if ($valid) $ans++;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfSets(_ n: Int, _ maxDistance: Int, _ roads: [[Int]]) -> Int {
        let INF = Int.max / 4
        var dist = Array(repeating: Array(repeating: INF, count: n), count: n)
        for i in 0..<n { dist[i][i] = 0 }
        for road in roads {
            let u = road[0], v = road[1], w = road[2]
            if w < dist[u][v] {
                dist[u][v] = w
                dist[v][u] = w
            }
        }
        // Floyd‑Warshall on the full graph to have initial shortest paths (optional)
        for k in 0..<n {
            for i in 0..<n where dist[i][k] < INF {
                for j in 0..<n where dist[k][j] < INF {
                    let nd = dist[i][k] + dist[k][j]
                    if nd < dist[i][j] { dist[i][j] = nd }
                }
            }
        }
        
        let totalMasks = 1 << n
        var answer = 0
        
        for activeMask in 0..<totalMasks {
            // count bits
            if activeMask == 0 || (activeMask & (activeMask - 1)) == 0 {
                // empty or single vertex always valid
                answer += 1
                continue
            }
            
            var d = Array(repeating: Array(repeating: INF, count: n), count: n)
            for i in 0..<n where ((activeMask >> i) & 1) == 1 {
                for j in 0..<n where ((activeMask >> j) & 1) == 1 {
                    d[i][j] = dist[i][j]
                }
                d[i][i] = 0
            }
            
            // Floyd‑Warshall limited to active vertices
            for k in 0..<n where ((activeMask >> k) & 1) == 1 {
                for i in 0..<n where ((activeMask >> i) & 1) == 1 && d[i][k] < INF {
                    for j in 0..<n where ((activeMask >> j) & 1) == 1 && d[k][j] < INF {
                        let nd = d[i][k] + d[k][j]
                        if nd < d[i][j] { d[i][j] = nd }
                    }
                }
            }
            
            var ok = true
            outer: for i in 0..<n where ((activeMask >> i) & 1) == 1 {
                for j in (i+1)..<n where ((activeMask >> j) & 1) == 1 {
                    if d[i][j] > maxDistance {
                        ok = false
                        break outer
                    }
                }
            }
            
            if ok { answer += 1 }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfSets(n: Int, maxDistance: Int, roads: Array<IntArray>): Int {
        val INF = Long.MAX_VALUE / 4
        val dist = Array(n) { LongArray(n) { INF } }
        for (i in 0 until n) dist[i][i] = 0L
        for (road in roads) {
            val u = road[0]
            val v = road[1]
            val w = road[2].toLong()
            if (w < dist[u][v]) {
                dist[u][v] = w
                dist[v][u] = w
            }
        }

        var count = 0
        val fullMask = (1 shl n) - 1
        for (closedMask in 0..fullMask) {
            val activeMask = fullMask xor closedMask
            // popcount <= 1 always satisfies condition
            if (Integer.bitCount(activeMask) <= 1) {
                count++
                continue
            }
            // copy distances
            val cur = Array(n) { i -> dist[i].clone() }

            // Floyd-Warshall using only active vertices as intermediates
            for (k in 0 until n) if ((activeMask and (1 shl k)) != 0) {
                for (i in 0 until n) if ((activeMask and (1 shl i)) != 0) {
                    val dik = cur[i][k]
                    if (dik == INF) continue
                    for (j in 0 until n) if ((activeMask and (1 shl j)) != 0) {
                        val dkj = cur[k][j]
                        if (dkj == INF) continue
                        val nd = dik + dkj
                        if (nd < cur[i][j]) cur[i][j] = nd
                    }
                }
            }

            var ok = true
            outer@ for (i in 0 until n) {
                if ((activeMask and (1 shl i)) == 0) continue
                for (j in i + 1 until n) {
                    if ((activeMask and (1 shl j)) == 0) continue
                    if (cur[i][j] > maxDistance) {
                        ok = false
                        break@outer
                    }
                }
            }
            if (ok) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int numberOfSets(int n, int maxDistance, List<List<int>> roads) {
    const int INF = 1 << 30;
    // base adjacency matrix with minimal direct edge weight
    List<List<int>> baseDist = List.generate(n, (_) => List.filled(n, INF));
    for (int i = 0; i < n; ++i) baseDist[i][i] = 0;
    for (var r in roads) {
      int u = r[0], v = r[1], w = r[2];
      if (w < baseDist[u][v]) {
        baseDist[u][v] = w;
        baseDist[v][u] = w;
      }
    }

    int allMask = (1 << n) - 1;
    int total = 0;

    // helper to count bits
    int bitCount(int x) {
      int cnt = 0;
      while (x != 0) {
        cnt += x & 1;
        x >>= 1;
      }
      return cnt;
    }

    for (int closedMask = 0; closedMask <= allMask; ++closedMask) {
      int activeMask = allMask ^ closedMask;
      int activeCnt = bitCount(activeMask);
      if (activeCnt <= 1) {
        total++;
        continue;
      }

      // distance matrix for current active set
      List<List<int>> d = List.generate(n, (_) => List.filled(n, INF));
      for (int i = 0; i < n; ++i) {
        if ((activeMask & (1 << i)) != 0) {
          d[i][i] = 0;
          for (int j = 0; j < n; ++j) {
            if ((activeMask & (1 << j)) != 0 && baseDist[i][j] < INF) {
              d[i][j] = baseDist[i][j];
            }
          }
        }
      }

      // Floyd-Warshall limited to active vertices
      for (int k = 0; k < n; ++k) {
        if ((activeMask & (1 << k)) == 0) continue;
        for (int i = 0; i < n; ++i) {
          if ((activeMask & (1 << i)) == 0) continue;
          int dik = d[i][k];
          if (dik == INF) continue;
          for (int j = 0; j < n; ++j) {
            if ((activeMask & (1 << j)) == 0) continue;
            int nd = dik + d[k][j];
            if (nd < d[i][j]) d[i][j] = nd;
          }
        }
      }

      bool ok = true;
      outer:
      for (int i = 0; i < n; ++i) {
        if ((activeMask & (1 << i)) == 0) continue;
        for (int j = i + 1; j < n; ++j) {
          if ((activeMask & (1 << j)) == 0) continue;
          if (d[i][j] > maxDistance) {
            ok = false;
            break outer;
          }
        }
      }

      if (ok) total++;
    }

    return total;
  }
}
```

## Golang

```go
func numberOfSets(n int, maxDistance int, roads [][]int) int {
	const INF int64 = 1 << 60
	dist := make([][]int64, n)
	for i := 0; i < n; i++ {
		dist[i] = make([]int64, n)
		for j := 0; j < n; j++ {
			if i == j {
				dist[i][j] = 0
			} else {
				dist[i][j] = INF
			}
		}
	}
	for _, r := range roads {
		u, v, w := r[0], r[1], int64(r[2])
		if w < dist[u][v] {
			dist[u][v] = w
			dist[v][u] = w
		}
	}
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			if dist[i][k] == INF {
				continue
			}
			for j := 0; j < n; j++ {
				if dist[k][j] == INF {
					continue
				}
				if nd := dist[i][k] + dist[k][j]; nd < dist[i][j] {
					dist[i][j] = nd
				}
			}
		}
	}
	maxDist64 := int64(maxDistance)
	total := 0
	limit := 1 << n
	for mask := 0; mask < limit; mask++ {
		ok := true
		for i := 0; i < n && ok; i++ {
			if mask>>i&1 == 1 {
				continue
			}
			for j := i + 1; j < n; j++ {
				if mask>>j&1 == 1 {
					continue
				}
				if dist[i][j] > maxDist64 {
					ok = false
					break
				}
			}
		}
		if ok {
			total++
		}
	}
	return total
}
```

## Ruby

```ruby
def number_of_sets(n, max_distance, roads)
  inf = 1 << 60
  dist = Array.new(n) { Array.new(n, inf) }
  n.times { |i| dist[i][i] = 0 }

  roads.each do |u, v, w|
    if w < dist[u][v]
      dist[u][v] = w
      dist[v][u] = w
    end
  end

  n.times do |k|
    n.times do |i|
      next if dist[i][k] == inf
      n.times do |j|
        nd = dist[i][k] + dist[k][j]
        dist[i][j] = nd if nd < dist[i][j]
      end
    end
  end

  total = 0
  limit = 1 << n
  (0...limit).each do |mask|
    active = []
    n.times { |i| active << i if ((mask >> i) & 1) == 0 }

    ok = true
    if active.size > 1
      (0...active.size).each do |a_idx|
        i = active[a_idx]
        (a_idx + 1...active.size).each do |b_idx|
          j = active[b_idx]
          if dist[i][j] > max_distance
            ok = false
            break
          end
        end
        break unless ok
      end
    end

    total += 1 if ok
  end

  total
end
```

## Scala

```scala
object Solution {
    def numberOfSets(n: Int, maxDistance: Int, roads: Array[Array[Int]]): Int = {
        val INF: Long = Long.MaxValue / 4
        val base = Array.ofDim[Long](n, n)
        for (i <- 0 until n) {
            java.util.Arrays.fill(base(i), INF)
            base(i)(i) = 0L
        }
        for (r <- roads) {
            val u = r(0)
            val v = r(1)
            val w = r(2).toLong
            if (w < base(u)(v)) {
                base(u)(v) = w
                base(v)(u) = w
            }
        }

        var ans = 0
        val fullMask = (1 << n) - 1

        for (closedMask <- 0 to fullMask) {
            val activeMask = fullMask ^ closedMask
            val cntActive = Integer.bitCount(activeMask)
            if (cntActive <= 1) {
                ans += 1
            } else {
                // copy base distances
                val d = Array.ofDim[Long](n, n)
                for (i <- 0 until n) {
                    System.arraycopy(base(i), 0, d(i), 0, n)
                }

                var k = 0
                while (k < n) {
                    if ((activeMask & (1 << k)) != 0) {
                        var i = 0
                        while (i < n) {
                            if ((activeMask & (1 << i)) != 0 && d(i)(k) != INF) {
                                var j = 0
                                while (j < n) {
                                    if ((activeMask & (1 << j)) != 0 && d(k)(j) != INF) {
                                        val nd = d(i)(k) + d(k)(j)
                                        if (nd < d(i)(j)) d(i)(j) = nd
                                    }
                                    j += 1
                                }
                            }
                            i += 1
                        }
                    }
                    k += 1
                }

                var ok = true
                var i = 0
                while (i < n && ok) {
                    if ((activeMask & (1 << i)) != 0) {
                        var j = i + 1
                        while (j < n && ok) {
                            if ((activeMask & (1 << j)) != 0) {
                                if (d(i)(j) > maxDistance) ok = false
                            }
                            j += 1
                        }
                    }
                    i += 1
                }

                if (ok) ans += 1
            }
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_sets(n: i32, max_distance: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let maxd = max_distance as i64;
        const INF: i64 = 1_000_000_000_000;
        // adjacency matrix with minimum edge weight
        let mut adj = vec![vec![INF; n]; n];
        for i in 0..n {
            adj[i][i] = 0;
        }
        for r in roads {
            let u = r[0] as usize;
            let v = r[1] as usize;
            let w = r[2] as i64;
            if w < adj[u][v] {
                adj[u][v] = w;
                adj[v][u] = w;
            }
        }

        let total_masks = 1usize << n;
        let mut count: i32 = 0;

        for mask in 0..total_masks {
            // vertices that remain active
            let active_mask = (!mask) & (total_masks - 1);
            if active_mask == 0 {
                count += 1; // empty set of active branches always valid
                continue;
            }

            // collect indices of active vertices
            let mut act_idx = Vec::new();
            for i in 0..n {
                if (active_mask >> i) & 1 == 1 {
                    act_idx.push(i);
                }
            }
            let m = act_idx.len();

            // distance matrix for the induced subgraph
            let mut dist = vec![vec![INF; m]; m];
            for a in 0..m {
                dist[a][a] = 0;
                for b in (a + 1)..m {
                    let u = act_idx[a];
                    let v = act_idx[b];
                    let w = adj[u][v];
                    dist[a][b] = w;
                    dist[b][a] = w;
                }
            }

            // Floyd‑Warshall on the active vertices
            for k in 0..m {
                for i in 0..m {
                    if dist[i][k] == INF {
                        continue;
                    }
                    for j in 0..m {
                        if dist[k][j] == INF {
                            continue;
                        }
                        let nd = dist[i][k] + dist[k][j];
                        if nd < dist[i][j] {
                            dist[i][j] = nd;
                        }
                    }
                }
            }

            // verify pairwise distances
            let mut ok = true;
            for i in 0..m {
                for j in (i + 1)..m {
                    if dist[i][j] > maxd {
                        ok = false;
                        break;
                    }
                }
                if !ok {
                    break;
                }
            }

            if ok {
                count += 1;
            }
        }

        count
    }
}
```

## Racket

```racket
(define (number-of-sets n maxDistance roads)
  (let* ((INF 1000000000)
         ;; adjacency matrix with minimal edge weight
         (adj (make-vector n (lambda (_) (make-vector n INF))))
         (_ (for ([r roads])
              (let* ((u (list-ref r 0))
                     (v (list-ref r 1))
                     (w (list-ref r 2)))
                (when (< w (vector-ref (vector-ref adj u) v))
                  (vector-set! (vector-ref adj u) v w)
                  (vector-set! (vector-ref adj v) u w)))))
         (total (expt 2 n)))
    (let ((cnt 0))
      (for ([mask (in-range total)])
        ;; collect active nodes (those not closed in mask)
        (let loop-collect ((i 0) (act '()))
          (if (= i n)
              (let ((active act))
                (if (<= (length active) 1)
                    (set! cnt (+ cnt 1))
                    (begin
                      ;; distance matrix for this subset
                      (define d (make-vector n (lambda (_) (make-vector n INF))))
                      ;; init diagonal and direct edges among active nodes
                      (for ([i active])
                        (vector-set! (vector-ref d i) i 0))
                      (for ([r roads])
                        (let* ((u (list-ref r 0))
                               (v (list-ref r 1))
                               (w (list-ref r 2)))
                          (when (and (member u active) (member v active))
                            (when (< w (vector-ref (vector-ref d u) v))
                              (vector-set! (vector-ref d u) v w)
                              (vector-set! (vector-ref d v) u w)))))
                      ;; Floyd‑Warshall restricted to active nodes
                      (for ([k active])
                        (for ([i active])
                          (let ((dik (vector-ref (vector-ref d i) k)))
                            (when (< dik INF)
                              (for ([j active])
                                (let* ((dkj (vector-ref (vector-ref d k) j))
                                       (new (+ dik dkj)))
                                  (when (< new (vector-ref (vector-ref d i) j))
                                    (vector-set! (vector-ref d i) j new))))))))
                      ;; verify all pair distances
                      (let ((ok (let check-pairs ((lst active) (good #t))
                                 (if (or (null? lst) (not good))
                                     good
                                     (let ((i (car lst)))
                                       (check-pairs (cdr lst)
                                         (let inner ((rest (cdr lst)) (g good))
                                           (if (or (null? rest) (not g))
                                               g
                                               (let ((j (car rest))
                                                     (distij (vector-ref (vector-ref d i) j)))
                                                 (if (> distij maxDistance)
                                                     #f
                                                     (inner (cdr rest) g))))))))))
                        (when ok (set! cnt (+ cnt 1)))))))
              (loop-collect (+ i 1)
                (if (= 0 (bitwise-and mask (arithmetic-shift 1 i)))
                    (cons i act)
                    act))))))
      cnt)))
```

## Erlang

```erlang
-spec number_of_sets(N :: integer(), MaxDistance :: integer(), Roads :: [[integer()]]) -> integer().
number_of_sets(N, MaxDistance, Roads) ->
    Inf = 1 bsl 60,
    InitMap = init_map(N, Inf),
    EdgeMap = fill_edges(InitMap, Roads),
    DistMap = floyd_warshall(EdgeMap, N),
    TotalMasks = 1 bsl N,
    lists:foldl(
        fun(Mask, Acc) ->
            if valid_mask(Mask, DistMap, MaxDistance, N) -> Acc + 1;
               true -> Acc
            end
        end,
        0,
        lists:seq(0, TotalMasks - 1)
    ).

init_map(N, Inf) ->
    lists:foldl(
        fun(I, AccI) ->
            lists:foldl(
                fun(J, AccJ) ->
                    Val = if I == J -> 0; true -> Inf end,
                    maps:put({I,J}, Val, AccJ)
                end,
                AccI,
                lists:seq(0,N-1)
            )
        end,
        #{},
        lists:seq(0,N-1)
    ).

fill_edges(Map, Roads) ->
    lists:foldl(
        fun([U,V,W], M) ->
            M1 = update_min(M, {U,V}, W),
            update_min(M1, {V,U}, W)
        end,
        Map,
        Roads
    ).

update_min(Map, Key, NewVal) ->
    case maps:get(Key, Map) of
        Old when Old =< NewVal -> Map;
        _Old -> maps:put(Key, NewVal, Map)
    end.

floyd_warshall(Map, N) ->
    lists:foldl(
        fun(K, Mk) ->
            lists:foldl(
                fun(I, Mi) ->
                    lists:foldl(
                        fun(J, Mij) ->
                            Dij = maps:get({I,J}, Mij),
                            Dik = maps:get({I,K}, Mij),
                            Dkj = maps:get({K,J}, Mij),
                            New = Dik + Dkj,
                            if New < Dij -> maps:put({I,J}, New, Mij);
                               true -> Mij
                            end
                        end,
                        Mi,
                        lists:seq(0,N-1)
                    )
                end,
                Mk,
                lists:seq(0,N-1)
            )
        end,
        Map,
        lists:seq(0,N-1)
    ).

valid_mask(Mask, DistMap, MaxDist, N) ->
    Active = [I || I <- lists:seq(0,N-1), (Mask band (1 bsl I)) =:= 0],
    case length(Active) of
        0 -> true;
        1 -> true;
        _ -> all_pairs_ok(Active, DistMap, MaxDist)
    end.

all_pairs_ok([H|T], Map, MaxDist) ->
    case lists:all(
            fun(X) ->
                D = maps:get({H,X}, Map),
                D =< MaxDist
            end,
            T) of
        false -> false;
        true -> all_pairs_ok(T, Map, MaxDist)
    end;
all_pairs_ok([], _, _) -> true.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_sets(n :: integer, max_distance :: integer, roads :: [[integer]]) :: integer
  def number_of_sets(n, max_distance, roads) do
    import Bitwise

    inf = 1_000_000_000

    base_dist =
      for i <- 0..(n - 1), j <- 0..(n - 1), into: %{} do
        if i == j, do: {{i, j}, 0}, else: {{i, j}, inf}
      end

    dist0 = Enum.reduce(roads, base_dist, fn [u, v, w], acc ->
      key_uv = {u, v}
      key_vu = {v, u}
      cur_uv = Map.get(acc, key_uv)
      cur_vu = Map.get(acc, key_vu)

      acc
      |> Map.put(key_uv, min(cur_uv, w))
      |> Map.put(key_vu, min(cur_vu, w))
    end)

    total_masks = 1 <<< n
    max_mask = total_masks - 1

    Enum.reduce(0..max_mask, 0, fn closed_mask, ans ->
      active_mask = max_mask ^^^ closed_mask

      active_vertices =
        for v <- 0..(n - 1), ((active_mask >>> v) &&& 1) == 1, do: v

      if length(active_vertices) <= 1 do
        ans + 1
      else
        d =
          Enum.reduce(active_vertices, dist0, fn k, d_k ->
            Enum.reduce(active_vertices, d_k, fn i, d_i ->
              dik = Map.get(d_i, {i, k})

              Enum.reduce(active_vertices, d_i, fn j, d_j ->
                dkj = Map.get(d_j, {k, j})
                dij = Map.get(d_j, {i, j})
                new = dik + dkj

                if new < dij do
                  Map.put(d_j, {i, j}, new)
                else
                  d_j
                end
              end)
            end)
          end)

        valid =
          Enum.all?(active_vertices, fn i ->
            Enum.all?(active_vertices, fn j ->
              if i == j do
                true
              else
                Map.get(d, {i, j}) <= max_distance
              end
            end)
          end)

        if valid, do: ans + 1, else: ans
      end
    end)
  end
end
```

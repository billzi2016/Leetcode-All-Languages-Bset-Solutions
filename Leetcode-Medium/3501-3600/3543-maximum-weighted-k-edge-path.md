# 3543. Maximum Weighted K-Edge Path

## Cpp

```cpp
class Solution {
public:
    int maxWeight(int n, vector<vector<int>>& edges, int k, int t) {
        const int MAXT = 605; // t <= 600
        if (k == 0) return (0 < t ? 0 : -1);
        struct Edge {int u,v,w;};
        vector<Edge> es;
        es.reserve(edges.size());
        for (auto &e: edges) {
            es.push_back({e[0], e[1], e[2]});
        }
        // dp[len][node] -> bitset of achievable sums (< t)
        vector<vector<bitset<MAXT>>> dp(k + 1, vector<bitset<MAXT>>(n));
        for (const auto &e : es) {
            if (e.w < t) dp[1][e.v].set(e.w);
        }
        bitset<MAXT> mask;
        for (int i = 0; i < t; ++i) mask.set(i);
        for (int len = 2; len <= k; ++len) {
            for (const auto &e : es) {
                // shift previous sums by edge weight
                bitset<MAXT> shifted = (dp[len - 1][e.u] << e.w) & mask;
                dp[len][e.v] |= shifted;
            }
        }
        int ans = -1;
        for (int node = 0; node < n; ++node) {
            for (int sum = t - 1; sum >= 0; --sum) {
                if (dp[k][node].test(sum)) {
                    ans = sum;
                    break;
                }
            }
            if (ans != -1) break;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maxWeight(int n, int[][] edges, int k, int t) {
        // Build adjacency list
        List<int[]>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        int[] indeg = new int[n];
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].add(new int[]{v, w});
            indeg[v]++;
        }

        // Topological order
        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 0; i < n; i++) if (indeg[i] == 0) dq.add(i);
        List<Integer> topo = new ArrayList<>(n);
        while (!dq.isEmpty()) {
            int u = dq.poll();
            topo.add(u);
            for (int[] e : adj[u]) {
                indeg[e[0]]--;
                if (indeg[e[0]] == 0) dq.add(e[0]);
            }
        }

        // DP: dp[node][edgesUsed] -> BitSet of reachable sums (< t)
        BitSet[][] dp = new BitSet[n][k + 1];
        for (int i = 0; i < n; i++) {
            dp[i][0] = new BitSet(t);
            dp[i][0].set(0); // zero edges, sum 0
        }

        for (int u : topo) {
            for (int[] e : adj[u]) {
                int v = e[0];
                int w = e[1];
                for (int used = 0; used < k; used++) {
                    BitSet cur = dp[u][used];
                    if (cur == null || cur.isEmpty()) continue;
                    // shift left by w
                    BitSet shifted = new BitSet(t);
                    for (int bit = cur.nextSetBit(0); bit >= 0; bit = cur.nextSetBit(bit + 1)) {
                        int ns = bit + w;
                        if (ns < t) shifted.set(ns);
                    }
                    if (shifted.isEmpty()) continue;
                    if (dp[v][used + 1] == null) dp[v][used + 1] = new BitSet(t);
                    dp[v][used + 1].or(shifted);
                }
            }
        }

        int ans = -1;
        for (int i = 0; i < n; i++) {
            BitSet bs = dp[i][k];
            if (bs != null && !bs.isEmpty()) {
                int cand = bs.previousSetBit(t - 1);
                if (cand > ans) ans = cand;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxWeight(self, n, edges, k, t):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :type t: int
        :rtype: int
        """
        if t <= 0:
            return -1
        mask = (1 << t) - 1  # keep bits for sums < t

        # dp[length][node] -> bitmask of achievable sums
        dp = [[0] * n for _ in range(k + 1)]
        for v in range(n):
            dp[0][v] = 1  # sum 0 with 0 edges

        for length in range(k):
            cur_dp = dp[length]
            nxt_dp = dp[length + 1]
            for u, v, w in edges:
                bits = cur_dp[u]
                if bits:
                    shifted = (bits << w) & mask
                    if shifted:
                        nxt_dp[v] |= shifted

        final_bits = 0
        for node in range(n):
            final_bits |= dp[k][node]

        if final_bits == 0:
            return -1
        # highest set bit gives maximum sum < t
        return final_bits.bit_length() - 1
```

## Python3

```python
from typing import List
from collections import deque

class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        limit_mask = (1 << t) - 1  # keep bits for sums < t
        dp = [[0] * (k + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1  # sum 0 with 0 edges

        adj = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v, w in edges:
            adj[u].append((v, w))
            indeg[v] += 1

        q = deque([i for i in range(n) if indeg[i] == 0])
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        for u in topo:
            for v, w in adj[u]:
                shift = w
                for j in range(k):
                    mask = dp[u][j]
                    if mask:
                        new_mask = (mask << shift) & limit_mask
                        if new_mask:
                            dp[v][j + 1] |= new_mask

        final_mask = 0
        for i in range(n):
            final_mask |= dp[i][k]

        if final_mask == 0:
            return -1
        return final_mask.bit_length() - 1
```

## C

```c
#include <stdlib.h>
#include <string.h>

int maxWeight(int n, int** edges, int edgesSize, int* edgesColSize, int k, int t) {
    if (k == 0) return -1; // need at least one edge to have weight
    
    /* Build indegree for topological order */
    int *indeg = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        indeg[v]++;
    }
    
    /* Kahn's algorithm */
    int *queue = (int*)malloc(n * sizeof(int));
    int qh = 0, qt = 0;
    for (int i = 0; i < n; ++i) if (indeg[i] == 0) queue[qt++] = i;
    
    int *topo = (int*)malloc(n * sizeof(int));
    int tp = 0;
    while (qh < qt) {
        int u = queue[qh++];
        topo[tp++] = u;
        for (int i = 0; i < edgesSize; ++i) {
            if (edges[i][0] == u) {
                int v = edges[i][1];
                if (--indeg[v] == 0) queue[qt++] = v;
            }
        }
    }
    
    free(indeg);
    free(queue);
    
    /* DP: dp[node][edgeCount][sum] */
    static unsigned char dp[301][301][601]; // max constraints
    memset(dp, 0, sizeof(dp));
    for (int i = 0; i < n; ++i) dp[i][0][0] = 1;
    
    for (int idx = 0; idx < tp; ++idx) {
        int u = topo[idx];
        for (int e = 0; e < edgesSize; ++e) {
            if (edges[e][0] != u) continue;
            int v = edges[e][1];
            int w = edges[e][2];
            for (int cnt = 0; cnt < k; ++cnt) {
                for (int sum = 0; sum < t; ++sum) {
                    if (!dp[u][cnt][sum]) continue;
                    int ns = sum + w;
                    if (ns < t) dp[v][cnt + 1][ns] = 1;
                }
            }
        }
    }
    
    free(topo);
    
    int ans = -1;
    for (int i = 0; i < n; ++i) {
        for (int sum = t - 1; sum >= 0; --sum) {
            if (dp[i][k][sum]) {
                if (sum > ans) ans = sum;
                break; // larger sums already checked
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxWeight(int n, int[][] edges, int k, int t) {
        var adj = new List<(int to, int w)>[n];
        var indeg = new int[n];
        foreach (var e in edges) {
            int u = e[0], v = e[1], w = e[2];
            if (adj[u] == null) adj[u] = new List<(int, int)>();
            adj[u].Add((v, w));
            indeg[v]++;
        }

        var order = new List<int>();
        var q = new Queue<int>();
        for (int i = 0; i < n; i++) if (indeg[i] == 0) q.Enqueue(i);
        while (q.Count > 0) {
            int u = q.Dequeue();
            order.Add(u);
            if (adj[u] != null) {
                foreach (var edge in adj[u]) {
                    indeg[edge.to]--;
                    if (indeg[edge.to] == 0) q.Enqueue(edge.to);
                }
            }
        }

        var dp = new bool[n, k + 1, t];
        for (int i = 0; i < n; i++) dp[i, 0, 0] = true;

        foreach (int u in order) {
            if (adj[u] == null) continue;
            foreach (var (v, w) in adj[u]) {
                for (int e = 0; e < k; e++) {
                    int ne = e + 1;
                    for (int s = 0; s < t; s++) {
                        if (!dp[u, e, s]) continue;
                        int ns = s + w;
                        if (ns < t) dp[v, ne, ns] = true;
                    }
                }
            }
        }

        int ans = -1;
        for (int s = t - 1; s >= 0; s--) {
            bool found = false;
            for (int i = 0; i < n && !found; i++) {
                if (dp[i, k, s]) {
                    ans = s;
                    found = true;
                }
            }
            if (found) break;
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
 * @param {number} k
 * @param {number} t
 * @return {number}
 */
var maxWeight = function(n, edges, k, t) {
    // build adjacency list and indegree for topological sort
    const adj = Array.from({length: n}, () => []);
    const indeg = new Array(n).fill(0);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        indeg[v]++;
    }
    // Kahn's algorithm
    const queue = [];
    for (let i = 0; i < n; ++i) if (indeg[i] === 0) queue.push(i);
    const topo = [];
    while (queue.length) {
        const u = queue.shift();
        topo.push(u);
        for (const [v] of adj[u]) {
            indeg[v]--;
            if (indeg[v] === 0) queue.push(v);
        }
    }
    // dp[node][edgesUsed] = max sum (< t) achievable
    const dp = Array.from({length: n}, () => new Array(k + 1).fill(-Infinity));
    for (let i = 0; i < n; ++i) dp[i][0] = 0;
    // propagate in topological order
    for (const u of topo) {
        for (const [v, w] of adj[u]) {
            for (let e = 0; e < k; ++e) {
                const cur = dp[u][e];
                if (cur === -Infinity) continue;
                const ns = cur + w;
                if (ns < t && ns > dp[v][e + 1]) {
                    dp[v][e + 1] = ns;
                }
            }
        }
    }
    let ans = -Infinity;
    for (let i = 0; i < n; ++i) {
        if (dp[i][k] > ans) ans = dp[i][k];
    }
    return ans === -Infinity ? -1 : ans;
};
```

## Typescript

```typescript
function maxWeight(n: number, edges: number[][], k: number, t: number): number {
    const adj: Array<Array<[number, number]>> = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
    }

    // dp[node][edgesUsed][weight] = reachable (0/1)
    const dp: Uint8Array[][] = Array.from({ length: n }, () =>
        Array.from({ length: k + 1 }, () => new Uint8Array(t))
    );

    for (let u = 0; u < n; ++u) {
        dp[u][0][0] = 1;
    }

    for (let e = 0; e < k; ++e) {
        for (let u = 0; u < n; ++u) {
            const cur = dp[u][e];
            // iterate over possible sums
            for (let s = 0; s < t; ++s) {
                if (!cur[s]) continue;
                for (const [v, w] of adj[u]) {
                    const ns = s + w;
                    if (ns < t) {
                        dp[v][e + 1][ns] = 1;
                    }
                }
            }
        }
    }

    let ans = -1;
    for (let u = 0; u < n; ++u) {
        const finalArr = dp[u][k];
        for (let s = t - 1; s >= 0; --s) {
            if (finalArr[s]) {
                if (s > ans) ans = s;
                break; // found max for this node
            }
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $k
     * @param Integer $t
     * @return Integer
     */
    function maxWeight($n, $edges, $k, $t) {
        // adjacency list and indegree for topological order
        $adj = array_fill(0, $n, []);
        $indeg = array_fill(0, $n, 0);
        foreach ($edges as $e) {
            [$u, $v, $w] = $e;
            $adj[$u][] = [$v, $w];
            $indeg[$v]++;
        }

        // topological order (Kahn's algorithm)
        $queue = new SplQueue();
        for ($i = 0; $i < $n; $i++) {
            if ($indeg[$i] == 0) $queue->enqueue($i);
        }
        $topo = [];
        while (!$queue->isEmpty()) {
            $u = $queue->dequeue();
            $topo[] = $u;
            foreach ($adj[$u] as $edge) {
                [$v, $_] = $edge;
                $indeg[$v]--;
                if ($indeg[$v] == 0) $queue->enqueue($v);
            }
        }

        // bitset parameters
        $BITS = 64;
        $segCount = intdiv($t + $BITS - 1, $BITS);   // number of 64‑bit segments

        // dp[node][edges] => array of $segCount integers (bitset)
        $dp = array_fill(0, $n, null);
        for ($i = 0; $i < $n; $i++) {
            $dp[$i] = array_fill(0, $k + 1, null);
            for ($e = 0; $e <= $k; $e++) {
                $dp[$i][$e] = array_fill(0, $segCount, 0);
            }
            // zero edges -> sum 0 reachable
            $dp[$i][0][0] = 1;
        }

        // propagate DP along topological order
        foreach ($topo as $u) {
            foreach ($adj[$u] as $edge) {
                [$v, $w] = $edge;
                for ($e = 0; $e < $k; $e++) {
                    $src = $dp[$u][$e];
                    // quick skip if empty
                    $has = false;
                    foreach ($src as $val) { if ($val != 0) { $has = true; break; } }
                    if (!$has) continue;

                    $dest =& $dp[$v][$e + 1];

                    $full = intdiv($w, $BITS);
                    $off  = $w % $BITS;
                    for ($iSeg = $segCount - 1; $iSeg >= 0; $iSeg--) {
                        $srcIdx = $iSeg - $full;
                        if ($srcIdx < 0) continue;

                        $val = $src[$srcIdx] << $off;
                        if ($off != 0 && $srcIdx - 1 >= 0) {
                            // carry bits from lower segment
                            $carry = $src[$srcIdx - 1] >> (self::$BITS - $off);
                            $maskCarry = (1 << $off) - 1;   // off <=10, safe
                            $val |= ($carry & $maskCarry);
                        }
                        $dest[$iSeg] |= $val;
                    }

                    // mask bits beyond t-1 in the highest segment
                    $lastIdx = $segCount - 1;
                    $lastOffset = ($t - 1) % $BITS;
                    if ($lastOffset != $BITS - 1) {
                        $mask = (1 << ($lastOffset + 1)) - 1;
                        $dest[$lastIdx] &= $mask;
                    }
                }
            }
        }

        // find maximum sum < t with exactly k edges
        $ans = -1;
        for ($i = 0; $i < $n && $ans == -1; $i++) {
            $bits = $dp[$i][$k];
            for ($seg = $segCount - 1; $seg >= 0; $seg--) {
                $val = $bits[$seg];
                if ($val == 0) continue;
                // locate highest set bit in this segment
                for ($bit = $BITS - 1; $bit >= 0; $bit--) {
                    if ((($val >> $bit) & 1) == 1) {
                        $sum = $seg * $BITS + $bit;
                        if ($sum < $t) {
                            $ans = $sum;
                        }
                        break 2;
                    }
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxWeight(_ n: Int, _ edges: [[Int]], _ k: Int, _ t: Int) -> Int {
        if t <= 0 { return -1 }
        // dp[node][len][sum] = reachable
        var dp = Array(
            repeating: Array(
                repeating: [Bool](repeating: false, count: t),
                count: k + 1
            ),
            count: n
        )
        for node in 0..<n {
            dp[node][0][0] = true
        }
        if k == 0 {
            return 0 < t ? 0 : -1
        }
        for len in 1...k {
            for edge in edges {
                let u = edge[0]
                let v = edge[1]
                let w = edge[2]
                if w >= t { continue } // cannot fit even from sum 0
                let limit = t - w
                var s = 0
                while s < limit {
                    if dp[u][len - 1][s] {
                        dp[v][len][s + w] = true
                    }
                    s += 1
                }
            }
        }
        var ans = -1
        for node in 0..<n {
            for sum in 0..<t {
                if dp[node][k][sum] && sum > ans {
                    ans = sum
                }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxWeight(n: Int, edges: Array<IntArray>, k: Int, t: Int): Int {
        // Build adjacency list
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        val indeg = IntArray(n)
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val w = e[2]
            adj[u].add(Pair(v, w))
            indeg[v]++
        }

        // Topological order
        val queue: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
        for (i in 0 until n) if (indeg[i] == 0) queue.add(i)
        val topo = mutableListOf<Int>()
        while (!queue.isEmpty()) {
            val u = queue.poll()
            topo.add(u)
            for ((v, _) in adj[u]) {
                indeg[v]--
                if (indeg[v] == 0) queue.add(v)
            }
        }

        // dp[node][edgesUsed][sum] = reachable
        val dp = Array(n) { Array(k + 1) { BooleanArray(t) } }
        for (i in 0 until n) {
            dp[i][0][0] = true
        }

        for (u in topo) {
            for ((v, w) in adj[u]) {
                // propagate for each possible number of edges used so far
                for (used in 0 until k) {
                    val src = dp[u][used]
                    val dst = dp[v][used + 1]
                    // iterate sums where src is true and sum + w < t
                    var s = 0
                    while (s + w < t) {
                        if (src[s]) {
                            dst[s + w] = true
                        }
                        s++
                    }
                }
            }
        }

        var ans = -1
        for (i in 0 until n) {
            val arr = dp[i][k]
            for (s in 0 until t) {
                if (arr[s]) {
                    if (s > ans) ans = s
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:typed_data';

class Solution {
  int maxWeight(int n, List<List<int>> edges, int k, int t) {
    if (t <= 0 || k < 0) return -1;
    int segCount = (t + 63) >> 6; // number of 64‑bit segments
    // dp[edges][node] -> bitset of achievable sums (< t)
    List<List<Uint64List>> dp = List.generate(
        k + 1, (_) => List.generate(n, (_) => Uint64List(segCount)));

    // path with zero edges has sum 0 at any starting node
    for (int i = 0; i < n; ++i) {
      dp[0][i][0] = 1;
    }

    // build adjacency list and indegrees for topological order
    List<List<List<int>>> adj = List.generate(n, (_) => []);
    List<int> indeg = List.filled(n, 0);
    for (var e in edges) {
      int u = e[0], v = e[1], w = e[2];
      adj[u].add([v, w]);
      indeg[v]++;
    }

    // Kahn's algorithm
    List<int> queue = [];
    for (int i = 0; i < n; ++i) {
      if (indeg[i] == 0) queue.add(i);
    }
    int qIdx = 0;
    while (qIdx < queue.length) {
      int node = queue[qIdx++];
      for (var edge in adj[node]) {
        indeg[edge[0]]--;
        if (indeg[edge[0]] == 0) queue.add(edge[0]);
      }
    }

    // mask for the last segment to keep bits < t
    int lastBits = t & 63;
    int lastMask = lastBits == 0 ? -1 : ((1 << lastBits) - 1);

    // DP propagation following topological order
    for (int node in queue) {
      for (var edge in adj[node]) {
        int to = edge[0];
        int w = edge[1];
        int whole = w >> 6;
        int offset = w & 63;

        for (int e = 0; e < k; ++e) {
          Uint64List src = dp[e][node];
          // quick check if src has any bit set
          bool has = false;
          for (int s = 0; s < segCount; ++s) {
            if (src[s] != 0) {
              has = true;
              break;
            }
          }
          if (!has) continue;

          Uint64List tgt = dp[e + 1][to];
          // shift left by w and OR into target
          for (int seg = segCount - 1; seg >= 0; --seg) {
            int srcIdx = seg - whole;
            if (srcIdx < 0) continue;
            int val = src[srcIdx] << offset;
            if (offset != 0 && srcIdx > 0) {
              val |= src[srcIdx - 1] >> (64 - offset);
            }
            tgt[seg] |= val;
          }
          // apply mask to the last segment
          if (lastMask != -1) {
            tgt[segCount - 1] &= lastMask;
          }
        }
      }
    }

    int answer = -1;
    for (int node = 0; node < n; ++node) {
      Uint64List bits = dp[k][node];
      for (int segIdx = segCount - 1; segIdx >= 0; --segIdx) {
        int val = bits[segIdx];
        if (val == 0) continue;
        // highest set bit in this segment
        int pos = segIdx * 64 + (val.bitLength - 1);
        if (pos < t && pos > answer) answer = pos;
        break; // no need to check lower segments for this node
      }
    }
    return answer;
  }
}
```

## Golang

```go
func maxWeight(n int, edges [][]int, k int, t int) int {
	if t <= 0 || k < 0 {
		return -1
	}
	// adjacency list with weight
	type edge struct{ to, w int }
	graph := make([][]edge, n)
	indeg := make([]int, n)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		graph[u] = append(graph[u], edge{v, w})
		indeg[v]++
	}
	// topological order
	queue := make([]int, 0, n)
	for i := 0; i < n; i++ {
		if indeg[i] == 0 {
			queue = append(queue, i)
		}
	}
	order := make([]int, 0, n)
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		order = append(order, u)
		for _, e := range graph[u] {
			indeg[e.to]--
			if indeg[e.to] == 0 {
				queue = append(queue, e.to)
			}
		}
	}
	// dp[node][edgesUsed][sum] = reachable
	dp := make([][][]bool, n)
	for i := 0; i < n; i++ {
		dp[i] = make([][]bool, k+1)
		for e := 0; e <= k; e++ {
			dp[i][e] = make([]bool, t) // sums 0..t-1
		}
		dp[i][0][0] = true // start at any node with 0 edges and sum 0
	}

	for _, u := range order {
		if len(graph[u]) == 0 {
			continue
		}
		for _, ed := range graph[u] {
			v, w := ed.to, ed.w
			// propagate for each possible edge count
			for e := 0; e < k; e++ {
				src := dp[u][e]
				dst := dp[v][e+1]
				if src == nil || dst == nil {
					continue
				}
				limit := t - w
				if limit <= 0 {
					continue
				}
				for s := 0; s < limit; s++ {
					if src[s] {
						dst[s+w] = true
					}
				}
			}
		}
	}

	ans := -1
	for i := 0; i < n; i++ {
		arr := dp[i][k]
		for s := t - 1; s >= 0; s-- {
			if arr[s] {
				if s > ans {
					ans = s
				}
				break // found max for this node
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_weight(n, edges, k, t)
  # Edge case: zero edges required
  return 0 if k == 0

  limit_mask = (1 << t) - 1
  dp = Array.new(k + 1) { Array.new(n, 0) }

  # Initialize paths of length 1
  edges.each do |u, v, w|
    next unless w < t
    dp[1][v] |= (1 << w)
  end

  (2..k).each do |len|
    edges.each do |u, v, w|
      prev_mask = dp[len - 1][u]
      next if prev_mask == 0
      shifted = (prev_mask << w) & limit_mask
      dp[len][v] |= shifted
    end
  end

  best = -1
  dp[k].each do |mask|
    next if mask == 0
    cur = mask.bit_length - 1
    best = cur if cur > best
  end
  best
end
```

## Scala

```scala
import scala.collection.mutable

object Solution {
  def maxWeight(n: Int, edges: Array[Array[Int]], k: Int, t: Int): Int = {
    if (k == 0) return if (0 < t) 0 else -1

    // adjacency list
    val adj = Array.fill[List[(Int, Int)]](n)(Nil)
    val indeg = new Array[Int](n)
    for (e <- edges) {
      val u = e(0); val v = e(1); val w = e(2)
      adj(u) = (v, w) :: adj(u)
      indeg(v) += 1
    }

    // topological order
    val queue = new mutable.Queue[Int]()
    for (i <- 0 until n if indeg(i) == 0) queue.enqueue(i)
    val topo = new mutable.ArrayBuffer[Int]()
    while (queue.nonEmpty) {
      val u = queue.dequeue()
      topo += u
      for ((v, _) <- adj(u)) {
        indeg(v) -= 1
        if (indeg(v) == 0) queue.enqueue(v)
      }
    }

    // dp[node][len] -> BitSet of achievable sums (< t)
    val dp = Array.ofDim[mutable.BitSet](n, k + 1)
    for (i <- 0 until n; j <- 0 to k) {
      dp(i)(j) = mutable.BitSet.empty
    }

    // initialize length 1 paths directly from edges
    for (e <- edges) {
      val u = e(0); val v = e(1); val w = e(2)
      if (w < t) dp(v)(1).add(w)
    }

    // propagate in topological order
    for (u <- topo) {
      for (len <- 1 until k) {
        val curSet = dp(u)(len)
        if (curSet.nonEmpty) {
          for ((v, w) <- adj(u)) {
            val targetSet = dp(v)(len + 1)
            var it = curSet.iterator
            while (it.hasNext) {
              val s = it.next()
              val ns = s + w
              if (ns < t) targetSet.add(ns)
            }
          }
        }
      }
    }

    // find maximum sum with exactly k edges
    var ans = -1
    for (i <- 0 until n) {
      val setK = dp(i)(k)
      if (setK.nonEmpty) {
        val maxSum = setK.max
        if (maxSum > ans) ans = maxSum
      }
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_weight(n: i32, edges: Vec<Vec<i32>>, k: i32, t: i32) -> i32 {
        let n = n as usize;
        let k = k as usize;
        let t = t as usize;

        // Build adjacency list and indegree for topological sort
        let mut adj: Vec<Vec<(usize, usize)>> = vec![Vec::new(); n];
        let mut indeg = vec![0usize; n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2] as usize;
            adj[u].push((v, w));
            indeg[v] += 1;
        }

        // Topological order (Kahn's algorithm)
        use std::collections::VecDeque;
        let mut q = VecDeque::new();
        for i in 0..n {
            if indeg[i] == 0 {
                q.push_back(i);
            }
        }
        let mut topo = Vec::with_capacity(n);
        while let Some(u) = q.pop_front() {
            topo.push(u);
            for &(v, _) in adj[u].iter() {
                indeg[v] -= 1;
                if indeg[v] == 0 {
                    q.push_back(v);
                }
            }
        }

        // dp[node][edges_used][sum] = reachable (bool)
        let mut dp = vec![vec![vec![false; t]; k + 1]; n];
        for i in 0..n {
            dp[i][0][0] = true;
        }

        for &u in topo.iter() {
            // For each possible number of edges used so far (except the max)
            if k == 0 { continue; }
            for used in 0..k {
                // Collect reachable sums for this state to avoid mutable/immutable borrow conflict
                let mut sums = Vec::new();
                for s in 0..t {
                    if dp[u][used][s] {
                        sums.push(s);
                    }
                }
                if sums.is_empty() {
                    continue;
                }
                let next_used = used + 1;
                for &(v, w) in adj[u].iter() {
                    for &s in sums.iter() {
                        let ns = s + w;
                        if ns < t {
                            dp[v][next_used][ns] = true;
                        }
                    }
                }
            }
        }

        // Find maximum sum with exactly k edges
        let mut ans: i32 = -1;
        for node in 0..n {
            for s in (0..t).rev() {
                if dp[node][k][s] {
                    ans = s as i32;
                    break;
                }
            }
            if ans != -1 {
                break;
            }
        }

        ans
    }
}
```

## Racket

```racket
(require racket/match)

(define/contract (max-weight n edges k t)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer?)
  (let* ((adj (make-vector n '()))
         (indeg (make-vector n 0)))
    ;; build adjacency list and indegrees
    (for ([e edges])
      (match-define (list u v w) e)
      (vector-set! adj u (cons (list v w) (vector-ref adj u)))
      (vector-set! indeg v (+ (vector-ref indeg v) 1)))
    ;; topological order (Kahn)
    (let loop ((queue (filter (lambda (i) (= (vector-ref indeg i) 0)) (range n)))
               (order '()))
      (if (null? queue)
          (reverse order)
          (let* ((u (car queue))
                 (rest (cdr queue)))
            (for ([edge (vector-ref adj u)])
              (match-define (list v w) edge)
              (vector-set! indeg v (- (vector-ref indeg v) 1))
              (when (= (vector-ref indeg v) 0)
                (set! rest (cons v rest))))
            (loop rest (cons u order))))) ; => topological order list
    => order)

    ;; dp[j][node] = vector of length t with booleans for achievable sums
    (define dp (make-vector (+ k 1) #f))
    (do ([j 0 (+ j 1)]) ((> j k))
      (vector-set! dp j (make-vector n #f))
      (do ([i 0 (+ i 1)]) ((= i n))
        (vector-set! (vector-ref dp j) i (make-vector t #f))))
    ;; base: zero edges, sum 0 reachable at any node
    (do ([i 0 (+ i 1)]) ((= i n))
      (let* ((vec0 (vector-ref (vector-ref dp 0) i)))
        (vector-set! vec0 0 #t)))

    ;; propagate along topological order
    (for ([u order])
      (for ([edge (vector-ref adj u)])
        (match-define (list v w) edge)
        (do ([j 0 (+ j 1)]) ((> j (- k 1)))
          (let* ((src (vector-ref (vector-ref dp j) u))
                 (dst (vector-ref (vector-ref dp (+ j 1)) v)))
            (do ([s 0 (+ s 1)]) ((>= s (- t w))) ; s <= t-w-1
              (when (vector-ref src s)
                (vector-set! dst (+ s w) #t)))))))

    ;; find maximum sum < t with exactly k edges
    (let ([ans -1])
      (do ([i 0 (+ i 1)]) ((= i n))
        (let* ((vec (vector-ref (vector-ref dp k) i)))
          (do ([s (- t 1) (- s 1)]) ((< s 0))
            (when (and (> s ans) (vector-ref vec s))
              (set! ans s)))))
      ans)))
```

## Erlang

```erlang
-spec max_weight(N :: integer(), Edges :: [[integer()]], K :: integer(), T :: integer()) -> integer().
max_weight(N, Edges, K, T) ->
    MaxMask = (1 bsl T) - 1,
    %% initial tuple: each node can have sum 0 (bit 0 set)
    InitTuple = list_to_tuple(lists:duplicate(N, 1)),
    FinalTuple = iterate(K, 0, N, Edges, MaxMask, InitTuple),
    find_max_sum(FinalTuple, T).

%% iterate over edge count
iterate(0, _Cnt, _N, _Edges, _MaxMask, Tuple) ->
    Tuple;
iterate(Remaining, Cnt, N, Edges, MaxMask, CurrTuple) ->
    NextTuple = make_tuple(N, 0),
    UpdatedNext = process_edges(Edges, CurrTuple, NextTuple, MaxMask),
    iterate(Remaining - 1, Cnt + 1, N, Edges, MaxMask, UpdatedNext).

%% process each edge and update masks
process_edges([], _Curr, Acc, _MaxMask) ->
    Acc;
process_edges([[U,V,W]|Rest], Curr, Acc, MaxMask) ->
    MaskU = element(U + 1, Curr),
    Shifted = (MaskU bsl W) band MaxMask,
    OldV = element(V + 1, Acc),
    NewV = OldV bor Shifted,
    UpdatedAcc = setelement(V + 1, Acc, NewV),
    process_edges(Rest, Curr, UpdatedAcc, MaxMask).

%% find the maximum achievable sum (< T) across all nodes
find_max_sum(Tuple, T) ->
    N = tuple_size(Tuple),
    find_max_sum(1, N, Tuple, T - 1, -1).

find_max_sum(I, N, _Tuple, _Pos, Max) when I > N ->
    Max;
find_max_sum(I, N, Tuple, PosLimit, MaxSoFar) ->
    Mask = element(I, Tuple),
    NewMax = case highest_bit(Mask, PosLimit) of
                 -1 -> MaxSoFar;
                 S  -> max(S, MaxSoFar)
             end,
    find_max_sum(I + 1, N, Tuple, PosLimit, NewMax).

%% return the highest set bit index (<= Limit), or -1 if none
highest_bit(_Mask, Limit) when Limit < 0 ->
    -1;
highest_bit(Mask, Limit) ->
    Bit = 1 bsl Limit,
    case Mask band Bit of
        0 -> highest_bit(Mask, Limit - 1);
        _ -> Limit
    end.

max(A, B) when A >= B -> A;
max(_A, B) -> B.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_weight(n :: integer, edges :: [[integer]], k :: integer, t :: integer) :: integer
  def max_weight(n, edges, k, t) do
    # Initialize DP map with sum 0 for path length 0 at every node
    init_map =
      Enum.reduce(0..n - 1, %{}, fn node, acc ->
        Map.put(acc, {node, 0}, MapSet.new([0]))
      end)

    dp =
      Enum.reduce(0..k - 1, init_map, fn e, cur_map ->
        Enum.reduce(edges, cur_map, fn [u, v, w], m ->
          set_u = Map.get(m, {u, e}, MapSet.new())

          if MapSet.size(set_u) == 0 do
            m
          else
            Enum.reduce(set_u, m, fn s, mm ->
              ns = s + w

              if ns < t do
                key = {v, e + 1}
                cur_set = Map.get(mm, key, MapSet.new())
                new_set = MapSet.put(cur_set, ns)
                Map.put(mm, key, new_set)
              else
                mm
              end
            end)
          end
        end)
      end)

    Enum.reduce(0..n - 1, -1, fn node, acc ->
      set_k = Map.get(dp, {node, k}, MapSet.new())

      if MapSet.size(set_k) == 0 do
        acc
      else
        m = Enum.max(set_k)
        if m > acc, do: m, else: acc
      end
    end)
  end
end
```

# 1617. Count Subtrees With Max Distance Between Cities

## Cpp

```cpp
class Solution {
public:
    vector<int> countSubgraphsForEachDiameter(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            int u = e[0] - 1;
            int v = e[1] - 1;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        // all-pairs distances in the original tree
        vector<vector<int>> dist(n, vector<int>(n, 0));
        for (int s = 0; s < n; ++s) {
            queue<int> q;
            vector<int> d(n, -1);
            d[s] = 0;
            q.push(s);
            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (int v : adj[u]) {
                    if (d[v] == -1) {
                        d[v] = d[u] + 1;
                        q.push(v);
                    }
                }
            }
            dist[s] = move(d);
        }

        vector<int> ans(n - 1, 0);
        int totalMask = 1 << n;
        for (int mask = 1; mask < totalMask; ++mask) {
            if (__builtin_popcount(mask) < 2) continue;

            // connectivity check
            int start = __builtin_ctz(mask);
            queue<int> q;
            int visitedMask = 0;
            q.push(start);
            visitedMask |= (1 << start);
            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (int v : adj[u]) {
                    if ((mask >> v) & 1 && !(visitedMask >> v & 1)) {
                        visitedMask |= (1 << v);
                        q.push(v);
                    }
                }
            }
            if (visitedMask != mask) continue; // not a connected subtree

            // collect nodes in this subset
            vector<int> nodes;
            int tmp = mask;
            while (tmp) {
                int i = __builtin_ctz(tmp);
                nodes.push_back(i);
                tmp &= (tmp - 1);
            }

            // compute diameter
            int diam = 0;
            for (size_t i = 0; i < nodes.size(); ++i) {
                for (size_t j = i + 1; j < nodes.size(); ++j) {
                    diam = max(diam, dist[nodes[i]][nodes[j]]);
                }
            }
            ans[diam - 1]++; // diam >=1
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] countSubgraphsForEachDiameter(int n, int[][] edges) {
        @SuppressWarnings("unchecked")
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0] - 1;
            int v = e[1] - 1;
            adj[u].add(v);
            adj[v].add(u);
        }

        int[] ans = new int[n - 1];
        int totalMask = 1 << n;

        for (int mask = 0; mask < totalMask; mask++) {
            if (Integer.bitCount(mask) < 2) continue;

            // find a start node in the subset
            int start = Integer.numberOfTrailingZeros(mask);

            // connectivity check using BFS limited to nodes in mask
            int visitedMask = bfsReachable(start, mask, adj);
            if (visitedMask != mask) continue; // not connected

            // first BFS to find farthest node from start within the subset
            int farNode = bfsFarthestNode(start, mask, adj);

            // second BFS from farNode to get diameter
            int diameter = bfsMaxDistance(farNode, mask, adj);
            ans[diameter - 1]++; // diameters are >=1
        }

        return ans;
    }

    private int bfsReachable(int src, int mask, List<Integer>[] adj) {
        int n = adj.length;
        int[] q = new int[n];
        int head = 0, tail = 0;
        int visitedMask = 0;

        q[tail++] = src;
        visitedMask |= (1 << src);

        while (head < tail) {
            int cur = q[head++];
            for (int nb : adj[cur]) {
                if ((mask & (1 << nb)) != 0 && (visitedMask & (1 << nb)) == 0) {
                    visitedMask |= (1 << nb);
                    q[tail++] = nb;
                }
            }
        }
        return visitedMask;
    }

    private int bfsFarthestNode(int src, int mask, List<Integer>[] adj) {
        int n = adj.length;
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        int[] q = new int[n];
        int head = 0, tail = 0;

        dist[src] = 0;
        q[tail++] = src;
        int farNode = src;

        while (head < tail) {
            int cur = q[head++];
            for (int nb : adj[cur]) {
                if ((mask & (1 << nb)) != 0 && dist[nb] == -1) {
                    dist[nb] = dist[cur] + 1;
                    q[tail++] = nb;
                    if (dist[nb] > dist[farNode]) farNode = nb;
                }
            }
        }
        return farNode;
    }

    private int bfsMaxDistance(int src, int mask, List<Integer>[] adj) {
        int n = adj.length;
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        int[] q = new int[n];
        int head = 0, tail = 0;

        dist[src] = 0;
        q[tail++] = src;
        int maxDist = 0;

        while (head < tail) {
            int cur = q[head++];
            for (int nb : adj[cur]) {
                if ((mask & (1 << nb)) != 0 && dist[nb] == -1) {
                    dist[nb] = dist[cur] + 1;
                    q[tail++] = nb;
                    if (dist[nb] > maxDist) maxDist = dist[nb];
                }
            }
        }
        return maxDist;
    }
}
```

## Python

```python
class Solution(object):
    def countSubgraphsForEachDiameter(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque

        # build adjacency list (0-indexed)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)

        ans = [0] * (n - 1)

        total_masks = 1 << n
        for mask in range(1, total_masks):
            # need at least two nodes to have a positive diameter
            size = bin(mask).count('1')
            if size < 2:
                continue

            # find any node inside the subset
            start = (mask & -mask).bit_length() - 1

            # first BFS: check connectivity and get farthest node
            visited = [False] * n
            q = deque()
            visited[start] = True
            q.append((start, 0))
            cnt = 1
            far_node = start
            max_dist = 0

            while q:
                node, d = q.popleft()
                if d > max_dist:
                    max_dist = d
                    far_node = node
                for nb in adj[node]:
                    if (mask >> nb) & 1 and not visited[nb]:
                        visited[nb] = True
                        cnt += 1
                        q.append((nb, d + 1))

            # if not all nodes are reachable, it's not a valid subtree
            if cnt != size:
                continue

            # second BFS from far_node to obtain the diameter
            visited2 = [False] * n
            q = deque()
            visited2[far_node] = True
            q.append((far_node, 0))
            diam = 0

            while q:
                node, d = q.popleft()
                if d > diam:
                    diam = d
                for nb in adj[node]:
                    if (mask >> nb) & 1 and not visited2[nb]:
                        visited2[nb] = True
                        q.append((nb, d + 1))

            # diameter is at least 1 here
            ans[diam - 1] += 1

        return ans
```

## Python3

```python
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges):
        from collections import deque

        adj = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)

        # precompute all-pairs distances using BFS from each node
        dist = [[0] * n for _ in range(n)]
        for s in range(n):
            d = [-1] * n
            dq = deque([s])
            d[s] = 0
            while dq:
                u = dq.popleft()
                for v in adj[u]:
                    if d[v] == -1:
                        d[v] = d[u] + 1
                        dq.append(v)
            dist[s] = d

        ans = [0] * (n - 1)

        total_masks = 1 << n
        for mask in range(1, total_masks):
            sz = mask.bit_count()
            if sz < 2:
                continue

            # find any node in the subset to start DFS
            first = (mask & -mask).bit_length() - 1

            # connectivity check within the subset
            stack = [first]
            visited_mask = 0
            while stack:
                u = stack.pop()
                if (visited_mask >> u) & 1:
                    continue
                visited_mask |= 1 << u
                for v in adj[u]:
                    if (mask >> v) & 1 and not ((visited_mask >> v) & 1):
                        stack.append(v)

            if visited_mask != mask:
                continue

            # compute diameter: max distance among all pairs in subset
            diam = 0
            sub = mask
            while sub:
                i_bit = sub & -sub
                i = i_bit.bit_length() - 1
                sub2 = mask
                while sub2:
                    j_bit = sub2 & -sub2
                    j = j_bit.bit_length() - 1
                    if dist[i][j] > diam:
                        diam = dist[i][j]
                    sub2 -= j_bit
                sub -= i_bit

            ans[diam - 1] += 1

        return ans
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countSubgraphsForEachDiameter(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize){
    int adj[15][15];
    int deg[15] = {0};
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0] - 1;
        int v = edges[i][1] - 1;
        adj[u][deg[u]++] = v;
        adj[v][deg[v]++] = u;
    }

    int totalMasks = 1 << n;
    int* ans = (int*)calloc(n - 1, sizeof(int));

    for (int mask = 0; mask < totalMasks; ++mask) {
        if (__builtin_popcount(mask) < 2) continue;

        int start = __builtin_ctz(mask);   // first set bit
        int visitedMask = 0;
        int queue[15];
        int qh = 0, qt = 0;

        queue[qt++] = start;
        visitedMask |= (1 << start);

        while (qh < qt) {
            int cur = queue[qh++];
            for (int j = 0; j < deg[cur]; ++j) {
                int nb = adj[cur][j];
                if ((mask & (1 << nb)) && !(visitedMask & (1 << nb))) {
                    visitedMask |= (1 << nb);
                    queue[qt++] = nb;
                }
            }
        }

        if (visitedMask != mask) continue;   // not connected

        // First BFS to find farthest node from start
        int dist[15];
        for (int i = 0; i < n; ++i) dist[i] = -1;
        qh = qt = 0;
        queue[qt++] = start;
        dist[start] = 0;
        int farNode = start;

        while (qh < qt) {
            int cur = queue[qh++];
            for (int j = 0; j < deg[cur]; ++j) {
                int nb = adj[cur][j];
                if ((mask & (1 << nb)) && dist[nb] == -1) {
                    dist[nb] = dist[cur] + 1;
                    queue[qt++] = nb;
                    if (dist[nb] > dist[farNode]) farNode = nb;
                }
            }
        }

        // Second BFS from farNode to get diameter
        for (int i = 0; i < n; ++i) dist[i] = -1;
        qh = qt = 0;
        queue[qt++] = farNode;
        dist[farNode] = 0;
        int maxDist = 0;

        while (qh < qt) {
            int cur = queue[qh++];
            for (int j = 0; j < deg[cur]; ++j) {
                int nb = adj[cur][j];
                if ((mask & (1 << nb)) && dist[nb] == -1) {
                    dist[nb] = dist[cur] + 1;
                    queue[qt++] = nb;
                    if (dist[nb] > maxDist) maxDist = dist[nb];
                }
            }
        }

        ans[maxDist - 1]++;   // diameter d corresponds to index d-1
    }

    *returnSize = n - 1;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Numerics;

public class Solution {
    public int[] CountSubgraphsForEachDiameter(int n, int[][] edges) {
        // build adjacency list
        List<int>[] adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0] - 1;
            int v = e[1] - 1;
            adj[u].Add(v);
            adj[v].Add(u);
        }

        int[] answer = new int[n - 1];
        int totalMasks = 1 << n;

        for (int mask = 1; mask < totalMasks; mask++) {
            int cnt = BitOperations.PopCount((uint)mask);
            if (cnt < 2) continue; // diameter zero, not needed

            // find any node in the subset
            int start = BitOperations.TrailingZeroCount((uint)mask);

            // connectivity check using BFS within the mask
            int visitedMask = 0;
            Queue<int> q = new Queue<int>();
            q.Enqueue(start);
            visitedMask |= 1 << start;

            while (q.Count > 0) {
                int u = q.Dequeue();
                foreach (int v in adj[u]) {
                    if (((mask >> v) & 1) == 1 && ((visitedMask >> v) & 1) == 0) {
                        visitedMask |= 1 << v;
                        q.Enqueue(v);
                    }
                }
            }

            if (BitOperations.PopCount((uint)visitedMask) != cnt) continue; // not connected

            // first BFS to find farthest node from start
            int farNode = BFS(start, mask, adj, n, out int _);
            // second BFS from farNode to get diameter
            BFS(farNode, mask, adj, n, out int diameter);

            // diameter is at least 1 and at most n-1
            answer[diameter - 1]++;
        }

        return answer;
    }

    private int BFS(int src, int mask, List<int>[] adj, int n, out int maxDist) {
        int[] dist = new int[n];
        for (int i = 0; i < n; i++) dist[i] = -1;

        Queue<int> q = new Queue<int>();
        q.Enqueue(src);
        dist[src] = 0;
        int farNode = src;
        maxDist = 0;

        while (q.Count > 0) {
            int u = q.Dequeue();
            foreach (int v in adj[u]) {
                if (((mask >> v) & 1) == 1 && dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    if (dist[v] > maxDist) {
                        maxDist = dist[v];
                        farNode = v;
                    }
                    q.Enqueue(v);
                }
            }
        }

        return farNode;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var countSubgraphsForEachDiameter = function(n, edges) {
    const adj = Array.from({length: n}, () => []);
    for (const [u, v] of edges) {
        const a = u - 1, b = v - 1;
        adj[a].push(b);
        adj[b].push(a);
    }

    const ans = new Array(n - 1).fill(0);

    // popcount
    const bitCount = (x) => {
        let c = 0;
        while (x) { c += x & 1; x >>>= 1; }
        return c;
    };

    // BFS limited to vertices in mask, returns farthest node and distance array
    const bfs = (start, mask) => {
        const dist = new Int16Array(n);
        for (let i = 0; i < n; ++i) dist[i] = -1;
        const q = new Array(n);
        let head = 0, tail = 0;
        q[tail++] = start;
        dist[start] = 0;
        let far = start;

        while (head < tail) {
            const v = q[head++];
            if (dist[v] > dist[far]) far = v;
            for (const nb of adj[v]) {
                if (((mask >> nb) & 1) && dist[nb] === -1) {
                    dist[nb] = dist[v] + 1;
                    q[tail++] = nb;
                }
            }
        }
        return {far, dist};
    };

    const totalMasks = 1 << n;
    for (let mask = 1; mask < totalMasks; ++mask) {
        const sz = bitCount(mask);
        if (sz < 2) continue;

        // find any set bit as start
        let start = 0;
        while (((mask >> start) & 1) === 0) ++start;

        const firstBFS = bfs(start, mask);
        // check connectivity
        let visited = 0;
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1 && firstBFS.dist[i] !== -1) visited++;
        }
        if (visited !== sz) continue; // not connected

        const u = firstBFS.far;
        const secondBFS = bfs(u, mask);
        let diameter = 0;
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1 && secondBFS.dist[i] > diameter) {
                diameter = secondBFS.dist[i];
            }
        }
        // diameter is at least 1
        ans[diameter - 1]++;
    }

    return ans;
};
```

## Typescript

```typescript
function countSubgraphsForEachDiameter(n: number, edges: number[][]): number[] {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        const a = u - 1;
        const b = v - 1;
        adj[a].push(b);
        adj[b].push(a);
    }

    // all‑pair shortest distances
    const dist: number[][] = Array.from({ length: n }, () => Array(n).fill(Infinity));
    for (let s = 0; s < n; ++s) {
        const q: number[] = [];
        dist[s][s] = 0;
        q.push(s);
        let qi = 0;
        while (qi < q.length) {
            const cur = q[qi++];
            for (const nb of adj[cur]) {
                if (dist[s][nb] === Infinity) {
                    dist[s][nb] = dist[s][cur] + 1;
                    q.push(nb);
                }
            }
        }
    }

    const ans: number[] = Array(n - 1).fill(0);
    const totalMask = 1 << n;

    for (let mask = 1; mask < totalMask; ++mask) {
        const sz = popcnt(mask);
        if (sz < 2) continue;

        // find any set bit as start
        let start = 0;
        while (((mask >> start) & 1) === 0) ++start;

        const visitedMask = bfsWithinMask(start, mask);
        if (visitedMask !== mask) continue; // not connected

        // compute diameter inside this subset
        let diam = 0;
        for (let i = 0; i < n; ++i) {
            if (((mask >> i) & 1) === 0) continue;
            for (let j = i + 1; j < n; ++j) {
                if (((mask >> j) & 1) === 0) continue;
                const d = dist[i][j];
                if (d > diam) diam = d;
            }
        }
        ans[diam - 1]++; // diam >= 1
    }

    return ans;

    function popcnt(x: number): number {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            ++cnt;
        }
        return cnt;
    }

    function bfsWithinMask(start: number, mask: number): number {
        const q: number[] = [];
        let visited = 0;
        q.push(start);
        visited |= 1 << start;
        let qi = 0;
        while (qi < q.length) {
            const cur = q[qi++];
            for (const nb of adj[cur]) {
                if (((mask >> nb) & 1) === 0) continue; // not in subset
                if (((visited >> nb) & 1) === 0) {
                    visited |= 1 << nb;
                    q.push(nb);
                }
            }
        }
        return visited;
    }
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer[]
     */
    public function countSubgraphsForEachDiameter($n, $edges) {
        // build adjacency list (0-indexed)
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0] - 1;
            $v = $e[1] - 1;
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }

        $res = array_fill(0, $n - 1, 0);
        $totalMask = 1 << $n;

        for ($mask = 1; $mask < $totalMask; $mask++) {
            $cnt = $this->popcount($mask);
            if ($cnt < 2) continue; // need at least two nodes

            // find any node in the subset
            $start = -1;
            for ($i = 0; $i < $n; $i++) {
                if (($mask >> $i) & 1) {
                    $start = $i;
                    break;
                }
            }

            // check connectivity using BFS limited to nodes in mask
            $queue = [];
            $head = 0;
            $queue[] = $start;
            $visMask = 1 << $start;

            while ($head < count($queue)) {
                $u = $queue[$head++];
                foreach ($adj[$u] as $v) {
                    if ((($mask >> $v) & 1) && !(($visMask >> $v) & 1)) {
                        $visMask |= (1 << $v);
                        $queue[] = $v;
                    }
                }
            }

            if ($this->popcount($visMask) != $cnt) continue; // not connected

            // first BFS to find farthest node from start
            list($farNode, ) = $this->bfsFarthest($start, $mask, $adj, $n);
            // second BFS from farNode to get diameter
            list($_, $diameter) = $this->bfsFarthest($farNode, $mask, $adj, $n);

            $res[$diameter - 1]++; // diameters are >=1
        }

        return $res;
    }

    private function popcount(int $x): int {
        $cnt = 0;
        while ($x) {
            $x &= $x - 1;
            $cnt++;
        }
        return $cnt;
    }

    /**
     * @return array [farthestNode, maxDistance]
     */
    private function bfsFarthest(int $src, int $mask, array &$adj, int $n): array {
        $queue = [];
        $head = 0;
        $queue[] = $src;
        $dist = array_fill(0, $n, -1);
        $dist[$src] = 0;

        $farthestNode = $src;
        $maxDist = 0;

        while ($head < count($queue)) {
            $u = $queue[$head++];
            foreach ($adj[$u] as $v) {
                if ((($mask >> $v) & 1) && $dist[$v] == -1) {
                    $dist[$v] = $dist[$u] + 1;
                    if ($dist[$v] > $maxDist) {
                        $maxDist = $dist[$v];
                        $farthestNode = $v;
                    }
                    $queue[] = $v;
                }
            }
        }

        return [$farthestNode, $maxDist];
    }
}
```

## Swift

```swift
class Solution {
    func countSubgraphsForEachDiameter(_ n: Int, _ edges: [[Int]]) -> [Int] {
        var adj = [[Int]](repeating: [], count: n)
        for e in edges {
            let u = e[0] - 1
            let v = e[1] - 1
            adj[u].append(v)
            adj[v].append(u)
        }
        var ans = [Int](repeating: 0, count: n - 1)
        let totalMask = 1 << n
        
        for mask in 0..<totalMask {
            // skip subsets with less than two nodes
            if mask & (mask - 1) == 0 { continue }
            
            // find any node in the subset
            var start = -1
            for i in 0..<n {
                if ((mask >> i) & 1) == 1 {
                    start = i
                    break
                }
            }
            if start == -1 { continue }
            
            // check connectivity using BFS within the mask
            var visitedMask = 0
            var queue = [Int]()
            var qIdx = 0
            queue.append(start)
            visitedMask |= (1 << start)
            while qIdx < queue.count {
                let node = queue[qIdx]
                qIdx += 1
                for nb in adj[node] {
                    if ((mask >> nb) & 1) == 1 && ((visitedMask >> nb) & 1) == 0 {
                        visitedMask |= (1 << nb)
                        queue.append(nb)
                    }
                }
            }
            if visitedMask != mask { continue } // not connected
            
            // helper BFS to find farthest node and its distance within the subset
            func bfs(_ s: Int) -> (node: Int, dist: Int) {
                var distArr = [Int](repeating: -1, count: n)
                var q = [Int]()
                var idx = 0
                distArr[s] = 0
                q.append(s)
                var farNode = s
                while idx < q.count {
                    let cur = q[idx]
                    idx += 1
                    for nb in adj[cur] {
                        if ((mask >> nb) & 1) == 1 && distArr[nb] == -1 {
                            distArr[nb] = distArr[cur] + 1
                            q.append(nb)
                            if distArr[nb] > distArr[farNode] {
                                farNode = nb
                            }
                        }
                    }
                }
                return (farNode, distArr[farNode])
            }
            
            // double BFS to get diameter
            let first = bfs(start)
            let second = bfs(first.node)
            let diameter = second.dist
            if diameter > 0 {
                ans[diameter - 1] += 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSubgraphsForEachDiameter(n: Int, edges: Array<IntArray>): IntArray {
        val adjList = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0] - 1
            val v = e[1] - 1
            adjList[u].add(v)
            adjList[v].add(u)
        }
        val adj = Array(n) { IntArray(adjList[it].size) }
        for (i in 0 until n) {
            var idx = 0
            for (v in adjList[i]) {
                adj[i][idx++] = v
            }
        }

        val ans = IntArray(n - 1)
        val totalMask = 1 shl n

        for (mask in 0 until totalMask) {
            val sz = Integer.bitCount(mask)
            if (sz < 2) continue

            var first = -1
            for (i in 0 until n) {
                if ((mask and (1 shl i)) != 0) {
                    first = i
                    break
                }
            }

            val bfsInfo = bfs(first, mask, adj, n)
            if (bfsInfo.visited != sz) continue

            val u = bfsInfo.farthestNode
            val bfsInfo2 = bfs(u, mask, adj, n)
            val diam = bfsInfo2.maxDist
            ans[diam - 1]++
        }

        return ans
    }

    private data class BfsResult(val visited: Int, val farthestNode: Int, val maxDist: Int)

    private fun bfs(start: Int, mask: Int, adj: Array<IntArray>, n: Int): BfsResult {
        val dist = IntArray(n) { -1 }
        val queue = IntArray(n)
        var head = 0
        var tail = 0
        dist[start] = 0
        queue[tail++] = start
        var farNode = start
        var visited = 0

        while (head < tail) {
            val u = queue[head++]
            visited++
            for (v in adj[u]) {
                if ((mask and (1 shl v)) != 0 && dist[v] == -1) {
                    dist[v] = dist[u] + 1
                    queue[tail++] = v
                    if (dist[v] > dist[farNode]) farNode = v
                }
            }
        }
        return BfsResult(visited, farNode, dist[farNode])
    }
}
```

## Golang

```go
import "math/bits"

func countSubgraphsForEachDiameter(n int, edges [][]int) []int {
	adj := make([][]int, n)
	for _, e := range edges {
		u, v := e[0]-1, e[1]-1
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}

	// all-pair distances in the tree
	dist := make([][]int, n)
	for i := 0; i < n; i++ {
		dist[i] = make([]int, n)
		queue := []int{i}
		visited := make([]bool, n)
		visited[i] = true
		for len(queue) > 0 {
			cur := queue[0]
			queue = queue[1:]
			for _, nb := range adj[cur] {
				if !visited[nb] {
					visited[nb] = true
					dist[i][nb] = dist[i][cur] + 1
					queue = append(queue, nb)
				}
			}
		}
	}

	ans := make([]int, n-1)
	totalMask := 1 << n

	for mask := 1; mask < totalMask; mask++ {
		if bits.OnesCount(uint(mask)) < 2 {
			continue
		}
		// find a start node in the subset
		start := -1
		for i := 0; i < n; i++ {
			if (mask>>i)&1 == 1 {
				start = i
				break
			}
		}
		// BFS restricted to nodes inside mask
		visitedMask := 0
		queue := []int{start}
		visitedMask |= 1 << start
		for len(queue) > 0 {
			cur := queue[0]
			queue = queue[1:]
			for _, nb := range adj[cur] {
				if (mask>>nb)&1 == 1 && ((visitedMask>>nb)&1) == 0 {
					visitedMask |= 1 << nb
					queue = append(queue, nb)
				}
			}
		}
		if visitedMask != mask {
			continue // not connected
		}

		// compute diameter within this subset
		maxDist := 0
		for i := 0; i < n; i++ {
			if (mask>>i)&1 == 0 {
				continue
			}
			for j := i + 1; j < n; j++ {
				if (mask>>j)&1 == 0 {
					continue
				}
				if dist[i][j] > maxDist {
					maxDist = dist[i][j]
				}
			}
		}
		if maxDist > 0 {
			ans[maxDist-1]++
		}
	}

	return ans
}
```

## Ruby

```ruby
def count_subgraphs_for_each_diameter(n, edges)
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    u -= 1
    v -= 1
    adj[u] << v
    adj[v] << u
  end

  ans = Array.new(n - 1, 0)

  total_masks = 1 << n
  (1...total_masks).each do |mask|
    size = mask.to_s(2).count('1')
    next if size < 2

    # find a start node in the subset
    start = nil
    (0...n).each { |i| if (mask & (1 << i)) != 0; start = i; break; end }

    # connectivity check
    visited_mask = 0
    queue = [start]
    head = 0
    visited_mask |= 1 << start
    while head < queue.length
      cur = queue[head]
      head += 1
      adj[cur].each do |nbr|
        next if (mask & (1 << nbr)).zero? || (visited_mask & (1 << nbr)) != 0
        visited_mask |= 1 << nbr
        queue << nbr
      end
    end
    next unless visited_mask == mask

    # first BFS to find farthest node
    far_node, _ = bfs_farthest(start, mask, adj, n)
    # second BFS from farthest node to get diameter
    _, diam = bfs_farthest(far_node, mask, adj, n)

    ans[diam - 1] += 1 if diam >= 1 && diam <= n - 1
  end

  ans
end

def bfs_farthest(src, mask, adj, n)
  dist = Array.new(n, -1)
  q = [src]
  head = 0
  dist[src] = 0
  far_node = src
  maxd = 0
  while head < q.length
    cur = q[head]
    head += 1
    dcur = dist[cur]
    if dcur > maxd
      maxd = dcur
      far_node = cur
    end
    adj[cur].each do |nbr|
      next if (mask & (1 << nbr)).zero? || dist[nbr] != -1
      dist[nbr] = dcur + 1
      q << nbr
    end
  end
  [far_node, maxd]
end
```

## Scala

```scala
object Solution {
    def countSubgraphsForEachDiameter(n: Int, edges: Array[Array[Int]]): Array[Int] = {
        import scala.collection.mutable.{ArrayBuffer, ArrayDeque}
        val adj = Array.fill(n)(ArrayBuffer[Int]())
        for (e <- edges) {
            val u = e(0) - 1
            val v = e(1) - 1
            adj(u).append(v)
            adj(v).append(u)
        }
        val ans = new Array[Int](n - 1)

        val totalMask = 1 << n
        var mask = 1
        while (mask < totalMask) {
            val cnt = Integer.bitCount(mask)
            if (cnt >= 2) {
                // find a start node in the subset
                var start = -1
                var i = 0
                while (i < n && start == -1) {
                    if (((mask >> i) & 1) == 1) start = i
                    i += 1
                }
                // connectivity check via BFS
                val seen = Array.fill(n)(false)
                val q = new ArrayDeque[Int]()
                q.append(start)
                seen(start) = true
                var visitedCount = 0
                while (q.nonEmpty) {
                    val cur = q.removeHead()
                    visitedCount += 1
                    for (nb <- adj(cur)) {
                        if (((mask >> nb) & 1) == 1 && !seen(nb)) {
                            seen(nb) = true
                            q.append(nb)
                        }
                    }
                }
                if (visitedCount == cnt) {
                    // double BFS to get diameter
                    def bfs(s: Int): (Int, Array[Int]) = {
                        val dist = Array.fill(n)(-1)
                        val qq = new ArrayDeque[Int]()
                        qq.append(s)
                        dist(s) = 0
                        var far = s
                        while (qq.nonEmpty) {
                            val cur = qq.removeHead()
                            for (nb <- adj(cur)) {
                                if (((mask >> nb) & 1) == 1 && dist(nb) == -1) {
                                    dist(nb) = dist(cur) + 1
                                    qq.append(nb)
                                    if (dist(nb) > dist(far)) far = nb
                                }
                            }
                        }
                        (far, dist)
                    }
                    val (u, _) = bfs(start)
                    val (_, dist2) = bfs(u)
                    var diam = 0
                    var j = 0
                    while (j < n) {
                        if (((mask >> j) & 1) == 1 && dist2(j) > diam) diam = dist2(j)
                        j += 1
                    }
                    ans(diam - 1) += 1
                }
            }
            mask += 1
        }
        ans
    }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn count_subgraphs_for_each_diameter(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut adj = vec![Vec::<usize>::new(); n];
        for e in edges.iter() {
            let u = (e[0] - 1) as usize;
            let v = (e[1] - 1) as usize;
            adj[u].push(v);
            adj[v].push(u);
        }

        // Precompute all-pairs distances using BFS from each node
        let mut dist = vec![vec![0i32; n]; n];
        for src in 0..n {
            let mut dists = vec![-1i32; n];
            let mut q = VecDeque::new();
            dists[src] = 0;
            q.push_back(src);
            while let Some(u) = q.pop_front() {
                for &v in adj[u].iter() {
                    if dists[v] == -1 {
                        dists[v] = dists[u] + 1;
                        q.push_back(v);
                    }
                }
            }
            for i in 0..n {
                dist[src][i] = dists[i];
            }
        }

        let mut ans = vec![0i32; n - 1];
        let total_masks = 1usize << n;

        for mask in 0..total_masks {
            let size = mask.count_ones();
            if size < 2 {
                continue;
            }

            // Find any node in the subset to start connectivity check
            let mut start = None;
            for i in 0..n {
                if (mask >> i) & 1 == 1 {
                    start = Some(i);
                    break;
                }
            }
            let start = start.unwrap();

            // BFS within the subset to verify connectivity
            let mut visited_mask = 0usize;
            let mut q = VecDeque::new();
            visited_mask |= 1 << start;
            q.push_back(start);
            while let Some(u) = q.pop_front() {
                for &v in adj[u].iter() {
                    if ((mask >> v) & 1) == 1 && ((visited_mask >> v) & 1) == 0 {
                        visited_mask |= 1 << v;
                        q.push_back(v);
                    }
                }
            }

            if visited_mask != mask {
                continue; // not connected
            }

            // Compute diameter of the subset using precomputed distances
            let mut max_d = 0i32;
            for i in 0..n {
                if (mask >> i) & 1 == 0 {
                    continue;
                }
                for j in (i + 1)..n {
                    if (mask >> j) & 1 == 0 {
                        continue;
                    }
                    let d = dist[i][j];
                    if d > max_d {
                        max_d = d;
                    }
                }
            }

            // max_d is at least 1
            ans[(max_d - 1) as usize] += 1;
        }

        ans
    }
}
```

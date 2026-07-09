# 3372. Maximize the Number of Target Nodes After Connecting Trees I

## Cpp

```cpp
class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2, int k) {
        int n = (int)edges1.size() + 1;
        int m = (int)edges2.size() + 1;
        vector<vector<int>> adj1(n), adj2(m);
        for (auto& e : edges1) {
            adj1[e[0]].push_back(e[1]);
            adj1[e[1]].push_back(e[0]);
        }
        for (auto& e : edges2) {
            adj2[e[0]].push_back(e[1]);
            adj2[e[1]].push_back(e[0]);
        }

        vector<int> cnt1(n, 0), cnt2(m, 0);

        // Count nodes within distance <= k in the first tree for each source
        if (k >= 0) {
            for (int s = 0; s < n; ++s) {
                vector<int> dist(n, -1);
                queue<int> q;
                dist[s] = 0;
                q.push(s);
                int c = 0;
                while (!q.empty()) {
                    int u = q.front(); q.pop();
                    if (dist[u] > k) continue;
                    ++c;
                    if (dist[u] == k) continue;
                    for (int v : adj1[u]) {
                        if (dist[v] == -1) {
                            dist[v] = dist[u] + 1;
                            q.push(v);
                        }
                    }
                }
                cnt1[s] = c;
            }
        }

        int limit2 = k - 1;
        // Count nodes within distance <= k-1 in the second tree for each source
        if (limit2 >= 0) {
            for (int s = 0; s < m; ++s) {
                vector<int> dist(m, -1);
                queue<int> q;
                dist[s] = 0;
                q.push(s);
                int c = 0;
                while (!q.empty()) {
                    int u = q.front(); q.pop();
                    if (dist[u] > limit2) continue;
                    ++c;
                    if (dist[u] == limit2) continue;
                    for (int v : adj2[u]) {
                        if (dist[v] == -1) {
                            dist[v] = dist[u] + 1;
                            q.push(v);
                        }
                    }
                }
                cnt2[s] = c;
            }
        }

        int maxCnt2 = 0;
        for (int x : cnt2) if (x > maxCnt2) maxCnt2 = x;

        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            ans[i] = cnt1[i] + maxCnt2;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] maxTargetNodes(int[][] edges1, int[][] edges2, int k) {
        int n = edges1.length + 1;
        int m = edges2.length + 1;

        List<Integer>[] g1 = new ArrayList[n];
        for (int i = 0; i < n; i++) g1[i] = new ArrayList<>();
        for (int[] e : edges1) {
            g1[e[0]].add(e[1]);
            g1[e[1]].add(e[0]);
        }

        List<Integer>[] g2 = new ArrayList[m];
        for (int i = 0; i < m; i++) g2[i] = new ArrayList<>();
        for (int[] e : edges2) {
            g2[e[0]].add(e[1]);
            g2[e[1]].add(e[0]);
        }

        int[] cnt1 = new int[n];
        for (int i = 0; i < n; i++) {
            cnt1[i] = bfsCount(g1, i, k);
        }

        int maxCnt2 = 0;
        if (k > 0) {
            for (int j = 0; j < m; j++) {
                int c = bfsCount(g2, j, k - 1);
                if (c > maxCnt2) maxCnt2 = c;
            }
        }

        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = cnt1[i] + maxCnt2;
        }
        return ans;
    }

    private int bfsCount(List<Integer>[] graph, int src, int limit) {
        if (limit < 0) return 0;
        int n = graph.length;
        boolean[] visited = new boolean[n];
        int[] dist = new int[n];
        ArrayDeque<Integer> q = new ArrayDeque<>();
        visited[src] = true;
        dist[src] = 0;
        q.add(src);
        int cnt = 0;
        while (!q.isEmpty()) {
            int u = q.poll();
            if (dist[u] > limit) continue;
            cnt++;
            if (dist[u] == limit) continue;
            for (int v : graph[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    dist[v] = dist[u] + 1;
                    q.add(v);
                }
            }
        }
        return cnt;
    }
}
```

## Python

```python
class Solution(object):
    def maxTargetNodes(self, edges1, edges2, k):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque

        def build_adj(edges, size):
            adj = [[] for _ in range(size)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def count_within(adj, start, limit):
            if limit < 0:
                return 0
            n = len(adj)
            visited = [False] * n
            q = deque()
            q.append((start, 0))
            visited[start] = True
            cnt = 0
            while q:
                node, d = q.popleft()
                if d > limit:
                    continue
                cnt += 1
                nd = d + 1
                if nd > limit:
                    continue
                for nb in adj[node]:
                    if not visited[nb]:
                        visited[nb] = True
                        q.append((nb, nd))
            return cnt

        n = max(max(e) for e in edges1) + 1 if edges1 else 0
        m = max(max(e) for e in edges2) + 1 if edges2 else 0

        adj1 = build_adj(edges1, n)
        adj2 = build_adj(edges2, m)

        # counts for first tree
        cnt1 = [count_within(adj1, i, k) for i in range(n)]

        # max count for second tree with limit k-1
        if k - 1 >= 0:
            max_cnt2 = 0
            for j in range(m):
                c = count_within(adj2, j, k - 1)
                if c > max_cnt2:
                    max_cnt2 = c
        else:
            max_cnt2 = 0

        return [cnt1[i] + max_cnt2 for i in range(n])
```

## Python3

```python
class Solution:
    def maxTargetNodes(self, edges1, edges2, k):
        from collections import deque

        def bfs_counts(adj, limit):
            n = len(adj)
            if limit < 0:
                return [0] * n
            counts = [0] * n
            for s in range(n):
                dist = [-1] * n
                q = deque([s])
                dist[s] = 0
                cnt = 1  # distance to itself is 0 <= limit (limit >=0 here)
                while q:
                    u = q.popleft()
                    d = dist[u]
                    nd = d + 1
                    if nd > limit:
                        continue
                    for v in adj[u]:
                        if dist[v] == -1:
                            dist[v] = nd
                            cnt += 1
                            q.append(v)
                counts[s] = cnt
            return counts

        n = len(edges1) + 1
        m = len(edges2) + 1

        adj1 = [[] for _ in range(n)]
        for a, b in edges1:
            adj1[a].append(b)
            adj1[b].append(a)

        adj2 = [[] for _ in range(m)]
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        count1 = bfs_counts(adj1, k)

        limit2 = k - 1
        if limit2 < 0:
            max_count2 = 0
        else:
            count2 = bfs_counts(adj2, limit2)
            max_count2 = max(count2) if count2 else 0

        return [c + max_count2 for c in count1]
```

## C

```c
#include <stdlib.h>
#include <string.h>

int* maxTargetNodes(int** edges1, int edges1Size, int* edges1ColSize,
                    int** edges2, int edges2Size, int* edges2ColSize,
                    int k, int* returnSize) {
    int n = edges1Size + 1;
    int m = edges2Size + 1;

    /* Build adjacency for tree 1 */
    int *deg1 = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edges1Size; ++i) {
        deg1[edges1[i][0]]++;
        deg1[edges1[i][1]]++;
    }
    int **adj1 = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i)
        adj1[i] = (int*)malloc(deg1[i] * sizeof(int));
    int *cur1 = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edges1Size; ++i) {
        int u = edges1[i][0], v = edges1[i][1];
        adj1[u][cur1[u]++] = v;
        adj1[v][cur1[v]++] = u;
    }

    /* Build adjacency for tree 2 */
    int *deg2 = (int*)calloc(m, sizeof(int));
    for (int i = 0; i < edges2Size; ++i) {
        deg2[edges2[i][0]]++;
        deg2[edges2[i][1]]++;
    }
    int **adj2 = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; ++i)
        adj2[i] = (int*)malloc(deg2[i] * sizeof(int));
    int *cur2 = (int*)calloc(m, sizeof(int));
    for (int i = 0; i < edges2Size; ++i) {
        int u = edges2[i][0], v = edges2[i][1];
        adj2[u][cur2[u]++] = v;
        adj2[v][cur2[v]++] = u;
    }

    /* Compute count1 for each node in tree 1 (distance <= k) */
    int *count1 = (int*)malloc(n * sizeof(int));
    int *dist = (int*)malloc((n > m ? n : m) * sizeof(int));
    int *queue = (int*)malloc((n > m ? n : m) * sizeof(int));

    for (int s = 0; s < n; ++s) {
        memset(dist, -1, n * sizeof(int));
        int front = 0, back = 0;
        dist[s] = 0;
        queue[back++] = s;
        int cnt = 0;
        while (front < back) {
            int u = queue[front++];
            if (dist[u] > k) continue;
            cnt++;
            if (dist[u] == k) continue; // no need to go deeper
            for (int i = 0; i < deg1[u]; ++i) {
                int v = adj1[u][i];
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    queue[back++] = v;
                }
            }
        }
        count1[s] = cnt;
    }

    /* Compute maxCount2 for tree 2 (distance <= k-1) */
    int limit = k - 1;
    int maxCount2 = 0;
    if (limit >= 0) {
        int *count2 = (int*)malloc(m * sizeof(int));
        for (int s = 0; s < m; ++s) {
            memset(dist, -1, m * sizeof(int));
            int front = 0, back = 0;
            dist[s] = 0;
            queue[back++] = s;
            int cnt = 0;
            while (front < back) {
                int u = queue[front++];
                if (dist[u] > limit) continue;
                cnt++;
                if (dist[u] == limit) continue;
                for (int i = 0; i < deg2[u]; ++i) {
                    int v = adj2[u][i];
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        queue[back++] = v;
                    }
                }
            }
            count2[s] = cnt;
            if (cnt > maxCount2) maxCount2 = cnt;
        }
        free(count2);
    } else {
        maxCount2 = 0;
    }

    /* Build answer */
    int *ans = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i)
        ans[i] = count1[i] + maxCount2;

    *returnSize = n;

    /* Free allocated memory */
    free(count1);
    free(dist);
    free(queue);
    for (int i = 0; i < n; ++i) free(adj1[i]);
    for (int i = 0; i < m; ++i) free(adj2[i]);
    free(adj1);
    free(adj2);
    free(deg1);
    free(deg2);
    free(cur1);
    free(cur2);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] MaxTargetNodes(int[][] edges1, int[][] edges2, int k) {
        int n = GetNodeCount(edges1);
        int m = GetNodeCount(edges2);
        var adj1 = BuildAdjacency(n, edges1);
        var adj2 = BuildAdjacency(m, edges2);

        int[] cnt1 = CountWithinLimit(adj1, n, k);
        int[] cnt2 = CountWithinLimit(adj2, m, k - 1);

        int maxSecond = 0;
        foreach (int v in cnt2) if (v > maxSecond) maxSecond = v;

        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = cnt1[i] + maxSecond;
        }
        return ans;
    }

    private int GetNodeCount(int[][] edges) {
        // nodes are labeled from 0 to max label, but we also receive n,m via constraints.
        // Since the caller knows sizes, we can infer size by scanning edges for max index.
        int max = -1;
        foreach (var e in edges) {
            if (e[0] > max) max = e[0];
            if (e[1] > max) max = e[1];
        }
        return max + 1; // assumes contiguous labeling starting at 0
    }

    private List<int>[] BuildAdjacency(int size, int[][] edges) {
        var adj = new List<int>[size];
        for (int i = 0; i < size; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            adj[u].Add(v);
            adj[v].Add(u);
        }
        return adj;
    }

    private int[] CountWithinLimit(List<int>[] adj, int size, int limit) {
        var result = new int[size];
        if (limit < 0) return result; // all zeros

        for (int start = 0; start < size; start++) {
            var dist = new int[size];
            for (int i = 0; i < size; i++) dist[i] = -1;
            var q = new Queue<int>();
            dist[start] = 0;
            q.Enqueue(start);
            while (q.Count > 0) {
                int u = q.Dequeue();
                if (dist[u] > limit) continue;
                result[start]++;
                foreach (int v in adj[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        if (dist[v] <= limit) q.Enqueue(v);
                    }
                }
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges1
 * @param {number[][]} edges2
 * @param {number} k
 * @return {number[]}
 */
var maxTargetNodes = function(edges1, edges2, k) {
    const buildAdj = (edges, size) => {
        const adj = Array.from({length: size}, () => []);
        for (const [u, v] of edges) {
            adj[u].push(v);
            adj[v].push(u);
        }
        return adj;
    };
    
    const bfsCount = (adj, start, limit) => {
        if (limit < 0) return 0;
        const n = adj.length;
        const visited = new Array(n).fill(false);
        const queue = [];
        let head = 0;
        visited[start] = true;
        queue.push([start, 0]);
        let cnt = 0;
        while (head < queue.length) {
            const [node, dist] = queue[head++];
            if (dist > limit) continue;
            cnt++;
            if (dist === limit) continue;
            for (const nb of adj[node]) {
                if (!visited[nb]) {
                    visited[nb] = true;
                    queue.push([nb, dist + 1]);
                }
            }
        }
        return cnt;
    };
    
    // Determine sizes from edges
    const n = Math.max(...edges1.flat()) + 1; // nodes are labeled 0..n-1
    const m = Math.max(...edges2.flat()) + 1;
    
    const adj1 = buildAdj(edges1, n);
    const adj2 = buildAdj(edges2, m);
    
    // cnt1 for first tree with radius k
    const cnt1 = new Array(n);
    for (let i = 0; i < n; ++i) {
        cnt1[i] = bfsCount(adj1, i, k);
    }
    
    // cnt2 for second tree with radius k-1
    let maxCnt2 = 0;
    if (k > 0) {
        const limit2 = k - 1;
        for (let j = 0; j < m; ++j) {
            const c = bfsCount(adj2, j, limit2);
            if (c > maxCnt2) maxCnt2 = c;
        }
    }
    
    const ans = new Array(n);
    for (let i = 0; i < n; ++i) {
        ans[i] = cnt1[i] + maxCnt2;
    }
    return ans;
};
```

## Typescript

```typescript
function maxTargetNodes(edges1: number[][], edges2: number[][], k: number): number[] {
    const n = edges1.length + 1;
    const m = edges2.length + 1;

    const buildAdj = (size: number, edges: number[][]): number[][] => {
        const adj: number[][] = Array.from({ length: size }, () => []);
        for (const [u, v] of edges) {
            adj[u].push(v);
            adj[v].push(u);
        }
        return adj;
    };

    const adj1 = buildAdj(n, edges1);
    const adj2 = buildAdj(m, edges2);

    const bfsCount = (start: number, limit: number, adj: number[][]): number => {
        if (limit < 0) return 0;
        const visited = new Uint8Array(adj.length);
        const dist = new Int16Array(adj.length);
        const queue: number[] = [];
        visited[start] = 1;
        queue.push(start);
        let cnt = 1; // start node distance 0
        while (queue.length) {
            const u = queue.shift()!;
            const d = dist[u];
            if (d === limit) continue;
            for (const v of adj[u]) {
                if (!visited[v]) {
                    visited[v] = 1;
                    dist[v] = d + 1;
                    cnt++;
                    queue.push(v);
                }
            }
        }
        return cnt;
    };

    const cnt1: number[] = new Array(n);
    for (let i = 0; i < n; ++i) {
        cnt1[i] = bfsCount(i, k, adj1);
    }

    const limit2 = k - 1;
    const cnt2: number[] = new Array(m);
    let maxCnt2 = 0;
    for (let j = 0; j < m; ++j) {
        const c = bfsCount(j, limit2, adj2);
        cnt2[j] = c;
        if (c > maxCnt2) maxCnt2 = c;
    }

    const answer: number[] = new Array(n);
    for (let i = 0; i < n; ++i) {
        answer[i] = cnt1[i] + maxCnt2;
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $edges1
     * @param Integer[][] $edges2
     * @param Integer $k
     * @return Integer[]
     */
    function maxTargetNodes($edges1, $edges2, $k) {
        $n = count($edges1) + 1;
        $m = count($edges2) + 1;

        // Build adjacency lists
        $adj1 = array_fill(0, $n, []);
        foreach ($edges1 as $e) {
            [$a, $b] = $e;
            $adj1[$a][] = $b;
            $adj1[$b][] = $a;
        }

        $adj2 = array_fill(0, $m, []);
        foreach ($edges2 as $e) {
            [$u, $v] = $e;
            $adj2[$u][] = $v;
            $adj2[$v][] = $u;
        }

        // Count nodes within distance <= k in first tree for each node
        $count1 = array_fill(0, $n, 0);
        if ($k >= 0) {
            for ($i = 0; $i < $n; $i++) {
                $queue = new SplQueue();
                $dist = array_fill(0, $n, -1);
                $dist[$i] = 0;
                $queue->enqueue($i);
                $cnt = 0;
                while (!$queue->isEmpty()) {
                    $u = $queue->dequeue();
                    if ($dist[$u] > $k) continue;
                    $cnt++;
                    foreach ($adj1[$u] as $v) {
                        if ($dist[$v] == -1 && $dist[$u] + 1 <= $k) {
                            $dist[$v] = $dist[$u] + 1;
                            $queue->enqueue($v);
                        }
                    }
                }
                $count1[$i] = $cnt;
            }
        }

        // Compute maximum count in second tree within distance <= k-1
        $maxCount2 = 0;
        $limit2 = $k - 1;
        if ($limit2 >= 0) {
            for ($j = 0; $j < $m; $j++) {
                $queue = new SplQueue();
                $dist = array_fill(0, $m, -1);
                $dist[$j] = 0;
                $queue->enqueue($j);
                $cnt = 0;
                while (!$queue->isEmpty()) {
                    $u = $queue->dequeue();
                    if ($dist[$u] > $limit2) continue;
                    $cnt++;
                    foreach ($adj2[$u] as $v) {
                        if ($dist[$v] == -1 && $dist[$u] + 1 <= $limit2) {
                            $dist[$v] = $dist[$u] + 1;
                            $queue->enqueue($v);
                        }
                    }
                }
                if ($cnt > $maxCount2) $maxCount2 = $cnt;
            }
        }

        // Build answer
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $ans[] = $count1[$i] + $maxCount2;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxTargetNodes(_ edges1: [[Int]], _ edges2: [[Int]], _ k: Int) -> [Int] {
        var n = 0
        for e in edges1 {
            n = max(n, e[0])
            n = max(n, e[1])
        }
        n += 1
        var m = 0
        for e in edges2 {
            m = max(m, e[0])
            m = max(m, e[1])
        }
        m += 1
        
        let adj1 = buildAdj(edges1, n)
        let adj2 = buildAdj(edges2, m)
        
        var maxCount2 = 0
        if k > 0 {
            for v in 0..<m {
                let cnt = countWithin(start: v, adj: adj2, limit: k - 1)
                if cnt > maxCount2 { maxCount2 = cnt }
            }
        }
        
        var answer = Array(repeating: 0, count: n)
        for i in 0..<n {
            let cnt1 = countWithin(start: i, adj: adj1, limit: k)
            answer[i] = cnt1 + maxCount2
        }
        return answer
    }
    
    private func buildAdj(_ edges: [[Int]], _ size: Int) -> [[Int]] {
        var adj = Array(repeating: [Int](), count: size)
        for e in edges {
            let u = e[0], v = e[1]
            adj[u].append(v)
            adj[v].append(u)
        }
        return adj
    }
    
    private func countWithin(start: Int, adj: [[Int]], limit: Int) -> Int {
        if limit < 0 { return 0 }
        var visited = Array(repeating: false, count: adj.count)
        var dist = Array(repeating: 0, count: adj.count)
        var queue = [Int]()
        var head = 0
        visited[start] = true
        queue.append(start)
        var cnt = 0
        while head < queue.count {
            let u = queue[head]
            head += 1
            if dist[u] <= limit { cnt += 1 }
            if dist[u] == limit { continue }
            for v in adj[u] where !visited[v] {
                visited[v] = true
                dist[v] = dist[u] + 1
                queue.append(v)
            }
        }
        return cnt
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxTargetNodes(edges1: Array<IntArray>, edges2: Array<IntArray>, k: Int): IntArray {
        val n = edges1.size + 1
        val m = edges2.size + 1

        val adj1 = Array(n) { mutableListOf<Int>() }
        for (e in edges1) {
            val a = e[0]
            val b = e[1]
            adj1[a].add(b)
            adj1[b].add(a)
        }

        val adj2 = Array(m) { mutableListOf<Int>() }
        for (e in edges2) {
            val u = e[0]
            val v = e[1]
            adj2[u].add(v)
            adj2[v].add(u)
        }

        fun bfsCount(adj: Array<MutableList<Int>>, start: Int, limit: Int): Int {
            if (limit < 0) return 0
            val size = adj.size
            val dist = IntArray(size) { -1 }
            val queue = IntArray(size)
            var head = 0
            var tail = 0
            dist[start] = 0
            queue[tail++] = start
            var cnt = 1
            while (head < tail) {
                val cur = queue[head++]
                val d = dist[cur]
                if (d == limit) continue
                for (nb in adj[cur]) {
                    if (dist[nb] == -1) {
                        val nd = d + 1
                        if (nd <= limit) {
                            dist[nb] = nd
                            queue[tail++] = nb
                            cnt++
                        }
                    }
                }
            }
            return cnt
        }

        val countFirst = IntArray(n)
        for (i in 0 until n) {
            countFirst[i] = bfsCount(adj1, i, k)
        }

        var maxSecond = 0
        if (k > 0) {
            for (j in 0 until m) {
                val cnt = bfsCount(adj2, j, k - 1)
                if (cnt > maxSecond) maxSecond = cnt
            }
        }

        val ans = IntArray(n)
        for (i in 0 until n) {
            ans[i] = countFirst[i] + maxSecond
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  List<int> maxTargetNodes(List<List<int>> edges1, List<List<int>> edges2, int k) {
    int n = edges1.length + 1;
    int m = edges2.length + 1;

    List<List<int>> adj1 = List.generate(n, (_) => <int>[]);
    for (var e in edges1) {
      int a = e[0], b = e[1];
      adj1[a].add(b);
      adj1[b].add(a);
    }

    List<List<int>> adj2 = List.generate(m, (_) => <int>[]);
    for (var e in edges2) {
      int u = e[0], v = e[1];
      adj2[u].add(v);
      adj2[v].add(u);
    }

    // Helper BFS to count nodes within distance <= limit from start
    int bfsCount(List<List<int>> adj, int start, int limit) {
      if (limit < 0) return 0;
      int size = adj.length;
      List<int> dist = List.filled(size, -1);
      Queue<int> q = Queue<int>();
      dist[start] = 0;
      q.add(start);
      int cnt = 0;
      while (q.isNotEmpty) {
        int node = q.removeFirst();
        int d = dist[node];
        if (d > limit) continue;
        cnt++;
        for (int nb in adj[node]) {
          if (dist[nb] == -1) {
            int nd = d + 1;
            if (nd <= limit) {
              dist[nb] = nd;
              q.add(nb);
            } else {
              // No need to store distance beyond limit
              dist[nb] = nd; // still mark visited to avoid reprocessing
            }
          }
        }
      }
      return cnt;
    }

    // Count for first tree
    List<int> count1 = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      count1[i] = bfsCount(adj1, i, k);
    }

    // Max count for second tree with limit k-1
    int maxCount2 = 0;
    int limit2 = k - 1;
    if (limit2 >= 0) {
      for (int j = 0; j < m; j++) {
        int cnt = bfsCount(adj2, j, limit2);
        if (cnt > maxCount2) maxCount2 = cnt;
      }
    }

    List<int> answer = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      answer[i] = count1[i] + maxCount2;
    }
    return answer;
  }
}
```

## Golang

```go
func maxTargetNodes(edges1 [][]int, edges2 [][]int, k int) []int {
    // Build adjacency list for first tree
    n := len(edges1) + 1
    adj1 := make([][]int, n)
    for _, e := range edges1 {
        a, b := e[0], e[1]
        adj1[a] = append(adj1[a], b)
        adj1[b] = append(adj1[b], a)
    }

    // Build adjacency list for second tree
    m := len(edges2) + 1
    adj2 := make([][]int, m)
    for _, e := range edges2 {
        a, b := e[0], e[1]
        adj2[a] = append(adj2[a], b)
        adj2[b] = append(adj2[b], a)
    }

    // Helper: count nodes within distance <= limit from start using BFS
    bfsCount := func(adj [][]int, start, limit int) int {
        if limit < 0 {
            return 0
        }
        n := len(adj)
        dist := make([]int, n)
        for i := range dist {
            dist[i] = -1
        }
        queue := make([]int, 0, n)
        dist[start] = 0
        queue = append(queue, start)

        cnt := 0
        for head := 0; head < len(queue); head++ {
            u := queue[head]
            if dist[u] > limit {
                continue
            }
            cnt++
            if dist[u] == limit {
                continue
            }
            for _, v := range adj[u] {
                if dist[v] == -1 {
                    dist[v] = dist[u] + 1
                    queue = append(queue, v)
                }
            }
        }
        return cnt
    }

    // Count within distance k in first tree for each node
    cnt1 := make([]int, n)
    for i := 0; i < n; i++ {
        cnt1[i] = bfsCount(adj1, i, k)
    }

    // Count within distance k-1 in second tree and keep the maximum
    limit2 := k - 1
    maxCnt2 := 0
    if limit2 >= 0 {
        for j := 0; j < m; j++ {
            c := bfsCount(adj2, j, limit2)
            if c > maxCnt2 {
                maxCnt2 = c
            }
        }
    }

    // Combine results
    ans := make([]int, n)
    for i := 0; i < n; i++ {
        ans[i] = cnt1[i] + maxCnt2
    }
    return ans
}
```

## Ruby

```ruby
def compute_counts(adj, limit)
  n = adj.size
  res = Array.new(n, 0)
  return res if limit < 0
  (0...n).each do |src|
    visited = Array.new(n, false)
    queue = [[src, 0]]
    visited[src] = true
    cnt = 0
    until queue.empty?
      node, d = queue.shift
      cnt += 1
      next if d == limit
      adj[node].each do |nbr|
        unless visited[nbr]
          visited[nbr] = true
          queue << [nbr, d + 1]
        end
      end
    end
    res[src] = cnt
  end
  res
end

# @param {Integer[][]} edges1
# @param {Integer[][]} edges2
# @param {Integer} k
# @return {Integer[]}
def max_target_nodes(edges1, edges2, k)
  n = edges1.length + 1
  m = edges2.length + 1

  adj1 = Array.new(n) { [] }
  edges1.each do |a, b|
    adj1[a] << b
    adj1[b] << a
  end

  adj2 = Array.new(m) { [] }
  edges2.each do |u, v|
    adj2[u] << v
    adj2[v] << u
  end

  count1 = compute_counts(adj1, k)
  count2 = compute_counts(adj2, k - 1)

  max_c2 = count2.max || 0

  Array.new(n) { |i| count1[i] + max_c2 }
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable.{ArrayBuffer, Queue}

    private def buildAdj(n: Int, edges: Array[Array[Int]]): Array[ArrayBuffer[Int]] = {
        val adj = Array.fill(n)(new ArrayBuffer[Int]())
        for (e <- edges) {
            val a = e(0)
            val b = e(1)
            adj(a).append(b)
            adj(b).append(a)
        }
        adj
    }

    private def countWithin(adj: Array[ArrayBuffer[Int]], limit: Int): Array[Int] = {
        val n = adj.length
        val res = new Array[Int](n)
        if (limit < 0) return res // all zeros
        for (src <- 0 until n) {
            val visited = new Array[Boolean](n)
            val q: Queue[(Int, Int)] = Queue()
            visited(src) = true
            q.enqueue((src, 0))
            var cnt = 0
            while (q.nonEmpty) {
                val (node, d) = q.dequeue()
                if (d <= limit) cnt += 1
                if (d < limit) {
                    for (nb <- adj(node)) {
                        if (!visited(nb)) {
                            visited(nb) = true
                            q.enqueue((nb, d + 1))
                        }
                    }
                }
            }
            res(src) = cnt
        }
        res
    }

    def maxTargetNodes(edges1: Array[Array[Int]], edges2: Array[Array[Int]], k: Int): Array[Int] = {
        val n = edges1.length + 1
        val m = edges2.length + 1
        val adj1 = buildAdj(n, edges1)
        val adj2 = buildAdj(m, edges2)

        val cnt1 = countWithin(adj1, k)
        val cnt2 = countWithin(adj2, k - 1)
        var maxCnt2 = 0
        for (v <- cnt2) if (v > maxCnt2) maxCnt2 = v

        val ans = new Array[Int](n)
        for (i <- 0 until n) {
            ans(i) = cnt1(i) + maxCnt2
        }
        ans
    }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn max_target_nodes(edges1: Vec<Vec<i32>>, edges2: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let n = edges1.len() + 1;
        let m = edges2.len() + 1;

        // Build adjacency lists
        let mut adj1: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in edges1.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj1[a].push(b);
            adj1[b].push(a);
        }

        let mut adj2: Vec<Vec<usize>> = vec![Vec::new(); m];
        for e in edges2.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj2[a].push(b);
            adj2[b].push(a);
        }

        // Count within distance k for each node in first tree
        let mut cnt1: Vec<i32> = vec![0; n];
        for i in 0..n {
            cnt1[i] = bfs_count(&adj1, i, k);
        }

        // Count within distance k-1 for second tree and take maximum
        let limit2 = if k > 0 { k - 1 } else { -1 };
        let mut max2: i32 = 0;
        if limit2 >= 0 {
            for j in 0..m {
                let c = bfs_count(&adj2, j, limit2);
                if c > max2 {
                    max2 = c;
                }
            }
        }

        // Combine results
        let mut ans: Vec<i32> = vec![0; n];
        for i in 0..n {
            ans[i] = cnt1[i] + max2;
        }
        ans
    }
}

// Helper BFS to count nodes within a distance limit from start
fn bfs_count(adj: &Vec<Vec<usize>>, start: usize, limit: i32) -> i32 {
    if limit < 0 {
        return 0;
    }
    let n = adj.len();
    let mut dist: Vec<i32> = vec![-1; n];
    let mut q: VecDeque<usize> = VecDeque::new();

    dist[start] = 0;
    q.push_back(start);
    let mut count: i32 = 0;

    while let Some(u) = q.pop_front() {
        let d = dist[u];
        if d > limit {
            continue;
        }
        count += 1;
        for &v in &adj[u] {
            if dist[v] == -1 {
                dist[v] = d + 1;
                if dist[v] <= limit {
                    q.push_back(v);
                }
            }
        }
    }

    count
}
```

## Racket

```racket
(define/contract (max-target-nodes edges1 edges2 k)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      exact-integer?
      (listof exact-integer?))
  (define (build-adj edges size)
    (let ((adj (make-vector size '())))
      (for ([e edges])
        (match-define (list a b) e)
        (vector-set! adj a (cons b (vector-ref adj a)))
        (vector-set! adj b (cons a (vector-ref adj b))))
      adj))
  (define (count-within adj start limit)
    (if (< limit 0)
        0
        (let* ((n (vector-length adj))
               (dist (make-vector n -1))
               (queue (make-vector n 0))
               (head 0) (tail 0))
          (vector-set! dist start 0)
          (vector-set! queue tail start)
          (set! tail (+ tail 1))
          (let loop ()
            (when (< head tail)
              (define u (vector-ref queue head))
              (set! head (+ head 1))
              (for ([v (vector-ref adj u)])
                (when (= (vector-ref dist v) -1)
                  (define d (+ (vector-ref dist u) 1))
                  (when (<= d limit)
                    (vector-set! dist v d)
                    (vector-set! queue tail v)
                    (set! tail (+ tail 1)))))
              (loop)))
          (for/sum ([d (in-vector dist)]) (if (>= d 0) 1 0)))))
  (define n
    (let loop ((max -1) (lst edges1))
      (cond [(null? lst) max]
            [else (let* ((e (car lst))
                         (a (list-ref e 0))
                         (b (list-ref e 1)))
                    (loop (max max a b) (cdr lst)))])))
  (define m
    (let loop ((max -1) (lst edges2))
      (cond [(null? lst) max]
            [else (let* ((e (car lst))
                         (a (list-ref e 0))
                         (b (list-ref e 1)))
                    (loop (max max a b) (cdr lst)))])))
  ;; n and m are the maximum node index + 1 because nodes are labeled from 0..n-1, etc.
  (define adj1 (build-adj edges1 n))
  (define adj2 (build-adj edges2 m))
  (define cnt1 (make-vector n 0))
  (for ([i (in-range n)])
    (vector-set! cnt1 i (count-within adj1 i k)))
  (define limit2 (- k 1))
  (define maxCnt2
    (let ((maxv 0))
      (for ([j (in-range m)])
        (define c (count-within adj2 j limit2))
        (when (> c maxv) (set! maxv c)))
      maxv))
  (for/list ([i (in-range n)])
    (+ (vector-ref cnt1 i) maxCnt2)))
```

## Erlang

```erlang
-spec max_target_nodes(Edges1 :: [[integer()]], Edges2 :: [[integer()]], K :: integer()) -> [integer()].
max_target_nodes(Edges1, Edges2, K) ->
    N = length(Edges1) + 1,
    M = length(Edges2) + 1,
    Adj1 = build_adj(Edges1, N),
    Adj2 = build_adj(Edges2, M),

    MaxCount2 =
        case K of
            0 -> 0;
            _ ->
                Limit2 = K - 1,
                CountList2 = [count_within(Node, Adj2, Limit2) || Node <- lists:seq(0, M - 1)],
                lists:max(CountList2)
        end,

    [count_within(Node, Adj1, K) + MaxCount2 || Node <- lists:seq(0, N - 1)].

%% Build adjacency map for a tree
build_adj(Edges, N) ->
    Empty = maps:from_list([{I, []} || I <- lists:seq(0, N - 1)]),
    lists:foldl(fun([A, B], Acc) ->
        Acc1 = maps:update_with(A,
                fun(L) -> [B | L] end,
                [B],
                Acc),
        maps:update_with(B,
                fun(L) -> [A | L] end,
                [A],
                Acc1)
    end, Empty, Edges).

%% Count nodes within distance Limit from Start using DFS (tree property)
count_within(Start, Adj, Limit) ->
    dfs_count(Start, -1, 0, Adj, Limit).

dfs_count(_Node, _Parent, Dist, _Adj, Limit) when Dist > Limit ->
    0;
dfs_count(Node, Parent, Dist, Adj, Limit) ->
    Neighs = maps:get(Node, Adj),
    SubSum = lists:foldl(fun(Nbr, Acc) ->
                if Nbr =/= Parent ->
                        Acc + dfs_count(Nbr, Node, Dist + 1, Adj, Limit);
                   true -> Acc
                end
            end, 0, Neighs),
    1 + SubSum.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_target_nodes(edges1 :: [[integer]], edges2 :: [[integer]], k :: integer) :: [integer]
  def max_target_nodes(edges1, edges2, k) do
    n = length(edges1) + 1
    m = length(edges2) + 1

    adj1 = build_adj(n, edges1)
    adj2 = build_adj(m, edges2)

    cnt1 = for i <- 0..(n - 1), do: bfs_count(adj1, i, k, n)
    cnt2 = for j <- 0..(m - 1), do: bfs_count(adj2, j, k - 1, m)

    max_cnt2 = if cnt2 == [], do: 0, else: Enum.max(cnt2)

    for i <- 0..(n - 1), do: Enum.at(cnt1, i) + max_cnt2
  end

  defp build_adj(size, edges) do
    Enum.reduce(edges, %{}, fn [a, b], acc ->
      acc
      |> Map.update(a, [b], &[b | &1])
      |> Map.update(b, [a], &[a | &1])
    end)
    # ensure all nodes exist in map (optional)
    |> ensure_all_nodes(size)
  end

  defp ensure_all_nodes(map, size) do
    Enum.reduce(0..(size - 1), map, fn i, acc ->
      Map.put_new(acc, i, [])
    end)
  end

  defp bfs_count(_adj, _start, limit, _n) when limit < 0, do: 0

  defp bfs_count(adj, start, limit, _n) do
    queue = :queue.in({start, 0}, :queue.new())
    visited = MapSet.new([start])
    bfs(queue, visited, adj, limit)
  end

  defp bfs(queue, visited, adj, limit) do
    case :queue.out(queue) do
      {:empty, _} ->
        MapSet.size(visited)

      {{:value, {node, dist}}, q_rest} ->
        if dist < limit do
          neighbors = Map.get(adj, node, [])
          {new_queue, new_visited} =
            Enum.reduce(neighbors, {q_rest, visited}, fn nb, {q_acc, v_acc} ->
              if MapSet.member?(v_acc, nb) do
                {q_acc, v_acc}
              else
                {
                  :queue.in({nb, dist + 1}, q_acc),
                  MapSet.put(v_acc, nb)
                }
              end
            end)

          bfs(new_queue, new_visited, adj, limit)
        else
          bfs(q_rest, visited, adj, limit)
        end
    end
  end
end
```

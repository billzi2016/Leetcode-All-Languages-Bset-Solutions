# 2646. Minimize the Total Price of the Trips

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumTotalPrice(int n, vector<vector<int>>& edges, vector<int>& price, vector<vector<int>>& trips) {
        vector<vector<int>> adj(n);
        for (auto &e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        vector<int> freq(n, 0);
        
        // helper to find path nodes between s and t
        function<bool(int,int,int,vector<int>&)> dfsPath = [&](int u, int target, int parent, vector<int>& path) -> bool {
            if (u == target) {
                path.push_back(u);
                return true;
            }
            for (int v : adj[u]) {
                if (v == parent) continue;
                if (dfsPath(v, target, u, path)) {
                    path.push_back(u);
                    return true;
                }
            }
            return false;
        };
        
        // count frequencies
        for (auto &tr : trips) {
            int s = tr[0], t = tr[1];
            vector<int> path;
            dfsPath(s, t, -1, path); // path from t to s
            for (int node : path) freq[node]++; // each node visited once per trip
        }
        
        vector<long long> dp0(n), dp1(n);
        function<void(int,int)> dfsDP = [&](int u, int parent) {
            long long costFull = 1LL * freq[u] * price[u];
            long long costHalf = 1LL * freq[u] * (price[u] / 2);
            long long sum0 = 0, sum1 = 0;
            for (int v : adj[u]) {
                if (v == parent) continue;
                dfsDP(v, u);
                sum0 += min(dp0[v], dp1[v]); // child may be selected or not
                sum1 += dp0[v];               // child cannot be selected
            }
            dp0[u] = costFull + sum0;
            dp1[u] = costHalf + sum1;
        };
        
        dfsDP(0, -1);
        long long ans = min(dp0[0], dp1[0]);
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumTotalPrice(int n, int[][] edges, int[] price, int[][] trips) {
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(e[1]);
            adj[e[1]].add(e[0]);
        }

        int[] freq = new int[n];
        for (int[] trip : trips) {
            List<Integer> path = new ArrayList<>();
            dfsPath(trip[0], trip[1], -1, adj, path);
            for (int node : path) freq[node]++;
        }

        long total = 0;
        long[] weight = new long[n];
        for (int i = 0; i < n; i++) {
            weight[i] = (long) freq[i] * price[i];
            total += weight[i];
        }

        long[][] dp = new long[n][2];
        dfsDP(0, -1, adj, weight, dp);
        long maxReductionWeight = Math.max(dp[0][0], dp[0][1]);
        long answer = total - maxReductionWeight / 2;
        return (int) answer;
    }

    private boolean dfsPath(int u, int target, int parent, List<Integer>[] adj, List<Integer> path) {
        if (u == target) {
            path.add(u);
            return true;
        }
        for (int v : adj[u]) {
            if (v == parent) continue;
            if (dfsPath(v, target, u, adj, path)) {
                path.add(u);
                return true;
            }
        }
        return false;
    }

    private void dfsDP(int u, int parent, List<Integer>[] adj, long[] weight, long[][] dp) {
        long notTake = 0;
        long take = weight[u];
        for (int v : adj[u]) {
            if (v == parent) continue;
            dfsDP(v, u, adj, weight, dp);
            notTake += Math.max(dp[v][0], dp[v][1]);
            take += dp[v][0]; // children cannot be taken when u is taken
        }
        dp[u][0] = notTake;
        dp[u][1] = take;
    }
}
```

## Python

```python
class Solution(object):
    def minimumTotalPrice(self, n, edges, price, trips):
        """
        :type n: int
        :type edges: List[List[int]]
        :type price: List[int]
        :type trips: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        # build adjacency list
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # helper to get path nodes between two vertices using DFS
        def get_path(s, t):
            path = []
            def dfs(u, target, parent):
                if u == target:
                    path.append(u)
                    return True
                for v in adj[u]:
                    if v == parent:
                        continue
                    if dfs(v, target, u):
                        path.append(u)
                        return True
                return False
            dfs(s, t, -1)
            path.reverse()
            return path

        # frequency of visits per node
        freq = [0] * n
        for s, t in trips:
            p = get_path(s, t)
            for node in p:
                freq[node] += 1

        total = sum(freq[i] * price[i] for i in range(n))
        save = [freq[i] * (price[i] // 2) for i in range(n)]

        # tree DP for maximum saving with no adjacent selected
        def dp(u, parent):
            not_sel = 0          # max saving when u is NOT selected
            sel = save[u]        # max saving when u IS selected
            for v in adj[u]:
                if v == parent:
                    continue
                child_not, child_sel = dp(v, u)
                not_sel += max(child_not, child_sel)
                sel += child_not   # children cannot be selected
            return not_sel, sel

        root = 0
        best_not, best_sel = dp(root, -1)
        max_save = max(best_not, best_sel)

        return total - max_save
```

## Python3

```python
import sys
sys.setrecursionlimit(10000)
from typing import List

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        freq = [0] * n

        # helper to find path between two nodes
        def find_path(u: int, target: int, parent: int) -> List[int]:
            if u == target:
                return [u]
            for v in adj[u]:
                if v == parent:
                    continue
                sub = find_path(v, target, u)
                if sub:
                    return [u] + sub
            return []

        for s, e in trips:
            path = find_path(s, e, -1)
            for node in path:
                freq[node] += 1

        # tree DP for maximum saving (independent set)
        def dfs(u: int, parent: int):
            save_u = freq[u] * price[u] // 2
            dp0 = 0          # u not selected
            dp1 = save_u     # u selected
            for v in adj[u]:
                if v == parent:
                    continue
                child0, child1 = dfs(v, u)
                dp0 += max(child0, child1)   # u not taken, child may be taken or not
                dp1 += child0                # u taken, child cannot be taken
            return dp0, dp1

        root = 0
        best_save = max(dfs(root, -1))
        total_original = sum(freq[i] * price[i] for i in range(n))
        return total_original - best_save
```

## C

```c
#include <stdbool.h>

static int n;
static int priceArr[55];
static long long freqArr[55];
static int deg[55];
static int adj[55][55];

static long long dp0[55]; // not selected
static long long dp1[55]; // selected

static bool dfsPath(int u, int target, int parent) {
    if (u == target) {
        freqArr[u]++;
        return true;
    }
    for (int i = 0; i < deg[u]; ++i) {
        int v = adj[u][i];
        if (v == parent) continue;
        if (dfsPath(v, target, u)) {
            freqArr[u]++;
            return true;
        }
    }
    return false;
}

static void dfsDP(int u, int parent) {
    long long save = freqArr[u] * priceArr[u] / 2; // halving saves this amount
    dp1[u] = save;
    dp0[u] = 0;
    for (int i = 0; i < deg[u]; ++i) {
        int v = adj[u][i];
        if (v == parent) continue;
        dfsDP(v, u);
        dp1[u] += dp0[v];
        dp0[u] += (dp0[v] > dp1[v]) ? dp0[v] : dp1[v];
    }
}

int minimumTotalPrice(int nParam, int** edges, int edgesSize, int* edgesColSize,
                      int* price, int priceSize,
                      int** trips, int tripsSize, int* tripsColSize) {
    n = nParam;
    for (int i = 0; i < n; ++i) {
        priceArr[i] = price[i];
        freqArr[i] = 0;
        deg[i] = 0;
    }
    // build adjacency
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        adj[a][deg[a]++] = b;
        adj[b][deg[b]++] = a;
    }
    // count frequencies on all trips
    for (int i = 0; i < tripsSize; ++i) {
        int s = trips[i][0];
        int t = trips[i][1];
        dfsPath(s, t, -1);
    }
    long long totalOriginal = 0;
    for (int i = 0; i < n; ++i) {
        totalOriginal += freqArr[i] * priceArr[i];
    }
    // tree DP to maximize saved amount with independent set constraint
    dfsDP(0, -1);
    long long maxSaved = dp0[0] > dp1[0] ? dp0[0] : dp1[0];
    long long answer = totalOriginal - maxSaved;
    return (int)answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumTotalPrice(int n, int[][] edges, int[] price, int[][] trips) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            graph[a].Add(b);
            graph[b].Add(a);
        }

        int[] parent = new int[n];
        int[] depth = new int[n];
        Array.Fill(parent, -1);
        var stack = new Stack<int>();
        stack.Push(0);
        depth[0] = 0;
        while (stack.Count > 0) {
            int u = stack.Pop();
            foreach (int v in graph[u]) {
                if (parent[v] == -1 && v != 0) {
                    parent[v] = u;
                    depth[v] = depth[u] + 1;
                    stack.Push(v);
                }
            }
        }

        long[] freq = new long[n];
        foreach (var tr in trips) {
            int u = tr[0], v = tr[1];
            while (depth[u] > depth[v]) {
                freq[u]++;
                u = parent[u];
            }
            while (depth[v] > depth[u]) {
                freq[v]++;
                v = parent[v];
            }
            while (u != v) {
                freq[u]++;
                freq[v]++;
                u = parent[u];
                v = parent[v];
            }
            freq[u]++; // LCA
        }

        long[] weight = new long[n];
        for (int i = 0; i < n; i++) {
            weight[i] = freq[i] * price[i] / 2;
        }

        bool[] visited = new bool[n];
        (long notSel, long sel) DFS(int node) {
            visited[node] = true;
            long sumNotSel = 0;
            long sumSel = weight[node];
            foreach (int nb in graph[node]) {
                if (!visited[nb]) {
                    var child = DFS(nb);
                    sumNotSel += Math.Max(child.notSel, child.sel);
                    sumSel += child.notSel;
                }
            }
            return (sumNotSel, sumSel);
        }

        var rootRes = DFS(0);
        long maxSaved = Math.Max(rootRes.notSel, rootRes.sel);

        long baseTotal = 0;
        for (int i = 0; i < n; i++) {
            baseTotal += freq[i] * price[i];
        }

        long answer = baseTotal - maxSaved;
        return (int)answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} price
 * @param {number[][]} trips
 * @return {number}
 */
var minimumTotalPrice = function(n, edges, price, trips) {
    const adj = Array.from({length: n}, () => []);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
    }

    const freq = new Array(n).fill(0);

    function addPath(s, e) {
        const parent = new Array(n).fill(-1);
        const stack = [s];
        parent[s] = s;
        while (stack.length) {
            const u = stack.pop();
            if (u === e) break;
            for (const v of adj[u]) {
                if (parent[v] === -1) {
                    parent[v] = u;
                    stack.push(v);
                }
            }
        }
        let cur = e;
        while (true) {
            freq[cur]++;
            if (cur === s) break;
            cur = parent[cur];
        }
    }

    for (const [s, e] of trips) {
        addPath(s, e);
    }

    const save = new Array(n);
    let totalCost = 0;
    for (let i = 0; i < n; ++i) {
        totalCost += price[i] * freq[i];
        save[i] = (price[i] >> 1) * freq[i]; // price[i] is even
    }

    const dp0 = new Array(n).fill(0); // not selected
    const dp1 = new Array(n).fill(0); // selected

    function dfs(u, p) {
        let sum0 = 0;
        let sum1 = save[u];
        for (const v of adj[u]) {
            if (v === p) continue;
            dfs(v, u);
            sum0 += Math.max(dp0[v], dp1[v]);
            sum1 += dp0[v];
        }
        dp0[u] = sum0;
        dp1[u] = sum1;
    }

    dfs(0, -1);
    const maxSaved = Math.max(dp0[0], dp1[0]);
    return totalCost - maxSaved;
};
```

## Typescript

```typescript
function minimumTotalPrice(n: number, edges: number[][], price: number[], trips: number[][]): number {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    // frequency of visits per node
    const freq = new Array<number>(n).fill(0);

    // helper to get path nodes between two vertices
    function getPath(start: number, end: number): number[] {
        const path: number[] = [];
        function dfs(u: number, target: number, parent: number): boolean {
            if (u === target) {
                path.push(u);
                return true;
            }
            for (const v of adj[u]) {
                if (v === parent) continue;
                if (dfs(v, target, u)) {
                    path.push(u);
                    return true;
                }
            }
            return false;
        }
        dfs(start, end, -1);
        path.reverse(); // now from start to end
        return path;
    }

    for (const [s, e] of trips) {
        const p = getPath(s, e);
        for (const node of p) freq[node]++;
    }

    // total original cost
    let total = 0;
    for (let i = 0; i < n; ++i) total += freq[i] * price[i];

    // DP on tree for maximum saving
    const visited = new Array<boolean>(n).fill(false);
    function dfsDP(u: number, parent: number): [number, number] {
        let dpNot = 0; // u not selected
        let dpSel = (freq[u] * price[u]) / 2; // saving if selected (half price)
        for (const v of adj[u]) {
            if (v === parent) continue;
            const [childNot, childSel] = dfsDP(v, u);
            dpNot += Math.max(childNot, childSel);
            dpSel += childNot; // children cannot be selected
        }
        return [dpNot, dpSel];
    }

    const [rootNot, rootSel] = dfsDP(0, -1);
    const maxSaving = Math.max(rootNot, rootSel);

    return total - maxSaving;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer[] $price
     * @param Integer[][] $trips
     * @return Integer
     */
    function minimumTotalPrice($n, $edges, $price, $trips) {
        // build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            $adj[$a][] = $b;
            $adj[$b][] = $a;
        }

        // parent and depth arrays (root at 0)
        $parent = array_fill(0, $n, -1);
        $depth  = array_fill(0, $n, 0);
        $stack = [0];
        $order = [];
        while (!empty($stack)) {
            $v = array_pop($stack);
            $order[] = $v;
            foreach ($adj[$v] as $to) {
                if ($to === $parent[$v]) continue;
                $parent[$to] = $v;
                $depth[$to]  = $depth[$v] + 1;
                $stack[] = $to;
            }
        }

        // frequency of visits
        $freq = array_fill(0, $n, 0);
        foreach ($trips as $trip) {
            $u = $trip[0];
            $v = $trip[1];
            while ($u !== $v) {
                if ($depth[$u] > $depth[$v]) {
                    $freq[$u]++;
                    $u = $parent[$u];
                } elseif ($depth[$v] > $depth[$u]) {
                    $freq[$v]++;
                    $v = $parent[$v];
                } else {
                    $freq[$u]++;
                    $freq[$v]++;
                    $u = $parent[$u];
                    $v = $parent[$v];
                }
            }
            $freq[$u]++; // LCA counted once
        }

        // total original cost and gain if halved
        $total = 0;
        $gain  = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $total += $freq[$i] * $price[$i];
            $gain[$i] = intdiv($freq[$i] * $price[$i], 2); // saved amount when halved
        }

        // DP on tree for maximum saved amount with independent set constraint
        $dp0 = array_fill(0, $n, 0); // not selected
        $dp1 = array_fill(0, $n, 0); // selected

        $this->dfsDP(0, -1, $adj, $gain, $dp0, $dp1);

        $maxSaved = max($dp0[0], $dp1[0]);
        return $total - $maxSaved;
    }

    private function dfsDP($v, $p, &$adj, &$gain, &$dp0, &$dp1) {
        $dp1[$v] = $gain[$v];
        $dp0[$v] = 0;
        foreach ($adj[$v] as $to) {
            if ($to === $p) continue;
            $this->dfsDP($to, $v, $adj, $gain, $dp0, $dp1);
            $dp1[$v] += $dp0[$to];
            $dp0[$v] += max($dp0[$to], $dp1[$to]);
        }
    }
}
```

## Swift

```swift
class Solution {
    func minimumTotalPrice(_ n: Int, _ edges: [[Int]], _ price: [Int], _ trips: [[Int]]) -> Int {
        var adj = [[Int]](repeating: [], count: n)
        for e in edges {
            let a = e[0], b = e[1]
            adj[a].append(b)
            adj[b].append(a)
        }
        
        var freq = [Int](repeating: 0, count: n)
        
        func dfsFind(_ cur: Int, _ target: Int, _ parent: Int, _ path: inout [Int]) -> Bool {
            if cur == target {
                path.append(cur)
                return true
            }
            for nb in adj[cur] where nb != parent {
                if dfsFind(nb, target, cur, &path) {
                    path.append(cur)
                    return true
                }
            }
            return false
        }
        
        for trip in trips {
            let start = trip[0], end = trip[1]
            var path = [Int]()
            _ = dfsFind(start, end, -1, &path)
            // path is from end to start; count all nodes
            for node in path {
                freq[node] += 1
            }
        }
        
        func dp(_ v: Int, _ parent: Int) -> (Int, Int) {
            var notHalved = freq[v] * price[v]
            var halved = freq[v] * (price[v] / 2)
            for nb in adj[v] where nb != parent {
                let child = dp(nb, v)
                notHalved += min(child.0, child.1)
                halved += child.0   // child cannot be halved if v is halved
            }
            return (notHalved, halved)
        }
        
        let result = dp(0, -1)
        return min(result.0, result.1)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumTotalPrice(n: Int, edges: Array<IntArray>, price: IntArray, trips: Array<IntArray>): Int {
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val a = e[0]
            val b = e[1]
            adj[a].add(b)
            adj[b].add(a)
        }

        val freq = IntArray(n)

        fun findPath(u: Int, parent: Int, target: Int, path: MutableList<Int>): Boolean {
            if (u == target) {
                path.add(u)
                return true
            }
            for (v in adj[u]) {
                if (v == parent) continue
                if (findPath(v, u, target, path)) {
                    path.add(u)
                    return true
                }
            }
            return false
        }

        for (trip in trips) {
            val start = trip[0]
            val end = trip[1]
            val path = mutableListOf<Int>()
            findPath(start, -1, end, path)
            for (node in path) {
                freq[node]++
            }
        }

        var totalOriginal = 0L
        for (i in 0 until n) {
            totalOriginal += freq[i].toLong() * price[i]
        }

        fun dp(u: Int, parent: Int): Pair<Long, Long> {
            var notSel = 0L
            var sel = freq[u].toLong() * price[u] / 2
            for (v in adj[u]) {
                if (v == parent) continue
                val child = dp(v, u)
                notSel += maxOf(child.first, child.second)
                sel += child.first
            }
            return Pair(notSel, sel)
        }

        val rootRes = dp(0, -1)
        val maxSaving = maxOf(rootRes.first, rootRes.second)

        return (totalOriginal - maxSaving).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minimumTotalPrice(int n, List<List<int>> edges, List<int> price,
      List<List<int>> trips) {
    // Build adjacency list
    List<List<int>> graph = List.generate(n, (_) => []);
    for (var e in edges) {
      int a = e[0], b = e[1];
      graph[a].add(b);
      graph[b].add(a);
    }

    // Frequency of visits per node
    List<int> freq = List.filled(n, 0);

    bool dfsPath(int u, int target, int parent, List<int> path) {
      if (u == target) {
        path.add(u);
        return true;
      }
      for (int v in graph[u]) {
        if (v == parent) continue;
        if (dfsPath(v, target, u, path)) {
          path.add(u);
          return true;
        }
      }
      return false;
    }

    for (var tr in trips) {
      int start = tr[0], end = tr[1];
      List<int> path = [];
      dfsPath(start, end, -1, path);
      // path is from end to start; count each node
      for (int node in path) {
        freq[node] += 1;
      }
    }

    // Compute weight saved if node is halved: price[i]/2 * freq[i]
    List<int> save = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      save[i] = (price[i] ~/ 2) * freq[i];
    }

    // Tree DP for maximum weighted independent set
    List<int> dp0 = List.filled(n, 0); // not selected
    List<int> dp1 = List.filled(n, 0); // selected

    void dfsDP(int u, int parent) {
      int sumNotSel = 0;
      int sumSel = save[u];
      for (int v in graph[u]) {
        if (v == parent) continue;
        dfsDP(v, u);
        sumNotSel += dp0[v] > dp1[v] ? dp0[v] : dp1[v];
        sumSel += dp0[v];
      }
      dp0[u] = sumNotSel;
      dp1[u] = sumSel;
    }

    dfsDP(0, -1);
    int maxSaved = dp0[0] > dp1[0] ? dp0[0] : dp1[0];

    // Total original cost
    int total = 0;
    for (int i = 0; i < n; ++i) {
      total += price[i] * freq[i];
    }

    return total - maxSaved;
  }
}
```

## Golang

```go
func minimumTotalPrice(n int, edges [][]int, price []int, trips [][]int) int {
    // Build adjacency list
    g := make([][]int, n)
    for _, e := range edges {
        a, b := e[0], e[1]
        g[a] = append(g[a], b)
        g[b] = append(g[b], a)
    }

    const LOG = 6 // since 2^6 = 64 > 50
    parent := make([]int, n)
    depth := make([]int, n)
    up := make([][]int, LOG)
    for i := 0; i < LOG; i++ {
        up[i] = make([]int, n)
    }

    // DFS to set parent and depth
    var stack []int
    stack = append(stack, 0)
    parent[0] = -1
    depth[0] = 0
    order := []int{0}
    for len(stack) > 0 {
        v := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        for _, to := range g[v] {
            if to == parent[v] {
                continue
            }
            parent[to] = v
            depth[to] = depth[v] + 1
            stack = append(stack, to)
            order = append(order, to)
        }
    }

    // binary lifting table
    for i := 0; i < n; i++ {
        if parent[i] == -1 {
            up[0][i] = -1
        } else {
            up[0][i] = parent[i]
        }
    }
    for k := 1; k < LOG; k++ {
        for i := 0; i < n; i++ {
            prev := up[k-1][i]
            if prev == -1 {
                up[k][i] = -1
            } else {
                up[k][i] = up[k-1][prev]
            }
        }
    }

    // LCA function
    lca := func(u, v int) int {
        if depth[u] < depth[v] {
            u, v = v, u
        }
        diff := depth[u] - depth[v]
        bit := 0
        for diff > 0 {
            if diff&1 == 1 {
                u = up[bit][u]
            }
            diff >>= 1
            bit++
        }
        if u == v {
            return u
        }
        for k := LOG - 1; k >= 0; k-- {
            if up[k][u] != -1 && up[k][u] != up[k][v] {
                u = up[k][u]
                v = up[k][v]
            }
        }
        return parent[u]
    }

    // Compute frequency of each node in all trips
    freq := make([]int, n)
    for _, tr := range trips {
        s, e := tr[0], tr[1]
        l := lca(s, e)

        cur := s
        for cur != l {
            freq[cur]++
            cur = parent[cur]
        }
        cur = e
        for cur != l {
            freq[cur]++
            cur = parent[cur]
        }
        freq[l]++ // LCA counted once
    }

    // Tree DP: dp0 - not halved, dp1 - halved
    var dfs func(v, p int) (int64, int64)
    dfs = func(v, p int) (int64, int64) {
        var sum0, sum1 int64
        for _, to := range g[v] {
            if to == p {
                continue
            }
            child0, child1 := dfs(to, v)
            // when v not halved, child can be either state
            if child0 < child1 {
                sum0 += child0
            } else {
                sum0 += child1
            }
            // when v halved, child cannot be halved
            sum1 += child0
        }
        dp0 := int64(freq[v])*int64(price[v]) + sum0
        dp1 := int64(freq[v])*int64(price[v]/2) + sum1
        return dp0, dp1
    }

    root0, root1 := dfs(0, -1)
    ans := root0
    if root1 < ans {
        ans = root1
    }
    return int(ans)
}
```

## Ruby

```ruby
def get_path(start_node, end_node, adj)
  n = adj.size
  parent = Array.new(n, -1)
  queue = [start_node]
  parent[start_node] = start_node
  until queue.empty?
    u = queue.shift
    break if u == end_node
    adj[u].each do |v|
      next if parent[v] != -1
      parent[v] = u
      queue << v
    end
  end
  path = []
  cur = end_node
  loop do
    path << cur
    break if cur == start_node
    cur = parent[cur]
  end
  path.reverse
end

def minimum_total_price(n, edges, price, trips)
  adj = Array.new(n) { [] }
  edges.each do |a, b|
    adj[a] << b
    adj[b] << a
  end

  freq = Array.new(n, 0)

  trips.each do |s, e|
    path = get_path(s, e, adj)
    path.each { |node| freq[node] += 1 }
  end

  total = 0
  n.times { |i| total += price[i] * freq[i] }

  w = Array.new(n) { |i| price[i] * freq[i] / 2 }

  dp0 = Array.new(n, 0)
  dp1 = Array.new(n, 0)

  dfs = nil
  dfs = ->(u, p) {
    dp1[u] = w[u]
    dp0[u] = 0
    adj[u].each do |v|
      next if v == p
      dfs.call(v, u)
      dp1[u] += dp0[v]
      dp0[u] += [dp0[v], dp1[v]].max
    end
  }
  dfs.call(0, -1)

  max_benefit = [dp0[0], dp1[0]].max
  total - max_benefit
end
```

## Scala

```scala
import scala.collection.mutable.ArrayBuffer

object Solution {
  def minimumTotalPrice(n: Int, edges: Array[Array[Int]], price: Array[Int], trips: Array[Array[Int]]): Int = {
    // build adjacency list
    val adj = Array.fill(n)(ArrayBuffer[Int]())
    for (e <- edges) {
      val a = e(0)
      val b = e(1)
      adj(a).append(b)
      adj(b).append(a)
    }

    // frequency of visits per node
    val freq = new Array[Long](n)

    // helper to find path nodes between two vertices
    def dfsPath(u: Int, target: Int, parent: Int): List[Int] = {
      if (u == target) return List(u)
      for (v <- adj(u) if v != parent) {
        val res = dfsPath(v, target, u)
        if (res.nonEmpty) return u :: res
      }
      Nil
    }

    // accumulate frequencies from all trips
    for (trip <- trips) {
      val start = trip(0)
      val end   = trip(1)
      val path = dfsPath(start, end, -1)
      for (node <- path) {
        freq(node) += 1L
      }
    }

    // total original cost and weight (saving) per node if halved
    var totalCost: Long = 0L
    val weight = new Array[Long](n)
    for (i <- 0 until n) {
      totalCost += freq(i) * price(i).toLong
      weight(i) = freq(i) * (price(i) / 2).toLong // saving when halved
    }

    // DP on tree to find maximum total saving with no adjacent selected
    def dp(u: Int, parent: Int): (Long, Long) = {
      var notTake: Long = 0L
      var take: Long = weight(u)
      for (v <- adj(u) if v != parent) {
        val (childNot, childTake) = dp(v, u)
        notTake += math.max(childNot, childTake)
        take += childNot // children cannot be taken when u is taken
      }
      (notTake, take)
    }

    val (rootNot, rootTake) = dp(0, -1)
    val maxSaving = math.max(rootNot, rootTake)

    (totalCost - maxSaving).toInt
  }
}
```

## Rust

```rust
use std::cmp::min;

impl Solution {
    pub fn minimum_total_price(n: i32, edges: Vec<Vec<i32>>, price: Vec<i32>, trips: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        const LOG: usize = 7; // since n <= 50

        // build adjacency list
        let mut adj = vec![Vec::<usize>::new(); n];
        for e in edges.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }

        // parent up table and depth
        let mut up = vec![vec![0usize; LOG]; n];
        let mut depth = vec![0usize; n];

        fn dfs(u: usize, p: usize, adj: &Vec<Vec<usize>>, up: &mut Vec<Vec<usize>>, depth: &mut Vec<usize>) {
            up[u][0] = p;
            for k in 1..up[0].len() {
                let mid = up[u][k - 1];
                up[u][k] = up[mid][k - 1];
            }
            for &v in adj[u].iter() {
                if v == p { continue; }
                depth[v] = depth[u] + 1;
                dfs(v, u, adj, up, depth);
            }
        }

        // root at 0, its parent is itself
        dfs(0, 0, &adj, &mut up, &mut depth);

        fn lca(mut a: usize, mut b: usize, depth: &Vec<usize>, up: &Vec<Vec<usize>>) -> usize {
            if depth[a] < depth[b] {
                std::mem::swap(&mut a, &mut b);
            }
            let diff = depth[a] - depth[b];
            for k in 0..LOG {
                if (diff >> k) & 1 == 1 {
                    a = up[a][k];
                }
            }
            if a == b { return a; }
            for k in (0..LOG).rev() {
                if up[a][k] != up[b][k] {
                    a = up[a][k];
                    b = up[b][k];
                }
            }
            up[a][0]
        }

        // frequency of visits
        let mut freq = vec![0i64; n];
        for tr in trips.iter() {
            let s = tr[0] as usize;
            let e = tr[1] as usize;
            let anc = lca(s, e, &depth, &up);
            // walk from s to anc
            let mut cur = s;
            while cur != anc {
                freq[cur] += 1;
                cur = up[cur][0];
            }
            // walk from e to anc
            let mut cur = e;
            while cur != anc {
                freq[cur] += 1;
                cur = up[cur][0];
            }
            // anc itself
            freq[anc] += 1;
        }

        // DP on tree for independent set (no adjacent selected)
        fn dp(u: usize, p: usize,
              adj: &Vec<Vec<usize>>,
              freq: &Vec<i64>,
              price: &Vec<i32>) -> (i64, i64) {
            let mut not_sel = freq[u] * price[u] as i64;
            let mut sel = freq[u] * (price[u] / 2) as i64; // halved price
            for &v in adj[u].iter() {
                if v == p { continue; }
                let (child_not, child_sel) = dp(v, u, adj, freq, price);
                not_sel += min(child_not, child_sel);
                sel += child_not;
            }
            (not_sel, sel)
        }

        let (root_not, root_sel) = dp(0, usize::MAX, &adj, &freq, &price);
        let ans = min(root_not, root_sel) as i32;
        ans
    }
}
```

## Racket

```racket
(define/contract (minimum-total-price n edges price trips)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof exact-integer?)
      (listof (listof exact-integer?))
      exact-integer?)
  (let* ((adj (make-vector n '()))
         (priceV (list->vector price))
         (freq (make-vector n 0)))
    ;; build adjacency list
    (for-each (lambda (e)
                (let ((a (list-ref e 0))
                      (b (list-ref e 1)))
                  (vector-set! adj a (cons b (vector-ref adj a)))
                  (vector-set! adj b (cons a (vector-ref adj b)))))
              edges)
    ;; find path between two nodes
    (define (dfs-find cur target parent)
      (if (= cur target)
          (list cur)
          (let loop ((neighbors (vector-ref adj cur)))
            (cond
              [(null? neighbors) #f]
              [else
               (let* ((next (car neighbors))
                      (rest (cdr neighbors)))
                 (if (= next parent)
                     (loop rest)
                     (let ((sub (dfs-find next target cur)))
                       (if sub
                           (cons cur sub)
                           (loop rest)))))]))))
    ;; count frequencies on all trips
    (for-each (lambda (tr)
                (let ((s (list-ref tr 0))
                      (t (list-ref tr 1)))
                  (let ((path (dfs-find s t -1)))
                    (for-each (lambda (node)
                                (vector-set! freq node (+ (vector-ref freq node) 1)))
                              path))))
              trips)
    ;; total price without any halving
    (define total
      (let loop ((i 0) (sum 0))
        (if (= i n) sum
            (loop (+ i 1)
                  (+ sum (* (vector-ref priceV i) (vector-ref freq i)))))))
    ;; DP for maximum saved amount respecting non‑adjacent constraint
    (define (dp v parent)
      (let ((save (* (/ (vector-ref priceV v) 2) (vector-ref freq v))))
        (let loop ((neighbors (vector-ref adj v)) (notSum 0) (selSum 0))
          (if (null? neighbors)
              (values notSum (+ selSum save))
              (let* ((child (car neighbors))
                     (rest (cdr neighbors)))
                (if (= child parent)
                    (loop rest notSum selSum)
                    (call-with-values
                      (lambda () (dp child v))
                      (lambda (cNot cSel)
                        (loop rest (+ notSum (max cNot cSel)) (+ selSum cNot))))))))))

    (call-with-values (lambda () (dp 0 -1))
      (lambda (rootNot rootSel)
        (- total (max rootNot rootSel))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_total_price/4]).

-spec minimum_total_price(N :: integer(), Edges :: [[integer()]], Price :: [integer()], Trips :: [[integer()]]) -> integer().
minimum_total_price(N, Edges, Price, Trips) ->
    Adj0 = maps:new(),
    Adj = lists:foldl(fun([A,B], M) ->
        M1 = maps:update_with(A,
                fun(L) -> [B|L] end,
                [B],
                M),
        maps:update_with(B,
                fun(L) -> [A|L] end,
                [A],
                M1)
    end, Adj0, Edges),

    Freq0 = lists:duplicate(N, 0),

    Freq = lists:foldl(fun([S,E], F) ->
        Path = find_path(S, E, Adj),
        update_freq(F, Path)
    end, Freq0, Trips),

    PriceT = list_to_tuple(Price),
    FreqT = list_to_tuple(Freq),

    TotalOrig = total_original(N, FreqT, PriceT),

    {DP0Root, DP1Root} = dp(0, -1, Adj, FreqT, PriceT),

    MaxSave = erlang:max(DP0Root, DP1Root),
    TotalOrig - MaxSave.

%% Find path between two nodes using DFS
find_path(Start, End, Adj) ->
    {true, Path} = dfs_path(Start, End, -1, Adj),
    Path.

dfs_path(Cur, Target, Parent, Adj) when Cur == Target ->
    {true, [Cur]};
dfs_path(Cur, Target, Parent, Adj) ->
    Neighs = maps:get(Cur, Adj),
    dfs_neighbors(Neighs, Target, Cur, Parent, Adj).

dfs_neighbors([], _Target, _Cur, _Parent, _Adj) ->
    {false, []};
dfs_neighbors([N|Rest], Target, Cur, Parent, Adj) ->
    if N == Parent ->
            dfs_neighbors(Rest, Target, Cur, Parent, Adj);
       true ->
            case dfs_path(N, Target, Cur, Adj) of
                {true, Path} -> {true, [Cur | Path]};
                {false, _} -> dfs_neighbors(Rest, Target, Cur, Parent, Adj)
            end
    end.

%% Update frequency list for nodes in path
update_freq(Freq, []) ->
    Freq;
update_freq(Freq, [Node|Rest]) ->
    Updated = list_update(Freq, Node, fun(V) -> V + 1 end),
    update_freq(Updated, Rest).

list_update(List, Index, Fun) ->
    {Prefix, [Old|Suffix]} = lists:split(Index, List),
    NewVal = Fun(Old),
    Prefix ++ [NewVal] ++ Suffix.

%% Compute total original cost
total_original(N, FreqT, PriceT) ->
    lists:foldl(fun(I, Acc) ->
        Acc + (element(I+1, FreqT) * element(I+1, PriceT))
    end, 0, lists:seq(0, N-1)).

%% DP on tree for maximum saving
dp(Node, Parent, Adj, FreqT, PriceT) ->
    Children = [C || C <- maps:get(Node, Adj), C =/= Parent],
    {DP0Children, DP1Children} =
        lists:foldl(fun(C, {Acc0, Acc1}) ->
            {C0, C1} = dp(C, Node, Adj, FreqT, PriceT),
            {Acc0 + erlang:max(C0, C1), Acc1 + C0}
        end, {0, 0}, Children),

    Save = (element(Node+1, FreqT) * element(Node+1, PriceT)) div 2,
    DP0 = DP0Children,
    DP1 = Save + DP1Children,
    {DP0, DP1}.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_total_price(n :: integer, edges :: [[integer]], price :: [integer], trips :: [[integer]]) :: integer
  def minimum_total_price(n, edges, price, trips) do
    # Build adjacency list
    adj =
      Enum.reduce(0..(n - 1), %{}, fn i, acc -> Map.put(acc, i, []) end)
      |> Enum.reduce(edges, fn [a, b], acc ->
        acc
        |> update_in([a], &[b | &1])
        |> update_in([b], &[a | &1])
      end)

    # Compute frequency of each node across all trips
    freq_map = Enum.reduce(trips, %{}, fn [s, e], fmap ->
      {:ok, path} = find_path(s, e, -1, adj)
      Enum.reduce(path, fmap, fn v, m -> Map.update(m, v, 1, &(&1 + 1)) end)
    end)

    # Total cost without any halving
    total_full =
      Enum.reduce(0..(n - 1), 0, fn i, acc ->
        f = Map.get(freq_map, i, 0)
        acc + f * Enum.at(price, i)
      end)

    # Save amount if a node is selected (half price reduction)
    save_list =
      for i <- 0..(n - 1) do
        f = Map.get(freq_map, i, 0)
        div(f * Enum.at(price, i), 2)
      end

    {dp0_root, dp1_root} = tree_dp(0, -1, adj, save_list)
    max_save = max(dp0_root, dp1_root)

    total_full - max_save
  end

  # DFS to find path between two nodes in a tree; returns {:ok, path}
  defp find_path(cur, target, prev, adj) do
    if cur == target do
      {:ok, [cur]}
    else
      Enum.reduce_while(adj[cur], :error, fn nb, _acc ->
        if nb != prev do
          case find_path(nb, target, cur, adj) do
            {:ok, path} -> {:halt, {:ok, [cur | path]}}
            :error -> {:cont, :error}
          end
        else
          {:cont, :error}
        end
      end)
    end
  end

  # Tree DP for maximum saved amount with independent set constraint
  defp tree_dp(v, parent, adj, save) do
    {sum0, sum1} =
      Enum.reduce(adj[v], {0, 0}, fn nb, {acc0, acc1} ->
        if nb == parent do
          {acc0, acc1}
        else
          {c0, c1} = tree_dp(nb, v, adj, save)
          {
            acc0 + max(c0, c1),
            acc1 + c0
          }
        end
      end)

    dp1 = Enum.at(save, v) + sum1
    dp0 = sum0
    {dp0, dp1}
  end
end
```

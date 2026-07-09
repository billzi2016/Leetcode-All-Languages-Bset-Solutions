# 3593. Minimum Increments to Equalize Leaf Paths

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minIncrease(int n, vector<vector<int>>& edges, vector<int>& cost) {
        vector<vector<int>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vector<int> parent(n, -2);
        vector<long long> pathSum(n, 0);
        vector<int> order;
        order.reserve(n);
        // DFS stack
        stack<int> st;
        st.push(0);
        parent[0] = -1;
        pathSum[0] = cost[0];
        while (!st.empty()) {
            int u = st.top(); st.pop();
            order.push_back(u);
            for (int v : adj[u]) {
                if (v == parent[u]) continue;
                parent[v] = u;
                pathSum[v] = pathSum[u] + cost[v];
                st.push(v);
            }
        }
        // find max leaf sum
        long long maxLeaf = LLONG_MIN;
        for (int i = 0; i < n; ++i) {
            bool isLeaf = (adj[i].size() == 1 && i != 0) || (n == 1);
            if (isLeaf) {
                maxLeaf = max(maxLeaf, pathSum[i]);
            }
        }
        // DP need values
        vector<long long> need(n, 0);
        for (int idx = n - 1; idx >= 0; --idx) {
            int u = order[idx];
            bool isLeaf = (adj[u].size() == 1 && u != 0) || (n == 1);
            if (isLeaf) {
                need[u] = maxLeaf - pathSum[u];
            } else {
                long long mx = 0;
                for (int v : adj[u]) {
                    if (v == parent[u]) continue;
                    mx = max(mx, need[v]);
                }
                need[u] = mx;
            }
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            long long parentNeed = (parent[i] == -1 ? 0 : need[parent[i]]);
            if (need[i] > parentNeed) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minIncrease(int n, int[][] edges, int[] cost) {
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            adj[e[0]].add(e[1]);
            adj[e[1]].add(e[0]);
        }

        int[] parent = new int[n];
        Arrays.fill(parent, -2);
        long[] pref = new long[n];
        List<Integer> order = new ArrayList<>(n);

        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        parent[0] = -1;
        pref[0] = cost[0];

        while (!stack.isEmpty()) {
            int node = stack.pop();
            order.add(node);
            for (int nb : adj[node]) {
                if (parent[nb] == -2) {
                    parent[nb] = node;
                    pref[nb] = pref[node] + cost[nb];
                    stack.push(nb);
                }
            }
        }

        long[] maxLeaf = new long[n];
        for (int i = order.size() - 1; i >= 0; --i) {
            int node = order.get(i);
            boolean isLeaf = true;
            long best = Long.MIN_VALUE;
            for (int nb : adj[node]) {
                if (nb == parent[node]) continue;
                isLeaf = false;
                if (maxLeaf[nb] > best) best = maxLeaf[nb];
            }
            if (isLeaf) {
                maxLeaf[node] = pref[node];
            } else {
                maxLeaf[node] = best;
            }
        }

        long M = maxLeaf[0];
        long[] need = new long[n];
        for (int i = 0; i < n; ++i) {
            need[i] = M - maxLeaf[i];
        }

        int ans = 0;
        for (int i = 1; i < n; ++i) {
            if (need[i] != need[parent[i]]) ans++;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minIncrease(self, n, edges, cost):
        """
        :type n: int
        :type edges: List[List[int]]
        :type cost: List[int]
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(1 << 25)

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        children = [[] for _ in range(n)]
        path_sum = [0] * n

        def build(u, p):
            cur = cost[u]
            if p != -1:
                cur += path_sum[p]
            path_sum[u] = cur
            for v in adj[u]:
                if v == p:
                    continue
                children[u].append(v)
                build(v, u)

        build(0, -1)

        leaves = [i for i in range(n) if not children[i]]
        max_leaf_sum = max(path_sum[l] for l in leaves)

        ans = 0

        def dfs(u):
            nonlocal ans
            if not children[u]:
                d = max_leaf_sum - path_sum[u]
                return {} if d == 0 else {d: 1}
            # small-to-large merging of child counters
            big = {}
            for v in children[u]:
                cnt = dfs(v)
                if len(cnt) > len(big):
                    big, cnt = cnt, big
                for k, val in cnt.items():
                    big[k] = big.get(k, 0) + val
            if not big:
                return {}
            min_key = min(big)
            if min_key > 0:
                ans += 1
                new_cnt = {}
                for k, v in big.items():
                    nk = k - min_key
                    if nk > 0:
                        new_cnt[nk] = new_cnt.get(nk, 0) + v
                return new_cnt
            return big

        dfs(0)
        return ans
```

## Python3

```python
import sys
from typing import List

sys.setrecursionlimit(300000)

class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # first dfs: compute path sums and collect leaf sums
        path_sum = [0] * n
        leaf_sums = []

        def dfs_path(u: int, p: int):
            path_sum[u] = cost[u] + (path_sum[p] if p != -1 else 0)
            is_leaf = True
            for v in adj[u]:
                if v == p:
                    continue
                is_leaf = False
                dfs_path(v, u)
            if is_leaf:
                leaf_sums.append(path_sum[u])

        dfs_path(0, -1)

        max_sum = max(leaf_sums)

        # second dfs: compute minimal deficit in each subtree
        INF = 10**20
        min_deficit = [INF] * n

        def dfs_min(u: int, p: int) -> int:
            is_leaf = True
            cur_min = INF
            for v in adj[u]:
                if v == p:
                    continue
                is_leaf = False
                child_min = dfs_min(v, u)
                if child_min < cur_min:
                    cur_min = child_min
            if is_leaf:
                cur_min = max_sum - path_sum[u]
            min_deficit[u] = cur_min
            return cur_min

        dfs_min(0, -1)

        # third dfs: count nodes where we need to add positive amount
        ans = 0

        def dfs_count(u: int, p: int, inc_from_ancestors: int):
            nonlocal ans
            needed = min_deficit[u] - inc_from_ancestors
            if needed > 0:
                ans += 1
                inc_from_ancestors += needed
            for v in adj[u]:
                if v == p:
                    continue
                dfs_count(v, u, inc_from_ancestors)

        dfs_count(0, -1, 0)
        return ans
```

## C

```c
#include <stdlib.h>

int minIncrease(int n, int** edges, int edgesSize, int* edgesColSize, int* cost, int costSize) {
    if (n <= 1) return 0;
    
    // degree count
    int *deg = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        deg[u]++; deg[v]++;
    }
    
    // adjacency list allocation
    int **adj = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        adj[i] = (int*)malloc(deg[i] * sizeof(int));
    }
    int *ptr = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u][ptr[u]++] = v;
        adj[v][ptr[v]++] = u;
    }
    free(ptr);
    
    // arrays for parent, order, prefix sum
    int *parent = (int*)malloc(n * sizeof(int));
    long long *pref = (long long*)malloc(n * sizeof(long long));
    int *order = (int*)malloc(n * sizeof(int));
    
    // iterative DFS to set parent and prefix sums
    int *stack = (int*)malloc(n * sizeof(int));
    int top = 0, ordIdx = 0;
    stack[top++] = 0;
    parent[0] = -1;
    pref[0] = cost[0];
    
    while (top) {
        int u = stack[--top];
        order[ordIdx++] = u;
        for (int i = 0; i < deg[u]; ++i) {
            int v = adj[u][i];
            if (v == parent[u]) continue;
            parent[v] = u;
            pref[v] = pref[u] + cost[v];
            stack[top++] = v;
        }
    }
    
    // find leaves and max leaf path sum
    long long maxLeafSum = -1LL;
    char *isLeaf = (char*)calloc(n, sizeof(char));
    for (int i = 0; i < n; ++i) {
        if ((deg[i] == 1 && i != 0) || (n == 1)) {
            isLeaf[i] = 1;
            if (pref[i] > maxLeafSum) maxLeafSum = pref[i];
        }
    }
    
    // deficit for each leaf, and subtree max deficit
    long long *subMax = (long long*)calloc(n, sizeof(long long));
    for (int i = n - 1; i >= 0; --i) {
        int u = order[i];
        if (isLeaf[u]) {
            subMax[u] = maxLeafSum - pref[u]; // deficit (>=0)
        }
        for (int j = 0; j < deg[u]; ++j) {
            int v = adj[u][j];
            if (v == parent[u]) continue;
            if (subMax[v] > subMax[u]) subMax[u] = subMax[v];
        }
    }
    
    // count nodes where increase is needed
    int ans = 0;
    if (subMax[0] > 0) ans++; // root needs increase
    for (int i = 1; i < n; ++i) {
        if (subMax[i] > subMax[parent[i]]) ans++;
    }
    
    // free allocated memory
    for (int i = 0; i < n; ++i) free(adj[i]);
    free(adj);
    free(deg);
    free(parent);
    free(pref);
    free(order);
    free(stack);
    free(isLeaf);
    free(subMax);
    
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinIncrease(int n, int[][] edges, int[] cost) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            graph[u].Add(v);
            graph[v].Add(u);
        }

        int[] parent = new int[n];
        Array.Fill(parent, -1);
        var order = new List<int>(n);
        var stack = new Stack<int>();
        stack.Push(0);
        parent[0] = 0;
        while (stack.Count > 0) {
            int u = stack.Pop();
            order.Add(u);
            foreach (int v in graph[u]) {
                if (v == parent[u]) continue;
                parent[v] = u;
                stack.Push(v);
            }
        }

        long[] sumPath = new long[n];
        sumPath[0] = cost[0];
        for (int i = 1; i < order.Count; i++) {
            int u = order[i];
            sumPath[u] = sumPath[parent[u]] + cost[u];
        }

        bool[] isLeaf = new bool[n];
        long maxSum = long.MinValue;
        for (int i = 0; i < n; i++) {
            if (i != 0 && graph[i].Count == 1) { // leaf
                isLeaf[i] = true;
                if (sumPath[i] > maxSum) maxSum = sumPath[i];
            }
        }

        const long INF = long.MaxValue / 4;
        long[] subMin = new long[n];
        for (int i = order.Count - 1; i >= 0; i--) {
            int u = order[i];
            if (isLeaf[u]) {
                subMin[u] = maxSum - sumPath[u];
            } else {
                long mn = INF;
                foreach (int v in graph[u]) {
                    if (v == parent[u]) continue;
                    if (subMin[v] < mn) mn = subMin[v];
                }
                subMin[u] = mn;
            }
        }

        int ans = 0;
        var stack2 = new Stack<(int node, long cum)>();
        stack2.Push((0, 0L));
        while (stack2.Count > 0) {
            var (u, cum) = stack2.Pop();
            if (subMin[u] > cum) {
                long add = subMin[u] - cum;
                ans++;
                cum += add;
            }
            foreach (int v in graph[u]) {
                if (v == parent[u]) continue;
                stack2.Push((v, cum));
            }
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
 * @param {number[]} cost
 * @return {number}
 */
var minIncrease = function(n, edges, cost) {
    const adj = Array.from({length: n}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    
    const parent = new Array(n).fill(-1);
    const curSum = new Array(n).fill(0);
    const order = [];
    
    // DFS to set parent and prefix sums
    const stack = [0];
    parent[0] = -1;
    curSum[0] = cost[0];
    while (stack.length) {
        const node = stack.pop();
        order.push(node);
        for (const nb of adj[node]) {
            if (nb === parent[node]) continue;
            parent[nb] = node;
            curSum[nb] = curSum[node] + cost[nb];
            stack.push(nb);
        }
    }
    
    // Find max leaf sum
    let maxLeaf = -Infinity;
    const isLeaf = new Array(n).fill(false);
    for (let i = 0; i < n; ++i) {
        if (i !== 0 && adj[i].length === 1) { // leaf (excluding root)
            isLeaf[i] = true;
            if (curSum[i] > maxLeaf) maxLeaf = curSum[i];
        }
    }
    // Edge case: root itself could be a leaf when n===1 (not in constraints)
    if (n === 1) {
        maxLeaf = curSum[0];
        isLeaf[0] = true;
    }
    
    const minDeltaSub = new Array(n).fill(0);
    // Initialize leaves with their delta
    for (let i = 0; i < n; ++i) {
        if (isLeaf[i]) {
            minDeltaSub[i] = maxLeaf - curSum[i];
        }
    }
    
    // Post-order compute minimum delta in each subtree
    for (let idx = order.length - 1; idx >= 0; --idx) {
        const node = order[idx];
        if (isLeaf[node]) continue;
        let minVal = Infinity;
        for (const nb of adj[node]) {
            if (nb === parent[node]) continue;
            if (minDeltaSub[nb] < minVal) minVal = minDeltaSub[nb];
        }
        // For internal nodes with no children (shouldn't happen), keep 0
        minDeltaSub[node] = (minVal === Infinity ? 0 : minVal);
    }
    
    // Count nodes where the required increment changes compared to parent
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        const p = parent[i];
        const parentVal = (p === -1) ? 0 : minDeltaSub[p];
        if (minDeltaSub[i] !== parentVal) ans++;
    }
    
    return ans;
};
```

## Typescript

```typescript
function minIncrease(n: number, edges: number[][], cost: number[]): number {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const parent = new Int32Array(n);
    parent.fill(-1);
    const sum = new Array<number>(n);
    const order: number[] = [];

    const stack: number[] = [0];
    parent[0] = 0;
    sum[0] = cost[0];

    while (stack.length) {
        const node = stack.pop()!;
        order.push(node);
        for (const nb of adj[node]) {
            if (parent[nb] === -1) {
                parent[nb] = node;
                sum[nb] = sum[node] + cost[nb];
                stack.push(nb);
            }
        }
    }

    const isLeaf = new Uint8Array(n);
    let maxSum = 0;
    for (let i = 0; i < n; i++) {
        if (i !== 0 && adj[i].length === 1) {
            isLeaf[i] = 1;
            if (sum[i] > maxSum) maxSum = sum[i];
        }
    }

    const required = new Array<number>(n).fill(0);
    for (let i = order.length - 1; i >= 0; i--) {
        const node = order[i];
        if (isLeaf[node]) {
            required[node] = maxSum - sum[node];
        } else {
            let mx = 0;
            for (const nb of adj[node]) {
                if (parent[nb] === node) {
                    if (required[nb] > mx) mx = required[nb];
                }
            }
            required[node] = mx;
        }
    }

    let ans = 0;
    for (let i = 0; i < n; i++) {
        const parentReq = i === 0 ? 0 : required[parent[i]];
        if (required[i] > parentReq) ans++;
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
     * @param Integer[] $cost
     * @return Integer
     */
    function minIncrease($n, $edges, $cost) {
        // Build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }

        // First DFS to get parent, order and prefix sums
        $parent = array_fill(0, $n, -1);
        $sum = array_fill(0, $n, 0);
        $order = [];
        $stack = [0];
        $parent[0] = -2; // mark root visited
        $sum[0] = $cost[0];

        while (!empty($stack)) {
            $node = array_pop($stack);
            $order[] = $node;
            foreach ($adj[$node] as $nei) {
                if ($parent[$nei] === -1) {
                    $parent[$nei] = $node;
                    $sum[$nei] = $sum[$node] + $cost[$nei];
                    $stack[] = $nei;
                }
            }
        }

        // Identify leaves and compute global max leaf sum
        $globalMax = PHP_INT_MIN;
        $isLeaf = array_fill(0, $n, false);
        foreach ($order as $node) {
            if ($node != 0 && count($adj[$node]) == 1) { // leaf (excluding root)
                $isLeaf[$node] = true;
                if ($sum[$node] > $globalMax) $globalMax = $sum[$node];
            }
        }
        // Edge case: root could be a leaf when n==1, but constraints n>=2 so ignore.

        // Second pass (post-order) to compute min deficit in each subtree
        $minDef = array_fill(0, $n, PHP_INT_MAX);
        for ($i = count($order) - 1; $i >= 0; --$i) {
            $node = $order[$i];
            if ($isLeaf[$node]) {
                $minDef[$node] = $globalMax - $sum[$node];
            } else {
                $curMin = PHP_INT_MAX;
                foreach ($adj[$node] as $nei) {
                    if ($parent[$nei] === $node) { // child
                        if ($minDef[$nei] < $curMin) $curMin = $minDef[$nei];
                    }
                }
                // If node has no children (possible only for root in degenerate case)
                if ($curMin === PHP_INT_MAX) {
                    // treat as leaf (should not happen with given constraints)
                    $curMin = $globalMax - $sum[$node];
                }
                $minDef[$node] = $curMin;
            }
        }

        // Count nodes where minDef differs from parent
        $ans = 0;
        for ($i = 1; $i < $n; ++$i) {
            $p = $parent[$i];
            if ($minDef[$i] > $minDef[$p]) {
                $ans++;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minIncrease(_ n: Int, _ edges: [[Int]], _ cost: [Int]) -> Int {
        var adj = [[Int]](repeating: [], count: n)
        for e in edges {
            let u = e[0], v = e[1]
            adj[u].append(v)
            adj[v].append(u)
        }
        
        var parent = [Int](repeating: -1, count: n)
        var pathSum = [Int64](repeating: 0, count: n)
        var order = [Int]()
        var stack: [(Int, Int64)] = []
        let root = 0
        stack.append((root, Int64(cost[root])))
        parent[root] = -2   // mark visited
        
        while let (node, cur) = stack.popLast() {
            pathSum[node] = cur
            order.append(node)
            for nb in adj[node] {
                if nb == parent[node] { continue }
                parent[nb] = node
                stack.append((nb, cur + Int64(cost[nb])))
            }
        }
        
        // compute max leaf path sum
        var maxPath: Int64 = 0
        for i in 0..<n {
            let isLeaf = (i != root && adj[i].count == 1) || (n == 1 && i == root)
            if isLeaf {
                if pathSum[i] > maxPath { maxPath = pathSum[i] }
            }
        }
        
        var required = [Int64](repeating: 0, count: n)
        for node in order.reversed() {
            let isLeaf = (node != root && adj[node].count == 1) || (n == 1 && node == root)
            if isLeaf {
                required[node] = maxPath - pathSum[node]
            } else {
                var mx: Int64 = 0
                for nb in adj[node] {
                    if nb == parent[node] { continue }
                    if required[nb] > mx { mx = required[nb] }
                }
                required[node] = mx
            }
        }
        
        var ans = 0
        if required[root] > 0 { ans += 1 }
        for i in 1..<n {
            let p = parent[i]
            if required[i] > required[p] {
                ans += 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minIncrease(n: Int, edges: Array<IntArray>, cost: IntArray): Int {
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        val parent = IntArray(n) { -1 }
        val order = IntArray(n)
        var idx = 0
        val stack = java.util.ArrayDeque<Int>()
        stack.add(0)
        parent[0] = 0
        while (stack.isNotEmpty()) {
            val u = stack.removeLast()
            order[idx++] = u
            for (v in adj[u]) {
                if (parent[v] == -1) {
                    parent[v] = u
                    stack.add(v)
                }
            }
        }

        // path sums from root
        val sum = LongArray(n)
        sum[0] = cost[0].toLong()
        for (i in 0 until n) {
            val u = order[i]
            for (v in adj[u]) {
                if (parent[v] == u) {
                    sum[v] = sum[u] + cost[v]
                }
            }
        }

        // identify leaves and compute max leaf sum
        var maxSum = Long.MIN_VALUE
        val isLeaf = BooleanArray(n)
        for (i in 0 until n) {
            if (i != 0 && adj[i].size == 1) { // leaf (excluding root)
                isLeaf[i] = true
                if (sum[i] > maxSum) maxSum = sum[i]
            }
        }

        // need array: minimal additional cost required in subtree
        val need = LongArray(n)
        for (i in n - 1 downTo 0) {
            val u = order[i]
            if (isLeaf[u]) {
                need[u] = maxSum - sum[u]
            } else {
                var minVal: Long? = null
                for (v in adj[u]) {
                    if (parent[v] == u) {
                        val childNeed = need[v]
                        if (minVal == null || childNeed < minVal) minVal = childNeed
                    }
                }
                need[u] = minVal ?: 0L
            }
        }

        var ans = 0
        for (i in 1 until n) {
            if (need[i] != need[parent[i]]) ans++
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minIncrease(int n, List<List<int>> edges, List<int> cost) {
    // Build adjacency list
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      adj[u].add(v);
      adj[v].add(u);
    }

    // Parent array and traversal order
    List<int> parent = List.filled(n, -1);
    List<int> order = [];
    List<int> stack = [0];
    parent[0] = -2; // mark root's parent specially

    // Path sums from root to each node
    List<int> pathSum = List.filled(n, 0);
    pathSum[0] = cost[0];

    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      order.add(node);
      for (int nb in adj[node]) {
        if (parent[nb] == -1) {
          parent[nb] = node;
          pathSum[nb] = pathSum[node] + cost[nb];
          stack.add(nb);
        }
      }
    }

    // Identify leaves and compute max leaf sum M
    int maxLeafSum = 0;
    List<bool> isLeaf = List.filled(n, false);
    for (int i = 0; i < n; ++i) {
      if ((adj[i].length == 1 && i != 0) || (i == 0 && adj[i].isEmpty)) {
        isLeaf[i] = true;
        if (pathSum[i] > maxLeafSum) maxLeafSum = pathSum[i];
      }
    }

    // Compute minIncrease value for each node (post-order)
    List<int> minInc = List.filled(n, 0);
    const int INF = 1 << 60;

    for (int idx = order.length - 1; idx >= 0; --idx) {
      int node = order[idx];
      if (isLeaf[node]) {
        minInc[node] = maxLeafSum - pathSum[node];
      } else {
        int best = INF;
        for (int nb in adj[node]) {
          if (parent[nb] == node) {
            if (minInc[nb] < best) best = minInc[nb];
          }
        }
        // If a non-leaf node somehow has no children (shouldn't happen), keep 0
        minInc[node] = best == INF ? 0 : best;
      }
    }

    // Count nodes where minInc differs from parent (root compared to 0)
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      int parentIdx = parent[i];
      int parentVal = (parentIdx == -2 || parentIdx == -1) ? 0 : minInc[parentIdx];
      if (minInc[i] != parentVal) ans++;
    }
    return ans;
  }
}
```

## Golang

```go
func minIncrease(n int, edges [][]int, cost []int) int {
    adj := make([][]int, n)
    for _, e := range edges {
        u, v := e[0], e[1]
        adj[u] = append(adj[u], v)
        adj[v] = append(adj[v], u)
    }

    parent := make([]int, n)
    for i := 0; i < n; i++ {
        parent[i] = -2
    }
    sum := make([]int64, n)
    order := make([]int, 0, n)

    stack := []int{0}
    parent[0] = -1
    sum[0] = int64(cost[0])
    for len(stack) > 0 {
        u := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        order = append(order, u)
        for _, v := range adj[u] {
            if v == parent[u] {
                continue
            }
            parent[v] = u
            sum[v] = sum[u] + int64(cost[v])
            stack = append(stack, v)
        }
    }

    var maxLeafSum int64 = 0
    for i := 0; i < n; i++ {
        if i != 0 && len(adj[i]) == 1 { // leaf (excluding root)
            if sum[i] > maxLeafSum {
                maxLeafSum = sum[i]
            }
        }
    }

    need := make([]int64, n)
    for i := len(order) - 1; i >= 0; i-- {
        u := order[i]
        if u != 0 && len(adj[u]) == 1 { // leaf
            need[u] = sum[u]
        } else {
            var mx int64 = 0
            for _, v := range adj[u] {
                if v == parent[u] {
                    continue
                }
                if need[v] > mx {
                    mx = need[v]
                }
            }
            need[u] = mx
        }
    }

    minInc := make([]int64, n)
    for i := 0; i < n; i++ {
        minInc[i] = maxLeafSum - need[i]
    }

    ans := 0
    for i := 0; i < n; i++ {
        if parent[i] == -1 { // root
            if minInc[i] > 0 {
                ans++
            }
        } else {
            if minInc[i] != minInc[parent[i]] {
                ans++
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def min_increase(n, edges, cost)
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  # First pass: find maximum root-to-leaf sum
  max_sum = -1 << 60
  stack = [[0, -1, cost[0]]]
  until stack.empty?
    node, parent, cur_sum = stack.pop
    children = adj[node].reject { |x| x == parent }
    if children.empty?
      max_sum = cur_sum if cur_sum > max_sum
    else
      children.each do |ch|
        stack << [ch, node, cur_sum + cost[ch]]
      end
    end
  end

  # Second pass: post‑order to compute needed increments and count nodes
  needs = Array.new(n, 0)
  ans = 0
  stack = [[0, -1, cost[0], false]] # node, parent, cur_sum, visited flag
  until stack.empty?
    node, parent, cur_sum, visited = stack.pop
    if visited
      children = adj[node].reject { |x| x == parent }
      if children.empty?
        need = max_sum - cur_sum
      else
        child_needs = children.map { |ch| needs[ch] }
        max_c = child_needs.max
        min_c = child_needs.min
        ans += 1 if max_c != min_c
        need = min_c
      end
      needs[node] = need
    else
      stack << [node, parent, cur_sum, true]
      adj[node].each do |ch|
        next if ch == parent
        stack << [ch, node, cur_sum + cost[ch], false]
      end
    end
  end

  ans += 1 if needs[0] > 0
  ans
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{ArrayBuffer, ArrayStack}
  def minIncrease(n: Int, edges: Array[Array[Int]], cost: Array[Int]): Int = {
    val adj = Array.fill(n)(new ArrayBuffer[Int]())
    for (e <- edges) {
      val u = e(0); val v = e(1)
      adj(u).append(v)
      adj(v).append(u)
    }

    // parent, order (preorder), path sum
    val parent = Array.fill(n)(-2)
    val order = new ArrayBuffer[Int]()
    val pathSum = new Array[Long](n)

    val stack = new java.util.ArrayDeque[Int]()
    stack.push(0)
    parent(0) = -1
    pathSum(0) = cost(0).toLong

    while (!stack.isEmpty) {
      val v = stack.pop()
      order.append(v)
      for (nb <- adj(v)) {
        if (parent(nb) == -2) {
          parent(nb) = v
          pathSum(nb) = pathSum(v) + cost(nb).toLong
          stack.push(nb)
        }
      }
    }

    // identify leaves and compute max leaf sum
    val isLeaf = new Array[Boolean](n)
    var maxLeafSum = Long.MinValue
    for (v <- 0 until n) {
      var childCnt = 0
      for (nb <- adj(v)) if (parent(nb) == v) childCnt += 1
      if (childCnt == 0) {
        isLeaf(v) = true
        if (pathSum(v) > maxLeafSum) maxLeafSum = pathSum(v)
      }
    }

    // leaf deficits and residual need initialization
    val leafDeficit = new Array[Long](n)
    val residualNeed = new Array[Long](n)
    for (v <- 0 until n) {
      if (isLeaf(v)) {
        val d = maxLeafSum - pathSum(v)
        leafDeficit(v) = d
        residualNeed(v) = d
      }
    }

    // bottom‑up to compute increments at internal nodes
    val inc = new Array[Long](n)
    var internalCount = 0
    for (i <- order.length - 1 to 0 by -1) {
      val v = order(i)
      if (!isLeaf(v)) {
        var maxN = Long.MinValue
        var minN = Long.MaxValue
        var hasChild = false
        for (nb <- adj(v)) {
          if (parent(nb) == v) {
            hasChild = true
            val rn = residualNeed(nb)
            if (rn > maxN) maxN = rn
            if (rn < minN) minN = rn
          }
        }
        if (hasChild) {
          inc(v) = minN
          if (inc(v) > 0) internalCount += 1
          residualNeed(v) = maxN - minN
        } else {
          // should not happen as leaves are handled earlier
          inc(v) = 0
          residualNeed(v) = 0
        }
      }
    }

    // top‑down to count leaf increments needed
    var leafCount = 0
    val stack2 = new java.util.ArrayDeque[(Int, Long)]()
    stack2.push((0, 0L))
    while (!stack2.isEmpty) {
      val (v, acc) = stack2.pop()
      if (isLeaf(v)) {
        if (leafDeficit(v) > acc) leafCount += 1
      } else {
        val newAcc = acc + inc(v)
        for (nb <- adj(v)) {
          if (parent(nb) == v) {
            stack2.push((nb, newAcc))
          }
        }
      }
    }

    internalCount + leafCount
  }
}
```

## Rust

```rust
use std::cmp::min;

impl Solution {
    pub fn min_increase(n: i32, edges: Vec<Vec<i32>>, cost: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut adj = vec![Vec::<usize>::new(); n];
        for e in edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }
        let cost: Vec<i64> = cost.iter().map(|&x| x as i64).collect();

        // parent, order (preorder), and prefix sums
        let mut parent = vec![n; n];
        let mut order = Vec::with_capacity(n);
        let mut stack = Vec::new();
        stack.push(0usize);
        parent[0] = 0;
        let mut sum = vec![0i64; n];
        sum[0] = cost[0];

        while let Some(v) = stack.pop() {
            order.push(v);
            for &to in &adj[v] {
                if to != parent[v] {
                    parent[to] = v;
                    sum[to] = sum[v] + cost[to];
                    stack.push(to);
                }
            }
        }

        // find leaves and maximum leaf sum
        let mut max_leaf_sum = i64::MIN;
        for &v in &order {
            if v != 0 && adj[v].len() == 1 {
                if sum[v] > max_leaf_sum {
                    max_leaf_sum = sum[v];
                }
            }
        }

        // deficit for each leaf
        let mut deficit = vec![0i64; n];
        for &v in &order {
            if v != 0 && adj[v].len() == 1 {
                deficit[v] = max_leaf_sum - sum[v];
            }
        }

        // DP bottom‑up
        let mut cnt = vec![0i32; n];
        let mut rem = vec![0i64; n]; // remaining deficit to be satisfied by ancestors

        for &v in order.iter().rev() {
            // collect children (excluding parent)
            let mut children = Vec::new();
            for &to in &adj[v] {
                if to != parent[v] {
                    children.push(to);
                }
            }
            if children.is_empty() {
                // leaf
                rem[v] = deficit[v];
                cnt[v] = 0;
            } else {
                let mut min_r = i64::MAX;
                for &c in &children {
                    if rem[c] < min_r {
                        min_r = rem[c];
                    }
                }
                let mut total_cnt: i32 = 0;
                for &c in &children {
                    total_cnt += cnt[c];
                    if rem[c] > min_r {
                        // increase child node to lower its remaining deficit
                        total_cnt += 1;
                    }
                }
                cnt[v] = total_cnt;
                rem[v] = min_r;
            }
        }

        let root = 0usize;
        let mut answer = cnt[root];
        if rem[root] > 0 {
            answer += 1; // increase the root
        }
        answer
    }
}
```

## Racket

```racket
(define/contract (min-increase n edges cost)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)
  (let* ((adj (make-vector n '()))
         ;; build adjacency
         (_ (for-each (lambda (e)
                        (let ((u (first e))
                              (v (second e)))
                          (vector-set! adj u (cons v (vector-ref adj u)))
                          (vector-set! adj v (cons u (vector-ref adj v)))))
                      edges))
         (cost-vec (list->vector cost))
         (parent (make-vector n -2))
         (prefix (make-vector n 0))
         ;; iterative DFS stacks
         (stack1 (list 0))
         (stack2 '()))
    ;; initialize root
    (vector-set! parent 0 -1)
    (vector-set! prefix 0 (vector-ref cost-vec 0))
    ;; DFS to set parent, prefix and obtain postorder in stack2
    (let loop ()
      (when (not (null? stack1))
        (define node (car stack1))
        (set! stack1 (cdr stack1))
        (set! stack2 (cons node stack2)) ; will be post‑order when finished
        (for-each (lambda (nb)
                    (when (= (vector-ref parent nb) -2)
                      (vector-set! parent nb node)
                      (vector-set! prefix nb (+ (vector-ref cost-vec nb)
                                                (vector-ref prefix node)))
                      (set! stack1 (cons nb stack1))))
                  (vector-ref adj node))
        (loop)))
    ;; find global maximum leaf sum
    (define max-leaf 0)
    (for ([i (in-range n)])
      (when (and (not (= i 0)) (= (length (vector-ref adj i)) 1))
        (set! max-leaf (max max-leaf (vector-ref prefix i)))))
    ;; compute maxSub for each node (maximum leaf sum in its subtree)
    (define max-sub (make-vector n 0))
    (for ([node (in-list stack2)]) ; children before parents
      (let ((best -1))
        (for-each (lambda (nb)
                    (when (= (vector-ref parent nb) node)
                      (set! best (max best (vector-ref max-sub nb)))))
                  (vector-ref adj node))
        (if (= best -1)
            (vector-set! max-sub node (vector-ref prefix node)) ; leaf
            (vector-set! max-sub node best))))
    ;; min increase needed at each node
    (define min-inc (make-vector n 0))
    (for ([i (in-range n)])
      (vector-set! min-inc i (- max-leaf (vector-ref max-sub i))))
    ;; count nodes where increment value changes compared to parent
    (let ((ans 0))
      (when (> (vector-ref min-inc 0) 0)
        (set! ans (+ ans 1)))
      (for ([i (in-range 1 n)])
        (when (> (vector-ref min-inc i)
                 (vector-ref min-inc (vector-ref parent i)))
          (set! ans (+ ans 1))))
      ans)))
```

## Erlang

```erlang
-spec min_increase(N :: integer(), Edges :: [[integer()]], Cost :: [integer()]) -> integer().
min_increase(_N, Edges, Cost) ->
    Adj0 = build_adj(Edges, #{}),
    % DFS to get parent map, order (preorder), and sum of costs along path
    {ParentMap, Order, SumMap} = dfs(Adj0, Cost),
    % Identify leaves
    Leaves = [Node || Node <- maps:keys(Adj0),
                     Node =/= 0,
                     length(maps:get(Node, Adj0)) == 1],
    % Compute max leaf sum
    MaxSum = lists:max([maps:get(L, SumMap) || L <- Leaves]),
    % Deficit for each leaf
    DefMap = maps:from_list([{L, MaxSum - maps:get(L, SumMap)} || L <- Leaves]),
    % Post-order processing to compute minimal deficit in subtree
    RevOrder = lists:reverse(Order),
    MinDefMap = compute_min_def(RevOrder, Adj0, ParentMap, DefMap, #{}),
    % Count nodes where minDef differs from parent (excluding root)
    count_changes(MinDefMap, ParentMap).

%% Build adjacency map
build_adj([], Adj) -> Adj;
build_adj([[U,V]|Rest], Adj) ->
    Adj1 = add_neighbor(Adj, U, V),
    Adj2 = add_neighbor(Adj1, V, U),
    build_adj(Rest, Adj2).

add_neighbor(Adj, From, To) ->
    case maps:is_key(From, Adj) of
        true ->
            List = maps:get(From, Adj),
            maps:put(From, [To|List], Adj);
        false ->
            maps:put(From, [To], Adj)
    end.

%% DFS iterative using stack
dfs(Adj, Cost) ->
    Stack0 = [{0, -1}],
    ParentMap0 = #{},
    Order0 = [],
    SumMap0 = #{},
    dfs_loop(Stack0, Adj, Cost, ParentMap0, Order0, SumMap0).

dfs_loop([], _Adj, _Cost, ParentMap, Order, SumMap) ->
    {ParentMap, lists:reverse(Order), SumMap};
dfs_loop([{Node, Par}|Rest], Adj, Cost, ParentMap, Order, SumMap) ->
    ParentMap1 = maps:put(Node, Par, ParentMap),
    PrevSum = case Par of
                  -1 -> 0;
                  _ -> maps:get(Par, SumMap)
              end,
    CurSum = PrevSum + lists:nth(Node+1, Cost), % Cost list is 0-indexed, nth/2 is 1-indexed
    SumMap1 = maps:put(Node, CurSum, SumMap),
    Neigh = maps:get(Node, Adj),
    Children = [C || C <- Neigh, C =/= Par],
    Stack1 = [{C, Node} || C <- Children] ++ Rest,
    dfs_loop(Stack1, Adj, Cost, ParentMap1, [Node|Order], SumMap1).

%% Compute minimal deficit per subtree (post-order)
compute_min_def([], _Adj, _ParentMap, _DefMap, MinDefAcc) ->
    MinDefAcc;
compute_min_def([Node|Rest], Adj, ParentMap, DefMap, MinDefAcc) ->
    MinDef =
        case maps:is_key(Node, DefMap) of
            true -> maps:get(Node, DefMap);
            false ->
                Children = [C || C <- maps:get(Node, Adj), C =/= maps:get(Node, ParentMap)],
                ChildMins = [maps:get(C, MinDefAcc) || C <- Children],
                lists:min(ChildMins)
        end,
    NewAcc = maps:put(Node, MinDef, MinDefAcc),
    compute_min_def(Rest, Adj, ParentMap, DefMap, NewAcc).

%% Count nodes where minDef differs from parent (excluding root)
count_changes(MinDefMap, ParentMap) ->
    Nodes = maps:keys(ParentMap),
    lists:foldl(fun(Node, Acc) ->
                        case maps:get(Node, ParentMap) of
                            -1 -> Acc; % root
                            Par ->
                                if maps:get(Node, MinDefMap) =/= maps:get(Par, MinDefMap) ->
                                        Acc + 1;
                                   true -> Acc
                                end
                        end
                end, 0, Nodes).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_increase(integer, [[integer]], [integer]) :: integer
  def min_increase(n, edges, cost) do
    # adjacency list (undirected)
    adj =
      Enum.reduce(edges, %{}, fn [u, v], acc ->
        acc
        |> Map.update(u, [v], &[v | &1])
        |> Map.update(v, [u], &[u | &1])
      end)

    cost_arr = :array.from_list(cost)

    parent_arr = :array.new(n, default: -1)
    sum_arr = :array.new(n, default: 0)
    children_arr = :array.new(n, default: [])

    # iterative DFS to set parents, sums and children, also record preorder
    {parent_arr, sum_arr, children_arr, preorder} =
      dfs_iter(0, -1, adj, cost_arr, parent_arr, sum_arr, children_arr, [])

    postorder = Enum.reverse(preorder)

    # find target: maximum root-to-leaf path sum
    target =
      0..(n - 1)
      |> Enum.reduce(0, fn i, acc ->
        if :array.get(i, children_arr) == [] do
          s = :array.get(i, sum_arr)
          if s > acc, do: s, else: acc
        else
          acc
        end
      end)

    # bottom‑up compute max needed increment for each subtree
    max_inc_arr =
      Enum.reduce(postorder, :array.new(n, default: 0), fn node, arr ->
        children = :array.get(node, children_arr)

        max_inc =
          if children == [] do
            target - :array.get(node, sum_arr)
          else
            children
            |> Enum.map(&(:array.get(&1, arr)))
            |> Enum.max()
          end

        :array.set(node, max_inc, arr)
      end)

    # count nodes where needed value changes compared to parent (root vs 0)
    root_need = :array.get(0, max_inc_arr)
    ans = if root_need > 0, do: 1, else: 0

    ans =
      1..(n - 1)
      |> Enum.reduce(ans, fn i, acc ->
        p = :array.get(i, parent_arr)

        if :array.get(i, max_inc_arr) != :array.get(p, max_inc_arr) do
          acc + 1
        else
          acc
        end
      end)

    ans
  end

  # iterative DFS using explicit stack; returns updated arrays and preorder list
  defp dfs_iter(start, parent, adj, cost_arr, parent_arr, sum_arr, children_arr, order) do
    stack = [{start, parent}]
    do_dfs(stack, adj, cost_arr, parent_arr, sum_arr, children_arr, order)
  end

  defp do_dfs([], _adj, _cost_arr, parent_arr, sum_arr, children_arr, order),
    do: {parent_arr, sum_arr, children_arr, order}

  defp do_dfs([{node, p} | rest], adj, cost_arr, parent_arr, sum_arr, children_arr, order) do
    # set parent
    parent_arr = :array.set(node, p, parent_arr)

    # compute cumulative sum to this node
    sum_parent = if p == -1, do: 0, else: :array.get(p, sum_arr)
    sum_node = sum_parent + :array.get(node, cost_arr)
    sum_arr = :array.set(node, sum_node, sum_arr)

    neighs = Map.get(adj, node, [])

    {parent_arr2, sum_arr2, children_arr2, new_stack} =
      Enum.reduce(neighs, {parent_arr, sum_arr, children_arr, []}, fn nb,
                                                                      {parr, sarr, carr,
                                                                       adds} ->
        if nb != p do
          # record child relationship
          old = :array.get(node, carr)
          carr = :array.set(node, [nb | old], carr)
          {parr, sarr, carr, [{nb, node} | adds]}
        else
          {parr, sarr, carr, adds}
        end
      end)

    # continue DFS; prepend newly discovered nodes to stack
    do_dfs(new_stack ++ rest, adj, cost_arr, parent_arr2, sum_arr2, children_arr2,
      [node | order])
  end
end
```

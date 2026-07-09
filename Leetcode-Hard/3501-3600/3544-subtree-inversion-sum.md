# 3544. Subtree Inversion Sum

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long subtreeInversionSum(vector<vector<int>>& edges, vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> g(n);
        for (auto &e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        const int K = k;
        // dp[node][dist][parity]
        vector<vector<array<long long,2>>> dp(n, vector<array<long long,2>>(K+1));
        
        function<void(int,int)> dfs = [&](int u, int p) {
            for (int v : g[u]) if (v != p) dfs(v, u);
            
            for (int d = 0; d <= K; ++d) {
                for (int par = 0; par < 2; ++par) {
                    long long curVal = (par == 0 ? nums[u] : -nums[u]);
                    
                    // Option 1: do not invert at u
                    int nd = min(d + 1, K);
                    long long sumA = curVal;
                    for (int v : g[u]) if (v != p) {
                        sumA += dp[v][nd][par];
                    }
                    long long best = sumA;
                    
                    // Option 2: invert at u (allowed only when distance >= k)
                    if (d == K) {
                        int ndChild = 1;               // distance for children after inversion
                        int newPar = par ^ 1;           // parity toggles
                        long long invVal = -curVal;
                        long long sumB = invVal;
                        for (int v : g[u]) if (v != p) {
                            sumB += dp[v][ndChild][newPar];
                        }
                        best = max(best, sumB);
                    }
                    
                    dp[u][d][par] = best;
                }
            }
        };
        
        dfs(0, -1);
        return dp[0][K][0];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long subtreeInversionSum(int[][] edges, int[] nums, int k) {
        int n = nums.length;
        List<Integer>[] g = new ArrayList[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }

        int[] parent = new int[n];
        int[] order = new int[n];
        int idx = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        parent[0] = -1;
        while (!stack.isEmpty()) {
            int node = stack.pop();
            order[idx++] = node;
            for (int nb : g[node]) {
                if (nb == parent[node]) continue;
                parent[nb] = node;
                stack.push(nb);
            }
        }

        // dp[node][parity][dist] where dist in [0..k], k means >=k
        long[][][] dp = new long[n][2][k + 1];
        for (int i = n - 1; i >= 0; --i) {
            int node = order[i];
            for (int p = 0; p < 2; ++p) {
                for (int d = 0; d <= k; ++d) {
                    long sumNoInv = (p == 0 ? nums[node] : - (long) nums[node]);
                    for (int nb : g[node]) {
                        if (nb == parent[node]) continue;
                        int nd = d + 1;
                        if (nd > k) nd = k;
                        sumNoInv += dp[nb][p][nd];
                    }
                    long best = sumNoInv;
                    if (d == k) { // can invert here
                        int p2 = p ^ 1;
                        long sumInv = (p2 == 0 ? nums[node] : - (long) nums[node]);
                        for (int nb : g[node]) {
                            if (nb == parent[node]) continue;
                            sumInv += dp[nb][p2][1];
                        }
                        best = Math.max(best, sumInv);
                    }
                    dp[node][p][d] = best;
                }
            }
        }
        return dp[0][0][k];
    }
}
```

## Python

```python
class Solution(object):
    def subtreeInversionSum(self, edges, nums, k):
        """
        :type edges: List[List[int]]
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Build adjacency list
        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        sys.setrecursionlimit(10**6)

        from functools import lru_cache

        @lru_cache(None)
        def dfs(u, parent):
            # dp[t][p] = max sum in subtree u using t inversions,
            # where p is parity of flips applied by ancestors (0 even,1 odd)
            # Returns a list of two lists: dp_even and dp_odd
            # Initialize with no inversion at this node
            dp_even = [-10**18] * (k + 1)
            dp_odd = [-10**18] * (k + 1)

            base_val = nums[u]
            dp_even[0] = base_val
            dp_odd[0] = -base_val

            for v in g[u]:
                if v == parent:
                    continue
                child_even, child_odd = dfs(v, u)
                new_even = [-10**18] * (k + 1)
                new_odd = [-10**18] * (k + 1)

                for i in range(k + 1):
                    if dp_even[i] == -10**18 and dp_odd[i] == -10**18:
                        continue
                    for j in range(k - i + 1):
                        # combine when current parity is even
                        if dp_even[i] != -10**18:
                            val = max(child_even[j], child_odd[j])
                            new_even[i + j] = max(new_even[i + j], dp_even[i] + val)
                        # combine when current parity is odd
                        if dp_odd[i] != -10**18:
                            val = max(child_even[j], child_odd[j])
                            new_odd[i + j] = max(new_odd[i + j], dp_odd[i] + val)

                dp_even, dp_odd = new_even, new_odd

            # Option to place an inversion at u
            for t in range(k, 0, -1):
                # flipping parity adds one inversion
                dp_even[t] = max(dp_even[t], dp_odd[t - 1])
                dp_odd[t] = max(dp_odd[t], dp_even[t - 1])

            return tuple(dp_even), tuple(dp_odd)

        root_even, root_odd = dfs(0, -1)
        return max(max(root_even), max(root_odd))
```

## Python3

```python
import sys
from typing import List

sys.setrecursionlimit(1000000)

class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        INF_NEG = -10**18

        def dfs(u: int, p: int):
            # dp0[t]: max sum of subtree u when total inversions on path to u is even
            # dp1[t]: same but odd parity
            dp0 = [INF_NEG] * (k + 1)
            dp1 = [INF_NEG] * (k + 1)
            dp0[0] = nums[u]
            dp1[0] = -nums[u]
            cur_max = 0  # maximum t with feasible value so far

            for v in adj[u]:
                if v == p:
                    continue
                child0, child1 = dfs(v, u)

                new0 = [INF_NEG] * (k + 1)
                new1 = [INF_NEG] * (k + 1)

                # merge for even parity (dp0 with child's even dp0)
                for i in range(cur_max + 1):
                    if dp0[i] == INF_NEG:
                        continue
                    for j in range(k - i + 1):
                        if child0[j] == INF_NEG:
                            continue
                        val = dp0[i] + child0[j]
                        if val > new0[i + j]:
                            new0[i + j] = val

                # merge for odd parity (dp1 with child's odd dp1)
                for i in range(cur_max + 1):
                    if dp1[i] == INF_NEG:
                        continue
                    for j in range(k - i + 1):
                        if child1[j] == INF_NEG:
                            continue
                        val = dp1[i] + child1[j]
                        if val > new1[i + j]:
                            new1[i + j] = val

                cur_max = min(k, cur_max + k)  # still bounded by k
                dp0, dp1 = new0, new1

            # consider performing inversion at u
            final0 = dp0[:]
            final1 = dp1[:]

            for t in range(1, k + 1):
                if dp1[t - 1] != INF_NEG:
                    # invert here: parity flips, consume one inversion
                    val = dp1[t - 1]
                    if val > final0[t]:
                        final0[t] = val
                if dp0[t - 1] != INF_NEG:
                    val = dp0[t - 1]
                    if val > final1[t]:
                        final1[t] = val

            return final0, final1

        root_dp0, _ = dfs(0, -1)
        return max(root_dp0[:k + 1])
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static const long long NEG_INF = -(1LL<<60);
static int MAXK;
static vector<vector<int>> graph;
static vector<long long> nodeVal;

vector<vector<long long>> dfs(int u, int parent){
    // f0: subtree sum when u is NOT inverted
    // f1: subtree sum when u IS inverted (consumes one inversion at u)
    vector<vector<long long>> f0(MAXK+1, vector<long long>(2, NEG_INF));
    vector<vector<long long>> f1(MAXK+1, vector<long long>(2, NEG_INF));

    for(int parity=0; parity<2; ++parity){
        long long base = nodeVal[u] * (parity ? -1LL : 1LL);
        f0[0][parity] = base;
        if(MAXK>=1){
            long long invBase = nodeVal[u] * (parity ? 1LL : -1LL);
            f1[1][parity] = invBase;
        }
    }

    for(int v: graph[u]){
        if(v==parent) continue;
        auto child = dfs(v, u);

        vector<vector<long long>> nf0(MAXK+1, vector<long long>(2, NEG_INF));
        vector<vector<long long>> nf1(MAXK+1, vector<long long>(2, NEG_INF));

        // merge for f0 (parity unchanged)
        for(int cu=0; cu<=MAXK; ++cu){
            for(int parity=0; parity<2; ++parity){
                long long cur = f0[cu][parity];
                if(cur==NEG_INF) continue;
                for(int cv=0; cv+cu<=MAXK; ++cv){
                    long long childVal = child[cv][parity];
                    if(childVal==NEG_INF) continue;
                    long long &ref = nf0[cu+cv][parity];
                    long long cand = cur + childVal;
                    if(cand > ref) ref = cand;
                }
            }
        }

        // merge for f1 (parity toggled)
        for(int cu=0; cu<=MAXK; ++cu){
            for(int parity=0; parity<2; ++parity){
                long long cur = f1[cu][parity];
                if(cur==NEG_INF) continue;
                int childParity = parity ^ 1;
                for(int cv=0; cv+cu<=MAXK; ++cv){
                    long long childVal = child[cv][childParity];
                    if(childVal==NEG_INF) continue;
                    long long &ref = nf1[cu+cv][parity];
                    long long cand = cur + childVal;
                    if(cand > ref) ref = cand;
                }
            }
        }

        f0.swap(nf0);
        f1.swap(nf1);
    }

    vector<vector<long long>> res(MAXK+1, vector<long long>(2, NEG_INF));
    for(int c=0; c<=MAXK; ++c){
        for(int p=0; p<2; ++p){
            res[c][p] = max(f0[c][p], f1[c][p]);
        }
    }
    return res;
}

long long subtreeInversionSum(int** edges, int edgesSize, int* edgesColSize, int* nums, int numsSize, int k) {
    MAXK = k;
    graph.assign(numsSize, {});
    for(int i=0;i<edgesSize;++i){
        int u = edges[i][0];
        int v = edges[i][1];
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    nodeVal.resize(numsSize);
    for(int i=0;i<numsSize;++i) nodeVal[i]=nums[i];

    auto dpRoot = dfs(0, -1);
    long long ans = NEG_INF;
    for(int used=0; used<=k; ++used){
        ans = max(ans, dpRoot[used][0]); // root parity 0 (no ancestor inversion)
    }
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long SubtreeInversionSum(int[][] edges, int[] nums, int k) {
        int n = nums.Length;
        var adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            adj[u].Add(v);
            adj[v].Add(u);
        }

        // Build parent array and traversal order (iterative DFS)
        var parent = new int[n];
        Array.Fill(parent, -1);
        var stack = new Stack<int>();
        var order = new List<int>(n);
        stack.Push(0);
        parent[0] = -2; // mark root
        while (stack.Count > 0) {
            int u = stack.Pop();
            order.Add(u);
            foreach (int v in adj[u]) {
                if (parent[v] == -1) {
                    parent[v] = u;
                    stack.Push(v);
                }
            }
        }

        int K = k;
        int stride = K + 1;               // number of distance states per parity
        long[][] dp = new long[n][];      // flattened [parity * stride + dist]

        // Process nodes in postorder (reverse of order)
        for (int idx = order.Count - 1; idx >= 0; idx--) {
            int u = order[idx];
            var cur = new long[2 * stride];
            dp[u] = cur;

            // Gather children
            List<int> children = new List<int>();
            foreach (int v in adj[u]) if (parent[v] == u) children.Add(v);

            for (int p = 0; p <= 1; p++) {
                long nodeValNoInv = (p == 0 ? nums[u] : -nums[u]);
                long nodeValInv   = (p == 0 ? -nums[u] : nums[u]); // parity toggled

                for (int d = 0; d <= K; d++) {
                    // Option: do NOT invert at this node
                    long sum = nodeValNoInv;
                    foreach (int v in children) {
                        var childArr = dp[v];
                        int nd = d == K ? K : Math.Min(d + 1, K);
                        sum += childArr[p * stride + nd];
                    }
                    long bestVal = sum;

                    // Option: invert here (allowed only when distance since last inversion == K)
                    if (d == K) {
                        long invSum = nodeValInv;
                        foreach (int v in children) {
                            var childArr = dp[v];
                            int ndChild = 1; // after inversion, distance for child is 1
                            invSum += childArr[(p ^ 1) * stride + ndChild];
                        }
                        if (invSum > bestVal) bestVal = invSum;
                    }

                    cur[p * stride + d] = bestVal;
                }
            }
        }

        // Answer: root with no prior inversions, distance considered K (allowed)
        return dp[0][0 * stride + K];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subtreeInversionSum = function(edges, nums, k) {
    const n = nums.length;
    const adj = Array.from({length: n}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    // parent array and order for post‑order processing
    const parent = new Int32Array(n).fill(-1);
    const order = [];
    const stack = [0];
    parent[0] = -2; // mark root visited
    while (stack.length) {
        const u = stack.pop();
        order.push(u);
        for (const v of adj[u]) {
            if (parent[v] === -1) {
                parent[v] = u;
                stack.push(v);
            }
        }
    }
    // dpEven[node][t], dpOdd[node][t]
    const dpEven = Array.from({length: n}, () => new Float64Array(k + 1).fill(Number.NEGATIVE_INFINITY));
    const dpOdd  = Array.from({length: n}, () => new Float64Array(k + 1).fill(Number.NEGATIVE_INFINITY));

    // process in reverse order (post‑order)
    for (let idx = order.length - 1; idx >= 0; --idx) {
        const u = order[idx];
        // curEven[t] / curOdd[t]: best sum of processed children when current parity is even/odd
        let curEven = new Float64Array(k + 1).fill(Number.NEGATIVE_INFINITY);
        let curOdd  = new Float64Array(k + 1).fill(Number.NEGATIVE_INFINITY);
        curEven[0] = 0;
        curOdd[0]  = 0;

        for (const v of adj[u]) {
            if (parent[v] !== u) continue; // only children
            const childEven = dpEven[v];
            const childOdd  = dpOdd[v];

            const nextEven = new Float64Array(k + 1).fill(Number.NEGATIVE_INFINITY);
            const nextOdd  = new Float64Array(k + 1).fill(Number.NEGATIVE_INFINITY);

            for (let used = 0; used <= k; ++used) {
                const baseEven = curEven[used];
                if (baseEven > Number.NEGATIVE_INFINITY) {
                    for (let c = 0; c + used <= k; ++c) {
                        const val = childEven[c];
                        if (val > Number.NEGATIVE_INFINITY) {
                            const nt = used + c;
                            const sum = baseEven + val;
                            if (sum > nextEven[nt]) nextEven[nt] = sum;
                        }
                    }
                }
                const baseOdd = curOdd[used];
                if (baseOdd > Number.NEGATIVE_INFINITY) {
                    for (let c = 0; c + used <= k; ++c) {
                        const val = childOdd[c];
                        if (val > Number.NEGATIVE_INFINITY) {
                            const nt = used + c;
                            const sum = baseOdd + val;
                            if (sum > nextOdd[nt]) nextOdd[nt] = sum;
                        }
                    }
                }
            }

            curEven = nextEven;
            curOdd  = nextOdd;
        }

        // now incorporate node u itself
        const val = nums[u];
        const dpE = dpEven[u];
        const dpO = dpOdd[u];

        for (let t = 0; t <= k; ++t) {
            // no inversion at u
            if (curEven[t] > Number.NEGATIVE_INFINITY) {
                const cand = curEven[t] + val;
                if (cand > dpE[t]) dpE[t] = cand;
            }
            if (curOdd[t] > Number.NEGATIVE_INFINITY) {
                const cand = curOdd[t] - val;
                if (cand > dpO[t]) dpO[t] = cand;
            }

            // inversion at u (requires one operation)
            if (t >= 1) {
                if (curOdd[t - 1] > Number.NEGATIVE_INFINITY) {
                    const cand = curOdd[t - 1] - val; // parity flips, node contribution becomes -val
                    if (cand > dpE[t]) dpE[t] = cand;
                }
                if (curEven[t - 1] > Number.NEGATIVE_INFINITY) {
                    const cand = curEven[t - 1] + val; // parity flips from odd to even, node contribution becomes +val
                    if (cand > dpO[t]) dpO[t] = cand;
                }
            }
        }
    }

    let ans = Number.NEGATIVE_INFINITY;
    const rootDP = dpEven[0];
    for (let t = 0; t <= k; ++t) {
        if (rootDP[t] > ans) ans = rootDP[t];
    }
    return Math.round(ans); // answer is integer
};
```

## Typescript

```typescript
function subtreeInversionSum(edges: number[][], nums: number[], k: number): number {
    const n = nums.length;
    const K = k; // minimum distance between ancestor inversion and descendant inversion
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    // Build parent array and order for post‑order processing
    const parent = new Int32Array(n).fill(-1);
    const order: number[] = [];
    const stack: number[] = [0];
    parent[0] = -2; // mark root visited
    while (stack.length) {
        const u = stack.pop()!;
        order.push(u);
        for (const v of adj[u]) {
            if (parent[v] === -1) {
                parent[v] = u;
                stack.push(v);
            }
        }
    }

    // dp[node][d][p] -> best sum in subtree rooted at node,
    // d = distance from last inversion (capped at K), p = parity (0 even, 1 odd)
    const dp: Array<Array<[number, number]>> = new Array(n);
    for (let idx = order.length - 1; idx >= 0; --idx) {
        const u = order[idx];
        const children: number[] = [];
        for (const v of adj[u]) if (parent[v] === u) children.push(v);

        // allocate dp table for node u
        const cur: Array<[number, number]> = new Array(K + 1);
        for (let d = 0; d <= K; ++d) {
            // option: do NOT invert at u
            let sumEven = nums[u];
            let sumOdd = -nums[u];
            const nd = d === K ? K : Math.min(d + 1, K); // distance passed to children when not inverting
            for (const v of children) {
                const childDP = dp[v];
                sumEven += childDP[nd][0];
                sumOdd += childDP[nd][1];
            }
            let bestEven = sumEven;
            let bestOdd = sumOdd;

            // option: invert at u (allowed only when d == K)
            if (d === K) {
                // after inversion parity toggles, distance resets to 0 for children
                let invEven = -nums[u]; // original even parity becomes odd after flip
                let invOdd = nums[u];   // original odd parity becomes even after flip
                for (const v of children) {
                    const childDP = dp[v];
                    invEven += childDP[0][1]; // parity toggled to 1
                    invOdd += childDP[0][0];  // parity toggled to 0
                }
                if (invEven > bestEven) bestEven = invEven;
                if (invOdd > bestOdd)   bestOdd = invOdd;
            }

            cur[d] = [bestEven, bestOdd];
        }
        dp[u] = cur;
    }

    // root starts with distance >= K and even parity
    return dp[0][K][0];
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer[][] $edges
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function subtreeInversionSum($edges, $nums, $k) {
        $n = count($nums);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $g[$u][] = $v;
            $g[$v][] = $u;
        }
        // dp[node][parity][d] = max sum in subtree of node,
        // parity: 0 even flips from ancestors, 1 odd flips
        // d: distance since last inversion (0..$k)
        $INF_NEG = -10**15;
        $dp = array_fill(0, $n, null);
        $stack = [[0, -1]];
        $order = [];
        while ($stack) {
            [$u,$p] = array_pop($stack);
            $order[] = [$u,$p];
            foreach ($g[$u] as $v) {
                if ($v == $p) continue;
                $stack[] = [$v,$u];
            }
        }
        // process in reverse order (post-order)
        for ($idx = count($order)-1; $idx >=0; --$idx) {
            [$u,$parent] = $order[$idx];
            // initialize dp for this node
            $dpNode = array_fill(0, 2, array_fill(0, $k+1, $INF_NEG));
            // base: leaf will be handled after merging children (none)
            foreach ([0,1] as $par) {
                // two choices at this node:
                // not invert here
                $valNo = ($par==0 ? $nums[$u] : -$nums[$u]);
                // invert here -> flips parity for children, distance resets to 0
                $valInv = ($par==0 ? -$nums[$u] : $nums[$u]);
                // start with just the node value, distance since last inversion is either:
                // if we inverted here, distance=0; else increase by 1 (capped at k)
                $dpNode[$par][($par==0?0:0)] = $valNo; // placeholder will be updated after children
            }
            // merge children
            foreach ($g[$u] as $v) {
                if ($v == $parent) continue;
                $childDP = $dp[$v];
                $newDP = array_fill(0, 2, array_fill(0, $k+1, $INF_NEG));
                for ($par=0;$par<2;$par++) {
                    for ($dist=0;$dist<=$k;$dist++) {
                        if ($dpNode[$par][$dist]==$INF_NEG) continue;
                        // option: do not invert at u (parity unchanged)
                        // child sees same parity, distance increments (if dist<k then +1 else stays k)
                        $nextDist = min($k, $dist+1);
                        for ($cDist=0;$cDist<=$k;$cDist++) {
                            if ($childDP[$par][$cDist]==$INF_NEG) continue;
                            // child's distance since last inversion relative to u is cDist,
                            // but we must ensure consistency: the child's stored distance assumes
                            // its own last inversion distance from u. Since we are just propagating,
                            // we can simply add values.
                            $newVal = $dpNode[$par][$dist] + $childDP[$par][$cDist];
                            if ($newVal > $newDP[$par][$nextDist]) {
                                $newDP[$par][$nextDist] = $newVal;
                            }
                        }
                    }
                }
                // also consider case where we invert at u before processing children
                // Inversion resets distance to 0 and flips parity for children.
                for ($par=0;$par<2;$par++) {
                    for ($dist=0;$dist<=$k;$dist++) {
                        if ($dpNode[$par][$dist]==$INF_NEG) continue;
                        $invPar = $par ^ 1;
                        $nextDist = 0; // after inversion distance resets
                        for ($cDist=0;$cDist<=$k;$cDist++) {
                            if ($childDP[$invPar][$cDist]==$INF_NEG) continue;
                            $newVal = $dpNode[$par][$dist] + $childDP[$invPar][$cDist];
                            if ($newVal > $newDP[$invPar][$nextDist]) {
                                $newDP[$invPar][$nextDist] = $newVal;
                            }
                        }
                    }
                }
                $dpNode = $newDP;
            }
            // after processing children, also consider performing inversion at u itself (if not already considered)
            // Actually handled in merge loop above by using invPar case before merging each child,
            // but we need to allow inversion exactly once at this node.
            // To simplify, we recompute final dp for this node:
            $finalDP = array_fill(0, 2, array_fill(0, $k+1, $INF_NEG));
            foreach ([0,1] as $par) {
                // not invert at u
                $baseVal = ($par==0 ? $nums[$u] : -$nums[$u]);
                $best = $INF_NEG;
                foreach (range(0,$k) as $dist) {
                    if ($dpNode[$par][$dist]==$INF_NEG) continue;
                    $candidate = $baseVal + $dpNode[$par][$dist];
                    if ($candidate > $finalDP[$par][min($k, $dist+1)]) {
                        $finalDP[$par][min($k, $dist+1)] = $candidate;
                    }
                }
                // invert at u
                $invPar = $par ^ 1;
                $baseInv = ($par==0 ? -$nums[$u] : $nums[$u]);
                foreach (range(0,$k) as $dist) {
                    if ($dpNode[$par][$dist]==$INF_NEG) continue;
                    $candidate = $baseInv + $dpNode[$par][$dist];
                    // after inversion distance resets to 0
                    if ($candidate > $finalDP[$invPar][0]) {
                        $finalDP[$invPar][0] = $candidate;
                    }
                }
            }
            $dp[$u] = $finalDP;
        }
        $ans = $INF_NEG;
        foreach (range(0,$k) as $d) {
            $ans = max($ans, $dp[0][0][$d]); // start with even parity
        }
        return $ans;
    }
}
?>
```

## Swift

```swift
class Solution {
    private var adj: [[Int]] = []
    private var values: [Int] = []
    private var K: Int = 0
    private let NEG = -1_000_000_000_000_000_000

    func subtreeInversionSum(_ edges: [[Int]], _ nums: [Int], _ k: Int) -> Int {
        self.values = nums
        self.K = k
        let n = nums.count
        adj = Array(repeating: [], count: n)
        for e in edges {
            let u = e[0], v = e[1]
            adj[u].append(v)
            adj[v].append(u)
        }
        let (dpRoot, _) = dfs(0, -1)   // root has ancestor parity 0
        var ans = NEG
        for i in 0...K {
            if dpRoot[i] > ans { ans = dpRoot[i] }
        }
        return ans
    }

    private func dfs(_ u: Int, _ parent: Int) -> ([Int], [Int]) {
        var childDPs: [([Int], [Int])] = []
        for v in adj[u] where v != parent {
            let (c0, c1) = dfs(v, u)
            childDPs.append((c0, c1))
        }
        let res0 = computeForParity(u, parity: 0, children: childDPs)
        let res1 = computeForParity(u, parity: 1, children: childDPs)
        return (res0, res1)
    }

    private func computeForParity(_ u: Int, parity p: Int, children: [([Int], [Int])]) -> [Int] {
        // merge helper
        func merge(_ cur: [Int], _ childArr: [Int]) -> [Int] {
            var next = Array(repeating: NEG, count: K + 1)
            for i in 0...K where cur[i] > NEG / 2 {
                let base = cur[i]
                if base == NEG { continue }
                let limit = K - i
                for j in 0...limit {
                    let val = childArr[j]
                    if val == NEG { continue }
                    let candidate = base + val
                    if candidate > next[i + j] {
                        next[i + j] = candidate
                    }
                }
            }
            return next
        }

        // Scenario: do NOT invert at u
        var dpNoInv = Array(repeating: NEG, count: K + 1)
        let baseNoInv = (p == 0 ? values[u] : -values[u])
        dpNoInv[0] = baseNoInv
        var curNoInv = dpNoInv
        for child in children {
            let childArr = (p == 0 ? child.0 : child.1)
            curNoInv = merge(curNoInv, childArr)
        }
        var result = curNoInv

        // Scenario: invert at u (cost 1)
        if K >= 1 {
            var dpInv = Array(repeating: NEG, count: K + 1)
            let baseInv = (p == 0 ? -values[u] : values[u])
            dpInv[1] = baseInv
            var curInv = dpInv
            for child in children {
                let childArr = ((p ^ 1) == 0 ? child.0 : child.1)
                curInv = merge(curInv, childArr)
            }
            for i in 0...K {
                if curInv[i] > result[i] {
                    result[i] = curInv[i]
                }
            }
        }

        return result
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque
import kotlin.math.max

class Solution {
    fun subtreeInversionSum(edges: Array<IntArray>, nums: IntArray, k: Int): Long {
        val n = nums.size
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
        val stack = ArrayDeque<Int>()
        stack.add(0)
        parent[0] = -2 // mark root visited
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

        val INF = Long.MIN_VALUE / 4
        val dpEven = Array(n) { LongArray(k + 1) { INF } }
        val dpOdd = Array(n) { LongArray(k + 1) { INF } }

        // process in reverse order (post-order)
        for (p in n - 1 downTo 0) {
            val u = order[p]

            // child contributions when they receive even / odd parity
            var childEven = LongArray(k + 1) { if (it == 0) 0L else INF }
            var childOdd = LongArray(k + 1) { if (it == 0) 0L else INF }

            for (v in adj[u]) {
                if (v == parent[u]) continue
                val ce = dpEven[v] // child's result when it receives even parity
                val co = dpOdd[v]   // child's result when it receives odd parity

                // merge into childEven using ce
                val newEven = LongArray(k + 1) { INF }
                var i = 0
                while (i <= k) {
                    val curVal = childEven[i]
                    if (curVal != INF) {
                        var j = 0
                        while (j + i <= k) {
                            val add = ce[j]
                            if (add != INF) {
                                val sum = curVal + add
                                if (sum > newEven[i + j]) newEven[i + j] = sum
                            }
                            j++
                        }
                    }
                    i++
                }

                // merge into childOdd using co
                val newOdd = LongArray(k + 1) { INF }
                i = 0
                while (i <= k) {
                    val curVal = childOdd[i]
                    if (curVal != INF) {
                        var j = 0
                        while (j + i <= k) {
                            val add = co[j]
                            if (add != INF) {
                                val sum = curVal + add
                                if (sum > newOdd[i + j]) newOdd[i + j] = sum
                            }
                            j++
                        }
                    }
                    i++
                }

                childEven = newEven
                childOdd = newOdd
            }

            val baseEven = nums[u].toLong()
            val baseOdd = -baseEven

            val dpE = LongArray(k + 1) { INF }
            val dpO = LongArray(k + 1) { INF }

            var t = 0
            while (t <= k) {
                // no inversion at u
                if (childEven[t] != INF) {
                    val cand = baseEven + childEven[t]
                    if (cand > dpE[t]) dpE[t] = cand
                }
                if (childOdd[t] != INF) {
                    val cand = baseOdd + childOdd[t]
                    if (cand > dpO[t]) dpO[t] = cand
                }

                // inversion at u
                if (t >= 1) {
                    if (childOdd[t - 1] != INF) {
                        val cand = -baseEven + childOdd[t - 1] // -nums[u] + childOdd
                        if (cand > dpE[t]) dpE[t] = cand
                    }
                    if (childEven[t - 1] != INF) {
                        val cand = -baseOdd + childEven[t - 1] // nums[u] + childEven
                        if (cand > dpO[t]) dpO[t] = cand
                    }
                }
                t++
            }

            dpEven[u] = dpE
            dpOdd[u] = dpO
        }

        var answer = Long.MIN_VALUE
        for (t in 0..k) {
            answer = max(answer, dpEven[0][t])
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int subtreeInversionSum(List<List<int>> edges, List<int> nums, int k) {
    int n = nums.length;
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0], v = e[1];
      adj[u].add(v);
      adj[v].add(u);
    }

    // Build parent array and traversal order
    List<int> parent = List.filled(n, -1);
    List<int> order = [];
    List<int> stack = [0];
    parent[0] = -2; // mark root visited
    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      order.add(node);
      for (int nb in adj[node]) {
        if (parent[nb] != -1) continue;
        parent[nb] = node;
        stack.add(nb);
      }
    }

    const int INF_NEG = -9000000000000000000; // sufficiently small
    // dp[node][flip][dist]
    List<List<List<int>>> dp = List.generate(
        n, (_) => List.generate(2, (_) => List.filled(k + 1, INF_NEG)));

    for (int idx = order.length - 1; idx >= 0; --idx) {
      int v = order[idx];
      // gather children list
      List<int> children = [];
      for (int nb in adj[v]) {
        if (parent[nb] == v) children.add(nb);
      }

      for (int flip = 0; flip <= 1; ++flip) {
        for (int dist = 0; dist <= k; ++dist) {
          // Option 1: do not invert at this node
          int nd = (dist == k) ? k : dist + 1;
          int sumChildren = 0;
          bool valid = true;
          for (int ch in children) {
            int val = dp[ch][flip][nd];
            if (val == INF_NEG) { valid = false; break; }
            sumChildren += val;
          }
          int nodeVal = (flip == 0) ? nums[v] : -nums[v];
          int best = valid ? nodeVal + sumChildren : INF_NEG;

          // Option 2: invert at this node if allowed
          if (dist == k) {
            int newFlip = flip ^ 1;
            int sumInvChildren = 0;
            bool invValid = true;
            for (int ch in children) {
              int val = dp[ch][newFlip][1];
              if (val == INF_NEG) { invValid = false; break; }
              sumInvChildren += val;
            }
            int nodeValInv = (newFlip == 0) ? nums[v] : -nums[v];
            if (invValid) {
              int totalInv = nodeValInv + sumInvChildren;
              if (totalInv > best) best = totalInv;
            }
          }

          dp[v][flip][dist] = best;
        }
      }
    }

    return dp[0][0][k];
  }
}
```

## Golang

```go
func subtreeInversionSum(edges [][]int, nums []int, k int) int64 {
	const negInf int64 = -1 << 60
	n := len(nums)

	// build adjacency list
	graph := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}

	// parent and order for post-order traversal
	parent := make([]int, n)
	for i := range parent {
		parent[i] = -2
	}
	order := make([]int, 0, n)

	stack := []int{0}
	parent[0] = -1
	for len(stack) > 0 {
		u := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		order = append(order, u)
		for _, v := range graph[u] {
			if parent[v] == -2 {
				parent[v] = u
				stack = append(stack, v)
			}
		}
	}
	// reverse to get post-order (children before parent)
	for i, j := 0, len(order)-1; i < j; i, j = i+1, j-1 {
		order[i], order[j] = order[j], order[i]
	}

	// dp[node][parity*(k+1)+dist] = max sum
	dp := make([][]int64, n)

	size := 2 * (k + 1)
	for _, u := range order {
		// accumulate contributions from children
		sumNoSel0 := make([]int64, k+1)
		sumNoSel1 := make([]int64, k+1)
		var sumSel0 int64 = 0
		var sumSel1 int64 = 0

		for _, v := range graph[u] {
			if parent[v] != u { // skip parent
				continue
			}
			childDP := dp[v]
			sumSel0 += childDP[0*(k+1)+0]
			sumSel1 += childDP[1*(k+1)+0]

			for d := 0; d <= k; d++ {
				nd := d + 1
				if nd > k {
					nd = k
				}
				sumNoSel0[d] += childDP[0*(k+1)+nd]
				sumNoSel1[d] += childDP[1*(k+1)+nd]
			}
		}

		cur := make([]int64, size)
		val := int64(nums[u])

		for p := 0; p < 2; p++ {
			for d := 0; d <= k; d++ {
				var notSel int64
				if p == 0 {
					notSel = val + sumNoSel0[d]
				} else {
					notSel = -val + sumNoSel1[d]
				}
				best := notSel

				if d == k { // can select here
					newP := p ^ 1
					var sel int64
					if newP == 0 {
						sel = val + sumSel0
					} else {
						sel = -val + sumSel1
					}
					if sel > best {
						best = sel
					}
				}
				cur[p*(k+1)+d] = best
			}
		}
		dp[u] = cur
	}

	// answer: root with no prior inversion, distance allowed = k
	return dp[0][0*(k+1)+k]
}
```

## Ruby

```ruby
def subtree_inversion_sum(edges, nums, k)
  n = nums.size
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  parent = Array.new(n, -1)
  order = []
  stack = [0]
  parent[0] = -2
  while (u = stack.pop)
    order << u
    adj[u].each do |v|
      next if v == parent[u]
      parent[v] = u
      stack << v
    end
  end

  dp = Array.new(n) { [Array.new(k + 1, 0), Array.new(k + 1, 0)] }
  sum_child = Array.new(n) { [Array.new(k + 1, 0), Array.new(k + 1, 0)] }

  order.reverse_each do |u|
    (0..k).each do |t|
      2.times do |p|
        node_val_no = p.zero? ? nums[u] : -nums[u]
        nxt = t < k ? t + 1 : k
        best = node_val_no + sum_child[u][p][nxt]

        if t == k
          node_val_inv = p.zero? ? -nums[u] : nums[u]
          inv_sum = node_val_inv + sum_child[u][p ^ 1][0]
          best = inv_sum if inv_sum > best
        end

        dp[u][p][t] = best
      end
    end

    pu = parent[u]
    next if pu < 0
    2.times do |p|
      (0..k).each do |d|
        sum_child[pu][p][d] += dp[u][p][d]
      end
    end
  end

  dp[0][0][k]
end
```

## Scala

```scala
object Solution {
  def subtreeInversionSum(edges: Array[Array[Int]], nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      adj(u).append(v)
      adj(v).append(u)
    }

    // Build parent array and postorder
    val parent = Array.fill(n)(-2)
    val order = new scala.collection.mutable.ArrayBuffer[Int]()
    val stack = new scala.collection.mutable.Stack[Int]()
    stack.push(0)
    parent(0) = -1
    while (stack.nonEmpty) {
      val u = stack.pop()
      order.append(u)
      for (v <- adj(u)) {
        if (parent(v) == -2) {
          parent(v) = u
          stack.push(v)
        }
      }
    }

    val K = k
    val NEG: Long = Long.MinValue / 4

    // dp0[u][c] : max sum for subtree u when incoming parity is 0 (no flip from ancestors)
    // dp1[u][c] : same when incoming parity is 1 (flipped from ancestors)
    val dp0 = Array.ofDim[Long](n, K + 1)
    val dp1 = Array.ofDim[Long](n, K + 1)

    for (idx <- order.reverse) {
      // initialize arrays
      var cur0 = Array.fill(K + 1)(NEG)
      var cur1 = Array.fill(K + 1)(NEG)
      var inv0 = Array.fill(K + 1)(NEG)
      var inv1 = Array.fill(K + 1)(NEG)

      cur0(0) = nums(idx).toLong          // parity 0, no inversion at this node
      cur1(0) = -nums(idx).toLong         // parity 1, no inversion at this node

      if (K >= 1) {
        inv0(1) = -nums(idx).toLong       // invert here: flips parity to 1
        inv1(1) = nums(idx).toLong        // invert here: flips parity to 0
      }

      for (v <- adj(idx) if parent(v) == idx) {
        // merge child v into the four scenarios
        def merge(a: Array[Long], b: Array[Long]): Array[Long] = {
          val res = Array.fill(K + 1)(NEG)
          var i = 0
          while (i <= K) {
            if (a(i) > NEG / 2) {
              var j = 0
              val limit = K - i
              while (j <= limit) {
                if (b(j) > NEG / 2) {
                  val cand = a(i) + b(j)
                  if (cand > res(i + j)) res(i + j) = cand
                }
                j += 1
              }
            }
            i += 1
          }
          res
        }

        // cur0 uses child's dp0 (parity unchanged)
        cur0 = merge(cur0, dp0(v))
        // cur1 uses child's dp1
        cur1 = merge(cur1, dp1(v))
        // inv0 (node inverted) children see parity 1 -> use dp1
        inv0 = merge(inv0, dp1(v))
        // inv1 (node inverted) children see parity 0 -> use dp0
        inv1 = merge(inv1, dp0(v))
      }

      var c = 0
      while (c <= K) {
        val best0 = if (cur0(c) > inv0(c)) cur0(c) else inv0(c)
        val best1 = if (cur1(c) > inv1(c)) cur1(c) else inv1(c)
        dp0(idx)(c) = best0
        dp1(idx)(c) = best1
        c += 1
      }
    }

    var ans: Long = NEG
    var i = 0
    while (i <= K) {
      if (dp0(0)(i) > ans) ans = dp0(0)(i)
      i += 1
    }
    ans
  }
}
```

## Rust

```rust
use std::cmp::max;

impl Solution {
    pub fn subtree_inversion_sum(edges: Vec<Vec<i32>>, nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let k_usize = k as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }

        // build parent array and order (post-order)
        let mut parent: Vec<usize> = vec![usize::MAX; n];
        let mut order: Vec<usize> = Vec::with_capacity(n);
        let mut stack: Vec<usize> = vec![0];
        parent[0] = 0;
        while let Some(u) = stack.pop() {
            order.push(u);
            for &v in adj[u].iter() {
                if v == parent[u] { continue; }
                parent[v] = u;
                stack.push(v);
            }
        }

        const INF: i64 = -9_000_000_000_000_000_000;

        let mut dp_even: Vec<Vec<i64>> = vec![vec![INF; k_usize + 1]; n];
        let mut dp_odd: Vec<Vec<i64>> = vec![vec![INF; k_usize + 1]; n];

        // process in reverse order (post-order)
        for &u in order.iter().rev() {
            // base without inversion at u
            let mut cur_even = vec![INF; k_usize + 1];
            let mut cur_odd = vec![INF; k_usize + 1];
            cur_even[0] = nums[u] as i64;
            cur_odd[0] = -(nums[u] as i64);

            // merge children for the "no inversion at u" case
            for &v in adj[u].iter() {
                if v == parent[u] { continue; }
                let child_even = &dp_even[v];
                let child_odd = &dp_odd[v];

                // merge into cur_even using child's even (parity unchanged)
                let mut nxt = vec![INF; k_usize + 1];
                for i in 0..=k_usize {
                    if cur_even[i] == INF { continue; }
                    for j in 0..=k_usize - i {
                        if child_even[j] == INF { continue; }
                        let val = cur_even[i] + child_even[j];
                        if val > nxt[i + j] { nxt[i + j] = val; }
                    }
                }
                cur_even = nxt;

                // merge into cur_odd using child's odd
                let mut nxt2 = vec![INF; k_usize + 1];
                for i in 0..=k_usize {
                    if cur_odd[i] == INF { continue; }
                    for j in 0..=k_usize - i {
                        if child_odd[j] == INF { continue; }
                        let val = cur_odd[i] + child_odd[j];
                        if val > nxt2[i + j] { nxt2[i + j] = val; }
                    }
                }
                cur_odd = nxt2;
            }

            // case with inversion at u (uses one operation)
            let mut inv_even = vec![INF; k_usize + 1]; // parent parity even, after inversion node value is -nums[u]
            let mut inv_odd = vec![INF; k_usize + 1];  // parent parity odd, after inversion node value is +nums[u]

            if k_usize >= 1 {
                inv_even[1] = -(nums[u] as i64);
                inv_odd[1] = nums[u] as i64;
            }

            for &v in adj[u].iter() {
                if v == parent[u] { continue; }
                let child_even = &dp_even[v];
                let child_odd = &dp_odd[v];

                // inv_even merges with child's odd (parity toggled)
                let mut nxt = vec![INF; k_usize + 1];
                for i in 0..=k_usize {
                    if inv_even[i] == INF { continue; }
                    for j in 0..=k_usize - i {
                        if child_odd[j] == INF { continue; }
                        let val = inv_even[i] + child_odd[j];
                        if val > nxt[i + j] { nxt[i + j] = val; }
                    }
                }
                inv_even = nxt;

                // inv_odd merges with child's even
                let mut nxt2 = vec![INF; k_usize + 1];
                for i in 0..=k_usize {
                    if inv_odd[i] == INF { continue; }
                    for j in 0..=k_usize - i {
                        if child_even[j] == INF { continue; }
                        let val = inv_odd[i] + child_even[j];
                        if val > nxt2[i + j] { nxt2[i + j] = val; }
                    }
                }
                inv_odd = nxt2;
            }

            // take maximum between not-inverted and inverted cases
            for t in 0..=k_usize {
                dp_even[u][t] = max(cur_even[t], inv_even[t]);
                dp_odd[u][t] = max(cur_odd[t], inv_odd[t]);
            }
        }

        // answer is best value at root with even parity (no ancestor inversions)
        let mut ans = INF;
        for t in 0..=k_usize {
            if dp_even[0][t] > ans { ans = dp_even[0][t]; }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (subtree-inversion-sum edges nums k)
  (-> (listof (listof exact-integer?))
      (listof exact-integer?)
      exact-integer?
      exact-integer?)
  (let* ((n (vector-length (list->vector nums)))
         (adj (let ((v (make-vector n '())))
                (for ([e edges])
                  (define u (first e))
                  (define w (second e))
                  (vector-set! v u (cons w (vector-ref v u)))
                  (vector-set! v w (cons u (vector-ref v w))))
                v))
         (num-vec (list->vector nums))
         (parent (make-vector n -1))
         ;; preorder traversal
         (preorder
          (let loop ((stack (list (cons 0 -1))) (out '()))
            (if (null? stack)
                (reverse out) ; will be processed in reverse for post‑order
                (let* ((pair (car stack))
                       (node (car pair))
                       (par (cdr pair))
                       (rest (cdr stack)))
                  (vector-set! parent node par)
                  (for ([nbr (in-list (vector-ref adj node))])
                    (when (not (= nbr par))
                      (set! rest (cons (cons nbr node) rest))))
                  (loop rest (cons node out))))))

         (dp-even (make-vector n #f))
         (dp-odd  (make-vector n #f))
         (neg-inf -1000000000000000)) ; sufficiently small

    ;; process nodes in post‑order
    (for ([u (in-list preorder)])
      (let* ((sum-even (make-vector (add1 k) 0))
             (sum-odd  (make-vector (add1 k) 0)))
        ;; accumulate children's dp
        (for ([v (in-list (vector-ref adj u))])
          (when (= (vector-ref parent v) u)
            (define ce (vector-ref dp-even v))
            (define co (vector-ref dp-odd v))
            (for ([d (in-range (add1 k))])
              (vector-set! sum-even d (+ (vector-ref sum-even d) (vector-ref ce d)))
              (vector-set! sum-odd  d (+ (vector-get sum-odd d)   (vector-ref co d))))))

        ;; compute dp for u
        (define res-even (make-vector (add1 k) 0))
        (define res-odd  (make-vector (add1 k) 0))
        (for ([d (in-range (add1 k))])
          (let* ((next (if (= d k) k (+ d 1))) ; min(d+1,k)
                 ;; parity even
                 (notInv-even (+ (vector-ref num-vec u)
                                 (vector-ref sum-even next)))
                 (inv-even (if (= d k)
                               (+ (- (vector-ref num-vec u))
                                  (vector-ref sum-odd 0))
                               neg-inf))
                 (best-even (max notInv-even inv-even))
                 ;; parity odd
                 (notInv-odd (+ (- (vector-ref num-vec u))
                                 (vector-ref sum-odd next)))
                 (inv-odd (if (= d k)
                              (+ (vector-ref num-vec u)
                                 (vector-ref sum-even 0))
                              neg-inf))
                 (best-odd (max notInv-odd inv-odd)))
            (vector-set! res-even d best-even)
            (vector-set! res-odd  d best-odd)))

        (vector-set! dp-even u res-even)
        (vector-set! dp-odd  u res-odd)))

    ;; answer: root with even parity and distance k
    (vector-ref (vector-ref dp-even 0) k)))
```

## Erlang

```erlang
-spec subtree_inversion_sum(Edges :: [[integer()]], Nums :: [integer()], K :: integer()) -> integer().
subtree_inversion_sum(Edges, Nums, K) ->
    Adj = build_adj(Edges, #{}),
    {RootDP, _} = dfs(0, -1, Adj, Nums, K),
    OrigSum = lists:sum(Nums),
    MaxGain = max_gain(RootDP, K),
    OrigSum + MaxGain.

build_adj([], Adj) -> Adj;
build_adj([[U,V]|Rest], Adj) ->
    Adj1 = maps:update_with(U,
            fun(L) -> [V|L] end,
            [V],
            Adj),
    Adj2 = maps:update_with(V,
            fun(L) -> [U|L] end,
            [U],
            Adj1),
    build_adj(Rest, Adj2).

dfs(Node, Parent, Adj, Nums, K) ->
    Children = [C || C <- maps:get(Node, Adj, []), C =/= Parent],
    InitDP = #{0 => {0, -1000000000000}},
    DPChildren = lists:foldl(
        fun(Child, AccDP) ->
            {ChildDP, _} = dfs(Child, Node, Adj, Nums, K),
            merge_maps(AccDP, ChildDP, K)
        end,
        InitDP,
        Children),
    Value = lists:nth(Node + 1, Nums),
    FinalDP = incorporate_self(DPChildren, Value, K),
    {FinalDP, ok}.

merge_maps(DP1, DP2, K) ->
    NegInf = -1000000000000,
    maps:fold(
        fun(Used1, {G0, G1}, Acc) ->
            maps:fold(
                fun(Used2, {C0, C1}, AccInner) ->
                    Total = Used1 + Used2,
                    if
                        Total =< K ->
                            Prev = maps:get(Total, AccInner, {NegInf, NegInf}),
                            NewEven = erlang:max(element(1, Prev), erlang:max(G0 + C0, G1 + C1)),
                            NewOdd  = erlang:max(element(2, Prev), erlang:max(G0 + C1, G1 + C0)),
                            maps:put(Total, {NewEven, NewOdd}, AccInner);
                        true ->
                            AccInner
                    end
                end,
                Acc,
                DP2)
        end,
        #{},
        DP1).

incorporate_self(DPChildren, Val, K) ->
    NegInf = -1000000000000,
    FlipGain = -2 * Val,
    maps:fold(
        fun(Used, {EvenGain, OddGain}, Acc) ->
            % not select current node
            GainEvenNoSel = EvenGain,
            GainOddNoSel  = OddGain + FlipGain,
            Acc1 = set_max(Acc, Used, GainEvenNoSel, GainOddNoSel),
            % select current node if possible
            case Used + 1 =< K of
                true ->
                    GainEvenSel = EvenGain + FlipGain,
                    GainOddSel  = OddGain,
                    set_max(Acc1, Used + 1, GainEvenSel, GainOddSel);
                false -> Acc1
            end
        end,
        #{},
        DPChildren).

set_max(Map, Used, NewEven, NewOdd) ->
    case maps:find(Used, Map) of
        error ->
            maps:put(Used, {NewEven, NewOdd}, Map);
        {ok, {OldEven, OldOdd}} ->
            Updated = {erlang:max(OldEven, NewEven), erlang:max(OldOdd, NewOdd)},
            maps:put(Used, Updated, Map)
    end.

max_gain(DP, K) ->
    NegInf = -1000000000000,
    maps:fold(
        fun(_Used, {E, O}, Acc) ->
            erlang:max(Acc, erlang:max(E, O))
        end,
        0,
        DP).
```

## Elixir

```elixir
defmodule Solution do
  @spec subtree_inversion_sum(edges :: [[integer]], nums :: [integer], k :: integer) :: integer
  def subtree_inversion_sum(edges, nums, k) do
    n = length(nums)

    # build adjacency using :array for O(1) updates
    adj0 = :array.new(n, default: [])
    {adj, _} =
      Enum.reduce(edges, {adj0, nil}, fn [u, v], {a, _} ->
        a1 = update_adj(a, u, v)
        a2 = update_adj(a1, v, u)
        {a2, nil}
      end)

    # build parent array and postorder traversal
    {postorder, parent_arr} = build_postorder(0, adj, n)

    dp0_arr = :array.new(n)
    dp1_arr = :array.new(n)

    # process nodes bottom‑up
    Enum.each(postorder, fn node ->
      children =
        (:array.get(node, adj))
        |> Enum.filter(fn nb -> :array.get(nb, parent_arr) == node end)

      child_data =
        Enum.map(children, fn ch ->
          { :array.get(ch, dp0_arr), :array.get(ch, dp1_arr) }
        end)

      val = Enum.at(nums, node)

      # parity 0 (even number of ancestor inversions)
      dp0_list =
        for c <- 0..k do
          base = val
          sum_no =
            Enum.reduce(child_data, 0, fn {dp0_child, _}, acc ->
              idx = if c > 0, do: c - 1, else: 0
              acc + elem(dp0_child, idx)
            end)

          best = base + sum_no

          # inversion allowed only when cooldown is zero
          if c == 0 do
            inv_base = -base
            sum_inv =
              Enum.reduce(child_data, 0, fn {_, dp1_child}, acc ->
                acc + elem(dp1_child, k - 1)
              end)

            max(best, inv_base + sum_inv)
          else
            best
          end
        end

      # parity 1 (odd number of ancestor inversions)
      dp1_list =
        for c <- 0..k do
          base = -val
          sum_no =
            Enum.reduce(child_data, 0, fn {_, dp1_child}, acc ->
              idx = if c > 0, do: c - 1, else: 0
              acc + elem(dp1_child, idx)
            end)

          best = base + sum_no

          if c == 0 do
            inv_base = -base
            sum_inv =
              Enum.reduce(child_data, 0, fn {dp0_child, _}, acc ->
                acc + elem(dp0_child, k - 1)
              end)

            max(best, inv_base + sum_inv)
          else
            best
          end
        end

      dp0_arr = :array.set(node, List.to_tuple(dp0_list), dp0_arr)
      dp1_arr = :array.set(node, List.to_tuple(dp1_list), dp1_arr)
    end)

    # answer: root with even parity and cooldown 0 (no restriction initially)
    root_dp0 = :array.get(0, dp0_arr)
    elem(root_dp0, 0)
  end

  defp update_adj(arr, u, v) do
    list = :array.get(u, arr)
    :array.set(u, [v | list], arr)
  end

  # builds parent array and returns nodes in postorder (children before parent)
  defp build_postorder(root, adj, n) do
    parent_arr = :array.new(n, default: -1)

    {post_rev, parent_arr} =
      dfs_stack([root], [], parent_arr, adj)

    {Enum.reverse(post_rev), parent_arr}
  end

  defp dfs_stack([], post_rev, parent_arr, _adj), do: {post_rev, parent_arr}

  defp dfs_stack([node | stack], post_rev, parent_arr, adj) do
    post_rev = [node | post_rev]

    neighbors = :array.get(node, adj)

    {parent_arr, new_stack} =
      Enum.reduce(neighbors, {parent_arr, stack}, fn nb, {par_acc, stk_acc} ->
        if :array.get(nb, par_acc) == -1 do
          par_acc = :array.set(nb, node, par_acc)
          {par_acc, [nb | stk_acc]}
        else
          {par_acc, stk_acc}
        end
      end)

    dfs_stack(new_stack, post_rev, parent_arr, adj)
  end
end
```

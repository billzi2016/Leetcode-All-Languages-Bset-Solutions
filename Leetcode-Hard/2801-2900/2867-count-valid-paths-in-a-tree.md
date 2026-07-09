# 2867. Count Valid Paths in a Tree

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long countPaths(int n, vector<vector<int>>& edges) {
        // build graph
        vector<vector<int>> g(n + 1);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            g[u].push_back(v);
            g[v].push_back(u);
        }
        // sieve primes up to n
        vector<char> isPrime(n + 1, true);
        if (n >= 0) isPrime[0] = false;
        if (n >= 1) isPrime[1] = false;
        for (int i = 2; i * 1LL * i <= n; ++i) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i)
                    isPrime[j] = false;
            }
        }
        // parent and order (iterative DFS)
        vector<int> parent(n + 1, -1), order;
        order.reserve(n);
        stack<int> st;
        st.push(1);
        parent[1] = 0;
        while (!st.empty()) {
            int u = st.top(); st.pop();
            order.push_back(u);
            for (int v : g[u]) if (parent[v] == -1) {
                parent[v] = u;
                st.push(v);
            }
        }
        // dp arrays
        vector<long long> dp0(n + 1, 0), dp1(n + 1, 0);
        for (int idx = n - 1; idx >= 0; --idx) {
            int u = order[idx];
            long long sum0 = 0, sum1 = 0;
            for (int v : g[u]) if (parent[v] == u) {
                sum0 += dp0[v];
                sum1 += dp1[v];
            }
            if (isPrime[u]) {
                dp0[u] = 0;
                dp1[u] = 1 + sum0; // path consisting only of u
            } else {
                dp0[u] = 1 + sum0; // single node path without prime
                dp1[u] = sum1;
            }
        }
        long long ans = 0;
        for (int u = 1; u <= n; ++u) {
            bool prime = isPrime[u];
            long long totalZero = 0, totalOne = 0;
            for (int v : g[u]) if (parent[v] == u) {
                totalZero += dp0[v];
                totalOne  += dp1[v];
            }
            if (prime) {
                // paths where one endpoint is u
                ans += totalZero;
                // pairs from different subtrees, both zero-prime paths
                long long cross = totalZero * totalZero;
                for (int v : g[u]) if (parent[v] == u) {
                    cross -= dp0[v] * dp0[v];
                }
                ans += cross / 2;
            } else {
                // paths where one endpoint is u
                ans += totalOne;
                // pairs from different subtrees, one zero and one one-prime path
                long long cross = totalZero * totalOne;
                for (int v : g[u]) if (parent[v] == u) {
                    cross -= dp0[v] * dp1[v];
                }
                ans += cross / 2;
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long countPaths(int n, int[][] edges) {
        boolean[] isPrime = sievePrimes(n);
        List<Integer>[] g = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            g[u].add(v);
            g[v].add(u);
        }
        long[] cnt0 = new long[n + 1];
        long[] cnt1 = new long[n + 1];
        long[] ans = new long[1]; // use array to modify inside lambda

        dfs(1, 0, g, isPrime, cnt0, cnt1, ans);

        return ans[0];
    }

    private void dfs(int u, int parent, List<Integer>[] g, boolean[] isPrime,
                     long[] cnt0, long[] cnt1, long[] ans) {
        long totalZero = 0;
        long totalOne = 0;

        for (int v : g[u]) {
            if (v == parent) continue;
            dfs(v, u, g, isPrime, cnt0, cnt1, ans);

            long childZero, childOne;
            if (!isPrime[u]) {
                childZero = cnt0[v];
                childOne = cnt1[v];
                // cross contributions for non‑prime LCA
                ans[0] += childZero * totalOne + childOne * totalZero;
            } else {
                childZero = 0;
                childOne = cnt0[v]; // only the prime at u counted
                // cross contributions for prime LCA
                ans[0] += childOne * totalOne;
            }

            totalZero += childZero;
            totalOne += childOne;
        }

        if (!isPrime[u]) {
            long sumZero = 1; // node u itself contributes zero primes
            long sumOne = 0;
            for (int v : g[u]) {
                if (v == parent) continue;
                sumZero += cnt0[v];
                sumOne += cnt1[v];
            }
            cnt0[u] = sumZero;
            cnt1[u] = sumOne;
        } else {
            long sumZero = 0;
            long sumOne = 1; // path consisting only of u
            for (int v : g[u]) {
                if (v == parent) continue;
                sumZero += cnt0[v];
                sumOne += cnt0[v];
            }
            cnt0[u] = sumZero;
            cnt1[u] = sumOne;
        }

        // pairs where one endpoint is u itself
        ans[0] += cnt1[u] - (isPrime[u] ? 1 : 0);
    }

    private boolean[] sievePrimes(int n) {
        boolean[] prime = new boolean[n + 1];
        Arrays.fill(prime, true);
        if (n >= 0) prime[0] = false;
        if (n >= 1) prime[1] = false;
        for (int i = 2; i * i <= n; i++) {
            if (prime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    prime[j] = false;
                }
            }
        }
        return prime;
    }
}
```

## Python

```python
class Solution(object):
    def countPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(300000)

        # sieve for primes up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                step = p
                start = p * p
                for i in range(start, n + 1, step):
                    is_prime[i] = False
            p += 1

        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = 0

        def dfs(u, parent):
            nonlocal ans
            if is_prime[u]:
                dp0 = 0          # paths from u with 0 primes (impossible)
                dp1 = 1          # the node itself counts as exactly one prime
            else:
                dp0 = 1          # the node itself has 0 primes on its path
                dp1 = 0

            total_zero = 0   # accumulated zero-counts from processed children
            total_one = 0    # accumulated one-counts from processed children

            for v in adj[u]:
                if v == parent:
                    continue
                child_dp0, child_dp1 = dfs(v, u)

                zero_c = child_dp0   # nodes in child's subtree with 0 primes on path u->node
                one_c = child_dp1    # nodes in child's subtree with exactly 1 prime on that path

                if is_prime[u]:
                    # need p_a + p_b = 2 (both sides must have 1)
                    ans += one_c * total_one
                else:
                    # need p_a + p_b = 1 (one side 0, other 1)
                    ans += zero_c * total_one + one_c * total_zero

                total_zero += zero_c
                total_one += one_c

                if is_prime[u]:
                    dp1 += child_dp0   # paths where only u contributes the prime
                else:
                    dp0 += child_dp0
                    dp1 += child_dp1

            # pairs where one endpoint is u itself
            if is_prime[u]:
                ans += dp1 - 1   # exclude (u,u)
            else:
                ans += dp1

            return dp0, dp1

        dfs(1, 0)
        return ans
```

## Python3

```python
import sys
from typing import List

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        sys.setrecursionlimit(200000)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # sieve for primes up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                step = i
                start = i * i
                for j in range(start, n + 1, step):
                    is_prime[j] = False

        dp0 = [0] * (n + 1)   # paths from node with 0 primes
        dp1 = [0] * (n + 1)   # paths from node with exactly 1 prime
        ans = 0

        def dfs(u: int, p: int):
            nonlocal ans
            child_vals = []          # list of (c0, c1) for each child
            total0 = total1 = 0

            for v in adj[u]:
                if v == p:
                    continue
                dfs(v, u)
                c0, c1 = dp0[v], dp1[v]
                child_vals.append((c0, c1))
                total0 += c0
                total1 += c1

            if is_prime[u]:
                dp0[u] = 0
                dp1[u] = 1 + total0   # node itself counts as one prime path
                # pairs where LCA is u and one endpoint is u
                ans += total0
                # pairs across different child subtrees, both sides need zero primes
                cum = 0
                for c0, _ in child_vals:
                    ans += cum * c0
                    cum += c0
            else:
                dp0[u] = 1 + total0    # node itself contributes a zero‑prime path
                dp1[u] = total1
                # pairs where LCA is u and one endpoint is u
                ans += total1
                # cross child pairs: one side zero primes, other side one prime
                cum0 = cum1 = 0
                for c0, c1 in child_vals:
                    ans += cum0 * c1 + cum1 * c0
                    cum0 += c0
                    cum1 += c1

        dfs(1, 0)
        return ans
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

typedef struct {
    int to;
    int next;
} Edge;

long long countPaths(int n, int** edges, int edgesSize, int* edgesColSize) {
    // Build adjacency list
    int m = edgesSize * 2;
    Edge *e = (Edge *)malloc(sizeof(Edge) * m);
    int *head = (int *)malloc(sizeof(int) * (n + 1));
    for (int i = 1; i <= n; ++i) head[i] = -1;
    int idx = 0;
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        e[idx].to = v;
        e[idx].next = head[u];
        head[u] = idx++;
        e[idx].to = u;
        e[idx].next = head[v];
        head[v] = idx++;
    }

    // Sieve for primes up to n
    bool *isPrime = (bool *)malloc(sizeof(bool) * (n + 1));
    for (int i = 0; i <= n; ++i) isPrime[i] = true;
    if (n >= 0) isPrime[0] = false;
    if (n >= 1) isPrime[1] = false;
    int limit = (int)sqrt((double)n);
    for (int p = 2; p <= limit; ++p) {
        if (isPrime[p]) {
            for (int mult = p * p; mult <= n; mult += p)
                isPrime[mult] = false;
        }
    }

    // Parent array and order for post-order traversal
    int *parent = (int *)malloc(sizeof(int) * (n + 1));
    int *order = (int *)malloc(sizeof(int) * n);
    int *stack = (int *)malloc(sizeof(int) * n);
    int top = 0, ordCnt = 0;
    stack[top++] = 1;
    parent[1] = 0;
    while (top) {
        int u = stack[--top];
        order[ordCnt++] = u;
        for (int ei = head[u]; ei != -1; ei = e[ei].next) {
            int v = e[ei].to;
            if (v == parent[u]) continue;
            parent[v] = u;
            stack[top++] = v;
        }
    }

    // DP arrays
    long long *dp0 = (long long *)calloc(n + 1, sizeof(long long));
    long long *dp1 = (long long *)calloc(n + 1, sizeof(long long));

    for (int i = n - 1; i >= 0; --i) {
        int u = order[i];
        if (isPrime[u]) {
            long long sum0 = 0;
            for (int ei = head[u]; ei != -1; ei = e[ei].next) {
                int v = e[ei].to;
                if (v == parent[u]) continue;
                sum0 += dp0[v];
            }
            dp0[u] = 0;
            dp1[u] = 1 + sum0; // node itself plus zero‑prime paths from children
        } else {
            long long sum0 = 0, sum1 = 0;
            for (int ei = head[u]; ei != -1; ei = e[ei].next) {
                int v = e[ei].to;
                if (v == parent[u]) continue;
                sum0 += dp0[v];
                sum1 += dp1[v];
            }
            dp0[u] = 1 + sum0; // node itself counts as zero‑prime path
            dp1[u] = sum1;
        }
    }

    long long ans = 0;
    for (int u = 1; u <= n; ++u) {
        long long total0 = 0, total1 = 0;
        for (int ei = head[u]; ei != -1; ei = e[ei].next) {
            int v = e[ei].to;
            if (v == parent[u]) continue;
            total0 += dp0[v];
            total1 += dp1[v];
        }
        if (isPrime[u]) {
            // pairs (u, node) where node lies in a zero‑prime subtree
            ans += total0;
            // pairs across two different child subtrees
            long long sumSq = 0;
            for (int ei = head[u]; ei != -1; ei = e[ei].next) {
                int v = e[ei].to;
                if (v == parent[u]) continue;
                long long sz = dp0[v];
                sumSq += sz * sz;
            }
            ans += (total0 * total0 - sumSq) / 2;
        } else {
            // pairs (u, node) where path contains exactly one prime
            ans += total1;
            // cross pairs: one side with exactly one prime, other side with zero primes
            for (int ei = head[u]; ei != -1; ei = e[ei].next) {
                int v = e[ei].to;
                if (v == parent[u]) continue;
                long long sz0 = dp0[v];
                long long sz1 = dp1[v];
                ans += sz1 * (total0 - sz0);
            }
        }
    }

    free(e);
    free(head);
    free(isPrime);
    free(parent);
    free(order);
    free(stack);
    free(dp0);
    free(dp1);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long CountPaths(int n, int[][] edges) {
        // Build graph
        List<int>[] g = new List<int>[n + 1];
        for (int i = 1; i <= n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            g[u].Add(v);
            g[v].Add(u);
        }

        // Sieve for primes up to n
        bool[] isPrime = new bool[n + 1];
        if (n >= 2) {
            for (int i = 2; i <= n; i++) isPrime[i] = true;
            for (int p = 2; p * p <= n; p++) {
                if (isPrime[p]) {
                    for (int mult = p * p; mult <= n; mult += p)
                        isPrime[mult] = false;
                }
            }
        }

        // Root the tree at 1, get parent and order
        int[] parent = new int[n + 1];
        List<int> order = new List<int>(n);
        Stack<int> stack = new Stack<int>();
        stack.Push(1);
        parent[1] = 0;
        while (stack.Count > 0) {
            int node = stack.Pop();
            order.Add(node);
            foreach (int nb in g[node]) {
                if (nb == parent[node]) continue;
                parent[nb] = node;
                stack.Push(nb);
            }
        }

        // DP arrays
        long[] dp0 = new long[n + 1]; // zero primes on path starting at node
        long[] dp1 = new long[n + 1]; // exactly one prime

        for (int idx = order.Count - 1; idx >= 0; idx--) {
            int v = order[idx];
            bool prime = isPrime[v];
            long sum0 = 0, sum1 = 0;
            foreach (int nb in g[v]) {
                if (parent[nb] == v) { // child
                    sum0 += dp0[nb];
                    sum1 += dp1[nb];
                }
            }
            if (prime) {
                dp0[v] = 0;
                dp1[v] = 1 + sum0; // path consisting only of v plus extensions with zero primes below
            } else {
                dp0[v] = 1 + sum0; // path consisting only of v plus extensions with zero primes below
                dp1[v] = sum1;
            }
        }

        long ans = 0;
        for (int v = 1; v <= n; v++) {
            bool prime = isPrime[v];
            // contributions where one endpoint is v
            foreach (int nb in g[v]) {
                if (parent[nb] == v) { // child
                    ans += prime ? dp0[nb] : dp1[nb];
                }
            }

            // contributions between different subtrees
            long cum0 = 0, cum1 = 0;
            foreach (int nb in g[v]) {
                if (parent[nb] != v) continue; // only children
                if (prime) {
                    ans += dp0[nb] * cum0;
                    cum0 += dp0[nb];
                } else {
                    ans += dp1[nb] * cum0;
                    ans += dp0[nb] * cum1;
                    cum0 += dp0[nb];
                    cum1 += dp1[nb];
                }
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
 * @return {number}
 */
var countPaths = function(n, edges) {
    // sieve of Eratosthenes for primes up to n
    const isPrime = new Array(n + 1).fill(true);
    isPrime[0] = isPrime[1] = false;
    for (let i = 2; i * i <= n; ++i) {
        if (isPrime[i]) {
            for (let j = i * i; j <= n; j += i) isPrime[j] = false;
        }
    }

    // build adjacency list
    const adj = Array.from({length: n + 1}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    // iterative DFS to get parent and order
    const parent = new Array(n + 1).fill(0);
    const order = [];
    const stack = [1];
    parent[1] = -1;
    while (stack.length) {
        const u = stack.pop();
        order.push(u);
        for (const v of adj[u]) {
            if (v !== parent[u]) {
                parent[v] = u;
                stack.push(v);
            }
        }
    }

    // dp0: paths from node downwards with 0 primes, dp1: with exactly 1 prime
    const dp0 = new Array(n + 1).fill(0);
    const dp1 = new Array(n + 1).fill(0);

    for (let i = order.length - 1; i >= 0; --i) {
        const u = order[i];
        if (isPrime[u]) {
            dp0[u] = 0;
            dp1[u] = 1; // the node itself
        } else {
            dp0[u] = 1; // just the node
            dp1[u] = 0;
        }
        for (const v of adj[u]) {
            if (parent[v] === u) { // child
                if (isPrime[u]) {
                    dp1[u] += dp0[v];
                } else {
                    dp0[u] += dp0[v];
                    dp1[u] += dp1[v];
                }
            }
        }
    }

    let ans = 0;
    for (let u = 1; u <= n; ++u) {
        let totalZero = 0;
        let totalOne = 0;
        let sameZeroOne = 0;          // sum of cnt0*cnt1 within same child (non‑prime case)
        let sameOneChoose2 = 0;       // sum of C(cnt1,2) within same child (prime case)

        for (const v of adj[u]) {
            if (parent[v] !== u) continue; // only children
            let c0, c1;
            if (isPrime[u]) {
                c0 = 0;
                c1 = dp0[v];   // paths where the only prime is u itself
            } else {
                c0 = dp0[v];
                c1 = dp1[v];
            }
            totalZero += c0;
            totalOne += c1;

            if (!isPrime[u]) {
                sameZeroOne += c0 * c1;
            } else {
                sameOneChoose2 += c1 * (c1 - 1) / 2;
            }
        }

        // pairs where one endpoint is u
        ans += totalOne;

        // cross‑subtree pairs
        if (!isPrime[u]) {
            ans += totalZero * totalOne - sameZeroOne;
        } else {
            ans += (totalOne * (totalOne - 1) / 2) - sameOneChoose2;
        }
    }

    return ans;
};
```

## Typescript

```typescript
function countPaths(n: number, edges: number[][]): number {
    const adj: number[][] = Array.from({ length: n + 1 }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    // sieve primes up to n
    const isPrime = new Uint8Array(n + 1);
    if (n >= 2) {
        const prime = new Uint8Array(n + 1);
        for (let i = 2; i <= n; i++) prime[i] = 1;
        for (let p = 2; p * p <= n; p++) {
            if (prime[p]) {
                for (let m = p * p; m <= n; m += p) prime[m] = 0;
            }
        }
        for (let i = 2; i <= n; i++) if (prime[i]) isPrime[i] = 1;
    }

    const dpZero: number[] = new Array(n + 1);
    const dpOne: number[] = new Array(n + 1);
    const parent = new Int32Array(n + 1);
    const order: number[] = [];

    // iterative DFS to get order and parents
    const stack: number[] = [1];
    parent[1] = 0;
    while (stack.length) {
        const u = stack.pop()!;
        order.push(u);
        for (const v of adj[u]) {
            if (v === parent[u]) continue;
            parent[v] = u;
            stack.push(v);
        }
    }

    // post-order DP
    for (let i = order.length - 1; i >= 0; i--) {
        const u = order[i];
        let zero = isPrime[u] ? 0 : 1;
        let one = isPrime[u] ? 1 : 0;
        for (const v of adj[u]) {
            if (v === parent[u]) continue;
            if (isPrime[u]) {
                one += dpZero[v];
            } else {
                zero += dpZero[v];
                one += dpOne[v];
            }
        }
        dpZero[u] = zero;
        dpOne[u] = one;
    }

    let ans = 0;

    // count contributions per node as LCA
    for (let u = 1; u <= n; u++) {
        const primeU = isPrime[u] === 1;

        // pairs where one endpoint is u
        if (primeU) {
            for (const v of adj[u]) {
                if (v === parent[u]) continue;
                ans += dpZero[v];
            }
        } else {
            for (const v of adj[u]) {
                if (v === parent[u]) continue;
                ans += dpOne[v];
            }
        }

        // pairs across different child subtrees
        let totalZero = 0;
        let totalOne = 0;
        for (const v of adj[u]) {
            if (v === parent[u]) continue;
            const zeroC = dpZero[v];
            const oneC = dpOne[v];
            if (primeU) {
                ans += zeroC * totalZero;
            } else {
                ans += zeroC * totalOne + oneC * totalZero;
            }
            totalZero += zeroC;
            totalOne += oneC;
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
     * @return Integer
     */
    function countPaths($n, $edges) {
        // build graph
        $graph = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $graph[$u][] = $v;
            $graph[$v][] = $u;
        }

        // sieve for primes up to n
        $isPrime = array_fill(0, $n + 1, true);
        $isPrime[0] = $isPrime[1] = false;
        $limit = (int)sqrt($n);
        for ($i = 2; $i <= $limit; $i++) {
            if ($isPrime[$i]) {
                for ($j = $i * $i; $j <= $n; $j += $i) {
                    $isPrime[$j] = false;
                }
            }
        }

        // iterative DFS to get parent and order
        $parent = array_fill(0, $n + 1, 0);
        $order = [];
        $stack = [1];
        $parent[1] = -1; // root marker
        while ($stack) {
            $u = array_pop($stack);
            $order[] = $u;
            foreach ($graph[$u] as $v) {
                if ($v === $parent[$u]) continue;
                $parent[$v] = $u;
                $stack[] = $v;
            }
        }

        // DP arrays
        $cnt0 = array_fill(0, $n + 1, 0); // zero primes on path from node to descendant (including itself if applicable)
        $cnt1 = array_fill(0, $n + 1, 0); // exactly one prime

        $ans = 0;

        // process nodes in post-order
        for ($idx = count($order) - 1; $idx >= 0; $idx--) {
            $u = $order[$idx];
            $totalZeroChildren = 0;
            $totalOneChildren = 0;
            $childrenC0 = [];
            $childrenC1 = [];

            foreach ($graph[$u] as $v) {
                if ($parent[$v] !== $u) continue; // only children
                $c0 = $cnt0[$v];
                $c1 = $cnt1[$v];
                $childrenC0[] = $c0;
                $childrenC1[] = $c1;
                $totalZeroChildren += $c0;
                $totalOneChildren += $c1;
            }

            if ($isPrime[$u]) {
                // node itself is prime
                $cnt0[$u] = 0;
                $cnt1[$u] = 1 + $totalZeroChildren; // self + zero‑prime descendants

                // pairs where one endpoint is u
                $ans += $totalZeroChildren;

                // pairs across different child subtrees (both sides have zero primes)
                $cross = 0;
                foreach ($childrenC0 as $c0) {
                    $cross += $c0 * ($totalZeroChildren - $c0);
                }
                $ans += intdiv($cross, 2);
            } else {
                // node is not prime
                $cnt0[$u] = 1 + $totalZeroChildren; // self counts as zero‑prime path
                $cnt1[$u] = $totalOneChildren;

                // pairs where one endpoint is u and the other side has exactly one prime
                $ans += $cnt1[$u];

                // cross child pairs: one side zero, other side one prime
                $cross = 0;
                $childCount = count($childrenC0);
                for ($i = 0; $i < $childCount; $i++) {
                    $c0 = $childrenC0[$i];
                    $c1 = $childrenC1[$i];
                    $cross += $c0 * ($totalOneChildren - $c1);
                }
                $ans += $cross;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countPaths(_ n: Int, _ edges: [[Int]]) -> Int {
        // Sieve for primes up to n
        var isPrime = [Bool](repeating: true, count: n + 1)
        if n >= 0 { isPrime[0] = false }
        if n >= 1 { isPrime[1] = false }
        var i = 2
        while i * i <= n {
            if isPrime[i] {
                var j = i * i
                while j <= n {
                    isPrime[j] = false
                    j += i
                }
            }
            i += 1
        }
        
        // Build adjacency list
        var adj = [[Int]](repeating: [], count: n + 1)
        for e in edges {
            let u = e[0]
            let v = e[1]
            adj[u].append(v)
            adj[v].append(u)
        }
        
        // Iterative DFS to get order and parent
        var parent = [Int](repeating: 0, count: n + 1)
        var order = [Int]()
        order.reserveCapacity(n)
        var stack = [Int]()
        stack.append(1)
        parent[1] = -1
        while let node = stack.popLast() {
            order.append(node)
            for nb in adj[node] where nb != parent[node] {
                parent[nb] = node
                stack.append(nb)
            }
        }
        
        var dp0 = [Int64](repeating: 0, count: n + 1) // zero primes
        var dp1 = [Int64](repeating: 0, count: n + 1) // exactly one prime
        var ans: Int64 = 0
        
        for node in order.reversed() {
            var totalZero: Int64 = 0
            var totalOne: Int64 = 0
            var sumZeroSq: Int64 = 0
            var sumZeroOne: Int64 = 0
            
            for nb in adj[node] where nb != parent[node] {
                let zero = dp0[nb]
                let one = dp1[nb]
                totalZero += zero
                totalOne += one
                sumZeroSq += zero * zero
                sumZeroOne += zero * one
            }
            
            if isPrime[node] {
                // pairs from two different children both having zero primes
                let crossPairs = (totalZero * totalZero - sumZeroSq) / 2
                ans += crossPairs
                // pairs where one endpoint is the node itself and other side has zero primes
                ans += totalZero
                dp0[node] = 0
                dp1[node] = totalZero + 1   // single node path counts as one prime
            } else {
                // pairs where exactly one side has a prime
                let crossPairs = totalZero * totalOne - sumZeroOne
                ans += crossPairs
                // pairs with the node itself and a side containing exactly one prime
                ans += totalOne
                dp0[node] = totalZero + 1   // path consisting only of this non‑prime node
                dp1[node] = totalOne        // paths that already contain one prime in a subtree
            }
        }
        
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun countPaths(n: Int, edges: Array<IntArray>): Long {
        val adj = Array(n + 1) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        // sieve for primes up to n
        val isPrime = BooleanArray(n + 1) { true }
        if (n >= 0) isPrime[0] = false
        if (n >= 1) isPrime[1] = false
        var p = 2
        while (p * p <= n) {
            if (isPrime[p]) {
                var mul = p * p
                while (mul <= n) {
                    isPrime[mul] = false
                    mul += p
                }
            }
            p++
        }

        val parent = IntArray(n + 1)
        val order = IntArray(n)
        var idx = 0
        val stack = ArrayDeque<Int>()
        stack.push(1)
        parent[1] = -1
        while (stack.isNotEmpty()) {
            val node = stack.pop()
            order[idx++] = node
            for (nb in adj[node]) {
                if (nb != parent[node]) {
                    parent[nb] = node
                    stack.push(nb)
                }
            }
        }

        val dp0 = LongArray(n + 1) // paths from node to descendant with 0 primes (including itself when applicable)
        val dp1 = LongArray(n + 1) // paths from node to descendant with exactly 1 prime

        var answer = 0L

        for (i in n - 1 downTo 0) {
            val node = order[i]
            var zeroTotal = 0L
            var oneTotal = 0L
            var sumSqZero = 0L
            var sumZeroOneSame = 0L

            for (child in adj[node]) {
                if (parent[child] == node) {
                    if (isPrime[node]) {
                        val childZero = dp0[child]
                        zeroTotal += childZero
                        sumSqZero += childZero * childZero
                    } else {
                        val childZero = dp0[child]
                        val childOne = dp1[child]
                        zeroTotal += childZero
                        oneTotal += childOne
                        sumSqZero += childZero * childZero
                        sumZeroOneSame += childZero * childOne
                    }
                }
            }

            if (isPrime[node]) {
                // pairs where node is one endpoint
                answer += zeroTotal
                // pairs across different subtrees
                answer += (zeroTotal * zeroTotal - sumSqZero) / 2

                dp0[node] = 0L
                dp1[node] = 1L + zeroTotal
            } else {
                // node not prime
                answer += oneTotal
                answer += zeroTotal * oneTotal - sumZeroOneSame

                dp0[node] = 1L + zeroTotal
                dp1[node] = oneTotal
            }
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  int countPaths(int n, List<List<int>> edges) {
    // Build adjacency list
    List<List<int>> g = List.generate(n + 1, (_) => []);
    for (var e in edges) {
      int u = e[0], v = e[1];
      g[u].add(v);
      g[v].add(u);
    }

    // Sieve of Eratosthenes to find primes up to n
    List<bool> isPrime = List.filled(n + 1, false);
    if (n >= 2) {
      List<bool> sieve = List.filled(n + 1, true);
      sieve[0] = sieve[1] = false;
      for (int i = 2; i * i <= n; ++i) {
        if (sieve[i]) {
          for (int j = i * i; j <= n; j += i) sieve[j] = false;
        }
      }
      isPrime = sieve;
    }

    // Parent array and order of traversal (DFS)
    List<int> parent = List.filled(n + 1, -1);
    List<int> order = [];
    List<int> stack = [1];
    parent[1] = 0;
    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      order.add(node);
      for (int nb in g[node]) {
        if (parent[nb] == -1) {
          parent[nb] = node;
          stack.add(nb);
        }
      }
    }

    // dp0: paths from node downwards with 0 primes, including the node itself when non‑prime
    // dp1: paths from node downwards with exactly 1 prime, including the node itself when prime
    List<int> dp0 = List.filled(n + 1, 0);
    List<int> dp1 = List.filled(n + 1, 0);

    for (int idx = order.length - 1; idx >= 0; --idx) {
      int i = order[idx];
      if (isPrime[i]) {
        dp0[i] = 0;
        dp1[i] = 1; // the node itself
        for (int nb in g[i]) {
          if (parent[nb] == i) {
            dp1[i] += dp0[nb];
          }
        }
      } else {
        dp0[i] = 1; // the node itself contributes a zero‑prime path
        dp1[i] = 0;
        for (int nb in g[i]) {
          if (parent[nb] == i) {
            dp0[i] += dp0[nb];
            dp1[i] += dp1[nb];
          }
        }
      }
    }

    int ans = 0;

    // Compute contributions per node
    for (int i = 1; i <= n; ++i) {
      int zeroSum = 0;
      int oneSum = 0;
      List<int> childZero = [];
      for (int nb in g[i]) {
        if (parent[nb] == i) {
          zeroSum += dp0[nb];
          oneSum += dp1[nb];
          childZero.add(dp0[nb]);
        }
      }

      if (isPrime[i]) {
        // pairs where the unique prime is the current node
        // a) both endpoints in different subtrees with zero primes
        int sumSq = 0;
        for (int z in childZero) {
          sumSq += z * z;
        }
        ans += ((zeroSum * zeroSum - sumSq) ~/ 2);
        // b) one endpoint is the node itself, other in a subtree with zero primes
        ans += zeroSum;
      } else {
        // pairs where exactly one prime lies in one subtree and the other side has none
        for (int nb in g[i]) {
          if (parent[nb] == i) {
            ans += dp1[nb] * (zeroSum - dp0[nb]);
          }
        }
        // pairs where one endpoint is the node itself and the other side contains exactly one prime
        ans += oneSum;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func countPaths(n int, edges [][]int) int64 {
    g := make([][]int, n+1)
    for _, e := range edges {
        u, v := e[0], e[1]
        g[u] = append(g[u], v)
        g[v] = append(g[v], u)
    }

    isPrime := make([]bool, n+1)
    if n >= 2 {
        for i := 2; i <= n; i++ {
            isPrime[i] = true
        }
        for p := 2; p*p <= n; p++ {
            if isPrime[p] {
                for m := p * p; m <= n; m += p {
                    isPrime[m] = false
                }
            }
        }
    }

    var ans int64

    var dfs func(int, int) (int64, int64)
    dfs = func(u, parent int) (int64, int64) {
        var cum0, cum1 int64
        if !isPrime[u] {
            cum0 = 1 // path consisting only of u with zero primes
        } else {
            cum1 = 1 // path consisting only of u with one prime
        }

        for _, v := range g[u] {
            if v == parent {
                continue
            }
            child0, child1 := dfs(v, u)
            if !isPrime[u] {
                ans += cum0*child1 + cum1*child0
                cum0 += child0
                cum1 += child1
            } else {
                // u is prime: only paths with exactly one prime are relevant
                ans += cum1 * child0
                cum1 += child0
                // cum0 stays zero
            }
        }

        var dp0, dp1 int64
        if !isPrime[u] {
            dp0 = cum0
            dp1 = cum1
        } else {
            dp0 = 0
            dp1 = cum1 // includes the trivial path and all child paths with zero primes
        }
        return dp0, dp1
    }

    dfs(1, 0)
    return ans
}
```

## Ruby

```ruby
def count_paths(n, edges)
  # Sieve of Eratosthenes for primality up to n
  prime = Array.new(n + 1, true)
  prime[0] = prime[1] = false
  i = 2
  while i * i <= n
    if prime[i]
      j = i * i
      while j <= n
        prime[j] = false
        j += i
      end
    end
    i += 1
  end

  # Build adjacency list
  adj = Array.new(n + 1) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  parent = Array.new(n + 1, 0)
  order = []
  stack = [1]
  parent[1] = -1
  while (v = stack.pop)
    order << v
    adj[v].each do |to|
      next if to == parent[v]
      parent[to] = v
      stack << to
    end
  end

  dp0 = Array.new(n + 1, 0) # paths from node with 0 primes (including itself)
  dp1 = Array.new(n + 1, 0) # paths from node with exactly 1 prime

  ans = 0

  order.reverse_each do |v|
    is_prime = prime[v]
    sum_cnt0 = 0
    sum_cnt1 = 0
    child_cnt0_total = 0
    child_cnt1_total = 0

    adj[v].each do |to|
      next if to == parent[v]

      cnt0 = dp0[to] # nodes in child's subtree with 0 primes from child downwards
      cnt1 = dp1[to] # nodes with exactly 1 prime from child downwards

      # contributions where endpoints are in different child subtrees (LCA = v)
      if is_prime
        ans += cnt0 * sum_cnt0
      else
        ans += cnt1 * sum_cnt0 + cnt0 * sum_cnt1
      end

      sum_cnt0 += cnt0
      sum_cnt1 += cnt1

      child_cnt0_total += cnt0
      child_cnt1_total += cnt1
    end

    # contributions where one endpoint is v itself
    if is_prime
      ans += child_cnt0_total
    else
      ans += child_cnt1_total
    end

    # compute dp values for parent use
    if is_prime
      dp0[v] = 0
      dp1[v] = 1 + child_cnt0_total
    else
      dp0[v] = 1 + child_cnt0_total
      dp1[v] = child_cnt1_total
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countPaths(n: Int, edges: Array[Array[Int]]): Long = {
        // adjacency list
        val adj = Array.fill(n + 1)(new scala.collection.mutable.ArrayBuffer[Int]())
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            adj(u).append(v)
            adj(v).append(u)
        }

        // sieve of Eratosthenes
        val isPrime = new Array[Boolean](n + 1)
        if (n >= 2) {
            java.util.Arrays.fill(isPrime, true)
            isPrime(0) = false
            isPrime(1) = false
            var p = 2
            while (p * p <= n) {
                if (isPrime(p)) {
                    var mul = p * p
                    while (mul <= n) {
                        isPrime(mul) = false
                        mul += p
                    }
                }
                p += 1
            }
        }

        // root the tree at 1, get parent and order for post‑order processing
        val parent = new Array[Int](n + 1)
        val order = new scala.collection.mutable.ArrayBuffer[Int]()
        val stack = new scala.collection.mutable.Stack[Int]()
        stack.push(1)
        parent(1) = 0
        while (stack.nonEmpty) {
            val u = stack.pop()
            order.append(u)
            for (v <- adj(u)) {
                if (v != parent(u)) {
                    parent(v) = u
                    stack.push(v)
                }
            }
        }

        // dp arrays: cnt0 - paths from node downwards with 0 primes, cnt1 - with exactly 1 prime
        val cnt0 = new Array[Long](n + 1)
        val cnt1 = new Array[Long](n + 1)

        for (i <- order.length - 1 to 0 by -1) {
            val u = order(i)
            if (isPrime(u)) {
                var sumZeroChildren = 0L
                for (v <- adj(u) if v != parent(u)) {
                    sumZeroChildren += cnt0(v)
                }
                cnt0(u) = 0L
                cnt1(u) = 1L + sumZeroChildren // includes the node itself
            } else {
                var sumZero = 1L // the node itself contributes a zero‑prime path
                var sumOne = 0L
                for (v <- adj(u) if v != parent(u)) {
                    sumZero += cnt0(v)
                    sumOne += cnt1(v)
                }
                cnt0(u) = sumZero
                cnt1(u) = sumOne
            }
        }

        var ans: Long = 0L

        for (u <- 1 to n) {
            // pairs where one endpoint is the node itself
            if (isPrime(u)) {
                var childZeroSum = 0L
                for (v <- adj(u) if v != parent(u)) {
                    childZeroSum += cnt0(v)
                }
                ans += childZeroSum
            } else {
                ans += cnt1(u)
            }

            // pairs where endpoints lie in different subtrees of u
            if (isPrime(u)) {
                var prefix: Long = 0L
                var cross: Long = 0L
                for (v <- adj(u) if v != parent(u)) {
                    val c0 = cnt0(v)
                    cross += prefix * c0
                    prefix += c0
                }
                ans += cross
            } else {
                var sum0: Long = 0L
                var sum1: Long = 0L
                var sameChild: Long = 0L
                for (v <- adj(u) if v != parent(u)) {
                    val c0 = cnt0(v)
                    val c1 = cnt1(v)
                    sum0 += c0
                    sum1 += c1
                    sameChild += c0 * c1
                }
                val orderedCross = sum0 * sum1 - sameChild
                ans += orderedCross / 2
            }
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_paths(n: i32, edges: Vec<Vec<i32>>) -> i64 {
        let n_usize = n as usize;
        // build adjacency list
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n_usize + 1];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }

        // sieve primes up to n
        let mut is_prime = vec![true; n_usize + 1];
        if n_usize >= 0 {
            is_prime[0] = false;
        }
        if n_usize >= 1 {
            is_prime[1] = false;
        }
        let limit = (n_usize as f64).sqrt() as usize + 1;
        for i in 2..=limit {
            if is_prime[i] {
                let mut j = i * i;
                while j <= n_usize {
                    is_prime[j] = false;
                    j += i;
                }
            }
        }

        // parent array and order (preorder)
        let mut parent = vec![0usize; n_usize + 1];
        let mut order: Vec<usize> = Vec::with_capacity(n_usize);
        let mut stack: Vec<usize> = Vec::new();
        stack.push(1);
        parent[1] = 0;
        while let Some(u) = stack.pop() {
            order.push(u);
            for &v in adj[u].iter() {
                if v != parent[u] {
                    parent[v] = u;
                    stack.push(v);
                }
            }
        }

        // dp arrays
        let mut dp0: Vec<i64> = vec![0; n_usize + 1];
        let mut dp1: Vec<i64> = vec![0; n_usize + 1];

        let mut answer: i64 = 0;

        for &u in order.iter().rev() {
            let mut total_zero: i64 = 0;
            let mut total_one: i64 = 0;
            let mut same_child_product: i64 = 0;

            for &v in adj[u].iter() {
                if parent[v] == u {
                    let c0 = dp0[v];
                    let c1 = dp1[v];
                    total_zero += c0;
                    total_one += c1;
                    same_child_product += c0 * c1;
                }
            }

            if is_prime[u] {
                // pairs where one endpoint is u
                answer += total_zero;
                // pairs across two different children both zero primes
                answer += total_zero * (total_zero - 1) / 2;

                dp0[u] = 0;
                dp1[u] = 1 + total_zero; // node itself plus paths through child with zero primes
            } else {
                // pairs where one endpoint is u and descendant has exactly one prime
                answer += total_one;
                // cross-child pairs: one side zero, other side one prime
                answer += total_zero * total_one - same_child_product;

                dp0[u] = 1 + total_zero; // node itself counted
                dp1[u] = total_one;
            }
        }

        answer
    }
}
```

## Racket

```racket
(define (count-paths n edges)
  (let* ((adj (make-vector (+ n 1) '()))
         (is-prime (make-vector (+ n 1) #t)))
    ;; sieve
    (vector-set! is-prime 0 #f)
    (when (> n 0) (vector-set! is-prime 1 #f))
    (let loop ((p 2))
      (when (<= (* p p) n)
        (when (vector-ref is-prime p)
          (let inner ((m (* p p)))
            (when (<= m n)
              (vector-set! is-prime m #f)
              (inner (+ m p)))))
        (loop (+ p 1))))
    ;; build adjacency
    (for-each (lambda (e)
                (let ((u (list-ref e 0))
                      (v (list-ref e 1)))
                  (vector-set! adj u (cons v (vector-ref adj u)))
                  (vector-set! adj v (cons u (vector-ref adj v)))))
              edges)
    ;; parent array and traversal order
    (define parent (make-vector (+ n 1) -1))
    (define order '())
    (let ((stack (list 1)))
      (vector-set! parent 1 0)
      (let loop ()
        (when (not (null? stack))
          (define node (car stack))
          (set! stack (cdr stack))
          (set! order (cons node order))
          (for-each (lambda (nbr)
                      (when (= (vector-ref parent nbr) -1)
                        (vector-set! parent nbr node)
                        (set! stack (cons nbr stack))))
                    (vector-ref adj node))
          (loop)))))
    ;; dp vectors
    (define dp0 (make-vector (+ n 1) 0))
    (define dp1 (make-vector (+ n 1) 0))
    (define ans 0)
    (for-each
     (lambda (node)
       (let ((sumZero 0)
             (sumOne 0)
             (sumSqZero 0)
             (sumProd 0))
         (for-each
          (lambda (nbr)
            (when (= (vector-ref parent nbr) node)
              (let ((cz (vector-ref dp0 nbr))
                    (co (vector-ref dp1 nbr)))
                (set! sumZero (+ sumZero cz))
                (set! sumOne (+ sumOne co))
                (set! sumSqZero (+ sumSqZero (* cz cz)))
                (set! sumProd (+ sumProd (* cz co))))))
          (vector-ref adj node))
         (if (vector-ref is-prime node)
             (begin
               ;; prime node
               (vector-set! dp0 node 0)
               (vector-set! dp1 node (+ sumZero 1))
               ;; contributions
               (set! ans (+ ans sumZero)) ; pairs (node, descendant) with zero primes elsewhere
               (let ((pairs (quotient (- (* sumZero sumZero) sumSqZero) 2)))
                 (set! ans (+ ans pairs))))
             (begin
               ;; non‑prime node
               (vector-set! dp0 node (+ sumZero 1))
               (vector-set! dp1 node sumOne)
               ;; contributions
               (set! ans (+ ans sumOne)) ; pairs (node, descendant) with exactly one prime
               (let ((cross (- (* sumZero sumOne) sumProd)))
                 (set! ans (+ ans cross))))))))
     (reverse order))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([count_paths/2]).

%% Entry point
-spec count_paths(N :: integer(), Edges :: [[integer()]]) -> integer().
count_paths(N, Edges) ->
    PrimeArr = sieve(N),
    Adj0 = array:new(N + 1, [{default, []}]),
    Adj = add_edges(Edges, Adj0),
    {ParentArr, Order} = dfs_order(Adj, N),
    RevOrder = lists:reverse(Order),
    DP0_0 = array:new(N + 1, [{default, 0}]),
    DP1_0 = array:new(N + 1, [{default, 0}]),
    Answer = process_nodes(RevOrder, Adj, ParentArr, PrimeArr, DP0_0, DP1_0, 0),
    Answer.

%% Sieve of Eratosthenes returning an array where Index -> true if prime
-spec sieve(integer()) -> any().
sieve(Limit) ->
    Arr0 = array:new(Limit + 1, [{default, true}]),
    Arr1 = array:set(0, false, Arr0),
    Arr2 = array:set(1, false, Arr1),
    Max = trunc(math:sqrt(Limit)),
    sieve_loop(2, Max, Limit, Arr2).

-spec sieve_loop(integer(), integer(), integer(), any()) -> any().
sieve_loop(I, Max, Limit, Arr) when I =< Max ->
    case array:get(I, Arr) of
        true ->
            Arr1 = mark_multiples(I * I, I, Limit, Arr),
            sieve_loop(I + 1, Max, Limit, Arr1);
        false ->
            sieve_loop(I + 1, Max, Limit, Arr)
    end;
sieve_loop(_, _, _, Arr) -> Arr.

-spec mark_multiples(integer(), integer(), integer(), any()) -> any().
mark_multiples(J, Step, Limit, Arr) when J =< Limit ->
    Arr1 = array:set(J, false, Arr),
    mark_multiples(J + Step, Step, Limit, Arr1);
mark_multiples(_, _, _, Arr) -> Arr.

%% Build adjacency list
-spec add_edges([[integer()]], any()) -> any().
add_edges([], Adj) -> Adj;
add_edges([[U,V]|Rest], Adj) ->
    ListU = array:get(U, Adj),
    ListV = array:get(V, Adj),
    Adj1 = array:set(U, [V|ListU], Adj),
    Adj2 = array:set(V, [U|ListV], Adj1),
    add_edges(Rest, Adj2).

%% Perform DFS to obtain parent array and preorder traversal order
-spec dfs_order(any(), integer()) -> {any(), [integer()]}.
dfs_order(Adj, N) ->
    Parent0 = array:new(N + 1, [{default, 0}]),
    dfs_stack([1], Parent0, Adj, [], []).

-spec dfs_stack([integer()], any(), any(), [integer()], [integer()]) -> {any(), [integer()]}.
dfs_stack([], ParentArr, _Adj, OrderAcc, _) ->
    {ParentArr, lists:reverse(OrderAcc)};
dfs_stack([Node|Stack], ParentArr, Adj, OrderAcc, Visited) ->
    Neigh = array:get(Node, Adj),
    {ParentArr1, Stack1} = process_neighbors(Neigh, Node, ParentArr, Stack, []),
    dfs_stack(Stack1, ParentArr1, Adj, [Node|OrderAcc], Visited).

-spec process_neighbors([integer()], integer(), any(), [integer()], [integer()]) -> {any(), [integer()]}.
process_neighbors([], _ParentNode, ParentArr, Stack, Acc) ->
    {ParentArr, lists:reverse(Acc) ++ Stack};
process_neighbors([Nb|Rest], ParentNode, ParentArr, Stack, Acc) ->
    case array:get(Nb, ParentArr) of
        0 -> % not visited yet
            ParentArr1 = array:set(Nb, ParentNode, ParentArr),
            process_neighbors(Rest, ParentNode, ParentArr1, [Nb|Stack], Acc);
        _Other ->
            process_neighbors(Rest, ParentNode, ParentArr, Stack, Acc)
    end.

%% Process nodes in postorder to compute dp values and answer
-spec process_nodes([integer()], any(), any(), any(), any(), any(), integer()) -> integer().
process_nodes([], _Adj, _Parent, _PrimeArr, DP0, DP1, Answer) ->
    Answer;
process_nodes([Node|Rest], Adj, ParentArr, PrimeArr, DP0Acc, DP1Acc, AnswerAcc) ->
    Children = [C || C <- array:get(Node, Adj), array:get(C, ParentArr) == Node],
    IsPrime = array:get(Node, PrimeArr),

    %% Gather sums of child dp values and endpoint contributions
    {SumDP0, SumDP1, EndpointAns} =
        lists:foldl(
            fun(Child, {Acc0, Acc1, AccAns}) ->
                C0 = array:get(Child, DP0Acc),
                C1 = array:get(Child, DP1Acc),
                Add = case IsPrime of
                          true -> C0;
                          false -> C1
                      end,
                {Acc0 + C0, Acc1 + C1, AccAns + Add}
            end,
            {0, 0, AnswerAcc},
            Children),

    %% Compute dp for current node
    {DP0Node, DP1Node} =
        case IsPrime of
            true -> {0, 1 + SumDP0};
            false -> {1 + SumDP0, SumDP1}
        end,
    DP0New = array:set(Node, DP0Node, DP0Acc),
    DP1New = array:set(Node, DP1Node, DP1Acc),

    %% Cross‑subtree pairs where LCA is current node
    CrossAns = cross_pairs(Children, IsPrime, DP0New, DP1New, 0, 0, 0),

    TotalAns = EndpointAns + CrossAns,
    process_nodes(Rest, Adj, ParentArr, PrimeArr, DP0New, DP1New, TotalAns).

%% Compute cross‑subtree contributions
-spec cross_pairs([integer()], boolean(), any(), any(),
                  integer(), integer(), integer()) -> integer().
cross_pairs([], _IsPrime, _DP0, _DP1, _Cum0, _Cum1, Acc) ->
    Acc;
cross_pairs([Child|Rest], IsPrime, DP0Arr, DP1Arr, Cum0, Cum1, Acc) ->
    C0 = array:get(Child, DP0Arr),
    C1 = array:get(Child, DP1Arr),
    Add =
        case IsPrime of
            true -> C0 * Cum0;
            false -> C0 * Cum1 + C1 * Cum0
        end,
    cross_pairs(Rest, IsPrime, DP0Arr, DP1Arr,
                Cum0 + C0, Cum1 + C1, Acc + Add).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_paths(n :: integer, edges :: [[integer]]) :: integer
  def count_paths(n, edges) do
    # Build adjacency map
    adj = Enum.reduce(edges, %{}, fn [u, v], acc ->
      acc
      |> Map.update(u, [v], &[v | &1])
      |> Map.update(v, [u], &[u | &1])
    end)

    # Sieve of Eratosthenes for primes up to n
    is_prime = sieve(n)

    # Iterative DFS to get parent map and postorder list
    {parent_map, postorder} = dfs_order(1, adj)

    # DP maps
    dp0 = %{}
    dp1 = %{}
    ans = 0

    Enum.each(postorder, fn node ->
      children =
        Map.get(adj, node, [])
        |> Enum.filter(fn v -> Map.get(parent_map, v) == node end)

      total0 = Enum.reduce(children, 0, fn c, acc -> acc + Map.get(dp0, c, 0) end)
      total1 = Enum.reduce(children, 0, fn c, acc -> acc + Map.get(dp1, c, 0) end)

      if :array.get(node, is_prime) do
        # node is prime
        dp0_val = 0
        dp1_val = total0 + 1

        contrib = total0
        prefix = 0

        Enum.each(children, fn child ->
          c0 = Map.get(dp0, child, 0)
          contrib = contrib + prefix * c0
          prefix = prefix + c0
        end)

        ans = ans + contrib
        dp0 = Map.put(dp0, node, dp0_val)
        dp1 = Map.put(dp1, node, dp1_val)
      else
        # node is not prime
        dp0_val = total0 + 1
        dp1_val = total1

        contrib = total1

        Enum.each(children, fn child ->
          c0 = Map.get(dp0, child, 0)
          c1 = Map.get(dp1, child, 0)
          contrib = contrib + c1 * (total0 - c0)
        end)

        ans = ans + contrib
        dp0 = Map.put(dp0, node, dp0_val)
        dp1 = Map.put(dp1, node, dp1_val)
      end
    end)

    ans
  end

  # Build sieve array of booleans (true if prime) using :array for O(1) access
  defp sieve(limit) do
    arr = :array.new(limit + 1, default: true)
    arr = :array.set(0, false, :array.set(1, false, arr))
    max = :math.sqrt(limit) |> trunc()

    Enum.reduce(2..max, arr, fn i, a ->
      if :array.get(i, a) do
        start = i * i
        Enum.reduce_while(start..limit, a, fn j, acc ->
          {:cont, :array.set(j, false, acc)}
        end)
      else
        a
      end
    end)
  end

  # Perform iterative DFS to obtain parent map and postorder traversal list
  defp dfs_order(root, adj) do
    stack = [{root, 0}]
    parent = %{}
    order = []

    {parent, order} =
      while_stack(stack, parent, order, adj)

    postorder = Enum.reverse(order)
    {parent, postorder}
  end

  defp while_stack([], parent, order, _adj), do: {parent, order}

  defp while_stack([{node, par} | rest], parent, order, adj) do
    parent = Map.put(parent, node, par)
    order = [node | order]

    children =
      Map.get(adj, node, [])
      |> Enum.filter(fn v -> v != par end)

    new_stack = Enum.reduce(children, rest, fn child, acc -> [{child, node} | acc] end)

    while_stack(new_stack, parent, order, adj)
  end
end
```

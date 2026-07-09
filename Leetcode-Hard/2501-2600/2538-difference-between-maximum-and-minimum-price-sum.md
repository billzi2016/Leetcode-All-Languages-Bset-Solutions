# 2538. Difference Between Maximum and Minimum Price Sum

## Cpp

```cpp
class Solution {
public:
    long long maxOutput(int n, vector<vector<int>>& edges, vector<int>& price) {
        vector<vector<int>> g(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            g[u].push_back(v);
            g[v].push_back(u);
        }
        vector<int> parent(n, -1), order;
        order.reserve(n);
        stack<int> st;
        st.push(0);
        parent[0] = 0;
        while (!st.empty()) {
            int u = st.top(); st.pop();
            order.push_back(u);
            for (int v : g[u]) if (v != parent[u]) {
                parent[v] = u;
                st.push(v);
            }
        }

        vector<long long> dpDown(n, 0), up(n, 0);
        vector<long long> best1(n, 0), best2(n, 0); // top two child contributions

        for (int i = n - 1; i >= 0; --i) {
            int u = order[i];
            long long mx = 0;
            for (int v : g[u]) if (v != parent[u]) {
                long long val = dpDown[v];
                if (val > mx) mx = val;
                if (val >= best1[u]) {
                    best2[u] = best1[u];
                    best1[u] = val;
                } else if (val > best2[u]) {
                    best2[u] = val;
                }
            }
            dpDown[u] = price[u] + mx;
        }

        up[0] = price[0];
        for (int u : order) {
            for (int v : g[u]) if (v != parent[u]) {
                long long siblingBest = (dpDown[v] == best1[u]) ? best2[u] : best1[u];
                long long candidateFromParent = max(up[u], price[u] + siblingBest);
                up[v] = price[v] + candidateFromParent;
            }
        }

        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            long long best = max(dpDown[i], up[i]);
            ans = max(ans, best - price[i]);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long maxOutput(int n, int[][] edges, int[] price) {
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            int a = e[0], b = e[1];
            adj[a].add(b);
            adj[b].add(a);
        }

        int[] parent = new int[n];
        Arrays.fill(parent, -1);
        int[] order = new int[n];
        int idx = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        parent[0] = -2; // visited marker
        while (!stack.isEmpty()) {
            int v = stack.pop();
            order[idx++] = v;
            for (int nb : adj[v]) {
                if (parent[nb] == -1) {
                    parent[nb] = v;
                    stack.push(nb);
                }
            }
        }

        long[] down = new long[n];
        for (int i = n - 1; i >= 0; --i) {
            int v = order[i];
            long best = 0;
            for (int nb : adj[v]) {
                if (nb == parent[v]) continue;
                best = Math.max(best, down[nb]);
            }
            down[v] = price[v] + best;
        }

        long[] up = new long[n];
        up[0] = 0; // no contribution from parent for root
        long answer = 0;

        for (int i = 0; i < n; ++i) {
            int v = order[i];

            // find top two child down values
            long max1 = 0, max2 = 0;
            for (int nb : adj[v]) {
                if (nb == parent[v]) continue;
                long val = down[nb];
                if (val > max1) {
                    max2 = max1;
                    max1 = val;
                } else if (val > max2) {
                    max2 = val;
                }
            }

            // update answer for this node
            long extra = Math.max(max1, up[v]);
            answer = Math.max(answer, extra);

            // propagate to children
            for (int nb : adj[v]) {
                if (nb == parent[v]) continue;
                long siblingBest = (down[nb] == max1) ? max2 : max1;
                long bestOther = Math.max(up[v], siblingBest);
                up[nb] = price[v] + Math.max(0, bestOther);
            }
        }

        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def maxOutput(self, n, edges, price):
        """
        :type n: int
        :type edges: List[List[int]]
        :type price: List[int]
        :rtype: int
        """
        if n == 1:
            return 0

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        parent = [-1] * n
        order = []
        stack = [0]
        parent[0] = -2  # mark root visited

        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    stack.append(v)

        down = [0] * n          # max sum from node downwards (including itself)
        best1 = [0] * n         # largest child contribution
        best2 = [0] * n         # second largest child contribution

        for u in reversed(order):
            max_child = 0
            for v in adj[u]:
                if parent[v] == u:   # v is a child of u
                    val = down[v]
                    if val > max_child:
                        max_child = val
                    # maintain top two values
                    if val >= best1[u]:
                        best2[u] = best1[u]
                        best1[u] = val
                    elif val > best2[u]:
                        best2[u] = val
            down[u] = price[u] + max_child

        up = [0] * n  # contribution from parent side (excluding node's own price)
        for u in order:
            for v in adj[u]:
                if parent[v] == u:   # child
                    # best sibling contribution excluding this child
                    use_best = best1[u] if down[v] != best1[u] else best2[u]
                    up[v] = price[u] + max(up[u], use_best)

        ans = 0
        for i in range(n):
            contrib = max(up[i], best1[i])
            if contrib > ans:
                ans = contrib
        return ans
```

## Python3

```python
import sys
from typing import List

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        sys.setrecursionlimit(1 << 25)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dp = [0] * n          # max sum from node downwards (including node)
        top1 = [0] * n        # largest child dp value
        top2 = [0] * n        # second largest child dp value

        def dfs1(u: int, p: int) -> None:
            best_a = best_b = 0
            for v in adj[u]:
                if v == p:
                    continue
                dfs1(v, u)
                val = dp[v]
                if val > best_a:
                    best_b = best_a
                    best_a = val
                elif val > best_b:
                    best_b = val
            top1[u] = best_a
            top2[u] = best_b
            dp[u] = price[u] + (best_a if best_a else 0)

        dfs1(0, -1)

        up = [0] * n   # max sum reachable from node via parent side (excluding node's own price)

        def dfs2(u: int, p: int) -> None:
            for v in adj[u]:
                if v == p:
                    continue
                # best child contribution of u excluding v
                use = top1[u] if dp[v] != top1[u] else top2[u]
                candidate = up[u] if up[u] > use else use
                up[v] = price[u] + (candidate if candidate else 0)
                dfs2(v, u)

        dfs2(0, -1)

        ans = 0
        for i in range(n):
            best_gain = top1[i]
            if up[i] > best_gain:
                best_gain = up[i]
            if best_gain > ans:
                ans = best_gain
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int farthest_node(int start, int n, int **adj, int *deg, const int *price, long long *dist) {
    char *vis = (char *)calloc(n, sizeof(char));
    int *stack = (int *)malloc(n * sizeof(int));
    int top = 0;
    stack[top++] = start;
    dist[start] = price[start];
    vis[start] = 1;

    int farNode = start;
    long long maxDist = dist[start];

    while (top) {
        int u = stack[--top];
        if (dist[u] > maxDist) {
            maxDist = dist[u];
            farNode = u;
        }
        for (int i = 0; i < deg[u]; ++i) {
            int v = adj[u][i];
            if (!vis[v]) {
                vis[v] = 1;
                dist[v] = dist[u] + price[v];
                stack[top++] = v;
            }
        }
    }

    free(vis);
    free(stack);
    return farNode;
}

long long maxOutput(int n, int** edges, int edgesSize, int* edgesColSize, int* price, int priceSize) {
    (void)edgesColSize; // unused
    if (n == 0) return 0;

    /* compute degrees */
    int *deg = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        deg[a]++; deg[b]++;
    }

    /* build adjacency list */
    int **adj = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        adj[i] = (int *)malloc(deg[i] * sizeof(int));
    }
    int *cur = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        adj[a][cur[a]++] = b;
        adj[b][cur[b]++] = a;
    }
    free(cur);

    /* first DFS to find one endpoint of diameter */
    long long *distTmp = (long long *)calloc(n, sizeof(long long));
    int A = farthest_node(0, n, adj, deg, price, distTmp);

    /* second DFS from A */
    long long *distA = (long long *)calloc(n, sizeof(long long));
    int B = farthest_node(A, n, adj, deg, price, distA);

    /* third DFS from B */
    long long *distB = (long long *)calloc(n, sizeof(long long));
    farthest_node(B, n, adj, deg, price, distB); // we only need distances

    long long answer = 0;
    for (int i = 0; i < n; ++i) {
        long long maxDist = distA[i] > distB[i] ? distA[i] : distB[i];
        long long cand = maxDist - price[i];
        if (cand > answer) answer = cand;
    }

    /* cleanup */
    for (int i = 0; i < n; ++i) free(adj[i]);
    free(adj);
    free(deg);
    free(distTmp);
    free(distA);
    free(distB);

    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MaxOutput(int n, int[][] edges, int[] price) {
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            g[a].Add(b);
            g[b].Add(a);
        }

        long[] p = new long[n];
        for (int i = 0; i < n; i++) p[i] = price[i];

        int[] parent = new int[n];
        Array.Fill(parent, -1);
        var order = new List<int>(n);
        var stack = new Stack<int>();
        stack.Push(0);
        parent[0] = -2; // mark as visited root

        while (stack.Count > 0) {
            int v = stack.Pop();
            order.Add(v);
            foreach (int nb in g[v]) {
                if (nb == parent[v]) continue;
                parent[nb] = v;
                stack.Push(nb);
            }
        }

        long[] down = new long[n];
        for (int i = order.Count - 1; i >= 0; --i) {
            int v = order[i];
            long best = 0;
            foreach (int nb in g[v]) {
                if (nb == parent[v]) continue;
                if (down[nb] > best) best = down[nb];
            }
            down[v] = p[v] + best;
        }

        long[] up = new long[n];
        up[0] = 0;

        foreach (int v in order) {
            // find top two child down values
            long first = 0, second = 0;
            foreach (int nb in g[v]) {
                if (nb == parent[v]) continue;
                long val = down[nb];
                if (val >= first) { second = first; first = val; }
                else if (val > second) { second = val; }
            }

            foreach (int nb in g[v]) {
                if (nb == parent[v]) continue;
                long use = (down[nb] == first) ? second : first;
                long candidate = up[v];
                if (use > candidate) candidate = use;
                up[nb] = p[v] + candidate;
            }
        }

        long ans = 0;
        for (int v = 0; v < n; ++v) {
            long best = up[v];
            foreach (int nb in g[v]) {
                if (nb == parent[v]) continue;
                if (down[nb] > best) best = down[nb];
            }
            if (best > ans) ans = best;
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
 * @param {number[]} price
 * @return {number}
 */
var maxOutput = function(n, edges, price) {
    const adj = Array.from({length: n}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    // parent and order for DFS
    const parent = new Int32Array(n);
    parent.fill(-1);
    const order = [];
    const stack = [0];
    parent[0] = -2; // root marker

    while (stack.length) {
        const v = stack.pop();
        order.push(v);
        for (const nb of adj[v]) {
            if (parent[nb] === -1) {
                parent[nb] = v;
                stack.push(nb);
            }
        }
    }

    // dpDown and top two child contributions
    const dpDown = new Array(n).fill(0);
    const top1 = new Array(n).fill(0);
    const top2 = new Array(n).fill(0);

    for (let i = order.length - 1; i >= 0; --i) {
        const v = order[i];
        let max1 = 0, max2 = 0;
        for (const nb of adj[v]) {
            if (nb === parent[v]) continue;
            const val = dpDown[nb];
            if (val > max1) {
                max2 = max1;
                max1 = val;
            } else if (val > max2) {
                max2 = val;
            }
        }
        top1[v] = max1;
        top2[v] = max2;
        dpDown[v] = price[v] + max1; // max1 is 0 for leaf
    }

    // up values (paths that go through parent side)
    const up = new Array(n).fill(0);
    up[0] = price[0]; // staying at root

    for (let i = 0; i < order.length; ++i) {
        const v = order[i];
        for (const nb of adj[v]) {
            if (nb === parent[v]) continue;
            const bestSibling = (dpDown[nb] === top1[v]) ? top2[v] : top1[v];
            let cand = up[v];
            const viaSibling = price[v] + bestSibling; // may be just price[v] if no sibling
            if (viaSibling > cand) cand = viaSibling;
            up[nb] = price[nb] + cand;
        }
    }

    let answer = 0;
    for (let i = 0; i < n; ++i) {
        const overall = Math.max(dpDown[i], up[i]);
        const cost = overall - price[i];
        if (cost > answer) answer = cost;
    }
    return answer;
};
```

## Typescript

```typescript
function maxOutput(n: number, edges: number[][], price: number[]): number {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
    }

    // Build parent array and traversal order (preorder)
    const parent = new Int32Array(n);
    parent.fill(-1);
    const order: number[] = [];
    const stack: number[] = [0];
    while (stack.length) {
        const u = stack.pop()!;
        order.push(u);
        for (const v of adj[u]) {
            if (v === parent[u]) continue;
            parent[v] = u;
            stack.push(v);
        }
    }

    // dpDown: max sum from node downwards (including itself)
    const dpDown = new Array<number>(n).fill(0);
    for (let i = order.length - 1; i >= 0; --i) {
        const u = order[i];
        let best = 0;
        for (const v of adj[u]) {
            if (v === parent[u]) continue;
            if (dpDown[v] > best) best = dpDown[v];
        }
        dpDown[u] = price[u] + best;
    }

    // For each node, store top two child contributions
    const max1Val = new Array<number>(n).fill(0);
    const max2Val = new Array<number>(n).fill(0);
    const max1Child = new Int32Array(n);
    max1Child.fill(-1);
    for (let u = 0; u < n; ++u) {
        for (const v of adj[u]) {
            if (v === parent[u]) continue;
            const val = dpDown[v];
            if (val > max1Val[u]) {
                max2Val[u] = max1Val[u];
                max1Val[u] = val;
                max1Child[u] = v;
            } else if (val > max2Val[u]) {
                max2Val[u] = val;
            }
        }
    }

    // up: max sum from node going through its parent side
    const up = new Array<number>(n).fill(0);
    up[0] = price[0];
    for (const u of order) {
        const upU = up[u];
        for (const v of adj[u]) {
            if (v === parent[u]) continue;
            const siblingBest = v === max1Child[u] ? max2Val[u] : max1Val[u];
            const bestFromUExcludingV = upU > siblingBest ? upU : siblingBest;
            up[v] = price[v] + bestFromUExcludingV;
        }
    }

    // Compute answer
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        const maxDist = dpDown[i] > up[i] ? dpDown[i] : up[i];
        const cost = maxDist - price[i];
        if (cost > ans) ans = cost;
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
     * @param Integer[] $price
     * @return Integer
     */
    function maxOutput($n, $edges, $price) {
        // build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            $adj[$a][] = $b;
            $adj[$b][] = $a;
        }

        $NEG = -PHP_INT_MAX; // sentinel for non‑existent values

        // first pass: get parent order and compute down values
        $parent = array_fill(0, $n, -1);
        $order = [];
        $stack = [0];
        $parent[0] = -2;
        while ($stack) {
            $u = array_pop($stack);
            $order[] = $u;
            foreach ($adj[$u] as $v) {
                if ($v === $parent[$u]) continue;
                $parent[$v] = $u;
                $stack[] = $v;
            }
        }

        $down = array_fill(0, $n, 0);
        $firstMax = array_fill(0, $n, $NEG);
        $secondMax = array_fill(0, $n, $NEG);

        for ($i = count($order) - 1; $i >= 0; --$i) {
            $u = $order[$i];
            $max1 = $NEG;
            $max2 = $NEG;
            foreach ($adj[$u] as $v) {
                if ($v === $parent[$u]) continue;
                $val = $down[$v]; // includes price[v]
                if ($val > $max1) {
                    $max2 = $max1;
                    $max1 = $val;
                } elseif ($val > $max2) {
                    $max2 = $val;
                }
            }
            $firstMax[$u] = $max1;
            $secondMax[$u] = $max2;

            $down[$u] = $price[$u];
            if ($max1 !== $NEG) {
                $candidate = $price[$u] + $max1;
                if ($candidate > $down[$u]) $down[$u] = $candidate;
            }
        }

        // second pass: propagate up values and compute answer
        $ans = 0;
        $stack = [[0, -1, 0]]; // node, parent, upFromParent (best sum starting at parent without this node)
        while ($stack) {
            [$u, $p, $up] = array_pop($stack);

            // best additional sum beyond price[u]
            $candidate = 0;
            if ($up > $candidate) $candidate = $up;
            if ($firstMax[$u] !== $NEG && $firstMax[$u] > $candidate) $candidate = $firstMax[$u];
            if ($candidate > $ans) $ans = $candidate;

            foreach ($adj[$u] as $v) {
                if ($v === $p) continue;
                // max sibling down excluding child v
                $maxSibling = $firstMax[$u];
                if ($down[$v] === $firstMax[$u]) {
                    $maxSibling = $secondMax[$u];
                }

                $bestAdd = 0;
                if ($up > $bestAdd) $bestAdd = $up;
                if ($maxSibling !== $NEG && $maxSibling > $bestAdd) $bestAdd = $maxSibling;

                // value to pass as up for child v (sum starting at u without using v)
                $newUp = $price[$u] + $bestAdd;
                $stack[] = [$v, $u, $newUp];
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxOutput(_ n: Int, _ edges: [[Int]], _ price: [Int]) -> Int {
        var adj = Array(repeating: [Int](), count: n)
        for e in edges {
            let u = e[0], v = e[1]
            adj[u].append(v)
            adj[v].append(u)
        }
        
        func getDistances(_ start: Int) -> [Int64] {
            var dist = Array(repeating: Int64.min, count: n)
            var stack: [(Int, Int)] = [(start, -1)]
            dist[start] = Int64(price[start])
            while let (u, p) = stack.popLast() {
                for v in adj[u] where v != p {
                    dist[v] = dist[u] + Int64(price[v])
                    stack.append((v, u))
                }
            }
            return dist
        }
        
        // First DFS to find one endpoint of the diameter
        let d0 = getDistances(0)
        var nodeA = 0
        var maxVal = d0[0]
        for i in 0..<n where d0[i] > maxVal {
            maxVal = d0[i]
            nodeA = i
        }
        
        // DFS from nodeA to find the other endpoint
        let distA = getDistances(nodeA)
        var nodeB = nodeA
        maxVal = distA[nodeA]
        for i in 0..<n where distA[i] > maxVal {
            maxVal = distA[i]
            nodeB = i
        }
        
        // Distances from both diameter endpoints
        let distB = getDistances(nodeB)
        
        var answer: Int64 = 0
        for i in 0..<n {
            let best = max(distA[i], distB[i]) - Int64(price[i])
            if best > answer { answer = best }
        }
        return Int(answer)
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun maxOutput(n: Int, edges: Array<IntArray>, price: IntArray): Long {
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val a = e[0]
            val b = e[1]
            adj[a].add(b)
            adj[b].add(a)
        }

        val parent = IntArray(n) { -1 }
        val order = IntArray(n)
        var idx = 0
        val stack = ArrayDeque<Int>()
        stack.push(0)
        parent[0] = -2 // mark visited root

        while (stack.isNotEmpty()) {
            val u = stack.pop()
            order[idx++] = u
            for (v in adj[u]) {
                if (v == parent[u]) continue
                parent[v] = u
                stack.push(v)
            }
        }

        val down = LongArray(n)
        val max1 = LongArray(n)
        val max2 = LongArray(n)

        // post-order to compute down values and top two child contributions
        for (i in n - 1 downTo 0) {
            val u = order[i]
            var best1 = 0L
            var best2 = 0L
            for (v in adj[u]) {
                if (parent[v] != u) continue // only children
                val cand = down[v]
                if (cand > best1) {
                    best2 = best1
                    best1 = cand
                } else if (cand > best2) {
                    best2 = cand
                }
            }
            max1[u] = best1
            max2[u] = best2
            var sum = price[u].toLong()
            if (best1 > 0) sum += best1
            down[u] = sum
        }

        val up = LongArray(n)
        up[0] = price[0].toLong()

        // pre-order to compute up values using parent contributions
        for (i in 0 until n) {
            val u = order[i]
            for (v in adj[u]) {
                if (parent[v] != u) continue // only children
                val siblingBest = if (down[v] == max1[u]) max2[u] else max1[u]

                var bestViaNode = up[u] // path through parent side (includes price[u])
                if (siblingBest > 0) {
                    val cand = price[u].toLong() + siblingBest
                    if (cand > bestViaNode) bestViaNode = cand
                }
                up[v] = price[v].toLong() + bestViaNode
            }
        }

        var answer = 0L
        for (i in 0 until n) {
            val bestFromRoot = kotlin.math.max(down[i], up[i])
            val cost = bestFromRoot - price[i]
            if (cost > answer) answer = cost
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maxOutput(int n, List<List<int>> edges, List<int> price) {
    // Build adjacency list
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      adj[u].add(v);
      adj[v].add(u);
    }

    // Parent array and down DP
    List<int> parent = List.filled(n, -1);
    List<int> down = List.filled(n, 0);

    // Iterative post-order DFS to compute down values
    List<int> stackNode = [0];
    List<int> stackParent = [-1];
    List<bool> visited = [false];

    while (stackNode.isNotEmpty) {
      int node = stackNode.removeLast();
      int par = stackParent.removeLast();
      bool vis = visited.removeLast();

      if (!vis) {
        // First time: push back as visited, then children
        stackNode.add(node);
        stackParent.add(par);
        visited.add(true);

        for (int nb in adj[node]) {
          if (nb == par) continue;
          parent[nb] = node;
          stackNode.add(nb);
          stackParent.add(node);
          visited.add(false);
        }
      } else {
        // Compute down[node]
        int best = 0;
        for (int nb in adj[node]) {
          if (nb == par) continue;
          if (down[nb] > best) best = down[nb];
        }
        down[node] = price[node] + best;
      }
    }

    // Reroot DP to compute up contributions and answer
    List<int> up = List.filled(n, 0);
    int answer = 0;

    List<int> stack = [0];
    while (stack.isNotEmpty) {
      int node = stack.removeLast();

      // Find top two maximum down values among children
      int max1 = -1, max2 = -1;
      for (int nb in adj[node]) {
        if (nb == parent[node]) continue;
        int val = down[nb];
        if (val > max1) {
          max2 = max1;
          max1 = val;
        } else if (val > max2) {
          max2 = val;
        }
      }

      // Best neighbor contribution for current node
      int bestNeighbour = up[node];
      if (max1 > bestNeighbour) bestNeighbour = max1;
      if (bestNeighbour > answer) answer = bestNeighbour;

      // Propagate to children
      for (int nb in adj[node]) {
        if (nb == parent[node]) continue;
        int use = (down[nb] == max1) ? max2 : max1;
        int candidate = up[node];
        if (use > candidate) candidate = use;
        if (candidate < 0) candidate = 0; // no other side
        up[nb] = price[node] + candidate;
        stack.add(nb);
      }
    }

    return answer;
  }
}
```

## Golang

```go
func maxOutput(n int, edges [][]int, price []int) int64 {
    if n == 0 {
        return 0
    }
    adj := make([][]int, n)
    for _, e := range edges {
        a, b := e[0], e[1]
        adj[a] = append(adj[a], b)
        adj[b] = append(adj[b], a)
    }

    parent := make([]int, n)
    for i := range parent {
        parent[i] = -1
    }
    order := make([]int, 0, n)

    // iterative DFS to get parent and traversal order
    stack := []int{0}
    parent[0] = -2
    for len(stack) > 0 {
        v := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        order = append(order, v)
        for _, nb := range adj[v] {
            if parent[nb] == -1 {
                parent[nb] = v
                stack = append(stack, nb)
            }
        }
    }

    dpDown := make([]int64, n)
    best1Val := make([]int64, n)
    best2Val := make([]int64, n)
    best1Child := make([]int, n)
    for i := range best1Child {
        best1Child[i] = -1
    }

    // post-order processing to compute dpDown and top two child contributions
    for i := len(order) - 1; i >= 0; i-- {
        v := order[i]
        maxVal := int64(0)
        secondVal := int64(0)
        bestChild := -1
        for _, nb := range adj[v] {
            if parent[nb] != v { // child only
                continue
            }
            cand := dpDown[nb]
            if cand > maxVal {
                secondVal = maxVal
                maxVal = cand
                bestChild = nb
            } else if cand > secondVal {
                secondVal = cand
            }
        }
        best1Val[v] = maxVal
        best2Val[v] = secondVal
        best1Child[v] = bestChild
        if maxVal > 0 {
            dpDown[v] = int64(price[v]) + maxVal
        } else {
            dpDown[v] = int64(price[v])
        }
    }

    up := make([]int64, n)
    up[0] = int64(price[0])

    // preorder traversal to compute up values
    for _, v := range order {
        for _, nb := range adj[v] {
            if parent[nb] != v { // only children
                continue
            }
            var siblingBest int64
            if best1Child[v] == nb {
                siblingBest = best2Val[v]
            } else {
                siblingBest = best1Val[v]
            }

            bestFromParent := up[v] // includes price[v]
            if siblingBest > 0 {
                cand := int64(price[v]) + siblingBest
                if cand > bestFromParent {
                    bestFromParent = cand
                }
            }
            up[nb] = int64(price[nb]) + bestFromParent
        }
    }

    var ans int64 = 0
    for i := 0; i < n; i++ {
        maxDist := dpDown[i]
        if up[i] > maxDist {
            maxDist = up[i]
        }
        diff := maxDist - int64(price[i])
        if diff > ans {
            ans = diff
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_output(n, edges, price)
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  dp = Array.new(n, 0)          # down DP (max sum from node into its subtree, excluding itself)
  max1 = Array.new(n, 0)        # best child contribution
  max2 = Array.new(n, 0)        # second best child contribution
  best_child = Array.new(n, -1) # which child gave max1

  # Post-order traversal to compute dp, max1, max2
  stack = [[0, -1, false]]
  while !stack.empty?
    node, parent, visited = stack.pop
    if visited
      best = 0
      second = 0
      child_best = -1
      adj[node].each do |nbr|
        next if nbr == parent
        val = dp[nbr]
        if val > best
          second = best
          best = val
          child_best = nbr
        elsif val > second
          second = val
        end
      end
      max1[node] = best
      max2[node] = second
      best_child[node] = child_best
      dp[node] = price[node] + (best > 0 ? best : 0)
    else
      stack << [node, parent, true]
      adj[node].each do |nbr|
        next if nbr == parent
        stack << [nbr, node, false]
      end
    end
  end

  up = Array.new(n, 0) # contribution from parent side (excluding current node's price)

  # Pre-order traversal to compute up values
  stack = [[0, -1]]
  while !stack.empty?
    node, parent = stack.pop
    adj[node].each do |nbr|
      next if nbr == parent
      sibling_best = (best_child[node] == nbr) ? max2[node] : max1[node]
      up[nbr] = price[node] + [up[node], sibling_best].max
      stack << [nbr, node]
    end
  end

  ans = 0
  n.times do |i|
    candidate = [max1[i], up[i]].max
    ans = candidate if candidate > ans
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maxOutput(n: Int, edges: Array[Array[Int]], price: Array[Int]): Long = {
        val adj = Array.fill[n](new scala.collection.mutable.ArrayBuffer[Int]())
        for (e <- edges) {
            val a = e(0)
            val b = e(1)
            adj(a) += b
            adj(b) += a
        }
        val priceL = price.map(_.toLong)

        // parent array and post-order traversal
        val parent = Array.fill[Int](n)(-1)
        val order = new scala.collection.mutable.ArrayStack[Int]()
        val stack = new scala.collection.mutable.Stack[(Int, Int)]()
        stack.push((0, 0))
        parent(0) = -2
        while (stack.nonEmpty) {
            val (u, state) = stack.pop()
            if (state == 0) {
                stack.push((u, 1))
                for (v <- adj(u)) {
                    if (parent(v) == -1) {
                        parent(v) = u
                        stack.push((v, 0))
                    }
                }
            } else {
                order.push(u)
            }
        }

        // down DP: max sum starting at node going into its subtree
        val down = Array.fill[Long](n)(0L)
        while (order.nonEmpty) {
            val u = order.pop()
            var bestChildDown = 0L
            for (v <- adj(u)) {
                if (parent(v) == u) {
                    if (down(v) > bestChildDown) bestChildDown = down(v)
                }
            }
            down(u) = priceL(u) + bestChildDown
        }

        // store top two child down values and which child gives the top
        val top1 = Array.fill[Long](n)(0L)
        val top2 = Array.fill[Long](n)(0L)
        val bestChildIdx = Array.fill[Int](n)(-1)
        for (u <- 0 until n) {
            var m1 = 0L
            var m2 = 0L
            var idx = -1
            for (v <- adj(u)) {
                if (parent(v) == u) {
                    val d = down(v)
                    if (d > m1) {
                        m2 = m1
                        m1 = d
                        idx = v
                    } else if (d > m2) {
                        m2 = d
                    }
                }
            }
            top1(u) = m1
            top2(u) = m2
            bestChildIdx(u) = idx
        }

        // up DP: max sum starting at node going outside its subtree
        val up = Array.fill[Long](n)(0L)
        up(0) = priceL(0)

        val stack2 = new scala.collection.mutable.Stack[Int]()
        stack2.push(0)
        while (stack2.nonEmpty) {
            val u = stack2.pop()
            for (v <- adj(u)) {
                if (parent(v) == u) {
                    // best contribution from u excluding child v
                    val siblingBest = if (bestChildIdx(u) == v) top2(u) else top1(u)
                    val viaSibling = if (siblingBest > 0L) priceL(u) + siblingBest else priceL(u)
                    val bestExcl = math.max(up(u), viaSibling)
                    up(v) = priceL(v) + bestExcl
                    stack2.push(v)
                }
            }
        }

        var answer = 0L
        for (i <- 0 until n) {
            val far = math.max(down(i), up(i))
            val diff = far - priceL(i)
            if (diff > answer) answer = diff
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_output(n: i32, edges: Vec<Vec<i32>>, price: Vec<i32>) -> i64 {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n_usize];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }
        let price_i64: Vec<i64> = price.iter().map(|&x| x as i64).collect();

        // initial answer from edges (parent-child case)
        let mut ans: i64 = 0;
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            ans = ans.max(price_i64[u].max(price_i64[v]));
        }

        // parent array and order for post-order traversal
        let mut parent: Vec<usize> = vec![n_usize; n_usize];
        let mut order: Vec<usize> = Vec::with_capacity(n_usize);
        let mut stack: Vec<usize> = Vec::new();
        stack.push(0);
        parent[0] = 0;
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
        let mut dp1: Vec<i64> = vec![0; n_usize]; // includes leaf price
        let mut dp0: Vec<i64> = vec![0; n_usize]; // excludes leaf price

        // process in reverse order (post-order)
        for &u in order.iter().rev() {
            let mut has_child = false;
            // track best two dp0 and dp1 among children
            let mut best0_val: i64 = i64::MIN;
            let mut best0_idx: usize = n_usize;
            let mut second0_val: i64 = i64::MIN;

            let mut best1_val: i64 = i64::MIN;
            let mut best1_idx: usize = n_usize;
            let mut second1_val: i64 = i64::MIN;

            for &v in adj[u].iter() {
                if parent[v] == u {
                    has_child = true;
                    // dp0
                    let val0 = dp0[v];
                    if val0 > best0_val {
                        second0_val = best0_val;
                        best0_val = val0;
                        best0_idx = v;
                    } else if val0 > second0_val {
                        second0_val = val0;
                    }
                    // dp1
                    let val1 = dp1[v];
                    if val1 > best1_val {
                        second1_val = best1_val;
                        best1_val = val1;
                        best1_idx = v;
                    } else if val1 > second1_val {
                        second1_val = val1;
                    }
                }
            }

            if !has_child {
                dp1[u] = price_i64[u];
                dp0[u] = 0;
            } else {
                // compute dp values for u
                dp1[u] = price_i64[u] + best1_val;
                dp0[u] = price_i64[u] + best0_val;

                // candidate combining two different children
                if adj[u].len() >= 2 {
                    let mut cand: i64 = i64::MIN;
                    if best0_idx != best1_idx && best0_idx != n_usize && best1_idx != n_usize {
                        cand = best0_val + best1_val + price_i64[u];
                    } else {
                        // try alternative combinations
                        if best0_idx != n_usize && second1_val != i64::MIN {
                            cand = cand.max(best0_val + second1_val + price_i64[u]);
                        }
                        if second0_val != i64::MIN && best1_idx != n_usize {
                            cand = cand.max(second0_val + best1_val + price_i64[u]);
                        }
                    }
                    if cand > ans {
                        ans = cand;
                    }
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
#lang racket

(define/contract (max-output n edges price)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)
  (let* ((adj (make-vector n '()))
         (add-edge
          (lambda (a b)
            (vector-set! adj a (cons b (vector-ref adj a)))
            (vector-set! adj b (cons a (vector-ref adj b))))))
    ;; build adjacency list
    (for-each (lambda (e) (add-edge (first e) (second e))) edges)

    (define price-vec (list->vector price))
    (define parent (make-vector n -1))
    (define order (make-vector n 0))

    ;; iterative DFS to get preorder and parents
    (let loop ((stack (list 0)) (idx 0))
      (when (null? stack)
        (void))
      (if (null? stack)
          (void)
          (let* ((node (car stack))
                 (rest (cdr stack)))
            (vector-set! order idx node)
            (set! idx (+ idx 1))
            (when (= (vector-ref parent node) -1)
              (vector-set! parent node -2)) ; mark root visited
            (for-each (lambda (nbr)
                        (when (= (vector-ref parent nbr) -1)
                          (vector-set! parent nbr node)
                          (set! stack (cons nbr stack))))
                      (vector-ref adj node))
            (loop rest idx))))

    (define neg-inf -1000000000000)

    ;; compute down values and best child contributions
    (define down (make-vector n 0))
    (define best1 (make-vector n neg-inf))
    (define best2 (make-vector n neg-inf))

    (let loop ((i (- n 1)))
      (when (>= i 0)
        (let* ((node (vector-ref order i))
               (maxc neg-inf)
               (secondc neg-inf))
          (for-each
           (lambda (nbr)
             (when (= (vector-ref parent nbr) node) ; child
               (let ((val (vector-ref down nbr)))
                 (cond [(> val maxc) (set! secondc maxc) (set! maxc val)]
                       [(> val secondc) (set! secondc val)]))))
           (vector-ref adj node))
          (vector-set! best1 node maxc)
          (vector-set! best2 node secondc)
          (if (= maxc neg-inf)
              (vector-set! down node (vector-ref price-vec node))
              (vector-set! down node (+ (vector-ref price-vec node) maxc)))
          (loop (- i 1)))))

    ;; compute up values using preorder
    (define up (make-vector n 0))
    (vector-set! up 0 (vector-ref price-vec 0))

    (let loop ((i 0))
      (when (< i n)
        (let ((node (vector-ref order i)))
          (for-each
           (lambda (nbr)
             (when (= (vector-ref parent nbr) node) ; child
               (define sibling-best
                 (if (= (vector-ref down nbr) (vector-ref best1 node))
                     (vector-ref best2 node)
                     (vector-ref best1 node)))
               (define max-through (vector-ref up node))
               (when (> sibling-best neg-inf)
                 (let ((cand (+ (vector-ref price-vec node) sibling-best)))
                   (when (> cand max-through) (set! max-through cand))))
               (vector-set! up nbr
                            (+ (vector-ref price-vec nbr) max-through))))
           (vector-ref adj node))
          (loop (+ i 1)))))

    ;; final answer: max over nodes of (maxDist - price)
    (let ((ans 0))
      (for ([i (in-range n)])
        (define max-dist (max (vector-ref down i) (vector-ref up i)))
        (define diff (- max-dist (vector-ref price-vec i)))
        (when (> diff ans) (set! ans diff)))
      ans)))
```

## Erlang

```erlang
-spec max_output(N :: integer(), Edges :: [[integer()]], Price :: [integer()]) -> integer().
max_output(N, Edges, Price) ->
    Adj = build_adj(Edges),
    PriceArr = array:from_list(Price),

    {_, A} = bfs(0, Adj, PriceArr),
    {DistA, B} = bfs(A, Adj, PriceArr),
    {DistB, _} = bfs(B, Adj, PriceArr),

    lists:max(
        [ (max(maps:get(I, DistA), maps:get(I, DistB)) - array:get(I, PriceArr))
          || I <- lists:seq(0, N-1) ]).

%% Build adjacency map
build_adj([]) -> #{};
build_adj([[A,B]|Rest]) ->
    Adj1 = maps:update_with(A,
            fun(L) -> [B|L] end,
            [B],
            build_adj(Rest)),
    Adj2 = maps:update_with(B,
            fun(L) -> [A|L] end,
            [A],
            Adj1),
    Adj2.

%% BFS/DFS to compute distances and farthest node
bfs(Source, Adj, PriceArr) ->
    InitDist = array:get(Source, PriceArr),
    bfs_loop([{Source, -1, InitDist}], #{Source => InitDist},
             Source, InitDist, Adj, PriceArr).

bfs_loop([], DistMap, MaxNode, _MaxDist, _Adj, _PriceArr) ->
    {DistMap, MaxNode};
bfs_loop([{U, Par, D}|Rest], DistMap, CurMaxNode, CurMaxDist, Adj, PriceArr) ->
    Neigh = maps:get(U, Adj, []),
    {NewStack, NewDistMap, NewMaxNode, NewMaxDist} =
        lists:foldl(
            fun(V, {StAcc, DistAcc, MNode, MDist}) ->
                if V =/= Par ->
                        Dv = D + array:get(V, PriceArr),
                        St2 = [{V, U, Dv}|StAcc],
                        Dist2 = maps:put(V, Dv, DistAcc),
                        case Dv > MDist of
                            true -> {St2, Dist2, V, Dv};
                            false -> {St2, Dist2, MNode, MDist}
                        end;
                   true ->
                        {StAcc, DistAcc, MNode, MDist}
                end
            end,
            {Rest, DistMap, CurMaxNode, CurMaxDist},
            Neigh),
    bfs_loop(NewStack, NewDistMap, NewMaxNode, NewMaxDist, Adj, PriceArr).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_output(n :: integer, edges :: [[integer]], price :: [integer]) :: integer
  def max_output(n, edges, price) do
    # Build adjacency map
    adj =
      Enum.reduce(edges, %{}, fn [a, b], acc ->
        acc
        |> Map.update(a, [b], &[b | &1])
        |> Map.update(b, [a], &[a | &1])
      end)

    price_arr = :array.from_list(price)

    # First DFS to get parent and order (preorder)
    {parent_arr, preorder} =
      dfs_parent_order(0, n, adj)

    # Postorder list
    postorder = Enum.reverse(preorder)

    # Compute down values
    down_arr = compute_down(postorder, parent_arr, adj, price_arr)

    # Compute top two child down values for each node
    {max1_arr, max2_arr} = compute_top_two(postorder, parent_arr, adj, down_arr)

    # Compute up values using preorder traversal
    up_arr = compute_up(preorder, parent_arr, adj, price_arr, down_arr, max1_arr, max2_arr)

    # Calculate answer
    Enum.reduce(0..(n - 1), 0, fn v, acc ->
      best_down = :array.get(v, down_arr)
      best_up = :array.get(v, up_arr)
      best = if best_down > best_up, do: best_down, else: best_up
      diff = best - :array.get(v, price_arr)
      if diff > acc, do: diff, else: acc
    end)
  end

  # DFS to obtain parent array and preorder traversal list
  defp dfs_parent_order(root, n, adj) do
    parent_arr = :array.new(n, default: -1)
    stack = [{root, -1}]
    {parent_arr, preorder} = dfs_loop(stack, parent_arr, [], adj)
    {parent_arr, Enum.reverse(preorder)} # reverse to get actual preorder (root first)
  end

  defp dfs_loop([], parent_arr, order, _adj), do: {parent_arr, order}
  defp dfs_loop([{v, p} | rest], parent_arr, order, adj) do
    parent_arr = :array.set(v, p, parent_arr)
    neighbors = Map.get(adj, v, [])
    children = Enum.filter(neighbors, fn nb -> nb != p end)
    new_stack = Enum.reduce(children, [{v, p} | rest], fn child, acc -> [{child, v} | acc] end)
    dfs_loop(new_stack, parent_arr, [v | order], adj)
  end

  # Compute down values (max sum starting at node within its subtree)
  defp compute_down(postorder, parent_arr, adj, price_arr) do
    n = :array.size(price_arr)
    down_arr = :array.new(n, default: 0)

    Enum.reduce(postorder, down_arr, fn v, d_arr ->
      p = :array.get(v, parent_arr)
      max_child =
        Map.get(adj, v, [])
        |> Enum.filter(fn nb -> nb != p end)
        |> Enum.map(fn child -> :array.get(child, d_arr) end)
        |> Enum.max(fn -> 0 end)

      down_val = :array.get(v, price_arr) + max_child
      :array.set(v, down_val, d_arr)
    end)
  end

  # Compute for each node the largest and second largest child down values
  defp compute_top_two(postorder, parent_arr, adj, down_arr) do
    n = :array.size(down_arr)
    max1_arr = :array.new(n, default: 0)
    max2_arr = :array.new(n, default: 0)

    {max1_arr, max2_arr} =
      Enum.reduce(postorder, {max1_arr, max2_arr}, fn v, {m1_arr, m2_arr} ->
        p = :array.get(v, parent_arr)
        {first, second} =
          Map.get(adj, v, [])
          |> Enum.filter(fn nb -> nb != p end)
          |> Enum.reduce({0, 0}, fn child, {f, s} ->
            val = :array.get(child, down_arr)
            cond do
              val > f -> {val, f}
              val > s -> {f, val}
              true -> {f, s}
            end
          end)

        {
          :array.set(v, first, m1_arr),
          :array.set(v, second, m2_arr)
        }
      end)

    {max1_arr, max2_arr}
  end

  # Compute up values using preorder traversal
  defp compute_up(preorder, parent_arr, adj, price_arr, down_arr, max1_arr, max2_arr) do
    n = :array.size(price_arr)
    up_arr = :array.new(n, default: 0)

    # root up is its own price
    root = hd(preorder)
    up_arr = :array.set(root, :array.get(root, price_arr), up_arr)

    Enum.reduce(preorder, up_arr, fn v, u_arr ->
      p = :array.get(v, parent_arr)
      neighbors = Map.get(adj, v, [])
      Enum.each(neighbors, fn child ->
        if child != p do
          # sibling best down value excluding this child
          max1 = :array.get(v, max1_arr)
          max2 = :array.get(v, max2_arr)
          child_down = :array.get(child, down_arr)

          sibling_best =
            if child_down == max1 do
              max2
            else
              max1
            end

          price_v = :array.get(v, price_arr)
          up_v = :array.get(v, u_arr)

          best_excluding_child =
            cond do
              up_v > price_v + sibling_best -> up_v
              true -> price_v + sibling_best
            end

          up_child = :array.get(child, price_arr) + best_excluding_child
          u_arr = :array.set(child, up_child, u_arr)
        end
      end)

      u_arr
    end)
  end
end
```

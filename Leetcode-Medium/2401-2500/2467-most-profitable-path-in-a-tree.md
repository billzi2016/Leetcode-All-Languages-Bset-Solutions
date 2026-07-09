# 2467. Most Profitable Path in a Tree

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        int n = amount.size();
        vector<vector<int>> g(n);
        for (auto &e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        vector<int> parent(n, -1), depth(n, 0);
        function<void(int,int)> dfsRoot = [&](int u, int p){
            parent[u] = p;
            for (int v : g[u]) if (v != p) {
                depth[v] = depth[u] + 1;
                dfsRoot(v, u);
            }
        };
        dfsRoot(0, -1);
        
        const int INF = 1e9;
        vector<int> bobTime(n, INF);
        int t = 0;
        for (int cur = bob; cur != -1; cur = parent[cur]) {
            bobTime[cur] = t++;
        }
        
        long long best = LLONG_MIN;
        function<void(int,int,long long)> dfsAlice = [&](int u, int p, long long cur){
            if (depth[u] < bobTime[u]) cur += amount[u];
            else if (depth[u] == bobTime[u]) cur += amount[u] / 2;
            
            bool isLeaf = (u != 0 && g[u].size() == 1);
            if (isLeaf) best = max(best, cur);
            
            for (int v : g[u]) if (v != p) {
                dfsAlice(v, u, cur);
            }
        };
        dfsAlice(0, -1, 0);
        return (int)best;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int mostProfitablePath(int[][] edges, int bob, int[] amount) {
        int n = amount.length;
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }

        // distances from Bob to every node
        int[] bobDist = new int[n];
        Arrays.fill(bobDist, -1);
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(bob);
        bobDist[bob] = 0;
        while (!q.isEmpty()) {
            int cur = q.poll();
            for (int nb : graph[cur]) {
                if (bobDist[nb] == -1) {
                    bobDist[nb] = bobDist[cur] + 1;
                    q.offer(nb);
                }
            }
        }

        long maxProfit = Long.MIN_VALUE;

        // iterative DFS from root
        class State {
            int node, parent, time;
            long sum;
            State(int n, int p, int t, long s) { node=n; parent=p; time=t; sum=s; }
        }
        Deque<State> stack = new ArrayDeque<>();
        stack.push(new State(0, -1, 0, 0L));

        while (!stack.isEmpty()) {
            State st = stack.pop();
            int node = st.node;
            int parent = st.parent;
            int time = st.time;
            long curSum = st.sum;

            if (time < bobDist[node]) {
                curSum += amount[node];
            } else if (time == bobDist[node]) {
                curSum += amount[node] / 2;
            }

            boolean isLeaf = (node != 0 && graph[node].size() == 1);
            if (isLeaf) {
                maxProfit = Math.max(maxProfit, curSum);
            }

            for (int nb : graph[node]) {
                if (nb == parent) continue;
                stack.push(new State(nb, node, time + 1, curSum));
            }
        }

        return (int) maxProfit;
    }
}
```

## Python

```python
class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(300000)
        n = len(amount)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n

        # iterative DFS to set parent and depth (Alice's arrival time)
        stack = [(0, -1)]
        while stack:
            node, par = stack.pop()
            for nb in adj[node]:
                if nb == par:
                    continue
                parent[nb] = node
                depth[nb] = depth[node] + 1
                stack.append((nb, node))

        # Bob's arrival times on his unique path to root
        INF = float('inf')
        bob_time = [INF] * n
        cur = bob
        t = 0
        while cur != -1:
            bob_time[cur] = t
            cur = parent[cur]
            t += 1

        max_profit = -10**18

        def dfs(u, p, cur_sum):
            nonlocal max_profit
            if depth[u] < bob_time[u]:
                cur_sum += amount[u]
            elif depth[u] == bob_time[u]:
                cur_sum += amount[u] // 2
            # else Bob arrived earlier; add nothing

            is_leaf = (u != 0 and len(adj[u]) == 1)
            if is_leaf:
                max_profit = max(max_profit, cur_sum)

            for v in adj[u]:
                if v == p:
                    continue
                dfs(v, u, cur_sum)

        dfs(0, -1, 0)
        return max_profit
```

## Python3

```python
import sys
sys.setrecursionlimit(300000)

class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n

        # DFS to set parent and depth from root (0)
        stack = [(0, -1, 0)]
        while stack:
            node, par, d = stack.pop()
            parent[node] = par
            depth[node] = d
            for nb in adj[node]:
                if nb == par:
                    continue
                stack.append((nb, node, d + 1))

        INF = 10 ** 9
        bob_time = [INF] * n
        cur = bob
        t = 0
        while cur != -1:
            bob_time[cur] = t
            cur = parent[cur]
            t += 1

        def dfs(u, p, alice_t):
            if alice_t < bob_time[u]:
                cur_val = amount[u]
            elif alice_t == bob_time[u]:
                cur_val = amount[u] // 2
            else:
                cur_val = 0

            max_child = -float('inf')
            for v in adj[u]:
                if v == p:
                    continue
                child_res = dfs(v, u, alice_t + 1)
                if child_res > max_child:
                    max_child = child_res

            if max_child == -float('inf'):   # leaf
                return cur_val
            else:
                return cur_val + max_child

        return dfs(0, -1, 0)
```

## C

```c
#include <limits.h>
#include <stdlib.h>

int mostProfitablePath(int** edges, int edgesSize, int* edgesColSize, int bob, int* amount, int amountSize) {
    int n = amountSize;
    // degree count
    int *deg = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        deg[u]++; deg[v]++;
    }
    // adjacency lists
    int **adj = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        adj[i] = (int*)malloc(deg[i] * sizeof(int));
    }
    int *cur = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u][cur[u]++] = v;
        adj[v][cur[v]++] = u;
    }
    free(cur);
    
    // BFS from root to get parent and depth
    int *parent = (int*)malloc(n * sizeof(int));
    int *depth = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        parent[i] = -1;
        depth[i] = -1;
    }
    int *queue = (int*)malloc(n * sizeof(int));
    int qh = 0, qt = 0;
    queue[qt++] = 0;
    depth[0] = 0;
    while (qh < qt) {
        int u = queue[qh++];
        for (int i = 0; i < deg[u]; ++i) {
            int v = adj[u][i];
            if (depth[v] == -1) {
                depth[v] = depth[u] + 1;
                parent[v] = u;
                queue[qt++] = v;
            }
        }
    }
    free(queue);
    
    // Bob's arrival times
    const int INF = 1e9;
    int *bobTime = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) bobTime[i] = INF;
    int curNode = bob;
    int t = 0;
    while (curNode != -1) {
        bobTime[curNode] = t++;
        curNode = parent[curNode];
    }
    
    // Iterative DFS for Alice
    struct Item {int node; int parent; long long sum;};
    struct Item *stack = (struct Item*)malloc(n * sizeof(struct Item));
    int top = 0;
    long long rootAdd = 0;
    if (depth[0] < bobTime[0]) rootAdd = amount[0];
    else if (depth[0] == bobTime[0]) rootAdd = amount[0] / 2;
    stack[top++] = (struct Item){0, -1, rootAdd};
    
    long long best = LLONG_MIN;
    while (top) {
        struct Item curIt = stack[--top];
        int u = curIt.node;
        int p = curIt.parent;
        long long curSum = curIt.sum;
        // leaf check
        if (u != 0 && deg[u] == 1) {
            if (curSum > best) best = curSum;
        }
        for (int i = 0; i < deg[u]; ++i) {
            int v = adj[u][i];
            if (v == p) continue;
            long long add = 0;
            if (depth[v] < bobTime[v]) add = amount[v];
            else if (depth[v] == bobTime[v]) add = amount[v] / 2;
            stack[top++] = (struct Item){v, u, curSum + add};
        }
    }
    
    // free allocated memory
    for (int i = 0; i < n; ++i) free(adj[i]);
    free(adj);
    free(deg);
    free(parent);
    free(depth);
    free(bobTime);
    free(stack);
    
    return (int)best;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private List<int>[] graph;
    private int[] bobDist;
    private int[] amount;
    private const int INF = int.MaxValue / 2;

    private long Dfs(int node, int parent, int time) {
        long contrib;
        if (bobDist[node] == INF) {
            contrib = amount[node];
        } else {
            if (time < bobDist[node]) contrib = amount[node];
            else if (time == bobDist[node]) contrib = amount[node] / 2;
            else contrib = 0;
        }

        long maxChild = long.MinValue;
        foreach (int nei in graph[node]) {
            if (nei == parent) continue;
            long child = Dfs(nei, node, time + 1);
            if (child > maxChild) maxChild = child;
        }

        return maxChild == long.MinValue ? contrib : contrib + maxChild;
    }

    public int MostProfitablePath(int[][] edges, int bob, int[] amount) {
        int n = amount.Length;
        this.amount = amount;

        graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            graph[u].Add(v);
            graph[v].Add(u);
        }

        // Build parent array using BFS from root (0)
        int[] parent = new int[n];
        Array.Fill(parent, -1);
        Queue<int> q = new Queue<int>();
        q.Enqueue(0);
        parent[0] = -2; // sentinel for root
        while (q.Count > 0) {
            int cur = q.Dequeue();
            foreach (int nb in graph[cur]) {
                if (parent[nb] == -1) {
                    parent[nb] = cur;
                    q.Enqueue(nb);
                }
            }
        }

        // Record Bob's arrival times along his unique path to root
        bobDist = new int[n];
        for (int i = 0; i < n; i++) bobDist[i] = INF;

        int node = bob;
        int dist = 0;
        while (node != -2 && node != -1) {
            bobDist[node] = dist;
            node = parent[node];
            dist++;
        }

        long result = Dfs(0, -1, 0);
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @param {number} bob
 * @param {number[]} amount
 * @return {number}
 */
var mostProfitablePath = function(edges, bob, amount) {
    const n = amount.length;
    const adj = Array.from({length: n}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    // Build parent array using iterative DFS/BFS from root 0
    const parent = new Array(n).fill(-1);
    const stack = [0];
    parent[0] = -2; // mark root's parent specially
    while (stack.length) {
        const node = stack.pop();
        for (const nb of adj[node]) {
            if (parent[nb] === -1) {
                parent[nb] = node;
                stack.push(nb);
            }
        }
    }

    // Bob's arrival times; default Infinity (never visited)
    const bobTime = new Array(n).fill(Infinity);
    let cur = bob;
    let t = 0;
    while (cur !== -2 && cur !== -1) {
        bobTime[cur] = t;
        cur = parent[cur];
        t++;
    }

    // DFS for Alice, iterative stack: [node, parent, time, score]
    let maxScore = -Infinity;
    const initScore = (() => {
        if (0 < bobTime[0]) return amount[0];
        if (0 === bobTime[0]) return amount[0] / 2;
        return 0;
    })();
    const st = [[0, -1, 0, initScore]];
    while (st.length) {
        const [node, par, time, score] = st.pop();

        // leaf check (excluding root)
        if (node !== 0 && adj[node].length === 1) {
            if (score > maxScore) maxScore = score;
        }

        for (const nb of adj[node]) {
            if (nb === par) continue;
            const nextTime = time + 1;
            let add = 0;
            if (nextTime < bobTime[nb]) add = amount[nb];
            else if (nextTime === bobTime[nb]) add = amount[nb] / 2;
            // else add stays 0
            st.push([nb, node, nextTime, score + add]);
        }
    }

    return maxScore;
};
```

## Typescript

```typescript
function mostProfitablePath(edges: number[][], bob: number, amount: number[]): number {
    const n = amount.length;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    // Build parent array using BFS from root (0)
    const parent = new Array<number>(n).fill(-1);
    const queue: number[] = [0];
    parent[0] = 0;
    while (queue.length) {
        const cur = queue.shift()!;
        for (const nb of adj[cur]) {
            if (parent[nb] === -1) {
                parent[nb] = cur;
                queue.push(nb);
            }
        }
    }

    // Compute Bob's arrival times to nodes on his path to root
    const INF = Number.MAX_SAFE_INTEGER;
    const bobDist = new Array<number>(n).fill(INF);
    let node = bob;
    let d = 0;
    while (true) {
        bobDist[node] = d;
        if (node === 0) break;
        node = parent[node];
        d++;
    }

    // Iterative DFS for Alice's paths
    let maxProfit = -Infinity;
    const stack: [number, number, number, number][] = [[0, 0, 0, -1]]; // node, time, profitSoFar, parent

    while (stack.length) {
        const [curNode, curTime, curProfit, prev] = stack.pop()!;
        let add = 0;
        if (curTime < bobDist[curNode]) {
            add = amount[curNode];
        } else if (curTime === bobDist[curNode]) {
            add = amount[curNode] / 2;
        }
        const newProfit = curProfit + add;

        const isLeaf = curNode !== 0 && adj[curNode].length === 1;
        if (isLeaf) {
            if (newProfit > maxProfit) maxProfit = newProfit;
        }

        for (const nb of adj[curNode]) {
            if (nb === prev) continue;
            stack.push([nb, curTime + 1, newProfit, curNode]);
        }
    }

    return maxProfit;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @param Integer $bob
     * @param Integer[] $amount
     * @return Integer
     */
    function mostProfitablePath($edges, $bob, $amount) {
        $n = count($amount);
        // build adjacency list
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $graph[$u][] = $v;
            $graph[$v][] = $u;
        }

        // BFS to get parent and depth (Alice's arrival time)
        $parent = array_fill(0, $n, -1);
        $depth  = array_fill(0, $n, 0);
        $queue = new SplQueue();
        $queue->enqueue(0);
        $parent[0] = -2; // sentinel for root
        while (!$queue->isEmpty()) {
            $node = $queue->dequeue();
            foreach ($graph[$node] as $nei) {
                if ($parent[$nei] === -1) {
                    $parent[$nei] = $node;
                    $depth[$nei] = $depth[$node] + 1;
                    $queue->enqueue($nei);
                }
            }
        }

        // compute Bob's arrival time for nodes on his path to root
        $bobTime = array_fill(0, $n, PHP_INT_MAX);
        $cur = $bob;
        $t = 0;
        while ($cur != -2) {
            $bobTime[$cur] = $t;
            $cur = $parent[$cur];
            $t++;
        }

        // DFS to compute maximum profit
        $maxProfit = -PHP_INT_MAX;

        $dfs = function($node, $prev, $time) use (&$graph, &$amount, &$bobTime, &$maxProfit, &$dfs) {
            // contribution at current node
            if ($time < $bobTime[$node]) {
                $cur = $amount[$node];
            } elseif ($time == $bobTime[$node]) {
                $cur = intdiv($amount[$node], 2);
            } else {
                $cur = 0;
            }

            // leaf check (excluding root)
            $isLeaf = ($node != 0 && count($graph[$node]) == 1);

            if ($isLeaf) {
                if ($cur > $maxProfit) $maxProfit = $cur;
                return $cur;
            }

            $bestChild = -PHP_INT_MAX;
            foreach ($graph[$node] as $nei) {
                if ($nei === $prev) continue;
                $childVal = $dfs($nei, $node, $time + 1);
                if ($childVal > $bestChild) $bestChild = $childVal;
            }

            // If node has no children (shouldn't happen except leaf), treat bestChild as 0
            if ($bestChild == -PHP_INT_MAX) $bestChild = 0;

            $total = $cur + $bestChild;
            if ($total > $maxProfit) $maxProfit = $total;
            return $total;
        };

        $dfs(0, -1, 0);
        return $maxProfit;
    }
}
```

## Swift

```swift
class Solution {
    func mostProfitablePath(_ edges: [[Int]], _ bob: Int, _ amount: [Int]) -> Int {
        let n = edges.count + 1
        var graph = Array(repeating: [Int](), count: n)
        for e in edges {
            let u = e[0], v = e[1]
            graph[u].append(v)
            graph[v].append(u)
        }
        
        // parent array using iterative DFS
        var parent = Array(repeating: -1, count: n)
        var stack = [(Int, Int)]()   // (node, parent)
        stack.append((0, -1))
        while let (node, par) = stack.popLast() {
            parent[node] = par
            for nb in graph[node] where nb != par {
                stack.append((nb, node))
            }
        }
        
        // Bob's arrival times
        var bobTime = Array(repeating: Int.max, count: n)
        var cur = bob
        var t = 0
        while cur != -1 {
            bobTime[cur] = t
            cur = parent[cur]
            t += 1
        }
        
        // DFS for Alice (iterative)
        var maxProfit = Int.min
        var stackA = [(Int, Int, Int, Int)]()   // (node, parent, time, profitSoFar)
        stackA.append((0, -1, 0, 0))
        while let (node, par, time, profitSoFar) = stackA.popLast() {
            var profit = profitSoFar
            let bTime = bobTime[node]
            if bTime == Int.max {
                profit += amount[node]
            } else {
                if time < bTime {
                    profit += amount[node]
                } else if time == bTime {
                    profit += amount[node] / 2
                }
            }
            
            // leaf check (excluding root)
            let isLeaf = node != 0 && graph[node].count == 1
            if isLeaf {
                if profit > maxProfit { maxProfit = profit }
                continue
            }
            
            for nb in graph[node] where nb != par {
                stackA.append((nb, node, time + 1, profit))
            }
        }
        
        return maxProfit
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mostProfitablePath(edges: Array<IntArray>, bob: Int, amount: IntArray): Int {
        val n = amount.size
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        // parent and depth from root (Alice's arrival time)
        val parent = IntArray(n) { -1 }
        val depth = IntArray(n)
        val stack = java.util.ArrayDeque<Int>()
        stack.add(0)
        parent[0] = 0
        while (!stack.isEmpty()) {
            val node = stack.removeFirst()
            for (nei in adj[node]) {
                if (parent[nei] == -1) {
                    parent[nei] = node
                    depth[nei] = depth[node] + 1
                    stack.add(nei)
                }
            }
        }

        // Bob's arrival times on his path to root
        val INF = Int.MAX_VALUE / 2
        val bobTime = IntArray(n) { INF }
        var cur = bob
        var t = 0
        while (true) {
            bobTime[cur] = t
            if (cur == 0) break
            cur = parent[cur]
            t++
        }

        var maxProfit = Int.MIN_VALUE

        fun dfs(node: Int, profitSoFar: Int) {
            var profit = profitSoFar
            val aliceDist = depth[node]
            when {
                aliceDist < bobTime[node] -> profit += amount[node]
                aliceDist == bobTime[node] -> profit += amount[node] / 2
                else -> {} // Alice arrives after Bob, gets nothing
            }

            // leaf check (excluding root)
            if (node != 0 && adj[node].size == 1) {
                if (profit > maxProfit) maxProfit = profit
                return
            }

            for (nei in adj[node]) {
                if (nei == parent[node]) continue
                dfs(nei, profit)
            }
        }

        dfs(0, 0)
        return maxProfit
    }
}
```

## Dart

```dart
class Solution {
  int mostProfitablePath(List<List<int>> edges, int bob, List<int> amount) {
    int n = amount.length;
    List<List<int>> g = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      g[u].add(v);
      g[v].add(u);
    }

    // parent and depth from root (node 0)
    List<int> parent = List.filled(n, -1);
    List<int> stack = [0];
    parent[0] = -2; // mark visited
    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      for (int nb in g[node]) {
        if (parent[nb] == -1) {
          parent[nb] = node;
          stack.add(nb);
        }
      }
    }

    const int INF = 1 << 30;
    List<int> bobDist = List.filled(n, INF);

    // record Bob's arrival times along his unique path to root
    int cur = bob;
    int d = 0;
    while (true) {
      bobDist[cur] = d;
      if (cur == 0) break;
      cur = parent[cur];
      d++;
    }

    int ans = -1 << 60; // sufficiently small

    void dfs(int node, int time, int acc, int par) {
      int add = 0;
      if (time < bobDist[node]) {
        add = amount[node];
      } else if (time == bobDist[node]) {
        add = amount[node] ~/ 2;
      }
      int newAcc = acc + add;

      bool isLeaf = node != 0 && g[node].length == 1;
      if (isLeaf) {
        if (newAcc > ans) ans = newAcc;
      }

      for (int nb in g[node]) {
        if (nb == par) continue;
        dfs(nb, time + 1, newAcc, node);
      }
    }

    dfs(0, 0, 0, -1);
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"math"
)

func mostProfitablePath(edges [][]int, bob int, amount []int) int {
	n := len(amount)
	adj := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}

	parent := make([]int, n)
	for i := 0; i < n; i++ {
		parent[i] = -1
	}
	var buildParent func(int, int)
	buildParent = func(u, p int) {
		parent[u] = p
		for _, v := range adj[u] {
			if v == p {
				continue
			}
			buildParent(v, u)
		}
	}
	buildParent(0, -1)

	const INF = 1 << 30
	bobTime := make([]int, n)
	for i := 0; i < n; i++ {
		bobTime[i] = INF
	}
	t := 0
	cur := bob
	for cur != -1 {
		bobTime[cur] = t
		t++
		cur = parent[cur]
	}

	maxProfit := math.MinInt64

	var dfsAlice func(int, int, int) int
	dfsAlice = func(u, p, time int) int {
		profit := 0
		if bobTime[u] > time {
			profit = amount[u]
		} else if bobTime[u] == time {
			profit = amount[u] / 2
		}
		isLeaf := u != 0 && len(adj[u]) == 1
		if isLeaf {
			if profit > maxProfit {
				maxProfit = profit
			}
			return profit
		}
		bestChild := math.MinInt64
		for _, v := range adj[u] {
			if v == p {
				continue
			}
			childProfit := dfsAlice(v, u, time+1)
			if childProfit > bestChild {
				bestChild = childProfit
			}
		}
		total := profit + bestChild
		if total > maxProfit {
			maxProfit = total
		}
		return total
	}

	dfsAlice(0, -1, 0)
	return maxProfit
}
```

## Ruby

```ruby
def most_profitable_path(edges, bob, amount)
  n = amount.length
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  # parent pointers from root (0)
  parent = Array.new(n, -1)
  stack = [0]
  parent[0] = 0
  while !stack.empty?
    node = stack.pop
    adj[node].each do |nei|
      next if parent[nei] != -1
      parent[nei] = node
      stack << nei
    end
  end

  # Bob's arrival times on his unique path to root
  bob_time = Array.new(n, Float::INFINITY)
  t = 0
  cur = bob
  loop do
    bob_time[cur] = t
    break if cur == 0
    cur = parent[cur]
    t += 1
  end

  max_income = [-Float::INFINITY]

  dfs = lambda do |node, par, time, cur_sum|
    bt = bob_time[node]
    add =
      if time < bt
        amount[node]
      elsif time == bt
        amount[node] / 2
      else
        0
      end
    cur_sum += add

    # leaf check (excluding root)
    if node != 0 && adj[node].size == 1
      max_income[0] = [max_income[0], cur_sum].max
    end

    adj[node].each do |nei|
      next if nei == par
      dfs.call(nei, node, time + 1, cur_sum)
    end
  end

  dfs.call(0, -1, 0, 0)
  max_income[0]
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{ArrayBuffer, ArrayDeque}

  def mostProfitablePath(edges: Array[Array[Int]], bob: Int, amount: Array[Int]): Int = {
    val n = amount.length
    val adj = Array.fill(n)(new ArrayBuffer[Int]())
    for (e <- edges) {
      val a = e(0)
      val b = e(1)
      adj(a) += b
      adj(b) += a
    }

    // parent array using BFS from root 0
    val parent = Array.fill(n)(-1)
    val q = new ArrayDeque[Int]()
    q.addLast(0)
    parent(0) = 0
    while (q.nonEmpty) {
      val u = q.removeFirst()
      for (v <- adj(u)) {
        if (parent(v) == -1) {
          parent(v) = u
          q.addLast(v)
        }
      }
    }

    // bob arrival times
    val bobTime = Array.fill(n)(Int.MaxValue)
    var cur = bob
    var t = 0
    while (true) {
      bobTime(cur) = t
      if (cur == 0) {
        // reached root
        break
      }
      cur = parent(cur)
      t += 1
    }

    def contribution(node: Int, time: Int): Int = {
      val bt = bobTime(node)
      if (bt == Int.MaxValue) amount(node)
      else if (time < bt) amount(node)
      else if (time == bt) amount(node) / 2
      else 0
    }

    var answer = Int.MinValue
    // stack for DFS: node, parent, timeFromRoot, accumulated sum (Long)
    val stack = new ArrayDeque[(Int, Int, Int, Long)]()
    val initSum = contribution(0, 0).toLong
    stack.addLast((0, -1, 0, initSum))

    while (stack.nonEmpty) {
      val (node, par, time, sum) = stack.removeLast()
      val isLeaf = node != 0 && adj(node).size == 1
      if (isLeaf) {
        answer = math.max(answer, sum.toInt)
      }
      for (v <- adj(node)) {
        if (v != par) {
          val newTime = time + 1
          val add = contribution(v, newTime)
          stack.addLast((v, node, newTime, sum + add))
        }
      }
    }

    answer
  }

  // Helper to break out of while loop when bob reaches root
  private def break: Nothing = throw new RuntimeException("break")
}
```

## Rust

```rust
impl Solution {
    pub fn most_profitable_path(edges: Vec<Vec<i32>>, bob: i32, amount: Vec<i32>) -> i32 {
        let n = amount.len();
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in edges.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }

        // parent array to trace path from any node to root (0)
        let mut parent: Vec<usize> = vec![usize::MAX; n];
        let mut stack: Vec<usize> = Vec::new();
        parent[0] = 0;
        stack.push(0);
        while let Some(u) = stack.pop() {
            for &v in adj[u].iter() {
                if v != parent[u] {
                    parent[v] = u;
                    stack.push(v);
                }
            }
        }

        // bobDist[i] = steps Bob needs to reach node i (INF if never)
        let mut bob_dist: Vec<i32> = vec![i32::MAX; n];
        let mut cur = bob as usize;
        let mut d: i32 = 0;
        loop {
            bob_dist[cur] = d;
            if cur == 0 { break; }
            cur = parent[cur];
            d += 1;
        }

        let mut ans: i32 = i32::MIN;

        fn dfs(
            u: usize,
            p: usize,
            time: i32,
            sum: i32,
            adj: &Vec<Vec<usize>>,
            amount: &Vec<i32>,
            bob_dist: &Vec<i32>,
            ans: &mut i32,
        ) {
            let mut cur_sum = sum;
            if time < bob_dist[u] {
                cur_sum += amount[u];
            } else if time == bob_dist[u] {
                cur_sum += amount[u] / 2;
            }
            // leaf check (excluding root)
            if u != 0 && adj[u].len() == 1 {
                if cur_sum > *ans {
                    *ans = cur_sum;
                }
            }
            for &v in adj[u].iter() {
                if v != p {
                    dfs(v, u, time + 1, cur_sum, adj, amount, bob_dist, ans);
                }
            }
        }

        dfs(0, usize::MAX, 0, 0, &adj, &amount, &bob_dist, &mut ans);
        ans
    }
}
```

## Racket

```racket
(require racket/vector)
(require racket/list)
(require racket/match)

(define (most-profitable-path edges bob amount)
  (let* ((n (length amount))
         (amt-vec (list->vector amount))
         (adj (make-vector n '())))

    ;; build adjacency list
    (for-each (lambda (e)
                (let ((a (first e))
                      (b (second e)))
                  (vector-set! adj a (cons b (vector-ref adj a)))
                  (vector-set! adj b (cons a (vector-ref adj b)))))
              edges)

    ;; BFS to compute parent and depth from root 0
    (define parent (make-vector n -1))
    (define depth (make-vector n 0))
    (let ((queue (make-vector n 0))
          (head 0)
          (tail 0))
      (vector-set! queue tail 0)
      (set! tail (+ tail 1))
      (vector-set! parent 0 -2) ; mark root as visited
      (let loop ()
        (when (< head tail)
          (let ((node (vector-ref queue head)))
            (set! head (+ head 1))
            (for-each (lambda (nbr)
                        (when (= (vector-ref parent nbr) -1)
                          (vector-set! parent nbr node)
                          (vector-set! depth nbr (+ (vector-ref depth node) 1))
                          (vector-set! queue tail nbr)
                          (set! tail (+ tail 1))))
                      (vector-ref adj node)))
          (loop))))

    ;; Bob's arrival times along his unique path to root
    (define INF (+ n 5))
    (define bob-time (make-vector n INF))
    (let loop ((node bob) (t 0))
      (vector-set! bob-time node t)
      (let ((par (vector-ref parent node)))
        (when (>= par 0)               ; stop when reaching root (-2)
          (loop par (+ t 1)))))

    ;; DFS using explicit stack to evaluate all root‑to‑leaf paths
    (define max-profit (box (- (expt 10 15))))   ; sufficiently negative
    (let ((stack (make-vector n #f))
          (sp 0))
      ;; push initial state: node, parent, current sum
      (vector-set! stack sp (list 0 -1 0))
      (set! sp (+ sp 1))

      (let loop ()
        (when (> sp 0)
          (set! sp (- sp 1))
          (define item (vector-ref stack sp))
          (match-define (list node par cur) item)

          (define a-time (vector-ref depth node))
          (define b-time (vector-ref bob-time node))

          (cond [(< a-time b-time)
                 (set! cur (+ cur (vector-ref amt-vec node)))]
                [(= a-time b-time)
                 (set! cur (+ cur (/ (vector-ref amt-vec node) 2)))])

          (let ((neighbors (vector-ref adj node)))
            (if (and (not (= node 0))
                     (= (length neighbors) 1))   ; leaf
                (when (> cur (unbox max-profit))
                  (set-box! max-profit cur))
                (for-each (lambda (nbr)
                            (when (not (= nbr par))
                              (vector-set! stack sp (list nbr node cur))
                              (set! sp (+ sp 1))))
                          neighbors)))
          (loop)))

      (unbox max-profit))))
```

## Erlang

```erlang
-module(solution).
-export([most_profitable_path/3]).

-spec most_profitable_path(Edges :: [[integer()]], Bob :: integer(), Amount :: [integer()]) -> integer().
most_profitable_path(Edges, Bob, Amount) ->
    N = length(Amount),
    Adj = build_adj(Edges, #{}),

    ParentMap = bfs(queue:in(0, queue:new()), #{0 => -1}, Adj),

    BobTimeMap = bob_time(Bob, 0, ParentMap, #{}),

    AmountArr = array:from_list(Amount),
    INF = N + 5,

    RootBobT = maps:get(0, BobTimeMap, INF),
    RootAmt = array:get(0, AmountArr),
    RootContrib =
        case compare_times(0, RootBobT) of
            less -> RootAmt;
            equal -> RootAmt div 2;
            greater -> 0
        end,

    max_profit([{0, -1, 0, RootContrib}], -1000000000000, Adj, BobTimeMap, AmountArr, INF).

build_adj([], Acc) ->
    Acc;
build_adj([[A, B] | Rest], Acc) ->
    Acc1 = maps:update_with(A,
            fun(L) -> [B | L] end,
            [B],
            Acc),
    Acc2 = maps:update_with(B,
            fun(L) -> [A | L] end,
            [A],
            Acc1),
    build_adj(Rest, Acc2).

bfs(Queue, ParentMap, Adj) ->
    case queue:out(Queue) of
        {empty, _} ->
            ParentMap;
        {{value, Node}, QRest} ->
            Neighs = maps:get(Node, Adj),
            {NewParentMap, NewQ} =
                lists:foldl(fun(Nbr, {PMap, QAcc}) ->
                    case maps:is_key(Nbr, PMap) of
                        true -> {PMap, QAcc};
                        false -> {maps:put(Nbr, Node, PMap), queue:in(Nbr, QAcc)}
                    end
                end, {ParentMap, QRest}, Neighs),
            bfs(NewQ, NewParentMap, Adj)
    end.

bob_time(Node, Time, ParentMap, Acc) ->
    NewAcc = maps:put(Node, Time, Acc),
    case maps:get(Node, ParentMap) of
        -1 -> NewAcc;
        P -> bob_time(P, Time + 1, ParentMap, NewAcc)
    end.

compare_times(A, B) when A < B -> less;
compare_times(A, B) when A == B -> equal;
compare_times(_, _) -> greater.

max_profit([], Max, _Adj, _BobTimeMap, _AmountArr, _INF) ->
    Max;
max_profit([{Node, Parent, ATime, Sum} | Rest], Max, Adj, BobTimeMap, AmountArr, INF) ->
    Children = [C || C <- maps:get(Node, Adj), C =/= Parent],
    NewMax =
        case Children of
            [] -> max(Max, Sum);
            _ -> Max
        end,
    NewStack =
        lists:foldl(fun(Child, AccStack) ->
                NewATime = ATime + 1,
                BobT = maps:get(Child, BobTimeMap, INF),
                Amt = array:get(Child, AmountArr),
                Contrib =
                    case compare_times(NewATime, BobT) of
                        less -> Amt;
                        equal -> Amt div 2;
                        greater -> 0
                    end,
                [{Child, Node, NewATime, Sum + Contrib} | AccStack]
            end, Rest, Children),
    max_profit(NewStack, NewMax, Adj, BobTimeMap, AmountArr, INF).
```

## Elixir

```elixir
defmodule Solution do
  @spec most_profitable_path(edges :: [[integer]], bob :: integer, amount :: [integer]) :: integer
  def most_profitable_path(edges, bob, amount) do
    n = length(amount)

    # Build adjacency list as a map: node => list of neighbors
    adj =
      Enum.reduce(edges, %{}, fn [u, v], acc ->
        acc
        |> Map.update(u, [v], fn lst -> [v | lst] end)
        |> Map.update(v, [u], fn lst -> [u | lst] end)
      end)

    # BFS to compute parent map (rooted at 0)
    {parent, _depth} = bfs_parent(0, adj)

    # Compute Bob's arrival times on his unique path to the root
    bob_dist = compute_bob_dist(bob, parent)

    amount_t = List.to_tuple(amount)

    # Iterative DFS from root to all leaves, tracking max profit
    dfs_iter(adj, amount_t, bob_dist)
  end

  defp bfs_parent(start, adj) do
    parent = %{start => start}
    depth = %{start => 0}
    queue = :queue.from_list([start])
    bfs(parent, depth, queue, adj)
  end

  defp bfs(parent, depth, queue, adj) do
    case :queue.out(queue) do
      {:empty, _} ->
        {parent, depth}

      {{:value, node}, q2} ->
        neigh = Map.get(adj, node, [])
        {parent2, depth2, q3} =
          Enum.reduce(neigh, {parent, depth, q2}, fn nb, {p_acc, d_acc, q_acc} ->
            if Map.has_key?(p_acc, nb) do
              {p_acc, d_acc, q_acc}
            else
              p_new = Map.put(p_acc, nb, node)
              d_new = Map.put(d_acc, nb, Map.get(d_acc, node) + 1)
              q_new = :queue.in(nb, q_acc)
              {p_new, d_new, q_new}
            end
          end)

        bfs(parent2, depth2, q3, adj)
    end
  end

  defp compute_bob_dist(bob, parent) do
    compute_bob_dist(bob, 0, %{}, parent)
  end

  defp compute_bob_dist(node, time, acc, parent) do
    acc = Map.put(acc, node, time)

    if node == 0 do
      acc
    else
      parent_node = Map.get(parent, node)
      compute_bob_dist(parent_node, time + 1, acc, parent)
    end
  end

  defp dfs_iter(adj, amount_t, bob_dist) do
    # stack elements: {node, parent, time_from_root, current_sum}
    init_stack = [{0, -1, 0, 0}]
    go(init_stack, -1_000_000_000, adj, amount_t, bob_dist)
  end

  defp go([], best, _adj, _amount_t, _bob_dist), do: best

  defp go([{node, parent, time, cur_sum} | rest], best, adj, amount_t, bob_dist) do
    contribution =
      case Map.get(bob_dist, node) do
        nil ->
          elem(amount_t, node)

        b when time < b ->
          elem(amount_t, node)

        b when time == b ->
          div(elem(amount_t, node), 2)

        _ ->
          0
      end

    new_sum = cur_sum + contribution
    children = Enum.filter(Map.get(adj, node, []), fn nb -> nb != parent end)

    if children == [] do
      best2 = if new_sum > best, do: new_sum, else: best
      go(rest, best2, adj, amount_t, bob_dist)
    else
      new_stack =
        Enum.reduce(children, rest, fn child, acc ->
          [{child, node, time + 1, new_sum} | acc]
        end)

      go(new_stack, best, adj, amount_t, bob_dist)
    end
  end
end
```

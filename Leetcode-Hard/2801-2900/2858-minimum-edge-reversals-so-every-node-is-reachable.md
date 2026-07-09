# 2858. Minimum Edge Reversals So Every Node Is Reachable

## Cpp

```cpp
class Solution {
public:
    vector<int> minEdgeReversals(int n, vector<vector<int>>& edges) {
        vector<vector<pair<int,int>>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            // original direction u -> v
            adj[u].push_back({v, 0}); // no reversal needed when moving from u to v
            adj[v].push_back({u, 1}); // would need reversal when moving from v to u
        }
        long long rootCost = 0;
        vector<int> parent(n, -1);
        // first DFS to compute cost for node 0 as root
        stack<int> st;
        st.push(0);
        parent[0] = 0;
        while (!st.empty()) {
            int u = st.top(); st.pop();
            for (auto &p : adj[u]) {
                int v = p.first, c = p.second;
                if (v == parent[u]) continue;
                parent[v] = u;
                rootCost += c;
                st.push(v);
            }
        }
        vector<int> ans(n);
        ans[0] = (int)rootCost;
        // second DFS to reroot and compute answers for all nodes
        fill(parent.begin(), parent.end(), -1);
        st.push(0);
        parent[0] = 0;
        while (!st.empty()) {
            int u = st.top(); st.pop();
            for (auto &p : adj[u]) {
                int v = p.first, c = p.second;
                if (v == parent[u]) continue;
                // if edge direction is u->v (c==0), moving root to v adds 1 reversal
                // else (c==1) subtracts 1 reversal
                ans[v] = ans[u] + (c == 0 ? 1 : -1);
                parent[v] = u;
                st.push(v);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] minEdgeReversals(int n, int[][] edges) {
        // Build adjacency list with weight:
        // w = 0 if original direction is from current node to neighbor,
        // w = 1 otherwise (needs reversal when moving away from current).
        @SuppressWarnings("unchecked")
        java.util.ArrayList<int[]>[] graph = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new java.util.ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            graph[u].add(new int[]{v, 0}); // u -> v, no reversal needed when moving from u
            graph[v].add(new int[]{u, 1}); // opposite direction, needs reversal when moving from v
        }

        int[] parent = new int[n];
        java.util.Arrays.fill(parent, -1);
        int[] weightToParent = new int[n]; // weight from parent to this node (0 or 1)
        java.util.Stack<Integer> stack = new java.util.Stack<>();
        stack.push(0);
        parent[0] = -2; // mark visited
        long totalReversals = 0;
        while (!stack.isEmpty()) {
            int u = stack.pop();
            for (int[] edge : graph[u]) {
                int v = edge[0];
                int w = edge[1];
                if (parent[v] == -1) {
                    parent[v] = u;
                    weightToParent[v] = w;
                    totalReversals += w; // when moving from parent to child, count needed reversal
                    stack.push(v);
                }
            }
        }

        int[] answer = new int[n];
        answer[0] = (int) totalReversals;

        // Reroot DP: propagate answers to children
        java.util.Stack<Integer> st2 = new java.util.Stack<>();
        st2.push(0);
        while (!st2.isEmpty()) {
            int u = st2.pop();
            for (int[] edge : graph[u]) {
                int v = edge[0];
                int w = edge[1];
                if (parent[v] == u) { // v is child of u
                    // If original direction is u->v (w==0), moving root to v adds a reversal (+1)
                    // else (w==1) it removes one reversal (-1)
                    answer[v] = answer[u] + (w == 0 ? 1 : -1);
                    st2.push(v);
                }
            }
        }

        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def minEdgeReversals(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            # original direction u -> v has cost 0 when moving from u to v,
            # and cost 1 when moving opposite.
            adj[u].append((v, 0))
            adj[v].append((u, 1))

        import sys
        sys.setrecursionlimit(3000000)

        ans = [0] * n

        def dfs1(u, parent):
            total = 0
            for v, c in adj[u]:
                if v == parent:
                    continue
                total += c + dfs1(v, u)
            return total

        ans[0] = dfs1(0, -1)

        def dfs2(u, parent):
            for v, c in adj[u]:
                if v == parent:
                    continue
                # if edge originally u->v (c==0) we need one extra reversal,
                # otherwise we save one reversal.
                ans[v] = ans[u] + (1 if c == 0 else -1)
                dfs2(v, u)

        dfs2(0, -1)
        return ans
```

## Python3

```python
import sys
from typing import List

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        sys.setrecursionlimit(1 << 25)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            # edge u -> v
            adj[u].append((v, 0))  # correct direction when moving from u outward
            adj[v].append((u, 1))  # opposite direction when moving from v outward

        def dfs1(node: int, parent: int) -> int:
            cnt = 0
            for nb, w in adj[node]:
                if nb == parent:
                    continue
                cnt += w + dfs1(nb, node)
            return cnt

        ans = [0] * n
        ans[0] = dfs1(0, -1)

        def dfs2(node: int, parent: int):
            for nb, w in adj[node]:
                if nb == parent:
                    continue
                # moving root across edge (node, nb)
                if w == 0:      # original direction node -> nb
                    ans[nb] = ans[node] + 1
                else:           # original direction nb -> node
                    ans[nb] = ans[node] - 1
                dfs2(nb, node)

        dfs2(0, -1)
        return ans
```

## C

```c
#include <stdlib.h>

static int *head;
static int *toArr;
static int *costArr;
static int *nextArr;
static int edgeIdx;

static void addEdge(int u, int v, int c) {
    toArr[edgeIdx] = v;
    costArr[edgeIdx] = c;
    nextArr[edgeIdx] = head[u];
    head[u] = edgeIdx++;
}

/* First DFS: compute answer for root 0 */
static void dfs1(int u, int parent, long long *total) {
    for (int e = head[u]; e != -1; e = nextArr[e]) {
        int v = toArr[e];
        if (v == parent) continue;
        *total += costArr[e];
        dfs1(v, u, total);
    }
}

/* Second DFS: reroot and fill answers */
static void dfs2(int u, int parent, int *ans) {
    for (int e = head[u]; e != -1; e = nextArr[e]) {
        int v = toArr[e];
        if (v == parent) continue;
        ans[v] = ans[u] + (costArr[e] == 0 ? 1 : -1);
        dfs2(v, u, ans);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minEdgeReversals(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    head = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;
    
    toArr   = (int*)malloc(2 * edgesSize * sizeof(int));
    costArr = (int*)malloc(2 * edgesSize * sizeof(int));
    nextArr = (int*)malloc(2 * edgesSize * sizeof(int));
    edgeIdx = 0;
    
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        addEdge(u, v, 0); // original direction u->v needs no reversal when moving u->v
        addEdge(v, u, 1); // opposite direction needs one reversal when moving v->u
    }
    
    long long total = 0;
    dfs1(0, -1, &total);
    
    int *answer = (int*)malloc(n * sizeof(int));
    answer[0] = (int)total;
    dfs2(0, -1, answer);
    
    *returnSize = n;
    return answer;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[] MinEdgeReversals(int n, int[][] edges) {
        var adj = new List<(int to, int w)>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<(int, int)>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            adj[u].Add((v, 0)); // edge direction u -> v
            adj[v].Add((u, 1)); // opposite direction when traversed from v to u
        }

        var answer = new int[n];

        // First DFS: compute reversals needed for root 0
        long total = 0;
        var stack = new Stack<(int node, int parent)>();
        stack.Push((0, -1));
        while (stack.Count > 0) {
            var (node, parent) = stack.Pop();
            foreach (var (to, w) in adj[node]) {
                if (to == parent) continue;
                total += w;          // add 1 if edge is opposite to traversal direction
                stack.Push((to, node));
            }
        }
        answer[0] = (int)total;

        // Second DFS: rerooting to compute answers for all nodes
        var stack2 = new Stack<(int node, int parent)>();
        stack2.Push((0, -1));
        while (stack2.Count > 0) {
            var (node, parent) = stack2.Pop();
            foreach (var (to, w) in adj[node]) {
                if (to == parent) continue;
                // w == 0 : edge originally node -> to (good for node, bad for child)
                // w == 1 : edge originally to -> node (bad for node, good for child)
                answer[to] = answer[node] + (w == 0 ? 1 : -1);
                stack2.Push((to, node));
            }
        }

        return answer;
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
var minEdgeReversals = function(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        // edge u -> v is correct when moving from u to v (weight 0)
        adj[u].push([v, 0]);
        // opposite direction needs a reversal (weight 1)
        adj[v].push([u, 1]);
    }

    const parent = new Int32Array(n);
    parent.fill(-1);
    const pw = new Uint8Array(n); // weight of edge from parent to node
    const order = [];
    const stack = [0];
    parent[0] = -2; // mark root as visited

    while (stack.length) {
        const node = stack.pop();
        order.push(node);
        for (const [to, w] of adj[node]) {
            if (parent[to] !== -1) continue;
            parent[to] = node;
            pw[to] = w;
            stack.push(to);
        }
    }

    const dp = new Int32Array(n);
    // post-order accumulation
    for (let i = order.length - 1; i >= 0; --i) {
        const node = order[i];
        if (node === 0) continue;
        const p = parent[node];
        dp[p] += dp[node] + pw[node];
    }

    const answer = new Int32Array(n);
    answer[0] = dp[0];

    // re-rooting using forward order
    for (let i = 1; i < order.length; ++i) {
        const node = order[i];
        const p = parent[node];
        answer[node] = answer[p] + (pw[node] === 0 ? 1 : -1);
    }

    return Array.from(answer);
};
```

## Typescript

```typescript
function minEdgeReversals(n: number, edges: number[][]): number[] {
    const adj: Array<Array<[number, number]>> = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push([v, 0]); // correct direction, no reversal needed when moving u->v
        adj[v].push([u, 1]); // opposite direction, would need a reversal when moving v->u
    }

    const parent = new Int32Array(n);
    parent.fill(-1);

    let totalReversals = 0;
    const stack: number[] = [0];
    while (stack.length) {
        const u = stack.pop()!;
        for (const [to, w] of adj[u]) {
            if (to === parent[u]) continue;
            parent[to] = u;
            totalReversals += w;
            stack.push(to);
        }
    }

    const answer: number[] = new Array(n);
    answer[0] = totalReversals;

    const stack2: number[] = [0];
    while (stack2.length) {
        const u = stack2.pop()!;
        for (const [to, w] of adj[u]) {
            if (to === parent[u]) continue;
            // If edge is originally u->to (w==0), moving root to 'to' adds a reversal.
            // If edge is originally to->u (w==1), moving root to 'to' removes a reversal.
            answer[to] = answer[u] + (w === 0 ? 1 : -1);
            stack2.push(to);
        }
    }

    return answer;
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
    function minEdgeReversals($n, $edges) {
        // Build adjacency list with cost flag:
        // cost = 0 if edge direction matches node -> neighbor,
        // cost = 1 otherwise (needs reversal when moving away from current node).
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $adj[$u][] = [$v, 0]; // u -> v matches direction
            $adj[$v][] = [$u, 1]; // opposite when moving from v to u
        }

        $ans = array_fill(0, $n, 0);

        // First pass: compute answer for node 0 (total reversals needed)
        $rootReversals = 0;
        $stack = [[0, -1]]; // [node, parent]
        while (!empty($stack)) {
            $item = array_pop($stack);
            $node = $item[0];
            $parent = $item[1];
            foreach ($adj[$node] as $edge) {
                $to = $edge[0];
                $cost = $edge[1];
                if ($to === $parent) continue;
                $rootReversals += $cost;
                $stack[] = [$to, $node];
            }
        }
        $ans[0] = $rootReversals;

        // Second pass: reroot DP to compute answers for all nodes
        $stack = [[0, -1]];
        while (!empty($stack)) {
            $item = array_pop($stack);
            $node = $item[0];
            $parent = $item[1];
            foreach ($adj[$node] as $edge) {
                $to = $edge[0];
                $cost = $edge[1];
                if ($to === $parent) continue;
                // If original direction is node -> to (cost == 0), moving root adds a reversal.
                // Otherwise, it removes one reversal.
                if ($cost == 0) {
                    $ans[$to] = $ans[$node] + 1;
                } else {
                    $ans[$to] = $ans[$node] - 1;
                }
                $stack[] = [$to, $node];
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minEdgeReversals(_ n: Int, _ edges: [[Int]]) -> [Int] {
        var adj = Array(repeating: [(to: Int, cost: Int)](), count: n)
        for e in edges {
            let u = e[0], v = e[1]
            adj[u].append((to: v, cost: 0))
            adj[v].append((to: u, cost: 1))
        }
        
        var parent = Array(repeating: -1, count: n)
        var edgeCostToParent = Array(repeating: 0, count: n)
        var order = [Int]()
        var stack = [Int]()
        stack.append(0)
        parent[0] = 0
        
        while let node = stack.popLast() {
            order.append(node)
            for nb in adj[node] {
                if nb.to != parent[node] {
                    parent[nb.to] = node
                    edgeCostToParent[nb.to] = nb.cost
                    stack.append(nb.to)
                }
            }
        }
        
        var dpRoot = 0
        if n > 1 {
            for i in 1..<n {
                dpRoot += edgeCostToParent[i]
            }
        }
        
        var ans = Array(repeating: 0, count: n)
        ans[0] = dpRoot
        
        for node in order {
            for nb in adj[node] {
                let child = nb.to
                if parent[child] == node {
                    ans[child] = ans[node] + (nb.cost == 0 ? 1 : -1)
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
    fun minEdgeReversals(n: Int, edges: Array<IntArray>): IntArray {
        // Build adjacency list with cost:
        // cost = 0 if original direction is from current node to neighbor,
        // cost = 1 otherwise (needs reversal when moving outward from current).
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(Pair(v, 0)) // u -> v correct direction
            adj[v].add(Pair(u, 1)) // moving from v to u would need reversal
        }

        // First pass: root the tree at 0, compute dp (reversals needed for subtree) and answer[0].
        val parent = IntArray(n) { -1 }
        val costToParent = IntArray(n)
        val order = IntArray(n)
        var idx = 0
        val stack = java.util.ArrayDeque<Int>()
        stack.add(0)
        parent[0] = -2 // mark visited root

        while (stack.isNotEmpty()) {
            val u = stack.removeLast()
            order[idx++] = u
            for ((v, cost) in adj[u]) {
                if (parent[v] != -1) continue
                parent[v] = u
                costToParent[v] = cost
                stack.add(v)
            }
        }

        // post-order accumulation
        val dp = IntArray(n)
        for (i in n - 1 downTo 0) {
            val node = order[i]
            val p = parent[node]
            if (p >= 0) {
                dp[p] += dp[node] + costToParent[node]
            }
        }

        // Second pass: reroot to compute answer for all nodes
        val answer = IntArray(n)
        answer[0] = dp[0]
        // reuse stack for BFS/DFS from root
        stack.clear()
        stack.add(0)

        while (stack.isNotEmpty()) {
            val u = stack.removeLast()
            for ((v, cost) in adj[u]) {
                if (parent[v] != u) continue  // ensure v is child of u in rooted tree
                // delta: +1 if edge direction is u->v (cost==0), else -1
                answer[v] = answer[u] + if (cost == 0) 1 else -1
                stack.add(v)
            }
        }

        return answer
    }
}
```

## Dart

```dart
class EdgeInfo {
  int to;
  int cost; // 0 if original direction is from current node to 'to', else 1
  EdgeInfo(this.to, this.cost);
}

class Solution {
  List<int> minEdgeReversals(int n, List<List<int>> edges) {
    List<List<EdgeInfo>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      // original direction u -> v
      adj[u].add(EdgeInfo(v, 0));
      adj[v].add(EdgeInfo(u, 1));
    }

    List<int> answer = List.filled(n, 0);

    // First DFS (iterative) to compute reversals needed when root is 0
    int totalReversals = 0;
    var stack = <List<int>>[[0, -1]];
    while (stack.isNotEmpty) {
      var cur = stack.removeLast();
      int node = cur[0];
      int parent = cur[1];
      for (var e in adj[node]) {
        if (e.to == parent) continue;
        totalReversals += e.cost;
        stack.add([e.to, node]);
      }
    }
    answer[0] = totalReversals;

    // Second DFS to reroot and compute answers for all nodes
    var stack2 = <List<int>>[[0, -1]];
    while (stack2.isNotEmpty) {
      var cur = stack2.removeLast();
      int node = cur[0];
      int parent = cur[1];
      for (var e in adj[node]) {
        if (e.to == parent) continue;
        // If edge from node to child matches original direction (cost 0), moving root adds 1 reversal.
        // Otherwise, it removes a reversal.
        answer[e.to] = answer[node] + (e.cost == 0 ? 1 : -1);
        stack2.add([e.to, node]);
      }
    }

    return answer;
  }
}
```

## Golang

```go
func minEdgeReversals(n int, edges [][]int) []int {
	type Edge struct {
		to int
		w  int // 0 if original direction is from current node to 'to', else 1
	}
	adj := make([][]Edge, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], Edge{v, 0})
		adj[v] = append(adj[v], Edge{u, 1})
	}
	ans := make([]int, n)

	var dfs1 func(int, int) int
	dfs1 = func(node, parent int) int {
		total := 0
		for _, e := range adj[node] {
			if e.to == parent {
				continue
			}
			sub := dfs1(e.to, node)
			total += sub + e.w
		}
		return total
	}
	ans[0] = dfs1(0, -1)

	var dfs2 func(int, int)
	dfs2 = func(node, parent int) {
		for _, e := range adj[node] {
			if e.to == parent {
				continue
			}
			// if edge direction is node->child (w==0), moving root to child adds 1 reversal,
			// otherwise subtracts 1.
			if e.w == 0 {
				ans[e.to] = ans[node] + 1
			} else {
				ans[e.to] = ans[node] - 1
			}
			dfs2(e.to, node)
		}
	}
	dfs2(0, -1)

	return ans
}
```

## Ruby

```ruby
def min_edge_reversals(n, edges)
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    adj[u] << [v, 0]   # original direction u -> v
    adj[v] << [u, 1]   # opposite direction when moving from v to u
  end

  ans = Array.new(n)

  # First DFS: compute reversals needed for root 0
  total = 0
  stack = [[0, -1]]
  while (node_parent = stack.pop)
    node, parent = node_parent
    adj[node].each do |nbr, w|
      next if nbr == parent
      total += w
      stack << [nbr, node]
    end
  end
  ans[0] = total

  # Second DFS: re-rooting to compute answer for all nodes
  stack = [[0, -1]]
  while (node_parent = stack.pop)
    node, parent = node_parent
    adj[node].each do |nbr, w|
      next if nbr == parent
      ans[nbr] = ans[node] + (w == 0 ? 1 : -1)
      stack << [nbr, node]
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  def minEdgeReversals(n: Int, edges: Array[Array[Int]]): Array[Int] = {
    val adj = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    var i = 0
    while (i < edges.length) {
      val u = edges(i)(0)
      val v = edges(i)(1)
      adj(u).append((v, 0)) // edge direction u -> v is correct when moving from u to v
      adj(v).append((u, 1)) // need reversal when moving from v to u
      i += 1
    }

    val answer = new Array[Int](n)

    // First DFS: compute reversals needed for root 0
    var ans0 = 0
    val stack = new scala.collection.mutable.Stack[(Int, Int)]()
    stack.push((0, -1))
    while (stack.nonEmpty) {
      val (node, parent) = stack.pop()
      for ((nei, cost) <- adj(node)) {
        if (nei != parent) {
          ans0 += cost
          stack.push((nei, node))
        }
      }
    }
    answer(0) = ans0

    // Second DFS: reroot DP to compute answers for all nodes
    val stack2 = new scala.collection.mutable.Stack[(Int, Int)]()
    stack2.push((0, -1))
    while (stack2.nonEmpty) {
      val (node, parent) = stack2.pop()
      for ((nei, cost) <- adj(node)) {
        if (nei != parent) {
          // If original edge is node -> nei (cost == 0), moving root to nei adds a reversal (+1)
          // otherwise it removes a needed reversal (-1)
          val delta = if (cost == 0) 1 else -1
          answer(nei) = answer(node) + delta
          stack2.push((nei, node))
        }
      }
    }

    answer
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_edge_reversals(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<(usize, i32)>> = vec![Vec::new(); n_usize];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            // original direction u -> v
            adj[u].push((v, 0)); // no reversal needed when moving u->v
            adj[v].push((u, 1)); // need reversal when moving v->u
        }

        // First DFS to get parent relationship and order
        let mut parent: Vec<usize> = vec![n_usize; n_usize];
        let mut pw: Vec<i32> = vec![0; n_usize]; // cost from parent to node
        let mut order: Vec<usize> = Vec::with_capacity(n_usize);
        let mut stack: Vec<usize> = Vec::new();
        stack.push(0);
        parent[0] = n_usize;
        while let Some(u) = stack.pop() {
            order.push(u);
            for &(v, w) in &adj[u] {
                if v == parent[u] {
                    continue;
                }
                parent[v] = u;
                pw[v] = w;
                stack.push(v);
            }
        }

        // Bottom‑up DP: dp[x] = reversals needed for subtree of x
        let mut dp: Vec<i64> = vec![0; n_usize];
        for &u in order.iter().rev() {
            for &(v, w) in &adj[u] {
                if v == parent[u] {
                    continue;
                }
                dp[u] += dp[v] + w as i64;
            }
        }

        // Rerooting to compute answer for every node
        let mut ans: Vec<i64> = vec![0; n_usize];
        ans[0] = dp[0];
        for &u in order.iter() {
            for &(v, w) in &adj[u] {
                if v == parent[u] {
                    continue;
                }
                // delta = +1 if edge direction is u->v (w==0), else -1
                let delta: i64 = if w == 0 { 1 } else { -1 };
                ans[v] = ans[u] + delta;
            }
        }

        ans.into_iter().map(|x| x as i32).collect()
    }
}
```

## Racket

```racket
(define/contract (min-edge-reversals n edges)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((adj (make-vector n '()))
         ;; build adjacency with direction flag:
         ;; d = 0 if edge goes from current node to neighbor (already correct for outward root)
         ;; d = 1 otherwise (needs reversal when moving outward)
         )
    (for ([e edges])
      (let* ((u (first e))
             (v (second e)))
        (vector-set! adj u (cons (cons v 0) (vector-ref adj u)))
        (vector-set! adj v (cons (cons u 1) (vector-ref adj v)))))
    ;; first DFS to compute total reversals needed for root 0
    (define visited (make-vector n #f))
    (define parent (make-vector n -1))
    (define dir-from-parent (make-vector n 0)) ; not used later but kept for completeness
    (define stack (list 0))
    (vector-set! visited 0 #t)
    (define total 0)
    (let loop ()
      (when (not (null? stack))
        (let* ((node (car stack))
               (rest (cdr stack)))
          (set! stack rest)
          (for ([pair (vector-ref adj node)])
            (let* ((nb (car pair))
                   (d  (cdr pair)))
              (unless (vector-ref visited nb)
                (vector-set! visited nb #t)
                (vector-set! parent nb node)
                (vector-set! dir-from-parent nb d)
                (set! total (+ total d))
                (set! stack (cons nb stack)))))
          (loop))))
    ;; second DFS to reroot and compute answer for each node
    (define ans (make-vector n 0))
    (vector-set! ans 0 total)
    (define stack2 (list 0))
    (let loop2 ()
      (when (not (null? stack2))
        (let* ((x (car stack2))
               (rest (cdr stack2)))
          (set! stack2 rest)
          (for ([pair (vector-ref adj x)])
            (let* ((nb (car pair))
                   (d  (cdr pair)))
              (when (= (vector-ref parent nb) x)
                (if (= d 0)
                    (vector-set! ans nb (+ (vector-ref ans x) 1))
                    (vector-set! ans nb (- (vector-ref ans x) 1)))
                (set! stack2 (cons nb stack2)))))
          (loop2))))
    ;; collect results
    (for/list ([i (in-range n)]) (vector-ref ans i))))
```

## Erlang

```erlang
-module(solution).
-export([min_edge_reversals/2]).

-spec min_edge_reversals(N :: integer(), Edges :: [[integer()]]) -> [integer()].
min_edge_reversals(N, Edges) ->
    Adj = build_adj(Edges, #{}),
    {ParentMap, CostMap, Preorder} = dfs_build(Adj),
    Answer0 = maps:fold(fun(_K, V, Acc) -> Acc + V end, 0, CostMap),
    AnsMap = compute_answers(Preorder, ParentMap, CostMap, Answer0),
    [maps:get(I, AnsMap) || I <- lists:seq(0, N - 1)].

build_adj([], Adj) ->
    Adj;
build_adj([[U, V] | Rest], Adj) ->
    Adj1 = maps:update_with(
        U,
        fun(L) -> [{V, 0} | L] end,
        [{V, 0}],
        Adj),
    Adj2 = maps:update_with(
        V,
        fun(L) -> [{U, 1} | L] end,
        [{U, 1}],
        Adj1),
    build_adj(Rest, Adj2).

dfs_build(Adj) ->
    dfs_build_loop([0], #{0 => -1}, #{}, [], Adj).

dfs_build_loop([], ParentMap, CostMap, OrderAcc, _Adj) ->
    {ParentMap, CostMap, lists:reverse(OrderAcc)};
dfs_build_loop([Node | Stack], ParentMap, CostMap, OrderAcc, Adj) ->
    Neigh = maps:get(Node, Adj, []),
    {NewParent, NewCost, NewStack} =
        lists:foldl(
            fun({Nbr, Cost}, {Pm, Cm, Stk}) ->
                case maps:is_key(Nbr, Pm) of
                    true -> {Pm, Cm, Stk};
                    false ->
                        {
                            maps:put(Nbr, Node, Pm),
                            maps:put(Nbr, Cost, Cm),
                            [Nbr | Stk]
                        }
                end
            end,
            {ParentMap, CostMap, Stack},
            Neigh),
    dfs_build_loop(NewStack, NewParent, NewCost, [Node | OrderAcc], Adj).

compute_answers(Preorder, ParentMap, CostMap, Answer0) ->
    lists:foldl(
        fun(Node, AccMap) ->
            case maps:is_key(Node, AccMap) of
                true -> AccMap;
                false ->
                    Parent = maps:get(Node, ParentMap),
                    EdgeCost = maps:get(Node, CostMap),
                    ParentAns = maps:get(Parent, AccMap),
                    NewAns = ParentAns + (if EdgeCost == 0 -> 1; true -> -1 end),
                    maps:put(Node, NewAns, AccMap)
            end
        end,
        #{0 => Answer0},
        Preorder).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_edge_reversals(n :: integer, edges :: [[integer]]) :: [integer]
  def min_edge_reversals(n, edges) do
    # Build adjacency map: for each node store list of {neighbor, cost}
    # cost = 0 if original edge goes from current node to neighbor, else 1
    adj =
      Enum.reduce(edges, %{}, fn [u, v], acc ->
        acc
        |> Map.update(u, [{v, 0}], fn lst -> [{v, 0} | lst] end)
        |> Map.update(v, [{u, 1}], fn lst -> [{u, 1} | lst] end)
      end)

    # First DFS to get parent relationship and cost from parent to child
    {parent, cost_to_parent, order} = dfs_build(adj)

    # Total reversals needed for root 0
    dp_root =
      Enum.reduce(cost_to_parent, 0, fn {_node, c}, acc -> acc + c end)

    # Second DFS to compute answer for every node using rerooting formula
    ans_map = compute_answers(adj, parent, dp_root)

    # Return answers in order 0..n-1
    Enum.map(0..(n - 1), fn i -> Map.get(ans_map, i) end)
  end

  # Iterative DFS building parent map, cost to parent, and visitation order
  defp dfs_build(adj) do
    stack = [0]
    parent = %{0 => -1}
    cost_to_parent = %{}
    order = []

    dfs_loop(stack, parent, cost_to_parent, order, adj)
  end

  defp dfs_loop([], parent, cost, order, _adj), do: {parent, cost, Enum.reverse(order)}

  defp dfs_loop([v | rest], parent, cost, order, adj) do
    neighbors = Map.get(adj, v, [])

    {parent2, cost2, stack2} =
      Enum.reduce(neighbors, {parent, cost, rest}, fn {to, w},
                                                    {par_acc, cost_acc, stk_acc} ->
        if Map.has_key?(par_acc, to) do
          {par_acc, cost_acc, stk_acc}
        else
          {
            Map.put(par_acc, to, v),
            Map.put(cost_acc, to, w),
            [to | stk_acc]
          }
        end
      end)

    dfs_loop(stack2, parent2, cost2, [v | order], adj)
  end

  # Compute answers using rerooting DP
  defp compute_answers(adj, parent, dp_root) do
    ans = %{0 => dp_root}
    stack = [0]
    compute_loop(stack, adj, parent, ans)
  end

  defp compute_loop([], _adj, _parent, ans), do: ans

  defp compute_loop([v | rest], adj, parent, ans) do
    cur = Map.get(ans, v)

    {ans2, stack2} =
      Enum.reduce(Map.get(adj, v, []), {ans, rest}, fn {to, w},
                                                    {a_acc, stk_acc} ->
        if Map.get(parent, to) == v do
          delta = if w == 0, do: 1, else: -1
          a_new = Map.put(a_acc, to, cur + delta)
          {a_new, [to | stk_acc]}
        else
          {a_acc, stk_acc}
        end
      end)

    compute_loop(stack2, adj, parent, ans2)
  end
end
```

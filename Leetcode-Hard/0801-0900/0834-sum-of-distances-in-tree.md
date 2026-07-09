# 0834. Sum of Distances in Tree

## Cpp

```cpp
class Solution {
public:
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        if (n == 0) return {};
        vector<vector<int>> g(n);
        for (auto& e : edges) {
            int a = e[0], b = e[1];
            g[a].push_back(b);
            g[b].push_back(a);
        }
        vector<int> cnt(n, 1);
        vector<long long> ansLL(n, 0);
        
        function<void(int,int)> dfs1 = [&](int u, int p) {
            for (int v : g[u]) if (v != p) {
                dfs1(v, u);
                cnt[u] += cnt[v];
                ansLL[u] += ansLL[v] + cnt[v];
            }
        };
        dfs1(0, -1);
        
        function<void(int,int)> dfs2 = [&](int u, int p) {
            for (int v : g[u]) if (v != p) {
                ansLL[v] = ansLL[u] - cnt[v] + (n - cnt[v]);
                dfs2(v, u);
            }
        };
        dfs2(0, -1);
        
        vector<int> ans(n);
        for (int i = 0; i < n; ++i) ans[i] = static_cast<int>(ansLL[i]);
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] sumOfDistancesInTree(int n, int[][] edges) {
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        int[] count = new int[n];
        int[] ans = new int[n];
        dfs1(0, -1, graph, count, ans);
        dfs2(0, -1, graph, count, ans, n);
        return ans;
    }

    private void dfs1(int node, int parent, List<Integer>[] graph, int[] count, int[] ans) {
        count[node] = 1;
        for (int nei : graph[node]) {
            if (nei == parent) continue;
            dfs1(nei, node, graph, count, ans);
            count[node] += count[nei];
            ans[0] += count[nei]; // each node in child's subtree is one edge farther from root
        }
    }

    private void dfs2(int node, int parent, List<Integer>[] graph, int[] count, int[] ans, int n) {
        for (int nei : graph[node]) {
            if (nei == parent) continue;
            ans[nei] = ans[node] - count[nei] + (n - count[nei]);
            dfs2(nei, node, graph, count, ans, n);
        }
    }
}
```

## Python

```python
class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        import sys
        sys.setrecursionlimit(1000000)
        if n == 1:
            return [0]

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        count = [1] * n          # size of subtree rooted at node
        ans = [0] * n            # answer for each node

        def dfs1(u, parent):
            for v in adj[u]:
                if v == parent:
                    continue
                dfs1(v, u)
                count[u] += count[v]
                ans[0] += count[v]   # distance from root to nodes in child's subtree increases by 1

        def dfs2(u, parent):
            for v in adj[u]:
                if v == parent:
                    continue
                # when moving root from u to v
                ans[v] = ans[u] - count[v] + (n - count[v])
                dfs2(v, u)

        dfs1(0, -1)
        dfs2(0, -1)
        return ans
```

## Python3

```python
class Solution:
    def sumOfDistancesInTree(self, n: int, edges):
        import sys
        sys.setrecursionlimit(10**6)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        size = [1] * n          # subtree sizes
        dp = [0] * n            # sum of distances from node to nodes in its subtree

        def post(u, p):
            for v in g[u]:
                if v == p:
                    continue
                post(v, u)
                size[u] += size[v]
                dp[u] += dp[v] + size[v]

        post(0, -1)

        ans = [0] * n
        ans[0] = dp[0]

        def pre(u, p):
            for v in g[u]:
                if v == p:
                    continue
                # when moving root from u to v
                ans[v] = ans[u] - size[v] + (n - size[v])
                pre(v, u)

        pre(0, -1)
        return ans
```

## C

```c
#include <stdlib.h>

static int N;
static int **Adj;
static int *Deg;
static int *SubSize;
static int *AnsArr;
static long long rootSum;

static void dfs1(int u, int parent) {
    SubSize[u] = 1;
    for (int i = 0; i < Deg[u]; ++i) {
        int v = Adj[u][i];
        if (v == parent) continue;
        dfs1(v, u);
        SubSize[u] += SubSize[v];
        rootSum += SubSize[v];
    }
}

static void dfs2(int u, int parent) {
    for (int i = 0; i < Deg[u]; ++i) {
        int v = Adj[u][i];
        if (v == parent) continue;
        AnsArr[v] = AnsArr[u] - SubSize[v] + (N - SubSize[v]);
        dfs2(v, u);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumOfDistancesInTree(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    N = n;
    Deg = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        Deg[a]++; Deg[b]++;
    }

    Adj = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        Adj[i] = (int *)malloc(Deg[i] * sizeof(int));
    }

    int *idx = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        Adj[a][idx[a]++] = b;
        Adj[b][idx[b]++] = a;
    }
    free(idx);

    SubSize = (int *)malloc(n * sizeof(int));
    AnsArr  = (int *)malloc(n * sizeof(int));

    rootSum = 0;
    dfs1(0, -1);
    AnsArr[0] = (int)rootSum;
    dfs2(0, -1);

    int *result = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) result[i] = AnsArr[i];
    *returnSize = n;

    // clean up temporary allocations
    free(SubSize);
    free(AnsArr);
    for (int i = 0; i < n; ++i) free(Adj[i]);
    free(Adj);
    free(Deg);

    return result;
}
```

## Csharp

```csharp
public class Solution {
    private List<int>[] graph;
    private int[] subtreeSize;
    private long[] subDistSum;
    private int totalNodes;

    public int[] SumOfDistancesInTree(int n, int[][] edges) {
        if (n == 1) return new int[] { 0 };
        totalNodes = n;
        graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            graph[a].Add(b);
            graph[b].Add(a);
        }

        subtreeSize = new int[n];
        subDistSum = new long[n];
        DfsPost(0, -1);

        int[] answer = new int[n];
        answer[0] = (int)subDistSum[0];
        DfsPre(0, -1, answer);
        return answer;
    }

    private void DfsPost(int node, int parent) {
        subtreeSize[node] = 1;
        foreach (int nei in graph[node]) {
            if (nei == parent) continue;
            DfsPost(nei, node);
            subtreeSize[node] += subtreeSize[nei];
            subDistSum[node] += subDistSum[nei] + subtreeSize[nei];
        }
    }

    private void DfsPre(int node, int parent, int[] answer) {
        foreach (int nei in graph[node]) {
            if (nei == parent) continue;
            // Move root from node to neighbor
            answer[nei] = answer[node] - subtreeSize[nei] + (totalNodes - subtreeSize[nei]);
            DfsPre(nei, node, answer);
        }
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
var sumOfDistancesInTree = function(n, edges) {
    if (n === 1) return [0];
    const graph = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    const parent = new Array(n).fill(-1);
    const order = [];
    const stack = [0];
    parent[0] = -2; // mark root as visited

    while (stack.length) {
        const node = stack.pop();
        order.push(node);
        for (const nei of graph[node]) {
            if (parent[nei] !== -1) continue;
            parent[nei] = node;
            stack.push(nei);
        }
    }

    const sz = new Array(n).fill(1); // subtree sizes
    const dp = new Array(n).fill(0); // sum of distances within subtree

    for (let i = order.length - 1; i >= 0; --i) {
        const node = order[i];
        for (const nei of graph[node]) {
            if (nei === parent[node]) continue;
            sz[node] += sz[nei];
            dp[node] += dp[nei] + sz[nei];
        }
    }

    const ans = new Array(n);
    ans[0] = dp[0];

    for (let i = 0; i < order.length; ++i) {
        const node = order[i];
        for (const nei of graph[node]) {
            if (nei === parent[node]) continue;
            // reroot from node to child nei
            ans[nei] = ans[node] - sz[nei] + (n - sz[nei]);
        }
    }

    return ans;
};
```

## Typescript

```typescript
function sumOfDistancesInTree(n: number, edges: number[][]): number[] {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const size = new Array<number>(n).fill(0);
    const ans = new Array<number>(n).fill(0);

    function dfs1(node: number, parent: number): void {
        size[node] = 1;
        for (const nei of adj[node]) {
            if (nei === parent) continue;
            dfs1(nei, node);
            size[node] += size[nei];
            ans[0] += size[nei]; // distance contribution from root to subtree nodes
        }
    }

    function dfs2(node: number, parent: number): void {
        for (const nei of adj[node]) {
            if (nei === parent) continue;
            ans[nei] = ans[node] - size[nei] + (n - size[nei]);
            dfs2(nei, node);
        }
    }

    if (n > 0) {
        dfs1(0, -1);
        dfs2(0, -1);
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
     * @return Integer[]
     */
    function sumOfDistancesInTree($n, $edges) {
        // Build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            $adj[$a][] = $b;
            $adj[$b][] = $a;
        }

        // subtree sizes and answer array
        $subSize = array_fill(0, $n, 1);
        $ans = array_fill(0, $n, 0);

        // First DFS: compute subtree sizes and ans[0] (sum distances from root)
        $dfs1 = function ($u, $parent) use (&$adj, &$subSize, &$ans, &$dfs1) {
            foreach ($adj[$u] as $v) {
                if ($v === $parent) continue;
                $dfs1($v, $u);
                $subSize[$u] += $subSize[$v];
                $ans[0] += $subSize[$v]; // each node in child subtree is one edge farther from root
            }
        };
        $dfs1(0, -1);

        // Second DFS: reroot to compute answers for all nodes
        $dfs2 = function ($u, $parent) use (&$adj, &$subSize, &$ans, $n, &$dfs2) {
            foreach ($adj[$u] as $v) {
                if ($v === $parent) continue;
                // When moving root from u to v:
                // distances to nodes in v's subtree decrease by 1 (subSize[v] nodes)
                // distances to all other nodes increase by 1 (n - subSize[v] nodes)
                $ans[$v] = $ans[$u] - $subSize[$v] + ($n - $subSize[$v]);
                $dfs2($v, $u);
            }
        };
        $dfs2(0, -1);

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func sumOfDistancesInTree(_ n: Int, _ edges: [[Int]]) -> [Int] {
        if n == 1 { return [0] }
        var graph = [[Int]](repeating: [], count: n)
        for e in edges {
            let a = e[0], b = e[1]
            graph[a].append(b)
            graph[b].append(a)
        }
        var count = [Int](repeating: 1, count: n)
        var ans = [Int](repeating: 0, count: n)

        func dfs(_ node: Int, _ parent: Int) {
            for nei in graph[node] {
                if nei == parent { continue }
                dfs(nei, node)
                count[node] += count[nei]
                ans[0] += count[nei]
            }
        }

        dfs(0, -1)

        func dfs2(_ node: Int, _ parent: Int) {
            for nei in graph[node] {
                if nei == parent { continue }
                ans[nei] = ans[node] - count[nei] + (n - count[nei])
                dfs2(nei, node)
            }
        }

        dfs2(0, -1)

        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumOfDistancesInTree(n: Int, edges: Array<IntArray>): IntArray {
        val graph = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val a = e[0]
            val b = e[1]
            graph[a].add(b)
            graph[b].add(a)
        }
        val size = IntArray(n)
        val ans = IntArray(n)

        fun postOrder(node: Int, parent: Int) {
            size[node] = 1
            for (nei in graph[node]) {
                if (nei == parent) continue
                postOrder(nei, node)
                size[node] += size[nei]
                ans[0] += ans[nei] + size[nei]
            }
        }

        fun preOrder(node: Int, parent: Int) {
            for (nei in graph[node]) {
                if (nei == parent) continue
                ans[nei] = ans[node] - size[nei] + (n - size[nei])
                preOrder(nei, node)
            }
        }

        postOrder(0, -1)
        preOrder(0, -1)

        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> sumOfDistancesInTree(int n, List<List<int>> edges) {
    List<List<int>> graph = List.generate(n, (_) => <int>[]);
    for (var e in edges) {
      int a = e[0];
      int b = e[1];
      graph[a].add(b);
      graph[b].add(a);
    }

    List<int> sz = List.filled(n, 1);
    List<int> ans = List.filled(n, 0);

    void dfs1(int u, int p) {
      for (int v in graph[u]) {
        if (v == p) continue;
        dfs1(v, u);
        sz[u] += sz[v];
        ans[0] += sz[v];
      }
    }

    void dfs2(int u, int p) {
      for (int v in graph[u]) {
        if (v == p) continue;
        ans[v] = ans[u] - sz[v] + (n - sz[v]);
        dfs2(v, u);
      }
    }

    if (n > 0) {
      dfs1(0, -1);
      dfs2(0, -1);
    }
    return ans;
  }
}
```

## Golang

```go
func sumOfDistancesInTree(n int, edges [][]int) []int {
	if n == 1 {
		return []int{0}
	}
	graph := make([][]int, n)
	for _, e := range edges {
		a, b := e[0], e[1]
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}

	count := make([]int, n) // size of subtree rooted at each node
	ans := make([]int, n)   // sum of distances for each node

	var postOrder func(node, parent int)
	postOrder = func(node, parent int) {
		count[node] = 1
		for _, nb := range graph[node] {
			if nb == parent {
				continue
			}
			postOrder(nb, node)
			count[node] += count[nb]
			ans[node] += ans[nb] + count[nb]
		}
	}
	postOrder(0, -1)

	var preOrder func(node, parent int)
	preOrder = func(node, parent int) {
		for _, nb := range graph[node] {
			if nb == parent {
				continue
			}
			ans[nb] = ans[node] - count[nb] + (n - count[nb])
			preOrder(nb, node)
		}
	}
	preOrder(0, -1)

	return ans
}
```

## Ruby

```ruby
def sum_of_distances_in_tree(n, edges)
  graph = Array.new(n) { [] }
  edges.each do |u, v|
    graph[u] << v
    graph[v] << u
  end

  count = Array.new(n, 1)
  ans = Array.new(n, 0)

  dfs = lambda do |node, parent|
    graph[node].each do |nei|
      next if nei == parent
      dfs.call(nei, node)
      count[node] += count[nei]
      ans[node] += ans[nei] + count[nei]
    end
  end

  dfs2 = lambda do |node, parent|
    graph[node].each do |nei|
      next if nei == parent
      ans[nei] = ans[node] - count[nei] + (n - count[nei])
      dfs2.call(nei, node)
    end
  end

  dfs.call(0, -1)
  dfs2.call(0, -1)

  ans
end
```

## Scala

```scala
object Solution {
    def sumOfDistancesInTree(n: Int, edges: Array[Array[Int]]): Array[Int] = {
        val adj = Array.fill(n)(scala.collection.mutable.ArrayBuffer[Int]())
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            adj(u).append(v)
            adj(v).append(u)
        }
        val count = new Array[Int](n)
        val ansLong = new Array[Long](n)

        def post(node: Int, parent: Int): Unit = {
            count(node) = 1
            var sum: Long = 0L
            for (nei <- adj(node)) {
                if (nei != parent) {
                    post(nei, node)
                    count(node) += count(nei)
                    sum += ansLong(nei) + count(nei).toLong
                }
            }
            ansLong(node) = sum
        }

        def pre(node: Int, parent: Int): Unit = {
            for (nei <- adj(node)) {
                if (nei != parent) {
                    ansLong(nei) = ansLong(node) - count(nei).toLong + (n - count(nei)).toLong
                    pre(nei, node)
                }
            }
        }

        post(0, -1)
        pre(0, -1)

        ansLong.map(_.toInt)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_of_distances_in_tree(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n_usize = n as usize;
        let mut adj = vec![Vec::new(); n_usize];
        for e in edges.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }
        let mut cnt = vec![0i32; n_usize];
        let mut ans = vec![0i64; n_usize];

        fn dfs1(
            u: usize,
            parent: usize,
            adj: &Vec<Vec<usize>>,
            cnt: &mut Vec<i32>,
            ans: &mut Vec<i64>,
        ) {
            cnt[u] = 1;
            for &v in &adj[u] {
                if v == parent {
                    continue;
                }
                dfs1(v, u, adj, cnt, ans);
                cnt[u] += cnt[v];
                ans[u] += ans[v] + cnt[v] as i64;
            }
        }

        fn dfs2(
            u: usize,
            parent: usize,
            n: usize,
            adj: &Vec<Vec<usize>>,
            cnt: &Vec<i32>,
            ans: &mut Vec<i64>,
        ) {
            for &v in &adj[u] {
                if v == parent {
                    continue;
                }
                ans[v] = ans[u] - cnt[v] as i64 + (n as i64 - cnt[v] as i64);
                dfs2(v, u, n, adj, cnt, ans);
            }
        }

        if n_usize > 0 {
            dfs1(0, n_usize, &adj, &mut cnt, &mut ans);
            dfs2(0, n_usize, n_usize, &adj, &cnt, &mut ans);
        }

        ans.iter().map(|&x| x as i32).collect()
    }
}
```

## Racket

```racket
(define/contract (sum-of-distances-in-tree n edges)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([adj (make-vector n '())]
         [subtreeSize (make-vector n 0)]
         [answer (make-vector n 0)]
         [total-dist (box 0)])
    ;; build adjacency list
    (for-each (lambda (e)
                (define a (first e))
                (define b (second e))
                (vector-set! adj a (cons b (vector-ref adj a)))
                (vector-set! adj b (cons a (vector-ref adj b))))
              edges)
    ;; first DFS: compute subtree sizes and total distance from root 0
    (letrec ([dfs1 (lambda (u p d)
                     (vector-set! subtreeSize u 1)
                     (set-box! total-dist (+ (unbox total-dist) d))
                     (for ([v (in-list (vector-ref adj u))])
                       (when (not (= v p))
                         (dfs1 v u (+ d 1))
                         (let ([child-size (vector-ref subtreeSize v)])
                           (vector-set! subtreeSize u
                                        (+ (vector-ref subtreeSize u) child-size))))))])
      (dfs1 0 -1 0))
    (vector-set! answer 0 (unbox total-dist))
    ;; second DFS: reroot to compute answers for all nodes
    (letrec ([dfs2 (lambda (u p)
                     (for ([v (in-list (vector-ref adj u))])
                       (when (not (= v p))
                         (let* ([newAns (+ (vector-ref answer u)
                                           (- n (* 2 (vector-ref subtreeSize v))))])
                           (vector-set! answer v newAns)
                           (dfs2 v u)))) )])
      (dfs2 0 -1))
    (vector->list answer)))
```

## Erlang

```erlang
-module(solution).
-export([sum_of_distances_in_tree/2]).

-spec sum_of_distances_in_tree(N :: integer(), Edges :: [[integer()]]) -> [integer()].
sum_of_distances_in_tree(N, Edges) ->
    Adj = build_adj(Edges, #{}),
    SizeTab = ets:new(size_tab, [set, private]),
    DpTab = ets:new(dp_tab, [set, private]),
    AnsTab = ets:new(ans_tab, [set, private]),
    _RootSize = dfs1(0, -1, Adj, SizeTab, DpTab),
    RootAns = ets:lookup_element(DpTab, 0, 2),
    ets:insert(AnsTab, {0, RootAns}),
    dfs2(0, -1, Adj, N, SizeTab, AnsTab),
    [ets:lookup_element(AnsTab, I, 2) || I <- lists:seq(0, N-1)].

build_adj([], Adj) -> Adj;
build_adj([[A,B]|Rest], Adj) ->
    Adj1 = maps:update_with(A,
            fun(L) -> [B|L] end,
            [B],
            Adj),
    Adj2 = maps:update_with(B,
            fun(L) -> [A|L] end,
            [A],
            Adj1),
    build_adj(Rest, Adj2).

dfs1(Node, Parent, Adj, SizeTab, DpTab) ->
    Neigh = maps:get(Node, Adj, []),
    {SizeSum, DpSum} = lists:foldl(
        fun(Child, {SAcc, DAcc}) ->
            if Child == Parent -> {SAcc, DAcc};
               true ->
                   ChildSize = dfs1(Child, Node, Adj, SizeTab, DpTab),
                   ChildDp = ets:lookup_element(DpTab, Child, 2),
                   NewS = SAcc + ChildSize,
                   NewD = DAcc + ChildDp + ChildSize,
                   {NewS, NewD}
            end
        end,
        {0,0},
        Neigh),
    TotalSize = SizeSum + 1,
    ets:insert(SizeTab, {Node, TotalSize}),
    ets:insert(DpTab, {Node, DpSum}),
    TotalSize.

dfs2(Node, Parent, Adj, N, SizeTab, AnsTab) ->
    Neigh = maps:get(Node, Adj, []),
    lists:foreach(
        fun(Child) ->
            if Child == Parent -> ok;
               true ->
                   ParentAns = ets:lookup_element(AnsTab, Node, 2),
                   ChildSize = ets:lookup_element(SizeTab, Child, 2),
                   ChildAns = ParentAns - ChildSize + (N - ChildSize),
                   ets:insert(AnsTab, {Child, ChildAns}),
                   dfs2(Child, Node, Adj, N, SizeTab, AnsTab)
            end
        end,
        Neigh).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_of_distances_in_tree(n :: integer, edges :: [[integer]]) :: [integer]
  def sum_of_distances_in_tree(n, edges) do
    # Build adjacency list using :array for O(1) access
    adj = :array.new(n, default: [])
    adj =
      Enum.reduce(edges, adj, fn [u, v], a ->
        lu = :array.get(u, a)
        lv = :array.get(v, a)

        a = :array.set(u, [v | lu], a)
        :array.set(v, [u | lv], a)
      end)

    # First DFS: compute subtree sizes (cnt) and dp values (sum distances within subtree)
    {cnt_arr, dp_arr} = dfs1(0, -1, adj, :array.new(n, default: 0), :array.new(n, default: 0))

    # Initialize answer array with root's total distance
    ans_root = :array.get(0, dp_arr)
    ans_arr = :array.set(0, ans_root, :array.new(n, default: 0))

    # Second DFS: reroot to compute answers for all nodes
    ans_arr = dfs2(0, -1, adj, n, cnt_arr, ans_arr)

    # Convert result array to list
    Enum.map(0..n - 1, fn i -> :array.get(i, ans_arr) end)
  end

  defp dfs1(node, parent, adj, cnt_arr, dp_arr) do
    # Process children recursively
    {cnt_arr, dp_arr} =
      Enum.reduce(:array.get(node, adj), {cnt_arr, dp_arr}, fn child, {carr, darr} ->
        if child != parent do
          dfs1(child, node, adj, carr, darr)
        else
          {carr, darr}
        end
      end)

    # After children are processed, compute current node's count and dp
    cnt = 1
    dp = 0

    Enum.each(:array.get(node, adj), fn child ->
      if child != parent do
        cnt_child = :array.get(child, cnt_arr)
        dp_child = :array.get(child, dp_arr)

        cnt = cnt + cnt_child
        dp = dp + dp_child + cnt_child
      end
    end)

    cnt_arr = :array.set(node, cnt, cnt_arr)
    dp_arr = :array.set(node, dp, dp_arr)
    {cnt_arr, dp_arr}
  end

  defp dfs2(node, parent, adj, n, cnt_arr, ans_arr) do
    Enum.reduce(:array.get(node, adj), ans_arr, fn child, aarr ->
      if child != parent do
        cnt_child = :array.get(child, cnt_arr)
        ans_node = :array.get(node, aarr)

        ans_child = ans_node - cnt_child + (n - cnt_child)
        aarr2 = :array.set(child, ans_child, aarr)

        dfs2(child, node, adj, n, cnt_arr, aarr2)
      else
        aarr
      end
    end)
  end
end
```

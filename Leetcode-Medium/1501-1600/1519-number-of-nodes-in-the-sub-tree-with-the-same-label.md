# 1519. Number of Nodes in the Sub-Tree With the Same Label

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> countSubTrees(int n, vector<vector<int>>& edges, string labels) {
        vector<vector<int>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vector<int> ans(n);
        function<array<int,26>(int,int)> dfs = [&](int u, int p) -> array<int,26> {
            array<int,26> cnt{};
            cnt.fill(0);
            for (int v : adj[u]) {
                if (v == p) continue;
                auto childCnt = dfs(v, u);
                for (int i = 0; i < 26; ++i) cnt[i] += childCnt[i];
            }
            int idx = labels[u] - 'a';
            cnt[idx]++;               // include current node
            ans[u] = cnt[idx];        // answer for this node
            return cnt;
        };
        dfs(0, -1);
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] countSubTrees(int n, int[][] edges, String labels) {
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }

        int[] parent = new int[n];
        Arrays.fill(parent, -2); // unvisited marker
        List<Integer> order = new ArrayList<>(n);
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        parent[0] = -1;

        while (!stack.isEmpty()) {
            int node = stack.pop();
            order.add(node);
            for (int nei : graph[node]) {
                if (parent[nei] != -2) continue;
                parent[nei] = node;
                stack.push(nei);
            }
        }

        int[][] cnt = new int[n][26];
        int[] ans = new int[n];

        for (int i = order.size() - 1; i >= 0; --i) {
            int node = order.get(i);
            int idx = labels.charAt(node) - 'a';
            cnt[node][idx]++;               // count itself
            ans[node] = cnt[node][idx];     // answer for this node

            int p = parent[node];
            if (p != -1) {
                for (int k = 0; k < 26; ++k) {
                    cnt[p][k] += cnt[node][k];
                }
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        import sys
        sys.setrecursionlimit(200000)

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = [0] * n

        def dfs(node, parent):
            cnt = [0] * 26
            idx = ord(labels[node]) - ord('a')
            cnt[idx] = 1
            for nei in graph[node]:
                if nei == parent:
                    continue
                child_cnt = dfs(nei, node)
                for i in range(26):
                    cnt[i] += child_cnt[i]
            ans[node] = cnt[idx]
            return cnt

        dfs(0, -1)
        return ans
```

## Python3

```python
class Solution:
    def countSubTrees(self, n, edges, labels):
        import sys
        sys.setrecursionlimit(200000)
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = [0] * n

        def dfs(node, parent):
            cnt = [0] * 26
            idx = ord(labels[node]) - ord('a')
            cnt[idx] = 1
            for nei in graph[node]:
                if nei == parent:
                    continue
                child_cnt = dfs(nei, node)
                for i in range(26):
                    cnt[i] += child_cnt[i]
            ans[node] = cnt[idx]
            return cnt

        dfs(0, -1)
        return ans
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countSubTrees(int n, int** edges, int edgesSize, int* edgesColSize, char* labels, int* returnSize) {
    int *ans = (int*)malloc(n * sizeof(int));
    *returnSize = n;
    if (n == 0) return ans;

    // degree of each node
    int *deg = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        deg[u]++; deg[v]++;
    }

    // adjacency list
    int **adj = (int**)malloc(n * sizeof(int*));
    int *pos = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) {
        adj[i] = (int*)malloc(deg[i] * sizeof(int));
    }
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u][pos[u]++] = v;
        adj[v][pos[v]++] = u;
    }

    // parent array and traversal order (preorder)
    int *parent = (int*)malloc(n * sizeof(int));
    int *order  = (int*)malloc(n * sizeof(int));
    int *stack  = (int*)malloc(n * sizeof(int));
    int top = 0, idx = 0;
    stack[top++] = 0;
    parent[0] = -1;

    while (top) {
        int u = stack[--top];
        order[idx++] = u;
        for (int j = 0; j < deg[u]; ++j) {
            int v = adj[u][j];
            if (v == parent[u]) continue;
            parent[v] = u;
            stack[top++] = v;
        }
    }

    // count array: flattened n x 26
    int *cnt = (int*)calloc(n * 26, sizeof(int));

    for (int i = n - 1; i >= 0; --i) {
        int u = order[i];
        int labelIdx = labels[u] - 'a';
        cnt[u * 26 + labelIdx] += 1;
        ans[u] = cnt[u * 26 + labelIdx];

        if (parent[u] != -1) {
            int p = parent[u];
            for (int c = 0; c < 26; ++c) {
                cnt[p * 26 + c] += cnt[u * 26 + c];
            }
        }
    }

    // clean up temporary allocations
    free(deg);
    free(pos);
    for (int i = 0; i < n; ++i) free(adj[i]);
    free(adj);
    free(parent);
    free(order);
    free(stack);
    free(cnt);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] CountSubTrees(int n, int[][] edges, string labels) {
        var graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            graph[a].Add(b);
            graph[b].Add(a);
        }

        var ans = new int[n];
        int[][] cnt = new int[n][];
        var stack = new Stack<(int node, int parent, bool processed)>();
        stack.Push((0, -1, false));

        while (stack.Count > 0) {
            var (node, parent, processed) = stack.Pop();
            if (!processed) {
                stack.Push((node, parent, true));
                foreach (var nb in graph[node]) {
                    if (nb != parent) stack.Push((nb, node, false));
                }
            } else {
                int[] cur = new int[26];
                foreach (var nb in graph[node]) {
                    if (nb == parent) continue;
                    var childArr = cnt[nb];
                    for (int i = 0; i < 26; i++) cur[i] += childArr[i];
                }
                int idx = labels[node] - 'a';
                cur[idx]++;
                ans[node] = cur[idx];
                cnt[node] = cur;
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
 * @param {string} labels
 * @return {number[]}
 */
var countSubTrees = function(n, edges, labels) {
    const adj = Array.from({length: n}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    
    const parent = new Int32Array(n).fill(-1);
    const order = [];
    const stack = [0];
    parent[0] = -2; // mark root visited
    
    while (stack.length) {
        const node = stack.pop();
        order.push(node);
        for (const nb of adj[node]) {
            if (parent[nb] === -1) {
                parent[nb] = node;
                stack.push(nb);
            }
        }
    }
    
    const labelIdx = new Uint8Array(n);
    for (let i = 0; i < n; ++i) {
        labelIdx[i] = labels.charCodeAt(i) - 97;
    }
    
    const freq = Array.from({length: n}, () => new Uint32Array(26));
    const ans = new Int32Array(n);
    
    for (let i = order.length - 1; i >= 0; --i) {
        const node = order[i];
        const arr = freq[node];
        const idx = labelIdx[node];
        arr[idx]++;                     // count itself
        ans[node] = arr[idx];           // result for this node
        
        const p = parent[node];
        if (p >= 0) {                   // merge into parent if not root
            const parArr = freq[p];
            for (let c = 0; c < 26; ++c) {
                parArr[c] += arr[c];
            }
        }
    }
    
    return Array.from(ans);
};
```

## Typescript

```typescript
function countSubTrees(n: number, edges: number[][], labels: string): number[] {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
    }

    const parent = new Int32Array(n);
    parent.fill(-1);
    const order: number[] = [];
    const stack: number[] = [0];
    parent[0] = 0;

    while (stack.length) {
        const node = stack.pop()!;
        order.push(node);
        for (const nb of adj[node]) {
            if (parent[nb] === -1) {
                parent[nb] = node;
                stack.push(nb);
            }
        }
    }

    const counts: Int32Array[] = Array.from({ length: n }, () => new Int32Array(26));
    const ans = new Array<number>(n);

    for (let i = order.length - 1; i >= 0; --i) {
        const node = order[i];
        const cur = counts[node];

        // aggregate children's counts
        for (const nb of adj[node]) {
            if (parent[nb] === node) { // child
                const childArr = counts[nb];
                for (let c = 0; c < 26; ++c) {
                    cur[c] += childArr[c];
                }
            }
        }

        const idx = labels.charCodeAt(node) - 97;
        cur[idx] += 1; // include the node itself
        ans[node] = cur[idx];
    }

    return ans;
}
```

## Php

```php
class Solution {
    private $graph;
    private $labels;
    private $ans;
    private $cnts;

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param String $labels
     * @return Integer[]
     */
    function countSubTrees($n, $edges, $labels) {
        $this->graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $this->graph[$u][] = $v;
            $this->graph[$v][] = $u;
        }
        $this->labels = $labels;
        $this->ans = array_fill(0, $n, 0);
        $this->cnts = [];

        $this->dfs(0, -1);

        return $this->ans;
    }

    private function dfs($node, $parent) {
        $idx = ord($this->labels[$node]) - 97; // 'a' => 97
        $cnt = array_fill(0, 26, 0);
        $cnt[$idx] = 1;

        foreach ($this->graph[$node] as $nei) {
            if ($nei === $parent) continue;
            $this->dfs($nei, $node);
            $childCnt = $this->cnts[$nei];
            for ($i = 0; $i < 26; $i++) {
                $cnt[$i] += $childCnt[$i];
            }
        }

        $this->cnts[$node] = $cnt;
        $this->ans[$node] = $cnt[$idx];
    }
}
```

## Swift

```swift
class Solution {
    func countSubTrees(_ n: Int, _ edges: [[Int]], _ labels: String) -> [Int] {
        var graph = Array(repeating: [Int](), count: n)
        for e in edges {
            let a = e[0], b = e[1]
            graph[a].append(b)
            graph[b].append(a)
        }
        let labelBytes = Array(labels.utf8)
        var ans = Array(repeating: 0, count: n)

        func dfs(_ node: Int, _ parent: Int) -> [Int] {
            var cnt = Array(repeating: 0, count: 26)
            let idx = Int(labelBytes[node] - 97)
            cnt[idx] = 1
            for nb in graph[node] {
                if nb == parent { continue }
                let childCnt = dfs(nb, node)
                for i in 0..<26 {
                    cnt[i] += childCnt[i]
                }
            }
            ans[node] = cnt[idx]
            return cnt
        }

        _ = dfs(0, -1)
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSubTrees(n: Int, edges: Array<IntArray>, labels: String): IntArray {
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val a = e[0]
            val b = e[1]
            adj[a].add(b)
            adj[b].add(a)
        }

        val parent = IntArray(n) { -2 } // -2 means unvisited
        val order = mutableListOf<Int>()
        val stack = java.util.ArrayDeque<Int>()
        stack.push(0)
        parent[0] = -1

        while (stack.isNotEmpty()) {
            val node = stack.pop()
            order.add(node)
            for (nei in adj[node]) {
                if (parent[nei] == -2) {
                    parent[nei] = node
                    stack.push(nei)
                }
            }
        }

        val counts = Array(n) { IntArray(26) }
        val ans = IntArray(n)

        for (i in order.size - 1 downTo 0) {
            val node = order[i]
            val idx = labels[node] - 'a'
            counts[node][idx]++
            ans[node] = counts[node][idx]
            val p = parent[node]
            if (p != -1) {
                for (c in 0 until 26) {
                    counts[p][c] += counts[node][c]
                }
            }
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> countSubTrees(int n, List<List<int>> edges, String labels) {
    // Build adjacency list
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      adj[u].add(v);
      adj[v].add(u);
    }

    // Parent tracking and traversal order (preorder)
    List<int> parent = List.filled(n, -1);
    List<int> order = [];
    List<int> stack = [0];
    parent[0] = -2; // sentinel for root

    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      order.add(node);
      for (int nei in adj[node]) {
        if (nei == parent[node]) continue;
        parent[nei] = node;
        stack.add(nei);
      }
    }

    // Frequency arrays for each subtree
    List<List<int>> freq = List.generate(n, (_) => List.filled(26, 0));
    List<int> answer = List.filled(n, 0);

    // Process nodes in reverse order (post-order aggregation)
    for (int i = order.length - 1; i >= 0; i--) {
      int node = order[i];
      int labelIdx = labels.codeUnitAt(node) - 97;
      freq[node][labelIdx] = 1; // count the node itself

      for (int child in adj[node]) {
        if (child == parent[node]) continue;
        List<int> childFreq = freq[child];
        for (int j = 0; j < 26; j++) {
          freq[node][j] += childFreq[j];
        }
      }

      answer[node] = freq[node][labelIdx];
    }

    return answer;
  }
}
```

## Golang

```go
func countSubTrees(n int, edges [][]int, labels string) []int {
	adj := make([][]int, n)
	for _, e := range edges {
		a, b := e[0], e[1]
		adj[a] = append(adj[a], b)
		adj[b] = append(adj[b], a)
	}
	ans := make([]int, n)
	visited := make([]bool, n)

	var dfs func(int) []int
	dfs = func(u int) []int {
		visited[u] = true
		cnt := make([]int, 26)
		idx := int(labels[u] - 'a')
		cnt[idx] = 1
		for _, v := range adj[u] {
			if !visited[v] {
				childCnt := dfs(v)
				for i := 0; i < 26; i++ {
					cnt[i] += childCnt[i]
				}
			}
		}
		ans[u] = cnt[idx]
		return cnt
	}

	dfs(0)
	return ans
}
```

## Ruby

```ruby
def count_sub_trees(n, edges, labels)
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  parent = Array.new(n, -1)
  order = []
  stack = [[0, -1]]
  while (node_par = stack.pop)
    node, par = node_par
    order << node
    parent[node] = par
    adj[node].each do |nei|
      next if nei == par
      stack << [nei, node]
    end
  end

  freq = Array.new(n) { Array.new(26, 0) }
  ans = Array.new(n, 0)

  order.reverse_each do |node|
    idx = labels.getbyte(node) - 97
    f_node = freq[node]
    f_node[idx] += 1
    ans[node] = f_node[idx]

    p = parent[node]
    if p != -1
      f_parent = freq[p]
      26.times { |i| f_parent[i] += f_node[i] }
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  def countSubTrees(n: Int, edges: Array[Array[Int]], labels: String): Array[Int] = {
    val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
    for (e <- edges) {
      val a = e(0)
      val b = e(1)
      adj(a) += b
      adj(b) += a
    }

    val ans = new Array[Int](n)
    val cnt = Array.ofDim[Int](n, 26)

    val stack = new scala.collection.mutable.Stack[(Int, Int, Boolean)]()
    stack.push((0, -1, false))

    while (stack.nonEmpty) {
      val (node, parent, processed) = stack.pop()
      if (!processed) {
        stack.push((node, parent, true))
        for (nbr <- adj(node)) {
          if (nbr != parent) stack.push((nbr, node, false))
        }
      } else {
        // start with own label
        val idx = labels.charAt(node) - 'a'
        cnt(node)(idx) += 1

        // accumulate children's counts
        for (nbr <- adj(node)) {
          if (nbr != parent) {
            var i = 0
            while (i < 26) {
              cnt(node)(i) += cnt(nbr)(i)
              i += 1
            }
          }
        }

        ans(node) = cnt(node)(idx)
      }
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_sub_trees(n: i32, edges: Vec<Vec<i32>>, labels: String) -> Vec<i32> {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n_usize];
        for e in edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }
        let lbl_bytes = labels.as_bytes();
        let mut ans: Vec<i32> = vec![0; n_usize];
        let mut counts: Vec<[i32; 26]> = vec![[0; 26]; n_usize];

        // stack holds (node, parent, visited_flag)
        let mut stack: Vec<(usize, usize, bool)> = Vec::new();
        stack.push((0, n_usize, false)); // use n as sentinel for no parent

        while let Some((node, parent, visited)) = stack.pop() {
            if !visited {
                // push node again after processing children
                stack.push((node, parent, true));
                for &child in &adj[node] {
                    if child != parent {
                        stack.push((child, node, false));
                    }
                }
            } else {
                let mut cur = [0i32; 26];
                // aggregate children's counts
                for &child in &adj[node] {
                    if child != parent {
                        let child_counts = &counts[child];
                        for i in 0..26 {
                            cur[i] += child_counts[i];
                        }
                    }
                }
                // include current node's label
                let idx = (lbl_bytes[node] - b'a') as usize;
                cur[idx] += 1;
                ans[node] = cur[idx];
                counts[node] = cur;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (count-sub-trees n edges labels)
  (-> exact-integer? (listof (listof exact-integer?)) string? (listof exact-integer?))
  (let* ((adj (make-vector n '()))
         (ans (make-vector n 0)))
    ;; build adjacency list
    (for-each (lambda (e)
                (let ((a (first e))
                      (b (second e)))
                  (vector-set! adj a (cons b (vector-ref adj a)))
                  (vector-set! adj b (cons a (vector-ref adj b)))))
              edges)
    ;; helper to map character to index 0-25
    (define (char-index ch)
      (- (char->integer ch) (char->integer #\a)))
    ;; depth‑first search returning count vector for subtree
    (define (dfs node parent)
      (let ((cnt (make-vector 26 0)))
        (let ((idx (char-index (string-ref labels node))))
          (vector-set! cnt idx 1))
        (for ([nbr (in-list (vector-ref adj node))])
          (when (not (= nbr parent))
            (let ((child-cnt (dfs nbr node)))
              (for ([i (in-range 26)])
                (vector-set! cnt i (+ (vector-ref cnt i)
                                      (vector-ref child-cnt i)))))))
        (let ((idx (char-index (string-ref labels node))))
          (vector-set! ans node (vector-ref cnt idx)))
        cnt))
    (dfs 0 -1)
    (vector->list ans)))
```

## Erlang

```erlang
-spec count_sub_trees(N :: integer(), Edges :: [[integer()]], Labels :: unicode:unicode_binary()) -> [integer()].
count_sub_trees(N, Edges, Labels) ->
    Adj0 = init_adj(N),
    Adj = add_edges(Adj0, Edges),

    % DFS to obtain parent map and preorder list
    {ParentMap, PreOrder} = dfs([{0, -1}], Adj, #{}, []),

    PostOrder = lists:reverse(PreOrder),

    ZeroTuple = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
    ResultMap = process_nodes(PostOrder, Adj, ParentMap, Labels, ZeroTuple, #{}),

    % Build final list in order 0..N-1
    [maps:get(I, ResultMap) || I <- lists:seq(0, N-1)].

%% Initialize adjacency map with empty neighbor lists
init_adj(N) ->
    lists:foldl(fun(I, Acc) -> maps:put(I, [], Acc) end,
                #{},
                lists:seq(0, N-1)).

%% Add all edges to the adjacency map (undirected)
add_edges(Adj, []) -> Adj;
add_edges(Adj, [[A,B]|Rest]) ->
    Adj1 = maps:update_with(A, fun(L) -> [B|L] end, [B], Adj),
    Adj2 = maps:update_with(B, fun(L) -> [A|L] end, [A], Adj1),
    add_edges(Adj2, Rest).

%% Iterative DFS using a stack to collect parent map and preorder traversal
dfs([], _Adj, ParentMap, Order) ->
    {ParentMap, Order};
dfs([{Node, Par}|Stack], Adj, ParentMap, Order) ->
    NewParentMap = maps:put(Node, Par, ParentMap),
    Neigh = maps:get(Node, Adj),
    Children = [C || C <- Neigh, C =/= Par],
    NewStack = [{Child, Node} || Child <- Children] ++ Stack,
    dfs(NewStack, Adj, NewParentMap, [Node|Order]).

%% Process nodes in postorder to compute label counts
process_nodes([], _Adj, _ParentMap, _Labels, _ZeroTuple, ResultMap) ->
    ResultMap;
process_nodes([Node|Rest], Adj, ParentMap, Labels, ZeroTuple, ResultMap) ->
    Par = maps:get(Node, ParentMap),
    Neigh = maps:get(Node, Adj),
    Children = [C || C <- Neigh, C =/= Par],

    % Aggregate children's count tuples
    AggTuple = lists:foldl(fun(Child, Acc) ->
                               ChildTuple = maps:get(Child, ResultMap),
                               add_tuples(Acc, ChildTuple)
                           end,
                           ZeroTuple,
                           Children),

    % Increment for current node's label
    CharCode = binary:at(Labels, Node),
    Index = CharCode - $a,
    FinalTuple = inc(Index, AggTuple),

    Count = element(Index + 1, FinalTuple),
    NewResultMap = maps:put(Node, FinalTuple, ResultMap),
    % Store answer count separately (reuse map for final extraction)
    AnswerMap = maps:put(Node, Count, NewResultMap),

    process_nodes(Rest, Adj, ParentMap, Labels, ZeroTuple, AnswerMap).

%% Add two 26‑element tuples element‑wise
add_tuples(T1, T2) ->
    L1 = tuple_to_list(T1),
    L2 = tuple_to_list(T2),
    list_to_tuple(lists:zipwith(fun(A,B) -> A + B end, L1, L2)).

%% Increment the count at given index (0‑based) in a 26‑element tuple
inc(Index, Tuple) ->
    Pos = Index + 1,
    Val = element(Pos, Tuple) + 1,
    setelement(Pos, Tuple, Val).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_sub_trees(integer, [[integer]], String.t()) :: [integer]
  def count_sub_trees(n, edges, labels) do
    # Build adjacency map
    adj =
      Enum.reduce(edges, %{}, fn [a, b], acc ->
        acc
        |> Map.update(a, [b], fn list -> [b | list] end)
        |> Map.update(b, [a], fn list -> [a | list] end)
      end)

    # Convert labels to indices 0..25
    label_idxs = labels |> String.to_charlist() |> Enum.map(&(&1 - ?a))

    # Parent array: -1 means unvisited
    parent_arr = :array.new(n, default: -1) |> :array.set(0, 0)

    # Get post-order traversal (children before parents)
    {parent_arr, order} = dfs_iter([0], parent_arr, [], adj)

    empty_freq = List.duplicate(0, 26)
    freq_arr = :array.new(n, default: empty_freq)
    ans_arr = :array.new(n, default: 0)

    # Process nodes in post-order
    {final_freq_arr, final_ans_arr} =
      Enum.reduce(order, {freq_arr, ans_arr}, fn node, {farr, aarr} ->
        freq = empty_freq

        freq =
          Enum.reduce(Map.get(adj, node, []), freq, fn nb, acc ->
            if :array.get(nb, parent_arr) == node do
              child_freq = :array.get(nb, farr)
              Enum.zip(acc, child_freq) |> Enum.map(fn {x, y} -> x + y end)
            else
              acc
            end
          end)

        idx = Enum.at(label_idxs, node)
        freq = List.update_at(freq, idx, &(&1 + 1))
        ans = Enum.at(freq, idx)

        farr = :array.set(node, freq, farr)
        aarr = :array.set(node, ans, aarr)
        {farr, aarr}
      end)

    # Build result list
    Enum.map(0..(n - 1), fn i -> :array.get(i, final_ans_arr) end)
  end

  defp dfs_iter([], parent_arr, order, _adj), do: {parent_arr, order}

  defp dfs_iter([node | rest], parent_arr, order, adj) do
    neighbors = Map.get(adj, node, [])

    {new_parent_arr, new_stack} =
      Enum.reduce(neighbors, {parent_arr, rest}, fn nb, {par_acc, stack_acc} ->
        if :array.get(nb, par_acc) == -1 do
          { :array.set(nb, node, par_acc), [nb | stack_acc] }
        else
          {par_acc, stack_acc}
        end
      end)

    dfs_iter(new_stack, new_parent_arr, [node | order], adj)
  end
end
```

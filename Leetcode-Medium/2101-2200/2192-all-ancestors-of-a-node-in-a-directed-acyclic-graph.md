# 2192. All Ancestors of a Node in a Directed Acyclic Graph

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        const int MAXN = 1000; // constraint upper bound
        vector<vector<int>> adj(n);
        vector<int> indeg(n, 0);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            ++indeg[v];
        }
        queue<int> q;
        for (int i = 0; i < n; ++i)
            if (indeg[i] == 0) q.push(i);
        vector<int> topo;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            topo.push_back(u);
            for (int v : adj[u]) {
                if (--indeg[v] == 0) q.push(v);
            }
        }
        vector<bitset<MAXN>> anc(n);
        for (int u : topo) {
            for (int v : adj[u]) {
                anc[v] |= anc[u];
                anc[v].set(u);
            }
        }
        vector<vector<int>> ans(n);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (anc[i].test(j)) ans[i].push_back(j);
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
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        int[] indegree = new int[n];
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            graph[u].add(v);
            indegree[v]++;
        }

        BitSet[] ancestors = new BitSet[n];
        for (int i = 0; i < n; i++) ancestors[i] = new BitSet(n);

        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++) if (indegree[i] == 0) queue.add(i);

        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int v : graph[u]) {
                ancestors[v].or(ancestors[u]);
                ancestors[v].set(u);
                indegree[v]--;
                if (indegree[v] == 0) queue.add(v);
            }
        }

        List<List<Integer>> result = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            List<Integer> list = new ArrayList<>();
            BitSet bs = ancestors[i];
            for (int bit = bs.nextSetBit(0); bit >= 0; bit = bs.nextSetBit(bit + 1)) {
                list.add(bit);
            }
            result.add(list);
        }
        return result;
    }
}
```

## Python

```python
import collections

class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            adj[u].append(v)
            indeg[v] += 1

        q = collections.deque([i for i in range(n) if indeg[i] == 0])
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for nb in adj[node]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    q.append(nb)

        ancestors = [set() for _ in range(n)]
        for node in topo:
            for nb in adj[node]:
                ancestors[nb].add(node)
                ancestors[nb].update(ancestors[node])

        return [sorted(list(s)) for s in ancestors]
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            adj[u].append(v)
            indeg[v] += 1

        q = deque([i for i in range(n) if indeg[i] == 0])
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for nb in adj[node]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    q.append(nb)

        ancestors = [set() for _ in range(n)]
        for u in topo:
            for v in adj[u]:
                ancestors[v].add(u)
                ancestors[v].update(ancestors[u])

        return [sorted(list(s)) for s in ancestors]
```

## C

```c
#include <stdlib.h>
#include <string.h>

int** getAncestors(int n, int** edges, int edgesSize, int* edgesColSize,
                   int* returnSize, int*** returnColumnSizes) {
    // Initialize indegree and adjacency list
    int *indegree = (int *)calloc(n, sizeof(int));
    int **adj = (int **)malloc(n * sizeof(int *));
    int *adjSize = (int *)calloc(n, sizeof(int));
    int *adjCap  = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) {
        adj[i] = NULL;
        adjCap[i] = 0;
    }
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        if (adjSize[u] == adjCap[u]) {
            int newCap = adjCap[u] ? adjCap[u] * 2 : 4;
            adj[u] = (int *)realloc(adj[u], newCap * sizeof(int));
            adjCap[u] = newCap;
        }
        adj[u][adjSize[u]++] = v;
        indegree[v]++;
    }

    // Topological order using Kahn's algorithm
    int *queue = (int *)malloc(n * sizeof(int));
    int qh = 0, qt = 0;
    for (int i = 0; i < n; ++i) {
        if (indegree[i] == 0) queue[qt++] = i;
    }

    // Ancestor matrix
    char **anc = (char **)malloc(n * sizeof(char *));
    for (int i = 0; i < n; ++i) anc[i] = (char *)calloc(n, sizeof(char));

    while (qh < qt) {
        int u = queue[qh++];
        for (int idx = 0; idx < adjSize[u]; ++idx) {
            int v = adj[u][idx];
            // direct ancestor
            anc[v][u] = 1;
            // propagate ancestors from u to v
            for (int k = 0; k < n; ++k) {
                if (anc[u][k]) anc[v][k] = 1;
            }
            indegree[v]--;
            if (indegree[v] == 0) queue[qt++] = v;
        }
    }

    // Build result
    *returnSize = n;
    int **colSizesPtr = (int **)malloc(sizeof(int *));
    *colSizesPtr = (int *)malloc(n * sizeof(int));
    int *colSizes = *colSizesPtr;
    int **result = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        int cnt = 0;
        for (int j = 0; j < n; ++j) if (anc[i][j]) cnt++;
        colSizes[i] = cnt;
        if (cnt == 0) {
            result[i] = NULL;
        } else {
            int *arr = (int *)malloc(cnt * sizeof(int));
            int pos = 0;
            for (int j = 0; j < n; ++j) {
                if (anc[i][j]) arr[pos++] = j;
            }
            result[i] = arr;
        }
    }

    // Cleanup
    free(indegree);
    free(queue);
    for (int i = 0; i < n; ++i) {
        free(adj[i]);
        free(anc[i]);
    }
    free(adj);
    free(adjSize);
    free(adjCap);
    free(anc);

    *returnColumnSizes = colSizes;
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> GetAncestors(int n, int[][] edges) {
        var adj = new List<int>[n];
        var indeg = new int[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            int u = e[0], v = e[1];
            adj[u].Add(v);
            indeg[v]++;
        }

        var queue = new Queue<int>();
        for (int i = 0; i < n; i++) if (indeg[i] == 0) queue.Enqueue(i);

        var topo = new List<int>(n);
        while (queue.Count > 0) {
            int u = queue.Dequeue();
            topo.Add(u);
            foreach (var v in adj[u]) {
                indeg[v]--;
                if (indeg[v] == 0) queue.Enqueue(v);
            }
        }

        var ancestors = new HashSet<int>[n];
        for (int i = 0; i < n; i++) ancestors[i] = new HashSet<int>();

        foreach (var u in topo) {
            foreach (var v in adj[u]) {
                ancestors[v].Add(u);
                foreach (var a in ancestors[u]) {
                    ancestors[v].Add(a);
                }
            }
        }

        IList<IList<int>> result = new List<IList<int>>(n);
        for (int i = 0; i < n; i++) {
            var list = new List<int>(ancestors[i]);
            list.Sort();
            result.Add(list);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[][]}
 */
var getAncestors = function(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    const indeg = new Array(n).fill(0);
    for (const [u, v] of edges) {
        adj[u].push(v);
        indeg[v]++;
    }
    
    // Kahn's algorithm for topological order
    const queue = [];
    for (let i = 0; i < n; i++) {
        if (indeg[i] === 0) queue.push(i);
    }
    let qIdx = 0;
    const topo = [];
    while (qIdx < queue.length) {
        const node = queue[qIdx++];
        topo.push(node);
        for (const nb of adj[node]) {
            indeg[nb]--;
            if (indeg[nb] === 0) queue.push(nb);
        }
    }
    
    // ancestors sets
    const ancSets = Array.from({ length: n }, () => new Set());
    
    for (const node of topo) {
        for (const nb of adj[node]) {
            ancSets[nb].add(node);
            for (const a of ancSets[node]) {
                ancSets[nb].add(a);
            }
        }
    }
    
    const result = [];
    for (let i = 0; i < n; i++) {
        const arr = Array.from(ancSets[i]);
        arr.sort((a, b) => a - b);
        result.push(arr);
    }
    return result;
};
```

## Typescript

```typescript
function getAncestors(n: number, edges: number[][]): number[][] {
    const adj: number[][] = Array.from({ length: n }, () => []);
    const indeg: number[] = new Array<number>(n).fill(0);
    for (const [u, v] of edges) {
        adj[u].push(v);
        indeg[v]++;
    }

    const queue: number[] = [];
    for (let i = 0; i < n; i++) {
        if (indeg[i] === 0) queue.push(i);
    }

    const order: number[] = [];
    let qIdx = 0;
    while (qIdx < queue.length) {
        const node = queue[qIdx++];
        order.push(node);
        for (const nb of adj[node]) {
            indeg[nb]--;
            if (indeg[nb] === 0) queue.push(nb);
        }
    }

    const ancestors: Set<number>[] = Array.from({ length: n }, () => new Set<number>());
    for (const node of order) {
        for (const nb of adj[node]) {
            ancestors[nb].add(node);
            for (const a of ancestors[node]) {
                ancestors[nb].add(a);
            }
        }
    }

    const result: number[][] = Array.from({ length: n }, () => []);
    for (let i = 0; i < n; i++) {
        const arr = Array.from(ancestors[i]);
        arr.sort((a, b) => a - b);
        result[i] = arr;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer[][]
     */
    function getAncestors($n, $edges) {
        // Build adjacency list and indegree array
        $adj = array_fill(0, $n, []);
        $indeg = array_fill(0, $n, 0);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $adj[$u][] = $v;
            $indeg[$v]++;
        }

        // Kahn's algorithm for topological order
        $queue = new SplQueue();
        for ($i = 0; $i < $n; $i++) {
            if ($indeg[$i] == 0) {
                $queue->enqueue($i);
            }
        }

        $topo = [];
        while (!$queue->isEmpty()) {
            $u = $queue->dequeue();
            $topo[] = $u;
            foreach ($adj[$u] as $v) {
                $indeg[$v]--;
                if ($indeg[$v] == 0) {
                    $queue->enqueue($v);
                }
            }
        }

        // Ancestors sets for each node
        $ancestors = array_fill(0, $n, []);
        foreach ($topo as $node) {
            foreach ($adj[$node] as $nbr) {
                // direct parent
                $ancestors[$nbr][$node] = true;
                // inherit ancestors from current node
                foreach ($ancestors[$node] as $a => $_) {
                    $ancestors[$nbr][$a] = true;
                }
            }
        }

        // Convert sets to sorted lists
        $result = [];
        for ($i = 0; $i < $n; $i++) {
            if (empty($ancestors[$i])) {
                $result[] = [];
            } else {
                $list = array_keys($ancestors[$i]);
                sort($list, SORT_NUMERIC);
                $result[] = $list;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func getAncestors(_ n: Int, _ edges: [[Int]]) -> [[Int]] {
        var adj = [[Int]](repeating: [], count: n)
        var indegree = [Int](repeating: 0, count: n)
        for e in edges {
            let u = e[0], v = e[1]
            adj[u].append(v)
            indegree[v] += 1
        }
        
        var queue = [Int]()
        for i in 0..<n where indegree[i] == 0 {
            queue.append(i)
        }
        var head = 0
        
        var ancestors = [Set<Int>](repeating: Set<Int>(), count: n)
        
        while head < queue.count {
            let u = queue[head]
            head += 1
            for v in adj[u] {
                // add u as ancestor of v
                ancestors[v].insert(u)
                // merge ancestors of u into v's set
                ancestors[v].formUnion(ancestors[u])
                
                indegree[v] -= 1
                if indegree[v] == 0 {
                    queue.append(v)
                }
            }
        }
        
        var result = [[Int]]()
        for i in 0..<n {
            let sortedAncestors = ancestors[i].sorted()
            result.append(sortedAncestors)
        }
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque
import java.util.TreeSet

class Solution {
    fun getAncestors(n: Int, edges: Array<IntArray>): List<List<Int>> {
        val adj = MutableList(n) { mutableListOf<Int>() }
        val indeg = IntArray(n)
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            indeg[v]++
        }

        val queue: ArrayDeque<Int> = ArrayDeque()
        for (i in 0 until n) {
            if (indeg[i] == 0) queue.add(i)
        }

        val topo = mutableListOf<Int>()
        while (!queue.isEmpty()) {
            val cur = queue.removeFirst()
            topo.add(cur)
            for (nei in adj[cur]) {
                indeg[nei]--
                if (indeg[nei] == 0) queue.add(nei)
            }
        }

        val ancestors = Array(n) { TreeSet<Int>() }

        for (node in topo) {
            for (nei in adj[node]) {
                ancestors[nei].add(node)
                ancestors[nei].addAll(ancestors[node])
            }
        }

        val result = mutableListOf<List<Int>>()
        for (i in 0 until n) {
            result.add(ArrayList(ancestors[i]))
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> getAncestors(int n, List<List<int>> edges) {
    // Build adjacency list and indegree array
    List<List<int>> graph = List.generate(n, (_) => []);
    List<int> indegree = List.filled(n, 0);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      graph[u].add(v);
      indegree[v]++;
    }

    // Kahn's algorithm for topological order
    List<int> queue = [];
    for (int i = 0; i < n; i++) {
      if (indegree[i] == 0) queue.add(i);
    }
    int qIdx = 0;
    List<int> topo = [];
    while (qIdx < queue.length) {
      int node = queue[qIdx++];
      topo.add(node);
      for (int nb in graph[node]) {
        indegree[nb]--;
        if (indegree[nb] == 0) queue.add(nb);
      }
    }

    // Ancestor sets
    List<Set<int>> anc = List.generate(n, (_) => <int>{});
    for (int node in topo) {
      for (int nb in graph[node]) {
        anc[nb].add(node);
        anc[nb].addAll(anc[node]);
      }
    }

    // Convert sets to sorted lists
    List<List<int>> res = List.generate(n, (_) => []);
    for (int i = 0; i < n; i++) {
      var list = anc[i].toList();
      list.sort();
      res[i] = list;
    }
    return res;
  }
}
```

## Golang

```go
func getAncestors(n int, edges [][]int) [][]int {
    // Build adjacency list and indegree array
    adj := make([][]int, n)
    indeg := make([]int, n)
    for _, e := range edges {
        u, v := e[0], e[1]
        adj[u] = append(adj[u], v)
        indeg[v]++
    }

    // Kahn's algorithm for topological order
    queue := make([]int, 0, n)
    for i := 0; i < n; i++ {
        if indeg[i] == 0 {
            queue = append(queue, i)
        }
    }
    topo := make([]int, 0, n)
    for front := 0; front < len(queue); front++ {
        node := queue[front]
        topo = append(topo, node)
        for _, nb := range adj[node] {
            indeg[nb]--
            if indeg[nb] == 0 {
                queue = append(queue, nb)
            }
        }
    }

    // ancestors matrix: anc[i][j] == true means j is an ancestor of i
    anc := make([][]bool, n)
    for i := 0; i < n; i++ {
        anc[i] = make([]bool, n)
    }

    // Propagate ancestors following topological order
    for _, node := range topo {
        for _, nb := range adj[node] {
            // direct ancestor
            anc[nb][node] = true
            // inherit all ancestors of node
            for i := 0; i < n; i++ {
                if anc[node][i] {
                    anc[nb][i] = true
                }
            }
        }
    }

    // Build result lists in ascending order
    res := make([][]int, n)
    for i := 0; i < n; i++ {
        list := make([]int, 0)
        for j := 0; j < n; j++ {
            if anc[i][j] {
                list = append(list, j)
            }
        }
        res[i] = list
    }
    return res
}
```

## Ruby

```ruby
def get_ancestors(n, edges)
  require 'set'
  adj = Array.new(n) { [] }
  indeg = Array.new(n, 0)

  edges.each do |u, v|
    adj[u] << v
    indeg[v] += 1
  end

  queue = []
  n.times { |i| queue << i if indeg[i].zero? }

  order = []
  q_idx = 0
  while q_idx < queue.size
    node = queue[q_idx]
    q_idx += 1
    order << node
    adj[node].each do |nbr|
      indeg[nbr] -= 1
      queue << nbr if indeg[nbr].zero?
    end
  end

  anc_sets = Array.new(n) { Set.new }

  order.each do |node|
    adj[node].each do |nbr|
      anc_sets[nbr].add(node)
      anc_sets[node].each { |a| anc_sets[nbr].add(a) }
    end
  end

  result = []
  n.times { |i| result << anc_sets[i].to_a.sort }
  result
end
```

## Scala

```scala
object Solution {
  def getAncestors(n: Int, edges: Array[Array[Int]]): List[List[Int]] = {
    import scala.collection.mutable.{ArrayBuffer, ArrayDeque, BitSet}

    // Build adjacency list and indegree array
    val adj = Array.fill(n)(new ArrayBuffer[Int]())
    val indeg = new Array[Int](n)
    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      adj(u).append(v)
      indeg(v) += 1
    }

    // Kahn's algorithm for topological order
    val queue = new ArrayDeque[Int]()
    for (i <- 0 until n if indeg(i) == 0) queue.append(i)

    val topo = new ArrayBuffer[Int]()
    while (queue.nonEmpty) {
      val u = queue.removeHead()
      topo.append(u)
      for (v <- adj(u)) {
        indeg(v) -= 1
        if (indeg(v) == 0) queue.append(v)
      }
    }

    // Ancestor sets using BitSet for O(1) union operations
    val ancestors = Array.fill(n)(new BitSet())
    for (u <- topo) {
      for (v <- adj(u)) {
        ancestors(v) += u          // direct parent
        ancestors(v) ++= ancestors(u) // all ancestors of u
      }
    }

    // Convert each BitSet to a sorted List[Int]
    (0 until n).map(i => ancestors(i).toList.sorted).toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn get_ancestors(n: i32, edges: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        let mut indeg = vec![0usize; n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            indeg[v] += 1;
        }

        use std::collections::VecDeque;
        let mut q = VecDeque::new();
        for i in 0..n {
            if indeg[i] == 0 {
                q.push_back(i);
            }
        }

        let mut order = Vec::with_capacity(n);
        while let Some(u) = q.pop_front() {
            order.push(u);
            for &v in adj[u].iter() {
                indeg[v] -= 1;
                if indeg[v] == 0 {
                    q.push_back(v);
                }
            }
        }

        // ancestor matrix: anc[i][j] == true iff i is an ancestor of j
        let mut anc = vec![vec![false; n]; n];
        for &u in order.iter() {
            for &v in adj[u].iter() {
                anc[u][v] = true;
                for i in 0..n {
                    if anc[i][u] {
                        anc[i][v] = true;
                    }
                }
            }
        }

        let mut res: Vec<Vec<i32>> = vec![Vec::new(); n];
        for v in 0..n {
            let mut list = Vec::new();
            for i in 0..n {
                if anc[i][v] {
                    list.push(i as i32);
                }
            }
            res[v] = list;
        }
        res
    }
}
```

## Racket

```racket
(define/contract (get-ancestors n edges)
  (-> exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ((adj (make-vector n '()))
         (indeg (make-vector n 0)))
    ;; build graph and indegrees
    (for ([e edges])
      (define from (first e))
      (define to   (second e))
      (vector-set! adj from (cons to (vector-ref adj from)))
      (vector-set! indeg to (+ 1 (vector-ref indeg to))))
    ;; topological sort (Kahn's algorithm)
    (define queue (make-vector n 0))
    (define qhead 0)
    (define qtail 0)
    (for ([i (in-range n)])
      (when (= (vector-ref indeg i) 0)
        (vector-set! queue qtail i)
        (set! qtail (+ qtail 1))))
    (define topo '())
    (let loop ()
      (when (< qhead qtail)
        (define node (vector-ref queue qhead))
        (set! qhead (+ qhead 1))
        (set! topo (cons node topo))
        (for ([nbr (vector-ref adj node)])
          (vector-set! indeg nbr (- (vector-ref indeg nbr) 1))
          (when (= (vector-ref indeg nbr) 0)
            (vector-set! queue qtail nbr)
            (set! qtail (+ qtail 1))))
        (loop)))
    (set! topo (reverse topo))
    ;; ancestors sets per node
    (define anc-sets (make-vector n (make-hash))) ; each a mutable hash table
    (for ([node topo])
      (for ([nbr (vector-ref adj node)])
        (define set-nbr (vector-ref anc-sets nbr))
        (define set-node (vector-ref anc-sets node))
        ;; add direct ancestor
        (hash-set! set-nbr node #t)
        ;; add all ancestors of node
        (for ([k (in-hash-keys set-node)])
          (hash-set! set-nbr k #t))))
    ;; build result list
    (define result (make-vector n '()))
    (for ([i (in-range n)])
      (define keys (sort (hash->list (vector-ref anc-sets i)) < #:key car))
      (vector-set! result i (map car keys)))
    (vector->list result)))
```

## Erlang

```erlang
-module(solution).
-export([get_ancestors/2]).
-spec get_ancestors(N :: integer(), Edges :: [[integer()]]) -> [[integer()]].
get_ancestors(N, Edges) ->
    Adj0 = erlang:make_tuple(N, []),
    Indeg0 = erlang:make_tuple(N, 0),
    {Adj, Indeg} = build_graph(Edges, Adj0, Indeg0),
    Q0 = init_queue(N, Indeg, queue:new()),
    AncMap = #{},
    {_FinalIndeg, FinalAncMap} = bfs(Q0, Adj, Indeg, AncMap),
    [lists:sort(gb_sets:to_list(maps:get(I, FinalAncMap, gb_sets:new()))) ||
        I <- lists:seq(0, N - 1)].

build_graph([], Adj, Indeg) ->
    {Adj, Indeg};
build_graph([[U, V] | Rest], Adj, Indeg) ->
    OldList = element(U + 1, Adj),
    NewAdj = setelement(U + 1, Adj, [V | OldList]),
    OldInd = element(V + 1, Indeg),
    NewIndeg = setelement(V + 1, Indeg, OldInd + 1),
    build_graph(Rest, NewAdj, NewIndeg).

init_queue(N, Indeg, Q) ->
    init_queue(0, N, Indeg, Q).

init_queue(I, N, _Indeg, Q) when I >= N ->
    Q;
init_queue(I, N, Indeg, Q) ->
    Deg = element(I + 1, Indeg),
    Q1 = if Deg == 0 -> queue:in(I, Q); true -> Q end,
    init_queue(I + 1, N, Indeg, Q1).

bfs(Q, Adj, Indeg, AncMap) ->
    case queue:out(Q) of
        {value, Node, RestQ} ->
            Neighs = element(Node + 1, Adj),
            {NewIndeg, NewAncMap, NewQ} =
                process_neighbors(Neighs, Node, Indeg, AncMap, RestQ),
            bfs(NewQ, Adj, NewIndeg, NewAncMap);
        empty ->
            {Indeg, AncMap}
    end.

process_neighbors([], _Node, Indeg, AncMap, Q) ->
    {Indeg, AncMap, Q};
process_neighbors([Nbr | Rest], Node, Indeg, AncMap, Q) ->
    AncSetNode = maps:get(Node, AncMap, gb_sets:new()),
    AncSetNbr = maps:get(Nbr, AncMap, gb_sets:new()),
    Temp = gb_sets:add(Node, AncSetNode),
    UpdatedSet = gb_sets:union(AncSetNbr, Temp),
    NewAncMap = maps:put(Nbr, UpdatedSet, AncMap),

    OldDeg = element(Nbr + 1, Indeg),
    NewDegVal = OldDeg - 1,
    NewIndegTmp = setelement(Nbr + 1, Indeg, NewDegVal),
    Q1 = if NewDegVal == 0 -> queue:in(Nbr, Q); true -> Q end,

    process_neighbors(Rest, Node, NewIndegTmp, NewAncMap, Q1).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_ancestors(n :: integer, edges :: [[integer]]) :: [[integer]]
  def get_ancestors(n, edges) do
    # Build adjacency map and indegree map
    {adj, indeg} =
      Enum.reduce(edges, {%{}, Map.new(0..(n - 1), fn i -> {i, 0} end)}, fn [u, v], {a, d} ->
        a = Map.update(a, u, [v], &[v | &1])
        d = Map.update!(d, v, &(&1 + 1))
        {a, d}
      end)

    # Kahn's algorithm for topological order
    zero_deg_nodes = indeg |> Enum.filter(fn {_k, v} -> v == 0 end) |> Enum.map(&elem(&1, 0))

    topo_order = kahn(zero_deg_nodes, indeg, adj, [])

    # Ancestors sets initialization
    anc_sets = Enum.map(0..(n - 1), fn _ -> MapSet.new() end)

    # Propagate ancestors following topological order
    final_sets =
      Enum.reduce(topo_order, anc_sets, fn node, sets_acc ->
        neighbors = Map.get(adj, node, [])

        Enum.reduce(neighbors, sets_acc, fn neighbor, inner_sets ->
          neighbor_set = Enum.at(inner_sets, neighbor)
          node_set = Enum.at(inner_sets, node)

          updated =
            neighbor_set
            |> MapSet.put(node)
            |> MapSet.union(node_set)

          List.replace_at(inner_sets, neighbor, updated)
        end)
      end)

    # Convert sets to sorted lists
    Enum.map(final_sets, fn set -> set |> MapSet.to_list() |> Enum.sort() end)
  end

  defp kahn([], _indeg, _adj, order), do: Enum.reverse(order)

  defp kahn([node | rest_queue], indeg, adj, order) do
    {new_indeg, new_queue} =
      Enum.reduce(Map.get(adj, node, []), {indeg, rest_queue}, fn neighbor,
                                                                {indeg_acc, q_acc} ->
        deg = Map.get(indeg_acc, neighbor)
        deg2 = deg - 1
        indeg_updated = Map.put(indeg_acc, neighbor, deg2)

        if deg2 == 0 do
          {indeg_updated, q_acc ++ [neighbor]}
        else
          {indeg_updated, q_acc}
        end
      end)

    kahn(new_queue, new_indeg, adj, [node | order])
  end
end
```

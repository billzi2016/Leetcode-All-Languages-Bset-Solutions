# 2581. Count Number of Possible Root Nodes

## Cpp

```cpp
class Solution {
public:
    int rootCount(vector<vector<int>>& edges, vector<vector<int>>& guesses, int k) {
        int n = edges.size() + 1;
        vector<vector<int>> g(n);
        for (auto& e : edges) {
            int a = e[0], b = e[1];
            g[a].push_back(b);
            g[b].push_back(a);
        }
        unordered_set<long long> guessSet;
        guessSet.reserve(guesses.size() * 2 + 1);
        for (auto& p : guesses) {
            int u = p[0], v = p[1];
            long long key = ((long long)u << 32) | (unsigned int)v;
            guessSet.insert(key);
        }
        // Build parent array and order using iterative DFS
        vector<int> parent(n, -1);
        vector<int> order;
        order.reserve(n);
        stack<int> st;
        st.push(0);
        parent[0] = 0;
        while (!st.empty()) {
            int u = st.top(); st.pop();
            order.push_back(u);
            for (int v : g[u]) {
                if (v == parent[u]) continue;
                parent[v] = u;
                st.push(v);
            }
        }
        // Initial correct guesses count when root is 0
        int cntRoot = 0;
        for (int i = 1; i < n; ++i) { // skip node 0 which has no parent edge upward
            int v = order[i];
            int p = parent[v];
            long long key = ((long long)p << 32) | (unsigned int)v;
            if (guessSet.find(key) != guessSet.end()) ++cntRoot;
        }
        vector<int> cnt(n);
        cnt[0] = cntRoot;
        int answer = (cntRoot >= k) ? 1 : 0;
        // Reroot DP
        for (int u : order) {
            for (int v : g[u]) {
                if (v == parent[u]) continue; // child direction in original rooting at 0
                // move root from u to v
                int cur = cnt[u];
                long long loseKey = ((long long)u << 32) | (unsigned int)v;
                long long gainKey = ((long long)v << 32) | (unsigned int)u;
                if (guessSet.find(loseKey) != guessSet.end()) --cur;
                if (guessSet.find(gainKey) != guessSet.end()) ++cur;
                cnt[v] = cur;
                if (cur >= k) ++answer;
            }
        }
        return answer;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int rootCount(int[][] edges, int[][] guesses, int k) {
        int n = edges.length + 1;
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            int a = e[0], b = e[1];
            graph[a].add(b);
            graph[b].add(a);
        }

        Set<Long> guessSet = new HashSet<>(guesses.length * 2);
        for (int[] g : guesses) {
            long key = ((long) g[0] << 32) | (g[1] & 0xffffffffL);
            guessSet.add(key);
        }

        // First DFS to compute correct guesses when root is 0
        int[] parent = new int[n];
        Arrays.fill(parent, -1);
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        parent[0] = 0;
        int cntRootZero = 0;
        while (!stack.isEmpty()) {
            int u = stack.pop();
            for (int v : graph[u]) {
                if (parent[v] == -1) {
                    parent[v] = u;
                    long key = ((long) u << 32) | (v & 0xffffffffL);
                    if (guessSet.contains(key)) cntRootZero++;
                    stack.push(v);
                }
            }
        }

        // Rerooting DFS
        int answer = 0;
        class NodeInfo {
            int node, parent, cnt;
            NodeInfo(int n, int p, int c) { node = n; parent = p; cnt = c; }
        }
        Deque<NodeInfo> dq = new ArrayDeque<>();
        dq.push(new NodeInfo(0, -1, cntRootZero));

        while (!dq.isEmpty()) {
            NodeInfo cur = dq.pop();
            if (cur.cnt >= k) answer++;
            for (int v : graph[cur.node]) {
                if (v == cur.parent) continue;
                int newCnt = cur.cnt;
                long key1 = ((long) cur.node << 32) | (v & 0xffffffffL);
                if (guessSet.contains(key1)) newCnt--;
                long key2 = ((long) v << 32) | (cur.node & 0xffffffffL);
                if (guessSet.contains(key2)) newCnt++;
                dq.push(new NodeInfo(v, cur.node, newCnt));
            }
        }

        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def rootCount(self, edges, guesses, k):
        """
        :type edges: List[List[int]]
        :type guesses: List[List[int]]
        :type k: int
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(300000)
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        guess_set = set((u, v) for u, v in guesses)

        def dfs_initial(u, parent):
            cnt = 0
            for v in adj[u]:
                if v == parent:
                    continue
                if (u, v) in guess_set:
                    cnt += 1
                cnt += dfs_initial(v, u)
            return cnt

        initial_correct = dfs_initial(0, -1)

        ans = 0

        def dfs_reroot(u, parent, cur):
            nonlocal ans
            if cur >= k:
                ans += 1
            for v in adj[u]:
                if v == parent:
                    continue
                new_cur = cur
                if (u, v) in guess_set:
                    new_cur -= 1
                if (v, u) in guess_set:
                    new_cur += 1
                dfs_reroot(v, u, new_cur)

        dfs_reroot(0, -1, initial_correct)
        return ans
```

## Python3

```python
class Solution:
    def rootCount(self, edges, guesses, k):
        from collections import defaultdict
        import sys
        sys.setrecursionlimit(300000)
        
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        guess_set = set((u, v) for u, v in guesses)
        
        def dfs_initial(node, parent):
            cnt = 0
            for nb in adj[node]:
                if nb == parent:
                    continue
                if (node, nb) in guess_set:
                    cnt += 1
                cnt += dfs_initial(nb, node)
            return cnt
        
        initial_correct = dfs_initial(0, -1)
        
        def dfs_reroot(node, parent, cur):
            total = 1 if cur >= k else 0
            for nb in adj[node]:
                if nb == parent:
                    continue
                new_cur = cur
                if (node, nb) in guess_set:
                    new_cur -= 1
                if (nb, node) in guess_set:
                    new_cur += 1
                total += dfs_reroot(nb, node, new_cur)
            return total
        
        return dfs_reroot(0, -1, initial_correct)
```

## C

```c
#include <stdlib.h>

static int guessExists(const long long *arr, int size, int u, int v) {
    long long key = ((long long)u << 32) | (unsigned int)v;
    int l = 0, r = size - 1;
    while (l <= r) {
        int m = (l + r) >> 1;
        if (arr[m] == key) return 1;
        if (arr[m] < key) l = m + 1;
        else r = m - 1;
    }
    return 0;
}

static int cmpLongLong(const void *a, const void *b) {
    long long x = *(const long long *)a;
    long long y = *(const long long *)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int rootCount(int** edges, int edgesSize, int* edgesColSize,
              int** guesses, int guessesSize, int* guessesColSize,
              int k) {
    int n = edgesSize + 1;

    /* Build adjacency list */
    int m = edgesSize;
    int total = 2 * m;
    int *head = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;
    int *to = (int *)malloc(total * sizeof(int));
    int *next = (int *)malloc(total * sizeof(int));
    int idx = 0;
    for (int i = 0; i < m; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        to[idx] = v; next[idx] = head[u]; head[u] = idx++;
        to[idx] = u; next[idx] = head[v]; head[v] = idx++;
    }

    /* Store guesses in sorted array for binary search */
    long long *gkeys = (long long *)malloc(guessesSize * sizeof(long long));
    for (int i = 0; i < guessesSize; ++i) {
        int u = guesses[i][0];
        int v = guesses[i][1];
        gkeys[i] = ((long long)u << 32) | (unsigned int)v;
    }
    qsort(gkeys, guessesSize, sizeof(long long), cmpLongLong);

    /* First DFS to get parent array and order */
    int *parent = (int *)malloc(n * sizeof(int));
    int *stack = (int *)malloc(n * sizeof(int));
    int top = 0;
    stack[top++] = 0;
    parent[0] = -1;

    int *order = (int *)malloc(n * sizeof(int));
    int ordCnt = 0;

    while (top) {
        int node = stack[--top];
        order[ordCnt++] = node;
        for (int e = head[node]; e != -1; e = next[e]) {
            int nb = to[e];
            if (nb == parent[node]) continue;
            parent[nb] = node;
            stack[top++] = nb;
        }
    }

    /* Compute initial correct guesses count for root 0 */
    int initCorrect = 0;
    for (int i = 1; i < n; ++i) {
        int p = parent[i];
        if (guessExists(gkeys, guessesSize, p, i)) ++initCorrect;
    }

    /* Second DFS to reroot and count valid roots */
    int ans = 0;
    top = 0;
    stack[top++] = 0;
    int *cntStack = (int *)malloc(n * sizeof(int));
    cntStack[0] = initCorrect;

    while (top) {
        int node = stack[--top];
        int curCnt = cntStack[top];
        if (curCnt >= k) ++ans;
        for (int e = head[node]; e != -1; e = next[e]) {
            int nb = to[e];
            if (nb == parent[node]) continue;
            int newCnt = curCnt
                         - (guessExists(gkeys, guessesSize, node, nb) ? 1 : 0)
                         + (guessExists(gkeys, guessesSize, nb, node) ? 1 : 0);
            stack[top] = nb;
            cntStack[top++] = newCnt;
        }
    }

    /* Free allocated memory */
    free(head);
    free(to);
    free(next);
    free(gkeys);
    free(parent);
    free(stack);
    free(order);
    free(cntStack);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int RootCount(int[][] edges, int[][] guesses, int k) {
        int n = edges.Length + 1;
        var adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            adj[a].Add(b);
            adj[b].Add(a);
        }

        var guessSet = new HashSet<long>();
        foreach (var g in guesses) {
            long key = ((long)g[0] << 32) | (uint)g[1];
            guessSet.Add(key);
        }

        // Compute initial correct guess count when root is 0
        int initCnt = 0;
        var stackInit = new Stack<(int node, int parent)>();
        stackInit.Push((0, -1));
        while (stackInit.Count > 0) {
            var (node, parent) = stackInit.Pop();
            foreach (int nb in adj[node]) {
                if (nb == parent) continue;
                long key = ((long)node << 32) | (uint)nb;
                if (guessSet.Contains(key)) initCnt++;
                stackInit.Push((nb, node));
            }
        }

        int answer = 0;
        var stack = new Stack<(int node, int parent, int cnt)>();
        stack.Push((0, -1, initCnt));

        while (stack.Count > 0) {
            var (node, parent, cnt) = stack.Pop();
            if (cnt >= k) answer++;

            foreach (int nb in adj[node]) {
                if (nb == parent) continue;
                int newCnt = cnt;

                long keyOut = ((long)node << 32) | (uint)nb; // edge node->nb
                if (guessSet.Contains(keyOut)) newCnt--;

                long keyIn = ((long)nb << 32) | (uint)node; // edge nb->node after reroot
                if (guessSet.Contains(keyIn)) newCnt++;

                stack.Push((nb, node, newCnt));
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @param {number[][]} guesses
 * @param {number} k
 * @return {number}
 */
var rootCount = function(edges, guesses, k) {
    const n = edges.length + 1;
    const adj = Array.from({length: n}, () => []);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
    }
    
    // store guesses as encoded numbers u * n + v
    const guessSet = new Set();
    for (const [u, v] of guesses) {
        guessSet.add(u * n + v);
    }
    
    // initial correct count when root is 0
    let curCorrect = 0;
    const stack = [[0, -1]];
    while (stack.length) {
        const [node, parent] = stack.pop();
        for (const nb of adj[node]) {
            if (nb === parent) continue;
            if (guessSet.has(node * n + nb)) curCorrect++;
            stack.push([nb, node]);
        }
    }
    
    let answer = 0;
    const stack2 = [[0, -1, curCorrect]];
    while (stack2.length) {
        const [node, parent, cnt] = stack2.pop();
        if (cnt >= k) answer++;
        for (const nb of adj[node]) {
            if (nb === parent) continue;
            let newCnt = cnt;
            // edge direction flips when re-rooting to neighbor
            if (guessSet.has(node * n + nb)) newCnt--;
            if (guessSet.has(nb * n + node)) newCnt++;
            stack2.push([nb, node, newCnt]);
        }
    }
    
    return answer;
};
```

## Typescript

```typescript
function rootCount(edges: number[][], guesses: number[][], k: number): number {
    const n = edges.length + 1;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
    }

    const guessSet = new Set<string>();
    for (const [u, v] of guesses) {
        guessSet.add(`${u}#${v}`);
    }

    const parent = new Int32Array(n);
    parent.fill(-1);
    const stack: number[] = [0];
    let initCorrect = 0;

    while (stack.length) {
        const u = stack.pop()!;
        for (const v of adj[u]) {
            if (v === parent[u]) continue;
            parent[v] = u;
            if (guessSet.has(`${u}#${v}`)) initCorrect++;
            stack.push(v);
        }
    }

    let answer = 0;
    const dfsStack: [number, number][] = [[0, initCorrect]];

    while (dfsStack.length) {
        const [u, cnt] = dfsStack.pop()!;
        if (cnt >= k) answer++;

        for (const v of adj[u]) {
            if (v === parent[u]) continue;
            let newCnt = cnt;
            if (guessSet.has(`${u}#${v}`)) newCnt--;
            if (guessSet.has(`${v}#${u}`)) newCnt++;
            dfsStack.push([v, newCnt]);
        }
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @param Integer[][] $guesses
     * @param Integer $k
     * @return Integer
     */
    function rootCount($edges, $guesses, $k) {
        $n = count($edges) + 1;
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            [$a, $b] = $e;
            $adj[$a][] = $b;
            $adj[$b][] = $a;
        }

        // store guesses in a hash set
        $guessSet = [];
        foreach ($guesses as $g) {
            [$u, $v] = $g;
            $guessSet[$u . ',' . $v] = true;
        }

        // first DFS to compute correct guesses when root is 0
        $stack = [[0, -1]];
        $initCorrect = 0;
        while ($stack) {
            [$node, $par] = array_pop($stack);
            foreach ($adj[$node] as $nei) {
                if ($nei === $par) continue;
                if (isset($guessSet[$node . ',' . $nei])) {
                    $initCorrect++;
                }
                $stack[] = [$nei, $node];
            }
        }

        // second DFS for rerooting
        $ans = 0;
        $stack = [[0, -1, $initCorrect]];
        while ($stack) {
            [$node, $par, $cur] = array_pop($stack);
            if ($cur >= $k) $ans++;

            foreach ($adj[$node] as $nei) {
                if ($nei === $par) continue;
                $next = $cur;

                // edge direction changes from node->nei to nei->node
                if (isset($guessSet[$node . ',' . $nei])) {
                    $next--; // was correct, now wrong
                }
                if (isset($guessSet[$nei . ',' . $node])) {
                    $next++; // becomes correct
                }

                $stack[] = [$nei, $node, $next];
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func rootCount(_ edges: [[Int]], _ guesses: [[Int]], _ k: Int) -> Int {
        let n = edges.count + 1
        var adj = Array(repeating: [Int](), count: n)
        for e in edges {
            let a = e[0], b = e[1]
            adj[a].append(b)
            adj[b].append(a)
        }
        func encode(_ u: Int, _ v: Int) -> UInt64 {
            return (UInt64(u) << 32) | UInt64(v)
        }
        var guessSet = Set<UInt64>()
        for g in guesses {
            guessSet.insert(encode(g[0], g[1]))
        }
        
        var parent = Array(repeating: -1, count: n)
        var order = [Int]()
        var stack = [Int]()
        stack.append(0)
        parent[0] = 0
        var initCorrect = 0
        
        while let u = stack.popLast() {
            order.append(u)
            for v in adj[u] {
                if v == parent[u] { continue }
                parent[v] = u
                if guessSet.contains(encode(u, v)) {
                    initCorrect += 1
                }
                stack.append(v)
            }
        }
        
        var correctCount = Array(repeating: 0, count: n)
        correctCount[0] = initCorrect
        var result = 0
        if initCorrect >= k { result += 1 }
        
        for u in order {
            for v in adj[u] {
                if parent[v] == u {
                    var cnt = correctCount[u]
                    if guessSet.contains(encode(u, v)) { cnt -= 1 }
                    if guessSet.contains(encode(v, u)) { cnt += 1 }
                    correctCount[v] = cnt
                    if cnt >= k { result += 1 }
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    private lateinit var adj: Array<MutableList<Int>>
    private lateinit var guessSet: HashSet<Long>
    private var nNodes = 0

    private fun encode(u: Int, v: Int): Long = u.toLong() * nNodes + v

    fun rootCount(edges: Array<IntArray>, guesses: Array<IntArray>, k: Int): Int {
        nNodes = edges.size + 1
        adj = Array(nNodes) { mutableListOf() }
        for (e in edges) {
            val a = e[0]
            val b = e[1]
            adj[a].add(b)
            adj[b].add(a)
        }

        guessSet = HashSet()
        for (g in guesses) {
            guessSet.add(encode(g[0], g[1]))
        }

        var initCorrect = 0
        fun dfsInit(node: Int, parent: Int) {
            for (nei in adj[node]) {
                if (nei == parent) continue
                if (guessSet.contains(encode(node, nei))) initCorrect++
                dfsInit(nei, node)
            }
        }
        dfsInit(0, -1)

        var answer = 0
        fun dfsReroot(node: Int, parent: Int, curCorrect: Int) {
            if (curCorrect >= k) answer++
            for (nei in adj[node]) {
                if (nei == parent) continue
                var newCorrect = curCorrect
                if (guessSet.contains(encode(node, nei))) newCorrect--
                if (guessSet.contains(encode(nei, node))) newCorrect++
                dfsReroot(nei, node, newCorrect)
            }
        }
        dfsReroot(0, -1, initCorrect)

        return answer
    }
}
```

## Dart

```dart
class Solution {
  int rootCount(List<List<int>> edges, List<List<int>> guesses, int k) {
    int n = edges.length + 1;
    var adj = List.generate(n, (_) => <int>[]);
    for (var e in edges) {
      int a = e[0], b = e[1];
      adj[a].add(b);
      adj[b].add(a);
    }

    // Encode guess pairs as u * n + v
    var guessSet = <int>{};
    for (var g in guesses) {
      int u = g[0], v = g[1];
      guessSet.add(u * n + v);
    }

    // First DFS to set parent and compute initial correct count for root 0
    List<int> parent = List.filled(n, -1);
    var stack = <int>[0];
    parent[0] = -2; // mark visited
    int initCnt = 0;
    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      for (int nb in adj[node]) {
        if (parent[nb] == -1) {
          parent[nb] = node;
          if (guessSet.contains(node * n + nb)) initCnt++;
          stack.add(nb);
        }
      }
    }

    // Reroot DP using iterative DFS
    int answer = 0;
    var nodesStack = <int>[0];
    var cntStack = <int>[initCnt];
    while (nodesStack.isNotEmpty) {
      int node = nodesStack.removeLast();
      int curCnt = cntStack.removeLast();
      if (curCnt >= k) answer++;

      for (int nb in adj[node]) {
        if (parent[nb] == node) { // child direction
          int newCnt = curCnt;
          if (guessSet.contains(node * n + nb)) newCnt--;
          if (guessSet.contains(nb * n + node)) newCnt++;
          nodesStack.add(nb);
          cntStack.add(newCnt);
        }
      }
    }

    return answer;
  }
}
```

## Golang

```go
func rootCount(edges [][]int, guesses [][]int, k int) int {
    n := len(edges) + 1
    adj := make([][]int, n)
    for _, e := range edges {
        a, b := e[0], e[1]
        adj[a] = append(adj[a], b)
        adj[b] = append(adj[b], a)
    }

    guessSet := make(map[[2]int]struct{}, len(guesses))
    for _, g := range guesses {
        guessSet[[2]int{g[0], g[1]}] = struct{}{}
    }

    parent := make([]int, n)
    for i := 0; i < n; i++ {
        parent[i] = -1
    }
    // initial DFS from node 0 to compute parent array and initial correct guess count
    stack := []int{0}
    parent[0] = -2 // mark root
    initCnt := 0
    for len(stack) > 0 {
        u := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        for _, v := range adj[u] {
            if v == parent[u] {
                continue
            }
            parent[v] = u
            if _, ok := guessSet[[2]int{u, v}]; ok {
                initCnt++
            }
            stack = append(stack, v)
        }
    }

    ans := 0
    type item struct {
        node int
        cnt  int
    }
    // iterative rerooting DFS using the original parent orientation
    st := []item{{0, initCnt}}
    for len(st) > 0 {
        cur := st[len(st)-1]
        st = st[:len(st)-1]
        if cur.cnt >= k {
            ans++
        }
        u := cur.node
        for _, v := range adj[u] {
            if v == parent[u] {
                continue
            }
            newCnt := cur.cnt
            if _, ok := guessSet[[2]int{u, v}]; ok {
                newCnt--
            }
            if _, ok := guessSet[[2]int{v, u}]; ok {
                newCnt++
            }
            st = append(st, item{v, newCnt})
        }
    }

    return ans
}
```

## Ruby

```ruby
def root_count(edges, guesses, k)
  n = edges.length + 1
  adj = Array.new(n) { [] }
  edges.each do |a, b|
    adj[a] << b
    adj[b] << a
  end

  guess_set = {}
  guesses.each do |u, v|
    guess_set[u * n + v] = true
  end

  parent = Array.new(n, -1)
  order = []
  stack = [[0, -1]]
  until stack.empty?
    node, par = stack.pop
    parent[node] = par
    order << node
    adj[node].each do |nb|
      next if nb == par
      stack << [nb, node]
    end
  end

  cur_correct = 0
  order.each do |node|
    p = parent[node]
    next if p == -1
    cur_correct += 1 if guess_set[p * n + node]
  end

  ans = 0
  ans += 1 if cur_correct >= k

  stack2 = [[0, -1, cur_correct]]
  until stack2.empty?
    node, par, cnt = stack2.pop
    adj[node].each do |nb|
      next if nb == par
      delta = 0
      delta -= 1 if guess_set[node * n + nb]
      delta += 1 if guess_set[nb * n + node]
      new_cnt = cnt + delta
      ans += 1 if new_cnt >= k
      stack2 << [nb, node, new_cnt]
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{ArrayBuffer, Stack, HashSet}

  def rootCount(edges: Array[Array[Int]], guesses: Array[Array[Int]], k: Int): Int = {
    val n = edges.length + 1
    val adj = Array.fill(n)(new ArrayBuffer[Int]())
    for (e <- edges) {
      val a = e(0)
      val b = e(1)
      adj(a) += b
      adj(b) += a
    }

    // encode directed edge as long: (u << 32) | v
    def enc(u: Int, v: Int): Long = (u.toLong << 32) | v.toLong

    val guessSet = new HashSet[Long]()
    for (g <- guesses) {
      guessSet += enc(g(0), g(1))
    }

    // First DFS to set parent relationships rooted at 0
    val parent = Array.fill[Int](n)(-2) // -2 means unvisited
    val order = new ArrayBuffer[Int]()
    val stack = new Stack[Int]()
    stack.push(0)
    parent(0) = -1

    while (stack.nonEmpty) {
      val node = stack.pop()
      order += node
      for (nei <- adj(node)) {
        if (parent(nei) == -2) {
          parent(nei) = node
          stack.push(nei)
        }
      }
    }

    // Compute initial correct guess count when root is 0
    var curCnt = 0
    for (i <- 1 until n) { // skip root
      val p = parent(i)
      if (guessSet.contains(enc(p, i))) curCnt += 1
    }

    // Rerooting DFS
    var answer = 0
    val stack2 = new Stack[(Int, Int)]()
    stack2.push((0, curCnt))

    while (stack2.nonEmpty) {
      val (node, cnt) = stack2.pop()
      if (cnt >= k) answer += 1
      for (nei <- adj(node)) {
        if (nei != parent(node)) { // child in original rooting
          var newCnt = cnt
          if (guessSet.contains(enc(node, nei))) newCnt -= 1
          if (guessSet.contains(enc(nei, node))) newCnt += 1
          stack2.push((nei, newCnt))
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
    pub fn root_count(edges: Vec<Vec<i32>>, guesses: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = edges.len() + 1;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in edges.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }
        use std::collections::HashSet;
        let mut guess_set: HashSet<u64> = HashSet::with_capacity(guesses.len() * 2);
        for g in guesses.iter() {
            let u = g[0] as usize;
            let v = g[1] as usize;
            let key = ((u as u64) << 32) | (v as u64);
            guess_set.insert(key);
        }
        // initial correct guesses when rooted at 0
        let mut init: i32 = 0;
        let mut stack: Vec<(usize, usize)> = Vec::new();
        stack.push((0, usize::MAX));
        while let Some((u, p)) = stack.pop() {
            for &v in adj[u].iter() {
                if v == p { continue; }
                let key_uv = ((u as u64) << 32) | (v as u64);
                if guess_set.contains(&key_uv) {
                    init += 1;
                }
                stack.push((v, u));
            }
        }
        // reroot DP
        let mut ans: i32 = 0;
        let mut stack2: Vec<(usize, usize, i32)> = Vec::new();
        stack2.push((0, usize::MAX, init));
        while let Some((u, p, cur)) = stack2.pop() {
            if cur >= k { ans += 1; }
            for &v in adj[u].iter() {
                if v == p { continue; }
                let mut next = cur;
                let key_uv = ((u as u64) << 32) | (v as u64);
                if guess_set.contains(&key_uv) {
                    next -= 1;
                }
                let key_vu = ((v as u64) << 32) | (u as u64);
                if guess_set.contains(&key_vu) {
                    next += 1;
                }
                stack2.push((v, u, next));
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (root-count edges guesses k)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((n (+ 1 (length edges)))                     ; n = number of nodes
         (adj (make-vector n '()))                   ; adjacency list
         (add-edge
          (lambda (u v)
            (vector-set! adj u (cons v (vector-ref adj u)))
            (vector-set! adj v (cons u (vector-ref adj v))))))
    ;; build adjacency
    (for-each (lambda (e) (let ((u (first e)) (v (second e))) (add-edge u v))) edges)
    ;; store guesses in a hash set
    (define guess-set (make-hash))
    (for-each (lambda (g) (hash-set! guess-set (cons (first g) (second g)) #t)) guesses)
    (define (guess? u v) (hash-has-key? guess-set (cons u v)))
    ;; first DFS: compute parent array and initial correct count for root 0
    (let ((parent (make-vector n -1))
          (stack (list 0))
          (init-count 0))
      (vector-set! parent 0 -2) ; mark root as visited
      (let loop ()
        (when (not (null? stack))
          (define cur (car stack))
          (set! stack (cdr stack))
          (for-each (lambda (nbr)
                      (when (= (vector-ref parent nbr) -1)
                        (vector-set! parent nbr cur)
                        (when (guess? cur nbr)
                          (set! init-count (+ init-count 1)))
                        (set! stack (cons nbr stack))))
                    (vector-ref adj cur))
          (loop)))
      ;; second DFS: reroot and count valid roots
      (let ((ans 0)
            (stack2 (list (list 0 init-count)))) ; each element = (node current-count)
        (let loop2 ()
          (when (not (null? stack2))
            (define pair (car stack2))
            (set! stack2 (cdr stack2))
            (define node (first pair))
            (define curcnt (second pair))
            (when (>= curcnt k) (set! ans (+ ans 1)))
            (for-each (lambda (nbr)
                        (when (= (vector-ref parent nbr) node) ; nbr is child of node in current rooting
                          (define newcnt (- curcnt (if (guess? node nbr) 1 0)))
                          (set! newcnt (+ newcnt (if (guess? nbr node) 1 0)))
                          (set! stack2 (cons (list nbr newcnt) stack2))))
                      (vector-ref adj node))
            (loop2)))
        ans))))
```

## Erlang

```erlang
-module(solution).
-export([root_count/3]).

-spec root_count(Edges :: [[integer()]], Guesses :: [[integer()]], K :: integer()) -> integer().
root_count(Edges, Guesses, K) ->
    Adj = build_adj(Edges, #{}),
    GuessSet = build_guess_set(Guesses, #{}),
    InitCnt = initial_correct_cnt(Adj, GuessSet),
    count_possible_roots(Adj, GuessSet, K, InitCnt).

%% Build adjacency list as a map Node -> [Neighbors]
build_adj([], Adj) ->
    Adj;
build_adj([[A, B] | Rest], Adj) ->
    Adj1 = maps:update_with(A,
            fun(L) -> [B | L] end,
            [B],
            Adj),
    Adj2 = maps:update_with(B,
            fun(L) -> [A | L] end,
            [A],
            Adj1),
    build_adj(Rest, Adj2).

%% Build guess set as a map {U,V} -> true
build_guess_set([], Set) ->
    Set;
build_guess_set([[U, V] | Rest], Set) ->
    NewSet = maps:put({U, V}, true, Set),
    build_guess_set(Rest, NewSet).

%% Compute initial correct guess count when rooted at node 0
initial_correct_cnt(Adj, GuessSet) ->
    initial_correct_cnt([{0, -1}], Adj, GuessSet, 0).

initial_correct_cnt([], _Adj, _GuessSet, Count) ->
    Count;
initial_correct_cnt([{Node, Parent} | Rest], Adj, GuessSet, Count) ->
    NewCount = case Parent of
        -1 -> Count;
        _ when maps:is_key({Parent, Node}, GuessSet) -> Count + 1;
        _ -> Count
    end,
    Neigh = maps:get(Node, Adj, []),
    ChildStack = lists:foldl(fun(Nei, Acc) ->
        if Nei =:= Parent -> Acc;
           true -> [{Nei, Node} | Acc]
        end
    end, Rest, Neigh),
    initial_correct_cnt(ChildStack, Adj, GuessSet, NewCount).

%% Reroot DP to count nodes with at least K correct guesses
count_possible_roots(Adj, GuessSet, K, InitCnt) ->
    count_possible_roots([{0, -1, InitCnt}], Adj, GuessSet, K, 0).

count_possible_roots([], _Adj, _GuessSet, _K, Ans) ->
    Ans;
count_possible_roots([{Node, Parent, CurCnt} | Rest], Adj, GuessSet, K, Ans) ->
    NewAns = if CurCnt >= K -> Ans + 1; true -> Ans end,
    Neigh = maps:get(Node, Adj, []),
    UpdatedStack = lists:foldl(fun(Nei, Acc) ->
        if Nei =:= Parent -> Acc;
           true ->
               C1 = case maps:is_key({Node, Nei}, GuessSet) of
                        true -> CurCnt - 1;
                        false -> CurCnt
                    end,
               C2 = case maps:is_key({Nei, Node}, GuessSet) of
                        true -> C1 + 1;
                        false -> C1
                    end,
               [{Nei, Node, C2} | Acc]
        end
    end, Rest, Neigh),
    count_possible_roots(UpdatedStack, Adj, GuessSet, K, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec root_count(edges :: [[integer]], guesses :: [[integer]], k :: integer) :: integer
  def root_count(edges, guesses, k) do
    n = length(edges) + 1

    adj = build_adj(edges)

    guess_set = MapSet.new(Enum.map(guesses, fn [u, v] -> {u, v} end))

    {parents, init_score} = dfs_initial(adj, guess_set)

    count_possible_roots(adj, parents, init_score, guess_set, k)
  end

  defp build_adj(edges) do
    Enum.reduce(edges, %{}, fn [a, b], acc ->
      acc
      |> Map.update(a, [b], fn list -> [b | list] end)
      |> Map.update(b, [a], fn list -> [a | list] end)
    end)
  end

  # First DFS: compute parent map and initial correct guess count when root = 0
  defp dfs_initial(adj, guess_set) do
    dfs_initial([{0, -1}], %{}, 0, adj, guess_set)
  end

  defp dfs_initial([], parents, score, _adj, _guess_set), do: {parents, score}

  defp dfs_initial([{node, par} | stack], parents, score, adj, guess_set) do
    new_parents = Map.put(parents, node, par)

    {new_stack, new_score} =
      Enum.reduce(Map.get(adj, node, []), {stack, score}, fn nb, {stk, sc} ->
        if nb == par do
          {stk, sc}
        else
          inc = if MapSet.member?(guess_set, {node, nb}), do: 1, else: 0
          {[{nb, node} | stk], sc + inc}
        end
      end)

    dfs_initial(new_stack, new_parents, new_score, adj, guess_set)
  end

  # Second DFS: reroot DP to compute score for each possible root
  defp count_possible_roots(adj, parents, init_score, guess_set, k) do
    count_possible_roots([{0, init_score}], adj, parents, guess_set, k, 0)
  end

  defp count_possible_roots([], _adj, _parents, _guess_set, _k, acc), do: acc

  defp count_possible_roots([{node, cur_score} | stack], adj, parents, guess_set, k, acc) do
    new_acc = if cur_score >= k, do: acc + 1, else: acc

    {new_stack, _} =
      Enum.reduce(Map.get(adj, node, []), {stack, nil}, fn nb, {stk, _} ->
        if nb == Map.get(parents, node) do
          {stk, nil}
        else
          delta =
            (if MapSet.member?(guess_set, {node, nb}), do: -1, else: 0) +
              (if MapSet.member?(guess_set, {nb, node}), do: 1, else: 0)

          {[{nb, cur_score + delta} | stk], nil}
        end
      end)

    count_possible_roots(new_stack, adj, parents, guess_set, k, new_acc)
  end
end
```

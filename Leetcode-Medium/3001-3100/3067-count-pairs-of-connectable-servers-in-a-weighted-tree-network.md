# 3067. Count Pairs of Connectable Servers in a Weighted Tree Network

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> countPairsOfConnectableServers(vector<vector<int>>& edges, int signalSpeed) {
        // determine number of nodes
        int n = 0;
        for (auto &e : edges) {
            n = max(n, max(e[0], e[1]) + 1);
        }
        vector<vector<pair<int,int>>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }

        vector<int> answer(n, 0);

        // helper DFS to collect remainder counts in a subtree
        function<void(int,int,long long, unordered_map<int,int>&)> dfs = [&](int u, int parent,
                                                                            long long curMod,
                                                                            unordered_map<int,int>& mp) {
            int r = (int)curMod;
            ++mp[r];
            for (auto &pr : adj[u]) {
                int v = pr.first;
                int w = pr.second;
                if (v == parent) continue;
                dfs(v, u, (curMod + w) % signalSpeed, mp);
            }
        };

        for (int root = 0; root < n; ++root) {
            vector<unordered_map<int,int>> childMaps;
            childMaps.reserve(adj[root].size());

            // build remainder maps for each neighbor subtree
            for (auto &pr : adj[root]) {
                int nb = pr.first;
                int w = pr.second;
                unordered_map<int,int> mp;
                dfs(nb, root, w % signalSpeed, mp);
                childMaps.push_back(move(mp));
            }

            unordered_map<int,int> accumulated; // counts from processed children
            long long totalPairs = 0;

            for (auto &cm : childMaps) {
                // count pairs between current child and previously seen nodes
                for (const auto &p : cm) {
                    int r = p.first;
                    long long cnt = p.second;
                    int need = (signalSpeed - r) % signalSpeed;
                    auto it = accumulated.find(need);
                    if (it != accumulated.end()) {
                        totalPairs += cnt * 1LL * it->second;
                    }
                }
                // merge current child counts into accumulated
                for (const auto &p : cm) {
                    accumulated[p.first] += p.second;
                }
            }

            answer[root] = (int)totalPairs;
        }

        return answer;
    }
};
```

## Java

```java
class Solution {
    public int[] countPairsOfConnectableServers(int[][] edges, int signalSpeed) {
        int n = edges.length + 1;
        List<int[]>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            int a = e[0], b = e[1], w = e[2];
            adj[a].add(new int[]{b, w});
            adj[b].add(new int[]{a, w});
        }
        int[] ans = new int[n];
        for (int root = 0; root < n; root++) {
            long sum = 0;
            long sumSq = 0;
            for (int[] edge : adj[root]) {
                int nb = edge[0];
                int w = edge[1] % signalSpeed;
                int cnt = dfs(nb, root, w, adj, signalSpeed);
                sum += cnt;
                sumSq += (long) cnt * cnt;
            }
            long pairs = (sum * sum - sumSq) / 2;
            ans[root] = (int) pairs;
        }
        return ans;
    }

    private int dfs(int node, int parent, int curMod, List<int[]>[] adj, int speed) {
        int cnt = (curMod == 0) ? 1 : 0;
        for (int[] e : adj[node]) {
            int nxt = e[0];
            if (nxt == parent) continue;
            int nextMod = (curMod + e[1]) % speed;
            cnt += dfs(nxt, node, nextMod, adj, speed);
        }
        return cnt;
    }
}
```

## Python

```python
class Solution(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        """
        :type edges: List[List[int]]
        :type signalSpeed: int
        :rtype: List[int]
        """
        # determine number of nodes
        n = 0
        for a, b, _ in edges:
            n = max(n, a, b)
        n += 1

        adj = [[] for _ in range(n)]
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))

        sys_setrecursionlimit = __import__('sys').setrecursionlimit
        sys_setrecursionlimit(10000)

        def dfs(u, parent, cur_mod):
            cnt = 1 if cur_mod == 0 else 0
            for v, w in adj[u]:
                if v == parent:
                    continue
                cnt += dfs(v, u, (cur_mod + w) % signalSpeed)
            return cnt

        result = [0] * n
        for c in range(n):
            subtree_counts = []
            for nb, w in adj[c]:
                cnt = dfs(nb, c, w % signalSpeed)
                subtree_counts.append(cnt)
            total = sum(subtree_counts)
            sq_sum = sum(x * x for x in subtree_counts)
            result[c] = (total * total - sq_sum) // 2
        return result
```

## Python3

```python
import sys
from typing import List

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        # Determine number of nodes
        n = 0
        for a, b, _ in edges:
            n = max(n, a, b)
        n += 1

        adj = [[] for _ in range(n)]
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))

        k = signalSpeed
        result = [0] * n

        for root in range(n):
            child_counts = {}
            # explore each neighbor subtree separately
            for nb, w in adj[root]:
                cnt = 0
                stack = [(nb, root, w % k)]
                while stack:
                    node, parent, dist_mod = stack.pop()
                    if dist_mod == 0:
                        cnt += 1
                    for nxt, wt in adj[node]:
                        if nxt != parent:
                            stack.append((nxt, node, (dist_mod + wt) % k))
                child_counts[nb] = cnt

            total = sum(child_counts.values())
            pairs = 0
            for c in child_counts.values():
                pairs += c * (total - c)
            result[root] = pairs // 2  # each unordered pair counted twice

        return result
```

## C

```c
#include <stdlib.h>

typedef struct {
    int to;
    int w;
    int next;
} Edge;

int* countPairsOfConnectableServers(int** edges, int edgesSize, int* edgesColSize, int signalSpeed, int* returnSize) {
    int n = edgesSize + 1;
    int maxEdges = edgesSize * 2;
    Edge *E = (Edge*)malloc(sizeof(Edge) * maxEdges);
    int *head = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;
    int *deg = (int*)calloc(n, sizeof(int));
    int edgeCnt = 0;

    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        int w = edges[i][2];

        E[edgeCnt].to = b;
        E[edgeCnt].w = w;
        E[edgeCnt].next = head[a];
        head[a] = edgeCnt++;
        deg[a]++;

        E[edgeCnt].to = a;
        E[edgeCnt].w = w;
        E[edgeCnt].next = head[b];
        head[b] = edgeCnt++;
        deg[b]++;
    }

    int *answer = (int*)malloc(sizeof(int) * n);
    *returnSize = n;

    // temporary stacks for DFS
    int *stackNode = (int*)malloc(sizeof(int) * n);
    int *stackParent = (int*)malloc(sizeof(int) * n);
    int *stackMod = (int*)malloc(sizeof(int) * n);
    int *stackComp = (int*)malloc(sizeof(int) * n);

    for (int c = 0; c < n; ++c) {
        int d = deg[c];
        int *cnt = (int*)calloc(d, sizeof(int));

        // push initial nodes from each neighbor component
        int top = 0;
        int compIdx = 0;
        for (int e = head[c]; e != -1; e = E[e].next) {
            int v = E[e].to;
            int wmod = E[e].w % signalSpeed;
            stackNode[top] = v;
            stackParent[top] = c;
            stackMod[top] = wmod;
            stackComp[top] = compIdx;
            top++;
            compIdx++;
        }

        while (top > 0) {
            --top;
            int node = stackNode[top];
            int parent = stackParent[top];
            int mod = stackMod[top];
            int comp = stackComp[top];

            if (mod == 0) cnt[comp]++;

            for (int e = head[node]; e != -1; e = E[e].next) {
                int nxt = E[e].to;
                if (nxt == parent) continue;
                int newMod = (mod + E[e].w) % signalSpeed;
                stackNode[top] = nxt;
                stackParent[top] = node;
                stackMod[top] = newMod;
                stackComp[top] = comp;
                top++;
            }
        }

        long long S = 0;
        for (int i = 0; i < d; ++i) S += cnt[i];
        long long pairs = 0;
        for (int i = 0; i < d; ++i) {
            pairs += (S - cnt[i]) * cnt[i];
        }
        answer[c] = (int)(pairs / 2);
        free(cnt);
    }

    free(stackNode);
    free(stackParent);
    free(stackMod);
    free(stackComp);
    free(E);
    free(head);
    free(deg);

    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int[] CountPairsOfConnectableServers(int[][] edges, int signalSpeed) {
        int n = 0;
        foreach (var e in edges) {
            n = Math.Max(n, Math.Max(e[0], e[1]));
        }
        n += 1;

        var graph = new List<(int to, int w)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, int)>();
        foreach (var e in edges) {
            int a = e[0], b = e[1], w = e[2];
            graph[a].Add((b, w));
            graph[b].Add((a, w));
        }

        var result = new long[n];

        for (int root = 0; root < n; ++root) {
            // count of nodes in each neighbor component whose distance to root is divisible by signalSpeed
            var cnt = new Dictionary<int, int>();
            foreach (var edge in graph[root]) cnt[edge.to] = 0;

            var stack = new Stack<(int node, int parent, int origin, int mod)>();
            foreach (var edge in graph[root]) {
                int nb = edge.to;
                int mod = edge.w % signalSpeed;
                stack.Push((nb, root, nb, mod));
            }

            while (stack.Count > 0) {
                var cur = stack.Pop();
                if (cur.mod == 0) {
                    cnt[cur.origin] = cnt[cur.origin] + 1;
                }
                foreach (var e2 in graph[cur.node]) {
                    if (e2.to == cur.parent) continue;
                    int newMod = (cur.mod + e2.w) % signalSpeed;
                    stack.Push((e2.to, cur.node, cur.origin, newMod));
                }
            }

            long total = 0;
            foreach (var v in cnt.Values) total += v;

            long pairs = 0;
            foreach (var v in cnt.Values) {
                pairs += (total - v) * v;
            }
            result[root] = pairs / 2; // each unordered pair counted twice
        }

        var ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = (int)result[i];
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @param {number} signalSpeed
 * @return {number[]}
 */
var countPairsOfConnectableServers = function(edges, signalSpeed) {
    // determine number of nodes
    let maxNode = 0;
    for (const [a, b] of edges) {
        if (a > maxNode) maxNode = a;
        if (b > maxNode) maxNode = b;
    }
    const n = maxNode + 1;

    // build adjacency list
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }

    // DFS to count nodes whose distance modulo signalSpeed == 0
    function dfs(node, parent, mod) {
        let cnt = (mod === 0) ? 1 : 0;
        for (const [nei, w] of adj[node]) {
            if (nei === parent) continue;
            const newMod = (mod + w) % signalSpeed;
            cnt += dfs(nei, node, newMod);
        }
        return cnt;
    }

    const result = Array(n).fill(0);

    for (let c = 0; c < n; ++c) {
        const childCounts = [];
        for (const [nei, w] of adj[c]) {
            const startMod = w % signalSpeed;
            const cnt = dfs(nei, c, startMod);
            childCounts.push(cnt);
        }
        let sum = 0;
        for (const v of childCounts) sum += v;
        let pairs = 0;
        for (const v of childCounts) {
            pairs += v * (sum - v);
        }
        result[c] = pairs / 2; // each pair counted twice
    }

    return result;
};
```

## Typescript

```typescript
function countPairsOfConnectableServers(edges: number[][], signalSpeed: number): number[] {
    const n = edges.length + 1;
    const adj: { to: number; w: number }[][] = Array.from({ length: n }, () => []);
    for (const [a, b, w] of edges) {
        adj[a].push({ to: b, w });
        adj[b].push({ to: a, w });
    }

    function dfs(node: number, parent: number, distMod: number): number {
        let cnt = distMod === 0 ? 1 : 0;
        for (const e of adj[node]) {
            if (e.to === parent) continue;
            cnt += dfs(e.to, node, (distMod + e.w) % signalSpeed);
        }
        return cnt;
    }

    const result: number[] = new Array(n).fill(0);
    for (let c = 0; c < n; ++c) {
        const childCounts: number[] = [];
        for (const e of adj[c]) {
            const cnt = dfs(e.to, c, e.w % signalSpeed);
            childCounts.push(cnt);
        }
        let total = 0;
        let sumSq = 0;
        for (const x of childCounts) {
            total += x;
            sumSq += x * x;
        }
        result[c] = (total * total - sumSq) / 2;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @param Integer $signalSpeed
     * @return Integer[]
     */
    function countPairsOfConnectableServers($edges, $signalSpeed) {
        $max = 0;
        foreach ($edges as $e) {
            $max = max($max, $e[0], $e[1]);
        }
        $n = $max + 1;

        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            [$u, $v, $w] = $e;
            $adj[$u][] = [$v, $w];
            $adj[$v][] = [$u, $w];
        }

        $result = array_fill(0, $n, 0);

        for ($c = 0; $c < $n; $c++) {
            $cnts = [];
            foreach ($adj[$c] as $edge) {
                [$nbr, $w] = $edge;
                $cnt = $this->dfsCount($nbr, $c, $w % $signalSpeed, $adj, $signalSpeed);
                $cnts[] = $cnt;
            }
            $S = array_sum($cnts);
            $pairs = 0;
            foreach ($cnts as $cnt) {
                $pairs += $cnt * ($S - $cnt);
            }
            $result[$c] = intdiv($pairs, 2);
        }

        return $result;
    }

    private function dfsCount($node, $parent, $distMod, $adj, $signalSpeed) {
        $cnt = ($distMod == 0) ? 1 : 0;
        foreach ($adj[$node] as $edge) {
            [$next, $w] = $edge;
            if ($next === $parent) continue;
            $newMod = ($distMod + $w) % $signalSpeed;
            $cnt += $this->dfsCount($next, $node, $newMod, $adj, $signalSpeed);
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func countPairsOfConnectableServers(_ edges: [[Int]], _ signalSpeed: Int) -> [Int] {
        let n = edges.count + 1
        var adj = Array(repeating: [(to: Int, w: Int)](), count: n)
        for e in edges {
            let a = e[0], b = e[1], w = e[2]
            adj[a].append((to: b, w: w))
            adj[b].append((to: a, w: w))
        }
        var answer = Array(repeating: 0, count: n)
        let speedMod = Int64(signalSpeed)

        func dfs(_ node: Int, _ parent: Int, _ dist: Int64, _ rootIdx: Int, _ cnt: inout [Int]) {
            if dist % speedMod == 0 {
                cnt[rootIdx] += 1
            }
            for edge in adj[node] {
                let nxt = edge.to
                if nxt == parent { continue }
                dfs(nxt, node, dist + Int64(edge.w), rootIdx, &cnt)
            }
        }

        for c in 0..<n {
            let deg = adj[c].count
            var cnt = Array(repeating: 0, count: deg)

            for (i, edge) in adj[c].enumerated() {
                dfs(edge.to, c, Int64(edge.w), i, &cnt)
            }

            let totalNodes = cnt.reduce(0, +)
            var pairSum = 0
            for v in cnt {
                pairSum += v * (totalNodes - v)
            }
            answer[c] = pairSum / 2
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPairsOfConnectableServers(edges: Array<IntArray>, signalSpeed: Int): IntArray {
        val n = edges.size + 1
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (e in edges) {
            val a = e[0]
            val b = e[1]
            val w = e[2]
            adj[a].add(Pair(b, w))
            adj[b].add(Pair(a, w))
        }

        fun dfs(u: Int, parent: Int, distMod: Int): Int {
            var cnt = if (distMod == 0) 1 else 0
            for ((v, w) in adj[u]) {
                if (v == parent) continue
                cnt += dfs(v, u, (distMod + w) % signalSpeed)
            }
            return cnt
        }

        val result = IntArray(n)
        for (root in 0 until n) {
            val childCounts = mutableListOf<Int>()
            for ((nbr, w) in adj[root]) {
                val initDistMod = w % signalSpeed
                val cnt = dfs(nbr, root, initDistMod)
                childCounts.add(cnt)
            }
            var total = 0
            for (c in childCounts) total += c
            var pairs = total.toLong() * (total - 1) / 2
            for (c in childCounts) {
                pairs -= c.toLong() * (c - 1) / 2
            }
            result[root] = pairs.toInt()
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> countPairsOfConnectableServers(List<List<int>> edges, int signalSpeed) {
    int n = edges.length + 1;
    var adj = List.generate(n, (_) => <_Edge>[]);
    for (var e in edges) {
      int a = e[0], b = e[1], w = e[2];
      adj[a].add(_Edge(b, w));
      adj[b].add(_Edge(a, w));
    }
    List<int> result = List.filled(n, 0);
    for (int root = 0; root < n; ++root) {
      List<int> childCounts = [];
      for (var e in adj[root]) {
        int cnt = _dfs(e.to, root, e.w % signalSpeed, adj, signalSpeed);
        childCounts.add(cnt);
      }
      int S = 0;
      int sumSq = 0;
      for (int c in childCounts) {
        S += c;
        sumSq += c * c;
      }
      result[root] = ((S * S - sumSq) ~/ 2);
    }
    return result;
  }

  int _dfs(int node, int parent, int curMod, List<List<_Edge>> adj, int signalSpeed) {
    int cnt = (curMod == 0) ? 1 : 0;
    for (var e in adj[node]) {
      if (e.to != parent) {
        cnt += _dfs(e.to, node, (curMod + e.w) % signalSpeed, adj, signalSpeed);
      }
    }
    return cnt;
  }
}

class _Edge {
  int to;
  int w;
  _Edge(this.to, this.w);
}
```

## Golang

```go
func countPairsOfConnectableServers(edges [][]int, signalSpeed int) []int {
    n := len(edges) + 1
    type edge struct{ to, w int }
    adj := make([][]edge, n)
    for _, e := range edges {
        a, b, w := e[0], e[1], e[2]
        adj[a] = append(adj[a], edge{b, w})
        adj[b] = append(adj[b], edge{a, w})
    }

    var dfs func(u, parent, mod int) int
    dfs = func(u, parent, mod int) int {
        cnt := 0
        if mod == 0 {
            cnt = 1
        }
        for _, e := range adj[u] {
            if e.to == parent {
                continue
            }
            newMod := (mod + e.w) % signalSpeed
            cnt += dfs(e.to, u, newMod)
        }
        return cnt
    }

    res := make([]int, n)
    for c := 0; c < n; c++ {
        total := 0
        var parts []int
        for _, e := range adj[c] {
            cnt := dfs(e.to, c, e.w%signalSpeed)
            parts = append(parts, cnt)
            total += cnt
        }
        totalPairs := int64(total) * int64(total-1) / 2
        for _, p := range parts {
            totalPairs -= int64(p) * int64(p-1) / 2
        }
        res[c] = int(totalPairs)
    }
    return res
}
```

## Ruby

```ruby
def count_pairs_of_connectable_servers(edges, signal_speed)
  n = edges.size + 1
  adj = Array.new(n) { [] }
  edges.each do |u, v, w|
    adj[u] << [v, w]
    adj[v] << [u, w]
  end

  result = Array.new(n, 0)

  (0...n).each do |c|
    dist_mod = Array.new(n)
    dir = Array.new(n) # first neighbor of c on the path to node
    queue = [c]
    head = 0
    dist_mod[c] = 0
    dir[c] = -1

    while head < queue.size
      v = queue[head]
      head += 1
      adj[v].each do |to, w|
        next if !dist_mod[to].nil?
        dist_mod[to] = (dist_mod[v] + w) % signal_speed
        dir[to] = (v == c) ? to : dir[v]
        queue << to
      end
    end

    cnt_per_dir = Hash.new(0)
    (0...n).each do |node|
      next if node == c
      if dist_mod[node] % signal_speed == 0
        d = dir[node]
        cnt_per_dir[d] += 1
      end
    end

    total = cnt_per_dir.values.sum
    pairs = 0
    cnt_per_dir.each_value do |cnt|
      pairs += cnt * (total - cnt)
    end
    result[c] = pairs / 2
  end

  result
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.ArrayBuffer

  def countPairsOfConnectableServers(edges: Array[Array[Int]], signalSpeed: Int): Array[Int] = {
    val n = edges.length + 1
    val adj = Array.fill(n)(new ArrayBuffer[(Int, Int)]())
    for (e <- edges) {
      val a = e(0)
      val b = e(1)
      val w = e(2)
      adj(a).append((b, w))
      adj(b).append((a, w))
    }

    def dfs(u: Int, parent: Int, curMod: Int): Int = {
      var cnt = if (curMod == 0) 1 else 0
      for ((v, w) <- adj(u)) {
        if (v != parent) {
          val nextMod = (curMod + w) % signalSpeed
          cnt += dfs(v, u, nextMod)
        }
      }
      cnt
    }

    val result = new Array[Int](n)

    for (root <- 0 until n) {
      var sum: Long = 0L
      var sumSq: Long = 0L
      for ((nbr, w) <- adj(root)) {
        val cnt = dfs(nbr, root, w % signalSpeed)
        sum += cnt
        sumSq += cnt.toLong * cnt
      }
      val pairs = (sum * sum - sumSq) / 2
      result(root) = pairs.toInt
    }

    result
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn count_pairs_of_connectable_servers(edges: Vec<Vec<i32>>, signal_speed: i32) -> Vec<i32> {
        let n = edges.len() + 1;
        let mut adj: Vec<Vec<(usize, i32)>> = vec![Vec::new(); n];
        for e in edges.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            let w = e[2];
            adj[a].push((b, w));
            adj[b].push((a, w));
        }

        fn dfs(
            u: usize,
            parent: usize,
            cur_mod: i32,
            s: i32,
            adj: &Vec<Vec<(usize, i32)>>,
        ) -> i32 {
            let mut cnt = if cur_mod == 0 { 1 } else { 0 };
            for &(v, w) in &adj[u] {
                if v != parent {
                    let next_mod = (cur_mod + w % s) % s;
                    cnt += dfs(v, u, next_mod, s, adj);
                }
            }
            cnt
        }

        let mut answer: Vec<i32> = vec![0; n];
        for root in 0..n {
            let mut child_counts: Vec<i32> = Vec::new();
            for &(v, w) in &adj[root] {
                let start_mod = w % signal_speed;
                let cnt = dfs(v, root, start_mod, signal_speed, &adj);
                child_counts.push(cnt);
            }
            let total: i32 = child_counts.iter().sum();
            let mut pairs: i64 = 0;
            for &c in &child_counts {
                pairs += (c as i64) * ((total - c) as i64);
            }
            pairs /= 2; // each unordered pair counted twice
            answer[root] = pairs as i32;
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (count-pairs-of-connectable-servers edges signalSpeed)
  (-> (listof (listof exact-integer?)) exact-integer? (listof exact-integer?))
  (let* ((n
          (let loop ((es edges) (mx -1))
            (if (null? es)
                (+ mx 1)
                (let* ((e (car es))
                       (a (list-ref e 0))
                       (b (list-ref e 1))
                       (new-mx (max mx a b)))
                  (loop (cdr es) new-mx)))))
         (adj (make-vector n '()))
         (_
          (for-each
           (lambda (e)
             (let ((a (list-ref e 0))
                   (b (list-ref e 1))
                   (w (list-ref e 2)))
               (vector-set! adj a (cons (list b w) (vector-ref adj a)))
               (vector-set! adj b (cons (list a w) (vector-ref adj b)))))
           edges))
         (result
          (let loop ((c 0) (acc '()))
            (if (= c n)
                (reverse acc)
                (let* ((counts (make-vector n 0))
                       (visit
                        (lambda (node parent dist label)
                          (when (and (not (= node c))
                                     (= (modulo dist signalSpeed) 0)
                                     (>= label 0))
                            (vector-set! counts label (+ (vector-ref counts label) 1)))
                          (for-each
                           (lambda (nbr-w)
                             (let ((nbr (list-ref nbr-w 0))
                                   (w   (list-ref nbr-w 1)))
                               (when (not (= nbr parent))
                                 (let ((new-label (if (= label -1) nbr label)))
                                   (visit nbr node (+ dist w) new-label)))))
                           (vector-ref adj node))))) )
                  (visit c -1 0 -1)
                  ;; compute total pairs for this root
                  (let* ((sum-subtrees
                          (let loop2 ((i 0) (s 0))
                            (if (= i n) s
                                (loop2 (+ i 1) (+ s (vector-ref counts i))))))
                         (total-pairs
                          (let loop3 ((i 0) (tot 0))
                            (if (= i n) tot
                                (let ((v (vector-ref counts i)))
                                  (if (> v 0)
                                      (loop3 (+ i 1)
                                             (+ tot (quotient (* (- sum-subtrees v) v) 2)))
                                      (loop3 (+ i 1) tot)))))))
                    (loop (+ c 1) (cons total-pairs acc))))))
          result))
  result)
```

## Erlang

```erlang
-spec count_pairs_of_connectable_servers(Edges :: [[integer()]], SignalSpeed :: integer()) -> [integer()].
count_pairs_of_connectable_servers(Edges, SignalSpeed) ->
    N = length(Edges) + 1,
    Adj = build_adj(N, Edges),
    lists:map(fun(Node) -> count_for_node(Node, Adj, SignalSpeed) end,
              lists:seq(0, N - 1)).

build_adj(N, Edges) ->
    EmptyAdj = maps:from_list([{I, []} || I <- lists:seq(0, N - 1)]),
    lists:foldl(fun([A, B, W], Acc) ->
        Acc1 = maps:update_with(A,
                fun(L) -> [{B, W} | L] end,
                [{B, W}], Acc),
        maps:update_with(B,
                fun(L) -> [{A, W} | L] end,
                [{A, W}], Acc1)
    end, EmptyAdj, Edges).

count_for_node(Root, Adj, Speed) ->
    Children = maps:get(Root, Adj),
    Cnts = [subtree_count(Child, Weight, Root, Adj, Speed) ||
            {Child, Weight} <- Children],
    S = lists:sum(Cnts),
    PairSum = lists:foldl(fun(Cnt, Acc) -> Acc + Cnt * (S - Cnt) end,
                          0, Cnts),
    PairSum div 2.

subtree_count(Node, EdgeW, Parent, Adj, Speed) ->
    dfs_collect(Node, EdgeW rem Speed, Parent, Adj, Speed).

dfs_collect(Node, Mod, Parent, Adj, Speed) ->
    CountHere = if Mod == 0 -> 1; true -> 0 end,
    Children = maps:get(Node, Adj),
    SubCounts = [dfs_collect(Next, (Mod + W) rem Speed, Node, Adj, Speed) ||
                 {Next, W} <- Children, Next =/= Parent],
    CountHere + lists:sum(SubCounts).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_pairs_of_connectable_servers(edges :: [[integer]], signal_speed :: integer) :: [integer]
  def count_pairs_of_connectable_servers(edges, signal_speed) do
    n =
      edges
      |> Enum.flat_map(fn [a, b, _] -> [a, b] end)
      |> Enum.max()
      |> Kernel.+(1)

    adj = build_adj(n, edges)

    0..(n - 1)
    |> Enum.map(fn c ->
      neighbors = Map.get(adj, c, [])

      nums =
        Enum.map(neighbors, fn {v, w} ->
          dfs(v, c, rem(w, signal_speed), adj, signal_speed)
        end)

      s = Enum.sum(nums)

      if length(nums) < 2 do
        0
      else
        Enum.reduce(nums, 0, fn x, acc -> acc + (s - x) * x end)
        |> div(2)
      end
    end)
  end

  defp build_adj(n, edges) do
    base = for i <- 0..(n - 1), into: %{}, do: {i, []}

    Enum.reduce(edges, base, fn [a, b, w], acc ->
      acc
      |> Map.update!(a, fn list -> [{b, w} | list] end)
      |> Map.update!(b, fn list -> [{a, w} | list] end)
    end)
  end

  defp dfs(node, parent, dist_mod, adj, speed) do
    cnt = if rem(dist_mod, speed) == 0, do: 1, else: 0

    Enum.reduce(Map.get(adj, node, []), cnt, fn {nbr, w}, acc ->
      if nbr == parent do
        acc
      else
        acc + dfs(nbr, node, rem(dist_mod + w, speed), adj, speed)
      end
    end)
  end
end
```

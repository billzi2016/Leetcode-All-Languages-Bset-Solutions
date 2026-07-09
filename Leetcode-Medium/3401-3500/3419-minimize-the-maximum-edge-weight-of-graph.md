# 3419. Minimize the Maximum Edge Weight of Graph

## Cpp

```cpp
class Solution {
public:
    int minMaxWeight(int n, vector<vector<int>>& edges, int threshold) {
        // Collect all unique weights
        vector<int> ws;
        ws.reserve(edges.size());
        for (auto &e : edges) ws.push_back(e[2]);
        sort(ws.begin(), ws.end());
        ws.erase(unique(ws.begin(), ws.end()), ws.end());
        if (ws.empty()) return -1;

        // Helper to check feasibility with max allowed weight 'limit'
        auto feasible = [&](int limit)->bool{
            vector<vector<int>> revAdj(n);
            for (auto &e : edges) {
                if (e[2] <= limit) {
                    int u = e[0], v = e[1];
                    // reverse edge: from v to u
                    revAdj[v].push_back(u);
                }
            }
            vector<int> dist(n, -1);
            queue<int> q;
            dist[0] = 0;
            q.push(0);
            while (!q.empty()) {
                int cur = q.front(); q.pop();
                for (int nxt : revAdj[cur]) {
                    if (dist[nxt] == -1) {
                        dist[nxt] = dist[cur] + 1;
                        q.push(nxt);
                    }
                }
            }
            for (int d : dist) {
                if (d == -1 || d > threshold) return false;
            }
            return true;
        };

        // If even the largest weight cannot satisfy, return -1
        if (!feasible(ws.back())) return -1;

        int lo = 0, hi = ws.size() - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (feasible(ws[mid])) hi = mid;
            else lo = mid + 1;
        }
        return ws[lo];
    }
};
```

## Java

```java
class Solution {
    public int minMaxWeight(int n, int[][] edges, int threshold) {
        int maxW = 0;
        for (int[] e : edges) {
            maxW = Math.max(maxW, e[2]);
        }
        int left = 1, right = maxW;
        int answer = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canReachAll(n, edges, threshold, mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return answer;
    }

    private boolean canReachAll(int n, int[][] edges, int threshold, int limit) {
        @SuppressWarnings("unchecked")
        java.util.ArrayList<Integer>[] adj = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new java.util.ArrayList<>();
        for (int[] e : edges) {
            if (e[2] <= limit) {
                // reverse edge: from destination to source
                adj[e[1]].add(e[0]);
            }
        }
        int[] dist = new int[n];
        java.util.Arrays.fill(dist, Integer.MAX_VALUE);
        java.util.ArrayDeque<Integer> q = new java.util.ArrayDeque<>();
        dist[0] = 0;
        q.add(0);
        while (!q.isEmpty()) {
            int cur = q.poll();
            if (dist[cur] == threshold) continue; // cannot go deeper
            for (int nb : adj[cur]) {
                if (dist[nb] > dist[cur] + 1) {
                    dist[nb] = dist[cur] + 1;
                    q.add(nb);
                }
            }
        }
        for (int d : dist) {
            if (d == Integer.MAX_VALUE || d > threshold) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def minMaxWeight(self, n, edges, threshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        from collections import deque

        max_w = 0
        for _, _, w in edges:
            if w > max_w:
                max_w = w

        # Build adjacency list grouped by weight limit check on the fly
        def feasible(limit):
            adj = [[] for _ in range(n)]
            for a, b, w in edges:
                if w <= limit:
                    # reverse edge: from b we can go to a (original a->b)
                    adj[b].append(a)

            dist = [-1] * n
            q = deque()
            q.append(0)
            dist[0] = 0
            while q:
                u = q.popleft()
                if dist[u] == threshold:  # no need to go deeper from this node
                    continue
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)

            return all(d != -1 and d <= threshold for d in dist)

        ans = -1
        lo, hi = 1, max_w
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
```

## Python3

```python
class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        from collections import deque

        max_w = 0
        for _, _, w in edges:
            if w > max_w:
                max_w = w

        # helper to check feasibility with weight limit lim
        def feasible(lim: int) -> bool:
            adj = [[] for _ in range(n)]
            for a, b, w in edges:
                if w <= lim:
                    # reverse edge for BFS from 0
                    adj[b].append(a)
            dist = [-1] * n
            q = deque([0])
            dist[0] = 0
            while q:
                u = q.popleft()
                if dist[u] == threshold:
                    continue
                nd = dist[u] + 1
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = nd
                        q.append(v)
            return all(d != -1 and d <= threshold for d in dist)

        # quick check if impossible even with max weight
        if not feasible(max_w):
            return -1

        lo, hi = 1, max_w
        ans = max_w
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
```

## C

```c
int minMaxWeight(int n, int** edges, int edgesSize, int* edgesColSize, int threshold) {
    // Find maximum weight among all edges
    int maxW = 0;
    for (int i = 0; i < edgesSize; ++i) {
        if (edges[i][2] > maxW) maxW = edges[i][2];
    }
    
    // Allocate memory for adjacency representation (reversed graph)
    int *head = (int*)malloc(n * sizeof(int));
    int *to   = (int*)malloc(edgesSize * sizeof(int));
    int *next = (int*)malloc(edgesSize * sizeof(int));
    int *dist = (int*)malloc(n * sizeof(int));
    int *queue = (int*)malloc(n * sizeof(int));
    
    // Helper lambda to test feasibility for a given max weight
    int feasible(int limit) {
        for (int i = 0; i < n; ++i) head[i] = -1;
        int eidx = 0;
        for (int i = 0; i < edgesSize; ++i) {
            if (edges[i][2] <= limit) {
                int a = edges[i][0];
                int b = edges[i][1];
                // reversed edge: b -> a
                to[eidx] = a;
                next[eidx] = head[b];
                head[b] = eidx++;
            }
        }
        for (int i = 0; i < n; ++i) dist[i] = -1;
        int front = 0, back = 0;
        queue[back++] = 0;
        dist[0] = 0;
        while (front < back) {
            int u = queue[front++];
            for (int ei = head[u]; ei != -1; ei = next[ei]) {
                int v = to[ei];
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    if (dist[v] > threshold) return 0; // early exit
                    queue[back++] = v;
                }
            }
        }
        for (int i = 0; i < n; ++i) {
            if (dist[i] == -1 || dist[i] > threshold) return 0;
        }
        return 1;
    };
    
    int left = 1, right = maxW, answer = -1;
    while (left <= right) {
        int mid = left + ((right - left) >> 1);
        if (feasible(mid)) {
            answer = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    free(head);
    free(to);
    free(next);
    free(dist);
    free(queue);
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int MinMaxWeight(int n, int[][] edges, int threshold) {
        int maxW = 0;
        foreach (var e in edges) {
            if (e[2] > maxW) maxW = e[2];
        }

        // Helper to test feasibility with weight limit 'limit'
        bool Feasible(int limit) {
            var adj = new List<int>[n];
            for (int i = 0; i < n; i++) adj[i] = new List<int>();
            foreach (var e in edges) {
                if (e[2] <= limit) {
                    int from = e[0];
                    int to = e[1];
                    // reverse edge for BFS from node 0
                    adj[to].Add(from);
                }
            }

            var dist = new int[n];
            for (int i = 0; i < n; i++) dist[i] = -1;
            var q = new System.Collections.Generic.Queue<int>();
            dist[0] = 0;
            q.Enqueue(0);

            while (q.Count > 0) {
                int u = q.Dequeue();
                if (dist[u] == threshold) continue; // cannot go deeper
                foreach (int v in adj[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.Enqueue(v);
                    }
                }
            }

            for (int i = 0; i < n; i++) {
                if (dist[i] == -1 || dist[i] > threshold) return false;
            }
            return true;
        }

        // If even with all edges it's impossible, return -1
        if (!Feasible(maxW)) return -1;

        int left = 1, right = maxW, ans = maxW;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            if (Feasible(mid)) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
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
 * @param {number} threshold
 * @return {number}
 */
var minMaxWeight = function(n, edges, threshold) {
    let maxW = 0;
    for (const e of edges) {
        if (e[2] > maxW) maxW = e[2];
    }

    const canReach = (limit) => {
        const adj = Array.from({ length: n }, () => []);
        for (const [a, b, w] of edges) {
            if (w <= limit) {
                // reverse edge to run BFS from node 0
                adj[b].push(a);
            }
        }

        const dist = new Int32Array(n).fill(-1);
        const queue = [];
        dist[0] = 0;
        queue.push(0);
        let qIdx = 0;

        while (qIdx < queue.length) {
            const u = queue[qIdx++];
            const du = dist[u];
            if (du >= threshold) continue; // further nodes would exceed limit
            for (const v of adj[u]) {
                if (dist[v] === -1) {
                    dist[v] = du + 1;
                    queue.push(v);
                }
            }
        }

        for (let i = 0; i < n; ++i) {
            if (dist[i] === -1 || dist[i] > threshold) return false;
        }
        return true;
    };

    // If even the largest weight cannot satisfy, answer is -1
    if (!canReach(maxW)) return -1;

    let left = 1, right = maxW, ans = maxW;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (canReach(mid)) {
            ans = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minMaxWeight(n: number, edges: number[][], threshold: number): number {
    const weights = Array.from(new Set(edges.map(e => e[2]))).sort((a, b) => a - b);
    let left = 0, right = weights.length - 1;
    let answer = -1;

    while (left <= right) {
        const mid = (left + right) >> 1;
        const limit = weights[mid];

        const adj: number[][] = Array.from({ length: n }, () => []);
        for (const [a, b, w] of edges) {
            if (w <= limit) {
                adj[b].push(a); // invert edge
            }
        }

        const visited = new Uint8Array(n);
        const queue: number[] = [];
        visited[0] = 1;
        queue.push(0);
        for (let q = 0; q < queue.length; ++q) {
            const u = queue[q];
            for (const v of adj[u]) {
                if (!visited[v]) {
                    visited[v] = 1;
                    queue.push(v);
                }
            }
        }

        let reachable = 0;
        for (let i = 0; i < n; ++i) if (visited[i]) ++reachable;

        if (reachable >= n - threshold) {
            answer = limit;
            right = mid - 1;
        } else {
            left = mid + 1;
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
     * @param Integer $threshold
     * @return Integer
     */
    function minMaxWeight($n, $edges, $threshold) {
        $maxW = 0;
        foreach ($edges as $e) {
            if ($e[2] > $maxW) $maxW = $e[2];
        }

        // helper closure to test feasibility for a given weight limit
        $feasible = function($limit) use ($n, $edges, $threshold) {
            $adj = array_fill(0, $n, []);
            foreach ($edges as $e) {
                if ($e[2] <= $limit) {
                    // reverse the edge: from destination to source
                    $adj[$e[1]][] = $e[0];
                }
            }

            $queue = new SplQueue();
            $dist  = array_fill(0, $n, -1);
            $queue->enqueue(0);
            $dist[0] = 0;
            $visited = 1;

            while (!$queue->isEmpty()) {
                $u = $queue->dequeue();
                if ($dist[$u] == $threshold) continue; // depth limit reached
                foreach ($adj[$u] as $v) {
                    if ($dist[$v] === -1) {
                        $dist[$v] = $dist[$u] + 1;
                        $visited++;
                        if ($visited == $n) return true;
                        $queue->enqueue($v);
                    }
                }
            }
            return $visited == $n;
        };

        // quick check: if even the maximum weight cannot satisfy, return -1
        if (!$feasible($maxW)) {
            return -1;
        }

        $low = 0;
        $high = $maxW;
        $ans = -1;

        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            if ($feasible($mid)) {
                $ans = $mid;
                $high = $mid - 1;
            } else {
                $low = $mid + 1;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minMaxWeight(_ n: Int, _ edges: [[Int]], _ threshold: Int) -> Int {
        var edgeList = [(from: Int, to: Int, w: Int)]()
        var maxW = 0
        for e in edges {
            let a = e[0], b = e[1], w = e[2]
            edgeList.append((a, b, w))
            if w > maxW { maxW = w }
        }
        
        func can(_ limit: Int) -> Bool {
            var adj = [[Int]](repeating: [], count: n)
            for e in edgeList where e.w <= limit {
                // reverse the direction
                adj[e.to].append(e.from)
            }
            var visited = [Bool](repeating: false, count: n)
            visited[0] = true
            var current = [0]
            var steps = 0
            while steps < threshold && !current.isEmpty {
                var next = [Int]()
                for node in current {
                    for nb in adj[node] where !visited[nb] {
                        visited[nb] = true
                        next.append(nb)
                    }
                }
                current = next
                steps += 1
            }
            for v in visited where !v { return false }
            return true
        }
        
        var left = 1
        var right = maxW
        var answer = -1
        while left <= right {
            let mid = (left + right) / 2
            if can(mid) {
                answer = mid
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMaxWeight(n: Int, edges: Array<IntArray>, threshold: Int): Int {
        var maxW = 0
        for (e in edges) if (e[2] > maxW) maxW = e[2]

        var lo = 1
        var hi = maxW
        var answer = -1

        while (lo <= hi) {
            val mid = (lo + hi) ushr 1

            // build reversed adjacency list using only edges with weight <= mid
            val adj = Array(n) { mutableListOf<Int>() }
            for (e in edges) {
                if (e[2] <= mid) {
                    // original edge a -> b, reversed b -> a
                    adj[e[1]].add(e[0])
                }
            }

            // BFS from node 0 in the reversed graph
            val visited = BooleanArray(n)
            val queue: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
            visited[0] = true
            queue.add(0)
            var count = 1

            while (!queue.isEmpty()) {
                val cur = queue.poll()
                for (next in adj[cur]) {
                    if (!visited[next]) {
                        visited[next] = true
                        queue.add(next)
                        count++
                    }
                }
            }

            if (count == n) {
                answer = mid
                hi = mid - 1
            } else {
                lo = mid + 1
            }
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minMaxWeight(int n, List<List<int>> edges, int threshold) {
    // Extract unique sorted weights
    var weightSet = <int>{};
    for (var e in edges) {
      weightSet.add(e[2]);
    }
    var weights = weightSet.toList()..sort();
    if (weights.isEmpty) return -1;

    bool can(int limit) {
      // Build reversed adjacency list using only edges with weight <= limit
      var revAdj = List<List<int>>.generate(n, (_) => []);
      for (var e in edges) {
        if (e[2] <= limit) {
          revAdj[e[1]].add(e[0]); // reverse direction
        }
      }
      // BFS from node 0 up to depth 'threshold'
      var dist = List<int>.filled(n, -1);
      var queue = <int>[];
      int head = 0;
      dist[0] = 0;
      queue.add(0);
      while (head < queue.length) {
        int u = queue[head++];
        if (dist[u] == threshold) continue;
        for (var v in revAdj[u]) {
          if (dist[v] == -1) {
            dist[v] = dist[u] + 1;
            queue.add(v);
          }
        }
      }
      // Check all nodes are reachable within the allowed steps
      for (int d in dist) {
        if (d == -1) return false;
      }
      return true;
    }

    int left = 0, right = weights.length - 1;
    int answer = -1;
    while (left <= right) {
      int mid = (left + right) >> 1;
      if (can(weights[mid])) {
        answer = weights[mid];
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
    return answer;
  }
}
```

## Golang

```go
func minMaxWeight(n int, edges [][]int, threshold int) int {
	type Edge struct {
		from, to, w int
	}
	revEdges := make([]Edge, len(edges))
	weightsMap := make(map[int]struct{})
	for i, e := range edges {
		a, b, w := e[0], e[1], e[2]
		// reverse direction: b -> a
		revEdges[i] = Edge{from: b, to: a, w: w}
		weightsMap[w] = struct{}{}
	}
	weights := make([]int, 0, len(weightsMap))
	for w := range weightsMap {
		weights = append(weights, w)
	}
	if len(weights) == 0 {
		return -1
	}
	// sort unique weights
	sort.Ints(weights)

	feasible := func(limit int) bool {
		adj := make([][]int, n)
		for _, e := range revEdges {
			if e.w <= limit {
				adj[e.from] = append(adj[e.from], e.to)
			}
		}
		dist := make([]int, n)
		for i := 0; i < n; i++ {
			dist[i] = -1
		}
		queue := make([]int, 0, n)
		dist[0] = 0
		queue = append(queue, 0)
		head := 0
		for head < len(queue) {
			u := queue[head]
			head++
			if dist[u] == threshold {
				continue
			}
			for _, v := range adj[u] {
				if dist[v] == -1 {
					dist[v] = dist[u] + 1
					queue = append(queue, v)
				}
			}
		}
		for i := 0; i < n; i++ {
			if dist[i] == -1 {
				return false
			}
		}
		return true
	}

	// check if possible with maximum weight
	if !feasible(weights[len(weights)-1]) {
		return -1
	}
	lo, hi := 0, len(weights)-1
	ans := weights[hi]
	for lo <= hi {
		mid := (lo + hi) / 2
		if feasible(weights[mid]) {
			ans = weights[mid]
			hi = mid - 1
		} else {
			lo = mid + 1
		}
	}
	return ans
}

import "sort"
```

## Ruby

```ruby
def feasible?(n, edges_sorted, limit, threshold)
  adj = Array.new(n) { [] }
  edges_sorted.each do |e|
    a, b, w = e
    break if w > limit
    adj[b] << a
  end
  dist = Array.new(n, -1)
  queue = [0]
  dist[0] = 0
  head = 0
  while head < queue.size
    u = queue[head]
    head += 1
    next if dist[u] == threshold
    adj[u].each do |v|
      if dist[v] == -1
        dist[v] = dist[u] + 1
        queue << v
      end
    end
  end
  (0...n).all? { |i| dist[i] != -1 && dist[i] <= threshold }
end

def min_max_weight(n, edges, threshold)
  max_w = edges.map { |e| e[2] }.max
  left = 1
  right = max_w
  ans = -1
  edges_sorted = edges.sort_by { |e| e[2] }

  while left <= right
    mid = (left + right) / 2
    if feasible?(n, edges_sorted, mid, threshold)
      ans = mid
      right = mid - 1
    else
      left = mid + 1
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def minMaxWeight(n: Int, edges: Array[Array[Int]], threshold: Int): Int = {
        if (n == 0) return -1
        val maxW = edges.map(_(2)).max
        var lo = 1
        var hi = maxW
        var answer = -1

        def can(limit: Int): Boolean = {
            val adj = Array.fill[List[Int]](n)(Nil)
            var i = 0
            while (i < edges.length) {
                val e = edges(i)
                if (e(2) <= limit) {
                    // reversed edge from destination to source
                    val a = e(0)
                    val b = e(1)
                    adj(b) = a :: adj(b)
                }
                i += 1
            }

            val visited = new Array[Boolean](n)
            val queue = new java.util.ArrayDeque[(Int, Int)]()
            visited(0) = true
            queue.add((0, 0))

            while (!queue.isEmpty) {
                val (node, dist) = queue.poll()
                if (dist < threshold) {
                    var list = adj(node)
                    while (list != Nil) {
                        val v = list.head
                        if (!visited(v)) {
                            visited(v) = true
                            queue.add((v, dist + 1))
                        }
                        list = list.tail
                    }
                }
            }

            var idx = 0
            while (idx < n) {
                if (!visited(idx)) return false
                idx += 1
            }
            true
        }

        while (lo <= hi) {
            val mid = lo + (hi - lo) / 2
            if (can(mid)) {
                answer = mid
                hi = mid - 1
            } else {
                lo = mid + 1
            }
        }
        answer
    }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn min_max_weight(n: i32, edges: Vec<Vec<i32>>, threshold: i32) -> i32 {
        let n_usize = n as usize;
        if edges.is_empty() {
            return -1;
        }
        // Find maximum weight among all edges
        let mut max_w = 0i32;
        for e in &edges {
            if e[2] > max_w {
                max_w = e[2];
            }
        }

        // Helper closure to test feasibility for a given weight limit
        let feasible = |limit: i32| -> bool {
            let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n_usize];
            for e in &edges {
                if e[2] <= limit {
                    // reverse the edge direction
                    let from = e[1] as usize;
                    let to = e[0] as usize;
                    adj[from].push(to);
                }
            }

            let mut dist: Vec<i32> = vec![-1; n_usize];
            let mut q: VecDeque<usize> = VecDeque::new();
            dist[0] = 0;
            q.push_back(0);

            while let Some(u) = q.pop_front() {
                if dist[u] == threshold {
                    continue;
                }
                for &v in &adj[u] {
                    if dist[v] == -1 {
                        dist[v] = dist[u] + 1;
                        q.push_back(v);
                    }
                }
            }

            dist.iter().all(|&d| d != -1)
        };

        // Binary search on answer
        let mut lo = 1i32;
        let mut hi = max_w;
        let mut ans = -1i32;

        while lo <= hi {
            let mid = lo + (hi - lo) / 2;
            if feasible(mid) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (min-max-weight n edges threshold)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([max-w
          (apply max (map third edges))]
         [feasible?
          (lambda (limit)
            (let ([adj (make-vector n '())])
              ;; build reversed adjacency using only edges with weight <= limit
              (for-each
               (lambda (e)
                 (define a (first e))
                 (define b (second e))
                 (define w (third e))
                 (when (<= w limit)
                   (vector-set! adj b (cons a (vector-ref adj b)))))
               edges)
              ;; BFS from 0 up to depth = threshold
              (let ([dist (make-vector n -1)]
                    [queue (make-vector n #f)]
                    [head 0] [tail 0])
                (vector-set! dist 0 0)
                (vector-set! queue tail 0) (set! tail (+ tail 1))
                (let loop ()
                  (if (>= head tail)
                      ;; finished BFS
                      (let check-all ()
                        (for/and ([i (in-range n)])
                          (not (= -1 (vector-ref dist i)))))
                      (let* ([v (vector-ref queue head)]
                             [d (vector-ref dist v)])
                        (set! head (+ head 1))
                        (when (< d threshold)
                          (for-each
                           (lambda (nbr)
                             (when (= -1 (vector-ref dist nbr))
                               (vector-set! dist nbr (+ d 1))
                               (vector-set! queue tail nbr)
                               (set! tail (+ tail 1))))
                           (vector-ref adj v)))
                        (loop))))) ) ) )
         [low 1]
         [high max-w]
         [ans -1])
    ;; first check if any solution exists
    (if (not (feasible? high))
        -1
        (let loop ()
          (when (<= low high)
            (define mid (quotient (+ low high) 2))
            (if (feasible? mid)
                (begin
                  (set! ans mid)
                  (set! high (- mid 1)))
                (set! low (+ mid 1)))
            (loop))))
    ans))
```

## Erlang

```erlang
-spec min_max_weight(integer(), [[integer()]], integer()) -> integer().
min_max_weight(N, Edges, Threshold) ->
    Weights = lists:usort([W || [_A,_B,W] <- Edges]),
    case bin_search(Weights, N, Edges, Threshold, 0, length(Weights) - 1) of
        undefined -> -1;
        Ans -> Ans
    end.

bin_search(_Weights, _N, _Edges, _Threshold, Low, High) when Low > High ->
    undefined;
bin_search(Weights, N, Edges, Threshold, Low, High) ->
    Mid = (Low + High) div 2,
    Wmid = lists:nth(Mid + 1, Weights),
    case feasible(N, Edges, Threshold, Wmid) of
        true ->
            case bin_search(Weights, N, Edges, Threshold, Low, Mid - 1) of
                undefined -> Wmid;
                Res -> Res
            end;
        false ->
            bin_search(Weights, N, Edges, Threshold, Mid + 1, High)
    end.

feasible(N, Edges, Threshold, MaxW) ->
    Adj = build_adj(N, Edges, MaxW),
    bfs(N, Adj, Threshold).

build_adj(N, Edges, MaxW) ->
    Empty = maps:from_list([{I, []} || I <- lists:seq(0, N - 1)]),
    lists:foldl(fun([A, B, W], Acc) ->
        if
            W =< MaxW ->
                Prev = maps:get(B, Acc),
                maps:put(B, [A | Prev], Acc);
            true -> Acc
        end
    end, Empty, Edges).

bfs(N, Adj, Threshold) ->
    Q0 = queue:in({0, 0}, queue:new()),
    Vis0 = #{0 => true},
    bfs_loop(Q0, Vis0, Adj, Threshold, N).

bfs_loop(Q, Visited, Adj, Threshold, N) ->
    case queue:out(Q) of
        {empty, _} ->
            maps:size(Visited) == N;
        {{value, {Node, Dist}}, Q1} ->
            if
                Dist < Threshold ->
                    Neighs = maps:get(Node, Adj),
                    {Q2, Vis2} = lists:foldl(
                        fun(Nbr, {AccQ, AccV}) ->
                            case maps:is_key(Nbr, AccV) of
                                false -> {queue:in({Nbr, Dist + 1}, AccQ), maps:put(Nbr, true, AccV)};
                                true -> {AccQ, AccV}
                            end
                        end,
                        {Q1, Visited},
                        Neighs),
                    bfs_loop(Q2, Vis2, Adj, Threshold, N);
                true ->
                    bfs_loop(Q1, Visited, Adj, Threshold, N)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_max_weight(integer, [[integer]], integer) :: integer
  def min_max_weight(n, edges, threshold) do
    max_w = Enum.max_by(edges, fn [_a, _b, w] -> w end) |> elem(2)

    # build incoming adjacency list: for each node v, store [{u, weight}] where u -> v exists
    in_adj =
      :array.new(n, default: [])
      |> Enum.reduce(edges, fn [a, b, w], acc ->
        list = :array.get(b, acc)
        :array.set(b, [{a, w} | list], acc)
      end)

    feasible = fn limit ->
      dist = :array.new(n, default: -1)
      q = :queue.from_list([0])
      dist = :array.set(0, 0, dist)

      bfs = fn bfs_fun, queue, d_arr ->
        case :queue.out(queue) do
          {:empty, _} ->
            {d_arr, :ok}

          {{:value, v}, q2} ->
            cur_d = :array.get(v, d_arr)
            neighbors = :array.get(v, in_adj)

            {new_dist, new_queue} =
              Enum.reduce(neighbors, {d_arr, q2}, fn {nbr, w}, {da, qa} ->
                if w <= limit and :array.get(nbr, da) == -1 do
                  da = :array.set(nbr, cur_d + 1, da)
                  {da, :queue.in(nbr, qa)}
                else
                  {da, qa}
                end
              end)

            bfs_fun.(bfs_fun, new_queue, new_dist)
        end
      end

      {final_dist, _} = bfs.(bfs, q, dist)

      0..(n - 1)
      |> Enum.all?(fn i ->
        d = :array.get(i, final_dist)
        d != -1 and d <= threshold
      end)
    end

    # quick check: if even the largest weight is not feasible, answer is -1
    unless feasible.(max_w), do: return(-1)

    # binary search for minimal feasible limit
    search = fn
      (lo, hi, ans) when lo > hi ->
        ans

      (lo, hi, _ans) ->
        mid = div(lo + hi, 2)
        if feasible.(mid) do
          search.(lo, mid - 1, mid)
        else
          search.(mid + 1, hi, -1)
        end
    end

    search.(1, max_w, -1)
  end

  # helper to early return from function
  defp return(val), do: val
end
```

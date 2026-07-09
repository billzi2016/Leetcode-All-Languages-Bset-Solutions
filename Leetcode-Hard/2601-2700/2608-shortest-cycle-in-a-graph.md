# 2608. Shortest Cycle in a Graph

## Cpp

```cpp
class Solution {
public:
    int findShortestCycle(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        const int INF = 1e9;
        int best = INF;
        vector<int> dist(n), parent(n);
        for (int s = 0; s < n; ++s) {
            fill(dist.begin(), dist.end(), -1);
            fill(parent.begin(), parent.end(), -1);
            queue<int> q;
            dist[s] = 0;
            q.push(s);
            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (int v : adj[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        parent[v] = u;
                        q.push(v);
                    } else if (parent[u] != v) { // found a cycle
                        int len = dist[u] + dist[v] + 1;
                        best = min(best, len);
                    }
                }
            }
            if (best == 3) break; // smallest possible cycle in simple graph
        }
        return best == INF ? -1 : best;
    }
};
```

## Java

```java
class Solution {
    public int findShortestCycle(int n, int[][] edges) {
        // Build adjacency list
        @SuppressWarnings("unchecked")
        java.util.ArrayList<Integer>[] adj = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new java.util.ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1];
            adj[u].add(v);
            adj[v].add(u);
        }

        int best = Integer.MAX_VALUE;
        int[] dist = new int[n];
        int[] parent = new int[n];
        java.util.ArrayDeque<Integer> queue = new java.util.ArrayDeque<>();

        for (int start = 0; start < n; start++) {
            java.util.Arrays.fill(dist, -1);
            java.util.Arrays.fill(parent, -1);
            queue.clear();

            dist[start] = 0;
            queue.add(start);

            while (!queue.isEmpty()) {
                int u = queue.poll();
                for (int v : adj[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        parent[v] = u;
                        queue.add(v);
                    } else if (parent[u] != v) { // found a cycle
                        int cycleLen = dist[u] + dist[v] + 1;
                        if (cycleLen < best) {
                            best = cycleLen;
                            if (best == 3) return 3; // smallest possible cycle
                        }
                    }
                }
            }
        }

        return best == Integer.MAX_VALUE ? -1 : best;
    }
}
```

## Python

```python
import collections

class Solution(object):
    def findShortestCycle(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        INF = float('inf')
        best = INF

        for s in range(n):
            dist = [-1] * n
            parent = [-1] * n
            q = collections.deque()
            dist[s] = 0
            q.append(s)

            while q:
                u = q.popleft()
                # early stop if current distance already exceeds best possible cycle length
                if dist[u] * 2 + 1 >= best:
                    continue
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif parent[u] != v:  # found a cycle
                        cycle_len = dist[u] + dist[v] + 1
                        if cycle_len < best:
                            best = cycle_len

        return -1 if best == INF else best
```

## Python3

```python
class Solution:
    def findShortestCycle(self, n: int, edges):
        from collections import deque

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        INF = 10**9
        ans = INF

        for s in range(n):
            dist = [-1] * n
            parent = [-1] * n
            q = deque()
            dist[s] = 0
            q.append(s)

            while q:
                u = q.popleft()
                # early stop if current distance already exceeds best possible cycle
                if dist[u] * 2 + 1 >= ans:
                    continue
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    elif parent[u] != v:  # found a cycle
                        cycle_len = dist[u] + dist[v] + 1
                        if cycle_len < ans:
                            ans = cycle_len
                # minimal possible cycle length is 3
                if ans == 3:
                    return 3

        return -1 if ans == INF else ans
```

## C

```c
int findShortestCycle(int n, int** edges, int edgesSize, int* edgesColSize) {
    // Build adjacency list
    int *deg = (int*)calloc(n, sizeof(int));
    int **adj = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) adj[i] = NULL;
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u] = (int*)realloc(adj[u], (deg[u] + 1) * sizeof(int));
        adj[u][deg[u]++] = v;
        adj[v] = (int*)realloc(adj[v], (deg[v] + 1) * sizeof(int));
        adj[v][deg[v]++] = u;
    }

    int INF = n + 5; // maximum possible cycle length is n
    int answer = INF;

    int *dist = (int*)malloc(n * sizeof(int));
    int *parent = (int*)malloc(n * sizeof(int));
    int *queue = (int*)malloc(n * sizeof(int));

    for (int start = 0; start < n; ++start) {
        // initialize BFS structures
        for (int i = 0; i < n; ++i) {
            dist[i] = -1;
            parent[i] = -1;
        }
        int front = 0, back = 0;
        queue[back++] = start;
        dist[start] = 0;

        while (front < back) {
            int u = queue[front++];
            for (int idx = 0; idx < deg[u]; ++idx) {
                int v = adj[u][idx];
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    queue[back++] = v;
                } else if (parent[u] != v) { // found a cycle
                    int cycle_len = dist[u] + dist[v] + 1;
                    if (cycle_len < answer) answer = cycle_len;
                }
            }
        }
    }

    // clean up
    for (int i = 0; i < n; ++i) {
        free(adj[i]);
    }
    free(adj);
    free(deg);
    free(dist);
    free(parent);
    free(queue);

    return (answer == INF) ? -1 : answer;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindShortestCycle(int n, int[][] edges)
    {
        var adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in edges)
        {
            int u = e[0], v = e[1];
            adj[u].Add(v);
            adj[v].Add(u);
        }

        int best = int.MaxValue;

        for (int start = 0; start < n; start++)
        {
            var dist = new int[n];
            var parent = new int[n];
            for (int i = 0; i < n; i++) { dist[i] = -1; parent[i] = -1; }

            var q = new Queue<int>();
            dist[start] = 0;
            q.Enqueue(start);

            while (q.Count > 0)
            {
                int u = q.Dequeue();
                foreach (int v in adj[u])
                {
                    if (dist[v] == -1)
                    {
                        dist[v] = dist[u] + 1;
                        parent[v] = u;
                        q.Enqueue(v);
                    }
                    else if (parent[u] != v) // found a cycle
                    {
                        int cycleLen = dist[u] + dist[v] + 1;
                        if (cycleLen < best) best = cycleLen;
                    }
                }
            }

            if (best == 3) break; // cannot get shorter than triangle
        }

        return best == int.MaxValue ? -1 : best;
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
var findShortestCycle = function(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    let best = Infinity;

    for (let start = 0; start < n; ++start) {
        const dist = new Array(n).fill(-1);
        const parent = new Array(n).fill(-1);
        const queue = [];
        let qh = 0;
        dist[start] = 0;
        queue.push(start);

        while (qh < queue.length) {
            const u = queue[qh++];
            // optional pruning: if current distance already exceeds best, skip further expansion
            if (dist[u] * 2 + 1 >= best) continue;

            for (const v of adj[u]) {
                if (dist[v] === -1) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    queue.push(v);
                } else if (parent[u] !== v) { // found a cycle
                    const cycleLen = dist[u] + dist[v] + 1;
                    if (cycleLen < best) best = cycleLen;
                }
            }
        }
    }

    return best === Infinity ? -1 : best;
};
```

## Typescript

```typescript
function findShortestCycle(n: number, edges: number[][]): number {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    let best = Infinity;
    const dist = new Int32Array(n);
    const parent = new Int32Array(n);

    for (let start = 0; start < n; ++start) {
        dist.fill(-1);
        parent.fill(-1);
        const queue: number[] = [];
        let qh = 0;
        dist[start] = 0;
        queue.push(start);

        while (qh < queue.length) {
            const u = queue[qh++];
            for (const v of adj[u]) {
                if (dist[v] === -1) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    queue.push(v);
                } else if (parent[u] !== v) { // found a cycle
                    const cycleLen = dist[u] + dist[v] + 1;
                    if (cycleLen < best) {
                        best = cycleLen;
                        if (best === 3) return 3; // smallest possible cycle
                    }
                }
            }
        }
    }

    return best === Infinity ? -1 : best;
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
    function findShortestCycle($n, $edges) {
        // Build adjacency list
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }

        $answer = PHP_INT_MAX;

        for ($start = 0; $start < $n; $start++) {
            $dist = array_fill(0, $n, -1);
            $parent = array_fill(0, $n, -1);
            $queue = new SplQueue();

            $dist[$start] = 0;
            $queue->enqueue($start);

            while (!$queue->isEmpty()) {
                $u = $queue->dequeue();
                foreach ($adj[$u] as $v) {
                    if ($dist[$v] == -1) {
                        $dist[$v] = $dist[$u] + 1;
                        $parent[$v] = $u;
                        $queue->enqueue($v);
                    } elseif ($parent[$u] != $v) { // found a cycle
                        $cycleLen = $dist[$u] + $dist[$v] + 1;
                        if ($cycleLen < $answer) {
                            $answer = $cycleLen;
                        }
                    }
                }
            }
        }

        return $answer === PHP_INT_MAX ? -1 : $answer;
    }
}
```

## Swift

```swift
class Solution {
    func findShortestCycle(_ n: Int, _ edges: [[Int]]) -> Int {
        var adj = Array(repeating: [Int](), count: n)
        for e in edges {
            let u = e[0], v = e[1]
            adj[u].append(v)
            adj[v].append(u)
        }
        
        var answer = Int.max
        var dist = [Int](repeating: -1, count: n)
        var parent = [Int](repeating: -1, count: n)
        
        for start in 0..<n {
            // reset distance and parent arrays
            for i in 0..<n {
                dist[i] = -1
                parent[i] = -1
            }
            
            var queue = [Int]()
            var head = 0
            dist[start] = 0
            queue.append(start)
            
            while head < queue.count {
                let u = queue[head]
                head += 1
                for v in adj[u] {
                    if dist[v] == -1 {
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        queue.append(v)
                    } else if parent[u] != v { // found a cycle
                        let cycleLen = dist[u] + dist[v] + 1
                        if cycleLen < answer {
                            answer = cycleLen
                        }
                    }
                }
            }
        }
        
        return answer == Int.max ? -1 : answer
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun findShortestCycle(n: Int, edges: Array<IntArray>): Int {
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        var best = Int.MAX_VALUE
        // Minimum possible cycle length in simple undirected graph is 3
        if (n < 3) return -1

        for (start in 0 until n) {
            val dist = IntArray(n) { -1 }
            val parent = IntArray(n) { -1 }
            val q: ArrayDeque<Int> = ArrayDeque()
            dist[start] = 0
            q.add(start)

            while (!q.isEmpty()) {
                val u = q.removeFirst()
                for (v in adj[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.add(v)
                    } else if (parent[u] != v) { // found a cycle
                        val cycleLen = dist[u] + dist[v] + 1
                        if (cycleLen < best) {
                            best = cycleLen
                            if (best == 3) return 3
                        }
                    }
                }
            }
        }

        return if (best == Int.MAX_VALUE) -1 else best
    }
}
```

## Dart

```dart
class Solution {
  int findShortestCycle(int n, List<List<int>> edges) {
    // Build adjacency list
    var adj = List.generate(n, (_) => <int>[]);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      adj[u].add(v);
      adj[v].add(u);
    }

    const int INF = 1 << 30;
    int answer = INF;

    // BFS from each vertex
    for (int start = 0; start < n; ++start) {
      List<int> dist = List.filled(n, -1);
      List<int> parent = List.filled(n, -1);
      List<int> queue = [];
      int qIndex = 0;

      dist[start] = 0;
      queue.add(start);

      while (qIndex < queue.length) {
        int u = queue[qIndex++];
        for (int v in adj[u]) {
          if (dist[v] == -1) {
            dist[v] = dist[u] + 1;
            parent[v] = u;
            queue.add(v);
          } else if (parent[u] != v) {
            // Found a cycle
            int cycleLen = dist[u] + dist[v] + 1;
            if (cycleLen < answer) answer = cycleLen;
          }
        }
      }
    }

    return answer == INF ? -1 : answer;
  }
}
```

## Golang

```go
func findShortestCycle(n int, edges [][]int) int {
	adj := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}
	const INF = int(^uint(0) >> 1) // max int
	ans := INF

	dist := make([]int, n)
	parent := make([]int, n)

	for s := 0; s < n; s++ {
		for i := 0; i < n; i++ {
			dist[i] = -1
			parent[i] = -1
		}
		queue := make([]int, 0, n)
		dist[s] = 0
		queue = append(queue, s)
		head := 0

		for head < len(queue) {
			u := queue[head]
			head++
			for _, v := range adj[u] {
				if dist[v] == -1 {
					dist[v] = dist[u] + 1
					parent[v] = u
					queue = append(queue, v)
				} else if parent[u] != v { // found a cycle
					cycleLen := dist[u] + dist[v] + 1
					if cycleLen < ans {
						ans = cycleLen
						if ans == 3 { // smallest possible cycle length
							return 3
						}
					}
				}
			}
		}
	}

	if ans == INF {
		return -1
	}
	return ans
}
```

## Ruby

```ruby
def find_shortest_cycle(n, edges)
  adj = Array.new(n) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  INF = n + 1
  best = INF

  (0...n).each do |start|
    dist = Array.new(n, -1)
    parent = Array.new(n, -1)
    queue = [start]
    head = 0
    dist[start] = 0

    while head < queue.length
      u = queue[head]
      head += 1
      adj[u].each do |v|
        if dist[v] == -1
          dist[v] = dist[u] + 1
          parent[v] = u
          queue << v
        elsif parent[u] != v
          cycle_len = dist[u] + dist[v] + 1
          best = cycle_len if cycle_len < best
        end
      end
    end

    break if best == 3
  end

  best == INF ? -1 : best
end
```

## Scala

```scala
object Solution {
    def findShortestCycle(n: Int, edges: Array[Array[Int]]): Int = {
        val adj = Array.fill(n)(scala.collection.mutable.ArrayBuffer[Int]())
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            adj(u).append(v)
            adj(v).append(u)
        }
        var best = Int.MaxValue
        val dist = new Array[Int](n)
        val parent = new Array[Int](n)
        import scala.collection.mutable.ArrayDeque
        for (start <- 0 until n) {
            java.util.Arrays.fill(dist, -1)
            java.util.Arrays.fill(parent, -1)
            val q = ArrayDeque[Int]()
            dist(start) = 0
            q.append(start)
            while (q.nonEmpty) {
                val u = q.removeHead()
                for (v <- adj(u)) {
                    if (dist(v) == -1) {
                        dist(v) = dist(u) + 1
                        parent(v) = u
                        q.append(v)
                    } else if (parent(u) != v) {
                        val length = dist(u) + dist(v) + 1
                        if (length < best) best = length
                    }
                }
            }
        }
        if (best == Int.MaxValue) -1 else best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_shortest_cycle(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut adj = vec![Vec::<usize>::new(); n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }
        let mut ans = i32::MAX;
        use std::collections::VecDeque;
        for s in 0..n {
            let mut dist = vec![-1i32; n];
            let mut parent = vec![-1i32; n];
            let mut q = VecDeque::new();
            dist[s] = 0;
            q.push_back(s);
            while let Some(u) = q.pop_front() {
                for &v in &adj[u] {
                    if dist[v] == -1 {
                        dist[v] = dist[u] + 1;
                        parent[v] = u as i32;
                        q.push_back(v);
                    } else if parent[u] != v as i32 {
                        let cycle_len = dist[u] + dist[v] + 1;
                        if cycle_len < ans {
                            ans = cycle_len;
                        }
                    }
                }
            }
        }
        if ans == i32::MAX { -1 } else { ans }
    }
}
```

## Racket

```racket
(define/contract (find-shortest-cycle n edges)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ([adj (make-vector n '())])
    (for-each
     (lambda (e)
       (let ([u (first e)] [v (second e)])
         (vector-set! adj u (cons v (vector-ref adj u)))
         (vector-set! adj v (cons u (vector-ref adj v)))))
     edges)
    (define INF 1000000)
    (define best INF)
    (for ([s (in-range n)])
      (let* ([dist (make-vector n -1)]
             [parent (make-vector n -1)]
             [queue (make-vector n 0)]
             [head 0] [tail 0])
        (vector-set! dist s 0)
        (vector-set! queue tail s)
        (set! tail (+ tail 1))
        (let bfs ()
          (when (< head tail)
            (define u (vector-ref queue head))
            (set! head (+ head 1))
            (for ([v (in-list (vector-ref adj u))])
              (cond
                [(= (vector-ref dist v) -1)
                 (vector-set! dist v (+ (vector-ref dist u) 1))
                 (vector-set! parent v u)
                 (vector-set! queue tail v)
                 (set! tail (+ tail 1))]
                [(not (= (vector-ref parent u) v))
                 (define cycle-length (+ (vector-ref dist u) (vector-ref dist v) 1))
                 (when (< cycle-length best)
                   (set! best cycle-length))]))
            (bfs)))))
    (if (= best INF) -1 best)))
```

## Erlang

```erlang
-module(solution).
-export([find_shortest_cycle/2]).

-spec find_shortest_cycle(N :: integer(), Edges :: [[integer()]]) -> integer().
find_shortest_cycle(N, Edges) ->
    Adj = build_adj(Edges),
    MaxVal = N + 1,
    MinCycle = lists:foldl(
        fun(S, CurMin) ->
            case bfs_cycle(S, Adj, N) of
                {ok, Len} -> erlang:min(Len, CurMin);
                not_found -> CurMin
            end
        end,
        MaxVal,
        lists:seq(0, N - 1)
    ),
    if MinCycle =:= MaxVal -> -1; true -> MinCycle end.

build_adj(Edges) ->
    lists:foldl(
        fun([U, V], Acc) ->
            Acc1 = maps:update_with(U,
                fun(L) -> [V | L] end,
                [V],
                Acc),
            maps:update_with(V,
                fun(L) -> [U | L] end,
                [U],
                Acc1)
        end,
        #{},
        Edges
    ).

bfs_cycle(Source, Adj, N) ->
    Q0 = queue:in(Source, queue:new()),
    Dist0 = #{Source => 0},
    Parent0 = #{Source => -1},
    bfs_loop(Q0, Dist0, Parent0, Adj, N, N + 1).

bfs_loop(Queue, DistMap, ParentMap, Adj, N, CurMin) ->
    case queue:out(Queue) of
        {empty, _} ->
            if CurMin =< N -> {ok, CurMin}; true -> not_found end;
        {{value, U}, Q1} ->
            Neighs = maps:get(U, Adj, []),
            {Q2, Dist2, Parent2, NewMin} =
                lists:foldl(
                    fun(V, {QAcc, DAcc, PAcc, MinAcc}) ->
                        case maps:is_key(V, DAcc) of
                            false ->
                                Qn = queue:in(V, QAcc),
                                Dn = maps:put(V, maps:get(U, DAcc) + 1, DAcc),
                                Pn = maps:put(V, U, PAcc),
                                {Qn, Dn, Pn, MinAcc};
                            true ->
                                ParentU = maps:get(U, PAcc, -1),
                                if V =/= ParentU ->
                                    CycleLen = maps:get(U, DAcc) + maps:get(V, DAcc) + 1,
                                    MinNew = erlang:min(CycleLen, MinAcc),
                                    {QAcc, DAcc, PAcc, MinNew};
                                   true ->
                                    {QAcc, DAcc, PAcc, MinAcc}
                                end
                        end
                    end,
                    {Q1, DistMap, ParentMap, CurMin},
                    Neighs
                ),
            bfs_loop(Q2, Dist2, Parent2, Adj, N, NewMin)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_shortest_cycle(n :: integer, edges :: [[integer]]) :: integer
  def find_shortest_cycle(n, edges) do
    adj = build_adj(edges)

    max_len = n + 1

    best =
      Enum.reduce(0..(n - 1), max_len, fn s, cur_best ->
        if cur_best == 3 do
          # cannot get shorter than a triangle
          cur_best
        else
          bfs_len = bfs(s, adj, n, cur_best)
          min(cur_best, bfs_len)
        end
      end)

    if best == max_len, do: -1, else: best
  end

  defp build_adj(edges) do
    Enum.reduce(edges, %{}, fn [u, v], acc ->
      acc
      |> Map.update(u, [v], &[v | &1])
      |> Map.update(v, [u], &[u | &1])
    end)
  end

  # BFS from source `s`. Returns length of shortest cycle found that includes `s`,
  # or a value larger than current global best (passed as limit) if none.
  defp bfs(s, adj, n, limit) do
    queue = :queue.new() |> :queue.in(s)
    dist = %{s => 0}
    parent = %{}
    bfs_loop(queue, dist, parent, adj, limit)
  end

  defp bfs_loop(queue, dist, parent, adj, best) do
    case :queue.out(queue) do
      {:empty, _} ->
        best

      {{:value, u}, q} ->
        du = Map.fetch!(dist, u)
        pu = Map.get(parent, u, -1)

        {new_dist, new_parent, new_q, new_best} =
          Enum.reduce(Map.get(adj, u, []), {dist, parent, q, best}, fn v,
                                                                      {dacc,
                                                                       pacc,
                                                                       qacc,
                                                                       bacc} ->
            cond do
              not Map.has_key?(dacc, v) ->
                dnew = Map.put(dacc, v, du + 1)
                pnew = Map.put(pacc, v, u)
                qnew = :queue.in(v, qacc)
                {dnew, pnew, qnew, bacc}

              pu != v ->
                cycle_len = du + Map.fetch!(dacc, v) + 1
                bnew = if cycle_len < bacc, do: cycle_len, else: bacc
                {dacc, pacc, qacc, bnew}

              true ->
                {dacc, pacc, qacc, bacc}
            end
          end)

        bfs_loop(new_q, new_dist, new_parent, adj, new_best)
    end
  end
end
```

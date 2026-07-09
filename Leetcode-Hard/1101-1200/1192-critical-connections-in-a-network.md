# 1192. Critical Connections in a Network

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        vector<vector<pair<int,int>>> adj(n);
        for (int i = 0; i < (int)connections.size(); ++i) {
            int u = connections[i][0];
            int v = connections[i][1];
            adj[u].push_back({v, i});
            adj[v].push_back({u, i});
        }
        vector<int> disc(n, -1), low(n, -1);
        int timer = 0;
        vector<vector<int>> bridges;
        
        function<void(int,int)> dfs = [&](int u, int parentEdge) {
            disc[u] = low[u] = timer++;
            for (auto [v, eid] : adj[u]) {
                if (eid == parentEdge) continue;
                if (disc[v] == -1) {
                    dfs(v, eid);
                    low[u] = min(low[u], low[v]);
                    if (low[v] > disc[u]) {
                        bridges.push_back({u, v});
                    }
                } else {
                    low[u] = min(low[u], disc[v]);
                }
            }
        };
        
        dfs(0, -1);
        return bridges;
    }
};
```

## Java

```java
class Solution {
    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (List<Integer> edge : connections) {
            int a = edge.get(0), b = edge.get(1);
            graph[a].add(b);
            graph[b].add(a);
        }

        int[] disc = new int[n];
        int[] low = new int[n];
        int[] parent = new int[n];
        int[] nextIdx = new int[n];
        Arrays.fill(parent, -1);

        List<List<Integer>> bridges = new ArrayList<>();
        int time = 1;
        Deque<Integer> stack = new ArrayDeque<>();

        for (int start = 0; start < n; start++) {
            if (disc[start] != 0) continue;

            stack.addLast(start);
            while (!stack.isEmpty()) {
                int u = stack.peekLast();

                // first time we see this node
                if (disc[u] == 0) {
                    disc[u] = low[u] = time++;
                }

                if (nextIdx[u] < graph[u].size()) {
                    int v = graph[u].get(nextIdx[u]++);
                    if (disc[v] == 0) {
                        parent[v] = u;
                        stack.addLast(v);
                    } else if (v != parent[u]) {
                        low[u] = Math.min(low[u], disc[v]);
                    }
                } else {
                    // all neighbors processed, backtrack
                    stack.removeLast();
                    int p = parent[u];
                    if (p != -1) {
                        low[p] = Math.min(low[p], low[u]);
                        if (low[u] > disc[p]) {
                            bridges.add(Arrays.asList(p, u));
                        }
                    }
                }
            }
        }

        return bridges;
    }
}
```

## Python

```python
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        import sys
        sys.setrecursionlimit(10 ** 6)

        adj = [[] for _ in range(n)]
        for idx, (u, v) in enumerate(connections):
            adj[u].append((v, idx))
            adj[v].append((u, idx))

        disc = [-1] * n
        low = [0] * n
        time = 0
        bridges = []

        def dfs(u, parent_eid):
            nonlocal time
            disc[u] = low[u] = time
            time += 1
            for v, eid in adj[u]:
                if eid == parent_eid:
                    continue
                if disc[v] == -1:
                    dfs(v, eid)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        bridges.append([u, v])
                else:
                    low[u] = min(low[u], disc[v])

        dfs(0, -1)
        return bridges
```

## Python3

```python
import sys
from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        sys.setrecursionlimit(1 << 25)
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n
        low = [0] * n
        timer = 0
        bridges: List[List[int]] = []

        def dfs(u: int, parent: int) -> None:
            nonlocal timer
            disc[u] = low[u] = timer
            timer += 1
            for v in graph[u]:
                if disc[v] == -1:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        bridges.append([u, v])
                elif v != parent:
                    low[u] = min(low[u], disc[v])

        for i in range(n):
            if disc[i] == -1:
                dfs(i, -1)

        return bridges
```

## C

```c
#include <stdlib.h>

static int **g_adj;
static int *g_deg;
static int *g_disc;
static int *g_low;
static int g_time;
static int **g_res;
static int g_resCount;

static void dfs(int u, int parent) {
    g_disc[u] = g_low[u] = ++g_time;
    for (int i = 0; i < g_deg[u]; ++i) {
        int v = g_adj[u][i];
        if (!g_disc[v]) {
            dfs(v, u);
            if (g_low[v] > g_disc[u]) {
                int *edge = (int *)malloc(2 * sizeof(int));
                edge[0] = u;
                edge[1] = v;
                g_res[g_resCount++] = edge;
            }
            if (g_low[v] < g_low[u])
                g_low[u] = g_low[v];
        } else if (v != parent) {
            if (g_disc[v] < g_low[u])
                g_low[u] = g_disc[v];
        }
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** criticalConnections(int n, int** connections, int connectionsSize, int* connectionsColSize, int* returnSize, int** returnColumnSizes) {
    (void)connectionsColSize; // unused

    int *deg = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < connectionsSize; ++i) {
        int a = connections[i][0];
        int b = connections[i][1];
        deg[a]++; deg[b]++;
    }

    g_adj = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        g_adj[i] = (int *)malloc(deg[i] * sizeof(int));
    }
    g_deg = deg;

    int *pos = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < connectionsSize; ++i) {
        int a = connections[i][0];
        int b = connections[i][1];
        g_adj[a][pos[a]++] = b;
        g_adj[b][pos[b]++] = a;
    }
    free(pos);

    g_disc = (int *)calloc(n, sizeof(int));
    g_low  = (int *)calloc(n, sizeof(int));
    g_time = 0;

    g_res = (int **)malloc(connectionsSize * sizeof(int *));
    g_resCount = 0;

    for (int i = 0; i < n; ++i) {
        if (!g_disc[i])
            dfs(i, -1);
    }

    *returnSize = g_resCount;
    *returnColumnSizes = (int *)malloc(g_resCount * sizeof(int));
    for (int i = 0; i < g_resCount; ++i)
        (*returnColumnSizes)[i] = 2;

    // Cleanup auxiliary structures (optional, as LeetCode will reclaim memory)
    for (int i = 0; i < n; ++i) free(g_adj[i]);
    free(g_adj);
    free(deg);
    free(g_disc);
    free(g_low);

    return g_res;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    private class Edge {
        public int To;
        public int Id;
        public Edge(int to, int id) { To = to; Id = id; }
    }

    public IList<IList<int>> CriticalConnections(int n, IList<IList<int>> connections) {
        var graph = new List<Edge>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<Edge>();

        int m = connections.Count;
        for (int i = 0; i < m; i++) {
            var conn = connections[i];
            int a = conn[0];
            int b = conn[1];
            graph[a].Add(new Edge(b, i));
            graph[b].Add(new Edge(a, i));
        }

        int[] disc = new int[n];
        int[] low = new int[n];
        bool[] visited = new bool[n];
        var result = new List<IList<int>>();
        int time = 0;

        void Dfs(int u, int parentEdge) {
            visited[u] = true;
            disc[u] = low[u] = ++time;
            foreach (var e in graph[u]) {
                int v = e.To;
                if (!visited[v]) {
                    Dfs(v, e.Id);
                    low[u] = System.Math.Min(low[u], low[v]);
                    if (low[v] > disc[u]) {
                        result.Add(new List<int> { u, v });
                    }
                } else if (e.Id != parentEdge) {
                    low[u] = System.Math.Min(low[u], disc[v]);
                }
            }
        }

        Dfs(0, -1);
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number[][]}
 */
var criticalConnections = function(n, connections) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of connections) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const disc = new Int32Array(n).fill(-1);
    const low = new Int32Array(n);
    const parent = new Int32Array(n).fill(-1);
    let time = 0;
    const bridges = [];

    for (let start = 0; start < n; ++start) {
        if (disc[start] !== -1) continue;

        // iterative DFS stack
        const stack = [];
        disc[start] = low[start] = time++;
        stack.push({ node: start, idx: 0 });

        while (stack.length) {
            const frame = stack[stack.length - 1];
            const u = frame.node;
            if (frame.idx < adj[u].length) {
                const v = adj[u][frame.idx++];
                if (disc[v] === -1) {
                    parent[v] = u;
                    disc[v] = low[v] = time++;
                    stack.push({ node: v, idx: 0 });
                } else if (v !== parent[u]) {
                    // back edge
                    low[u] = Math.min(low[u], disc[v]);
                }
            } else {
                // finished processing u
                stack.pop();
                const p = parent[u];
                if (p !== -1) {
                    low[p] = Math.min(low[p], low[u]);
                    if (low[u] > disc[p]) {
                        bridges.push([p, u]);
                    }
                }
            }
        }
    }

    return bridges;
};
```

## Typescript

```typescript
function criticalConnections(n: number, connections: number[][]): number[][] {
    const graph: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of connections) {
        graph[a].push(b);
        graph[b].push(a);
    }

    const disc = new Array<number>(n).fill(-1);
    const low = new Array<number>(n).fill(0);
    let time = 0;
    const bridges: number[][] = [];

    function dfs(u: number, parent: number): void {
        disc[u] = low[u] = time++;
        for (const v of graph[u]) {
            if (v === parent) continue;
            if (disc[v] === -1) {
                dfs(v, u);
                low[u] = Math.min(low[u], low[v]);
                if (low[v] > disc[u]) {
                    bridges.push([u, v]);
                }
            } else {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
    }

    dfs(0, -1);
    return bridges;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $connections
     * @return Integer[][]
     */
    function criticalConnections($n, $connections) {
        // Build adjacency list
        $graph = array_fill(0, $n, []);
        foreach ($connections as $conn) {
            $a = $conn[0];
            $b = $conn[1];
            $graph[$a][] = $b;
            $graph[$b][] = $a;
        }

        $disc = array_fill(0, $n, -1); // discovery times
        $low  = array_fill(0, $n, 0);  // low-link values
        $time = 0;
        $result = [];

        // Tarjan's DFS to find bridges
        $dfs = function ($u, $parent) use (&$graph, &$disc, &$low, &$time, &$result, &$dfs) {
            $disc[$u] = $low[$u] = $time++;
            foreach ($graph[$u] as $v) {
                if ($v === $parent) {
                    continue;
                }
                if ($disc[$v] === -1) {
                    $dfs($v, $u);
                    $low[$u] = min($low[$u], $low[$v]);
                    if ($low[$v] > $disc[$u]) {
                        // Edge (u, v) is a bridge
                        $result[] = [$u, $v];
                    }
                } else {
                    $low[$u] = min($low[$u], $disc[$v]);
                }
            }
        };

        for ($i = 0; $i < $n; $i++) {
            if ($disc[$i] === -1) {
                $dfs($i, -1);
            }
        }

        // Ensure each pair is ordered as [min, max]
        foreach ($result as &$pair) {
            if ($pair[0] > $pair[1]) {
                $tmp = $pair[0];
                $pair[0] = $pair[1];
                $pair[1] = $tmp;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func criticalConnections(_ n: Int, _ connections: [[Int]]) -> [[Int]] {
        var adj = Array(repeating: [(to: Int, id: Int)](), count: n)
        for (i, conn) in connections.enumerated() {
            let a = conn[0]
            let b = conn[1]
            adj[a].append((to: b, id: i))
            adj[b].append((to: a, id: i))
        }
        
        var disc = Array(repeating: -1, count: n)
        var low = Array(repeating: 0, count: n)
        var time = 0
        var result = [[Int]]()
        
        func dfs(_ u: Int, _ parentEdge: Int) {
            disc[u] = time
            low[u] = time
            time += 1
            
            for edge in adj[u] {
                let v = edge.to
                let id = edge.id
                if disc[v] == -1 {
                    dfs(v, id)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u] {
                        result.append(connections[id])
                    }
                } else if id != parentEdge {
                    low[u] = min(low[u], disc[v])
                }
            }
        }
        
        dfs(0, -1)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun criticalConnections(n: Int, connections: List<List<Int>>): List<List<Int>> {
        val graph = Array(n) { mutableListOf<Int>() }
        for (conn in connections) {
            val a = conn[0]
            val b = conn[1]
            graph[a].add(b)
            graph[b].add(a)
        }

        val ids = IntArray(n) { -1 }
        val low = IntArray(n)
        var id = 0
        val result = mutableListOf<List<Int>>()

        fun dfs(at: Int, parent: Int) {
            ids[at] = id
            low[at] = id
            id++
            for (to in graph[at]) {
                if (to == parent) continue
                if (ids[to] == -1) {
                    dfs(to, at)
                    low[at] = kotlin.math.min(low[at], low[to])
                    if (low[to] > ids[at]) {
                        result.add(listOf(at, to))
                    }
                } else {
                    low[at] = kotlin.math.min(low[at], ids[to])
                }
            }
        }

        for (i in 0 until n) {
            if (ids[i] == -1) dfs(i, -1)
        }

        return result
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  List<List<int>> criticalConnections(int n, List<List<int>> connections) {
    List<List<int>> graph = List.generate(n, (_) => []);
    for (var conn in connections) {
      int a = conn[0];
      int b = conn[1];
      graph[a].add(b);
      graph[b].add(a);
    }

    List<int> disc = List.filled(n, -1);
    List<int> low = List.filled(n, -1);
    int time = 0;
    List<List<int>> bridges = [];

    void dfs(int u, int parent) {
      disc[u] = low[u] = time++;
      for (int v in graph[u]) {
        if (disc[v] == -1) {
          dfs(v, u);
          low[u] = min(low[u], low[v]);
          if (low[v] > disc[u]) {
            bridges.add([u, v]);
          }
        } else if (v != parent) {
          low[u] = min(low[u], disc[v]);
        }
      }
    }

    for (int i = 0; i < n; ++i) {
      if (disc[i] == -1) dfs(i, -1);
    }

    return bridges;
  }
}
```

## Golang

```go
func criticalConnections(n int, connections [][]int) [][]int {
	type Edge struct {
		to int
		id int
	}
	adj := make([][]Edge, n)
	for i, c := range connections {
		a, b := c[0], c[1]
		adj[a] = append(adj[a], Edge{to: b, id: i})
		adj[b] = append(adj[b], Edge{to: a, id: i})
	}
	discovery := make([]int, n)
	low := make([]int, n)
	time := 1
	var result [][]int

	var dfs func(u int, parentEdge int)
	dfs = func(u int, parentEdge int) {
		discovery[u] = time
		low[u] = time
		time++
		for _, e := range adj[u] {
			v := e.to
			if e.id == parentEdge {
				continue
			}
			if discovery[v] == 0 {
				dfs(v, e.id)
				if low[v] > discovery[u] {
					result = append(result, []int{u, v})
				}
				if low[v] < low[u] {
					low[u] = low[v]
				}
			} else {
				if discovery[v] < low[u] {
					low[u] = discovery[v]
				}
			}
		}
	}

	dfs(0, -1)
	return result
}
```

## Ruby

```ruby
def critical_connections(n, connections)
  adj = Array.new(n) { [] }
  connections.each do |a, b|
    adj[a] << b
    adj[b] << a
  end

  disc = Array.new(n, -1)
  low = Array.new(n, 0)
  time = 0
  bridges = []

  (0...n).each do |start|
    next if disc[start] != -1
    stack = []
    stack << [start, -1, 0]

    while !stack.empty?
      u, parent, idx = stack[-1]

      if idx == 0 && disc[u] == -1
        time += 1
        disc[u] = low[u] = time
      end

      if idx < adj[u].length
        v = adj[u][idx]
        stack[-1][2] = idx + 1
        if disc[v] == -1
          stack << [v, u, 0]
        elsif v != parent
          low[u] = low[u] < disc[v] ? low[u] : disc[v]
        end
      else
        stack.pop
        if parent != -1
          bridges << [parent, u] if low[u] > disc[parent]
          unless stack.empty?
            pnode = stack[-1][0]
            low[pnode] = low[pnode] < low[u] ? low[pnode] : low[u]
          end
        end
      end
    end
  end

  bridges
end
```

## Scala

```scala
object Solution {
  def criticalConnections(n: Int, connections: List[List[Int]]): List[List[Int]] = {
    import scala.collection.mutable.{ArrayBuffer, ListBuffer}
    val graph = Array.fill(n)(new ArrayBuffer[Int]())
    for (c <- connections) {
      val u = c(0)
      val v = c(1)
      graph(u).append(v)
      graph(v).append(u)
    }
    val disc = new Array[Int](n)
    val low  = new Array[Int](n)
    var time = 0
    val bridges = ListBuffer[List[Int]]()

    def dfs(u: Int, parent: Int): Unit = {
      time += 1
      disc(u) = time
      low(u) = time
      for (v <- graph(u)) {
        if (v == parent) {
          // skip the edge back to parent
        } else if (disc(v) == 0) {
          dfs(v, u)
          low(u) = math.min(low(u), low(v))
          if (low(v) > disc(u)) bridges.append(List(u, v))
        } else {
          low(u) = math.min(low(u), disc(v))
        }
      }
    }

    for (i <- 0 until n) {
      if (disc(i) == 0) dfs(i, -1)
    }
    bridges.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn critical_connections(n: i32, connections: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<(usize, usize)>> = vec![Vec::new(); n_usize];
        for (idx, conn) in connections.iter().enumerate() {
            let a = conn[0] as usize;
            let b = conn[1] as usize;
            adj[a].push((b, idx));
            adj[b].push((a, idx));
        }

        fn dfs(
            u: usize,
            parent_edge: usize,
            time: &mut i32,
            disc: &mut Vec<i32>,
            low: &mut Vec<i32>,
            adj: &Vec<Vec<(usize, usize)>>,
            res: &mut Vec<Vec<i32>>,
        ) {
            *time += 1;
            disc[u] = *time;
            low[u] = *time;

            for &(v, eid) in &adj[u] {
                if eid == parent_edge {
                    continue;
                }
                if disc[v] == 0 {
                    dfs(v, eid, time, disc, low, adj, res);
                    low[u] = low[u].min(low[v]);
                    if low[v] > disc[u] {
                        let a = u as i32;
                        let b = v as i32;
                        if a < b {
                            res.push(vec![a, b]);
                        } else {
                            res.push(vec![b, a]);
                        }
                    }
                } else {
                    low[u] = low[u].min(disc[v]);
                }
            }
        }

        let mut disc = vec![0i32; n_usize];
        let mut low = vec![0i32; n_usize];
        let mut time = 0i32;
        let mut result: Vec<Vec<i32>> = Vec::new();

        for i in 0..n_usize {
            if disc[i] == 0 {
                dfs(i, usize::MAX, &mut time, &mut disc, &mut low, &adj, &mut result);
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (critical-connections n connections)
  (-> exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ((adj (make-vector n '()))
         (disc (make-vector n -1))
         (low (make-vector n 0))
         (time (box 0))
         (result '()))
    ;; build adjacency list
    (for ([e connections])
      (match e
        [(list a b)
         (vector-set! adj a (cons b (vector-ref adj a)))
         (vector-set! adj b (cons a (vector-ref adj b)))]))
    (letrec ((dfs (lambda (u parent)
                    (vector-set! disc u (unbox time))
                    (vector-set! low u (unbox time))
                    (set-box! time (+ (unbox time) 1))
                    (for ([v (in-list (vector-ref adj u))])
                      (cond
                        [(= v parent) (void)]
                        [(= (vector-ref disc v) -1)
                         (dfs v u)
                         (when (< (vector-ref low v) (vector-ref low u))
                           (vector-set! low u (vector-ref low v)))
                         (when (> (vector-ref low v) (vector-ref disc u))
                           (set! result (cons (list u v) result)))]
                        [else
                         (when (< (vector-ref disc v) (vector-ref low u))
                           (vector-set! low u (vector-ref disc v)))])))))
      ;; run DFS from every unvisited node (graph is connected but safe)
      (for ([i (in-range n)])
        (when (= (vector-ref disc i) -1)
          (dfs i -1))))
    result))
```

## Erlang

```erlang
-module(solution).
-export([critical_connections/2]).

-spec critical_connections(N :: integer(), Connections :: [[integer()]]) -> [[integer()]].
critical_connections(_N, Connections) ->
    Adj = build_adj(Connections, #{}),
    {_, _, _, Bridges} = dfs_all(maps:keys(Adj), Adj, #{}, #{}, 0, []),
    Bridges.

build_adj([], Adj) -> Adj;
build_adj([[U,V]|Rest], Adj) ->
    Adj1 = maps:update_with(U,
            fun(L) -> [V|L] end,
            [V],
            Adj),
    Adj2 = maps:update_with(V,
            fun(L) -> [U|L] end,
            [U],
            Adj1),
    build_adj(Rest, Adj2).

dfs_all([], _Adj, Disc, Low, Time, Bridges) ->
    {Disc, Low, Time, Bridges};
dfs_all([V|Vs], Adj, Disc, Low, Time, Bridges) ->
    case maps:is_key(V, Disc) of
        true -> dfs_all(Vs, Adj, Disc, Low, Time, Bridges);
        false ->
            {Disc1, Low1, Time1, Bridges1} = dfs(V, -1, Adj, Disc, Low, Time, Bridges),
            dfs_all(Vs, Adj, Disc1, Low1, Time1, Bridges1)
    end.

dfs(V, Parent, Adj, Disc, Low, Time, Bridges) ->
    Time1 = Time + 1,
    Disc1 = maps:put(V, Time1, Disc),
    Low1 = maps:put(V, Time1, Low),
    Neighs = maps:get(V, Adj, []),
    lists:foldl(fun(Nbr, {DAcc, LAcc, TAcc, BAcc}) ->
        case maps:is_key(Nbr, DAcc) of
            false ->
                % tree edge
                {D2, L2, T2, B2} = dfs(Nbr, V, Adj, DAcc, LAcc, TAcc, BAcc),
                LowV = maps:get(V, L2),
                LowNbr = maps:get(Nbr, L2),
                LowV1 = erlang:min(LowV, LowNbr),
                L3 = maps:put(V, LowV1, L2),
                BridgeCond = (LowNbr > maps:get(V, DAcc)),
                B3 = if BridgeCond -> [[V,Nbr]|B2]; true -> B2 end,
                {D2, L3, T2, B3};
            true ->
                case Nbr == Parent of
                    true -> {DAcc, LAcc, TAcc, BAcc};
                    false ->
                        LowV = maps:get(V, LAcc),
                        DiscNbr = maps:get(Nbr, DAcc),
                        LowV1 = erlang:min(LowV, DiscNbr),
                        L3 = maps:put(V, LowV1, LAcc),
                        {DAcc, L3, TAcc, BAcc}
                end
        end
    end, {Disc1, Low1, Time1, Bridges}, Neighs).
```

## Elixir

```elixir
defmodule Solution do
  @spec critical_connections(n :: integer, connections :: [[integer]]) :: [[integer]]
  def critical_connections(n, connections) do
    adj = build_adj(connections)

    {_time, _disc, _low, bridges} = dfs(0, -1, 1, %{}, %{}, [], adj)
    bridges
  end

  defp build_adj(conns) do
    Enum.reduce(conns, %{}, fn [a, b], acc ->
      acc
      |> Map.update(a, [b], &[b | &1])
      |> Map.update(b, [a], &[a | &1])
    end)
  end

  defp dfs(u, parent, time, disc, low, bridges, adj) do
    disc = Map.put(disc, u, time)
    low = Map.put(low, u, time)
    time = time + 1

    {time, disc, low, bridges} =
      Enum.reduce(Map.get(adj, u, []), {time, disc, low, bridges}, fn v,
                                                                      {t, d, l, b} ->
        cond do
          v == parent ->
            {t, d, l, b}

          Map.has_key?(d, v) ->
            # back edge
            low_u = min(Map.get(l, u), Map.get(d, v))
            l = Map.put(l, u, low_u)
            {t, d, l, b}

          true ->
            # tree edge
            {t2, d2, l2, b2} = dfs(v, u, t, d, l, b, adj)

            low_v = Map.get(l2, v)
            low_u = min(Map.get(l2, u), low_v)
            l2 = Map.put(l2, u, low_u)

            b2 =
              if low_v > Map.get(d2, u) do
                [[u, v] | b2]
              else
                b2
              end

            {t2, d2, l2, b2}
        end
      end)

    {time, disc, low, bridges}
  end
end
```

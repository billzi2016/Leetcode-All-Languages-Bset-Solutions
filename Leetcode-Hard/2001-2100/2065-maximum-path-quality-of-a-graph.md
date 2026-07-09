# 2065. Maximum Path Quality of a Graph

## Cpp

```cpp
class Solution {
public:
    int maximalPathQuality(vector<int>& values, vector<vector<int>>& edges, int maxTime) {
        int n = values.size();
        vector<vector<pair<int,int>>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1], t = e[2];
            adj[u].push_back({v, t});
            adj[v].push_back({u, t});
        }
        vector<char> visited(n, 0);
        int ans = values[0];
        visited[0] = 1;
        
        function<void(int,int,int)> dfs = [&](int node, int timeLeft, int curSum) {
            if (node == 0) ans = max(ans, curSum);
            for (auto &p : adj[node]) {
                int nxt = p.first, w = p.second;
                if (w > timeLeft) continue;
                bool firstVisit = !visited[nxt];
                if (firstVisit) visited[nxt] = 1;
                dfs(nxt, timeLeft - w, curSum + (firstVisit ? values[nxt] : 0));
                if (firstVisit) visited[nxt] = 0;
            }
        };
        
        dfs(0, maxTime, values[0]);
        return ans;
    }
};
```

## Java

```java
class Solution {
    private int[] values;
    private List<int[]>[] graph;
    private boolean[] visited;
    private int maxTime;
    private int curSum;
    private int answer;

    public int maximalPathQuality(int[] values, int[][] edges, int maxTime) {
        this.values = values;
        this.maxTime = maxTime;
        int n = values.length;
        graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], t = e[2];
            graph[u].add(new int[]{v, t});
            graph[v].add(new int[]{u, t});
        }
        visited = new boolean[n];
        visited[0] = true;
        curSum = values[0];
        answer = curSum;
        dfs(0, 0);
        return answer;
    }

    private void dfs(int node, int timeSpent) {
        if (node == 0) {
            if (curSum > answer) answer = curSum;
        }
        for (int[] edge : graph[node]) {
            int next = edge[0];
            int cost = edge[1];
            int newTime = timeSpent + cost;
            if (newTime > maxTime) continue;

            boolean firstVisit = !visited[next];
            if (firstVisit) {
                visited[next] = true;
                curSum += values[next];
            }

            dfs(next, newTime);

            if (firstVisit) {
                visited[next] = false;
                curSum -= values[next];
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def maximalPathQuality(self, values, edges, maxTime):
        """
        :type values: List[int]
        :type edges: List[List[int]]
        :type maxTime: int
        :rtype: int
        """
        n = len(values)
        adj = [[] for _ in range(n)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))

        visited = [False] * n
        ans = 0

        def dfs(node, time_left, cur_sum):
            nonlocal ans
            if node == 0:
                ans = max(ans, cur_sum)
            for nei, w in adj[node]:
                if w > time_left:
                    continue
                added = 0
                if not visited[nei]:
                    visited[nei] = True
                    added = values[nei]
                dfs(nei, time_left - w, cur_sum + added)
                if added:
                    visited[nei] = False

        visited[0] = True
        dfs(0, maxTime, values[0])
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        adj = [[] for _ in range(n)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))

        visited = [False] * n
        best = values[0]

        def dfs(node: int, time_spent: int, cur_sum: int) -> None:
            nonlocal best
            if node == 0:
                if cur_sum > best:
                    best = cur_sum
            for nxt, w in adj[node]:
                nt = time_spent + w
                if nt > maxTime:
                    continue
                added = 0
                if not visited[nxt]:
                    visited[nxt] = True
                    added = values[nxt]
                    dfs(nxt, nt, cur_sum + added)
                    visited[nxt] = False
                else:
                    dfs(nxt, nt, cur_sum)

        visited[0] = True
        dfs(0, 0, values[0])
        return best
```

## C

```c
#include <stddef.h>
#include <string.h>

struct Edge {
    int to;
    int w;
};

static void dfs(int cur, int timeLeft, int currSum,
                int n, const int *values,
                struct Edge adj[][4], const int *deg,
                int *visited, int *ans) {
    if (cur == 0 && currSum > *ans)
        *ans = currSum;
    for (int i = 0; i < deg[cur]; ++i) {
        int nxt = adj[cur][i].to;
        int w   = adj[cur][i].w;
        if (timeLeft >= w) {
            int prev = visited[nxt];
            visited[nxt] = 1;
            dfs(nxt, timeLeft - w,
                currSum + (prev ? 0 : values[nxt]),
                n, values, adj, deg, visited, ans);
            visited[nxt] = prev;
        }
    }
}

int maximalPathQuality(int* values, int valuesSize, int** edges, int edgesSize,
                       int* edgesColSize, int maxTime) {
    (void)edgesColSize; // unused, each edge has 3 columns
    const int n = valuesSize;
    struct Edge adj[1000][4];
    int deg[1000];
    memset(deg, 0, sizeof(deg));

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int t = edges[i][2];
        adj[u][deg[u]].to = v;
        adj[u][deg[u]].w  = t;
        deg[u]++;
        adj[v][deg[v]].to = u;
        adj[v][deg[v]].w  = t;
        deg[v]++;
    }

    int visited[1000] = {0};
    visited[0] = 1;
    int ans = values[0];
    dfs(0, maxTime, values[0], n, values, adj, deg, visited, &ans);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximalPathQuality(int[] values, int[][] edges, int maxTime) {
        int n = values.Length;
        var graph = new List<(int to, int time)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, int)>();
        foreach (var e in edges) {
            int u = e[0], v = e[1], t = e[2];
            graph[u].Add((v, t));
            graph[v].Add((u, t));
        }

        bool[] visited = new bool[n];
        long currentSum = 0;
        long best = 0;

        visited[0] = true;
        currentSum += values[0];

        void Dfs(int node, int elapsed) {
            if (node == 0 && currentSum > best) best = currentSum;

            foreach (var (to, time) in graph[node]) {
                int nextElapsed = elapsed + time;
                if (nextElapsed > maxTime) continue;

                bool firstVisit = !visited[to];
                if (firstVisit) {
                    visited[to] = true;
                    currentSum += values[to];
                }

                Dfs(to, nextElapsed);

                if (firstVisit) {
                    visited[to] = false;
                    currentSum -= values[to];
                }
            }
        }

        Dfs(0, 0);
        return (int)best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} values
 * @param {number[][]} edges
 * @param {number} maxTime
 * @return {number}
 */
var maximalPathQuality = function(values, edges, maxTime) {
    const n = values.length;
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, t] of edges) {
        adj[u].push([v, t]);
        adj[v].push([u, t]);
    }
    let best = values[0];
    const visited = new Array(n).fill(false);
    visited[0] = true;

    function dfs(node, timeSpent, curQuality) {
        if (node === 0) {
            if (curQuality > best) best = curQuality;
        }
        for (const [nei, w] of adj[node]) {
            const nt = timeSpent + w;
            if (nt > maxTime) continue;
            if (!visited[nei]) {
                visited[nei] = true;
                dfs(nei, nt, curQuality + values[nei]);
                visited[nei] = false;
            } else {
                dfs(nei, nt, curQuality);
            }
        }
    }

    dfs(0, 0, values[0]);
    return best;
};
```

## Typescript

```typescript
function maximalPathQuality(values: number[], edges: number[][], maxTime: number): number {
    const n = values.length;
    const adj: [number, number][][] = Array.from({ length: n }, () => []);
    for (const e of edges) {
        const u = e[0], v = e[1], t = e[2];
        adj[u].push([v, t]);
        adj[v].push([u, t]);
    }
    const visited = new Uint8Array(n);
    let best = 0;

    function dfs(node: number, timeUsed: number, curSum: number): void {
        if (node === 0 && curSum > best) {
            best = curSum;
        }
        for (const [next, w] of adj[node]) {
            const newTime = timeUsed + w;
            if (newTime > maxTime) continue;
            if (!visited[next]) {
                visited[next] = 1;
                dfs(next, newTime, curSum + values[next]);
                visited[next] = 0;
            } else {
                dfs(next, newTime, curSum);
            }
        }
    }

    visited[0] = 1;
    dfs(0, 0, values[0]);
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $values
     * @param Integer[][] $edges
     * @param Integer $maxTime
     * @return Integer
     */
    function maximalPathQuality($values, $edges, $maxTime) {
        $n = count($values);
        // build adjacency list
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            [$u, $v, $t] = $e;
            $graph[$u][] = [$v, $t];
            $graph[$v][] = [$u, $t];
        }

        $visited = array_fill(0, $n, false);
        $visited[0] = true;
        $maxQuality = $values[0];

        $dfs = function($node, $timeSpent, $currentSum) use (&$dfs, &$graph, &$values, $maxTime, &$visited, &$maxQuality) {
            if ($node === 0) {
                if ($currentSum > $maxQuality) {
                    $maxQuality = $currentSum;
                }
            }

            foreach ($graph[$node] as $edge) {
                [$next, $t] = $edge;
                $newTime = $timeSpent + $t;
                if ($newTime > $maxTime) {
                    continue;
                }

                $added = 0;
                if (!$visited[$next]) {
                    $visited[$next] = true;
                    $added = $values[$next];
                }

                $dfs($next, $newTime, $currentSum + $added);

                // backtrack
                if ($added > 0) {
                    $visited[$next] = false;
                }
            }
        };

        $dfs(0, 0, $values[0]);

        return $maxQuality;
    }
}
```

## Swift

```swift
class Solution {
    func maximalPathQuality(_ values: [Int], _ edges: [[Int]], _ maxTime: Int) -> Int {
        let n = values.count
        var graph = Array(repeating: [(Int, Int)](), count: n)
        for e in edges {
            let u = e[0], v = e[1], t = e[2]
            graph[u].append((v, t))
            graph[v].append((u, t))
        }
        var visited = Array(repeating: false, count: n)
        visited[0] = true
        var best = values[0]

        func dfs(_ node: Int, _ remaining: Int, _ curSum: Int) {
            if node == 0 && curSum > best {
                best = curSum
            }
            for (next, time) in graph[node] {
                if time <= remaining {
                    var added = 0
                    var firstVisit = false
                    if !visited[next] {
                        visited[next] = true
                        added = values[next]
                        firstVisit = true
                    }
                    dfs(next, remaining - time, curSum + added)
                    if firstVisit {
                        visited[next] = false
                    }
                }
            }
        }

        dfs(0, maxTime, values[0])
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximalPathQuality(values: IntArray, edges: Array<IntArray>, maxTime: Int): Int {
        val n = values.size
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val t = e[2]
            adj[u].add(Pair(v, t))
            adj[v].add(Pair(u, t))
        }

        var best = values[0]
        val visited = BooleanArray(n)
        visited[0] = true

        fun dfs(node: Int, timeUsed: Int, currentSum: Int) {
            if (node == 0) {
                if (currentSum > best) best = currentSum
            }
            for ((next, cost) in adj[node]) {
                val newTime = timeUsed + cost
                if (newTime > maxTime) continue

                var added = 0
                if (!visited[next]) {
                    visited[next] = true
                    added = values[next]
                }

                dfs(next, newTime, currentSum + added)

                if (added != 0) {
                    visited[next] = false
                }
            }
        }

        dfs(0, 0, values[0])
        return best
    }
}
```

## Dart

```dart
class Solution {
  int maximalPathQuality(List<int> values, List<List<int>> edges, int maxTime) {
    int n = values.length;
    List<List<List<int>>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0], v = e[1], t = e[2];
      adj[u].add([v, t]);
      adj[v].add([u, t]);
    }

    List<bool> visited = List.filled(n, false);
    visited[0] = true;
    int curSum = values[0];
    int ans = values[0];

    void dfs(int node, int elapsed) {
      if (node == 0) {
        if (curSum > ans) ans = curSum;
      }
      for (var edge in adj[node]) {
        int nxt = edge[0];
        int time = edge[1];
        int newElapsed = elapsed + time;
        if (newElapsed > maxTime) continue;

        bool firstVisit = !visited[nxt];
        if (firstVisit) {
          visited[nxt] = true;
          curSum += values[nxt];
        }

        dfs(nxt, newElapsed);

        if (firstVisit) {
          curSum -= values[nxt];
          visited[nxt] = false;
        }
      }
    }

    dfs(0, 0);
    return ans;
  }
}
```

## Golang

```go
func maximalPathQuality(values []int, edges [][]int, maxTime int) int {
    n := len(values)
    type edge struct{ to, w int }
    adj := make([][]edge, n)
    for _, e := range edges {
        u, v, w := e[0], e[1], e[2]
        adj[u] = append(adj[u], edge{v, w})
        adj[v] = append(adj[v], edge{u, w})
    }

    visited := make([]bool, n)
    ans := 0

    var dfs func(node, timeLeft, curSum int)
    dfs = func(node, timeLeft, curSum int) {
        if node == 0 && curSum > ans {
            ans = curSum
        }
        for _, nb := range adj[node] {
            if nb.w <= timeLeft {
                added := 0
                if !visited[nb.to] {
                    visited[nb.to] = true
                    added = values[nb.to]
                }
                dfs(nb.to, timeLeft-nb.w, curSum+added)
                if added > 0 {
                    visited[nb.to] = false
                }
            }
        }
    }

    visited[0] = true
    dfs(0, maxTime, values[0])
    return ans
}
```

## Ruby

```ruby
def maximal_path_quality(values, edges, max_time)
  n = values.size
  adj = Array.new(n) { [] }
  edges.each do |u, v, t|
    adj[u] << [v, t]
    adj[v] << [u, t]
  end

  visited = Array.new(n, false)
  ans = 0

  dfs = lambda do |node, time_left, cur_sum|
    ans = [ans, cur_sum].max if node == 0
    adj[node].each do |nbr, cost|
      next if cost > time_left
      added = false
      new_sum = cur_sum
      unless visited[nbr]
        visited[nbr] = true
        new_sum += values[nbr]
        added = true
      end
      dfs.call(nbr, time_left - cost, new_sum)
      visited[nbr] = false if added
    end
  end

  visited[0] = true
  dfs.call(0, max_time, values[0])
  ans
end
```

## Scala

```scala
object Solution {
    def maximalPathQuality(values: Array[Int], edges: Array[Array[Int]], maxTime: Int): Int = {
        val n = values.length
        val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[(Int, Int)]())
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            val t = e(2)
            adj(u).append((v, t))
            adj(v).append((u, t))
        }
        val graph = adj.map(_.toArray)

        val visited = new Array[Boolean](n)
        visited(0) = true
        var best = values(0)

        def dfs(node: Int, timeSpent: Int, curSum: Int): Unit = {
            if (node == 0 && curSum > best) best = curSum
            for ((next, cost) <- graph(node)) {
                val newTime = timeSpent + cost
                if (newTime <= maxTime) {
                    if (!visited(next)) {
                        visited(next) = true
                        dfs(next, newTime, curSum + values(next))
                        visited(next) = false
                    } else {
                        dfs(next, newTime, curSum)
                    }
                }
            }
        }

        dfs(0, 0, values(0))
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximal_path_quality(values: Vec<i32>, edges: Vec<Vec<i32>>, max_time: i32) -> i32 {
        let n = values.len();
        let mut adj = vec![Vec::<(usize, i32)>::new(); n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let t = e[2];
            adj[u].push((v, t));
            adj[v].push((u, t));
        }
        let mut visited = vec![false; n];
        visited[0] = true;
        let start_sum = values[0] as i64;
        let mut ans: i64 = 0;

        fn dfs(
            u: usize,
            time_left: i32,
            cur_sum: i64,
            adj: &Vec<Vec<(usize, i32)>>,
            visited: &mut Vec<bool>,
            values: &Vec<i32>,
            ans: &mut i64,
        ) {
            if u == 0 && cur_sum > *ans {
                *ans = cur_sum;
            }
            for &(v, w) in &adj[u] {
                if time_left >= w {
                    let need_visit = !visited[v];
                    if need_visit {
                        visited[v] = true;
                    }
                    let added = if need_visit { values[v] as i64 } else { 0 };
                    dfs(
                        v,
                        time_left - w,
                        cur_sum + added,
                        adj,
                        visited,
                        values,
                        ans,
                    );
                    if need_visit {
                        visited[v] = false;
                    }
                }
            }
        }

        dfs(0, max_time, start_sum, &adj, &mut visited, &values, &mut ans);
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (maximal-path-quality values edges maxTime)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((n (length values))
         (val-vec (list->vector values))
         (adj (make-vector n '()))
         (best (box 0)))
    ;; build adjacency list
    (for ([e edges])
      (let* ((u (list-ref e 0))
             (v (list-ref e 1))
             (t (list-ref e 2)))
        (vector-set! adj u (cons (cons v t) (vector-ref adj u)))
        (vector-set! adj v (cons (cons u t) (vector-ref adj v)))))
    (define visited (make-vector n #f))
    (vector-set! visited 0 #t)
    (letrec ((dfs
              (lambda (node time-spent cur-sum)
                (when (= node 0)
                  (when (> cur-sum (unbox best))
                    (set-box! best cur-sum)))
                (for ([pair (in-list (vector-ref adj node))])
                  (define to (car pair))
                  (define cost (cdr pair))
                  (define new-time (+ time-spent cost))
                  (when (<= new-time maxTime)
                    (if (not (vector-ref visited to))
                        (begin
                          (vector-set! visited to #t)
                          (dfs to new-time (+ cur-sum (vector-ref val-vec to)))
                          (vector-set! visited to #f))
                        (dfs to new-time cur-sum)))))))
      (dfs 0 0 (vector-ref val-vec 0))
      (unbox best))))
```

## Erlang

```erlang
-module(solution).
-export([maximal_path_quality/3]).
-spec maximal_path_quality(Values :: [integer()], Edges :: [[integer()]], MaxTime :: integer()) -> integer().
maximal_path_quality(Values, Edges, MaxTime) ->
    N = length(Values),
    Adj = build_adj(Edges, #{}),
    MinDist = dijkstra(Adj, N),
    ValuesTuple = list_to_tuple(Values),
    Visited0 = maps:put(0, true, #{}),
    StartSum = element(1, ValuesTuple),
    dfs(0, 0, StartSum, Visited0, Adj, MinDist, MaxTime, ValuesTuple).

build_adj([], Adj) -> Adj;
build_adj([[U,V,T]|Rest], Adj) ->
    Adj1 = maps:update_with(U,
            fun(L) -> [{V,T}|L] end,
            [{V,T}],
            Adj),
    Adj2 = maps:update_with(V,
            fun(L) -> [{U,T}|L] end,
            [{U,T}],
            Adj1),
    build_adj(Rest, Adj2).

dijkstra(Adj, N) ->
    Infinity = 1 bsl 30,
    InitDist = maps:from_list([{I, Infinity} || I <- lists:seq(0,N-1)]),
    Dist0 = maps:put(0, 0, InitDist),
    PQ0 = gb_sets:add_element({0,0}, gb_sets:new()),
    dijkstra_loop(PQ0, Dist0, Adj).

dijkstra_loop(PQ, Dist, Adj) ->
    case gb_sets:is_empty(PQ) of
        true -> Dist;
        false ->
            {{CurDist, Node}, PQRest} = gb_sets:take_smallest(PQ),
            case CurDist > maps:get(Node, Dist) of
                true ->
                    dijkstra_loop(PQRest, Dist, Adj);
                false ->
                    Neighs = maps:get(Node, Adj, []),
                    {NewPQ, NewDist} = lists:foldl(
                        fun({Nb, T}, {AccPQ, AccDist}) ->
                            ND = CurDist + T,
                            case ND < maps:get(Nb, AccDist) of
                                true ->
                                    UpdatedDist = maps:put(Nb, ND, AccDist),
                                    {gb_sets:add_element({ND, Nb}, AccPQ), UpdatedDist};
                                false -> {AccPQ, AccDist}
                            end
                        end,
                        {PQRest, Dist},
                        Neighs),
                    dijkstra_loop(NewPQ, NewDist, Adj)
            end
    end.

dfs(Node, TimeSpent, Sum, Visited, Adj, MinDist, MaxTime, ValuesTuple) ->
    Base = case Node of
        0 -> Sum;
        _ -> 0
    end,
    Neighs = maps:get(Node, Adj, []),
    lists:foldl(
        fun({Next, T}, Acc) ->
            NewTime = TimeSpent + T,
            if NewTime > MaxTime ->
                    Acc;
               true ->
                    MinBack = maps:get(Next, MinDist, 1 bsl 30),
                    if NewTime + MinBack > MaxTime ->
                            Acc;
                       true ->
                            AlreadyVisited = maps:is_key(Next, Visited),
                            NewSum = case AlreadyVisited of
                                true -> Sum;
                                false -> Sum + element(Next+1, ValuesTuple)
                            end,
                            NewVisited = case AlreadyVisited of
                                true -> Visited;
                                false -> maps:put(Next, true, Visited)
                            end,
                            Res = dfs(Next, NewTime, NewSum, NewVisited, Adj, MinDist, MaxTime, ValuesTuple),
                            erlang:max(Acc, Res)
                    end
            end
        end,
        Base,
        Neighs).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximal_path_quality(values :: [integer], edges :: [[integer]], max_time :: integer) :: integer
  def maximal_path_quality(values, edges, max_time) do
    n = length(values)

    adj = build_adj(edges)

    visited =
      List.duplicate(false, n)
      |> List.replace_at(0, true)

    dfs(0, 0, Enum.at(values, 0), visited, adj, values, max_time)
  end

  defp build_adj(edges) do
    Enum.reduce(edges, %{}, fn [u, v, t], acc ->
      acc
      |> Map.update(u, [{v, t}], fn lst -> [{v, t} | lst] end)
      |> Map.update(v, [{u, t}], fn lst -> [{u, t} | lst] end)
    end)
  end

  defp dfs(node, time_spent, quality, visited, adj, values, max_time) do
    init_best = if node == 0, do: quality, else: 0

    Enum.reduce(Map.get(adj, node, []), init_best, fn {nbr, t}, best ->
      new_time = time_spent + t

      if new_time <= max_time do
        visited_already = Enum.at(visited, nbr)

        new_quality =
          if visited_already,
            do: quality,
            else: quality + Enum.at(values, nbr)

        new_visited =
          if visited_already,
            do: visited,
            else: List.replace_at(visited, nbr, true)

        child_best = dfs(nbr, new_time, new_quality, new_visited, adj, values, max_time)
        max(best, child_best)
      else
        best
      end
    end)
  end
end
```

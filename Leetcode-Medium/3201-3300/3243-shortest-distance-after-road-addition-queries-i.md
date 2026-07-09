# 3243. Shortest Distance After Road Addition Queries I

## Cpp

```cpp
class Solution {
public:
    vector<int> shortestDistanceAfterQueries(int n, vector<vector<int>>& queries) {
        vector<vector<int>> adj(n);
        for (int i = 0; i < n - 1; ++i) adj[i].push_back(i + 1);
        
        auto bfs = [&](const vector<vector<int>>& g) -> int {
            vector<int> dist(n, -1);
            queue<int> q;
            dist[0] = 0;
            q.push(0);
            while (!q.empty()) {
                int u = q.front(); q.pop();
                if (u == n - 1) return dist[u];
                for (int v : g[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.push(v);
                    }
                }
            }
            return -1; // should never happen
        };
        
        vector<int> ans;
        for (auto& qu : queries) {
            int u = qu[0], v = qu[1];
            adj[u].push_back(v);
            ans.push_back(bfs(adj));
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] shortestDistanceAfterQueries(int n, int[][] queries) {
        @SuppressWarnings("unchecked")
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        // initial chain edges
        for (int i = 0; i < n - 1; i++) {
            adj[i].add(i + 1);
        }

        int q = queries.length;
        int[] answer = new int[q];
        for (int idx = 0; idx < q; idx++) {
            int u = queries[idx][0];
            int v = queries[idx][1];
            adj[u].add(v); // add new road

            // BFS to find shortest distance from 0 to n-1
            int[] dist = new int[n];
            Arrays.fill(dist, -1);
            ArrayDeque<Integer> deque = new ArrayDeque<>();
            dist[0] = 0;
            deque.add(0);
            while (!deque.isEmpty()) {
                int cur = deque.poll();
                if (cur == n - 1) break;
                for (int nb : adj[cur]) {
                    if (dist[nb] == -1) {
                        dist[nb] = dist[cur] + 1;
                        deque.add(nb);
                    }
                }
            }
            answer[idx] = dist[n - 1];
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque

        # build initial graph with edges i -> i+1
        adj = [[] for _ in range(n)]
        for i in range(n - 1):
            adj[i].append(i + 1)

        ans = []
        for u, v in queries:
            adj[u].append(v)
            # BFS to find shortest path from 0 to n-1
            dist = [-1] * n
            q = deque([0])
            dist[0] = 0
            while q:
                node = q.popleft()
                if node == n - 1:
                    break
                dnext = dist[node] + 1
                for nb in adj[node]:
                    if dist[nb] == -1:
                        dist[nb] = dnext
                        q.append(nb)
            ans.append(dist[n - 1])
        return ans
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for i in range(n - 1):
            adj[i].append(i + 1)

        def bfs() -> int:
            visited = [False] * n
            q = deque()
            q.append((0, 0))
            visited[0] = True
            while q:
                node, dist = q.popleft()
                if node == n - 1:
                    return dist
                for nb in adj[node]:
                    if not visited[nb]:
                        visited[nb] = True
                        q.append((nb, dist + 1))
            return -1

        ans = []
        for u, v in queries:
            adj[u].append(v)
            ans.append(bfs())
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

int* shortestDistanceAfterQueries(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    // adjacency list
    static int adj[501][1000];
    int adjCnt[501] = {0};

    // initial consecutive edges
    for (int i = 0; i < n - 1; ++i) {
        adj[i][adjCnt[i]++] = i + 1;
    }

    int *answer = (int *)malloc(sizeof(int) * queriesSize);
    *returnSize = queriesSize;

    // temporary arrays for BFS
    int q[501];
    int visited[501];

    for (int qi = 0; qi < queriesSize; ++qi) {
        int u = queries[qi][0];
        int v = queries[qi][1];
        adj[u][adjCnt[u]++] = v;   // add new road

        // BFS from 0 to n-1
        memset(visited, 0, sizeof(int) * n);
        int front = 0, back = 0;
        q[back++] = 0;
        visited[0] = 1;
        int dist = 0;
        int found = 0;

        while (front < back && !found) {
            int layerSize = back - front;
            for (int i = 0; i < layerSize; ++i) {
                int node = q[front++];
                if (node == n - 1) {
                    found = 1;
                    break;
                }
                for (int j = 0; j < adjCnt[node]; ++j) {
                    int nb = adj[node][j];
                    if (!visited[nb]) {
                        visited[nb] = 1;
                        q[back++] = nb;
                    }
                }
            }
            if (!found) dist++;
        }

        answer[qi] = dist;
    }

    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] ShortestDistanceAfterQueries(int n, int[][] queries) {
        var adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        for (int i = 0; i < n - 1; i++) adj[i].Add(i + 1);

        int[] answer = new int[queries.Length];

        for (int q = 0; q < queries.Length; q++) {
            int u = queries[q][0];
            int v = queries[q][1];
            adj[u].Add(v);

            // BFS to find shortest path from 0 to n-1
            var dist = new int[n];
            Array.Fill(dist, -1);
            var queue = new Queue<int>();
            dist[0] = 0;
            queue.Enqueue(0);

            while (queue.Count > 0) {
                int cur = queue.Dequeue();
                if (cur == n - 1) break;
                foreach (int nb in adj[cur]) {
                    if (dist[nb] == -1) {
                        dist[nb] = dist[cur] + 1;
                        queue.Enqueue(nb);
                    }
                }
            }

            answer[q] = dist[n - 1];
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
var shortestDistanceAfterQueries = function(n, queries) {
    const adj = Array.from({ length: n }, () => []);
    for (let i = 0; i < n - 1; ++i) {
        adj[i].push(i + 1);
    }
    
    const bfs = () => {
        const dist = new Array(n).fill(-1);
        const queue = [];
        let head = 0;
        queue.push(0);
        dist[0] = 0;
        while (head < queue.length) {
            const cur = queue[head++];
            if (cur === n - 1) return dist[cur];
            for (const nb of adj[cur]) {
                if (dist[nb] === -1) {
                    dist[nb] = dist[cur] + 1;
                    queue.push(nb);
                }
            }
        }
        return -1; // should never happen
    };
    
    const answer = [];
    for (const [u, v] of queries) {
        adj[u].push(v);
        answer.push(bfs());
    }
    return answer;
};
```

## Typescript

```typescript
function shortestDistanceAfterQueries(n: number, queries: number[][]): number[] {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (let i = 0; i < n - 1; i++) {
        adj[i].push(i + 1);
    }

    const answer: number[] = [];

    for (const [u, v] of queries) {
        adj[u].push(v);

        // BFS to find shortest distance from 0 to n-1
        const dist = new Int16Array(n);
        dist.fill(-1);
        const queue: number[] = new Array<number>(n);
        let head = 0,
            tail = 0;
        queue[tail++] = 0;
        dist[0] = 0;

        while (head < tail) {
            const node = queue[head++];
            if (node === n - 1) break;
            for (const nb of adj[node]) {
                if (dist[nb] === -1) {
                    dist[nb] = dist[node] + 1;
                    queue[tail++] = nb;
                }
            }
        }

        answer.push(dist[n - 1]);
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function shortestDistanceAfterQueries($n, $queries) {
        // Build initial adjacency list with edges i -> i+1
        $adj = array_fill(0, $n, []);
        for ($i = 0; $i < $n - 1; ++$i) {
            $adj[$i][] = $i + 1;
        }

        $answer = [];

        foreach ($queries as $q) {
            [$u, $v] = $q;
            // Add new edge
            $adj[$u][] = $v;

            // DP from right to left (graph is a DAG)
            $dp = array_fill(0, $n, $n); // large sentinel
            $dp[$n - 1] = 0;
            for ($i = $n - 2; $i >= 0; --$i) {
                $best = $n; // sentinel larger than any possible distance
                foreach ($adj[$i] as $to) {
                    $cand = $dp[$to] + 1;
                    if ($cand < $best) {
                        $best = $cand;
                    }
                }
                $dp[$i] = $best;
            }

            $answer[] = $dp[0];
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func shortestDistanceAfterQueries(_ n: Int, _ queries: [[Int]]) -> [Int] {
        var adj = Array(repeating: [Int](), count: n)
        if n > 1 {
            for i in 0..<(n - 1) {
                adj[i].append(i + 1)
            }
        }
        var dp = Array(repeating: 0, count: n)
        var answer = [Int]()
        
        for query in queries {
            let u = query[0]
            let v = query[1]
            adj[u].append(v)
            
            dp[n - 1] = 0
            if n >= 2 {
                for i in stride(from: n - 2, through: 0, by: -1) {
                    var best = Int.max
                    for nb in adj[i] {
                        let cand = 1 + dp[nb]
                        if cand < best { best = cand }
                    }
                    dp[i] = best
                }
            }
            answer.append(dp[0])
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shortestDistanceAfterQueries(n: Int, queries: Array<IntArray>): IntArray {
        val adj = Array(n) { mutableListOf<Int>() }
        for (i in 0 until n - 1) {
            adj[i].add(i + 1)
        }

        val answer = IntArray(queries.size)
        var idx = 0
        for (q in queries) {
            val u = q[0]
            val v = q[1]
            adj[u].add(v)

            // BFS to find shortest distance from 0 to n-1
            val dist = IntArray(n) { -1 }
            val deque: ArrayDeque<Int> = ArrayDeque()
            dist[0] = 0
            deque.add(0)
            while (deque.isNotEmpty()) {
                val cur = deque.removeFirst()
                if (cur == n - 1) break
                for (next in adj[cur]) {
                    if (dist[next] == -1) {
                        dist[next] = dist[cur] + 1
                        deque.add(next)
                    }
                }
            }
            answer[idx++] = dist[n - 1]
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> shortestDistanceAfterQueries(int n, List<List<int>> queries) {
    // Initialize adjacency list with the default consecutive edges.
    List<List<int>> adj = List.generate(n, (_) => <int>[]);
    for (int i = 0; i < n - 1; ++i) {
      adj[i].add(i + 1);
    }

    List<int> answer = [];

    for (var query in queries) {
      int u = query[0];
      int v = query[1];
      // Add the new road.
      adj[u].add(v);

      // Compute shortest distances to city n-1 using DP on DAG.
      List<int> dp = List.filled(n, n); // large initial value
      dp[n - 1] = 0;
      for (int i = n - 2; i >= 0; --i) {
        int best = n;
        for (int nb in adj[i]) {
          int cand = dp[nb] + 1;
          if (cand < best) best = cand;
        }
        dp[i] = best;
      }

      answer.add(dp[0]);
    }

    return answer;
  }
}
```

## Golang

```go
func shortestDistanceAfterQueries(n int, queries [][]int) []int {
    adj := make([][]int, n)
    for i := 0; i < n-1; i++ {
        adj[i] = append(adj[i], i+1)
    }

    res := make([]int, len(queries))
    const INF = int(^uint(0) >> 1) // max int

    for idx, q := range queries {
        u, v := q[0], q[1]
        adj[u] = append(adj[u], v)

        dp := make([]int, n)
        for i := 0; i < n; i++ {
            dp[i] = INF
        }
        dp[n-1] = 0

        for i := n - 2; i >= 0; i-- {
            best := INF
            for _, nb := range adj[i] {
                if d := dp[nb] + 1; d < best {
                    best = d
                }
            }
            dp[i] = best
        }
        res[idx] = dp[0]
    }

    return res
}
```

## Ruby

```ruby
def shortest_distance_after_queries(n, queries)
  adj = Array.new(n) { [] }
  (0...n - 1).each { |i| adj[i] << i + 1 }

  answers = []

  queries.each do |u, v|
    adj[u] << v

    visited = Array.new(n, false)
    dist = Array.new(n, 0)
    queue = [0]
    visited[0] = true
    front = 0

    while front < queue.length
      node = queue[front]
      front += 1
      break if node == n - 1

      adj[node].each do |nbr|
        next if visited[nbr]

        visited[nbr] = true
        dist[nbr] = dist[node] + 1
        queue << nbr
      end
    end

    answers << dist[n - 1]
  end

  answers
end
```

## Scala

```scala
object Solution {
  def shortestDistanceAfterQueries(n: Int, queries: Array[Array[Int]]): Array[Int] = {
    val adj = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (i <- 0 until n - 1) {
      adj(i).append(i + 1)
    }
    val result = new scala.collection.mutable.ArrayBuffer[Int]()
    val dist = new Array[Int](n)
    import java.util.{ArrayDeque, Arrays}
    for (q <- queries) {
      val u = q(0)
      val v = q(1)
      adj(u).append(v)

      Arrays.fill(dist, -1)
      val queue = new ArrayDeque[Int]()
      dist(0) = 0
      queue.add(0)
      var answer = -1

      while (!queue.isEmpty) {
        val cur = queue.poll()
        if (cur == n - 1) {
          answer = dist(cur)
          queue.clear() // exit loop early
        } else {
          val neighbors = adj(cur)
          var i = 0
          while (i < neighbors.length) {
            val nb = neighbors(i)
            if (dist(nb) == -1) {
              dist(nb) = dist(cur) + 1
              queue.add(nb)
            }
            i += 1
          }
        }
      }

      result.append(answer)
    }
    result.toArray
  }
}
```

## Rust

```rust
impl Solution {
    pub fn shortest_distance_after_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for i in 0..n - 1 {
            adj[i].push(i + 1);
        }
        let mut answer = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let u = q[0] as usize;
            let v = q[1] as usize;
            adj[u].push(v);
            // DP on DAG (edges only go forward)
            let mut dp = vec![0usize; n];
            dp[n - 1] = 0;
            for i in (0..n - 1).rev() {
                let mut best = usize::MAX;
                for &to in &adj[i] {
                    if dp[to] < best {
                        best = dp[to];
                    }
                }
                dp[i] = best + 1; // at least one outgoing edge exists
            }
            answer.push(dp[0] as i32);
        }
        answer
    }
}
```

## Racket

```racket
#lang racket
(provide shortest-distance-after-queries)

(define (bfs n adj)
  (let ([visited (make-vector n #f)])
    (vector-set! visited 0 #t)
    (let bfs-loop ([queue (list 0)] [dist 0])
      (cond
        [(null? queue) -1]
        [(member (- n 1) queue) dist]
        [else
         (define next '())
         (for ([node queue])
           (for ([nbr (vector-ref adj node)])
             (unless (vector-ref visited nbr)
               (vector-set! visited nbr #t)
               (set! next (cons nbr next)))))
         (bfs-loop next (+ dist 1))]))))

(define/contract (shortest-distance-after-queries n queries)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (let ([adj (make-vector n '())])
    ;; initial consecutive edges
    (for ([i (in-range (- n 1))])
      (vector-set! adj i (cons (+ i 1) (vector-ref adj i))))
    (let loop ([qs queries] [ans '()])
      (if (null? qs)
          (reverse ans)
          (let* ([pair (car qs)]
                 [u (first pair)]
                 [v (second pair)])
            (vector-set! adj u (cons v (vector-ref adj u)))
            (define d (bfs n adj))
            (loop (cdr qs) (cons d ans)))))))
```

## Erlang

```erlang
-module(solution).
-export([shortest_distance_after_queries/2]).

-spec shortest_distance_after_queries(N :: integer(), Queries :: [[integer()]]) -> [integer()].
shortest_distance_after_queries(N, Queries) ->
    Adj0 = init_adj(N),
    process_queries(Queries, Adj0, []).

init_adj(N) ->
    lists:foldl(fun(I, M) ->
        List = if I < N-1 -> [I+1]; true -> [] end,
        maps:put(I, List, M)
    end, #{}, lists:seq(0, N-1)).

process_queries([], _Adj, Acc) ->
    lists:reverse(Acc);
process_queries([[U,V]|Rest], Adj, Acc) ->
    OldList = maps:get(U, Adj),
    NewAdj = maps:put(U, [V|OldList], Adj),
    Dist = compute_shortest(N, NewAdj),
    process_queries(Rest, NewAdj, [Dist | Acc]).

compute_shortest(N, Adj) ->
    DP0 = #{N-1 => 0},
    DP = compute_dp(N-2, Adj, DP0),
    maps:get(0, DP).

compute_dp(-1, _Adj, DP) -> DP;
compute_dp(I, Adj, DP) ->
    Neigh = maps:get(I, Adj),
    MinDist = lists:min([maps:get(V, DP) + 1 || V <- Neigh]),
    NewDP = maps:put(I, MinDist, DP),
    compute_dp(I-1, Adj, NewDP).
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_distance_after_queries(n :: integer, queries :: [[integer]]) :: [integer]
  def shortest_distance_after_queries(n, queries) do
    # initial adjacency list: edge i -> i+1 for i < n-1
    adj0 =
      Enum.map(0..(n - 1), fn i ->
        if i < n - 1, do: [i + 1], else: []
      end)

    {answers_rev, _} =
      Enum.reduce(queries, {[], adj0}, fn [u, v], {ans_acc, cur_adj} ->
        # add new edge u -> v
        updated = [v | Enum.at(cur_adj, u)]
        new_adj = List.replace_at(cur_adj, u, updated)

        # compute shortest distance from 0 to n-1
        dist = compute_dp(new_adj, n)
        {[dist | ans_acc], new_adj}
      end)

    Enum.reverse(answers_rev)
  end

  defp compute_dp(adj, n) do
    init_arr = :array.set(n - 1, 0, :array.new(n, default: 0))

    dp_arr =
      Enum.reduce(Enum.reverse(0..(n - 2)), init_arr, fn i, acc ->
        neighbors = Enum.at(adj, i)

        min_dist =
          Enum.reduce(neighbors, n + 1, fn nb, best ->
            d = :array.get(nb, acc) + 1
            if d < best, do: d, else: best
          end)

        :array.set(i, min_dist, acc)
      end)

    :array.get(0, dp_arr)
  end
end
```

# 1377. Frog Position After T Seconds

## Cpp

```cpp
class Solution {
public:
    int T, TARGET;
    vector<vector<int>> g;
    
    double dfs(int node, int parent, int time, double prob) {
        if (time == T) {
            return node == TARGET ? prob : 0.0;
        }
        int childCnt = g[node].size() - (parent == 0 ? 0 : 1);
        if (childCnt == 0) { // leaf, stays forever
            return node == TARGET ? prob : 0.0;
        }
        double res = 0.0;
        for (int nxt : g[node]) {
            if (nxt == parent) continue;
            res += dfs(nxt, node, time + 1, prob / childCnt);
        }
        return res;
    }
    
    double frogPosition(int n, vector<vector<int>>& edges, int t, int target) {
        T = t;
        TARGET = target;
        g.assign(n + 1, {});
        for (auto &e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        return dfs(1, 0, 0, 1.0);
    }
};
```

## Java

```java
class Solution {
    private List<Integer>[] graph;
    private boolean[] visited;
    private int target;
    private int maxTime;

    public double frogPosition(int n, int[][] edges, int t, int target) {
        this.graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; ++i) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }
        this.visited = new boolean[n + 1];
        this.target = target;
        this.maxTime = t;
        visited[1] = true;
        return dfs(1, 0, 1.0);
    }

    private double dfs(int node, int time, double prob) {
        if (time == maxTime) {
            return node == target ? prob : 0.0;
        }
        if (node == target) {
            int cnt = 0;
            for (int nb : graph[node]) {
                if (!visited[nb]) cnt++;
            }
            return cnt == 0 ? prob : 0.0;
        }

        int unvisited = 0;
        for (int nb : graph[node]) {
            if (!visited[nb]) unvisited++;
        }
        if (unvisited == 0) return 0.0;

        double sum = 0.0;
        for (int nb : graph[node]) {
            if (!visited[nb]) {
                visited[nb] = true;
                sum += dfs(nb, time + 1, prob / unvisited);
                visited[nb] = false;
            }
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        adj = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, parent, time_elapsed, prob):
            if time_elapsed == t:
                return prob if node == target else 0.0
            if node == target:
                # If no unvisited neighbors, frog stays forever.
                if len(adj[node]) - (1 if parent != 0 else 0) == 0:
                    return prob
                return 0.0
            children = [nei for nei in adj[node] if nei != parent]
            if not children:
                return 0.0
            p_each = prob / len(children)
            total = 0.0
            for child in children:
                total += dfs(child, node, time_elapsed + 1, p_each)
            return total

        return dfs(1, 0, 0, 1.0)
```

## Python3

```python
from typing import List

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        adj = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node: int, parent: int, time: int, prob: float) -> float:
            if time == t:
                return prob if node == target else 0.0
            # If reached target before time runs out
            if node == target:
                # No further moves possible from this node
                if len(adj[node]) - (1 if parent != -1 else 0) == 0:
                    return prob
                return 0.0

            children = [nei for nei in adj[node] if nei != parent]
            if not children:
                return 0.0

            p_each = prob / len(children)
            total = 0.0
            for child in children:
                total += dfs(child, node, time + 1, p_each)
            return total

        return dfs(1, -1, 0, 1.0)
```

## C

```c
#include <stddef.h>

static int adj[101][101];
static int deg[101];
static int g_target;
static int g_t;
static double g_ans;

static void dfs(int node, int parent, int time, double prob) {
    if (node == g_target) {
        int children = deg[node] - (parent != 0);
        if (time == g_t || (time < g_t && children == 0)) {
            g_ans += prob;
        }
    }
    if (time == g_t) return;

    int children = deg[node] - (parent != 0);
    if (children == 0) return; // cannot move further

    double nextProb = prob / children;
    for (int i = 0; i < deg[node]; ++i) {
        int nxt = adj[node][i];
        if (nxt == parent) continue;
        dfs(nxt, node, time + 1, nextProb);
    }
}

double frogPosition(int n, int** edges, int edgesSize, int* edgesColSize, int t, int target) {
    for (int i = 1; i <= n; ++i) deg[i] = 0;
    for (int i = 0; i < edgesSize; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        adj[a][deg[a]++] = b;
        adj[b][deg[b]++] = a;
    }
    g_target = target;
    g_t = t;
    g_ans = 0.0;

    dfs(1, 0, 0, 1.0);
    return g_ans;
}
```

## Csharp

```csharp
public class Solution {
    private List<int>[] graph;
    private int targetNode;
    private int maxTime;

    public double FrogPosition(int n, int[][] edges, int t, int target) {
        targetNode = target;
        maxTime = t;
        graph = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            graph[a].Add(b);
            graph[b].Add(a);
        }
        return Dfs(1, 0, 0, 1.0);
    }

    private double Dfs(int node, int parent, int time, double prob) {
        if (time == maxTime) {
            return node == targetNode ? prob : 0.0;
        }

        int unvisited = graph[node].Count - (parent == 0 ? 0 : 1);

        // If at target and cannot move further, stay there.
        if (node == targetNode && unvisited == 0) {
            return prob;
        }

        // No where to go and not the target -> probability zero.
        if (unvisited == 0) {
            return 0.0;
        }

        double res = 0.0;
        foreach (int nxt in graph[node]) {
            if (nxt != parent) {
                res += Dfs(nxt, node, time + 1, prob / unvisited);
            }
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} t
 * @param {number} target
 * @return {number}
 */
var frogPosition = function(n, edges, t, target) {
    const adj = Array.from({length: n + 1}, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    
    function dfs(node, parent, timeLeft, prob) {
        // If no time left, frog stays where it is
        if (timeLeft === 0) {
            return node === target ? prob : 0;
        }
        const children = [];
        for (const nb of adj[node]) {
            if (nb !== parent) children.push(nb);
        }
        // Leaf node: frog stays forever
        if (children.length === 0) {
            return node === target ? prob : 0;
        }
        // If current node is the target but it can still move, probability becomes zero
        if (node === target) {
            return 0;
        }
        const share = prob / children.length;
        let res = 0;
        for (const child of children) {
            res += dfs(child, node, timeLeft - 1, share);
        }
        return res;
    }
    
    return dfs(1, 0, t, 1.0);
};
```

## Typescript

```typescript
function frogPosition(n: number, edges: number[][], t: number, target: number): number {
    const adj: number[][] = Array.from({ length: n + 1 }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    function dfs(node: number, parent: number, time: number, prob: number): number {
        if (time === t) {
            return node === target ? prob : 0;
        }
        const children = adj[node].filter(v => v !== parent);
        if (children.length === 0) {
            // No unvisited neighbors; frog stays here forever
            return node === target ? prob : 0;
        }
        let sum = 0;
        const eachProb = prob / children.length;
        for (const child of children) {
            sum += dfs(child, node, time + 1, eachProb);
        }
        return sum;
    }

    return dfs(1, 0, 0, 1);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $t
     * @param Integer $target
     * @return Float
     */
    function frogPosition($n, $edges, $t, $target) {
        $adj = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            $adj[$a][] = $b;
            $adj[$b][] = $a;
        }

        $ans = 0.0;

        $dfs = function($node, $parent, $time, $prob) use (&$dfs, &$adj, $t, $target, &$ans) {
            if ($node == $target) {
                $childrenCount = count($adj[$node]) - ($parent ? 1 : 0);
                if ($time == $t || $childrenCount == 0) {
                    $ans = $prob;
                }
                return;
            }

            if ($time == $t) {
                return;
            }

            $children = [];
            foreach ($adj[$node] as $nei) {
                if ($nei != $parent) {
                    $children[] = $nei;
                }
            }

            $cnt = count($children);
            if ($cnt == 0) {
                return;
            }

            $newProb = $prob / $cnt;
            foreach ($children as $child) {
                $dfs($child, $node, $time + 1, $newProb);
            }
        };

        $dfs(1, 0, 0, 1.0);
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func frogPosition(_ n: Int, _ edges: [[Int]], _ t: Int, _ target: Int) -> Double {
        var graph = [[Int]](repeating: [], count: n + 1)
        for e in edges {
            let a = e[0], b = e[1]
            graph[a].append(b)
            graph[b].append(a)
        }
        
        var visited = [Bool](repeating: false, count: n + 1)
        var result = 0.0
        
        func dfs(_ node: Int, _ time: Int, _ prob: Double) {
            // If we are at the target and either we've used exactly t seconds
            // or cannot move further (leaf), this probability contributes.
            let unvisitedNeighbors = graph[node].filter { !visited[$0] }
            if node == target && (time == t || unvisitedNeighbors.isEmpty) {
                result += prob
            }
            
            // If time reached t, we stop exploring further moves.
            if time == t { return }
            
            let cnt = unvisitedNeighbors.count
            if cnt == 0 { return } // cannot move further
            
            for nb in unvisitedNeighbors {
                visited[nb] = true
                dfs(nb, time + 1, prob / Double(cnt))
                visited[nb] = false
            }
        }
        
        visited[1] = true
        dfs(1, 0, 1.0)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun frogPosition(n: Int, edges: Array<IntArray>, t: Int, target: Int): Double {
        val adj = Array(n + 1) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }
        var answer = 0.0
        fun dfs(node: Int, parent: Int, prob: Double, time: Int) {
            if (node == target) {
                val unvisited = adj[node].size - if (parent == -1) 0 else 1
                if (time == t || unvisited == 0) {
                    answer = prob
                }
                return
            }
            if (time == t) return
            val unvisited = adj[node].size - if (parent == -1) 0 else 1
            if (unvisited == 0) return
            for (next in adj[node]) {
                if (next != parent) {
                    dfs(next, node, prob / unvisited, time + 1)
                }
            }
        }
        dfs(1, -1, 1.0, 0)
        return answer
    }
}
```

## Dart

```dart
class Solution {
  double frogPosition(int n, List<List<int>> edges, int t, int target) {
    List<List<int>> graph = List.generate(n + 1, (_) => []);
    for (var e in edges) {
      int a = e[0];
      int b = e[1];
      graph[a].add(b);
      graph[b].add(a);
    }

    double dfs(int node, int parent, int curTime, double prob) {
      if (node == target) {
        int unvisited = graph[node].length - (parent == 0 ? 0 : 1);
        if (curTime == t || unvisited == 0) return prob;
        return 0.0;
      }
      if (curTime >= t) return 0.0;
      int unvisited = graph[node].length - (parent == 0 ? 0 : 1);
      if (unvisited == 0) return 0.0;
      double sum = 0.0;
      for (int nei in graph[node]) {
        if (nei == parent) continue;
        sum += dfs(nei, node, curTime + 1, prob / unvisited);
      }
      return sum;
    }

    return dfs(1, 0, 0, 1.0);
  }
}
```

## Golang

```go
func frogPosition(n int, edges [][]int, t int, target int) float64 {
	adj := make([][]int, n+1)
	for _, e := range edges {
		a, b := e[0], e[1]
		adj[a] = append(adj[a], b)
		adj[b] = append(adj[b], a)
	}

	var dfs func(node, parent, timeLeft int, prob float64) float64
	dfs = func(node, parent, timeLeft int, prob float64) float64 {
		if node == target {
			// number of unvisited neighbors from this node
			cnt := len(adj[node])
			if parent != 0 {
				cnt--
			}
			if timeLeft == 0 || cnt == 0 {
				return prob
			}
			return 0.0
		}
		if timeLeft == 0 {
			return 0.0
		}
		// count unvisited neighbors
		cnt := len(adj[node])
		if parent != 0 {
			cnt--
		}
		if cnt == 0 { // leaf, frog stays here forever but not target
			return 0.0
		}
		per := prob / float64(cnt)
		sum := 0.0
		for _, nb := range adj[node] {
			if nb == parent {
				continue
			}
			sum += dfs(nb, node, timeLeft-1, per)
		}
		return sum
	}

	return dfs(1, 0, t, 1.0)
}
```

## Ruby

```ruby
def frog_position(n, edges, t, target)
  adj = Array.new(n + 1) { [] }
  edges.each do |u, v|
    adj[u] << v
    adj[v] << u
  end

  dfs = lambda do |node, parent, time, prob|
    if node == target
      children_cnt = adj[node].size - (parent ? 1 : 0)
      return prob if time == t || children_cnt == 0
    end

    return 0.0 if time >= t

    children = []
    adj[node].each do |nei|
      next if nei == parent
      children << nei
    end

    return 0.0 if children.empty?

    prob_per_child = prob / children.size.to_f
    sum = 0.0
    children.each do |child|
      sum += dfs.call(child, node, time + 1, prob_per_child)
    end
    sum
  end

  dfs.call(1, nil, 0, 1.0)
end
```

## Scala

```scala
object Solution {
    def frogPosition(n: Int, edges: Array[Array[Int]], t: Int, target: Int): Double = {
        val adj = Array.fill[List[Int]](n + 1)(List())
        for (e <- edges) {
            val a = e(0)
            val b = e(1)
            adj(a) = b :: adj(a)
            adj(b) = a :: adj(b)
        }

        def dfs(node: Int, parent: Int, time: Int, prob: Double): Double = {
            if (time > t) return 0.0
            if (node == target) {
                val children = adj(node).count(_ != parent)
                if (time == t || children == 0) return prob else return 0.0
            }
            if (time == t) return 0.0

            val children = adj(node).filter(_ != parent)
            val cnt = children.size
            var sum = 0.0
            for (child <- children) {
                sum += dfs(child, node, time + 1, prob / cnt)
            }
            sum
        }

        dfs(1, 0, 0, 1.0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn frog_position(n: i32, edges: Vec<Vec<i32>>, t: i32, target: i32) -> f64 {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n_usize + 1];
        for e in edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }

        fn dfs(
            node: usize,
            parent: usize,
            time: i32,
            prob: f64,
            t: i32,
            target: usize,
            adj: &Vec<Vec<usize>>,
        ) -> f64 {
            let child_cnt = if parent == 0 { adj[node].len() } else { adj[node].len() - 1 };
            if node == target {
                if time == t || child_cnt == 0 {
                    return prob;
                } else {
                    return 0.0;
                }
            }
            if time == t {
                return 0.0;
            }
            if child_cnt == 0 {
                return 0.0;
            }
            let mut sum = 0.0;
            for &next in adj[node].iter() {
                if next != parent {
                    sum += dfs(next, node, time + 1, prob / child_cnt as f64, t, target, adj);
                }
            }
            sum
        }

        dfs(1, 0, 0, 1.0, t, target as usize, &adj)
    }
}
```

## Racket

```racket
#lang racket

(provide frog-position)

(define/contract (frog-position n edges t target)
  (-> exact-integer?
      (listof (listof exact-integer?))
      exact-integer?
      exact-integer?
      flonum?)
  (let ([adj (make-vector (+ n 1) '())])
    (for ([e edges])
      (define a (first e))
      (define b (second e))
      (vector-set! adj a (cons b (vector-ref adj a)))
      (vector-set! adj b (cons a (vector-ref adj b))))
    (letrec ((dfs
              (lambda (node parent time prob)
                (cond
                  [(> time t) 0.0]
                  [(= node target)
                   (let* ([children (filter (lambda (nbr) (not (= nbr parent)))
                                            (vector-ref adj node))]
                          [cnt (length children)])
                     (if (or (= time t) (and (< time t) (= cnt 0)))
                         prob
                         0.0))]
                  [else
                   (let* ([children (filter (lambda (nbr) (not (= nbr parent)))
                                            (vector-ref adj node))]
                          [cnt (length children)])
                     (if (or (= cnt 0) (= time t))
                         0.0
                         (for/sum ([child children])
                           (dfs child node (+ time 1)
                                (* prob (/ 1.0 cnt))))))]))))
      (dfs 1 0 0 1.0))))
```

## Erlang

```erlang
-module(solution).
-export([frog_position/4]).

-spec frog_position(N :: integer(), Edges :: [[integer()]], T :: integer(), Target :: integer()) -> float().
frog_position(_N, Edges, T, Target) ->
    Adj = build_adj(Edges, #{}),
    Visited0 = #{1 => true},
    dfs(1, 0, 1.0, Visited0, Target, T, Adj).

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

dfs(Node, Time, Prob, Visited, Target, MaxT, Adj) ->
    case Node == Target of
        true ->
            if Time == MaxT ->
                    Prob;
               true ->
                    Unvisited = [N || N <- maps:get(Node, Adj, []), not maps:is_key(N, Visited)],
                    case Unvisited of
                        [] -> Prob; % stays forever
                        _  -> 0.0
                    end
            end;
        false ->
            if Time == MaxT ->
                    0.0;
               true ->
                    Unvisited = [N || N <- maps:get(Node, Adj, []), not maps:is_key(N, Visited)],
                    case Unvisited of
                        [] -> 0.0;
                        _ ->
                            Len = length(Unvisited),
                            ProbPer = Prob / Len,
                            lists:foldl(fun(Next, Acc) ->
                                Acc + dfs(Next, Time+1, ProbPer, maps:put(Next, true, Visited), Target, MaxT, Adj)
                            end, 0.0, Unvisited)
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec frog_position(n :: integer, edges :: [[integer]], t :: integer, target :: integer) :: float
  def frog_position(_n, edges, t, target) do
    adj =
      Enum.reduce(edges, %{}, fn [a, b], acc ->
        acc
        |> Map.update(a, [b], &[b | &1])
        |> Map.update(b, [a], &[a | &1])
      end)

    dfs(1, 0, t, 1.0, target, adj)
  end

  defp dfs(node, parent, time, prob, target, adj) do
    if node == target do
      children = Enum.filter(Map.get(adj, node, []), fn x -> x != parent end)

      if time == 0 or length(children) == 0 do
        prob
      else
        0.0
      end
    else
      if time == 0 do
        0.0
      else
        children = Enum.filter(Map.get(adj, node, []), fn x -> x != parent end)
        cnt = length(children)

        if cnt == 0 do
          0.0
        else
          new_prob = prob / cnt

          Enum.reduce(children, 0.0, fn child, acc ->
            acc + dfs(child, node, time - 1, new_prob, target, adj)
          end)
        end
      end
    end
  end
end
```

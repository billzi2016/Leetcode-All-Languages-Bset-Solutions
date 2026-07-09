# 1584. Min Cost to Connect All Points

## Cpp

```cpp
class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        vector<int> minDist(n, INT_MAX);
        vector<bool> visited(n, false);
        minDist[0] = 0;
        long long total = 0;
        for (int i = 0; i < n; ++i) {
            int u = -1;
            int best = INT_MAX;
            for (int j = 0; j < n; ++j) {
                if (!visited[j] && minDist[j] < best) {
                    best = minDist[j];
                    u = j;
                }
            }
            visited[u] = true;
            total += best;
            for (int v = 0; v < n; ++v) {
                if (!visited[v]) {
                    int w = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1]);
                    if (w < minDist[v]) minDist[v] = w;
                }
            }
        }
        return static_cast<int>(total);
    }
};
```

## Java

```java
class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        boolean[] visited = new boolean[n];
        int[] minDist = new int[n];
        java.util.Arrays.fill(minDist, Integer.MAX_VALUE);
        minDist[0] = 0;
        long total = 0;
        for (int i = 0; i < n; i++) {
            int u = -1;
            int best = Integer.MAX_VALUE;
            for (int j = 0; j < n; j++) {
                if (!visited[j] && minDist[j] < best) {
                    best = minDist[j];
                    u = j;
                }
            }
            visited[u] = true;
            total += best;
            for (int v = 0; v < n; v++) {
                if (!visited[v]) {
                    int w = Math.abs(points[u][0] - points[v][0]) + Math.abs(points[u][1] - points[v][1]);
                    if (w < minDist[v]) {
                        minDist[v] = w;
                    }
                }
            }
        }
        return (int) total;
    }
}
```

## Python

```python
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        in_mst = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        total_cost = 0

        for _ in range(n):
            # select the vertex with minimum distance to the MST
            u = -1
            best = float('inf')
            for i in range(n):
                if not in_mst[i] and min_dist[i] < best:
                    best = min_dist[i]
                    u = i

            in_mst[u] = True
            total_cost += best

            # update distances using the newly added vertex
            ux, uy = points[u]
            for v in range(n):
                if not in_mst[v]:
                    vx, vy = points[v]
                    d = abs(ux - vx) + abs(uy - vy)
                    if d < min_dist[v]:
                        min_dist[v] = d

        return total_cost
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        visited = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        heap = [(0, 0)]  # (cost, node)
        total_cost = 0
        visited_count = 0

        while visited_count < n:
            cost, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            total_cost += cost
            visited_count += 1

            ux, uy = points[u]
            for v in range(n):
                if not visited[v]:
                    vx, vy = points[v]
                    w = abs(ux - vx) + abs(uy - vy)
                    if w < min_dist[v]:
                        min_dist[v] = w
                        heapq.heappush(heap, (w, v))

        return total_cost
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int minCostConnectPoints(int** points, int pointsSize, int* pointsColSize) {
    if (pointsSize == 0) return 0;
    int *visited = (int *)calloc(pointsSize, sizeof(int));
    int *minDist = (int *)malloc(pointsSize * sizeof(int));
    for (int i = 0; i < pointsSize; ++i) {
        minDist[i] = INT_MAX;
    }
    minDist[0] = 0;
    long long total = 0;

    for (int i = 0; i < pointsSize; ++i) {
        int u = -1;
        int best = INT_MAX;
        for (int j = 0; j < pointsSize; ++j) {
            if (!visited[j] && minDist[j] < best) {
                best = minDist[j];
                u = j;
            }
        }
        visited[u] = 1;
        total += best;

        int ux = points[u][0];
        int uy = points[u][1];
        for (int v = 0; v < pointsSize; ++v) {
            if (!visited[v]) {
                int vx = points[v][0];
                int vy = points[v][1];
                int dist = abs(ux - vx) + abs(uy - vy);
                if (dist < minDist[v]) {
                    minDist[v] = dist;
                }
            }
        }
    }

    free(visited);
    free(minDist);
    return (int)total;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MinCostConnectPoints(int[][] points) {
        int n = points.Length;
        bool[] visited = new bool[n];
        int[] minDist = new int[n];
        for (int i = 0; i < n; i++) minDist[i] = int.MaxValue;
        minDist[0] = 0;
        int totalCost = 0;

        for (int i = 0; i < n; i++) {
            int u = -1;
            int best = int.MaxValue;
            for (int j = 0; j < n; j++) {
                if (!visited[j] && minDist[j] < best) {
                    best = minDist[j];
                    u = j;
                }
            }

            visited[u] = true;
            totalCost += best;

            for (int v = 0; v < n; v++) {
                if (!visited[v]) {
                    int w = Math.Abs(points[u][0] - points[v][0]) + Math.Abs(points[u][1] - points[v][1]);
                    if (w < minDist[v]) {
                        minDist[v] = w;
                    }
                }
            }
        }

        return totalCost;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var minCostConnectPoints = function(points) {
    const n = points.length;
    const visited = new Array(n).fill(false);
    const minDist = new Array(n).fill(Infinity);
    minDist[0] = 0;
    let total = 0;

    for (let i = 0; i < n; i++) {
        // Find the unvisited node with the smallest distance
        let u = -1;
        let best = Infinity;
        for (let j = 0; j < n; j++) {
            if (!visited[j] && minDist[j] < best) {
                best = minDist[j];
                u = j;
            }
        }

        visited[u] = true;
        total += best;

        // Update distances to the remaining nodes
        for (let v = 0; v < n; v++) {
            if (!visited[v]) {
                const dist = Math.abs(points[u][0] - points[v][0]) + Math.abs(points[u][1] - points[v][1]);
                if (dist < minDist[v]) {
                    minDist[v] = dist;
                }
            }
        }
    }

    return total;
};
```

## Typescript

```typescript
function minCostConnectPoints(points: number[][]): number {
    const n = points.length;
    if (n <= 1) return 0;

    const visited = new Array(n).fill(false);
    const minDist = new Array(n).fill(Infinity);
    minDist[0] = 0;

    let total = 0;

    for (let i = 0; i < n; i++) {
        // select the unvisited node with smallest distance
        let u = -1;
        let best = Infinity;
        for (let j = 0; j < n; j++) {
            if (!visited[j] && minDist[j] < best) {
                best = minDist[j];
                u = j;
            }
        }

        visited[u] = true;
        total += best;

        const [ux, uy] = points[u];
        // update distances to remaining nodes
        for (let v = 0; v < n; v++) {
            if (!visited[v]) {
                const [vx, vy] = points[v];
                const d = Math.abs(ux - vx) + Math.abs(uy - vy);
                if (d < minDist[v]) {
                    minDist[v] = d;
                }
            }
        }
    }

    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function minCostConnectPoints($points) {
        $n = count($points);
        if ($n <= 1) return 0;

        $inMST = array_fill(0, $n, false);
        $minDist = array_fill(0, $n, PHP_INT_MAX);
        $minDist[0] = 0;
        $total = 0;

        for ($i = 0; $i < $n; $i++) {
            // Find the vertex with minimum distance not yet in MST
            $u = -1;
            $best = PHP_INT_MAX;
            for ($j = 0; $j < $n; $j++) {
                if (!$inMST[$j] && $minDist[$j] < $best) {
                    $best = $minDist[$j];
                    $u = $j;
                }
            }

            // Add the selected vertex to MST
            $inMST[$u] = true;
            $total += $best; // best is 0 for the first vertex

            // Update distances of adjacent vertices
            for ($v = 0; $v < $n; $v++) {
                if (!$inMST[$v]) {
                    $dist = abs($points[$u][0] - $points[$v][0]) + abs($points[$u][1] - $points[$v][1]);
                    if ($dist < $minDist[$v]) {
                        $minDist[$v] = $dist;
                    }
                }
            }
        }

        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func minCostConnectPoints(_ points: [[Int]]) -> Int {
        let n = points.count
        var inMST = [Bool](repeating: false, count: n)
        var minDist = [Int](repeating: Int.max, count: n)
        minDist[0] = 0
        var total = 0

        for _ in 0..<n {
            var u = -1
            var best = Int.max
            for i in 0..<n where !inMST[i] && minDist[i] < best {
                best = minDist[i]
                u = i
            }
            total += best
            inMST[u] = true

            for v in 0..<n where !inMST[v] {
                let dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                if dist < minDist[v] {
                    minDist[v] = dist
                }
            }
        }

        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCostConnectPoints(points: Array<IntArray>): Int {
        val n = points.size
        if (n <= 1) return 0
        val inMST = BooleanArray(n)
        val minDist = IntArray(n) { Int.MAX_VALUE }
        minDist[0] = 0
        var total = 0
        repeat(n) {
            var u = -1
            var best = Int.MAX_VALUE
            for (v in 0 until n) {
                if (!inMST[v] && minDist[v] < best) {
                    best = minDist[v]
                    u = v
                }
            }
            inMST[u] = true
            total += best
            for (v in 0 until n) {
                if (!inMST[v]) {
                    val dist = kotlin.math.abs(points[u][0] - points[v][0]) +
                               kotlin.math.abs(points[u][1] - points[v][1])
                    if (dist < minDist[v]) {
                        minDist[v] = dist
                    }
                }
            }
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int minCostConnectPoints(List<List<int>> points) {
    int n = points.length;
    List<bool> visited = List.filled(n, false);
    const int INF = 1 << 60;
    List<int> minDist = List.filled(n, INF);
    minDist[0] = 0;
    int totalCost = 0;

    for (int i = 0; i < n; ++i) {
      int u = -1;
      int best = INF;
      for (int j = 0; j < n; ++j) {
        if (!visited[j] && minDist[j] < best) {
          best = minDist[j];
          u = j;
        }
      }

      visited[u] = true;
      totalCost += best;

      for (int v = 0; v < n; ++v) {
        if (!visited[v]) {
          int dist = (points[u][0] - points[v][0]).abs() +
              (points[u][1] - points[v][1]).abs();
          if (dist < minDist[v]) {
            minDist[v] = dist;
          }
        }
      }
    }

    return totalCost;
  }
}
```

## Golang

```go
func minCostConnectPoints(points [][]int) int {
    n := len(points)
    if n == 0 {
        return 0
    }
    visited := make([]bool, n)
    const INF = int(^uint(0) >> 1) // max int
    minDist := make([]int, n)
    for i := range minDist {
        minDist[i] = INF
    }
    minDist[0] = 0
    total := 0

    abs := func(a int) int {
        if a < 0 {
            return -a
        }
        return a
    }

    for i := 0; i < n; i++ {
        u := -1
        best := INF
        for j := 0; j < n; j++ {
            if !visited[j] && minDist[j] < best {
                best = minDist[j]
                u = j
            }
        }
        visited[u] = true
        total += best

        for v := 0; v < n; v++ {
            if !visited[v] {
                d := abs(points[u][0]-points[v][0]) + abs(points[u][1]-points[v][1])
                if d < minDist[v] {
                    minDist[v] = d
                }
            }
        }
    }

    return total
}
```

## Ruby

```ruby
def min_cost_connect_points(points)
  n = points.length
  return 0 if n <= 1

  visited = Array.new(n, false)
  min_dist = Array.new(n, Float::INFINITY)
  min_dist[0] = 0
  total = 0

  n.times do
    u = -1
    best = Float::INFINITY
    (0...n).each do |i|
      if !visited[i] && min_dist[i] < best
        best = min_dist[i]
        u = i
      end
    end

    visited[u] = true
    total += best

    (0...n).each do |v|
      next if visited[v]
      dist = (points[u][0] - points[v][0]).abs + (points[u][1] - points[v][1]).abs
      min_dist[v] = dist if dist < min_dist[v]
    end
  end

  total
end
```

## Scala

```scala
object Solution {
    def minCostConnectPoints(points: Array[Array[Int]]): Int = {
        val n = points.length
        if (n <= 1) return 0

        val visited = new Array[Boolean](n)
        val minDist = Array.fill(n)(Int.MaxValue)
        minDist(0) = 0

        var total = 0L

        var count = 0
        while (count < n) {
            var u = -1
            var best = Int.MaxValue
            var i = 0
            while (i < n) {
                if (!visited(i) && minDist(i) < best) {
                    best = minDist(i)
                    u = i
                }
                i += 1
            }

            visited(u) = true
            total += best
            count += 1

            var j = 0
            while (j < n) {
                if (!visited(j)) {
                    val d = math.abs(points(u)(0) - points(j)(0)) + math.abs(points(u)(1) - points(j)(1))
                    if (d < minDist(j)) minDist(j) = d
                }
                j += 1
            }
        }

        total.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost_connect_points(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        if n == 0 {
            return 0;
        }
        let mut visited = vec![false; n];
        let mut min_dist = vec![i32::MAX; n];
        min_dist[0] = 0;
        let mut total: i64 = 0;

        for _ in 0..n {
            // select the unvisited node with smallest distance
            let mut u = usize::MAX;
            let mut best = i32::MAX;
            for i in 0..n {
                if !visited[i] && min_dist[i] < best {
                    best = min_dist[i];
                    u = i;
                }
            }

            visited[u] = true;
            total += best as i64;

            // update distances to the newly added node
            let (ux, uy) = (points[u][0], points[u][1]);
            for v in 0..n {
                if !visited[v] {
                    let d = (ux - points[v][0]).abs() + (uy - points[v][1]).abs();
                    if d < min_dist[v] {
                        min_dist[v] = d;
                    }
                }
            }
        }

        total as i32
    }
}
```

## Racket

```racket
(define/contract (min-cost-connect-points points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([n (length points)]
         [pts (list->vector points)]
         [visited (make-vector n #f)]
         [INF (expt 2 60)]
         [dist (make-vector n INF)])
    (vector-set! dist 0 0)
    (let loop ((i 0) (total 0))
      (if (= i n)
          total
          (let* ([u (let find-min ((idx 0) (best -1) (bestd INF))
                     (cond [(= idx n) best]
                           [(and (not (vector-ref visited idx))
                                 (< (vector-ref dist idx) bestd))
                            (find-min (+ idx 1) idx (vector-ref dist idx))]
                           [else
                            (find-min (+ idx 1) best bestd)]))])
            (vector-set! visited u #t)
            (let* ([total2 (+ total (vector-ref dist u))])
              ;; update distances to unvisited vertices
              (let inner ((v 0))
                (when (< v n)
                  (unless (vector-ref visited v)
                    (let* ([pu (vector-ref pts u)]
                           [pv (vector-ref pts v)]
                           [d (+ (abs (- (first pu) (first pv)))
                                 (abs (- (second pu) (second pv))))])
                      (when (< d (vector-ref dist v))
                        (vector-set! dist v d))))
                  (inner (+ v 1))))
              (loop (+ i 1) total2)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_cost_connect_points/1]).

-spec min_cost_connect_points(Points :: [[integer()]]) -> integer().
min_cost_connect_points(Points) ->
    N = length(Points),
    Visited0 = lists:duplicate(N, false),
    MaxInt = 1 bsl 30,
    MinDist0 = [0 | lists:duplicate(N-1, MaxInt)],
    prim(Points, Visited0, MinDist0, N, 0).

%% Prim's algorithm recursion
prim(_Points, _Visited, _MinDist, 0, Acc) ->
    Acc;
prim(Points, Visited, MinDist, Rem, Acc) ->
    {Idx, MinVal} = find_min(MinDist, Visited, 1, {undefined, 1 bsl 30}),
    NewAcc = Acc + MinVal,
    NewVisited = set_nth(Idx, true, Visited),
    UpdatedMinDist = update_dist(Idx, Points, NewVisited, MinDist, 1),
    prim(Points, NewVisited, UpdatedMinDist, Rem - 1, NewAcc).

%% Find the unvisited node with smallest distance
find_min([], [], _Idx, Acc) ->
    Acc;
find_min([Dist|Ds], [Vis|Vs], Idx, {BestIdx, BestVal}) ->
    case Vis of
        true ->
            find_min(Ds, Vs, Idx + 1, {BestIdx, BestVal});
        false ->
            NewAcc = if Dist < BestVal -> {Idx, Dist};
                        true          -> {BestIdx, BestVal}
                     end,
            find_min(Ds, Vs, Idx + 1, NewAcc)
    end.

%% Update min distances after adding node Idx
update_dist(_CurIdx, _Points, [], [], _Idx) ->
    [];
update_dist(CurIdx, Points, [Vis|VisRest], [OldDist|DistRest], Idx) ->
    case Vis of
        true when CurIdx =:= Idx ->
            % already visited (the node just added)
            Rest = update_dist(CurIdx, Points, VisRest, DistRest, Idx + 1),
            [OldDist | Rest];
        true ->
            Rest = update_dist(CurIdx, Points, VisRest, DistRest, Idx + 1),
            [OldDist | Rest];
        false ->
            Pcur = nth(CurIdx, Points),
            Pj   = nth(Idx, Points),
            D = manhattan(Pcur, Pj),
            NewDist = if D < OldDist -> D; true -> OldDist end,
            Rest = update_dist(CurIdx, Points, VisRest, DistRest, Idx + 1),
            [NewDist | Rest]
    end.

%% Replace N-th element (1‑based) in list
set_nth(1, Val, [_|T]) ->
    [Val|T];
set_nth(N, Val, [H|T]) when N > 1 ->
    [H|set_nth(N-1, Val, T)].

%% Manhattan distance between two points
manhattan([X1,Y1], [X2,Y2]) ->
    abs(X1 - X2) + abs(Y1 - Y2).

abs(N) when N >= 0 -> N;
abs(N) -> -N.

%% Retrieve N-th element (1‑based)
nth(1, [H|_]) -> H;
nth(N, [_|T]) when N > 1 -> nth(N-1, T).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost_connect_points(points :: [[integer]]) :: integer
  def min_cost_connect_points(points) do
    n = length(points)
    max_val = 1_000_000_000

    dist = List.duplicate(max_val, n) |> List.replace_at(0, 0)
    visited = List.duplicate(false, n)

    {total, _dist, _visited} =
      Enum.reduce(1..n, {0, dist, visited}, fn _, {total_acc, dist_acc, visited_acc} ->
        {u_idx, u_dist} = find_min(dist_acc, visited_acc)
        total_new = total_acc + u_dist
        visited_new = List.replace_at(visited_acc, u_idx, true)

        point_u = Enum.at(points, u_idx)

        dist_updated =
          Enum.with_index(points)
          |> Enum.reduce(dist_acc, fn {point_j, j}, dacc ->
            if not Enum.at(visited_new, j) do
              w = manhattan(point_u, point_j)

              if w < Enum.at(dacc, j) do
                List.replace_at(dacc, j, w)
              else
                dacc
              end
            else
              dacc
            end
          end)

        {total_new, dist_updated, visited_new}
      end)

    total
  end

  defp find_min(dist, visited) do
    Enum.with_index(dist)
    |> Enum.reduce({-1, 1_000_000_000}, fn {d, idx}, {min_idx, min_val} ->
      if not Enum.at(visited, idx) and d < min_val do
        {idx, d}
      else
        {min_idx, min_val}
      end
    end)
  end

  defp manhattan([x1, y1], [x2, y2]) do
    Kernel.abs(x1 - x2) + Kernel.abs(y1 - y2)
  end
end
```

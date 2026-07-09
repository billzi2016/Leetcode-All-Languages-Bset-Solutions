# 2359. Find Closest Node to Given Two Nodes

## Cpp

```cpp
class Solution {
public:
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        int n = edges.size();
        vector<int> dist1(n, -1), dist2(n, -1);
        
        auto fillDist = [&](int start, vector<int>& dist) {
            int cur = start;
            int d = 0;
            while (cur != -1 && dist[cur] == -1) {
                dist[cur] = d++;
                cur = edges[cur];
            }
        };
        
        fillDist(node1, dist1);
        fillDist(node2, dist2);
        
        int ans = -1;
        int best = INT_MAX;
        for (int i = 0; i < n; ++i) {
            if (dist1[i] != -1 && dist2[i] != -1) {
                int curMax = max(dist1[i], dist2[i]);
                if (curMax < best) {
                    best = curMax;
                    ans = i;
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int closestMeetingNode(int[] edges, int node1, int node2) {
        int n = edges.length;
        int[] dist1 = getDistances(edges, node1);
        int[] dist2 = getDistances(edges, node2);
        int bestNode = -1;
        int bestDist = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (dist1[i] == -1 || dist2[i] == -1) continue;
            int curMax = Math.max(dist1[i], dist2[i]);
            if (curMax < bestDist || (curMax == bestDist && i < bestNode)) {
                bestDist = curMax;
                bestNode = i;
            }
        }
        return bestNode;
    }

    private int[] getDistances(int[] edges, int start) {
        int n = edges.length;
        int[] dist = new int[n];
        java.util.Arrays.fill(dist, -1);
        int steps = 0;
        int node = start;
        while (node != -1 && dist[node] == -1) {
            dist[node] = steps++;
            node = edges[node];
        }
        return dist;
    }
}
```

## Python

```python
class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        n = len(edges)
        INF = float('inf')
        
        def get_dist(start):
            dist = [INF] * n
            steps = 0
            cur = start
            while cur != -1 and dist[cur] == INF:
                dist[cur] = steps
                steps += 1
                cur = edges[cur]
            return dist
        
        d1 = get_dist(node1)
        d2 = get_dist(node2)
        
        best_node = -1
        best_val = INF
        for i in range(n):
            cur_max = max(d1[i], d2[i])
            if cur_max < best_val:
                best_val = cur_max
                best_node = i
        return best_node
```

## Python3

```python
from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def get_dist(start: int) -> List[int]:
            dist = [-1] * n
            cur = start
            d = 0
            while cur != -1 and dist[cur] == -1:
                dist[cur] = d
                cur = edges[cur]
                d += 1
            return dist

        dist1 = get_dist(node1)
        dist2 = get_dist(node2)

        best_node = -1
        best_max = float('inf')
        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                cur_max = max(dist1[i], dist2[i])
                if cur_max < best_max or (cur_max == best_max and i < best_node):
                    best_max = cur_max
                    best_node = i

        return best_node
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int* computeDist(int *edges, int n, int start) {
    int *dist = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i) dist[i] = -1;
    int cur = start, d = 0;
    while (cur != -1 && dist[cur] == -1) {
        dist[cur] = d;
        cur = edges[cur];
        ++d;
    }
    return dist;
}

int closestMeetingNode(int* edges, int edgesSize, int node1, int node2) {
    int *dist1 = computeDist(edges, edgesSize, node1);
    int *dist2 = computeDist(edges, edgesSize, node2);
    int answer = -1;
    int best = INT_MAX;
    for (int i = 0; i < edgesSize; ++i) {
        if (dist1[i] != -1 && dist2[i] != -1) {
            int curMax = dist1[i] > dist2[i] ? dist1[i] : dist2[i];
            if (curMax < best || (curMax == best && i < answer)) {
                best = curMax;
                answer = i;
            }
        }
    }
    free(dist1);
    free(dist2);
    return answer;
}
```

## Csharp

```csharp
public class Solution
{
    public int ClosestMeetingNode(int[] edges, int node1, int node2)
    {
        int n = edges.Length;
        const int INF = int.MaxValue;

        int[] dist1 = new int[n];
        int[] dist2 = new int[n];
        for (int i = 0; i < n; i++)
        {
            dist1[i] = INF;
            dist2[i] = INF;
        }

        FillDist(edges, node1, dist1);
        FillDist(edges, node2, dist2);

        int bestNode = -1;
        int bestDist = INF;

        for (int i = 0; i < n; i++)
        {
            if (dist1[i] == INF || dist2[i] == INF) continue;
            int cur = Math.Max(dist1[i], dist2[i]);
            if (cur < bestDist)
            {
                bestDist = cur;
                bestNode = i;
            }
        }

        return bestNode;
    }

    private void FillDist(int[] edges, int start, int[] dist)
    {
        int cur = start;
        int d = 0;
        while (cur != -1 && dist[cur] == int.MaxValue)
        {
            dist[cur] = d;
            cur = edges[cur];
            d++;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} edges
 * @param {number} node1
 * @param {number} node2
 * @return {number}
 */
var closestMeetingNode = function(edges, node1, node2) {
    const n = edges.length;
    const INF = Number.MAX_SAFE_INTEGER;
    const dist1 = new Array(n).fill(INF);
    const dist2 = new Array(n).fill(INF);
    
    const computeDist = (start, distArr) => {
        let cur = start;
        let d = 0;
        while (cur !== -1 && distArr[cur] === INF) {
            distArr[cur] = d;
            cur = edges[cur];
            d++;
        }
    };
    
    computeDist(node1, dist1);
    computeDist(node2, dist2);
    
    let answer = -1;
    let best = INF;
    for (let i = 0; i < n; i++) {
        if (dist1[i] === INF || dist2[i] === INF) continue;
        const curMax = Math.max(dist1[i], dist2[i]);
        if (curMax < best) {
            best = curMax;
            answer = i;
        }
    }
    
    return answer;
};
```

## Typescript

```typescript
function closestMeetingNode(edges: number[], node1: number, node2: number): number {
    const n = edges.length;
    const dist1 = new Array<number>(n).fill(Infinity);
    const dist2 = new Array<number>(n).fill(Infinity);

    const fillDist = (start: number, dist: number[]) => {
        let cur = start;
        let d = 0;
        while (cur !== -1 && dist[cur] === Infinity) {
            dist[cur] = d;
            cur = edges[cur];
            d++;
        }
    };

    fillDist(node1, dist1);
    fillDist(node2, dist2);

    let answer = -1;
    let best = Infinity;

    for (let i = 0; i < n; i++) {
        const maxDist = Math.max(dist1[i], dist2[i]);
        if (maxDist < best) {
            best = maxDist;
            answer = i;
        }
    }

    return answer;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $edges
     * @param Integer $node1
     * @param Integer $node2
     * @return Integer
     */
    function closestMeetingNode($edges, $node1, $node2) {
        $dist1 = $this->computeDist($node1, $edges);
        $dist2 = $this->computeDist($node2, $edges);
        
        $n = count($edges);
        $INF = PHP_INT_MAX;
        $bestMax = $INF;
        $answer = -1;
        
        for ($i = 0; $i < $n; $i++) {
            if ($dist1[$i] === $INF || $dist2[$i] === $INF) {
                continue;
            }
            $curMax = max($dist1[$i], $dist2[$i]);
            if ($curMax < $bestMax) {
                $bestMax = $curMax;
                $answer = $i;
            } elseif ($curMax == $bestMax && $i < $answer) {
                $answer = $i;
            }
        }
        
        return $answer;
    }
    
    private function computeDist($start, $edges) {
        $n = count($edges);
        $INF = PHP_INT_MAX;
        $dist = array_fill(0, $n, $INF);
        $node = $start;
        $d = 0;
        while ($node != -1 && $dist[$node] === $INF) {
            $dist[$node] = $d;
            $node = $edges[$node];
            $d++;
        }
        return $dist;
    }
}
```

## Swift

```swift
class Solution {
    func closestMeetingNode(_ edges: [Int], _ node1: Int, _ node2: Int) -> Int {
        let n = edges.count
        var dist1 = Array(repeating: Int.max, count: n)
        var dist2 = Array(repeating: Int.max, count: n)

        func fillDist(_ start: Int, _ dist: inout [Int]) {
            var cur = start
            var d = 0
            while cur != -1 && dist[cur] == Int.max {
                dist[cur] = d
                cur = edges[cur]
                d += 1
            }
        }

        fillDist(node1, &dist1)
        fillDist(node2, &dist2)

        var answer = -1
        var best = Int.max

        for i in 0..<n {
            let a = dist1[i]
            let b = dist2[i]
            if a == Int.max || b == Int.max { continue }
            let curMax = max(a, b)
            if curMax < best || (curMax == best && i < answer) {
                best = curMax
                answer = i
            }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun closestMeetingNode(edges: IntArray, node1: Int, node2: Int): Int {
        val n = edges.size

        fun getDist(start: Int): IntArray {
            val dist = IntArray(n) { -1 }
            var cur = start
            var d = 0
            while (cur != -1 && dist[cur] == -1) {
                dist[cur] = d
                cur = edges[cur]
                d++
            }
            return dist
        }

        val dist1 = getDist(node1)
        val dist2 = getDist(node2)

        var answer = -1
        var best = Int.MAX_VALUE

        for (i in 0 until n) {
            if (dist1[i] != -1 && dist2[i] != -1) {
                val curMax = kotlin.math.max(dist1[i], dist2[i])
                if (curMax < best || (curMax == best && i < answer)) {
                    best = curMax
                    answer = i
                }
            }
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  int closestMeetingNode(List<int> edges, int node1, int node2) {
    int n = edges.length;
    List<int> dist1 = List.filled(n, -1);
    List<int> dist2 = List.filled(n, -1);

    void fillDist(int start, List<int> dist) {
      int cur = start;
      int d = 0;
      while (cur != -1 && dist[cur] == -1) {
        dist[cur] = d;
        cur = edges[cur];
        d++;
      }
    }

    fillDist(node1, dist1);
    fillDist(node2, dist2);

    int answer = -1;
    int bestMax = 1 << 30; // large sentinel

    for (int i = 0; i < n; i++) {
      if (dist1[i] != -1 && dist2[i] != -1) {
        int curMax = dist1[i] > dist2[i] ? dist1[i] : dist2[i];
        if (curMax < bestMax || (curMax == bestMax && i < answer)) {
          bestMax = curMax;
          answer = i;
        }
      }
    }

    return answer;
  }
}
```

## Golang

```go
func closestMeetingNode(edges []int, node1 int, node2 int) int {
    n := len(edges)
    const INF = int(1e9)

    dist1 := make([]int, n)
    dist2 := make([]int, n)
    for i := 0; i < n; i++ {
        dist1[i] = INF
        dist2[i] = INF
    }

    walk := func(start int, dist []int) {
        steps := 0
        cur := start
        for cur != -1 && dist[cur] == INF {
            dist[cur] = steps
            cur = edges[cur]
            steps++
        }
    }

    walk(node1, dist1)
    walk(node2, dist2)

    ans := -1
    best := INF
    for i := 0; i < n; i++ {
        if dist1[i] == INF || dist2[i] == INF {
            continue
        }
        maxd := dist1[i]
        if dist2[i] > maxd {
            maxd = dist2[i]
        }
        if maxd < best {
            best = maxd
            ans = i
        }
    }
    return ans
}
```

## Ruby

```ruby
def closest_meeting_node(edges, node1, node2)
  n = edges.length
  inf = Float::INFINITY

  get_dist = lambda do |start|
    dist = Array.new(n, inf)
    cur = start
    d = 0
    while cur != -1 && dist[cur] == inf
      dist[cur] = d
      cur = edges[cur]
      d += 1
    end
    dist
  end

  dist1 = get_dist.call(node1)
  dist2 = get_dist.call(node2)

  best_node = -1
  best_max = inf

  (0...n).each do |i|
    max_d = [dist1[i], dist2[i]].max
    next if max_d == inf
    if max_d < best_max
      best_max = max_d
      best_node = i
    end
  end

  best_node
end
```

## Scala

```scala
object Solution {
    def closestMeetingNode(edges: Array[Int], node1: Int, node2: Int): Int = {
        val n = edges.length

        def getDist(start: Int): Array[Int] = {
            val dist = Array.fill(n)(-1)
            var cur = start
            var d = 0
            while (cur != -1 && dist(cur) == -1) {
                dist(cur) = d
                cur = edges(cur)
                d += 1
            }
            dist
        }

        val dist1 = getDist(node1)
        val dist2 = getDist(node2)

        var answer = -1
        var best = Int.MaxValue

        for (i <- 0 until n) {
            if (dist1(i) != -1 && dist2(i) != -1) {
                val curMax = math.max(dist1(i), dist2(i))
                if (curMax < best || (curMax == best && i < answer)) {
                    best = curMax
                    answer = i
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
    pub fn closest_meeting_node(edges: Vec<i32>, node1: i32, node2: i32) -> i32 {
        let n = edges.len();
        let mut dist1 = vec![-1; n];
        let mut dist2 = vec![-1; n];

        Self::fill_dist(node1 as usize, &edges, &mut dist1);
        Self::fill_dist(node2 as usize, &edges, &mut dist2);

        let mut answer = -1;
        let mut best = i32::MAX;

        for i in 0..n {
            if dist1[i] != -1 && dist2[i] != -1 {
                let cur = std::cmp::max(dist1[i], dist2[i]);
                if cur < best || (cur == best && (i as i32) < answer) {
                    best = cur;
                    answer = i as i32;
                }
            }
        }

        answer
    }

    fn fill_dist(start: usize, edges: &Vec<i32>, dist: &mut Vec<i32>) {
        let mut cur = start;
        let mut d = 0i32;
        loop {
            if dist[cur] != -1 {
                break;
            }
            dist[cur] = d;
            let next = edges[cur];
            if next == -1 {
                break;
            }
            cur = next as usize;
            d += 1;
        }
    }
}
```

## Racket

```racket
(define (compute-dist v start)
  (let* ((n (vector-length v))
         (dist (make-vector n -1)))
    (let loop ((cur start) (d 0))
      (when (and (>= cur 0) (< cur n) (= (vector-ref dist cur) -1))
        (vector-set! dist cur d)
        (let ((next (vector-ref v cur)))
          (if (or (= next -1) (not (>= next 0)) (>= next n))
              (void)
              (loop next (+ d 1))))))
    dist))

(define/contract (closest-meeting-node edges node1 node2)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((v (list->vector edges))
         (n (vector-length v))
         (dist1 (compute-dist v node1))
         (dist2 (compute-dist v node2)))
    (let loop ((i 0) (best -1) (bestmax (+ n 1)))
      (if (= i n)
          best
          (let* ((d1 (vector-ref dist1 i))
                 (d2 (vector-ref dist2 i)))
            (if (and (>= d1 0) (>= d2 0))
                (let ((m (max d1 d2)))
                  (cond [(or (< m bestmax)
                             (and (= m bestmax) (< i best)))
                         (loop (+ i 1) i m)]
                        [else
                         (loop (+ i 1) best bestmax)]))
                (loop (+ i 1) best bestmax)))))))
```

## Erlang

```erlang
-spec closest_meeting_node(Edges :: [integer()], Node1 :: integer(), Node2 :: integer()) -> integer().
closest_meeting_node(Edges, Node1, Node2) ->
    EdgesTuple = list_to_tuple(Edges),
    Dist1 = bfs_dist(Node1, EdgesTuple),
    Dist2 = bfs_dist(Node2, EdgesTuple),
    N = tuple_size(EdgesTuple),
    find_best(N - 1, Dist1, Dist2, -1, N + 1).

bfs_dist(Start, EdgesTuple) ->
    bfs_loop(Start, EdgesTuple, 0, #{}).

bfs_loop(-1, _EdgesTuple, _Dist, Map) ->
    Map;
bfs_loop(Curr, EdgesTuple, D, Map) ->
    case maps:is_key(Curr, Map) of
        true -> Map; % already visited (cycle)
        false ->
            NewMap = maps:put(Curr, D, Map),
            Next = element(Curr + 1, EdgesTuple), % tuple is 1‑based
            bfs_loop(Next, EdgesTuple, D + 1, NewMap)
    end.

find_best(Index, _Dist1, _Dist2, BestNode, _BestDist) when Index < 0 ->
    BestNode;
find_best(Index, Dist1, Dist2, BestNode, BestDist) ->
    case {maps:find(Index, Dist1), maps:find(Index, Dist2)} of
        {{ok, D1}, {ok, D2}} ->
            MaxD = if D1 > D2 -> D1; true -> D2 end,
            if MaxD < BestDist orelse (MaxD == BestDist andalso Index < BestNode) ->
                    find_best(Index - 1, Dist1, Dist2, Index, MaxD);
               true ->
                    find_best(Index - 1, Dist1, Dist2, BestNode, BestDist)
            end;
        _ ->
            find_best(Index - 1, Dist1, Dist2, BestNode, BestDist)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec closest_meeting_node(edges :: [integer], node1 :: integer, node2 :: integer) :: integer
  def closest_meeting_node(edges, node1, node2) do
    edges_t = List.to_tuple(edges)

    d1 = distances(edges_t, node1)
    d2 = distances(edges_t, node2)

    n = tuple_size(edges_t)

    {ans, _} =
      Enum.reduce(0..(n - 1), {-1, :infinity}, fn i, {cur_ans, cur_best} ->
        d1i = Map.get(d1, i, -1)
        d2i = Map.get(d2, i, -1)

        if d1i != -1 and d2i != -1 do
          maxd = max(d1i, d2i)

          cond do
            maxd < cur_best ->
              {i, maxd}

            maxd == cur_best and (cur_ans == -1 or i < cur_ans) ->
              {i, cur_best}

            true ->
              {cur_ans, cur_best}
          end
        else
          {cur_ans, cur_best}
        end
      end)

    ans
  end

  defp distances(edges_t, start), do: bfs(edges_t, start, 0, %{})

  defp bfs(_edges_t, -1, _step, dist), do: dist

  defp bfs(edges_t, cur, step, dist) do
    if Map.has_key?(dist, cur) do
      dist
    else
      next = elem(edges_t, cur)
      bfs(edges_t, next, step + 1, Map.put(dist, cur, step))
    end
  end
end
```

# 2360. Longest Cycle in a Graph

## Cpp

```cpp
class Solution {
public:
    int longestCycle(vector<int>& edges) {
        int n = edges.size();
        vector<int> state(n, 0); // 0=unvisited,1=visiting,2=done
        vector<int> depth(n, 0);
        int ans = -1;
        for (int i = 0; i < n; ++i) {
            if (state[i] != 0) continue;
            int cur = i;
            vector<int> path;
            while (cur != -1 && state[cur] == 0) {
                state[cur] = 1;
                depth[cur] = path.size();
                path.push_back(cur);
                cur = edges[cur];
            }
            if (cur != -1 && state[cur] == 1) {
                int cycle_len = (int)path.size() - depth[cur];
                ans = max(ans, cycle_len);
            }
            for (int node : path) state[node] = 2;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestCycle(int[] edges) {
        int n = edges.length;
        int[] visitTime = new int[n];
        boolean[] processed = new boolean[n];
        java.util.Arrays.fill(visitTime, -1);
        int maxLen = -1;

        for (int i = 0; i < n; i++) {
            if (processed[i]) continue;

            int cur = i;
            int step = 0;
            // traverse forward marking visit times
            while (cur != -1 && !processed[cur]) {
                if (visitTime[cur] != -1) { // found a cycle within current traversal
                    int cycleLen = step - visitTime[cur];
                    if (cycleLen > maxLen) maxLen = cycleLen;
                    break;
                }
                visitTime[cur] = step++;
                cur = edges[cur];
            }

            // clean up: mark all nodes visited in this traversal as processed and reset visitTime
            cur = i;
            while (cur != -1 && !processed[cur]) {
                int next = edges[cur];
                processed[cur] = true;
                visitTime[cur] = -1;
                cur = next;
            }
        }

        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        n = len(edges)
        visited_global = [False] * n
        ans = -1

        for i in range(n):
            if visited_global[i]:
                continue
            cur = i
            step = 0
            local_index = {}
            while cur != -1 and not visited_global[cur]:
                if cur in local_index:
                    cycle_len = step - local_index[cur]
                    if cycle_len > ans:
                        ans = cycle_len
                    break
                local_index[cur] = step
                step += 1
                cur = edges[cur]
            for node in local_index:
                visited_global[node] = True

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n
        answer = -1

        for i in range(n):
            if visited[i]:
                continue
            cur = i
            step = 0
            index_in_path = {}
            while cur != -1 and not visited[cur]:
                index_in_path[cur] = step
                step += 1
                nxt = edges[cur]
                if nxt in index_in_path:
                    cycle_len = step - index_in_path[nxt]
                    answer = max(answer, cycle_len)
                    break
                cur = nxt
            for node in index_in_path:
                visited[node] = True

        return answer
```

## C

```c
#include <stdlib.h>

int longestCycle(int* edges, int edgesSize) {
    int *visitMark = (int*)calloc(edgesSize, sizeof(int));
    int *stepAt   = (int*)calloc(edgesSize, sizeof(int));
    int ans = -1;

    for (int i = 0; i < edgesSize; ++i) {
        if (visitMark[i] != 0) continue;          // already processed
        int marker = i + 1;                       // unique id for this traversal
        int cur = i;
        int step = 1;

        while (cur != -1) {
            if (visitMark[cur] == marker) {       // found a cycle in current path
                int len = step - stepAt[cur];
                if (len > ans) ans = len;
                break;
            }
            if (visitMark[cur] != 0 && visitMark[cur] != marker) {
                // node visited in another traversal, no new cycle here
                break;
            }
            visitMark[cur] = marker;
            stepAt[cur] = step;
            ++step;
            cur = edges[cur];
        }
    }

    free(visitMark);
    free(stepAt);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestCycle(int[] edges) {
        int n = edges.Length;
        int[] visitId = new int[n];
        int[] depth = new int[n];
        int maxLen = -1;

        for (int i = 0; i < n; i++) {
            if (visitId[i] != 0) continue;
            int cur = i;
            int step = 0;
            while (cur != -1 && visitId[cur] == 0) {
                visitId[cur] = i + 1; // unique identifier for this traversal
                depth[cur] = step++;
                cur = edges[cur];
            }
            if (cur != -1 && visitId[cur] == i + 1) {
                int cycleLen = step - depth[cur];
                if (cycleLen > maxLen) maxLen = cycleLen;
            }
        }

        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} edges
 * @return {number}
 */
var longestCycle = function(edges) {
    const n = edges.length;
    const visited = new Array(n).fill(0); // traversal identifier
    const depth = new Array(n).fill(0);
    let ans = -1;
    let curId = 1;

    for (let i = 0; i < n; i++) {
        if (visited[i] !== 0) continue;
        let node = i;
        let step = 0;
        while (node !== -1 && visited[node] === 0) {
            visited[node] = curId;
            depth[node] = step;
            node = edges[node];
            step++;
        }
        if (node !== -1 && visited[node] === curId) {
            const len = step - depth[node];
            if (len > ans) ans = len;
        }
        curId++;
    }

    return ans;
};
```

## Typescript

```typescript
function longestCycle(edges: number[]): number {
    const n = edges.length;
    const done = new Array<boolean>(n).fill(false);
    const idx = new Array<number>(n).fill(-1);
    let maxLen = -1;

    for (let i = 0; i < n; i++) {
        if (done[i]) continue;
        let cur = i;
        const path: number[] = [];
        while (cur !== -1 && !done[cur]) {
            if (idx[cur] !== -1) {
                const cycleLen = path.length - idx[cur];
                if (cycleLen > maxLen) maxLen = cycleLen;
                break;
            }
            idx[cur] = path.length;
            path.push(cur);
            cur = edges[cur];
        }
        for (const node of path) {
            done[node] = true;
            idx[node] = -1;
        }
    }

    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $edges
     * @return Integer
     */
    function longestCycle($edges) {
        $n = count($edges);
        $vis = array_fill(0, $n, -1);   // traversal identifier for each node
        $depth = array_fill(0, $n, 0);  // step index within its traversal
        $maxLen = -1;

        for ($i = 0; $i < $n; $i++) {
            if ($vis[$i] != -1) {
                continue;
            }
            $cur = $i;
            $step = 0;
            while ($cur != -1 && $vis[$cur] == -1) {
                $vis[$cur] = $i;      // mark with current start node as identifier
                $depth[$cur] = $step;
                $step++;
                $cur = $edges[$cur];
            }
            if ($cur != -1 && $vis[$cur] == $i) { // found a cycle in this traversal
                $cycleLen = $step - $depth[$cur];
                if ($cycleLen > $maxLen) {
                    $maxLen = $cycleLen;
                }
            }
        }

        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func longestCycle(_ edges: [Int]) -> Int {
        let n = edges.count
        var visited = [Bool](repeating: false, count: n)
        var maxLen = -1

        for i in 0..<n {
            if visited[i] { continue }
            var node = i
            var step = 0
            var indexMap = [Int:Int]()   // node -> step order within this traversal

            while node != -1 && !visited[node] {
                visited[node] = true
                indexMap[node] = step
                step += 1

                let next = edges[node]
                if next == -1 { break }

                if let prevStep = indexMap[next] {
                    maxLen = max(maxLen, step - prevStep)
                    break
                }
                node = next
            }
        }

        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestCycle(edges: IntArray): Int {
        val n = edges.size
        val visited = BooleanArray(n)
        var answer = -1

        for (i in 0 until n) {
            if (!visited[i]) {
                var cur = i
                val stepMap = HashMap<Int, Int>()
                var step = 0
                while (cur != -1 && !visited[cur]) {
                    visited[cur] = true
                    stepMap[cur] = step
                    step++
                    cur = edges[cur]
                }
                if (cur != -1) {
                    val startIdx = stepMap[cur]
                    if (startIdx != null) {
                        answer = maxOf(answer, step - startIdx)
                    }
                }
            }
        }

        return answer
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int longestCycle(List<int> edges) {
    int n = edges.length;
    const int unvisited = -2;
    List<int> visitedFrom = List.filled(n, unvisited);
    List<int> depth = List.filled(n, 0);
    int ans = -1;

    for (int i = 0; i < n; ++i) {
      if (visitedFrom[i] != unvisited) continue;
      int cur = i;
      int step = 0;
      while (cur != -1 && visitedFrom[cur] == unvisited) {
        visitedFrom[cur] = i;
        depth[cur] = step;
        step++;
        cur = edges[cur];
      }
      if (cur != -1 && visitedFrom[cur] == i) {
        ans = max(ans, step - depth[cur]);
      }
    }

    return ans;
  }
}
```

## Golang

```go
func longestCycle(edges []int) int {
    n := len(edges)
    visited := make([]bool, n)
    depth := make([]int, n)
    visitMark := make([]int, n)

    ans := -1
    curMark := 1

    for i := 0; i < n; i++ {
        if visited[i] {
            continue
        }
        cur := i
        steps := 0
        for cur != -1 && !visited[cur] {
            visited[cur] = true
            visitMark[cur] = curMark
            depth[cur] = steps
            steps++
            cur = edges[cur]
        }
        if cur != -1 && visitMark[cur] == curMark {
            cycleLen := steps - depth[cur]
            if cycleLen > ans {
                ans = cycleLen
            }
        }
        curMark++
    }

    return ans
}
```

## Ruby

```ruby
def longest_cycle(edges)
  n = edges.length
  visited = Array.new(n, 0)   # 0 means not visited in any traversal
  depth = Array.new(n, 0)     # step index within current traversal
  mark = 1
  max_len = -1

  (0...n).each do |i|
    next if visited[i] != 0

    cur = i
    step = 0
    while cur != -1 && visited[cur] == 0
      visited[cur] = mark
      depth[cur] = step
      step += 1
      cur = edges[cur]
    end

    if cur != -1 && visited[cur] == mark
      cycle_len = step - depth[cur]
      max_len = [max_len, cycle_len].max
    end

    mark += 1
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def longestCycle(edges: Array[Int]): Int = {
        val n = edges.length
        val processed = new Array[Boolean](n)
        val visitId = new Array[Int](n)
        val depth = new Array[Int](n)

        var maxLen = -1
        var curId = 1

        for (i <- 0 until n) {
            if (!processed(i)) {
                var node = i
                var step = 0
                while (node != -1 && !processed(node)) {
                    visitId(node) = curId
                    depth(node) = step
                    step += 1
                    node = edges(node)
                }
                if (node != -1 && visitId(node) == curId) {
                    val cycleLen = step - depth(node)
                    if (cycleLen > maxLen) maxLen = cycleLen
                }
                var markNode = i
                while (markNode != -1 && !processed(markNode)) {
                    processed(markNode) = true
                    markNode = edges(markNode)
                }
                curId += 1
            }
        }

        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_cycle(edges: Vec<i32>) -> i32 {
        let n = edges.len();
        let mut visited = vec![false; n];
        let mut mark = vec![0i32; n];
        let mut depth = vec![0i32; n];
        let mut cur_mark: i32 = 1;
        let mut ans: i32 = -1;

        for i in 0..n {
            if visited[i] {
                continue;
            }
            let mut cur = i as i32;
            let mut step: i32 = 0;
            let mut path: Vec<usize> = Vec::new();

            loop {
                if cur == -1 {
                    break;
                }
                let u = cur as usize;
                if visited[u] {
                    break;
                }
                if mark[u] == cur_mark {
                    let cycle_len = step - depth[u];
                    if cycle_len > ans {
                        ans = cycle_len;
                    }
                    break;
                }
                mark[u] = cur_mark;
                depth[u] = step;
                path.push(u);
                step += 1;
                cur = edges[u];
            }

            for v in path {
                visited[v] = true;
            }
            cur_mark += 1;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (longest-cycle edges)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector edges))
         (n (vector-length v))
         (mark (make-vector n 0))   ; 0 = unvisited, otherwise traversal id (= start index + 1)
         (step (make-vector n 0))   ; step number within current traversal
         (ans -1))
    (for ([i (in-range n)])
      (when (= (vector-ref mark i) 0)
        (let loop ((cur i) (cnt 1))
          (if (or (< cur 0) (>= cur n))
              (void) ; reached a dead end
              (let ((m (vector-ref mark cur)))
                (cond
                  [(= m 0)
                   (vector-set! mark cur (+ i 1))
                   (vector-set! step cur cnt)
                   (loop (vector-ref v cur) (+ cnt 1))]
                  [(= m (+ i 1)) ; found a cycle in this traversal
                   (let ((cycle-len (- cnt (vector-ref step cur))))
                     (when (> cycle-len ans) (set! ans cycle-len)))
                   (void)]
                  [else ; visited in another traversal, stop
                   (void)]))))))
    ans)))
```

## Erlang

```erlang
-module(solution).
-export([longest_cycle/1]).

-spec longest_cycle(Edges :: [integer()]) -> integer().
longest_cycle(Edges) ->
    EdgesT = list_to_tuple(Edges),
    N = tuple_size(EdgesT),
    loop_nodes(0, N, EdgesT, #{}, -1).

loop_nodes(Index, N, _EdgesT, Visited, Max) when Index >= N ->
    Max;
loop_nodes(Index, N, EdgesT, Visited, Max) ->
    case maps:is_key(Index, Visited) of
        true ->
            loop_nodes(Index + 1, N, EdgesT, Visited, Max);
        false ->
            {Visited2, CycleLen} = explore(Index, EdgesT, #{}, Visited, 0, -1),
            NewMax = erlang:max(Max, CycleLen),
            loop_nodes(Index + 1, N, EdgesT, Visited2, NewMax)
    end.

explore(Node, _EdgesT, PathMap, Visited, _Step, CurrentMax) when Node == -1 ->
    {add_path_to_visited(PathMap, Visited), CurrentMax};
explore(Node, _EdgesT, PathMap, Visited, _Step, CurrentMax) when maps:is_key(Node, Visited) ->
    {add_path_to_visited(PathMap, Visited), CurrentMax};
explore(Node, _EdgesT, PathMap, Visited, Step, CurrentMax) when maps:is_key(Node, PathMap) ->
    CycleLen = Step - maps:get(Node, PathMap),
    NewMax = erlang:max(CycleLen, CurrentMax),
    {add_path_to_visited(PathMap, Visited), NewMax};
explore(Node, EdgesT, PathMap, Visited, Step, CurrentMax) ->
    Edge = element(Node + 1, EdgesT),
    NewPathMap = maps:put(Node, Step, PathMap),
    explore(Edge, EdgesT, NewPathMap, Visited, Step + 1, CurrentMax).

add_path_to_visited(PathMap, Visited) ->
    maps:fold(fun(K, _V, Acc) -> maps:put(K, true, Acc) end, Visited, PathMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_cycle(edges :: [integer]) :: integer
  def longest_cycle(edges) do
    n = length(edges)
    edges_t = List.to_tuple(edges)

    {_, answer} =
      Enum.reduce(0..(n - 1), {MapSet.new(), -1}, fn i, {visited, cur_max} ->
        if MapSet.member?(visited, i) do
          {visited, cur_max}
        else
          {new_visited, cycle_len} = traverse(i, edges_t, visited)
          {new_visited, max(cur_max, cycle_len)}
        end
      end)

    answer
  end

  defp traverse(start, edges_t, visited_global) do
    local_map = %{}
    path = []
    step = 0
    cur = start
    max_cycle = -1

    {local_map, path, max_cycle, _} =
      loop(cur, edges_t, visited_global, local_map, path, step, max_cycle)

    new_visited = Enum.reduce(path, visited_global, fn node, acc -> MapSet.put(acc, node) end)
    {new_visited, max_cycle}
  end

  defp loop(-1, _edges_t, _visited_global, local_map, path, _step, max_cycle) do
    {local_map, path, max_cycle, -1}
  end

  defp loop(cur, edges_t, visited_global, local_map, path, step, max_cycle) do
    cond do
      MapSet.member?(visited_global, cur) ->
        {local_map, path, max_cycle, cur}

      Map.has_key?(local_map, cur) ->
        cycle_len = step - Map.get(local_map, cur)
        new_max = if cycle_len > max_cycle, do: cycle_len, else: max_cycle
        {local_map, path, new_max, cur}

      true ->
        local_map = Map.put(local_map, cur, step)
        path = [cur | path]
        next = elem(edges_t, cur)
        loop(next, edges_t, visited_global, local_map, path, step + 1, max_cycle)
    end
  end
end
```

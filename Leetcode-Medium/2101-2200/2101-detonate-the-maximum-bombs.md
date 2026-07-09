# 2101. Detonate the Maximum Bombs

## Cpp

```cpp
class Solution {
public:
    int maximumDetonation(vector<vector<int>>& bombs) {
        int n = bombs.size();
        vector<vector<int>> adj(n);
        for (int i = 0; i < n; ++i) {
            long long xi = bombs[i][0], yi = bombs[i][1], ri = bombs[i][2];
            long long r2 = ri * ri;
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                long long dx = xi - bombs[j][0];
                long long dy = yi - bombs[j][1];
                if (dx*dx + dy*dy <= r2) {
                    adj[i].push_back(j);
                }
            }
        }
        int best = 0;
        for (int start = 0; start < n; ++start) {
            vector<char> visited(n, 0);
            stack<int> st;
            st.push(start);
            int cnt = 0;
            while (!st.empty()) {
                int u = st.top(); st.pop();
                if (visited[u]) continue;
                visited[u] = 1;
                ++cnt;
                for (int v : adj[u]) {
                    if (!visited[v]) st.push(v);
                }
            }
            best = max(best, cnt);
        }
        return best;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maximumDetonation(int[][] bombs) {
        int n = bombs.length;
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int i = 0; i < n; i++) {
            long xi = bombs[i][0];
            long yi = bombs[i][1];
            long ri = bombs[i][2];
            long r2 = ri * ri;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                long dx = xi - bombs[j][0];
                long dy = yi - bombs[j][1];
                long d2 = dx * dx + dy * dy;
                if (d2 <= r2) {
                    adj[i].add(j);
                }
            }
        }

        int maxDetonated = 0;
        for (int start = 0; start < n; start++) {
            boolean[] visited = new boolean[n];
            Deque<Integer> stack = new ArrayDeque<>();
            stack.push(start);
            visited[start] = true;
            int count = 0;

            while (!stack.isEmpty()) {
                int cur = stack.pop();
                count++;
                for (int nxt : adj[cur]) {
                    if (!visited[nxt]) {
                        visited[nxt] = true;
                        stack.push(nxt);
                    }
                }
            }

            maxDetonated = Math.max(maxDetonated, count);
        }

        return maxDetonated;
    }
}
```

## Python

```python
class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        n = len(bombs)
        # Build adjacency list: i -> j if bomb j is within range of bomb i
        adj = [[] for _ in range(n)]
        for i in range(n):
            xi, yi, ri = bombs[i]
            ri2 = ri * ri
            for j in range(n):
                if i == j:
                    continue
                xj, yj, _ = bombs[j]
                dx = xi - xj
                dy = yi - yj
                if dx*dx + dy*dy <= ri2:
                    adj[i].append(j)

        def bfs(start):
            visited = [False] * n
            stack = [start]
            visited[start] = True
            count = 0
            while stack:
                node = stack.pop()
                count += 1
                for nb in adj[node]:
                    if not visited[nb]:
                        visited[nb] = True
                        stack.append(nb)
            return count

        max_det = 0
        for i in range(n):
            max_det = max(max_det, bfs(i))
        return max_det
```

## Python3

```python
from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = [[] for _ in range(n)]
        for i in range(n):
            xi, yi, ri = bombs[i]
            r2 = ri * ri
            for j in range(n):
                if i == j:
                    continue
                xj, yj, _ = bombs[j]
                dx = xi - xj
                dy = yi - yj
                if dx * dx + dy * dy <= r2:
                    adj[i].append(j)

        def dfs(start: int) -> int:
            visited = [False] * n
            stack = [start]
            visited[start] = True
            count = 0
            while stack:
                u = stack.pop()
                count += 1
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            return count

        max_det = 0
        for i in range(n):
            max_det = max(max_det, dfs(i))
        return max_det
```

## C

```c
#include <stdbool.h>
#include <string.h>

int maximumDetonation(int** bombs, int bombsSize, int* bombsColSize) {
    int n = bombsSize;
    bool adj[100][100];
    memset(adj, 0, sizeof(adj));

    for (int i = 0; i < n; ++i) {
        long long xi = bombs[i][0];
        long long yi = bombs[i][1];
        long long ri = bombs[i][2];
        long long r2 = ri * ri;
        for (int j = 0; j < n; ++j) {
            if (i == j) continue;
            long long dx = xi - bombs[j][0];
            long long dy = yi - bombs[j][1];
            long long d2 = dx * dx + dy * dy;
            if (d2 <= r2) adj[i][j] = true;
        }
    }

    int maxCount = 0;
    for (int start = 0; start < n; ++start) {
        bool visited[100] = {false};
        int queue[100];
        int front = 0, back = 0;
        queue[back++] = start;
        visited[start] = true;
        int cnt = 0;

        while (front < back) {
            int cur = queue[front++];
            ++cnt;
            for (int nxt = 0; nxt < n; ++nxt) {
                if (adj[cur][nxt] && !visited[nxt]) {
                    visited[nxt] = true;
                    queue[back++] = nxt;
                }
            }
        }

        if (cnt > maxCount) maxCount = cnt;
    }

    return maxCount;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int MaximumDetonation(int[][] bombs) {
        int n = bombs.Length;
        var adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        
        for (int i = 0; i < n; i++) {
            long xi = bombs[i][0], yi = bombs[i][1], ri = bombs[i][2];
            long r2 = ri * ri;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                long dx = bombs[j][0] - xi;
                long dy = bombs[j][1] - yi;
                if (dx * dx + dy * dy <= r2) {
                    adj[i].Add(j);
                }
            }
        }

        int maxDet = 0;
        var stack = new Stack<int>();
        for (int i = 0; i < n; i++) {
            bool[] visited = new bool[n];
            int cnt = 0;
            stack.Clear();
            stack.Push(i);
            visited[i] = true;
            while (stack.Count > 0) {
                int cur = stack.Pop();
                cnt++;
                foreach (int nb in adj[cur]) {
                    if (!visited[nb]) {
                        visited[nb] = true;
                        stack.Push(nb);
                    }
                }
            }
            if (cnt > maxDet) maxDet = cnt;
        }

        return maxDet;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} bombs
 * @return {number}
 */
var maximumDetonation = function(bombs) {
    const n = bombs.length;
    const adj = Array.from({ length: n }, () => []);
    
    for (let i = 0; i < n; i++) {
        const [xi, yi, ri] = bombs[i];
        const r2 = ri * ri;
        for (let j = 0; j < n; j++) {
            if (i === j) continue;
            const dx = bombs[j][0] - xi;
            const dy = bombs[j][1] - yi;
            if (dx * dx + dy * dy <= r2) {
                adj[i].push(j);
            }
        }
    }
    
    let maxCount = 0;
    for (let i = 0; i < n; i++) {
        const visited = new Array(n).fill(false);
        const stack = [i];
        visited[i] = true;
        let count = 0;
        while (stack.length) {
            const node = stack.pop();
            count++;
            for (const nb of adj[node]) {
                if (!visited[nb]) {
                    visited[nb] = true;
                    stack.push(nb);
                }
            }
        }
        if (count > maxCount) maxCount = count;
    }
    
    return maxCount;
};
```

## Typescript

```typescript
function maximumDetonation(bombs: number[][]): number {
    const n = bombs.length;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (let i = 0; i < n; i++) {
        const [xi, yi, ri] = bombs[i];
        const r2 = ri * ri;
        for (let j = 0; j < n; j++) {
            if (i === j) continue;
            const dx = bombs[j][0] - xi;
            const dy = bombs[j][1] - yi;
            if (dx * dx + dy * dy <= r2) adj[i].push(j);
        }
    }

    let best = 0;
    for (let i = 0; i < n; i++) {
        const visited = new Array(n).fill(false);
        const stack: number[] = [i];
        visited[i] = true;
        let cnt = 0;
        while (stack.length) {
            const cur = stack.pop()!;
            cnt++;
            for (const nb of adj[cur]) {
                if (!visited[nb]) {
                    visited[nb] = true;
                    stack.push(nb);
                }
            }
        }
        if (cnt > best) best = cnt;
    }
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $bombs
     * @return Integer
     */
    function maximumDetonation($bombs) {
        $n = count($bombs);
        if ($n == 0) return 0;

        // Build adjacency list: edge i -> j if bomb j is within range of bomb i
        $adj = array_fill(0, $n, []);
        for ($i = 0; $i < $n; $i++) {
            [$xi, $yi, $ri] = $bombs[$i];
            $riSq = $ri * $ri;
            for ($j = 0; $j < $n; $j++) {
                if ($i === $j) continue;
                [$xj, $yj, $rj] = $bombs[$j];
                $dx = $xi - $xj;
                $dy = $yi - $yj;
                if ($dx * $dx + $dy * $dy <= $riSq) {
                    $adj[$i][] = $j;
                }
            }
        }

        $maxDetonated = 0;

        // Perform DFS/BFS from each bomb as the starting point
        for ($start = 0; $start < $n; $start++) {
            $visited = array_fill(0, $n, false);
            $stack = [$start];
            $visited[$start] = true;
            $count = 0;

            while (!empty($stack)) {
                $node = array_pop($stack);
                $count++;

                foreach ($adj[$node] as $neighbor) {
                    if (!$visited[$neighbor]) {
                        $visited[$neighbor] = true;
                        $stack[] = $neighbor;
                    }
                }
            }

            if ($count > $maxDetonated) {
                $maxDetonated = $count;
            }
        }

        return $maxDetonated;
    }
}
```

## Swift

```swift
class Solution {
    func maximumDetonation(_ bombs: [[Int]]) -> Int {
        let n = bombs.count
        var adj = [[Int]](repeating: [], count: n)
        
        for i in 0..<n {
            let xi = bombs[i][0]
            let yi = bombs[i][1]
            let ri = bombs[i][2]
            let rSq = Int64(ri) * Int64(ri)
            for j in 0..<n where i != j {
                let dx = Int64(xi - bombs[j][0])
                let dy = Int64(yi - bombs[j][1])
                if dx * dx + dy * dy <= rSq {
                    adj[i].append(j)
                }
            }
        }
        
        var maxDetonated = 0
        
        for start in 0..<n {
            var visited = [Bool](repeating: false, count: n)
            var stack = [Int]()
            stack.append(start)
            var count = 0
            
            while let node = stack.popLast() {
                if visited[node] { continue }
                visited[node] = true
                count += 1
                for neighbor in adj[node] where !visited[neighbor] {
                    stack.append(neighbor)
                }
            }
            
            maxDetonated = max(maxDetonated, count)
        }
        
        return maxDetonated
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumDetonation(bombs: Array<IntArray>): Int {
        val n = bombs.size
        val adj = Array(n) { mutableListOf<Int>() }

        for (i in 0 until n) {
            val xi = bombs[i][0]
            val yi = bombs[i][1]
            val ri = bombs[i][2].toLong()
            for (j in 0 until n) {
                if (i == j) continue
                val dx = xi - bombs[j][0]
                val dy = yi - bombs[j][1]
                val distSq = dx.toLong() * dx + dy.toLong() * dy
                if (distSq <= ri * ri) {
                    adj[i].add(j)
                }
            }
        }

        var maxDetonated = 0
        for (start in 0 until n) {
            val visited = BooleanArray(n)
            var count = 0
            val stack = java.util.ArrayDeque<Int>()
            stack.add(start)

            while (!stack.isEmpty()) {
                val cur = stack.poll()
                if (visited[cur]) continue
                visited[cur] = true
                count++
                for (next in adj[cur]) {
                    if (!visited[next]) {
                        stack.push(next)
                    }
                }
            }

            if (count > maxDetonated) maxDetonated = count
        }

        return maxDetonated
    }
}
```

## Dart

```dart
class Solution {
  int maximumDetonation(List<List<int>> bombs) {
    int n = bombs.length;
    List<List<int>> adj = List.generate(n, (_) => []);
    for (int i = 0; i < n; i++) {
      int xi = bombs[i][0];
      int yi = bombs[i][1];
      int ri = bombs[i][2];
      int r2 = ri * ri;
      for (int j = 0; j < n; j++) {
        if (i == j) continue;
        int dx = xi - bombs[j][0];
        int dy = yi - bombs[j][1];
        if (dx * dx + dy * dy <= r2) {
          adj[i].add(j);
        }
      }
    }

    int maxCount = 0;
    for (int start = 0; start < n; start++) {
      List<bool> visited = List.filled(n, false);
      List<int> stack = [start];
      visited[start] = true;
      int count = 0;

      while (stack.isNotEmpty) {
        int cur = stack.removeLast();
        count++;
        for (int nb in adj[cur]) {
          if (!visited[nb]) {
            visited[nb] = true;
            stack.add(nb);
          }
        }
      }

      if (count > maxCount) maxCount = count;
    }

    return maxCount;
  }
}
```

## Golang

```go
func maximumDetonation(bombs [][]int) int {
	n := len(bombs)
	adj := make([][]int, n)

	for i := 0; i < n; i++ {
		xi, yi, ri := bombs[i][0], bombs[i][1], bombs[i][2]
		rSq := int64(ri) * int64(ri)
		for j := 0; j < n; j++ {
			if i == j {
				continue
			}
			xj, yj := bombs[j][0], bombs[j][1]
			dx := int64(xi - xj)
			dy := int64(yi - yj)
			if dx*dx+dy*dy <= rSq {
				adj[i] = append(adj[i], j)
			}
		}
	}

	maxCount := 0
	for i := 0; i < n; i++ {
		visited := make([]bool, n)
		stack := []int{i}
		visited[i] = true
		count := 0

		for len(stack) > 0 {
			v := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			count++
			for _, nb := range adj[v] {
				if !visited[nb] {
					visited[nb] = true
					stack = append(stack, nb)
				}
			}
		}

		if count > maxCount {
			maxCount = count
		}
	}
	return maxCount
}
```

## Ruby

```ruby
def maximum_detonation(bombs)
  n = bombs.length
  adj = Array.new(n) { [] }
  (0...n).each do |i|
    xi, yi, ri = bombs[i]
    (0...n).each do |j|
      next if i == j
      xj, yj, _ = bombs[j]
      dx = xi - xj
      dy = yi - yj
      adj[i] << j if dx * dx + dy * dy <= ri * ri
    end
  end

  max_cnt = 0
  (0...n).each do |i|
    visited = Array.new(n, false)
    stack = [i]
    visited[i] = true
    cnt = 0
    until stack.empty?
      cur = stack.pop
      cnt += 1
      adj[cur].each do |nbr|
        next if visited[nbr]
        visited[nbr] = true
        stack << nbr
      end
    end
    max_cnt = cnt if cnt > max_cnt
  end
  max_cnt
end
```

## Scala

```scala
object Solution {
    def maximumDetonation(bombs: Array[Array[Int]]): Int = {
        val n = bombs.length
        val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
        for (i <- 0 until n) {
            val xi = bombs(i)(0)
            val yi = bombs(i)(1)
            val ri = bombs(i)(2).toLong
            val r2 = ri * ri
            for (j <- 0 until n if i != j) {
                val dx = bombs(j)(0) - xi
                val dy = bombs(j)(1) - yi
                val dist2 = dx.toLong * dx + dy.toLong * dy
                if (dist2 <= r2) adj(i).append(j)
            }
        }

        var maxDet = 0
        for (start <- 0 until n) {
            val visited = new Array[Boolean](n)
            val stack = new java.util.ArrayDeque[Int]()
            stack.push(start)
            visited(start) = true
            var count = 0
            while (!stack.isEmpty) {
                val cur = stack.pop()
                count += 1
                for (nbr <- adj(cur)) {
                    if (!visited(nbr)) {
                        visited(nbr) = true
                        stack.push(nbr)
                    }
                }
            }
            if (count > maxDet) maxDet = count
        }
        maxDet
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_detonation(bombs: Vec<Vec<i32>>) -> i32 {
        let n = bombs.len();
        let mut xs = vec![0i64; n];
        let mut ys = vec![0i64; n];
        let mut rs = vec![0i64; n];
        for (i, b) in bombs.iter().enumerate() {
            xs[i] = b[0] as i64;
            ys[i] = b[1] as i64;
            rs[i] = b[2] as i64;
        }

        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for i in 0..n {
            for j in 0..n {
                if i == j {
                    continue;
                }
                let dx = xs[i] - xs[j];
                let dy = ys[i] - ys[j];
                let dist2 = dx * dx + dy * dy;
                if dist2 <= rs[i] * rs[i] {
                    adj[i].push(j);
                }
            }
        }

        let mut max_cnt = 0usize;
        for start in 0..n {
            let mut visited = vec![false; n];
            let mut stack = Vec::new();
            stack.push(start);
            visited[start] = true;
            let mut cnt = 0usize;
            while let Some(u) = stack.pop() {
                cnt += 1;
                for &v in &adj[u] {
                    if !visited[v] {
                        visited[v] = true;
                        stack.push(v);
                    }
                }
            }
            if cnt > max_cnt {
                max_cnt = cnt;
            }
        }

        max_cnt as i32
    }
}
```

## Racket

```racket
(require racket)

(define/contract (maximum-detonation bombs)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length bombs))
         (xs (make-vector n))
         (ys (make-vector n))
         (rs (make-vector n)))
    ;; store coordinates and radii
    (for ([i (in-range n)]
          [b bombs])
      (vector-set! xs i (list-ref b 0))
      (vector-set! ys i (list-ref b 1))
      (vector-set! rs i (list-ref b 2)))
    ;; build adjacency list: i -> j if bomb i can trigger bomb j
    (define adj (make-vector n '()))
    (for ([i (in-range n)])
      (for ([j (in-range n)])
        (when (not (= i j))
          (let* ((dx (- (vector-ref xs i) (vector-ref xs j)))
                 (dy (- (vector-ref ys i) (vector-ref ys j)))
                 (dist2 (+ (* dx dx) (* dy dy)))
                 (r2 (* (vector-ref rs i) (vector-ref rs i))))
            (when (<= dist2 r2)
              (vector-set! adj i (cons j (vector-ref adj i))))))))
    ;; count reachable bombs from a start node using DFS
    (define (count-from s)
      (let ((visited (make-vector n #f))
            (stack (list s))
            (cnt 0))
        (let loop ()
          (if (null? stack)
              cnt
              (let* ((node (car stack))
                     (rest (cdr stack)))
                (set! stack rest)
                (if (vector-ref visited node)
                    (loop)
                    (begin
                      (vector-set! visited node #t)
                      (set! cnt (+ cnt 1))
                      (for ([nbr (vector-ref adj node)])
                        (set! stack (cons nbr stack)))
                      (loop))))))))
    ;; evaluate maximum over all possible starting bombs
    (let ((maxcnt 0))
      (for ([i (in-range n)])
        (let ((c (count-from i)))
          (when (> c maxcnt)
            (set! maxcnt c))))
      maxcnt)))
```

## Erlang

```erlang
-spec maximum_detonation(Bombs :: [[integer()]]) -> integer().
maximum_detonation(Bombs) ->
    BombTuples = [ {X,Y,R} || [X,Y,R] <- Bombs ],
    N = length(BombTuples),
    Adj = build_adj(N, BombTuples),
    max_from_all(0, N, Adj, 0).

build_adj(N, BombTuples) ->
    lists:map(
        fun(I) ->
            {Xi,Yi,Ri} = lists:nth(I+1, BombTuples),
            [ J || J <- lists:seq(0,N-1), I =/= J,
                    {Xj,Yj,_} = lists:nth(J+1,BombTuples),
                    (Xi-Xj)*(Xi-Xj) + (Yi-Yj)*(Yi-Yj) =< Ri*Ri ]
        end,
        lists:seq(0,N-1)
    ).

max_from_all(I, N, _Adj, Max) when I >= N -> Max;
max_from_all(I, N, Adj, Max) ->
    Count = reach_count(I, Adj),
    NewMax = if Count > Max -> Count; true -> Max end,
    max_from_all(I+1, N, Adj, NewMax).

reach_count(Start, Adj) ->
    dfs([Start], sets:new(), Adj).

dfs([], Visited, _Adj) -> sets:size(Visited);
dfs([Node|Rest], Visited, Adj) ->
    case sets:is_element(Node, Visited) of
        true -> dfs(Rest, Visited, Adj);
        false ->
            NewVisited = sets:add_element(Node, Visited),
            Neigh = lists:nth(Node+1, Adj),
            dfs(Neigh ++ Rest, NewVisited, Adj)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_detonation(bombs :: [[integer]]) :: integer
  def maximum_determinaton(_), do: :ok
  def maximum_detonation(bombs) do
    n = length(bombs)

    bombs_idx = Enum.with_index(bombs)

    adj =
      Enum.reduce(bombs_idx, %{}, fn {bomb_i, i}, acc ->
        edges =
          Enum.reduce(bombs_idx, [], fn {bomb_j, j}, eacc ->
            if i != j and in_range?(bomb_i, bomb_j) do
              [j | eacc]
            else
              eacc
            end
          end)

        Map.put(acc, i, edges)
      end)

    Enum.reduce(0..(n - 1), 0, fn start, best ->
      cnt = dfs(start, adj)
      if cnt > best, do: cnt, else: best
    end)
  end

  defp in_range?([x1, y1, r], [x2, y2, _]) do
    dx = x1 - x2
    dy = y1 - y2
    dx * dx + dy * dy <= r * r
  end

  defp dfs(start, adj) do
    dfs_stack([start], MapSet.new(), adj)
  end

  defp dfs_stack([], visited, _adj), do: MapSet.size(visited)

  defp dfs_stack([node | rest], visited, adj) do
    if MapSet.member?(visited, node) do
      dfs_stack(rest, visited, adj)
    else
      visited = MapSet.put(visited, node)
      neighbors = Map.get(adj, node, [])
      dfs_stack(neighbors ++ rest, visited, adj)
    end
  end
end
```

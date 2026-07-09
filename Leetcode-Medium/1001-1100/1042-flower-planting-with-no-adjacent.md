# 1042. Flower Planting With No Adjacent

## Cpp

```cpp
class Solution {
public:
    vector<int> gardenNoAdj(int n, vector<vector<int>>& paths) {
        vector<vector<int>> adj(n + 1);
        for (const auto& p : paths) {
            int u = p[0], v = p[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vector<int> ans(n, 0);
        for (int i = 1; i <= n; ++i) {
            bool used[5] = {false};
            for (int nb : adj[i]) {
                if (ans[nb - 1] != 0) {
                    used[ans[nb - 1]] = true;
                }
            }
            for (int c = 1; c <= 4; ++c) {
                if (!used[c]) {
                    ans[i - 1] = c;
                    break;
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
    public int[] gardenNoAdj(int n, int[][] paths) {
        // Build adjacency list
        List<Integer>[] adj = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int[] p : paths) {
            int a = p[0], b = p[1];
            adj[a].add(b);
            adj[b].add(a);
        }

        int[] ans = new int[n];
        // Assign colors greedily
        for (int i = 1; i <= n; i++) {
            boolean[] used = new boolean[5]; // indices 1..4
            for (int neighbor : adj[i]) {
                int color = ans[neighbor - 1];
                if (color != 0) {
                    used[color] = true;
                }
            }
            for (int c = 1; c <= 4; c++) {
                if (!used[c]) {
                    ans[i - 1] = c;
                    break;
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(n)]
        for u, v in paths:
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)

        ans = [0] * n
        for i in range(n):
            used = {ans[nb] for nb in adj[i] if ans[nb] != 0}
            for color in (1, 2, 3, 4):
                if color not in used:
                    ans[i] = color
                    break
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n + 1)]
        for u, v in paths:
            adj[u].append(v)
            adj[v].append(u)

        colors = [0] * (n + 1)  # 1-indexed
        for garden in range(1, n + 1):
            used = {colors[nei] for nei in adj[garden] if colors[nei] != 0}
            for c in range(1, 5):
                if c not in used:
                    colors[garden] = c
                    break

        return colors[1:]
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* gardenNoAdj(int n, int** paths, int pathsSize, int* pathsColSize, int* returnSize) {
    // adjacency list with maximum degree 3
    int **adj = (int **)malloc((n + 1) * sizeof(int *));
    int *deg = (int *)calloc(n + 1, sizeof(int));
    for (int i = 0; i <= n; ++i) {
        adj[i] = (int *)malloc(3 * sizeof(int));
    }

    // build graph
    for (int i = 0; i < pathsSize; ++i) {
        int u = paths[i][0];
        int v = paths[i][1];
        adj[u][deg[u]++] = v;
        adj[v][deg[v]++] = u;
    }

    int *ans = (int *)malloc(n * sizeof(int));
    memset(ans, 0, n * sizeof(int));

    // greedy coloring
    for (int i = 1; i <= n; ++i) {
        int used[5] = {0}; // indices 1..4
        for (int j = 0; j < deg[i]; ++j) {
            int nb = adj[i][j];
            if (ans[nb - 1] != 0) {
                used[ans[nb - 1]] = 1;
            }
        }
        for (int c = 1; c <= 4; ++c) {
            if (!used[c]) {
                ans[i - 1] = c;
                break;
            }
        }
    }

    // clean up auxiliary structures
    for (int i = 0; i <= n; ++i) {
        free(adj[i]);
    }
    free(adj);
    free(deg);

    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] GardenNoAdj(int n, int[][] paths) {
        var adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var p in paths) {
            int a = p[0] - 1;
            int b = p[1] - 1;
            adj[a].Add(b);
            adj[b].Add(a);
        }
        var ans = new int[n];
        for (int i = 0; i < n; i++) {
            bool[] used = new bool[5]; // indices 1..4
            foreach (var nb in adj[i]) {
                int c = ans[nb];
                if (c != 0) used[c] = true;
            }
            for (int color = 1; color <= 4; color++) {
                if (!used[color]) {
                    ans[i] = color;
                    break;
                }
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
 * @param {number[][]} paths
 * @return {number[]}
 */
var gardenNoAdj = function(n, paths) {
    const adj = Array.from({ length: n + 1 }, () => []);
    for (const [a, b] of paths) {
        adj[a].push(b);
        adj[b].push(a);
    }
    const ans = new Array(n).fill(0);
    for (let i = 1; i <= n; i++) {
        const used = [false, false, false, false, false]; // indices 1..4
        for (const nb of adj[i]) {
            const color = ans[nb - 1];
            if (color) used[color] = true;
        }
        let c = 1;
        while (c <= 4 && used[c]) c++;
        ans[i - 1] = c;
    }
    return ans;
};
```

## Typescript

```typescript
function gardenNoAdj(n: number, paths: number[][]): number[] {
    const adj: number[][] = Array.from({ length: n + 1 }, () => []);
    for (const [a, b] of paths) {
        adj[a].push(b);
        adj[b].push(a);
    }
    const res = new Array<number>(n).fill(0);
    for (let i = 1; i <= n; i++) {
        const used = new Set<number>();
        for (const nb of adj[i]) {
            const color = res[nb - 1];
            if (color) used.add(color);
        }
        for (let c = 1; c <= 4; c++) {
            if (!used.has(c)) {
                res[i - 1] = c;
                break;
            }
        }
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $paths
     * @return Integer[]
     */
    function gardenNoAdj($n, $paths) {
        // Build adjacency list (1-indexed)
        $adj = array_fill(0, $n + 1, []);
        foreach ($paths as $p) {
            $a = $p[0];
            $b = $p[1];
            $adj[$a][] = $b;
            $adj[$b][] = $a;
        }

        // Result array (1-indexed for convenience)
        $res = array_fill(0, $n + 1, 0);

        // Assign colors greedily
        for ($i = 1; $i <= $n; $i++) {
            $used = [false, false, false, false, false]; // indices 1..4
            foreach ($adj[$i] as $nei) {
                $c = $res[$nei];
                if ($c != 0) {
                    $used[$c] = true;
                }
            }
            for ($color = 1; $color <= 4; $color++) {
                if (!$used[$color]) {
                    $res[$i] = $color;
                    break;
                }
            }
        }

        // Convert to zero-indexed result array
        $answer = [];
        for ($i = 1; $i <= $n; $i++) {
            $answer[] = $res[$i];
        }
        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func gardenNoAdj(_ n: Int, _ paths: [[Int]]) -> [Int] {
        var adj = Array(repeating: [Int](), count: n + 1)
        for p in paths {
            let a = p[0]
            let b = p[1]
            adj[a].append(b)
            adj[b].append(a)
        }
        
        var colors = Array(repeating: 0, count: n + 1)
        for i in 1...n {
            var used = [Bool](repeating: false, count: 5) // indices 1..4
            for neighbor in adj[i] {
                let c = colors[neighbor]
                if c != 0 {
                    used[c] = true
                }
            }
            var chosen = 1
            while chosen <= 4 && used[chosen] {
                chosen += 1
            }
            colors[i] = chosen
        }
        
        return Array(colors[1...n])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun gardenNoAdj(n: Int, paths: Array<IntArray>): IntArray {
        val adj = Array(n) { mutableListOf<Int>() }
        for (p in paths) {
            val a = p[0] - 1
            val b = p[1] - 1
            adj[a].add(b)
            adj[b].add(a)
        }
        val result = IntArray(n)
        for (i in 0 until n) {
            val used = BooleanArray(5)
            for (nbr in adj[i]) {
                val color = result[nbr]
                if (color != 0) used[color] = true
            }
            var c = 1
            while (c <= 4 && used[c]) c++
            result[i] = c
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> gardenNoAdj(int n, List<List<int>> paths) {
    var adj = List.generate(n, (_) => <int>[]);
    for (var p in paths) {
      int a = p[0] - 1;
      int b = p[1] - 1;
      adj[a].add(b);
      adj[b].add(a);
    }
    var colors = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      var used = [false, false, false, false, false];
      for (var nb in adj[i]) {
        int c = colors[nb];
        if (c != 0) used[c] = true;
      }
      for (int col = 1; col <= 4; ++col) {
        if (!used[col]) {
          colors[i] = col;
          break;
        }
      }
    }
    return colors;
  }
}
```

## Golang

```go
func gardenNoAdj(n int, paths [][]int) []int {
	adj := make([][]int, n+1)
	for _, p := range paths {
		a, b := p[0], p[1]
		adj[a] = append(adj[a], b)
		adj[b] = append(adj[b], a)
	}
	ans := make([]int, n)
	for i := 1; i <= n; i++ {
		var used [5]bool
		for _, nb := range adj[i] {
			if c := ans[nb-1]; c != 0 {
				used[c] = true
			}
		}
		for c := 1; c <= 4; c++ {
			if !used[c] {
				ans[i-1] = c
				break
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def garden_no_adj(n, paths)
  adj = Array.new(n) { [] }
  paths.each do |x, y|
    x -= 1
    y -= 1
    adj[x] << y
    adj[y] << x
  end

  colors = Array.new(n, 0)

  (0...n).each do |i|
    used = [false] * 5
    adj[i].each do |nbr|
      c = colors[nbr]
      used[c] = true if c != 0
    end
    (1..4).each do |c|
      unless used[c]
        colors[i] = c
        break
      end
    end
  end

  colors
end
```

## Scala

```scala
object Solution {
    def gardenNoAdj(n: Int, paths: Array[Array[Int]]): Array[Int] = {
        val adj = Array.fill(n)(scala.collection.mutable.ArrayBuffer[Int]())
        for (p <- paths) {
            val a = p(0) - 1
            val b = p(1) - 1
            adj(a).append(b)
            adj(b).append(a)
        }
        val res = new Array[Int](n)
        for (i <- 0 until n) {
            val used = new Boolean(5) // indices 1..4
            for (nbr <- adj(i)) {
                val c = res(nbr)
                if (c != 0) used(c) = true
            }
            var color = 1
            while (color <= 4 && used(color)) color += 1
            res(i) = color
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn garden_no_adj(n: i32, paths: Vec<Vec<i32>>) -> Vec<i32> {
        let n_usize = n as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n_usize];
        for p in paths.iter() {
            let a = (p[0] - 1) as usize;
            let b = (p[1] - 1) as usize;
            adj[a].push(b);
            adj[b].push(a);
        }
        let mut ans: Vec<i32> = vec![0; n_usize];
        for i in 0..n_usize {
            let mut used = [false; 5]; // indices 1..4
            for &nbr in &adj[i] {
                let color = ans[nbr];
                if color != 0 {
                    used[color as usize] = true;
                }
            }
            for c in 1..=4 {
                if !used[c] {
                    ans[i] = c as i32;
                    break;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (garden-no-adj n paths)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((adj (make-vector (+ n 1) '()))
         (add-edge
          (lambda (u v)
            (vector-set! adj u (cons v (vector-ref adj u)))
            (vector-set! adj v (cons u (vector-ref adj v))))))
    (for-each (lambda (p) (add-edge (first p) (second p))) paths)
    (let ((colors (make-vector (+ n 1) 0))) ; index 1..n
      (do ((i 1 (+ i 1)))
          ((> i n))
        (define used (make-vector 5 #f)) ; indices 1..4
        (for ([nbr (vector-ref adj i)])
          (let ((c (vector-ref colors nbr)))
            (when (> c 0)
              (vector-set! used c #t))))
        (let loop ((col 1))
          (if (or (> col 4) (not (vector-ref used col)))
              (vector-set! colors i col)
              (loop (+ col 1)))))
      (let build ((i 1) (acc '()))
        (if (> i n)
            (reverse acc)
            (build (+ i 1) (cons (vector-ref colors i) acc)))))))
```

## Erlang

```erlang
-spec garden_no_adj(integer(), [[integer()]]) -> [integer()].
garden_no_adj(N, Paths) ->
    Adj = build_adj(Paths, #{}),
    assign(1, N, Adj, #{}).

build_adj([], Adj) ->
    Adj;
build_adj([[X, Y] | Rest], Adj0) ->
    Adj1 = maps:put(X, [Y | maps:get(X, Adj0, [])], Adj0),
    Adj2 = maps:put(Y, [X | maps:get(Y, Adj1, [])], Adj1),
    build_adj(Rest, Adj2).

assign(I, N, _Adj, ColorsMap) when I > N ->
    lists:map(fun(Index) -> maps:get(Index, ColorsMap) end,
              lists:seq(1, N));
assign(I, N, Adj, ColorsMap) ->
    Neigh = maps:get(I, Adj, []),
    Used = [maps:get(Nb, ColorsMap) || Nb <- Neigh, maps:is_key(Nb, ColorsMap)],
    Color = first_available([1, 2, 3, 4], Used),
    NewColorsMap = maps:put(I, Color, ColorsMap),
    assign(I + 1, N, Adj, NewColorsMap).

first_available([], _Used) ->
    1; % should never happen
first_available([C | Rest], Used) ->
    case lists:member(C, Used) of
        true -> first_available(Rest, Used);
        false -> C
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec garden_no_adj(n :: integer, paths :: [[integer]]) :: [integer]
  def garden_no_adj(n, paths) do
    adj = build_adj(n, paths)

    assignments =
      Enum.reduce(1..n, %{}, fn i, acc ->
        used_colors =
          adj[i]
          |> Enum.map(&Map.get(acc, &1, 0))
          |> Enum.filter(&(&1 != 0))
          |> MapSet.new()

        color = Enum.find(1..4, fn c -> not MapSet.member?(used_colors, c) end)
        Map.put(acc, i, color)
      end)

    Enum.map(1..n, &Map.get(assignments, &1))
  end

  defp build_adj(n, paths) do
    init = for i <- 1..n, into: %{}, do: {i, []}

    Enum.reduce(paths, init, fn [a, b], acc ->
      acc
      |> Map.update!(a, fn lst -> [b | lst] end)
      |> Map.update!(b, fn lst -> [a | lst] end)
    end)
  end
end
```

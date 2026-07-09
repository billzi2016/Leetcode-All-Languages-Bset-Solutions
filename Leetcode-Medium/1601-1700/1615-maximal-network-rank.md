# 1615. Maximal Network Rank

## Cpp

```cpp
class Solution {
public:
    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
        vector<int> deg(n, 0);
        vector<vector<bool>> adj(n, vector<bool>(n, false));
        for (const auto& r : roads) {
            int a = r[0], b = r[1];
            ++deg[a];
            ++deg[b];
            adj[a][b] = adj[b][a] = true;
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int rank = deg[i] + deg[j] - (adj[i][j] ? 1 : 0);
                ans = max(ans, rank);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximalNetworkRank(int n, int[][] roads) {
        int[] degree = new int[n];
        boolean[][] connected = new boolean[n][n];
        
        for (int[] road : roads) {
            int a = road[0];
            int b = road[1];
            degree[a]++;
            degree[b]++;
            connected[a][b] = true;
            connected[b][a] = true;
        }
        
        int maxRank = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int rank = degree[i] + degree[j];
                if (connected[i][j]) {
                    rank--;
                }
                if (rank > maxRank) {
                    maxRank = rank;
                }
            }
        }
        return maxRank;
    }
}
```

## Python

```python
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        degree = [0] * n
        connected = [[False] * n for _ in range(n)]
        
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            connected[a][b] = connected[b][a] = True
        
        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j]
                if connected[i][j]:
                    rank -= 1
                if rank > max_rank:
                    max_rank = rank
        return max_rank
```

## Python3

```python
from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        connected = [[False] * n for _ in range(n)]
        
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            connected[a][b] = connected[b][a] = True
        
        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j] - (1 if connected[i][j] else 0)
                if rank > max_rank:
                    max_rank = rank
        return max_rank
```

## C

```c
#include <stdlib.h>

int maximalNetworkRank(int n, int** roads, int roadsSize, int* roadsColSize) {
    int *deg = (int *)calloc(n, sizeof(int));
    int *adj = (int *)calloc(n * n, sizeof(int)); // adjacency matrix flattened

    for (int i = 0; i < roadsSize; ++i) {
        int a = roads[i][0];
        int b = roads[i][1];
        deg[a]++; 
        deg[b]++;
        adj[a * n + b] = 1;
        adj[b * n + a] = 1;
    }

    int maxRank = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int rank = deg[i] + deg[j];
            if (adj[i * n + j]) rank -= 1; // road counted twice
            if (rank > maxRank) maxRank = rank;
        }
    }

    free(deg);
    free(adj);
    return maxRank;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximalNetworkRank(int n, int[][] roads) {
        int[] degree = new int[n];
        bool[,] connected = new bool[n, n];

        foreach (var road in roads) {
            int a = road[0];
            int b = road[1];
            degree[a]++;
            degree[b]++;
            connected[a, b] = true;
            connected[b, a] = true;
        }

        int maxRank = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int rank = degree[i] + degree[j];
                if (connected[i, j]) rank--;
                if (rank > maxRank) maxRank = rank;
            }
        }

        return maxRank;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var maximalNetworkRank = function(n, roads) {
    const degree = new Array(n).fill(0);
    const connected = Array.from({ length: n }, () => Array(n).fill(false));
    
    for (const [a, b] of roads) {
        degree[a]++;
        degree[b]++;
        connected[a][b] = true;
        connected[b][a] = true;
    }
    
    let maxRank = 0;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            let rank = degree[i] + degree[j];
            if (connected[i][j]) rank--;
            if (rank > maxRank) maxRank = rank;
        }
    }
    
    return maxRank;
};
```

## Typescript

```typescript
function maximalNetworkRank(n: number, roads: number[][]): number {
    const degree = new Array<number>(n).fill(0);
    const adj: Set<number>[] = Array.from({ length: n }, () => new Set<number>());
    
    for (const [a, b] of roads) {
        degree[a]++;
        degree[b]++;
        adj[a].add(b);
        adj[b].add(a);
    }
    
    let maxRank = 0;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            let rank = degree[i] + degree[j];
            if (adj[i].has(j)) rank--;
            if (rank > maxRank) maxRank = rank;
        }
    }
    
    return maxRank;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $roads
     * @return Integer
     */
    function maximalNetworkRank($n, $roads) {
        $deg = array_fill(0, $n, 0);
        $connected = array_fill(0, $n, array_fill(0, $n, false));

        foreach ($roads as $road) {
            [$a, $b] = $road;
            $deg[$a]++;
            $deg[$b]++;
            $connected[$a][$b] = true;
            $connected[$b][$a] = true;
        }

        $maxRank = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $rank = $deg[$i] + $deg[$j];
                if ($connected[$i][$j]) {
                    $rank--;
                }
                if ($rank > $maxRank) {
                    $maxRank = $rank;
                }
            }
        }

        return $maxRank;
    }
}
```

## Swift

```swift
class Solution {
    func maximalNetworkRank(_ n: Int, _ roads: [[Int]]) -> Int {
        var degree = [Int](repeating: 0, count: n)
        var adj = Array(repeating: Array(repeating: false, count: n), count: n)
        
        for road in roads {
            let a = road[0]
            let b = road[1]
            degree[a] += 1
            degree[b] += 1
            adj[a][b] = true
            adj[b][a] = true
        }
        
        var maxRank = 0
        if n >= 2 {
            for i in 0..<(n - 1) {
                for j in (i + 1)..<n {
                    var rank = degree[i] + degree[j]
                    if adj[i][j] { rank -= 1 }
                    if rank > maxRank { maxRank = rank }
                }
            }
        }
        return maxRank
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximalNetworkRank(n: Int, roads: Array<IntArray>): Int {
        val degree = IntArray(n)
        val connected = Array(n) { BooleanArray(n) }
        for (road in roads) {
            val a = road[0]
            val b = road[1]
            degree[a]++
            degree[b]++
            connected[a][b] = true
            connected[b][a] = true
        }
        var maxRank = 0
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                var rank = degree[i] + degree[j]
                if (connected[i][j]) rank--
                if (rank > maxRank) maxRank = rank
            }
        }
        return maxRank
    }
}
```

## Dart

```dart
class Solution {
  int maximalNetworkRank(int n, List<List<int>> roads) {
    List<int> degree = List.filled(n, 0);
    List<List<bool>> connected = List.generate(n, (_) => List.filled(n, false));
    for (var road in roads) {
      int a = road[0];
      int b = road[1];
      degree[a]++;
      degree[b]++;
      connected[a][b] = true;
      connected[b][a] = true;
    }
    int maxRank = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        int rank = degree[i] + degree[j];
        if (connected[i][j]) rank--;
        if (rank > maxRank) maxRank = rank;
      }
    }
    return maxRank;
  }
}
```

## Golang

```go
func maximalNetworkRank(n int, roads [][]int) int {
	deg := make([]int, n)
	adj := make([][]bool, n)
	for i := 0; i < n; i++ {
		adj[i] = make([]bool, n)
	}
	for _, r := range roads {
		a, b := r[0], r[1]
		deg[a]++
		deg[b]++
		adj[a][b] = true
		adj[b][a] = true
	}
	maxRank := 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			rank := deg[i] + deg[j]
			if adj[i][j] {
				rank--
			}
			if rank > maxRank {
				maxRank = rank
			}
		}
	}
	return maxRank
}
```

## Ruby

```ruby
def maximal_network_rank(n, roads)
  degree = Array.new(n, 0)
  connected = Array.new(n) { Array.new(n, false) }
  roads.each do |a, b|
    degree[a] += 1
    degree[b] += 1
    connected[a][b] = true
    connected[b][a] = true
  end

  max_rank = 0
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      rank = degree[i] + degree[j]
      rank -= 1 if connected[i][j]
      max_rank = rank if rank > max_rank
    end
  end

  max_rank
end
```

## Scala

```scala
object Solution {
    def maximalNetworkRank(n: Int, roads: Array[Array[Int]]): Int = {
        val degree = new Array[Int](n)
        val connected = Array.ofDim[Boolean](n, n)

        for (road <- roads) {
            val a = road(0)
            val b = road(1)
            degree(a) += 1
            degree(b) += 1
            connected(a)(b) = true
            connected(b)(a) = true
        }

        var maxRank = 0
        for (i <- 0 until n; j <- i + 1 until n) {
            var rank = degree(i) + degree(j)
            if (connected(i)(j)) rank -= 1
            if (rank > maxRank) maxRank = rank
        }
        maxRank
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximal_network_rank(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut degree = vec![0i32; n];
        let mut connected = vec![vec![false; n]; n];

        for road in roads.iter() {
            let a = road[0] as usize;
            let b = road[1] as usize;
            degree[a] += 1;
            degree[b] += 1;
            connected[a][b] = true;
            connected[b][a] = true;
        }

        let mut max_rank = 0i32;
        for i in 0..n {
            for j in (i + 1)..n {
                let mut rank = degree[i] + degree[j];
                if connected[i][j] {
                    rank -= 1;
                }
                if rank > max_rank {
                    max_rank = rank;
                }
            }
        }

        max_rank
    }
}
```

## Racket

```racket
(define/contract (maximal-network-rank n roads)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ([deg (make-vector n 0)]
         [adj (for/vector ([i (in-range n)]) (make-vector n #f))])
    (for ([road roads])
      (match-define (list a b) road)
      (vector-set! deg a (+ 1 (vector-ref deg a)))
      (vector-set! deg b (+ 1 (vector-ref deg b)))
      (vector-set! (vector-ref adj a) b #t)
      (vector-set! (vector-ref adj b) a #t))
    (let loop ((i 0) (max-rank 0))
      (if (= i n)
          max-rank
          (let inner-loop ((j (+ i 1)) (cur-max max-rank))
            (if (>= j n)
                (loop (+ i 1) cur-max)
                (let* ([rank (+ (vector-ref deg i) (vector-ref deg j))]
                       [rank (if (vector-ref (vector-ref adj i) j) (- rank 1) rank)])
                  (inner-loop (+ j 1) (max cur-max rank)))))))))
```

## Erlang

```erlang
-spec maximal_network_rank(N :: integer(), Roads :: [[integer()]]) -> integer().
maximal_network_rank(N, Roads) ->
    DegInit = maps:from_list([{I,0} || I <- lists:seq(0,N-1)]),
    {DegMap, EdgeMap} =
        lists:foldl(
            fun([A,B], {DegM, EdgeM}) ->
                DegM1 = maps:update_with(A, fun(V) -> V + 1 end, 1, DegM),
                DegM2 = maps:update_with(B, fun(V) -> V + 1 end, 1, DegM1),
                Key = if A < B -> {A,B}; true -> {B,A} end,
                EdgeM1 = maps:put(Key, true, EdgeM),
                {DegM2, EdgeM1}
            end,
            {DegInit, #{}},
            Roads
        ),
    Pairs = [{I,J} || I <- lists:seq(0,N-2), J <- lists:seq(I+1, N-1)],
    Ranks = [
        (maps:get(I, DegMap) + maps:get(J, DegMap) -
            (if maps:is_key({erlang:min(I,J), erlang:max(I,J)}, EdgeMap) -> 1; true -> 0 end))
        || {I,J} <- Pairs
    ],
    lists:max(Ranks).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximal_network_rank(n :: integer, roads :: [[integer]]) :: integer
  def maximal_network_rank(n, roads) do
    degrees =
      Enum.reduce(roads, %{}, fn [a, b], acc ->
        acc
        |> Map.update(a, 1, &(&1 + 1))
        |> Map.update(b, 1, &(&1 + 1))
      end)

    adj =
      Enum.reduce(roads, MapSet.new(), fn [a, b], set ->
        if a < b do
          MapSet.put(set, {a, b})
        else
          MapSet.put(set, {b, a})
        end
      end)

    max_rank =
      for i <- 0..(n - 2), j <- (i + 1)..(n - 1), reduce: 0 do
        acc ->
          rank = Map.get(degrees, i, 0) + Map.get(degrees, j, 0)
          rank = if MapSet.member?(adj, {i, j}), do: rank - 1, else: rank
          if rank > acc, do: rank, else: acc
      end

    max_rank
  end
end
```

# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

## Cpp

```cpp
class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        const int INF = 1e9;
        vector<vector<int>> dist(n, vector<int>(n, INF));
        for (int i = 0; i < n; ++i) dist[i][i] = 0;
        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            dist[u][v] = min(dist[u][v], w);
            dist[v][u] = min(dist[v][u], w);
        }
        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < n; ++i) {
                if (dist[i][k] == INF) continue;
                for (int j = 0; j < n; ++j) {
                    if (dist[k][j] == INF) continue;
                    if (dist[i][j] > dist[i][k] + dist[k][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
        int answer = -1, minReachable = n + 1;
        for (int i = 0; i < n; ++i) {
            int cnt = 0;
            for (int j = 0; j < n; ++j) {
                if (i != j && dist[i][j] <= distanceThreshold) ++cnt;
            }
            if (cnt < minReachable || (cnt == minReachable && i > answer)) {
                minReachable = cnt;
                answer = i;
            }
        }
        return answer;
    }
};
```

## Java

```java
class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int INF = Integer.MAX_VALUE / 4;
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) {
            java.util.Arrays.fill(dist[i], INF);
            dist[i][i] = 0;
        }
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            dist[u][v] = w;
            dist[v][u] = w;
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                if (dist[i][k] == INF) continue;
                for (int j = 0; j < n; j++) {
                    if (dist[k][j] == INF) continue;
                    int nd = dist[i][k] + dist[k][j];
                    if (nd < dist[i][j]) {
                        dist[i][j] = nd;
                    }
                }
            }
        }

        int answer = -1;
        int minReachable = n + 1;
        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                if (i != j && dist[i][j] <= distanceThreshold) {
                    cnt++;
                }
            }
            if (cnt < minReachable || (cnt == minReachable && i > answer)) {
                minReachable = cnt;
                answer = i;
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        INF = 10**9
        # initialize distance matrix
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd-Warshall
        for k in range(n):
            dk = dist[k]
            for i in range(n):
                dik = dist[i][k]
                if dik == INF:
                    continue
                di = dist[i]
                for j in range(n):
                    nd = dik + dk[j]
                    if nd < di[j]:
                        di[j] = nd

        best_city = -1
        min_reachable = n + 1
        for i in range(n):
            cnt = sum(1 for d in dist[i] if d <= distanceThreshold)
            if cnt < min_reachable or (cnt == min_reachable and i > best_city):
                min_reachable = cnt
                best_city = i
        return best_city
```

## Python3

```python
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = 10**9
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            if w < dist[u][v]:
                dist[u][v] = dist[v][u] = w

        for k in range(n):
            dk = dist[k]
            for i in range(n):
                dik = dist[i][k]
                if dik == INF:
                    continue
                di = dist[i]
                for j in range(n):
                    nd = dik + dk[j]
                    if nd < di[j]:
                        di[j] = nd

        answer = -1
        min_reachable = n + 1
        for i in range(n):
            reachable = sum(1 for d in dist[i] if d <= distanceThreshold) - 1  # exclude self
            if reachable <= min_reachable:
                min_reachable = reachable
                answer = i
        return answer
```

## C

```c
#include <stdlib.h>

int findTheCity(int n, int** edges, int edgesSize, int* edgesColSize, int distanceThreshold) {
    const int INF = 0x3f3f3f3f; // sufficiently large
    
    // Allocate distance matrix
    int **dist = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        dist[i] = (int *)malloc(n * sizeof(int));
        for (int j = 0; j < n; ++j) {
            dist[i][j] = (i == j) ? 0 : INF;
        }
    }
    
    // Initialize with given edges
    for (int e = 0; e < edgesSize; ++e) {
        int u = edges[e][0];
        int v = edges[e][1];
        int w = edges[e][2];
        if (w < dist[u][v]) {
            dist[u][v] = w;
            dist[v][u] = w;
        }
    }
    
    // Floyd-Warshall
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            if (dist[i][k] == INF) continue;
            for (int j = 0; j < n; ++j) {
                if (dist[k][j] == INF) continue;
                int nd = dist[i][k] + dist[k][j];
                if (nd < dist[i][j]) {
                    dist[i][j] = nd;
                }
            }
        }
    }
    
    // Find the city with minimal reachable count (largest index on tie)
    int answer = -1;
    int bestCnt = n + 1;
    for (int i = 0; i < n; ++i) {
        int cnt = 0;
        for (int j = 0; j < n; ++j) {
            if (dist[i][j] <= distanceThreshold) {
                ++cnt;
            }
        }
        if (cnt <= bestCnt) { // tie -> larger index wins
            bestCnt = cnt;
            answer = i;
        }
    }
    
    // Free memory
    for (int i = 0; i < n; ++i) {
        free(dist[i]);
    }
    free(dist);
    
    return answer;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindTheCity(int n, int[][] edges, int distanceThreshold)
    {
        const int INF = 1_000_000_000;
        int[,] dist = new int[n, n];

        // Initialize distances
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
                dist[i, j] = INF;
            dist[i, i] = 0;
        }

        // Set direct edge weights
        foreach (var e in edges)
        {
            int u = e[0];
            int v = e[1];
            int w = e[2];
            if (w < dist[u, v])
            {
                dist[u, v] = w;
                dist[v, u] = w;
            }
        }

        // Floyd-Warshall
        for (int k = 0; k < n; k++)
        {
            for (int i = 0; i < n; i++)
            {
                if (dist[i, k] == INF) continue;
                for (int j = 0; j < n; j++)
                {
                    if (dist[k, j] == INF) continue;
                    int nd = dist[i, k] + dist[k, j];
                    if (nd < dist[i, j])
                        dist[i, j] = nd;
                }
            }
        }

        int answer = -1;
        int minReachable = n + 1;

        for (int i = 0; i < n; i++)
        {
            int cnt = 0;
            for (int j = 0; j < n; j++)
            {
                if (i != j && dist[i, j] <= distanceThreshold)
                    cnt++;
            }

            if (cnt < minReachable || (cnt == minReachable && i > answer))
            {
                minReachable = cnt;
                answer = i;
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} distanceThreshold
 * @return {number}
 */
var findTheCity = function(n, edges, distanceThreshold) {
    const INF = 1e9;
    const dist = Array.from({ length: n }, () => Array(n).fill(INF));
    for (let i = 0; i < n; i++) dist[i][i] = 0;
    for (const [u, v, w] of edges) {
        if (w < dist[u][v]) {
            dist[u][v] = w;
            dist[v][u] = w;
        }
    }
    for (let k = 0; k < n; k++) {
        for (let i = 0; i < n; i++) {
            const dik = dist[i][k];
            if (dik === INF) continue;
            for (let j = 0; j < n; j++) {
                const newDist = dik + dist[k][j];
                if (newDist < dist[i][j]) {
                    dist[i][j] = newDist;
                }
            }
        }
    }
    let answer = -1;
    let minReachable = n + 1;
    for (let i = 0; i < n; i++) {
        let cnt = 0;
        for (let j = 0; j < n; j++) {
            if (i !== j && dist[i][j] <= distanceThreshold) cnt++;
        }
        if (cnt < minReachable || (cnt === minReachable && i > answer)) {
            minReachable = cnt;
            answer = i;
        }
    }
    return answer;
};
```

## Typescript

```typescript
function findTheCity(n: number, edges: number[][], distanceThreshold: number): number {
    const INF = 1e9;
    const dist: number[][] = Array.from({ length: n }, () => Array(n).fill(INF));
    
    for (let i = 0; i < n; i++) {
        dist[i][i] = 0;
    }
    
    for (const [u, v, w] of edges) {
        if (w < dist[u][v]) { // in case multiple edges exist
            dist[u][v] = w;
            dist[v][u] = w;
        }
    }
    
    for (let k = 0; k < n; k++) {
        for (let i = 0; i < n; i++) {
            if (dist[i][k] === INF) continue;
            for (let j = 0; j < n; j++) {
                const nd = dist[i][k] + dist[k][j];
                if (nd < dist[i][j]) {
                    dist[i][j] = nd;
                }
            }
        }
    }
    
    let answer = -1;
    let minReachable = n + 1;
    
    for (let i = 0; i < n; i++) {
        let cnt = 0;
        for (let j = 0; j < n; j++) {
            if (i !== j && dist[i][j] <= distanceThreshold) cnt++;
        }
        if (cnt < minReachable || (cnt === minReachable && i > answer)) {
            minReachable = cnt;
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
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $distanceThreshold
     * @return Integer
     */
    function findTheCity($n, $edges, $distanceThreshold) {
        $INF = 1e9;
        // Initialize distance matrix
        $dist = array_fill(0, $n, array_fill(0, $n, $INF));
        for ($i = 0; $i < $n; $i++) {
            $dist[$i][$i] = 0;
        }
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $w = $e[2];
            if ($w < $dist[$u][$v]) {
                $dist[$u][$v] = $w;
                $dist[$v][$u] = $w;
            }
        }

        // Floyd-Warshall
        for ($k = 0; $k < $n; $k++) {
            for ($i = 0; $i < $n; $i++) {
                if ($dist[$i][$k] == $INF) continue;
                for ($j = 0; $j < $n; $j++) {
                    $newDist = $dist[$i][$k] + $dist[$k][$j];
                    if ($newDist < $dist[$i][$j]) {
                        $dist[$i][$j] = $newDist;
                    }
                }
            }
        }

        $answer = -1;
        $minReachable = $n + 1; // larger than any possible count
        for ($i = 0; $i < $n; $i++) {
            $cnt = 0;
            for ($j = 0; $j < $n; $j++) {
                if ($i != $j && $dist[$i][$j] <= $distanceThreshold) {
                    $cnt++;
                }
            }
            if ($cnt < $minReachable || ($cnt == $minReachable && $i > $answer)) {
                $minReachable = $cnt;
                $answer = $i;
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func findTheCity(_ n: Int, _ edges: [[Int]], _ distanceThreshold: Int) -> Int {
        let INF = Int.max / 4
        var dist = Array(repeating: Array(repeating: INF, count: n), count: n)
        for i in 0..<n { dist[i][i] = 0 }
        for e in edges {
            let u = e[0], v = e[1], w = e[2]
            dist[u][v] = w
            dist[v][u] = w
        }
        for k in 0..<n {
            for i in 0..<n where dist[i][k] != INF {
                for j in 0..<n {
                    let nd = dist[i][k] + dist[k][j]
                    if nd < dist[i][j] {
                        dist[i][j] = nd
                    }
                }
            }
        }
        var answer = -1
        var minReachable = n + 1
        for i in 0..<n {
            var cnt = 0
            for j in 0..<n where i != j && dist[i][j] <= distanceThreshold {
                cnt += 1
            }
            if cnt < minReachable || (cnt == minReachable && i > answer) {
                minReachable = cnt
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
    fun findTheCity(n: Int, edges: Array<IntArray>, distanceThreshold: Int): Int {
        val INF = 1_000_000_000
        val dist = Array(n) { IntArray(n) { INF } }
        for (i in 0 until n) {
            dist[i][i] = 0
        }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val w = e[2]
            if (w < dist[u][v]) {
                dist[u][v] = w
                dist[v][u] = w
            }
        }
        for (k in 0 until n) {
            for (i in 0 until n) {
                if (dist[i][k] == INF) continue
                for (j in 0 until n) {
                    if (dist[k][j] == INF) continue
                    val nd = dist[i][k] + dist[k][j]
                    if (nd < dist[i][j]) {
                        dist[i][j] = nd
                    }
                }
            }
        }
        var answer = 0
        var minCount = n + 1
        for (i in 0 until n) {
            var cnt = 0
            for (j in 0 until n) {
                if (i != j && dist[i][j] <= distanceThreshold) {
                    cnt++
                }
            }
            if (cnt < minCount || (cnt == minCount && i > answer)) {
                minCount = cnt
                answer = i
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int findTheCity(int n, List<List<int>> edges, int distanceThreshold) {
    const int INF = 1000000000;
    // Initialize distance matrix
    List<List<int>> dist = List.generate(
        n, (_) => List.filled(n, INF, growable: false),
        growable: false);
    for (int i = 0; i < n; i++) {
      dist[i][i] = 0;
    }
    // Fill direct edges
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      int w = e[2];
      if (w < dist[u][v]) {
        dist[u][v] = w;
        dist[v][u] = w;
      }
    }
    // Floyd-Warshall
    for (int k = 0; k < n; k++) {
      for (int i = 0; i < n; i++) {
        if (dist[i][k] == INF) continue;
        for (int j = 0; j < n; j++) {
          int via = dist[i][k] + dist[k][j];
          if (via < dist[i][j]) {
            dist[i][j] = via;
          }
        }
      }
    }
    // Find city with smallest reachable count, tie-breaking by larger index
    int bestCount = n + 1;
    int answer = -1;
    for (int i = 0; i < n; i++) {
      int cnt = 0;
      for (int j = 0; j < n; j++) {
        if (i != j && dist[i][j] <= distanceThreshold) cnt++;
      }
      if (cnt < bestCount || (cnt == bestCount && i > answer)) {
        bestCount = cnt;
        answer = i;
      }
    }
    return answer;
  }
}
```

## Golang

```go
func findTheCity(n int, edges [][]int, distanceThreshold int) int {
	const INF = int(1e9)

	// Initialize distance matrix
	dist := make([][]int, n)
	for i := 0; i < n; i++ {
		row := make([]int, n)
		for j := 0; j < n; j++ {
			if i == j {
				row[j] = 0
			} else {
				row[j] = INF
			}
		}
		dist[i] = row
	}

	// Set direct edges
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		if w < dist[u][v] { // just in case multiple edges (though problem says distinct)
			dist[u][v] = w
			dist[v][u] = w
		}
	}

	// Floyd-Warshall
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			if dist[i][k] == INF {
				continue
			}
			for j := 0; j < n; j++ {
				if dist[k][j] == INF {
					continue
				}
				if nd := dist[i][k] + dist[k][j]; nd < dist[i][j] {
					dist[i][j] = nd
				}
			}
		}
	}

	ans := -1
	minReachable := n + 1

	for i := 0; i < n; i++ {
		cnt := 0
		for j := 0; j < n; j++ {
			if dist[i][j] <= distanceThreshold {
				cnt++
			}
		}
		if cnt < minReachable || (cnt == minReachable && i > ans) {
			minReachable = cnt
			ans = i
		}
	}

	return ans
}
```

## Ruby

```ruby
def find_the_city(n, edges, distance_threshold)
  inf = 1 << 60
  dist = Array.new(n) { Array.new(n, inf) }
  n.times { |i| dist[i][i] = 0 }

  edges.each do |u, v, w|
    if w < dist[u][v]
      dist[u][v] = w
      dist[v][u] = w
    end
  end

  n.times do |k|
    n.times do |i|
      next if dist[i][k] == inf
      n.times do |j|
        via = dist[i][k] + dist[k][j]
        dist[i][j] = via if via < dist[i][j]
      end
    end
  end

  best_city = -1
  min_cnt = n + 1
  n.times do |i|
    cnt = 0
    n.times do |j|
      next if i == j
      cnt += 1 if dist[i][j] <= distance_threshold
    end
    if cnt < min_cnt || (cnt == min_cnt && i > best_city)
      min_cnt = cnt
      best_city = i
    end
  end

  best_city
end
```

## Scala

```scala
object Solution {
  def findTheCity(n: Int, edges: Array[Array[Int]], distanceThreshold: Int): Int = {
    val INF = 1_000_000_007
    val dist = Array.ofDim[Int](n, n)

    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        dist(i)(j) = if (i == j) 0 else INF
        j += 1
      }
      i += 1
    }

    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      val w = e(2)
      if (w < dist(u)(v)) {
        dist(u)(v) = w
        dist(v)(u) = w
      }
    }

    var k = 0
    while (k < n) {
      var ii = 0
      while (ii < n) {
        if (dist(ii)(k) != INF) {
          var jj = 0
          while (jj < n) {
            if (dist(k)(jj) != INF) {
              val newDist = dist(ii)(k).toLong + dist(k)(jj)
              if (newDist < dist(ii)(jj)) {
                dist(ii)(jj) = newDist.toInt
              }
            }
            jj += 1
          }
        }
        ii += 1
      }
      k += 1
    }

    var answer = -1
    var minCount = Int.MaxValue

    var city = 0
    while (city < n) {
      var cnt = 0
      var other = 0
      while (other < n) {
        if (city != other && dist(city)(other) <= distanceThreshold) cnt += 1
        other += 1
      }
      if (cnt < minCount || (cnt == minCount && city > answer)) {
        minCount = cnt
        answer = city
      }
      city += 1
    }

    answer
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_the_city(n: i32, edges: Vec<Vec<i32>>, distance_threshold: i32) -> i32 {
        let n = n as usize;
        let inf: i64 = 1_000_000_000_000; // sufficiently large
        let mut dist = vec![vec![inf; n]; n];
        for i in 0..n {
            dist[i][i] = 0;
        }
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2] as i64;
            if w < dist[u][v] {
                dist[u][v] = w;
                dist[v][u] = w;
            }
        }

        for k in 0..n {
            for i in 0..n {
                let dik = dist[i][k];
                if dik == inf {
                    continue;
                }
                for j in 0..n {
                    let nd = dik + dist[k][j];
                    if nd < dist[i][j] {
                        dist[i][j] = nd;
                    }
                }
            }
        }

        let mut answer: usize = 0;
        let mut best_cnt = n + 1;
        for i in 0..n {
            let mut cnt = 0usize;
            for j in 0..n {
                if i != j && dist[i][j] <= distance_threshold as i64 {
                    cnt += 1;
                }
            }
            if cnt < best_cnt || (cnt == best_cnt && i > answer) {
                best_cnt = cnt;
                answer = i;
            }
        }

        answer as i32
    }
}
```

## Racket

```racket
#lang racket

(define/contract (find-the-city n edges distanceThreshold)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([INF 1000000000]
         [dist (make-vector n)])
    ;; initialize distances
    (for ([i (in-range n)])
      (vector-set! dist i (make-vector n INF))
      (vector-set! (vector-ref dist i) i 0))
    ;; set direct edges
    (for ([e edges])
      (match e
        [(list u v w)
         (let* ([row-u (vector-ref dist u)]
                [row-v (vector-ref dist v)])
           (when (< w (vector-ref row-u v))
             (vector-set! row-u v w)
             (vector-set! row-v u w)))]))
    ;; Floyd‑Warshall
    (for ([k (in-range n)])
      (let ([dist-k (vector-ref dist k)])
        (for ([i (in-range n)])
          (let* ([dist-i (vector-ref dist i)]
                 [dik (vector-ref dist-i k)])
            (when (< dik INF)
              (for ([j (in-range n)])
                (let* ([dkj (vector-ref dist-k j)]
                       [new (+ dik dkj)])
                  (when (< new (vector-ref dist-i j))
                    (vector-set! dist-i j new)))))))))
    ;; find answer
    (let ([answer -1]
          [minCnt n])
      (for ([i (in-range n)])
        (define cnt
          (let loop ((j 0) (c 0))
            (if (= j n)
                c
                (let ([d (vector-ref (vector-ref dist i) j)])
                  (loop (+ j 1) (if (<= d distanceThreshold) (+ c 1) c))))))
        (when (or (< cnt minCnt) (and (= cnt minCnt) (> i answer)))
          (set! minCnt cnt)
          (set! answer i)))
      answer)))
```

## Erlang

```erlang
-module(solution).
-export([find_the_city/3]).

-define(INF, 1000000000).

-spec find_the_city(N :: integer(), Edges :: [[integer()]], DistanceThreshold :: integer()) -> integer().
find_the_city(N, Edges, DistanceThreshold) ->
    DistMap0 = init_dist_map(N, ?INF),
    DistMap1 = add_edges(Edges, DistMap0),
    FinalMap = floyd(0, N, DistMap1),
    best_city(0, N, FinalMap, DistanceThreshold, -1, N + 1).

%% Initialize distance map with INF and zero on diagonal
init_dist_map(N, Inf) ->
    lists:foldl(fun(I, AccI) ->
        lists:foldl(fun(J, AccJ) ->
            Dist = if I == J -> 0; true -> Inf end,
            maps:put({I,J}, Dist, AccJ)
        end, AccI, lists:seq(0, N-1))
    end, #{}, lists:seq(0, N-1)).

%% Add edges to the distance map (keep minimum weight if multiple edges)
add_edges([], Map) -> Map;
add_edges([[U,V,W]|Rest], Map) ->
    CurUV = maps:get({U,V}, Map),
    NewUV = if W < CurUV -> W; true -> CurUV end,
    CurVU = maps:get({V,U}, Map),
    NewVU = if W < CurVU -> W; true -> CurVU end,
    Map1 = maps:put({U,V}, NewUV, Map),
    Map2 = maps:put({V,U}, NewVU, Map1),
    add_edges(Rest, Map2).

%% Floyd‑Warshall algorithm using a map for distances
floyd(K, N, DistMap) when K >= N -> DistMap;
floyd(K, N, DistMap) ->
    UpdatedMap = process_i(0, K, N, DistMap),
    floyd(K + 1, N, UpdatedMap).

process_i(I, _K, N, DistMap) when I >= N -> DistMap;
process_i(I, K, N, DistMap) ->
    UpdatedMap = process_j(0, I, K, N, DistMap),
    process_i(I + 1, K, N, UpdatedMap).

process_j(J, _I, _K, N, DistMap) when J >= N -> DistMap;
process_j(J, I, K, N, DistMap) ->
    D_ik = maps:get({I,K}, DistMap),
    D_kj = maps:get({K,J}, DistMap),
    Sum  = D_ik + D_kj,
    Old  = maps:get({I,J}, DistMap),
    NewMap = if Sum < Old -> maps:put({I,J}, Sum, DistMap); true -> DistMap end,
    process_j(J + 1, I, K, N, NewMap).

%% Determine the city with minimal reachable count (tie → larger index)
best_city(I, _N, _DistMap, _Thresh, BestCity, _BestCount) when I < 0 -> BestCity; % unreachable case
best_city(I, N, DistMap, Thresh, BestCity, BestCount) when I >= N ->
    BestCity;
best_city(I, N, DistMap, Thresh, BestCity, BestCount) ->
    Count = count_reachable(I, N, DistMap, Thresh),
    {NewBestCity, NewBestCount} =
        if
            Count < BestCount orelse (Count == BestCount andalso I > BestCity) ->
                {I, Count};
            true -> {BestCity, BestCount}
        end,
    best_city(I + 1, N, DistMap, Thresh, NewBestCity, NewBestCount).

count_reachable(I, N, DistMap, Thresh) ->
    lists:foldl(fun(J, Acc) ->
        if
            I =/= J,
            maps:get({I,J}, DistMap) =< Thresh -> Acc + 1;
            true -> Acc
        end
    end, 0, lists:seq(0, N-1)).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_the_city(n :: integer, edges :: [[integer]], distance_threshold :: integer) :: integer
  def find_the_city(n, edges, distance_threshold) do
    inf = 1_000_000_000

    # Initialize distance matrix with INF and zero diagonal
    rows =
      Enum.map(0..(n - 1), fn i ->
        row = :array.new(n, default: inf)
        row = :array.set(i, 0, row)
        row
      end)

    matrix = :array.from_list(rows)

    # Set edge distances (undirected)
    matrix =
      Enum.reduce(edges, matrix, fn [u, v, w], mat ->
        row_u = :array.get(u, mat) |> :array.set(v, w)
        mat = :array.set(u, row_u, mat)

        row_v = :array.get(v, mat) |> :array.set(u, w)
        :array.set(v, row_v, mat)
      end)

    # Floyd‑Warshall
    matrix =
      Enum.reduce(0..(n - 1), matrix, fn k, mat_k ->
        Enum.reduce(0..(n - 1), mat_k, fn i, mat_i ->
          dik = :array.get(i, mat_i) |> :array.get(k)

          if dik == inf do
            mat_i
          else
            Enum.reduce(0..(n - 1), mat_i, fn j, mat_j ->
              dkj = :array.get(k, mat_j) |> :array.get(j)
              dij = :array.get(i, mat_j) |> :array.get(j)

              new_dist = dik + dkj

              if new_dist < dij do
                row_i = :array.get(i, mat_j) |> :array.set(j, new_dist)
                :array.set(i, row_i, mat_j)
              else
                mat_j
              end
            end)
          end
        end)
      end)

    # Find city with minimal reachable count (excluding itself), tie‑break by larger index
    {best_city, _} =
      Enum.reduce(0..(n - 1), {-1, n + 1}, fn i, {ans, min_cnt} ->
        cnt =
          Enum.reduce(0..(n - 1), 0, fn j, acc ->
            if i != j do
              d = :array.get(i, matrix) |> :array.get(j)

              if d <= distance_threshold do
                acc + 1
              else
                acc
              end
            else
              acc
            end
          end)

        cond do
          cnt < min_cnt -> {i, cnt}
          cnt == min_cnt and i > ans -> {i, cnt}
          true -> {ans, min_cnt}
        end
      end)

    best_city
  end
end
```

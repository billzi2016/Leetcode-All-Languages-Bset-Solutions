# 0787. Cheapest Flights Within K Stops

## Cpp

```cpp
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        const long long INF = 1e18;
        vector<long long> dist(n, INF);
        dist[src] = 0;
        for (int i = 0; i <= k; ++i) {
            vector<long long> tmp(dist);
            for (const auto& f : flights) {
                int u = f[0], v = f[1];
                int w = f[2];
                if (dist[u] == INF) continue;
                if (dist[u] + w < tmp[v]) {
                    tmp[v] = dist[u] + w;
                }
            }
            dist.swap(tmp);
        }
        return dist[dst] == INF ? -1 : static_cast<int>(dist[dst]);
    }
};
```

## Java

```java
class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        final int INF = Integer.MAX_VALUE / 2;
        int[] dist = new int[n];
        for (int i = 0; i < n; i++) dist[i] = INF;
        dist[src] = 0;

        // Perform Bellman-Ford up to k+1 edges
        for (int i = 0; i <= k; i++) {
            int[] curDist = dist.clone();
            for (int[] f : flights) {
                int u = f[0], v = f[1], w = f[2];
                if (dist[u] != INF && dist[u] + w < curDist[v]) {
                    curDist[v] = dist[u] + w;
                }
            }
            dist = curDist;
        }

        return dist[dst] == INF ? -1 : dist[dst];
    }
}
```

## Python

```python
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0
        for _ in range(k + 1):
            tmp = dist[:]
            for u, v, w in flights:
                if dist[u] == INF:
                    continue
                if dist[u] + w < tmp[v]:
                    tmp[v] = dist[u] + w
            dist = tmp
        return -1 if dist[dst] == INF else dist[dst]
```

## Python3

```python
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 10 ** 9
        dist = [INF] * n
        dist[src] = 0
        for _ in range(k + 1):
            tmp = dist[:]
            for u, v, w in flights:
                if dist[u] == INF:
                    continue
                if dist[u] + w < tmp[v]:
                    tmp[v] = dist[u] + w
            dist = tmp
        return -1 if dist[dst] == INF else dist[dst]
```

## C

```c
#include <stdlib.h>
#include <string.h>

int findCheapestPrice(int n, int** flights, int flightsSize, int* flightsColSize,
                      int src, int dst, int k) {
    const int INF = 1000000000;
    int *prev = (int *)malloc(n * sizeof(int));
    int *cur  = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; ++i) prev[i] = INF;
    prev[src] = 0;

    for (int i = 0; i <= k; ++i) {
        memcpy(cur, prev, n * sizeof(int));
        for (int j = 0; j < flightsSize; ++j) {
            int u = flights[j][0];
            int v = flights[j][1];
            int w = flights[j][2];
            if (prev[u] == INF) continue;
            if (prev[u] + w < cur[v]) cur[v] = prev[u] + w;
        }
        int *tmp = prev;
        prev = cur;
        cur = tmp;
    }

    int ans = prev[dst];
    free(prev);
    free(cur);
    return ans == INF ? -1 : ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindCheapestPrice(int n, int[][] flights, int src, int dst, int k)
    {
        const int INF = int.MaxValue / 2;
        var dist = new int[n];
        for (int i = 0; i < n; i++) dist[i] = INF;
        dist[src] = 0;

        // Perform Bellman-Ford relaxation up to k+1 edges
        for (int i = 0; i <= k; i++)
        {
            var temp = (int[])dist.Clone();
            foreach (var f in flights)
            {
                int u = f[0], v = f[1], w = f[2];
                if (dist[u] == INF) continue;
                if (dist[u] + w < temp[v])
                    temp[v] = dist[u] + w;
            }
            dist = temp;
        }

        return dist[dst] == INF ? -1 : dist[dst];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
var findCheapestPrice = function(n, flights, src, dst, k) {
    const INF = Number.MAX_SAFE_INTEGER;
    let dist = new Array(n).fill(INF);
    dist[src] = 0;
    for (let i = 0; i <= k; i++) {
        const temp = dist.slice();
        for (const [u, v, w] of flights) {
            if (dist[u] === INF) continue;
            const newCost = dist[u] + w;
            if (newCost < temp[v]) {
                temp[v] = newCost;
            }
        }
        dist = temp;
    }
    return dist[dst] === INF ? -1 : dist[dst];
};
```

## Typescript

```typescript
function findCheapestPrice(n: number, flights: number[][], src: number, dst: number, k: number): number {
    const INF = Number.MAX_SAFE_INTEGER;
    let dist: number[] = new Array(n).fill(INF);
    dist[src] = 0;

    for (let i = 0; i <= k; i++) {
        const temp = dist.slice();
        for (const [u, v, w] of flights) {
            if (dist[u] === INF) continue;
            const newCost = dist[u] + w;
            if (newCost < temp[v]) {
                temp[v] = newCost;
            }
        }
        dist = temp;
    }

    return dist[dst] === INF ? -1 : dist[dst];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $flights
     * @param Integer $src
     * @param Integer $dst
     * @param Integer $k
     * @return Integer
     */
    function findCheapestPrice($n, $flights, $src, $dst, $k) {
        $INF = PHP_INT_MAX;
        $dist = array_fill(0, $n, $INF);
        $dist[$src] = 0;

        for ($i = 0; $i <= $k; $i++) {
            $temp = $dist;
            foreach ($flights as $flight) {
                $u = $flight[0];
                $v = $flight[1];
                $w = $flight[2];
                if ($dist[$u] !== $INF && $dist[$u] + $w < $temp[$v]) {
                    $temp[$v] = $dist[$u] + $w;
                }
            }
            $dist = $temp;
        }

        return $dist[$dst] === $INF ? -1 : $dist[$dst];
    }
}
```

## Swift

```swift
class Solution {
    func findCheapestPrice(_ n: Int, _ flights: [[Int]], _ src: Int, _ dst: Int, _ k: Int) -> Int {
        var graph = Array(repeating: [(to: Int, price: Int)](), count: n)
        for f in flights {
            let from = f[0], to = f[1], price = f[2]
            graph[from].append((to, price))
        }
        
        struct PriorityQueue {
            var heap: [(Int, Int, Int)] = [] // (cost, node, stopsRemaining)
            
            mutating func push(_ item: (Int, Int, Int)) {
                heap.append(item)
                siftUp(heap.count - 1)
            }
            
            mutating func pop() -> (Int, Int, Int)? {
                guard !heap.isEmpty else { return nil }
                let top = heap[0]
                let last = heap.removeLast()
                if !heap.isEmpty {
                    heap[0] = last
                    siftDown(0)
                }
                return top
            }
            
            private mutating func siftUp(_ index: Int) {
                var child = index
                while child > 0 {
                    let parent = (child - 1) / 2
                    if heap[child].0 < heap[parent].0 {
                        heap.swapAt(child, parent)
                        child = parent
                    } else { break }
                }
            }
            
            private mutating func siftDown(_ index: Int) {
                var parent = index
                while true {
                    let left = parent * 2 + 1
                    let right = left + 1
                    var smallest = parent
                    if left < heap.count && heap[left].0 < heap[smallest].0 { smallest = left }
                    if right < heap.count && heap[right].0 < heap[smallest].0 { smallest = right }
                    if smallest == parent { break }
                    heap.swapAt(parent, smallest)
                    parent = smallest
                }
            }
        }
        
        var pq = PriorityQueue()
        pq.push((0, src, k + 1)) // stopsRemaining includes the final flight
        
        while let (cost, node, stops) = pq.pop() {
            if node == dst { return cost }
            if stops > 0 {
                for edge in graph[node] {
                    pq.push((cost + edge.price, edge.to, stops - 1))
                }
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findCheapestPrice(n: Int, flights: Array<IntArray>, src: Int, dst: Int, k: Int): Int {
        val INF = 1_000_000_007
        var dist = IntArray(n) { INF }
        dist[src] = 0
        for (i in 0..k) {
            val prev = dist.clone()
            for (f in flights) {
                val u = f[0]
                val v = f[1]
                val w = f[2]
                if (prev[u] == INF) continue
                val newCost = prev[u] + w
                if (newCost < dist[v]) {
                    dist[v] = newCost
                }
            }
        }
        return if (dist[dst] == INF) -1 else dist[dst]
    }
}
```

## Dart

```dart
class Solution {
  int findCheapestPrice(int n, List<List<int>> flights, int src, int dst, int k) {
    const int INF = 1 << 60;
    List<int> dist = List.filled(n, INF);
    dist[src] = 0;

    for (int i = 0; i <= k; i++) {
      List<int> temp = List.from(dist);
      for (var f in flights) {
        int u = f[0];
        int v = f[1];
        int w = f[2];
        if (dist[u] == INF) continue;
        int newCost = dist[u] + w;
        if (newCost < temp[v]) {
          temp[v] = newCost;
        }
      }
      dist = temp;
    }

    return dist[dst] == INF ? -1 : dist[dst];
  }
}
```

## Golang

```go
func findCheapestPrice(n int, flights [][]int, src int, dst int, k int) int {
	const INF = int(1e9)
	dist := make([]int, n)
	for i := 0; i < n; i++ {
		dist[i] = INF
	}
	dist[src] = 0

	for i := 0; i <= k; i++ {
		tmp := make([]int, n)
		copy(tmp, dist)
		for _, f := range flights {
			u, v, w := f[0], f[1], f[2]
			if dist[u] == INF {
				continue
			}
			if nd := dist[u] + w; nd < tmp[v] {
				tmp[v] = nd
			}
		}
		dist = tmp
	}

	if dist[dst] == INF {
		return -1
	}
	return dist[dst]
}
```

## Ruby

```ruby
def find_cheapest_price(n, flights, src, dst, k)
  inf = Float::INFINITY
  dist = Array.new(n, inf)
  dist[src] = 0

  (0..k).each do
    temp = dist.clone
    flights.each do |f|
      u, v, w = f
      next if dist[u] == inf
      cost = dist[u] + w
      temp[v] = cost if cost < temp[v]
    end
    dist = temp
  end

  ans = dist[dst]
  ans == inf ? -1 : ans.to_i
end
```

## Scala

```scala
object Solution {
    def findCheapestPrice(n: Int, flights: Array[Array[Int]], src: Int, dst: Int, k: Int): Int = {
        val INF = Int.MaxValue / 2
        var dist = Array.fill(n)(INF)
        dist(src) = 0

        for (_ <- 0 to k) {
            val prev = dist.clone()
            for (f <- flights) {
                val u = f(0)
                val v = f(1)
                val w = f(2)
                if (prev(u) != INF && prev(u) + w < dist(v)) {
                    dist(v) = prev(u) + w
                }
            }
        }

        if (dist(dst) == INF) -1 else dist(dst)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
        let n_usize = n as usize;
        const INF: i32 = 1_000_000_000;
        let mut dist = vec![INF; n_usize];
        dist[src as usize] = 0;

        for _ in 0..=k {
            let mut temp = dist.clone();
            for f in &flights {
                let u = f[0] as usize;
                let v = f[1] as usize;
                let w = f[2];
                if dist[u] != INF && dist[u] + w < temp[v] {
                    temp[v] = dist[u] + w;
                }
            }
            dist = temp;
        }

        if dist[dst as usize] == INF { -1 } else { dist[dst as usize] }
    }
}
```

## Racket

```racket
(require racket/vector)

(define INF 1000000000)

(define/contract (find-cheapest-price n flights src dst k)
  (-> exact-integer?
      (listof (listof exact-integer?))
      exact-integer?
      exact-integer?
      exact-integer?
      exact-integer?)
  (let loop ((i 0)
             (dist (let ([v (make-vector n INF)])
                     (vector-set! v src 0)
                     v)))
    (if (> i k)
        (let ([ans (vector-ref dist dst)])
          (if (= ans INF) -1 ans))
        (let* ([new-dist (vector-copy dist)])
          (for-each
           (lambda (flight)
             (define u (list-ref flight 0))
             (define v (list-ref flight 1))
             (define w (list-ref flight 2))
             (when (< (vector-ref dist u) INF)
               (let ([cand (+ (vector-ref dist u) w)])
                 (when (< cand (vector-ref new-dist v))
                   (vector-set! new-dist v cand)))))
           flights)
          (loop (+ i 1) new-dist)))))
```

## Erlang

```erlang
-spec find_cheapest_price(N :: integer(), Flights :: [[integer()]], Src :: integer(), Dst :: integer(), K :: integer()) -> integer().
find_cheapest_price(N, Flights, Src, Dst, K) ->
    Inf = 1 bsl 60,
    InitDist = erlang:make_tuple(N, Inf),
    Dist0 = setelement(Src + 1, InitDist, 0),
    FinalDist = loop(K + 1, Dist0, Flights, Inf),
    Res = element(Dst + 1, FinalDist),
    case Res of
        X when X >= Inf -> -1;
        _ -> Res
    end.

%% Perform Bellman‑Ford relaxation K+1 times (allow up to K stops)
-spec loop(Rem :: integer(), PrevDist :: tuple(), Flights :: [[integer()]], Inf :: integer()) -> tuple().
loop(0, Dist, _Flights, _Inf) ->
    Dist;
loop(Rem, PrevDist, Flights, Inf) ->
    NewDist = relax_edges(Flights, PrevDist, Inf),
    loop(Rem - 1, NewDist, Flights, Inf).

%% Relax all edges using distances from the previous iteration only
-spec relax_edges(Flights :: [[integer()]], PrevDist :: tuple(), Inf :: integer()) -> tuple().
relax_edges(Flights, PrevDist, Inf) ->
    lists:foldl(
        fun([U, V, W], Acc) ->
            CostU = element(U + 1, PrevDist),
            if
                CostU == Inf ->
                    Acc;
                true ->
                    NewCost = CostU + W,
                    OldV = element(V + 1, Acc),
                    if NewCost < OldV ->
                        setelement(V + 1, Acc, NewCost);
                       true ->
                        Acc
                    end
            end
        end,
        PrevDist,
        Flights
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_cheapest_price(n :: integer, flights :: [[integer]], src :: integer, dst :: integer, k :: integer) :: integer
  def find_cheapest_price(n, flights, src, dst, k) do
    inf = 1_000_000_000
    init_dist = List.duplicate(inf, n)
    init_dist = List.replace_at(init_dist, src, 0)

    final_dist =
      Enum.reduce(0..k, init_dist, fn _, dist ->
        prev = dist

        Enum.reduce(flights, dist, fn [u, v, w], acc ->
          cost_u = Enum.at(prev, u)

          if cost_u != inf do
            new_cost = cost_u + w
            cur_v = Enum.at(acc, v)

            if new_cost < cur_v do
              List.replace_at(acc, v, new_cost)
            else
              acc
            end
          else
            acc
          end
        end)
      end)

    ans = Enum.at(final_dist, dst)

    if ans == inf, do: -1, else: ans
  end
end
```

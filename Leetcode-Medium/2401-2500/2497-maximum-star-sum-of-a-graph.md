# 2497. Maximum Star Sum of a Graph

## Cpp

```cpp
class Solution {
public:
    int maxStarSum(vector<int>& vals, vector<vector<int>>& edges, int k) {
        int n = vals.size();
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        long long best = LLONG_MIN;
        for (int i = 0; i < n; ++i) {
            vector<int> posVals;
            posVals.reserve(adj[i].size());
            for (int nb : adj[i]) {
                if (vals[nb] > 0) posVals.push_back(vals[nb]);
            }
            sort(posVals.begin(), posVals.end(), greater<int>());
            long long cur = vals[i];
            int limit = min(k, (int)posVals.size());
            for (int j = 0; j < limit; ++j) {
                cur += posVals[j];
            }
            if (cur > best) best = cur;
        }
        return (int)best;
    }
};
```

## Java

```java
class Solution {
    public int maxStarSum(int[] vals, int[][] edges, int k) {
        int n = vals.length;
        @SuppressWarnings("unchecked")
        java.util.ArrayList<Integer>[] adj = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new java.util.ArrayList<>();
        }
        for (int[] e : edges) {
            int a = e[0], b = e[1];
            adj[a].add(vals[b]);
            adj[b].add(vals[a]);
        }

        long best = Long.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            java.util.ArrayList<Integer> list = adj[i];
            if (!list.isEmpty()) {
                list.sort(java.util.Collections.reverseOrder());
                long sum = vals[i];
                int limit = Math.min(k, list.size());
                for (int j = 0; j < limit; j++) {
                    int v = list.get(j);
                    if (v > 0) {
                        sum += v;
                    } else {
                        break;
                    }
                }
                if (sum > best) best = sum;
            } else {
                // isolated node
                long sum = vals[i];
                if (sum > best) best = sum;
            }
        }
        return (int) best;
    }
}
```

## Python

```python
class Solution(object):
    def maxStarSum(self, vals, edges, k):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(vals)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(vals[b])
            adj[b].append(vals[a])

        best = max(vals)  # at least one node alone
        if k == 0:
            return best

        for i in range(n):
            if not adj[i]:
                continue
            neighbors = adj[i]
            neighbors.sort(reverse=True)
            add = 0
            cnt = 0
            for v in neighbors:
                if cnt >= k or v <= 0:
                    break
                add += v
                cnt += 1
            best = max(best, vals[i] + add)

        return best
```

## Python3

```python
from typing import List

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        best = -10**15
        for i in range(n):
            neighbor_vals = [vals[j] for j in adj[i]]
            neighbor_vals.sort(reverse=True)

            cur_sum = vals[i]
            taken = 0
            for val in neighbor_vals:
                if taken == k or val <= 0:
                    break
                cur_sum += val
                taken += 1

            best = max(best, cur_sum)
        return best
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmp_desc(const void *a, const void *b) {
    return (*(int *)b) - (*(int *)a);
}

int maxStarSum(int* vals, int valsSize, int** edges, int edgesSize, int* edgesColSize, int k) {
    if (valsSize == 0) return 0;
    
    int *deg = calloc(valsSize, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        deg[u]++; deg[v]++;
    }
    
    int **adj = malloc(valsSize * sizeof(int *));
    for (int i = 0; i < valsSize; ++i) {
        adj[i] = malloc(deg[i] * sizeof(int));
    }
    
    int *cur = calloc(valsSize, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u][cur[u]++] = v;
        adj[v][cur[v]++] = u;
    }
    free(cur);
    
    long long best = LLONG_MIN;
    
    for (int i = 0; i < valsSize; ++i) {
        long long sum = vals[i];
        int d = deg[i];
        if (k > 0 && d > 0) {
            int *tmp = malloc(d * sizeof(int));
            int cnt = 0;
            for (int j = 0; j < d; ++j) {
                int nb = adj[i][j];
                if (vals[nb] > 0) tmp[cnt++] = vals[nb];
            }
            if (cnt > 0) {
                qsort(tmp, cnt, sizeof(int), cmp_desc);
                int take = k < cnt ? k : cnt;
                for (int t = 0; t < take; ++t) sum += tmp[t];
            }
            free(tmp);
        }
        if (sum > best) best = sum;
    }
    
    for (int i = 0; i < valsSize; ++i) {
        free(adj[i]);
    }
    free(adj);
    free(deg);
    
    return (int)best;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxStarSum(int[] vals, int[][] edges, int k) {
        int n = vals.Length;
        var adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            adj[a].Add(b);
            adj[b].Add(a);
        }

        int maxSum = int.MinValue;
        for (int i = 0; i < n; i++) {
            var neighbors = adj[i];
            if (neighbors.Count > 0) {
                neighbors.Sort((x, y) => vals[y].CompareTo(vals[x])); // sort by neighbor value descending
            }
            int cur = vals[i];
            int taken = 0;
            foreach (int nb in neighbors) {
                if (taken == k) break;
                int v = vals[nb];
                if (v <= 0) break; // no benefit adding non‑positive values
                cur += v;
                taken++;
            }
            if (cur > maxSum) maxSum = cur;
        }
        return maxSum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} vals
 * @param {number[][]} edges
 * @param {number} k
 * @return {number}
 */
var maxStarSum = function(vals, edges, k) {
    const n = vals.length;
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(vals[v]);
        adj[v].push(vals[u]);
    }
    let ans = -Infinity;
    for (let i = 0; i < n; ++i) {
        const neighbors = adj[i];
        if (neighbors.length === 0) {
            ans = Math.max(ans, vals[i]);
            continue;
        }
        neighbors.sort((a, b) => b - a);
        let sum = vals[i];
        const limit = Math.min(k, neighbors.length);
        for (let j = 0; j < limit; ++j) {
            if (neighbors[j] > 0) sum += neighbors[j];
            else break;
        }
        ans = Math.max(ans, sum);
    }
    return ans;
};
```

## Typescript

```typescript
function maxStarSum(vals: number[], edges: number[][], k: number): number {
    const n = vals.length;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    let best = -Infinity;
    for (let i = 0; i < n; ++i) {
        const neighborVals = adj[i].map(j => vals[j]);
        neighborVals.sort((a, b) => b - a);
        let sum = vals[i];
        const limit = Math.min(k, neighborVals.length);
        for (let t = 0; t < limit; ++t) {
            if (neighborVals[t] > 0) sum += neighborVals[t];
            else break;
        }
        if (sum > best) best = sum;
    }
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $vals
     * @param Integer[][] $edges
     * @param Integer $k
     * @return Integer
     */
    function maxStarSum($vals, $edges, $k) {
        $n = count($vals);
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            $adj[$a][] = $b;
            $adj[$b][] = $a;
        }

        // At least one node alone can be chosen
        $maxSum = PHP_INT_MIN;
        foreach ($vals as $v) {
            if ($v > $maxSum) $maxSum = $v;
        }

        for ($i = 0; $i < $n; ++$i) {
            $posVals = [];
            foreach ($adj[$i] as $nbr) {
                $val = $vals[$nbr];
                if ($val > 0) {
                    $posVals[] = $val;
                }
            }
            if (empty($posVals)) continue;

            rsort($posVals); // descending
            $sum = $vals[$i];
            $limit = min($k, count($posVals));
            for ($j = 0; $j < $limit; ++$j) {
                $sum += $posVals[$j];
            }
            if ($sum > $maxSum) $maxSum = $sum;
        }

        return $maxSum;
    }
}
```

## Swift

```swift
class Solution {
    func maxStarSum(_ vals: [Int], _ edges: [[Int]], _ k: Int) -> Int {
        let n = vals.count
        var adj = [[Int]](repeating: [], count: n)
        for e in edges {
            let u = e[0]
            let v = e[1]
            adj[u].append(v)
            adj[v].append(u)
        }
        
        var result = Int.min
        
        for i in 0..<n {
            var neighborVals = [Int]()
            neighborVals.reserveCapacity(adj[i].count)
            for nb in adj[i] {
                neighborVals.append(vals[nb])
            }
            if !neighborVals.isEmpty {
                neighborVals.sort(by: >)
                var sum = vals[i]
                var taken = 0
                for v in neighborVals {
                    if taken >= k { break }
                    if v <= 0 { break } // further values are not beneficial
                    sum += v
                    taken += 1
                }
                result = max(result, sum)
            } else {
                result = max(result, vals[i])
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxStarSum(vals: IntArray, edges: Array<IntArray>, k: Int): Int {
        val n = vals.size
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }
        var answer = Int.MIN_VALUE
        for (i in 0 until n) {
            var sum = vals[i]
            if (k > 0 && adj[i].isNotEmpty()) {
                val posVals = mutableListOf<Int>()
                for (nb in adj[i]) {
                    val v = vals[nb]
                    if (v > 0) posVals.add(v)
                }
                if (posVals.isNotEmpty()) {
                    posVals.sortDescending()
                    var cnt = 0
                    while (cnt < k && cnt < posVals.size) {
                        sum += posVals[cnt]
                        cnt++
                    }
                }
            }
            if (sum > answer) answer = sum
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maxStarSum(List<int> vals, List<List<int>> edges, int k) {
    int n = vals.length;
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int a = e[0];
      int b = e[1];
      adj[a].add(b);
      adj[b].add(a);
    }
    int ans = -9223372036854775808; // sufficiently small
    for (int i = 0; i < n; ++i) {
      List<int> neighborVals = [];
      for (int nb in adj[i]) {
        neighborVals.add(vals[nb]);
      }
      neighborVals.sort((a, b) => b.compareTo(a)); // descending order
      int sum = vals[i];
      int limit = k < neighborVals.length ? k : neighborVals.length;
      for (int j = 0; j < limit; ++j) {
        if (neighborVals[j] > 0) {
          sum += neighborVals[j];
        } else {
          break;
        }
      }
      if (sum > ans) ans = sum;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

func maxStarSum(vals []int, edges [][]int, k int) int {
	n := len(vals)
	adj := make([][]int, n)
	for _, e := range edges {
		a, b := e[0], e[1]
		adj[a] = append(adj[a], b)
		adj[b] = append(adj[b], a)
	}

	const infNeg = -1 << 60
	ans := infNeg

	for i := 0; i < n; i++ {
		neighbors := adj[i]
		if len(neighbors) == 0 || k == 0 {
			if vals[i] > ans {
				ans = vals[i]
			}
			continue
		}

		valsNei := make([]int, len(neighbors))
		for idx, nb := range neighbors {
			valsNei[idx] = vals[nb]
		}
		sort.Slice(valsNei, func(a, b int) bool { return valsNei[a] > valsNei[b] })

		sum := vals[i]
		cnt := 0
		for _, v := range valsNei {
			if cnt >= k || v <= 0 {
				break
			}
			sum += v
			cnt++
		}
		if sum > ans {
			ans = sum
		}
	}

	return ans
}
```

## Ruby

```ruby
def max_star_sum(vals, edges, k)
  n = vals.length
  adj = Array.new(n) { [] }
  edges.each do |a, b|
    adj[a] << b
    adj[b] << a
  end

  max_sum = -(1 << 60)

  n.times do |i|
    neighbor_vals = adj[i].map { |nbr| vals[nbr] }
    neighbor_vals.sort!.reverse!
    cur = vals[i]
    cnt = 0
    neighbor_vals.each do |v|
      break if cnt == k || v <= 0
      cur += v
      cnt += 1
    end
    max_sum = cur if cur > max_sum
  end

  max_sum
end
```

## Scala

```scala
object Solution {
    def maxStarSum(vals: Array[Int], edges: Array[Array[Int]], k: Int): Int = {
        val n = vals.length
        val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
        var eIdx = 0
        while (eIdx < edges.length) {
            val a = edges(eIdx)(0)
            val b = edges(eIdx)(1)
            adj(a).append(b)
            adj(b).append(a)
            eIdx += 1
        }

        var best: Long = Long.MinValue
        var node = 0
        while (node < n) {
            val neighbors = adj(node)
            if (neighbors.isEmpty || k == 0) {
                best = math.max(best, vals(node).toLong)
            } else {
                val arr = new Array[Int](neighbors.length)
                var i = 0
                while (i < neighbors.length) {
                    arr(i) = vals(neighbors(i))
                    i += 1
                }
                java.util.Arrays.sort(arr) // ascending
                var sum: Long = vals(node).toLong
                var taken = 0
                var idx = arr.length - 1
                while (taken < k && idx >= 0 && arr(idx) > 0) {
                    sum += arr(idx)
                    taken += 1
                    idx -= 1
                }
                best = math.max(best, sum)
            }
            node += 1
        }

        best.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_star_sum(vals: Vec<i32>, edges: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = vals.len();
        let mut adj: Vec<Vec<i32>> = vec![Vec::new(); n];
        for e in edges.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(vals[b]);
            adj[b].push(vals[a]);
        }
        let k_usize = k as usize;
        let mut ans = i32::MIN;
        for i in 0..n {
            let neigh = &mut adj[i];
            neigh.sort_unstable_by(|a, b| b.cmp(a));
            let mut sum = vals[i];
            let limit = std::cmp::min(k_usize, neigh.len());
            for j in 0..limit {
                if neigh[j] > 0 {
                    sum += neigh[j];
                } else {
                    break;
                }
            }
            if sum > ans {
                ans = sum;
            }
        }
        ans
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (max-star-sum vals edges k)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((n (length vals))
         (val-vec (list->vector vals))
         (adj (make-vector n '())))
    ;; build adjacency lists
    (for-each
     (lambda (e)
       (define a (first e))
       (define b (second e))
       (vector-set! adj a (cons b (vector-ref adj a)))
       (vector-set! adj b (cons a (vector-ref adj b))))
     edges)
    ;; compute maximum star sum
    (let ((max-sum (vector-ref val-vec 0))) ; n >= 1 per constraints
      (for ([i (in-range n)])
        (define center-val (vector-ref val-vec i))
        (define neighbor-indices (vector-ref adj i))
        (define neighbor-vals
          (map (lambda (nbr) (vector-ref val-vec nbr)) neighbor-indices))
        (define pos-neighbor-vals (filter (lambda (v) (> v 0)) neighbor-vals))
        (define sorted-pos (sort pos-neighbor-vals >))
        (define take-count (min k (length sorted-pos)))
        (define sum-top
          (for/sum ([v (in-list (take sorted-pos take-count))]) v))
        (define total (+ center-val sum-top))
        (when (> total max-sum)
          (set! max-sum total)))
      max-sum)))
```

## Erlang

```erlang
-module(solution).
-export([max_star_sum/3]).

-spec max_star_sum(Vals :: [integer()], Edges :: [[integer()]], K :: integer()) -> integer().
max_star_sum(Vals, Edges, K) ->
    ValsTuple = list_to_tuple(Vals),
    AdjMap = build_adj_map(Edges, ValsTuple, #{}),
    N = tuple_size(ValsTuple),
    max_star_sum_loop(0, N - 1, ValsTuple, AdjMap, K, -1000000000).

build_adj_map([], _, Map) -> Map;
build_adj_map([[A, B] | Rest], ValsT, Map) ->
    ValB = element(B + 1, ValsT),
    Map1 = maps:update_with(
        A,
        fun(L) -> [ValB | L] end,
        [ValB],
        Map
    ),
    ValA = element(A + 1, ValsT),
    Map2 = maps:update_with(
        B,
        fun(L) -> [ValA | L] end,
        [ValA],
        Map1
    ),
    build_adj_map(Rest, ValsT, Map2).

max_star_sum_loop(I, MaxIdx, _, _, _, MaxAcc) when I > MaxIdx ->
    MaxAcc;
max_star_sum_loop(I, MaxIdx, ValsT, AdjMap, K, MaxAcc) ->
    Center = element(I + 1, ValsT),
    NeighVals = maps:get(I, AdjMap, []),
    Sorted = lists:sort(fun(A, B) -> A > B end, NeighVals),
    SumNeigh = sum_top_k(Sorted, K, 0),
    Total = Center + SumNeigh,
    NewMax = if Total > MaxAcc -> Total; true -> MaxAcc end,
    max_star_sum_loop(I + 1, MaxIdx, ValsT, AdjMap, K, NewMax).

sum_top_k([], _, Acc) -> Acc;
sum_top_k(_, 0, Acc) -> Acc;
sum_top_k([H | T], K, Acc) when H > 0 ->
    sum_top_k(T, K - 1, Acc + H);
sum_top_k(_, _, Acc) -> Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_star_sum(vals :: [integer], edges :: [[integer]], k :: integer) :: integer
  def max_star_sum(vals, edges, k) do
    n = length(vals)
    vals_t = List.to_tuple(vals)

    adj =
      Enum.reduce(edges, %{}, fn [a, b], acc ->
        acc
        |> Map.update(a, [b], &[b | &1])
        |> Map.update(b, [a], &[a | &1])
      end)

    # start with the smallest possible value (vals[i] >= -10^4)
    init_max = -1_000_000_000

    Enum.reduce(0..(n - 1), init_max, fn i, cur_max ->
      neighbor_ids = Map.get(adj, i, [])

      neighbor_vals =
        neighbor_ids
        |> Enum.map(fn nb -> elem(vals_t, nb) end)
        |> Enum.sort(&>=/2)

      add_sum =
        neighbor_vals
        |> Enum.take(k)
        |> Enum.reduce(0, fn v, acc -> if v > 0, do: acc + v, else: acc end)

      total = elem(vals_t, i) + add_sum
      max(cur_max, total)
    end)
  end
end
```

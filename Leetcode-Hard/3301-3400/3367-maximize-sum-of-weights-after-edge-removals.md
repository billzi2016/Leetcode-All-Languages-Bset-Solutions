# 3367. Maximize Sum of Weights after Edge Removals

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maximizeSumOfWeights(vector<vector<int>>& edges, int k) {
        // Since all edge weights are positive, removing any edge can only decrease the total sum.
        // Therefore, the maximum possible sum is simply the sum of all edge weights,
        // regardless of the value of k (as we may choose to remove zero edges).
        long long total = 0;
        for (const auto& e : edges) total += e[2];
        return total;
    }
};
```

## Java

```java
class Solution {
    public long maximizeSumOfWeights(int[][] edges, int k) {
        int m = edges.length;
        long total = 0L;
        int[] weights = new int[m];
        for (int i = 0; i < m; i++) {
            int w = edges[i][2];
            weights[i] = w;
            total += w;
        }
        java.util.Arrays.sort(weights);
        int cuts = k - 1;
        long removed = 0L;
        for (int i = 0; i < cuts && i < m; i++) {
            removed += weights[i];
        }
        return total - removed;
    }
}
```

## Python

```python
class Solution(object):
    def maximizeSumOfWeights(self, edges, k):
        """
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        total = 0
        weights = []
        for u, v, w in edges:
            total += w
            weights.append(w)
        # To obtain k components we need to remove (k-1) edges.
        # Removing the smallest weights yields maximal remaining sum.
        if k > 1:
            weights.sort()
            remove_sum = sum(weights[:k - 1])
            return total - remove_sum
        else:
            return total
```

## Python3

```python
class Solution:
    def maximizeSumOfWeights(self, edges, k):
        """
        Remove exactly k edges with the smallest weights to maximize the sum of remaining edge weights.
        """
        total = 0
        weights = []
        for u, v, w in edges:
            total += w
            weights.append(w)
        if k <= 0:
            return total
        weights.sort()
        remove_sum = sum(weights[:k])
        return total - remove_sum
```

## C

```c
#include <stdlib.h>

static int cmpInt(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

long long maximizeSumOfWeights(int** edges, int edgesSize, int* edgesColSize, int k) {
    (void)edgesColSize; // unused
    if (edgesSize == 0) return 0;
    
    long long total = 0;
    int *weights = (int *)malloc(sizeof(int) * edgesSize);
    for (int i = 0; i < edgesSize; ++i) {
        int w = edges[i][2];
        weights[i] = w;
        total += w;
    }
    
    if (k > 1) {
        qsort(weights, edgesSize, sizeof(int), cmpInt);
        long long removeSum = 0;
        int cuts = k - 1;
        if (cuts > edgesSize) cuts = edgesSize;
        for (int i = 0; i < cuts; ++i) {
            removeSum += weights[i];
        }
        total -= removeSum;
    }
    
    free(weights);
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public long MaximizeSumOfWeights(int[][] edges, int k) {
        long total = 0;
        foreach (var e in edges) {
            total += e[2];
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @param {number} k
 * @return {number}
 */
var maximizeSumOfWeights = function(edges, k) {
    // Total sum of all edge weights
    let total = 0;
    const weights = new Array(edges.length);
    for (let i = 0; i < edges.length; ++i) {
        const w = edges[i][2];
        total += w;
        weights[i] = w;
    }
    // Need to remove exactly k-1 edges to obtain k components
    const removals = k - 1;
    if (removals <= 0) return total;
    // Find sum of the smallest `removals` weights
    weights.sort((a, b) => a - b);
    let removedSum = 0;
    for (let i = 0; i < removals && i < weights.length; ++i) {
        removedSum += weights[i];
    }
    return total - removedSum;
};
```

## Typescript

```typescript
function maximizeSumOfWeights(edges: number[][], k: number): number {
    const total = edges.reduce((sum, e) => sum + e[2], 0);
    if (k <= 1) return total;
    const weights = edges.map(e => e[2]);
    weights.sort((a, b) => a - b);
    let removeSum = 0;
    for (let i = 0; i < k - 1 && i < weights.length; i++) {
        removeSum += weights[i];
    }
    return total - removeSum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @param Integer $k
     * @return Integer
     */
    function maximizeSumOfWeights($edges, $k) {
        $total = 0;
        $weights = [];
        foreach ($edges as $e) {
            $w = $e[2];
            $total += $w;
            $weights[] = $w;
        }
        // Need to remove exactly k-1 edges to obtain k components.
        // Remove the smallest weights to maximize remaining sum.
        $removeCount = max(0, $k - 1);
        if ($removeCount > 0) {
            sort($weights); // ascending
            $sumRemove = 0;
            for ($i = 0; $i < $removeCount && $i < count($weights); $i++) {
                $sumRemove += $weights[$i];
            }
            return $total - $sumRemove;
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func maximizeSumOfWeights(_ edges: [[Int]], _ k: Int) -> Int {
        var totalWeight: Int64 = 0
        var weights = [Int]()
        for e in edges {
            let w = e[2]
            totalWeight += Int64(w)
            weights.append(w)
        }
        if k <= 1 { return Int(totalWeight) }
        weights.sort()
        var removeSum: Int64 = 0
        for i in 0..<(k - 1) {
            removeSum += Int64(weights[i])
        }
        let result = totalWeight - removeSum
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximizeSumOfWeights(edges: Array<IntArray>, k: Int): Long {
        val total = edges.fold(0L) { acc, e -> acc + e[2].toLong() }
        if (k <= 1) return total
        val weights = edges.map { it[2] }.sorted()
        var removeSum = 0L
        for (i in 0 until k - 1) {
            removeSum += weights[i]
        }
        return total - removeSum
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int maximizeSumOfWeights(List<List<int>> edges, int k) {
    int n = edges.length + 1;
    List<List<_Edge>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0], v = e[1], w = e[2];
      adj[u].add(_Edge(v, w));
      adj[v].add(_Edge(u, w));
    }

    // Build parent array and traversal order using stack
    List<int> parent = List.filled(n, -1);
    List<int> order = [];
    List<int> stack = [0];
    parent[0] = 0;
    while (stack.isNotEmpty) {
      int u = stack.removeLast();
      order.add(u);
      for (var e in adj[u]) {
        int v = e.to;
        if (parent[v] == -1) {
          parent[v] = u;
          stack.add(v);
        }
      }
    }

    List<int> dp0 = List.filled(n, 0); // edge to parent not kept
    List<int> dp1 = List.filled(n, 0); // edge to parent kept

    for (int idx = order.length - 1; idx >= 0; --idx) {
      int u = order[idx];
      int base = 0;
      List<int> gains = [];

      for (var e in adj[u]) {
        int v = e.to;
        if (v == parent[u]) continue;
        base += dp0[v];
        int gain = e.w + dp1[v] - dp0[v];
        gains.add(gain);
      }

      gains.sort((a, b) => b.compareTo(a));

      int sumGain0 = 0;
      for (int i = 0; i < gains.length && i < k; ++i) {
        if (gains[i] > 0) sumGain0 += gains[i];
        else break;
      }
      dp0[u] = base + sumGain0;

      int limit1 = k - 1;
      int sumGain1 = 0;
      for (int i = 0; i < gains.length && i < limit1; ++i) {
        if (gains[i] > 0) sumGain1 += gains[i];
        else break;
      }
      dp1[u] = base + sumGain1;
    }

    return dp0[0];
  }
}

class _Edge {
  final int to;
  final int w;
  _Edge(this.to, this.w);
}
```

## Golang

```go
import (
	"sort"
)

type edge struct {
	to int
	w  int
}

func maximizeSumOfWeights(edges [][]int, k int) int64 {
	n := len(edges) + 1
	adj := make([][]edge, n)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		adj[u] = append(adj[u], edge{v, w})
		adj[v] = append(adj[v], edge{u, w})
	}

	parent := make([]int, n)
	order := make([]int, 0, n)
	stack := []int{0}
	parent[0] = -1
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		order = append(order, v)
		for _, nb := range adj[v] {
			if nb.to == parent[v] {
				continue
			}
			parent[nb.to] = v
			stack = append(stack, nb.to)
		}
	}

	dp0 := make([]int64, n) // edge to parent not taken
	dp1 := make([]int64, n) // edge to parent taken

	const negInf int64 = -1 << 60

	for i := len(order) - 1; i >= 0; i-- {
		v := order[i]
		base := int64(0)
		gains := make([]int64, 0)

		for _, nb := range adj[v] {
			if nb.to == parent[v] {
				continue
			}
			child := nb.to
			base += dp0[child]
			gain := int64(nb.w) + dp1[child] - dp0[child]
			if gain > 0 {
				gains = append(gains, gain)
			}
		}

		sort.Slice(gains, func(i, j int) bool { return gains[i] > gains[j] })

		// state where edge to parent is NOT taken
		sum0 := base
		limit0 := k
		for j := 0; j < limit0 && j < len(gains); j++ {
			sum0 += gains[j]
		}
		dp0[v] = sum0

		// state where edge to parent IS taken
		if k-1 < 0 {
			dp1[v] = negInf
		} else {
			sum1 := base
			limit1 := k - 1
			for j := 0; j < limit1 && j < len(gains); j++ {
				sum1 += gains[j]
			}
			dp1[v] = sum1
		}
	}

	return dp0[0]
}
```

## Ruby

```ruby
def maximize_sum_of_weights(edges, k)
  n = edges.size + 1
  adj = Array.new(n) { [] }
  edges.each do |u, v, w|
    adj[u] << [v, w]
    adj[v] << [u, w]
  end

  parent = Array.new(n, -1)
  pw = Array.new(n, 0) # weight to parent (unused directly)
  order = []
  stack = [0]
  parent[0] = 0
  while !stack.empty?
    node = stack.pop
    order << node
    adj[node].each do |nbr, w|
      next if nbr == parent[node]
      parent[nbr] = node
      pw[nbr] = w
      stack << nbr
    end
  end

  dp0 = Array.new(n, 0) # edge to parent not kept
  dp1 = Array.new(n, 0) # edge to parent kept

  order.reverse_each do |node|
    base = 0
    deltas = []
    adj[node].each do |nbr, w|
      next if nbr == parent[node]
      base += dp0[nbr]
      delta = w + dp1[nbr] - dp0[nbr]
      deltas << delta if delta > 0
    end

    deltas.sort!.reverse!

    # when parent edge not kept: can keep up to k child edges
    sum0 = base
    limit0 = k
    i = 0
    while i < deltas.length && i < limit0
      sum0 += deltas[i]
      i += 1
    end
    dp0[node] = sum0

    # when parent edge kept: can keep up to k-1 child edges
    sum1 = base
    limit1 = k - 1
    i = 0
    while i < deltas.length && i < limit1
      sum1 += deltas[i]
      i += 1
    end
    dp1[node] = sum1
  end

  dp0[0]
end
```

## Scala

```scala
object Solution {
    def maximizeSumOfWeights(edges: Array[Array[Int]], k: Int): Long = {
        val total = edges.foldLeft(0L)((sum, e) => sum + e(2).toLong)
        if (k <= 1) return total
        val sortedWeights = edges.map(_(2)).sorted
        var removedSum = 0L
        var i = 0
        while (i < k - 1 && i < sortedWeights.length) {
            removedSum += sortedWeights(i)
            i += 1
        }
        total - removedSum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximize_sum_of_weights(edges: Vec<Vec<i32>>, k: i32) -> i64 {
        let mut total: i64 = 0;
        let mut weights: Vec<i32> = Vec::with_capacity(edges.len());
        for e in edges.iter() {
            let w = e[2];
            total += w as i64;
            weights.push(w);
        }
        if k <= 1 {
            return total;
        }
        let mut remove_cnt = (k - 1) as usize;
        if remove_cnt > weights.len() {
            remove_cnt = weights.len();
        }
        weights.sort_unstable();
        let mut removed: i64 = 0;
        for i in 0..remove_cnt {
            removed += weights[i] as i64;
        }
        total - removed
    }
}
```

## Racket

```racket
(define/contract (maximize-sum-of-weights edges k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((weights (map (lambda (e) (list-ref e 2)) edges))
         (total   (apply + weights))
         (sorted  (sort weights <))
         (remove-count (max 0 (- k 1)))
         (to-remove (if (= remove-count 0)
                       '()
                       (take sorted remove-count)))
         (removed-sum (if (null? to-remove) 0 (apply + to-remove))))
    (- total removed-sum)))
```

## Erlang

```erlang
-spec maximize_sum_of_weights(Edges :: [[integer()]], K :: integer()) -> integer().
maximize_sum_of_weights(Edges, K) ->
    Weights = [W || [_U, _V, W] <- Edges],
    Total = lists:sum(Weights),
    Sorted = lists:sort(Weights),
    RemoveCnt = K - 1,
    Removed = sum_first_n(Sorted, RemoveCnt, 0),
    Total - Removed.

-spec sum_first_n([integer()], integer(), integer()) -> integer().
sum_first_n(_, 0, Acc) ->
    Acc;
sum_first_n([H | T], N, Acc) when N > 0 ->
    sum_first_n(T, N - 1, Acc + H);
sum_first_n([], _, Acc) ->
    Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximize_sum_of_weights(edges :: [[integer]], k :: integer) :: integer
  def maximize_sum_of_weights(edges, k) do
    total = Enum.reduce(edges, 0, fn [_u, _v, w], acc -> acc + w end)
    cuts = max(k - 1, 0)

    if cuts == 0 do
      total
    else
      weights = Enum.map(edges, fn [_u, _v, w] -> w end)
      sorted = Enum.sort(weights)
      cut_sum = sorted |> Enum.take(cuts) |> Enum.sum()
      total - cut_sum
    end
  end
end
```

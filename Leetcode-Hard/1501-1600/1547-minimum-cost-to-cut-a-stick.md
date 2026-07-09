# 1547. Minimum Cost to Cut a Stick

## Cpp

```cpp
class Solution {
public:
    int minCost(int n, vector<int>& cuts) {
        sort(cuts.begin(), cuts.end());
        vector<int> a;
        a.reserve(cuts.size() + 2);
        a.push_back(0);
        for (int c : cuts) a.push_back(c);
        a.push_back(n);
        int m = a.size();
        vector<vector<int>> dp(m, vector<int>(m, 0));
        const int INF = 1e9;
        for (int len = 2; len < m; ++len) { // distance between indices
            for (int i = 0; i + len < m; ++i) {
                int j = i + len;
                int best = INF;
                for (int k = i + 1; k < j; ++k) {
                    best = min(best, dp[i][k] + dp[k][j]);
                }
                dp[i][j] = best + a[j] - a[i];
            }
        }
        return dp[0][m - 1];
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int minCost(int n, int[] cuts) {
        int m = cuts.length;
        int[] pos = new int[m + 2];
        pos[0] = 0;
        System.arraycopy(cuts, 0, pos, 1, m);
        Arrays.sort(pos, 1, m + 1); // sort only the cut positions
        pos[m + 1] = n;

        int[][] dp = new int[m + 2][m + 2];

        for (int len = 2; len <= m + 1; len++) {          // distance between left and right indices
            for (int left = 0; left + len <= m + 1; left++) {
                int right = left + len;
                int best = Integer.MAX_VALUE;
                for (int mid = left + 1; mid < right; mid++) {
                    int cost = dp[left][mid] + dp[mid][right] + pos[right] - pos[left];
                    if (cost < best) {
                        best = cost;
                    }
                }
                dp[left][right] = best == Integer.MAX_VALUE ? 0 : best;
            }
        }

        return dp[0][m + 1];
    }
}
```

## Python

```python
class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        m = len(cuts)
        if m == 0:
            return 0
        # include the two ends and sort
        points = [0] + sorted(cuts) + [n]
        size = m + 2
        dp = [[0] * size for _ in range(size)]
        # diff is the distance between left and right indices
        for diff in range(2, size):
            for left in range(size - diff):
                right = left + diff
                best = float('inf')
                length = points[right] - points[left]
                for mid in range(left + 1, right):
                    cost = dp[left][mid] + dp[mid][right] + length
                    if cost < best:
                        best = cost
                dp[left][right] = best
        return dp[0][size - 1]
```

## Python3

```python
from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        if not cuts:
            return 0
        cuts.sort()
        points = [0] + cuts + [n]
        m = len(cuts)
        size = m + 2
        dp = [[0] * size for _ in range(size)]
        for length in range(2, size):
            for left in range(0, size - length):
                right = left + length
                best = float('inf')
                segment_cost = points[right] - points[left]
                for k in range(left + 1, right):
                    cur = dp[left][k] + dp[k][right] + segment_cost
                    if cur < best:
                        best = cur
                dp[left][right] = best
        return dp[0][size - 1]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmpInt(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

int minCost(int n, int* cuts, int cutsSize) {
    int total = cutsSize + 2;
    int *pos = (int *)malloc(total * sizeof(int));
    if (!pos) return 0; // safety
    
    pos[0] = 0;
    for (int i = 0; i < cutsSize; ++i) pos[i + 1] = cuts[i];
    pos[total - 1] = n;
    
    qsort(pos, total, sizeof(int), cmpInt);
    
    int dp[102][102] = {0}; // max size: cutsSize <= 100
    
    for (int len = 2; len < total; ++len) {          // distance between left and right
        for (int left = 0; left + len < total; ++left) {
            int right = left + len;
            int best = INT_MAX;
            for (int mid = left + 1; mid < right; ++mid) {
                int cost = dp[left][mid] + dp[mid][right] + pos[right] - pos[left];
                if (cost < best) best = cost;
            }
            dp[left][right] = best;
        }
    }
    
    int result = dp[0][total - 1];
    free(pos);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinCost(int n, int[] cuts)
    {
        var points = new List<int>(cuts);
        points.Add(0);
        points.Add(n);
        points.Sort();

        int m = points.Count;
        int[,] dp = new int[m, m];
        const int INF = int.MaxValue / 2;

        for (int len = 2; len < m; ++len) // distance between left and right
        {
            for (int left = 0; left + len < m; ++left)
            {
                int right = left + len;
                int best = INF;
                for (int mid = left + 1; mid < right; ++mid)
                {
                    int cost = dp[left, mid] + dp[mid, right] + points[right] - points[left];
                    if (cost < best) best = cost;
                }
                dp[left, right] = best == INF ? 0 : best;
            }
        }

        return dp[0, m - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} cuts
 * @return {number}
 */
var minCost = function(n, cuts) {
    // Sort the cut positions and add the stick ends.
    const sortedCuts = cuts.slice().sort((a, b) => a - b);
    const points = [0, ...sortedCuts, n];
    const m = points.length;
    
    // dp[i][j] = minimum cost to cut the segment between points[i] and points[j]
    const dp = Array.from({ length: m }, () => Array(m).fill(0));
    
    // Consider segments of increasing length (number of points apart)
    for (let len = 2; len < m; ++len) {          // distance between i and j
        for (let i = 0; i + len < m; ++i) {
            const j = i + len;
            let best = Infinity;
            // Try every possible cut k between i and j
            for (let k = i + 1; k < j; ++k) {
                const cost = dp[i][k] + dp[k][j] + points[j] - points[i];
                if (cost < best) best = cost;
            }
            // If there is no cut inside, cost remains 0
            dp[i][j] = best === Infinity ? 0 : best;
        }
    }
    
    return dp[0][m - 1];
};
```

## Typescript

```typescript
function minCost(n: number, cuts: number[]): number {
    const sorted = cuts.slice().sort((a, b) => a - b);
    const points = [0, ...sorted, n];
    const m = cuts.length;
    const size = m + 2;

    const dp: number[][] = Array.from({ length: size }, () => Array(size).fill(0));

    for (let len = 2; len < size; ++len) {
        for (let left = 0; left + len < size; ++left) {
            const right = left + len;
            let best = Number.MAX_SAFE_INTEGER;
            for (let mid = left + 1; mid < right; ++mid) {
                const cost = dp[left][mid] + dp[mid][right] + points[right] - points[left];
                if (cost < best) best = cost;
            }
            dp[left][right] = best;
        }
    }

    return dp[0][size - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $cuts
     * @return Integer
     */
    function minCost($n, $cuts) {
        sort($cuts);
        $m = count($cuts);
        // positions including the two ends
        $pos = array_merge([0], $cuts, [$n]);
        $size = $m + 2;

        // dp[i][j] = minimum cost to cut between pos[i] and pos[j]
        $dp = [];
        for ($i = 0; $i < $size; $i++) {
            $dp[$i] = array_fill(0, $size, 0);
        }

        // length is the distance in indices (at least 2 to have a segment)
        for ($len = 2; $len < $size; $len++) { // len = j - i
            for ($i = 0; $i + $len < $size; $i++) {
                $j = $i + $len;
                $best = PHP_INT_MAX;
                for ($k = $i + 1; $k < $j; $k++) {
                    $cost = $dp[$i][$k] + $dp[$k][$j] + $pos[$j] - $pos[$i];
                    if ($cost < $best) {
                        $best = $cost;
                    }
                }
                $dp[$i][$j] = $best === PHP_INT_MAX ? 0 : $best;
            }
        }

        return $dp[0][$size - 1];
    }
}
```

## Swift

```swift
class Solution {
    func minCost(_ n: Int, _ cuts: [Int]) -> Int {
        let sortedCuts = cuts.sorted()
        var points = [0]
        points.append(contentsOf: sortedCuts)
        points.append(n)
        let m = points.count
        var dp = Array(repeating: Array(repeating: 0, count: m), count: m)
        
        if m <= 2 { return 0 }
        
        for length in 2..<m {
            for left in 0..<(m - length) {
                let right = left + length
                var best = Int.max
                for mid in (left + 1)..<right {
                    let cost = dp[left][mid] + dp[mid][right] + points[right] - points[left]
                    if cost < best {
                        best = cost
                    }
                }
                dp[left][right] = best
            }
        }
        return dp[0][m - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCost(n: Int, cuts: IntArray): Int {
        val sortedCuts = cuts.sorted()
        val m = sortedCuts.size
        val points = IntArray(m + 2)
        points[0] = 0
        for (i in 0 until m) {
            points[i + 1] = sortedCuts[i]
        }
        points[m + 1] = n

        val dp = Array(m + 2) { IntArray(m + 2) }

        for (len in 2..m + 1) {
            var left = 0
            while (left + len <= m + 1) {
                val right = left + len
                var best = Int.MAX_VALUE
                var mid = left + 1
                while (mid < right) {
                    val cost = dp[left][mid] + dp[mid][right] + points[right] - points[left]
                    if (cost < best) best = cost
                    mid++
                }
                dp[left][right] = if (best == Int.MAX_VALUE) 0 else best
                left++
            }
        }

        return dp[0][m + 1]
    }
}
```

## Dart

```dart
class Solution {
  int minCost(int n, List<int> cuts) {
    // Sort the cut positions
    List<int> sortedCuts = List.from(cuts);
    sortedCuts.sort();
    // Build the array with stick ends
    List<int> points = [0];
    points.addAll(sortedCuts);
    points.add(n);
    int m = cuts.length;
    // dp[i][j] = minimum cost to cut between points[i] and points[j]
    List<List<int>> dp = List.generate(m + 2, (_) => List.filled(m + 2, 0));
    const int INF = 1 << 60;

    for (int len = 2; len <= m + 1; ++len) {
      for (int i = 0; i + len <= m + 1; ++i) {
        int j = i + len;
        int best = INF;
        for (int k = i + 1; k < j; ++k) {
          int cost = dp[i][k] + dp[k][j] + points[j] - points[i];
          if (cost < best) best = cost;
        }
        dp[i][j] = best;
      }
    }

    return dp[0][m + 1];
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

func minCost(n int, cuts []int) int {
	m := len(cuts)
	points := make([]int, 0, m+2)
	points = append(points, 0)
	points = append(points, cuts...)
	points = append(points, n)
	sort.Ints(points)

	total := len(points)
	dp := make([][]int, total)
	for i := 0; i < total; i++ {
		dp[i] = make([]int, total)
	}

	const INF = int(1e9)

	for length := 2; length < total; length++ {
		for left := 0; left+length < total; left++ {
			right := left + length
			best := INF
			for mid := left + 1; mid < right; mid++ {
				cost := dp[left][mid] + dp[mid][right] + points[right] - points[left]
				if cost < best {
					best = cost
				}
			}
			dp[left][right] = best
		}
	}

	return dp[0][total-1]
}
```

## Ruby

```ruby
def min_cost(n, cuts)
  cuts.sort!
  points = [0] + cuts + [n]
  m = cuts.length
  size = m + 2
  dp = Array.new(size) { Array.new(size, 0) }

  (2..size - 1).each do |len|
    (0...(size - len)).each do |left|
      right = left + len
      best = Float::INFINITY
      ((left + 1)...right).each do |mid|
        cost = dp[left][mid] + dp[mid][right] + points[right] - points[left]
        best = cost if cost < best
      end
      dp[left][right] = best
    end
  end

  dp[0][size - 1]
end
```

## Scala

```scala
object Solution {
    def minCost(n: Int, cuts: Array[Int]): Int = {
        if (cuts.isEmpty) return 0
        val points = (cuts :+ 0 :+ n).sorted
        val m = points.length
        val dp = Array.ofDim[Int](m, m)

        for (diff <- 2 until m) {
            var left = 0
            while (left + diff < m) {
                val right = left + diff
                var best = Int.MaxValue
                var mid = left + 1
                while (mid < right) {
                    val cost = dp(left)(mid) + dp(mid)(right) + points(right) - points(left)
                    if (cost < best) best = cost
                    mid += 1
                }
                dp(left)(right) = best
                left += 1
            }
        }

        dp(0)(m - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost(n: i32, mut cuts: Vec<i32>) -> i32 {
        cuts.sort_unstable();
        let m = cuts.len() + 2;
        let mut pos = Vec::with_capacity(m);
        pos.push(0);
        pos.extend(cuts);
        pos.push(n);

        let mut dp = vec![vec![0i32; m]; m];

        for diff in 2..m {
            for left in 0..(m - diff) {
                let right = left + diff;
                let mut best = i32::MAX;
                for mid in (left + 1)..right {
                    let cost = dp[left][mid] + dp[mid][right] + pos[right] - pos[left];
                    if cost < best {
                        best = cost;
                    }
                }
                dp[left][right] = best;
            }
        }

        dp[0][m - 1]
    }
}
```

## Racket

```racket
(define/contract (min-cost n cuts)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort (cons 0 (append cuts (list n))) <))
         (len (+ (length cuts) 2))
         (v (list->vector sorted)))
    ;; dp[i][j] = min cost to cut segment between v[i] and v[j]
    (define dp (make-vector len))
    (for ([i (in-range len)])
      (vector-set! dp i (make-vector len 0)))
    (let ((INF (arithmetic-shift 1 60))) ; a large integer
      (for ([diff 2 (in-range 2 len)])               ; segment length
        (for ([left 0 (in-range (- len diff))])     ; left index
          (let* ((right (+ left diff))
                 (best
                  (let loop ((mid (+ left 1)) (cur INF))
                    (if (>= mid right)
                        cur
                        (let* ((cost (+ (vector-ref (vector-ref dp left) mid)
                                        (vector-ref (vector-ref dp mid) right)
                                        (- (vector-ref v right) (vector-ref v left)))))
                          (loop (+ mid 1) (if (< cost cur) cost cur)))))))
            (vector-set! (vector-ref dp left) right best))))
      (vector-ref (vector-ref dp 0) (- len 1)))))
```

## Erlang

```erlang
-module(solution).
-export([min_cost/2]).

-spec min_cost(N :: integer(), Cuts :: [integer()]) -> integer().
min_cost(N, Cuts) ->
    Sorted = lists:sort(Cuts),
    NewList = [0] ++ Sorted ++ [N],
    Len = length(NewList),
    Tuple = list_to_tuple(NewList),
    DP0 = maps:new(),
    MaxDiff = Len - 1,
    DP = fill_dp(2, MaxDiff, Tuple, DP0),
    maps:get({0, Len-1}, DP).

fill_dp(Diff, MaxDiff, _Tuple, DP) when Diff > MaxDiff ->
    DP;
fill_dp(Diff, MaxDiff, Tuple, DP) ->
    DP1 = fill_left(0, Diff, Tuple, DP),
    fill_dp(Diff + 1, MaxDiff, Tuple, DP1).

fill_left(Left, Diff, Tuple, DP) ->
    Limit = tuple_size(Tuple) - 1 - Diff,
    if Left > Limit -> DP;
       true ->
           Right = Left + Diff,
           MinCost = compute_min_cost(Left+1, Right-1, Left, Right, Tuple, DP, 1 bsl 60),
           DP2 = maps:put({Left,Right}, MinCost, DP),
           fill_left(Left+1, Diff, Tuple, DP2)
    end.

compute_min_cost(Mid, End, _Left, _Right, _Tuple, _DP, Min) when Mid > End ->
    Min;
compute_min_cost(Mid, End, Left, Right, Tuple, DP, Min) ->
    CostLeft = maps:get({Left,Mid}, DP, 0),
    CostRight = maps:get({Mid,Right}, DP, 0),
    SegmentCost = element(Right, Tuple) - element(Left, Tuple),
    Total = CostLeft + CostRight + SegmentCost,
    NewMin = if Total < Min -> Total; true -> Min end,
    compute_min_cost(Mid+1, End, Left, Right, Tuple, DP, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost(n :: integer, cuts :: [integer]) :: integer
  def min_cost(n, cuts) do
    sorted = Enum.sort(cuts)
    points = [0 | sorted] ++ [n]
    total = length(points)

    dp =
      Enum.reduce(2..(total - 1), %{}, fn diff, acc ->
        Enum.reduce(0..(total - diff - 1), acc, fn left, acc2 ->
          right = left + diff
          segment_len = Enum.at(points, right) - Enum.at(points, left)

          min_cost =
            Enum.reduce((left + 1)..(right - 1), nil, fn mid, cur_min ->
              left_mid = Map.get(acc2, {left, mid}, 0)
              mid_right = Map.get(acc2, {mid, right}, 0)
              cost = left_mid + mid_right + segment_len

              case cur_min do
                nil -> cost
                _ when cost < cur_min -> cost
                _ -> cur_min
              end
            end)

          Map.put(acc2, {left, right}, min_cost)
        end)
      end)

    Map.get(dp, {0, total - 1})
  end
end
```

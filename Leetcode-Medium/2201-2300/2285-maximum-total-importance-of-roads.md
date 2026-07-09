# 2285. Maximum Total Importance of Roads

## Cpp

```cpp
class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        vector<int> deg(n, 0);
        for (const auto& r : roads) {
            ++deg[r[0]];
            ++deg[r[1]];
        }
        sort(deg.begin(), deg.end());
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += static_cast<long long>(deg[i]) * (i + 1);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maximumImportance(int n, int[][] roads) {
        int[] degree = new int[n];
        for (int[] road : roads) {
            degree[road[0]]++;
            degree[road[1]]++;
        }
        int[] sortedDeg = degree.clone();
        java.util.Arrays.sort(sortedDeg);
        long total = 0L;
        for (int i = 0; i < n; i++) {
            total += (long) sortedDeg[i] * (i + 1);
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        degree.sort()
        total = 0
        for i, d in enumerate(degree, 1):
            total += d * i
        return total
```

## Python3

```python
from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        degree.sort()
        total = 0
        value = 1
        for d in degree:
            total += d * value
            value += 1
        return total
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

long long maximumImportance(int n, int** roads, int roadsSize, int* roadsColSize) {
    (void)roadsColSize; // unused
    int *degree = (int *)calloc(n, sizeof(int));
    if (!degree) return 0;

    for (int i = 0; i < roadsSize; ++i) {
        int u = roads[i][0];
        int v = roads[i][1];
        degree[u]++;
        degree[v]++;
    }

    qsort(degree, n, sizeof(int), cmp_int);

    long long total = 0;
    for (int i = 0; i < n; ++i) {
        total += (long long)degree[i] * (i + 1);
    }

    free(degree);
    return total;
}
```

## Csharp

```csharp
public class Solution
{
    public long MaximumImportance(int n, int[][] roads)
    {
        int[] degree = new int[n];
        foreach (var road in roads)
        {
            degree[road[0]]++;
            degree[road[1]]++;
        }

        Array.Sort(degree);

        long total = 0;
        for (int i = 0; i < n; i++)
        {
            total += (long)degree[i] * (i + 1);
        }

        return total;
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
var maximumImportance = function(n, roads) {
    const degree = new Array(n).fill(0);
    for (const [a, b] of roads) {
        degree[a]++;
        degree[b]++;
    }
    degree.sort((x, y) => x - y);
    let total = 0;
    for (let i = 0; i < n; i++) {
        total += degree[i] * (i + 1);
    }
    return total;
};
```

## Typescript

```typescript
function maximumImportance(n: number, roads: number[][]): number {
    const degree = new Array<number>(n).fill(0);
    for (const [a, b] of roads) {
        degree[a]++;
        degree[b]++;
    }
    degree.sort((x, y) => x - y);
    let total = 0;
    for (let i = 0; i < n; i++) {
        total += degree[i] * (i + 1);
    }
    return total;
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
    function maximumImportance($n, $roads) {
        $degree = array_fill(0, $n, 0);
        foreach ($roads as $road) {
            $a = $road[0];
            $b = $road[1];
            $degree[$a]++;
            $degree[$b]++;
        }
        sort($degree); // ascending
        $value = 1;
        $total = 0;
        foreach ($degree as $deg) {
            $total += $deg * $value;
            $value++;
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func maximumImportance(_ n: Int, _ roads: [[Int]]) -> Int {
        var degree = [Int](repeating: 0, count: n)
        for road in roads {
            let a = road[0]
            let b = road[1]
            degree[a] += 1
            degree[b] += 1
        }
        degree.sort()
        var total = 0
        for i in 0..<n {
            total += degree[i] * (i + 1)
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumImportance(n: Int, roads: Array<IntArray>): Long {
        val degree = IntArray(n)
        for (road in roads) {
            val a = road[0]
            val b = road[1]
            degree[a]++
            degree[b]++
        }
        degree.sort()
        var total = 0L
        for (i in 0 until n) {
            total += degree[i].toLong() * (i + 1)
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int maximumImportance(int n, List<List<int>> roads) {
    List<int> degree = List.filled(n, 0);
    for (var road in roads) {
      int a = road[0];
      int b = road[1];
      degree[a]++;
      degree[b]++;
    }
    degree.sort((a, b) => a.compareTo(b));
    int total = 0;
    for (int i = 0; i < n; i++) {
      total += degree[i] * (i + 1);
    }
    return total;
  }
}
```

## Golang

```go
import "sort"

func maximumImportance(n int, roads [][]int) int64 {
	degree := make([]int, n)
	for _, r := range roads {
		a, b := r[0], r[1]
		degree[a]++
		degree[b]++
	}
	sort.Ints(degree)
	var total int64
	for i, d := range degree {
		total += int64(d) * int64(i+1)
	}
	return total
}
```

## Ruby

```ruby
def maximum_importance(n, roads)
  degrees = Array.new(n, 0)
  roads.each do |a, b|
    degrees[a] += 1
    degrees[b] += 1
  end
  degrees.sort!
  total = 0
  value = 1
  degrees.each do |deg|
    total += deg * value
    value += 1
  end
  total
end
```

## Scala

```scala
object Solution {
    def maximumImportance(n: Int, roads: Array[Array[Int]]): Long = {
        val degree = Array.fill(n)(0)
        var i = 0
        while (i < roads.length) {
            val a = roads(i)(0)
            val b = roads(i)(1)
            degree(a) += 1
            degree(b) += 1
            i += 1
        }
        val sortedDeg = degree.sorted
        var total: Long = 0L
        var value = 1L
        var idx = 0
        while (idx < n) {
            total += sortedDeg(idx).toLong * value
            value += 1
            idx += 1
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_importance(n: i32, roads: Vec<Vec<i32>>) -> i64 {
        let n_usize = n as usize;
        let mut degree = vec![0i64; n_usize];
        for road in &roads {
            let a = road[0] as usize;
            let b = road[1] as usize;
            degree[a] += 1;
            degree[b] += 1;
        }
        degree.sort_unstable();
        let mut total: i64 = 0;
        for (i, &deg) in degree.iter().enumerate() {
            let value = i as i64 + 1;
            total += deg * value;
        }
        total
    }
}
```

## Racket

```racket
(define/contract (maximum-importance n roads)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((deg (make-vector n 0))
         ;; compute degrees
         (_ (for ([e roads])
              (let ((a (first e))
                    (b (second e)))
                (vector-set! deg a (+ 1 (vector-ref deg a)))
                (vector-set! deg b (+ 1 (vector-ref deg b))))))
         (deg-list (for/list ([i (in-range n)]) (vector-ref deg i)))
         (sorted-degrees (sort deg-list <))
         (total (let loop ((lst sorted-degrees) (val 1) (acc 0))
                  (if (null? lst)
                      acc
                      (loop (cdr lst) (+ val 1) (+ acc (* (car lst) val)))))))
    total))
```

## Erlang

```erlang
-module(solution).
-export([maximum_importance/2]).

-spec maximum_importance(N :: integer(), Roads :: [[integer()]]) -> integer().
maximum_importance(N, Roads) ->
    % Build degree map
    DegMap = lists:foldl(
        fun([A, B], Acc) ->
            Acc1 = maps:update_with(A,
                    fun(V) -> V + 1 end,
                    1,
                    Acc),
            maps:update_with(B,
                fun(V) -> V + 1 end,
                1,
                Acc1)
        end,
        #{},
        Roads),

    % Extract degrees for all cities
    Degrees = [maps:get(I, DegMap, 0) || I <- lists:seq(0, N - 1)],

    % Sort degrees in ascending order
    Sorted = lists:sort(Degrees),

    % Compute total importance: sum degree_i * assigned_value_i (values 1..N)
    {Total, _} =
        lists:foldl(
            fun({Deg, Val}, {Acc, _}) ->
                {Acc + Deg * Val, Val}
            end,
            {0, 0},
            lists:zip(Sorted, lists:seq(1, N))
        ),
    Total.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_importance(n :: integer, roads :: [[integer]]) :: integer
  def maximum_importance(n, roads) do
    deg_map =
      Enum.reduce(roads, %{}, fn [a, b], acc ->
        acc
        |> Map.update(a, 1, &(&1 + 1))
        |> Map.update(b, 1, &(&1 + 1))
      end)

    degrees = for i <- 0..(n - 1), do: Map.get(deg_map, i, 0)
    sorted = Enum.sort(degrees)

    {total, _} =
      Enum.reduce(sorted, {0, 1}, fn d, {sum, val} ->
        {sum + d * val, val + 1}
      end)

    total
  end
end
```

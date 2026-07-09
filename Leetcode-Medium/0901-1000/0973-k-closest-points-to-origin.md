# 0973. K Closest Points to Origin

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        nth_element(points.begin(), points.begin() + k, points.end(),
            [](const vector<int>& a, const vector<int>& b) {
                long long da = 1LL * a[0] * a[0] + 1LL * a[1] * a[1];
                long long db = 1LL * b[0] * b[0] + 1LL * b[1] * b[1];
                return da < db;
            });
        return vector<vector<int>>(points.begin(), points.begin() + k);
    }
};
```

## Java

```java
import java.util.PriorityQueue;

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        if (k >= points.length) return points;
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
            (a, b) -> Long.compare(dist(b), dist(a))
        );
        for (int[] p : points) {
            maxHeap.offer(p);
            if (maxHeap.size() > k) {
                maxHeap.poll();
            }
        }
        int[][] result = new int[k][2];
        int idx = 0;
        while (!maxHeap.isEmpty()) {
            result[idx++] = maxHeap.poll();
        }
        return result;
    }

    private long dist(int[] p) {
        long x = p[0];
        long y = p[1];
        return x * x + y * y;
    }
}
```

## Python

```python
import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        return heapq.nsmallest(k, points, key=lambda p: p[0]*p[0] + p[1]*p[1])
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use a max-heap of size k to keep the closest points
        # Store (-distance, point) so that the largest distance is on top
        max_heap = []
        for x, y in points:
            dist = x * x + y * y
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist, [x, y]))
            else:
                # If current point is closer than the farthest in heap, replace it
                if -max_heap[0][0] > dist:
                    heapq.heapreplace(max_heap, (-dist, [x, y]))
        return [pt for _, pt in max_heap]
```

## C

```c
#include <stdlib.h>

struct Pair {
    int idx;
    long long dist;
};

static int cmpPair(const void *a, const void *b) {
    const struct Pair *pa = (const struct Pair *)a;
    const struct Pair *pb = (const struct Pair *)b;
    if (pa->dist < pb->dist) return -1;
    if (pa->dist > pb->dist) return 1;
    return 0;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** kClosest(int** points, int pointsSize, int* pointsColSize, int k, int* returnSize, int*** returnColumnSizes) {
    (void)pointsColSize; // unused, each point has 2 columns

    struct Pair *arr = (struct Pair *)malloc(pointsSize * sizeof(struct Pair));
    for (int i = 0; i < pointsSize; ++i) {
        long long x = points[i][0];
        long long y = points[i][1];
        arr[i].idx = i;
        arr[i].dist = x * x + y * y;
    }

    qsort(arr, pointsSize, sizeof(struct Pair), cmpPair);

    int **result = (int **)malloc(k * sizeof(int *));
    int **colSizes = (int **)malloc(k * sizeof(int *));
    // In LeetCode C signature, returnColumnSizes is int**, but they expect an int* array.
    // We'll allocate a single int* and assign its address to *returnColumnSizes.
    int *sizes = (int *)malloc(k * sizeof(int));

    for (int i = 0; i < k; ++i) {
        int idx = arr[i].idx;
        result[i] = (int *)malloc(2 * sizeof(int));
        result[i][0] = points[idx][0];
        result[i][1] = points[idx][1];
        sizes[i] = 2;
    }

    free(arr);
    *returnSize = k;
    *returnColumnSizes = &sizes; // assign pointer to allocated array
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] KClosest(int[][] points, int k) {
        System.Array.Sort(points, (a, b) => {
            long d1 = (long)a[0] * a[0] + (long)a[1] * a[1];
            long d2 = (long)b[0] * b[0] + (long)b[1] * b[1];
            return d1.CompareTo(d2);
        });
        
        int[][] result = new int[k][];
        for (int i = 0; i < k; i++) {
            result[i] = points[i];
        }
        return result;
    }
}
```

## Javascript

```javascript
var kClosest = function(points, k) {
    points.sort((a, b) => {
        const d1 = a[0] * a[0] + a[1] * a[1];
        const d2 = b[0] * b[0] + b[1] * b[1];
        return d1 - d2;
    });
    return points.slice(0, k);
};
```

## Typescript

```typescript
function kClosest(points: number[][], k: number): number[][] {
    points.sort((a, b) => {
        const distA = a[0] * a[0] + a[1] * a[1];
        const distB = b[0] * b[0] + b[1] * b[1];
        return distA - distB;
    });
    return points.slice(0, k);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @param Integer $k
     * @return Integer[][]
     */
    function kClosest($points, $k) {
        usort($points, function ($a, $b) {
            $da = $a[0] * $a[0] + $a[1] * $a[1];
            $db = $b[0] * $b[0] + $b[1] * $b[1];
            if ($da == $db) return 0;
            return ($da < $db) ? -1 : 1;
        });
        return array_slice($points, 0, $k);
    }
}
```

## Swift

```swift
class Solution {
    func kClosest(_ points: [[Int]], _ k: Int) -> [[Int]] {
        let sorted = points.sorted { a, b in
            let d1 = a[0] * a[0] + a[1] * a[1]
            let d2 = b[0] * b[0] + b[1] * b[1]
            return d1 < d2
        }
        return Array(sorted.prefix(k))
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kClosest(points: Array<IntArray>, k: Int): Array<IntArray> {
        val sorted = points.sortedWith(compareBy { (it[0] * it[0] + it[1] * it[1]).toLong() })
        return Array(k) { sorted[it] }
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> kClosest(List<List<int>> points, int k) {
    points.sort((a, b) {
      int da = a[0] * a[0] + a[1] * a[1];
      int db = b[0] * b[0] + b[1] * b[1];
      return da.compareTo(db);
    });
    return points.sublist(0, k);
  }
}
```

## Golang

```go
import "sort"

func kClosest(points [][]int, k int) [][]int {
	sort.Slice(points, func(i, j int) bool {
		di := points[i][0]*points[i][0] + points[i][1]*points[i][1]
		dj := points[j][0]*points[j][0] + points[j][1]*points[j][1]
		return di < dj
	})
	return points[:k]
}
```

## Ruby

```ruby
def k_closest(points, k)
  points.sort_by { |x, y| x * x + y * y }[0, k]
end
```

## Scala

```scala
object Solution {
    def kClosest(points: Array[Array[Int]], k: Int): Array[Array[Int]] = {
        points.sortBy { p =>
            val x = p(0).toLong
            val y = p(1).toLong
            x * x + y * y
        }.take(k)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn k_closest(points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        use std::collections::BinaryHeap;
        let mut heap: BinaryHeap<(i64, usize)> = BinaryHeap::new();
        let kk = k as usize;
        for (i, p) in points.iter().enumerate() {
            let x = p[0] as i64;
            let y = p[1] as i64;
            let dist = x * x + y * y;
            heap.push((dist, i));
            if heap.len() > kk {
                heap.pop();
            }
        }
        let mut res = Vec::with_capacity(kk);
        while let Some((_d, idx)) = heap.pop() {
            res.push(points[idx].clone());
        }
        res
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (k-closest points k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof (listof exact-integer?)))
  (let* ([dist (lambda (p) (+ (* (first p) (first p))
                              (* (second p) (second p))))])
    (take (sort points
                (lambda (a b)
                  (< (dist a) (dist b))))
          k)))
```

## Erlang

```erlang
-module(solution).
-export([k_closest/2]).

-spec k_closest(Points :: [[integer()]], K :: integer()) -> [[integer()]].
k_closest(Points, K) ->
    WithDist = [{dist(Point), Point} || Point <- Points],
    Sorted = lists:keysort(1, WithDist),
    take_k(Sorted, K).

dist([X, Y]) ->
    X * X + Y * Y.

take_k(List, K) -> take_k(List, K, []).

take_k(_, 0, Acc) ->
    lists:reverse(Acc);
take_k([{_, Pt} | Rest], N, Acc) when N > 0 ->
    take_k(Rest, N - 1, [Pt | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec k_closest(points :: [[integer]], k :: integer) :: [[integer]]
  def k_closest(points, k) do
    points
    |> Enum.map(fn [x, y] = p -> {x * x + y * y, p} end)
    |> Enum.sort_by(fn {dist, _p} -> dist end)
    |> Enum.take(k)
    |> Enum.map(fn {_d, p} -> p end)
  end
end
```

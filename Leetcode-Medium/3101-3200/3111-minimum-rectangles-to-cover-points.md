# 3111. Minimum Rectangles to Cover Points

## Cpp

```cpp
class Solution {
public:
    int minRectanglesToCoverPoints(vector<vector<int>>& points, int w) {
        vector<long long> xs;
        xs.reserve(points.size());
        for (const auto& p : points) xs.push_back(p[0]);
        sort(xs.begin(), xs.end());
        int cnt = 0;
        size_t i = 0, n = xs.size();
        while (i < n) {
            ++cnt;
            long long limit = xs[i] + w;
            while (i < n && xs[i] <= limit) ++i;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int minRectanglesToCoverPoints(int[][] points, int w) {
        int n = points.length;
        int[] xs = new int[n];
        for (int i = 0; i < n; i++) {
            xs[i] = points[i][0];
        }
        java.util.Arrays.sort(xs);
        int count = 0;
        int i = 0;
        while (i < n) {
            int start = xs[i];
            count++;
            long limit = (long) start + w; // use long to avoid overflow
            i++;
            while (i < n && xs[i] <= limit) {
                i++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def minRectanglesToCoverPoints(self, points, w):
        """
        :type points: List[List[int]]
        :type w: int
        :rtype: int
        """
        xs = [p[0] for p in points]
        xs.sort()
        ans = 0
        i = 0
        n = len(xs)
        while i < n:
            ans += 1
            limit = xs[i] + w
            i += 1
            while i < n and xs[i] <= limit:
                i += 1
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        xs = sorted(p[0] for p in points)
        cnt = 0
        i = 0
        n = len(xs)
        while i < n:
            cnt += 1
            limit = xs[i] + w
            i += 1
            while i < n and xs[i] <= limit:
                i += 1
        return cnt
```

## C

```c
#include <stdlib.h>

static int compare_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

int minRectanglesToCoverPoints(int** points, int pointsSize, int* pointsColSize, int w) {
    if (pointsSize == 0) return 0;

    int *xs = (int *)malloc(pointsSize * sizeof(int));
    for (int i = 0; i < pointsSize; ++i) {
        xs[i] = points[i][0];
    }

    qsort(xs, pointsSize, sizeof(int), compare_int);

    int rectangles = 0;
    int i = 0;
    while (i < pointsSize) {
        long long limit = (long long)xs[i] + w; // use long long to avoid overflow
        ++rectangles;
        while (i < pointsSize && xs[i] <= limit) {
            ++i;
        }
    }

    free(xs);
    return rectangles;
}
```

## Csharp

```csharp
public class Solution {
    public int MinRectanglesToCoverPoints(int[][] points, int w) {
        int n = points.Length;
        long[] xs = new long[n];
        for (int i = 0; i < n; i++) {
            xs[i] = points[i][0];
        }
        Array.Sort(xs);
        int rectangles = 0;
        int idx = 0;
        while (idx < n) {
            long start = xs[idx];
            long limit = start + w;
            rectangles++;
            idx++;
            while (idx < n && xs[idx] <= limit) {
                idx++;
            }
        }
        return rectangles;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @param {number} w
 * @return {number}
 */
var minRectanglesToCoverPoints = function(points, w) {
    const xs = points.map(p => p[0]);
    xs.sort((a, b) => a - b);
    let rectangles = 0;
    let i = 0;
    const n = xs.length;
    while (i < n) {
        const left = xs[i];
        rectangles++;
        const limit = left + w;
        while (i < n && xs[i] <= limit) {
            i++;
        }
    }
    return rectangles;
};
```

## Typescript

```typescript
function minRectanglesToCoverPoints(points: number[][], w: number): number {
    const xs = points.map(p => p[0]);
    xs.sort((a, b) => a - b);
    let count = 0;
    let i = 0;
    const n = xs.length;
    while (i < n) {
        count++;
        const limit = xs[i] + w;
        i++;
        while (i < n && xs[i] <= limit) {
            i++;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @param Integer $w
     * @return Integer
     */
    function minRectanglesToCoverPoints($points, $w) {
        $xs = [];
        foreach ($points as $p) {
            $xs[] = $p[0];
        }
        sort($xs, SORT_NUMERIC);
        $n = count($xs);
        $i = 0;
        $rects = 0;
        while ($i < $n) {
            $rects++;
            $limit = $xs[$i] + $w;
            $i++;
            while ($i < $n && $xs[$i] <= $limit) {
                $i++;
            }
        }
        return $rects;
    }
}
```

## Swift

```swift
class Solution {
    func minRectanglesToCoverPoints(_ points: [[Int]], _ w: Int) -> Int {
        var xs = [Int]()
        xs.reserveCapacity(points.count)
        for p in points {
            xs.append(p[0])
        }
        xs.sort()
        var i = 0
        let n = xs.count
        var rects = 0
        while i < n {
            rects += 1
            let limit = xs[i] + w
            while i < n && xs[i] <= limit {
                i += 1
            }
        }
        return rects
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minRectanglesToCoverPoints(points: Array<IntArray>, w: Int): Int {
        val n = points.size
        if (n == 0) return 0
        val xs = IntArray(n)
        for (i in 0 until n) {
            xs[i] = points[i][0]
        }
        xs.sort()
        var count = 0
        var i = 0
        while (i < n) {
            count++
            val limit = xs[i] + w
            i++
            while (i < n && xs[i] <= limit) {
                i++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int minRectanglesToCoverPoints(List<List<int>> points, int w) {
    List<int> xs = points.map((p) => p[0]).toList();
    xs.sort();
    int count = 0;
    int i = 0;
    while (i < xs.length) {
      int start = xs[i];
      int limit = start + w;
      count++;
      i++;
      while (i < xs.length && xs[i] <= limit) {
        i++;
      }
    }
    return count;
  }
}
```

## Golang

```go
package main

import "sort"

func minRectanglesToCoverPoints(points [][]int, w int) int {
	n := len(points)
	xs := make([]int, n)
	for i, p := range points {
		xs[i] = p[0]
	}
	sort.Ints(xs)

	count := 0
	i := 0
	for i < n {
		limit := xs[i] + w
		count++
		i++
		for i < n && xs[i] <= limit {
			i++
		}
	}
	return count
}
```

## Ruby

```ruby
def min_rectangles_to_cover_points(points, w)
  xs = points.map { |p| p[0] }
  xs.sort!
  count = 0
  i = 0
  n = xs.length
  while i < n
    limit = xs[i] + w
    count += 1
    i += 1 while i < n && xs[i] <= limit
  end
  count
end
```

## Scala

```scala
object Solution {
    def minRectanglesToCoverPoints(points: Array[Array[Int]], w: Int): Int = {
        val n = points.length
        val xs = new Array[Int](n)
        var i = 0
        while (i < n) {
            xs(i) = points(i)(0)
            i += 1
        }
        java.util.Arrays.sort(xs)

        var rects = 0
        var idx = 0
        val wLong = w.toLong
        while (idx < n) {
            val left = xs(idx).toLong
            rects += 1
            val limit = left + wLong
            while (idx < n && xs(idx).toLong <= limit) {
                idx += 1
            }
        }
        rects
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_rectangles_to_cover_points(points: Vec<Vec<i32>>, w: i32) -> i32 {
        let mut xs: Vec<i64> = points.iter().map(|p| p[0] as i64).collect();
        xs.sort_unstable();
        let w_i64 = w as i64;
        let mut count = 0i32;
        let mut i = 0usize;
        let n = xs.len();
        while i < n {
            let start = xs[i];
            let limit = start + w_i64;
            count += 1;
            i += 1;
            while i < n && xs[i] <= limit {
                i += 1;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (min-rectangles-to-cover-points points w)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((xs (map car points))
         (sorted-xs (sort xs <)))
    (define (skip lst limit)
      (if (or (null? lst) (> (car lst) limit))
          lst
          (skip (cdr lst) limit)))
    (let recur ((lst sorted-xs) (cnt 0))
      (if (null? lst)
          cnt
          (let* ((start (car lst))
                 (limit (+ start w))
                 (rest (skip (cdr lst) limit)))
            (recur rest (+ cnt 1)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_rectangles_to_cover_points/2]).

-spec min_rectangles_to_cover_points(Points :: [[integer()]], W :: integer()) -> integer().
min_rectangles_to_cover_points(Points, W) ->
    Xs = [X || [X,_] <- Points],
    Sorted = lists:sort(Xs),
    count_intervals(Sorted, W, 0).

count_intervals([], _W, Count) -> Count;
count_intervals([H|T], W, Count) ->
    Limit = H + W,
    Rest = skip_until(T, Limit),
    count_intervals(Rest, W, Count + 1).

skip_until([], _Limit) -> [];
skip_until([X|Xs], Limit) when X =< Limit -> skip_until(Xs, Limit);
skip_until(L, _Limit) -> L.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_rectangles_to_cover_points(points :: [[integer]], w :: integer) :: integer
  def min_rectangles_to_cover_points(points, w) do
    points
    |> Enum.map(fn [x, _y] -> x end)
    |> Enum.sort()
    |> count_intervals(w)
  end

  defp count_intervals([], _w), do: 0

  defp count_intervals([head | tail], w) do
    limit = head + w

    {remaining, _} =
      Enum.split_while(tail, fn x -> x <= limit end)

    1 + count_intervals(remaining, w)
  end
end
```

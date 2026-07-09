# 0452. Minimum Number of Arrows to Burst Balloons

## Cpp

```cpp
class Solution {
public:
    int findMinArrowShots(std::vector<std::vector<int>>& points) {
        if (points.empty()) return 0;
        std::sort(points.begin(), points.end(),
                  [](const std::vector<int>& a, const std::vector<int>& b) {
                      return a[1] < b[1];
                  });
        int arrows = 1;
        int current_end = points[0][1];
        for (size_t i = 1; i < points.size(); ++i) {
            if (points[i][0] > current_end) {
                ++arrows;
                current_end = points[i][1];
            }
        }
        return arrows;
    }
};
```

## Java

```java
class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points == null || points.length == 0) return 0;
        java.util.Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));
        int arrows = 1;
        int arrowPos = points[0][1];
        for (int i = 1; i < points.length; i++) {
            if (points[i][0] > arrowPos) {
                arrows++;
                arrowPos = points[i][1];
            }
        }
        return arrows;
    }
}
```

## Python

```python
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        # Sort intervals by their end coordinate
        points.sort(key=lambda x: x[1])
        arrows = 1
        current_end = points[0][1]
        for start, end in points[1:]:
            if start > current_end:
                arrows += 1
                current_end = end
        return arrows
```

## Python3

```python
class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        current_end = points[0][1]
        for start, end in points[1:]:
            if start > current_end:
                arrows += 1
                current_end = end
        return arrows
```

## C

```c
#include <stdlib.h>

static int cmp(const void *a, const void *b) {
    int *ia = *(int **)a;
    int *ib = *(int **)b;
    if (ia[1] < ib[1]) return -1;
    if (ia[1] > ib[1]) return 1;
    return 0;
}

int findMinArrowShots(int** points, int pointsSize, int* pointsColSize) {
    if (pointsSize == 0) return 0;
    qsort(points, pointsSize, sizeof(int *), cmp);
    int arrows = 1;
    int current_end = points[0][1];
    for (int i = 1; i < pointsSize; ++i) {
        if (points[i][0] <= current_end) continue;
        arrows++;
        current_end = points[i][1];
    }
    return arrows;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindMinArrowShots(int[][] points)
    {
        if (points == null || points.Length == 0) return 0;

        Array.Sort(points, (a, b) => a[1].CompareTo(b[1]));

        int arrows = 1;
        int currentEnd = points[0][1];

        for (int i = 1; i < points.Length; i++)
        {
            if (points[i][0] > currentEnd)
            {
                arrows++;
                currentEnd = points[i][1];
            }
        }

        return arrows;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    if (!points || points.length === 0) return 0;
    
    // Sort intervals by their ending coordinate
    points.sort((a, b) => a[1] - b[1]);
    
    let arrows = 1;                     // At least one arrow needed for the first balloon
    let currentEnd = points[0][1];      // Position of the last arrow shot
    
    for (let i = 1; i < points.length; i++) {
        const [start, end] = points[i];
        if (start > currentEnd) {       // No overlap, need a new arrow
            arrows++;
            currentEnd = end;
        }
        // else: overlapping interval, current arrow still works
    }
    
    return arrows;
};
```

## Typescript

```typescript
function findMinArrowShots(points: number[][]): number {
    if (points.length === 0) return 0;
    points.sort((a, b) => a[1] - b[1]);
    let arrows = 1;
    let currentEnd = points[0][1];
    for (let i = 1; i < points.length; i++) {
        if (points[i][0] > currentEnd) {
            arrows++;
            currentEnd = points[i][1];
        }
    }
    return arrows;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function findMinArrowShots($points) {
        if (empty($points)) {
            return 0;
        }
        usort($points, function ($a, $b) {
            if ($a[1] == $b[1]) {
                return 0;
            }
            return ($a[1] < $b[1]) ? -1 : 1;
        });
        $arrows = 1;
        $arrowPos = $points[0][1];
        foreach ($points as $i => $interval) {
            if ($i == 0) continue;
            if ($interval[0] > $arrowPos) {
                $arrows++;
                $arrowPos = $interval[1];
            }
        }
        return $arrows;
    }
}
```

## Swift

```swift
class Solution {
    func findMinArrowShots(_ points: [[Int]]) -> Int {
        guard !points.isEmpty else { return 0 }
        let sorted = points.sorted { $0[1] < $1[1] }
        var arrows = 1
        var currentEnd = sorted[0][1]
        for i in 1..<sorted.count {
            if sorted[i][0] > currentEnd {
                arrows += 1
                currentEnd = sorted[i][1]
            }
        }
        return arrows
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMinArrowShots(points: Array<IntArray>): Int {
        if (points.isEmpty()) return 0
        points.sortWith(compareBy { it[1] })
        var arrows = 1
        var currentEnd = points[0][1]
        for (i in 1 until points.size) {
            if (points[i][0] > currentEnd) {
                arrows++
                currentEnd = points[i][1]
            }
        }
        return arrows
    }
}
```

## Dart

```dart
class Solution {
  int findMinArrowShots(List<List<int>> points) {
    if (points.isEmpty) return 0;
    points.sort((a, b) => a[1].compareTo(b[1]));
    int arrows = 1;
    int currentEnd = points[0][1];
    for (int i = 1; i < points.length; i++) {
      if (points[i][0] > currentEnd) {
        arrows++;
        currentEnd = points[i][1];
      }
    }
    return arrows;
  }
}
```

## Golang

```go
package main

import "sort"

func findMinArrowShots(points [][]int) int {
	if len(points) == 0 {
		return 0
	}
	sort.Slice(points, func(i, j int) bool {
		if points[i][1] == points[j][1] {
			return points[i][0] < points[j][0]
		}
		return points[i][1] < points[j][1]
	})
	arrows := 1
	end := points[0][1]
	for _, p := range points[1:] {
		if p[0] > end {
			arrows++
			end = p[1]
		}
	}
	return arrows
}
```

## Ruby

```ruby
def find_min_arrow_shots(points)
  return 0 if points.empty?
  points.sort_by! { |p| p[1] }
  arrows = 0
  current_end = -Float::INFINITY
  points.each do |start_x, end_x|
    if start_x > current_end
      arrows += 1
      current_end = end_x
    end
  end
  arrows
end
```

## Scala

```scala
object Solution {
    def findMinArrowShots(points: Array[Array[Int]]): Int = {
        if (points.isEmpty) return 0
        val sorted = points.sortBy(_(1))
        var arrows = 1
        var currentEnd = sorted(0)(1)
        for (i <- 1 until sorted.length) {
            if (sorted(i)(0) > currentEnd) {
                arrows += 1
                currentEnd = sorted(i)(1)
            }
        }
        arrows
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_min_arrow_shots(points: Vec<Vec<i32>>) -> i32 {
        if points.is_empty() {
            return 0;
        }
        let mut intervals: Vec<(i32, i32)> = points.into_iter().map(|v| (v[0], v[1])).collect();
        intervals.sort_unstable_by_key(|&(_, end)| end);
        let mut arrows = 1;
        let mut current_end = intervals[0].1;
        for &(start, end) in intervals.iter().skip(1) {
            if start > current_end {
                arrows += 1;
                current_end = end;
            }
        }
        arrows
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (find-min-arrow-shots points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (if (null? points)
      0
      (let* ([sorted (sort points (lambda (a b) (< (second a) (second b))))])
        (let loop ((remaining sorted) (arrows 0) (current-end #f))
          (cond
            [(null? remaining) arrows]
            [else
             (define start (first (car remaining)))
             (define end   (second (car remaining)))
             (if (or (not current-end) (> start current-end))
                 (loop (cdr remaining) (+ arrows 1) end)
                 (loop (cdr remaining) arrows current-end))])))))
```

## Erlang

```erlang
-spec find_min_arrow_shots(Points :: [[integer()]]) -> integer().
find_min_arrow_shots(Points) ->
    case Points of
        [] -> 0;
        _ ->
            Sorted = lists:sort(fun(A, B) -> element(2, A) =< element(2, B) end, Points),
            [{_, FirstEnd} | Rest] = Sorted,
            {Count, _} = lists:foldl(
                fun([Start, End], {Cnt, CurrEnd}) ->
                    if
                        Start =< CurrEnd -> {Cnt, CurrEnd};
                        true -> {Cnt + 1, End}
                    end
                end,
                {1, FirstEnd},
                Rest),
            Count
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_min_arrow_shots(points :: [[integer]]) :: integer
  def find_min_arrow_shots(points) do
    case points do
      [] -> 0
      _ ->
        sorted = Enum.sort_by(points, fn [_s, e] -> e end)

        {count, _} =
          Enum.reduce(sorted, {0, nil}, fn [s, e], {cnt, cur_end} ->
            if is_nil(cur_end) or s > cur_end do
              {cnt + 1, e}
            else
              {cnt, cur_end}
            end
          end)

        count
    end
  end
end
```

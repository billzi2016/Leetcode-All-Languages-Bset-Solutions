# 1266. Minimum Time Visiting All Points

## Cpp

```cpp
class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int total = 0;
        for (size_t i = 1; i < points.size(); ++i) {
            int dx = abs(points[i][0] - points[i-1][0]);
            int dy = abs(points[i][1] - points[i-1][1]);
            total += max(dx, dy);
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int total = 0;
        for (int i = 0; i < points.length - 1; i++) {
            int dx = Math.abs(points[i + 1][0] - points[i][0]);
            int dy = Math.abs(points[i + 1][1] - points[i][1]);
            total += Math.max(dx, dy);
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            total += max(abs(x2 - x1), abs(y2 - y1))
        return total
```

## Python3

```python
from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            total += max(abs(x2 - x1), abs(y2 - y1))
        return total
```

## C

```c
int minTimeToVisitAllPoints(int** points, int pointsSize, int* pointsColSize) {
    int total = 0;
    for (int i = 0; i < pointsSize - 1; ++i) {
        int dx = points[i + 1][0] - points[i][0];
        if (dx < 0) dx = -dx;
        int dy = points[i + 1][1] - points[i][1];
        if (dy < 0) dy = -dy;
        total += dx > dy ? dx : dy;
    }
    return total;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinTimeToVisitAllPoints(int[][] points)
    {
        int total = 0;
        for (int i = 0; i < points.Length - 1; i++)
        {
            int dx = Math.Abs(points[i + 1][0] - points[i][0]);
            int dy = Math.Abs(points[i + 1][1] - points[i][1]);
            total += Math.Max(dx, dy);
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var minTimeToVisitAllPoints = function(points) {
    let total = 0;
    for (let i = 0; i < points.length - 1; ++i) {
        const dx = Math.abs(points[i + 1][0] - points[i][0]);
        const dy = Math.abs(points[i + 1][1] - points[i][1]);
        total += Math.max(dx, dy);
    }
    return total;
};
```

## Typescript

```typescript
function minTimeToVisitAllPoints(points: number[][]): number {
    let total = 0;
    for (let i = 0; i < points.length - 1; ++i) {
        const dx = Math.abs(points[i + 1][0] - points[i][0]);
        const dy = Math.abs(points[i + 1][1] - points[i][1]);
        total += Math.max(dx, dy);
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function minTimeToVisitAllPoints($points) {
        $total = 0;
        $n = count($points);
        for ($i = 0; $i < $n - 1; $i++) {
            $dx = abs($points[$i + 1][0] - $points[$i][0]);
            $dy = abs($points[$i + 1][1] - $points[$i][1]);
            $total += max($dx, $dy);
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func minTimeToVisitAllPoints(_ points: [[Int]]) -> Int {
        var total = 0
        for i in 0..<(points.count - 1) {
            let dx = abs(points[i + 1][0] - points[i][0])
            let dy = abs(points[i + 1][1] - points[i][1])
            total += max(dx, dy)
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minTimeToVisitAllPoints(points: Array<IntArray>): Int {
        var total = 0
        for (i in 0 until points.size - 1) {
            val dx = kotlin.math.abs(points[i + 1][0] - points[i][0])
            val dy = kotlin.math.abs(points[i + 1][1] - points[i][1])
            total += maxOf(dx, dy)
        }
        return total
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int minTimeToVisitAllPoints(List<List<int>> points) {
    int total = 0;
    for (int i = 0; i < points.length - 1; i++) {
      int dx = (points[i + 1][0] - points[i][0]).abs();
      int dy = (points[i + 1][1] - points[i][1]).abs();
      total += max(dx, dy);
    }
    return total;
  }
}
```

## Golang

```go
func minTimeToVisitAllPoints(points [][]int) int {
	total := 0
	for i := 0; i+1 < len(points); i++ {
		dx := points[i+1][0] - points[i][0]
		if dx < 0 {
			dx = -dx
		}
		dy := points[i+1][1] - points[i][1]
		if dy < 0 {
			dy = -dy
		}
		if dx > dy {
			total += dx
		} else {
			total += dy
		}
	}
	return total
}
```

## Ruby

```ruby
def min_time_to_visit_all_points(points)
  time = 0
  (0...points.length - 1).each do |i|
    dx = (points[i + 1][0] - points[i][0]).abs
    dy = (points[i + 1][1] - points[i][1]).abs
    time += [dx, dy].max
  end
  time
end
```

## Scala

```scala
object Solution {
    def minTimeToVisitAllPoints(points: Array[Array[Int]]): Int = {
        var total = 0
        for (i <- 0 until points.length - 1) {
            val dx = math.abs(points(i + 1)(0) - points(i)(0))
            val dy = math.abs(points(i + 1)(1) - points(i)(1))
            total += math.max(dx, dy)
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        let mut ans = 0;
        for i in 0..points.len().saturating_sub(1) {
            let dx = (points[i + 1][0] - points[i][0]).abs();
            let dy = (points[i + 1][1] - points[i][1]).abs();
            ans += std::cmp::max(dx, dy);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-time-to-visit-all-points points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let loop ((remaining points) (prev #f) (total 0))
    (if (null? remaining)
        total
        (if prev
            (let* ((dx (abs (- (first remaining) (first prev))))
                   (dy (abs (- (second remaining) (second prev)))))
              (loop (cdr remaining) remaining (+ total (max dx dy))))
            (loop (cdr remaining) remaining total)))))
```

## Erlang

```erlang
-module(solution).
-export([min_time_to_visit_all_points/1]).

-spec min_time_to_visit_all_points(Points :: [[integer()]]) -> integer().
min_time_to_visit_all_points([]) ->
    0;
min_time_to_visit_all_points([_]) ->
    0;
min_time_to_visit_all_points(Points) ->
    min_time_to_visit_all_points(Points, 0).

min_time_to_visit_all_points([[X1,Y1],[X2,Y2]|Rest], Acc) ->
    Dx = abs(X2 - X1),
    Dy = abs(Y2 - Y1),
    NewAcc = Acc + max(Dx, Dy),
    min_time_to_visit_all_points([[X2,Y2]|Rest], NewAcc);
min_time_to_visit_all_points([_], Acc) ->
    Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_time_to_visit_all_points(points :: [[integer]]) :: integer
  def min_time_to_visit_all_points(points) do
    points
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.reduce(0, fn [p1, p2], acc ->
      [x1, y1] = p1
      [x2, y2] = p2
      dx = abs(x2 - x1)
      dy = abs(y2 - y1)
      acc + max(dx, dy)
    end)
  end
end
```

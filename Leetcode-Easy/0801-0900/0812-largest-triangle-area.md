# 0812. Largest Triangle Area

## Cpp

```cpp
class Solution {
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        int n = points.size();
        double maxArea = 0.0;
        for (int i = 0; i < n; ++i) {
            long long x1 = points[i][0];
            long long y1 = points[i][1];
            for (int j = i + 1; j < n; ++j) {
                long long x2 = points[j][0];
                long long y2 = points[j][1];
                for (int k = j + 1; k < n; ++k) {
                    long long x3 = points[k][0];
                    long long y3 = points[k][1];
                    // Compute twice the area using cross product
                    long long cross = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2);
                    double area = std::abs(cross) / 2.0;
                    if (area > maxArea) maxArea = area;
                }
            }
        }
        return maxArea;
    }
};
```

## Java

```java
class Solution {
    public double largestTriangleArea(int[][] points) {
        int n = points.length;
        double maxArea = 0.0;
        for (int i = 0; i < n - 2; i++) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for (int j = i + 1; j < n - 1; j++) {
                int x2 = points[j][0];
                int y2 = points[j][1];
                for (int k = j + 1; k < n; k++) {
                    int x3 = points[k][0];
                    int y3 = points[k][1];
                    double area = Math.abs(
                        x1 * (y2 - y3) +
                        x2 * (y3 - y1) +
                        x3 * (y1 - y2)
                    ) / 2.0;
                    if (area > maxArea) {
                        maxArea = area;
                    }
                }
            }
        }
        return maxArea;
    }
}
```

## Python

```python
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = 0.0
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
                    if area > max_area:
                        max_area = area
        return max_area
```

## Python3

```python
from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        max_area = 0.0
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    area = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2.0
                    if area > max_area:
                        max_area = area
        return max_area
```

## C

```c
#include <stdlib.h>
#include <math.h>

double largestTriangleArea(int** points, int pointsSize, int* pointsColSize) {
    double maxArea = 0.0;
    for (int i = 0; i < pointsSize - 2; ++i) {
        long long x1 = points[i][0];
        long long y1 = points[i][1];
        for (int j = i + 1; j < pointsSize - 1; ++j) {
            long long x2 = points[j][0];
            long long y2 = points[j][1];
            for (int k = j + 1; k < pointsSize; ++k) {
                long long x3 = points[k][0];
                long long y3 = points[k][1];
                long long cross = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2);
                double area = fabs((double)cross) / 2.0;
                if (area > maxArea) {
                    maxArea = area;
                }
            }
        }
    }
    return maxArea;
}
```

## Csharp

```csharp
public class Solution {
    public double LargestTriangleArea(int[][] points) {
        int n = points.Length;
        double maxArea = 0.0;
        for (int i = 0; i < n - 2; i++) {
            var p1 = points[i];
            for (int j = i + 1; j < n - 1; j++) {
                var p2 = points[j];
                for (int k = j + 1; k < n; k++) {
                    var p3 = points[k];
                    double area = Math.Abs(
                        p1[0] * (p2[1] - p3[1]) +
                        p2[0] * (p3[1] - p1[1]) +
                        p3[0] * (p1[1] - p2[1])
                    ) / 2.0;
                    if (area > maxArea) {
                        maxArea = area;
                    }
                }
            }
        }
        return maxArea;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var largestTriangleArea = function(points) {
    const n = points.length;
    let maxArea = 0;
    for (let i = 0; i < n - 2; ++i) {
        const [x1, y1] = points[i];
        for (let j = i + 1; j < n - 1; ++j) {
            const [x2, y2] = points[j];
            for (let k = j + 1; k < n; ++k) {
                const [x3, y3] = points[k];
                // Shoelace formula / cross product magnitude
                const area = Math.abs(
                    x1 * (y2 - y3) +
                    x2 * (y3 - y1) +
                    x3 * (y1 - y2)
                ) / 2;
                if (area > maxArea) maxArea = area;
            }
        }
    }
    return maxArea;
};
```

## Typescript

```typescript
function largestTriangleArea(points: number[][]): number {
    const n = points.length;
    let maxArea = 0;
    for (let i = 0; i < n - 2; i++) {
        const [x1, y1] = points[i];
        for (let j = i + 1; j < n - 1; j++) {
            const [x2, y2] = points[j];
            for (let k = j + 1; k < n; k++) {
                const [x3, y3] = points[k];
                const area = Math.abs(
                    x1 * (y2 - y3) +
                    x2 * (y3 - y1) +
                    x3 * (y1 - y2)
                ) / 2;
                if (area > maxArea) {
                    maxArea = area;
                }
            }
        }
    }
    return maxArea;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Float
     */
    function largestTriangleArea($points) {
        $n = count($points);
        $maxArea = 0.0;
        for ($i = 0; $i < $n - 2; $i++) {
            [$x1, $y1] = $points[$i];
            for ($j = $i + 1; $j < $n - 1; $j++) {
                [$x2, $y2] = $points[$j];
                for ($k = $j + 1; $k < $n; $k++) {
                    [$x3, $y3] = $points[$k];
                    $area = abs($x1 * ($y2 - $y3) + $x2 * ($y3 - $y1) + $x3 * ($y1 - $y2)) / 2.0;
                    if ($area > $maxArea) {
                        $maxArea = $area;
                    }
                }
            }
        }
        return $maxArea;
    }
}
```

## Swift

```swift
class Solution {
    func largestTriangleArea(_ points: [[Int]]) -> Double {
        let n = points.count
        var maxArea: Double = 0.0
        for i in 0..<(n - 2) {
            let x1 = points[i][0]
            let y1 = points[i][1]
            for j in (i + 1)..<(n - 1) {
                let x2 = points[j][0]
                let y2 = points[j][1]
                for k in (j + 1)..<n {
                    let x3 = points[k][0]
                    let y3 = points[k][1]
                    let area = abs(Double(x1) * (Double(y2) - Double(y3)) +
                                   Double(x2) * (Double(y3) - Double(y1)) +
                                   Double(x3) * (Double(y1) - Double(y2))) / 2.0
                    if area > maxArea {
                        maxArea = area
                    }
                }
            }
        }
        return maxArea
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestTriangleArea(points: Array<IntArray>): Double {
        var maxArea = 0.0
        val n = points.size
        for (i in 0 until n - 2) {
            val p1 = points[i]
            for (j in i + 1 until n - 1) {
                val p2 = points[j]
                for (k in j + 1 until n) {
                    val p3 = points[k]
                    val area = kotlin.math.abs(
                        p1[0] * (p2[1] - p3[1]) +
                        p2[0] * (p3[1] - p1[1]) +
                        p3[0] * (p1[1] - p2[1])
                    ) / 2.0
                    if (area > maxArea) {
                        maxArea = area
                    }
                }
            }
        }
        return maxArea
    }
}
```

## Dart

```dart
class Solution {
  double largestTriangleArea(List<List<int>> points) {
    int n = points.length;
    double maxArea = 0.0;
    for (int i = 0; i < n - 2; ++i) {
      for (int j = i + 1; j < n - 1; ++j) {
        for (int k = j + 1; k < n; ++k) {
          int x1 = points[i][0];
          int y1 = points[i][1];
          int x2 = points[j][0];
          int y2 = points[j][1];
          int x3 = points[k][0];
          int y3 = points[k][1];
          double area = ((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)).abs()) / 2.0;
          if (area > maxArea) {
            maxArea = area;
          }
        }
      }
    }
    return maxArea;
  }
}
```

## Golang

```go
func largestTriangleArea(points [][]int) float64 {
    n := len(points)
    maxArea := 0.0
    for i := 0; i < n-2; i++ {
        x1, y1 := points[i][0], points[i][1]
        for j := i + 1; j < n-1; j++ {
            x2, y2 := points[j][0], points[j][1]
            for k := j + 1; k < n; k++ {
                x3, y3 := points[k][0], points[k][1]
                area := float64(abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))) / 2.0
                if area > maxArea {
                    maxArea = area
                }
            }
        }
    }
    return maxArea
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}
```

## Ruby

```ruby
def largest_triangle_area(points)
  max = 0.0
  n = points.length
  (0...n - 2).each do |i|
    (i + 1...n - 1).each do |j|
      (j + 1...n).each do |k|
        x1, y1 = points[i]
        x2, y2 = points[j]
        x3, y3 = points[k]
        area = ((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)).abs).to_f / 2.0
        max = area if area > max
      end
    end
  end
  max
end
```

## Scala

```scala
object Solution {
    def largestTriangleArea(points: Array[Array[Int]]): Double = {
        var maxArea = 0.0
        val n = points.length
        for (i <- 0 until n - 2) {
            val p1 = points(i)
            for (j <- i + 1 until n - 1) {
                val p2 = points(j)
                for (k <- j + 1 until n) {
                    val p3 = points(k)
                    val area = math.abs(
                        p1(0) * (p2(1) - p3(1)) +
                        p2(0) * (p3(1) - p1(1)) +
                        p3(0) * (p1(1) - p2(1))
                    ) / 2.0
                    if (area > maxArea) maxArea = area
                }
            }
        }
        maxArea
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_triangle_area(points: Vec<Vec<i32>>) -> f64 {
        let n = points.len();
        let mut max_area = 0.0_f64;
        for i in 0..n {
            let (x1, y1) = (points[i][0] as i64, points[i][1] as i64);
            for j in i + 1..n {
                let (x2, y2) = (points[j][0] as i64, points[j][1] as i64);
                for k in j + 1..n {
                    let (x3, y3) = (points[k][0] as i64, points[k][1] as i64);
                    let area2 = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)).abs();
                    let area = area2 as f64 / 2.0;
                    if area > max_area {
                        max_area = area;
                    }
                }
            }
        }
        max_area
    }
}
```

## Racket

```racket
(define/contract (largest-triangle-area points)
  (-> (listof (listof exact-integer?)) flonum?)
  (let* ((n (length points))
         (max-area
          (for*/fold ([max 0.0])
                     ([i (in-range n)]
                      [j (in-range (+ i 1) n)]
                      [k (in-range (+ j 1) n)])
            (define p1 (list-ref points i))
            (define p2 (list-ref points j))
            (define p3 (list-ref points k))
            (define x1 (first p1)) (define y1 (second p1))
            (define x2 (first p2)) (define y2 (second p2))
            (define x3 (first p3)) (define y3 (second p3))
            (define cross (- (* (- x2 x1) (- y3 y1))
                             (* (- x3 x1) (- y2 y1))))
            (define area (/ (abs cross) 2.0))
            (if (> area max) area max)))))
    max-area))
```

## Erlang

```erlang
-module(solution).
-export([largest_triangle_area/1]).

-spec largest_triangle_area(Points :: [[integer()]]) -> float().
largest_triangle_area(Points) ->
    max_area_i(Points, length(Points), 0, 0.0).

max_area_i(_Points, N, I, Max) when I >= N - 2 ->
    Max;
max_area_i(Points, N, I, Max) ->
    Max1 = max_area_j(Points, N, I, I + 1, Max),
    max_area_i(Points, N, I + 1, Max1).

max_area_j(_Points, N, _I, J, Max) when J >= N - 1 ->
    Max;
max_area_j(Points, N, I, J, Max) ->
    Max1 = max_area_k(Points, N, I, J, J + 1, Max),
    max_area_j(Points, N, I, J + 1, Max1).

max_area_k(_Points, N, _I, _J, K, Max) when K >= N ->
    Max;
max_area_k(Points, N, I, J, K, Max) ->
    Pi = lists:nth(I + 1, Points),
    Pj = lists:nth(J + 1, Points),
    Pk = lists:nth(K + 1, Points),
    Area = triangle_area(Pi, Pj, Pk),
    NewMax = if Area > Max -> Area; true -> Max end,
    max_area_k(Points, N, I, J, K + 1, NewMax).

triangle_area([X1,Y1], [X2,Y2], [X3,Y3]) ->
    Abs = abs((X2 - X1)*(Y3 - Y1) - (X3 - X1)*(Y2 - Y1)),
    Abs / 2.0.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_triangle_area(points :: [[integer]]) :: float
  def largest_triangle_area(points) do
    points
    |> Enum.combination(3)
    |> Enum.map(fn [p1, p2, p3] -> triangle_area(p1, p2, p3) end)
    |> Enum.max()
  end

  defp triangle_area([x1, y1], [x2, y2], [x3, y3]) do
    abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2.0
  end
end
```

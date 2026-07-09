# 1779. Find Nearest Point That Has the Same X or Y Coordinate

## Cpp

```cpp
class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int bestIdx = -1;
        int bestDist = INT_MAX;
        for (int i = 0; i < (int)points.size(); ++i) {
            int px = points[i][0];
            int py = points[i][1];
            if (px == x || py == y) {
                int dist = abs(px - x) + abs(py - y);
                if (dist < bestDist) {
                    bestDist = dist;
                    bestIdx = i;
                }
            }
        }
        return bestIdx;
    }
};
```

## Java

```java
class Solution {
    public int nearestValidPoint(int x, int y, int[][] points) {
        int bestIdx = -1;
        int minDist = Integer.MAX_VALUE;
        for (int i = 0; i < points.length; i++) {
            int px = points[i][0];
            int py = points[i][1];
            if (px == x || py == y) {
                int dist = Math.abs(px - x) + Math.abs(py - y);
                if (dist < minDist) {
                    minDist = dist;
                    bestIdx = i;
                }
            }
        }
        return bestIdx;
    }
}
```

## Python

```python
class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        min_dist = float('inf')
        ans = -1
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                dist = abs(a - x) + abs(b - y)
                if dist < min_dist:
                    min_dist = dist
                    ans = i
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        best_idx = -1
        best_dist = float('inf')
        for i, (px, py) in enumerate(points):
            if px == x or py == y:
                dist = abs(px - x) + abs(py - y)
                if dist < best_dist:
                    best_dist = dist
                    best_idx = i
        return best_idx
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int nearestValidPoint(int x, int y, int** points, int pointsSize, int* pointsColSize) {
    int ans = -1;
    int minDist = INT_MAX;
    for (int i = 0; i < pointsSize; ++i) {
        int xi = points[i][0];
        int yi = points[i][1];
        if (xi == x || yi == y) {
            int dist = abs(x - xi) + abs(y - yi);
            if (dist < minDist) {
                minDist = dist;
                ans = i;
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int NearestValidPoint(int x, int y, int[][] points)
    {
        int minDist = int.MaxValue;
        int answer = -1;

        for (int i = 0; i < points.Length; i++)
        {
            int px = points[i][0];
            int py = points[i][1];

            if (px == x || py == y)
            {
                int dist = Math.Abs(px - x) + Math.Abs(py - y);
                if (dist < minDist)
                {
                    minDist = dist;
                    answer = i;
                }
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} x
 * @param {number} y
 * @param {number[][]} points
 * @return {number}
 */
var nearestValidPoint = function(x, y, points) {
    let bestIdx = -1;
    let minDist = Infinity;
    for (let i = 0; i < points.length; i++) {
        const [px, py] = points[i];
        if (px === x || py === y) {
            const dist = Math.abs(px - x) + Math.abs(py - y);
            if (dist < minDist) {
                minDist = dist;
                bestIdx = i;
            }
        }
    }
    return bestIdx;
};
```

## Typescript

```typescript
function nearestValidPoint(x: number, y: number, points: number[][]): number {
    let bestIdx = -1;
    let bestDist = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < points.length; i++) {
        const [a, b] = points[i];
        if (a === x || b === y) {
            const dist = Math.abs(a - x) + Math.abs(b - y);
            if (dist < bestDist) {
                bestDist = dist;
                bestIdx = i;
            }
        }
    }
    return bestIdx;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $x
     * @param Integer $y
     * @param Integer[][] $points
     * @return Integer
     */
    function nearestValidPoint($x, $y, $points) {
        $minDist = PHP_INT_MAX;
        $answer = -1;
        foreach ($points as $i => $p) {
            if ($p[0] == $x || $p[1] == $y) {
                $dist = abs($x - $p[0]) + abs($y - $p[1]);
                if ($dist < $minDist) {
                    $minDist = $dist;
                    $answer = $i;
                }
            }
        }
        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func nearestValidPoint(_ x: Int, _ y: Int, _ points: [[Int]]) -> Int {
        var minDist = Int.max
        var answer = -1
        for (i, p) in points.enumerated() {
            let a = p[0]
            let b = p[1]
            if a == x || b == y {
                let dist = abs(a - x) + abs(b - y)
                if dist < minDist {
                    minDist = dist
                    answer = i
                }
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun nearestValidPoint(x: Int, y: Int, points: Array<IntArray>): Int {
        var minDist = Int.MAX_VALUE
        var answer = -1
        for (i in points.indices) {
            val px = points[i][0]
            val py = points[i][1]
            if (px == x || py == y) {
                val dist = kotlin.math.abs(px - x) + kotlin.math.abs(py - y)
                if (dist < minDist) {
                    minDist = dist
                    answer = i
                }
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int nearestValidPoint(int x, int y, List<List<int>> points) {
    int minDist = 1 << 30;
    int ans = -1;
    for (int i = 0; i < points.length; i++) {
      final p = points[i];
      if (p[0] == x || p[1] == y) {
        int dist = (p[0] - x).abs() + (p[1] - y).abs();
        if (dist < minDist) {
          minDist = dist;
          ans = i;
        }
      }
    }
    return ans;
  }
}
```

## Golang

```go
func nearestValidPoint(x int, y int, points [][]int) int {
    minDist := int(^uint(0) >> 1)
    ans := -1
    for i, p := range points {
        if p[0] == x || p[1] == y {
            dist := abs(p[0]-x) + abs(p[1]-y)
            if dist < minDist {
                minDist = dist
                ans = i
            }
        }
    }
    return ans
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
# @param {Integer} x
# @param {Integer} y
# @param {Integer[][]} points
# @return {Integer}
def nearest_valid_point(x, y, points)
  min_dist = Float::INFINITY
  answer = -1

  points.each_with_index do |(px, py), idx|
    next unless px == x || py == y
    dist = (px - x).abs + (py - y).abs
    if dist < min_dist
      min_dist = dist
      answer = idx
    end
  end

  answer
end
```

## Scala

```scala
object Solution {
    def nearestValidPoint(x: Int, y: Int, points: Array[Array[Int]]): Int = {
        var bestIdx = -1
        var bestDist = Int.MaxValue
        for (i <- points.indices) {
            val px = points(i)(0)
            val py = points(i)(1)
            if (px == x || py == y) {
                val dist = math.abs(px - x) + math.abs(py - y)
                if (dist < bestDist) {
                    bestDist = dist
                    bestIdx = i
                }
            }
        }
        bestIdx
    }
}
```

## Rust

```rust
impl Solution {
    pub fn nearest_valid_point(x: i32, y: i32, points: Vec<Vec<i32>>) -> i32 {
        let mut best = i32::MAX;
        let mut ans = -1;
        for (i, p) in points.iter().enumerate() {
            if p[0] == x || p[1] == y {
                let d = (p[0] - x).abs() + (p[1] - y).abs();
                if d < best {
                    best = d;
                    ans = i as i32;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (nearest-valid-point x y points)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let loop ((pts points) (idx 0) (best -1) (best-dist +inf.0))
    (if (null? pts)
        best
        (let* ((pt (car pts))
               (a (first pt))
               (b (second pt)))
          (if (or (= a x) (= b y))
              (let ((dist (+ (abs (- a x)) (abs (- b y)))))
                (if (< dist best-dist)
                    (loop (cdr pts) (add1 idx) idx dist)
                    (loop (cdr pts) (add1 idx) best best-dist)))
              (loop (cdr pts) (add1 idx) best best-dist))))))
```

## Erlang

```erlang
-spec nearest_valid_point(X :: integer(), Y :: integer(), Points :: [[integer()]]) -> integer().
nearest_valid_point(X, Y, Points) ->
    loop(Points, X, Y, 0, 16#7fffffff, -1).

loop([], _X, _Y, _Idx, _BestDist, BestIdx) ->
    BestIdx;
loop([[A, B] | Rest], X, Y, Idx, BestDist, BestIdx) ->
    case (A =:= X orelse B =:= Y) of
        true ->
            Dist = erlang:abs(A - X) + erlang:abs(B - Y),
            if Dist < BestDist ->
                    loop(Rest, X, Y, Idx + 1, Dist, Idx);
               true ->
                    loop(Rest, X, Y, Idx + 1, BestDist, BestIdx)
            end;
        false ->
            loop(Rest, X, Y, Idx + 1, BestDist, BestIdx)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec nearest_valid_point(x :: integer, y :: integer, points :: [[integer]]) :: integer
  def nearest_valid_point(x, y, points) do
    {_, answer} =
      Enum.reduce(Enum.with_index(points), {nil, -1}, fn {[a, b], idx}, {min_dist, ans_idx} ->
        if a == x or b == y do
          dist = abs(a - x) + abs(b - y)

          case min_dist do
            nil -> {dist, idx}
            d when dist < d -> {dist, idx}
            _ -> {min_dist, ans_idx}
          end
        else
          {min_dist, ans_idx}
        end
      end)

    answer
  end
end
```

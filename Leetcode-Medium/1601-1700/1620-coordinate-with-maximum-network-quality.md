# 1620. Coordinate With Maximum Network Quality

## Cpp

```cpp
class Solution {
public:
    vector<int> bestCoordinate(vector<vector<int>>& towers, int radius) {
        int maxX = 0, maxY = 0;
        for (auto &t : towers) {
            maxX = max(maxX, t[0]);
            maxY = max(maxY, t[1]);
        }
        maxX += radius;
        maxY += radius;
        long long bestSum = -1;
        int bestX = 0, bestY = 0;
        double rad = static_cast<double>(radius);
        for (int x = 0; x <= maxX; ++x) {
            for (int y = 0; y <= maxY; ++y) {
                long long sum = 0;
                for (auto &t : towers) {
                    int tx = t[0], ty = t[1], q = t[2];
                    double dx = x - tx;
                    double dy = y - ty;
                    double d = sqrt(dx * dx + dy * dy);
                    if (d <= rad) {
                        sum += static_cast<int>(q / (1.0 + d));
                    }
                }
                if (sum > bestSum || (sum == bestSum && (x < bestX || (x == bestX && y < bestY)))) {
                    bestSum = sum;
                    bestX = x;
                    bestY = y;
                }
            }
        }
        return {bestX, bestY};
    }
};
```

## Java

```java
class Solution {
    public int[] bestCoordinate(int[][] towers, int radius) {
        int maxX = 0, maxY = 0;
        for (int[] t : towers) {
            maxX = Math.max(maxX, t[0]);
            maxY = Math.max(maxY, t[1]);
        }
        maxX += radius;
        maxY += radius;
        double r2 = radius * radius;

        int bestX = 0, bestY = 0, bestQuality = 0;

        for (int x = 0; x <= maxX; x++) {
            for (int y = 0; y <= maxY; y++) {
                int total = 0;
                for (int[] t : towers) {
                    long dx = x - t[0];
                    long dy = y - t[1];
                    double distSq = dx * dx + dy * dy;
                    if (distSq <= r2) {
                        double d = Math.sqrt(distSq);
                        int contrib = (int) Math.floor(t[2] / (1.0 + d));
                        total += contrib;
                    }
                }
                if (total > bestQuality || (total == bestQuality && (x < bestX || (x == bestX && y < bestY)))) {
                    bestQuality = total;
                    bestX = x;
                    bestY = y;
                }
            }
        }

        return new int[]{bestX, bestY};
    }
}
```

## Python

```python
import math

class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """
        max_q = -1
        ans = [0, 0]
        max_x = max(t[0] for t in towers) + radius
        max_y = max(t[1] for t in towers) + radius
        r_sq = radius * radius

        for x in range(max_x + 1):
            for y in range(max_y + 1):
                total = 0
                for tx, ty, q in towers:
                    dx = x - tx
                    dy = y - ty
                    dist_sq = dx * dx + dy * dy
                    if dist_sq <= r_sq:
                        d = math.sqrt(dist_sq)
                        total += int(q / (1 + d))
                if total > max_q or (total == max_q and (x < ans[0] or (x == ans[0] and y < ans[1]))):
                    max_q = total
                    ans = [x, y]
        return ans
```

## Python3

```python
import math
from typing import List

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_quality = -1
        best_x = 0
        best_y = 0
        limit = 51 + radius  # coordinates up to 50 plus possible radius extension
        r_sq = radius * radius
        for x in range(limit):
            for y in range(limit):
                total = 0
                for tx, ty, q in towers:
                    dx = tx - x
                    dy = ty - y
                    dist_sq = dx * dx + dy * dy
                    if dist_sq <= r_sq:
                        d = math.sqrt(dist_sq)
                        total += int(q / (1 + d))
                if total > max_quality or (total == max_quality and (x < best_x or (x == best_x and y < best_y))):
                    max_quality = total
                    best_x, best_y = x, y
        return [best_x, best_y]
```

## C

```c
#include <stdlib.h>
#include <math.h>

int* bestCoordinate(int** towers, int towersSize, int* towersColSize, int radius, int* returnSize) {
    int maxX = 0, maxY = 0;
    for (int i = 0; i < towersSize; ++i) {
        if (towers[i][0] > maxX) maxX = towers[i][0];
        if (towers[i][1] > maxY) maxY = towers[i][1];
    }
    int limit = (maxX > maxY ? maxX : maxY) + radius;
    long bestQuality = -1;
    int bestX = 0, bestY = 0;

    int rSq = radius * radius;

    for (int x = 0; x <= limit; ++x) {
        for (int y = 0; y <= limit; ++y) {
            long total = 0;
            for (int i = 0; i < towersSize; ++i) {
                int tx = towers[i][0];
                int ty = towers[i][1];
                int q  = towers[i][2];
                int dx = tx - x;
                int dy = ty - y;
                int distSq = dx * dx + dy * dy;
                if (distSq > rSq) continue;
                double d = sqrt((double)distSq);
                total += (int)(q / (1.0 + d));
            }
            if (total > bestQuality ||
               (total == bestQuality && (x < bestX || (x == bestX && y < bestY)))) {
                bestQuality = total;
                bestX = x;
                bestY = y;
            }
        }
    }

    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = bestX;
    ans[1] = bestY;
    *returnSize = 2;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] BestCoordinate(int[][] towers, int radius)
    {
        int maxX = 0, maxY = 0;
        foreach (var t in towers)
        {
            if (t[0] > maxX) maxX = t[0];
            if (t[1] > maxY) maxY = t[1];
        }

        int limitX = maxX + radius;
        int limitY = maxY + radius;
        double r = radius;

        int bestQuality = -1;
        int bestX = 0, bestY = 0;

        for (int x = 0; x <= limitX; x++)
        {
            for (int y = 0; y <= limitY; y++)
            {
                int total = 0;
                foreach (var t in towers)
                {
                    int dx = x - t[0];
                    int dy = y - t[1];
                    double dist = Math.Sqrt(dx * dx + dy * dy);
                    if (dist <= r)
                    {
                        total += (int)Math.Floor(t[2] / (1.0 + dist));
                    }
                }

                if (total > bestQuality || (total == bestQuality && (x < bestX || (x == bestX && y < bestY))))
                {
                    bestQuality = total;
                    bestX = x;
                    bestY = y;
                }
            }
        }

        return new int[] { bestX, bestY };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} towers
 * @param {number} radius
 * @return {number[]}
 */
var bestCoordinate = function(towers, radius) {
    let maxX = 0, maxY = 0;
    for (const [x, y] of towers) {
        if (x > maxX) maxX = x;
        if (y > maxY) maxY = y;
    }
    const limitX = maxX + radius;
    const limitY = maxY + radius;

    let best = [0, 0];
    let bestQuality = -1;

    for (let cx = 0; cx <= limitX; ++cx) {
        for (let cy = 0; cy <= limitY; ++cy) {
            let total = 0;
            for (const [tx, ty, q] of towers) {
                const dx = tx - cx;
                const dy = ty - cy;
                const d = Math.sqrt(dx * dx + dy * dy);
                if (d <= radius) {
                    total += Math.floor(q / (1 + d));
                }
            }
            if (
                total > bestQuality ||
                (total === bestQuality && (cx < best[0] || (cx === best[0] && cy < best[1])))
            ) {
                bestQuality = total;
                best = [cx, cy];
            }
        }
    }

    return best;
};
```

## Typescript

```typescript
function bestCoordinate(towers: number[][], radius: number): number[] {
    let maxX = 0;
    let maxY = 0;
    for (const [x, y] of towers) {
        if (x > maxX) maxX = x;
        if (y > maxY) maxY = y;
    }
    const limitX = maxX + radius;
    const limitY = maxY + radius;

    let bestSum = -1;
    let bestCoord: number[] = [0, 0];

    for (let cx = 0; cx <= limitX; cx++) {
        for (let cy = 0; cy <= limitY; cy++) {
            let sum = 0;
            for (const [tx, ty, q] of towers) {
                const dx = cx - tx;
                const dy = cy - ty;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist <= radius) {
                    sum += Math.floor(q / (1 + dist));
                }
            }
            if (
                sum > bestSum ||
                (sum === bestSum && (cx < bestCoord[0] || (cx === bestCoord[0] && cy < bestCoord[1])))
            ) {
                bestSum = sum;
                bestCoord = [cx, cy];
            }
        }
    }

    return bestCoord;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $towers
     * @param Integer $radius
     * @return Integer[]
     */
    function bestCoordinate($towers, $radius) {
        $maxX = 0;
        $maxY = 0;
        foreach ($towers as $tower) {
            $maxX = max($maxX, $tower[0] + $radius);
            $maxY = max($maxY, $tower[1] + $radius);
        }

        $bestQuality = -1;
        $bestCoord = [0, 0];

        for ($x = 0; $x <= $maxX; $x++) {
            for ($y = 0; $y <= $maxY; $y++) {
                $total = 0;
                foreach ($towers as $tower) {
                    $dx = $tower[0] - $x;
                    $dy = $tower[1] - $y;
                    $dist = sqrt($dx * $dx + $dy * $dy);
                    if ($dist <= $radius) {
                        $total += (int) floor($tower[2] / (1 + $dist));
                    }
                }

                if (
                    $total > $bestQuality ||
                    ($total == $bestQuality && ($x < $bestCoord[0] || ($x == $bestCoord[0] && $y < $bestCoord[1])))
                ) {
                    $bestQuality = $total;
                    $bestCoord = [$x, $y];
                }
            }
        }

        return $bestCoord;
    }
}
```

## Swift

```swift
class Solution {
    func bestCoordinate(_ towers: [[Int]], _ radius: Int) -> [Int] {
        var bestQuality = -1
        var bestX = 0
        var bestY = 0
        let maxCoord = 50 + radius
        let rDouble = Double(radius)
        
        for x in 0...maxCoord {
            for y in 0...maxCoord {
                var total = 0
                for tower in towers {
                    let tx = tower[0]
                    let ty = tower[1]
                    let q = tower[2]
                    let dx = Double(x - tx)
                    let dy = Double(y - ty)
                    let dist = sqrt(dx * dx + dy * dy)
                    if dist <= rDouble {
                        total += Int(floor(Double(q) / (1.0 + dist)))
                    }
                }
                if total > bestQuality || (total == bestQuality && (x < bestX || (x == bestX && y < bestY))) {
                    bestQuality = total
                    bestX = x
                    bestY = y
                }
            }
        }
        return [bestX, bestY]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun bestCoordinate(towers: Array<IntArray>, radius: Int): IntArray {
        var maxQuality = -1
        var bestX = 0
        var bestY = 0
        val r2 = radius * radius

        var minX = Int.MAX_VALUE
        var maxX = Int.MIN_VALUE
        var minY = Int.MAX_VALUE
        var maxY = Int.MIN_VALUE
        for (t in towers) {
            val x = t[0]
            val y = t[1]
            if (x < minX) minX = x
            if (x > maxX) maxX = x
            if (y < minY) minY = y
            if (y > maxY) maxY = y
        }

        val startX = 0
        val endX = maxX + radius
        val startY = 0
        val endY = maxY + radius

        for (cx in startX..endX) {
            for (cy in startY..endY) {
                var total = 0
                for (t in towers) {
                    val dx = t[0] - cx
                    val dy = t[1] - cy
                    val dist2 = dx * dx + dy * dy
                    if (dist2 <= r2) {
                        val d = Math.sqrt(dist2.toDouble())
                        val contribution = Math.floor(t[2] / (1.0 + d)).toInt()
                        total += contribution
                    }
                }
                if (total > maxQuality ||
                    (total == maxQuality && (cx < bestX || (cx == bestX && cy < bestY)))
                ) {
                    maxQuality = total
                    bestX = cx
                    bestY = cy
                }
            }
        }

        return intArrayOf(bestX, bestY)
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  List<int> bestCoordinate(List<List<int>> towers, int radius) {
    int maxX = 0;
    int maxY = 0;
    for (var t in towers) {
      maxX = max(maxX, t[0]);
      maxY = max(maxY, t[1]);
    }
    int limitX = maxX + radius;
    int limitY = maxY + radius;

    int bestQuality = -1;
    int bestX = 0;
    int bestY = 0;

    for (int x = 0; x <= limitX; ++x) {
      for (int y = 0; y <= limitY; ++y) {
        int total = 0;
        for (var t in towers) {
          int tx = t[0];
          int ty = t[1];
          int q = t[2];
          double dist = sqrt(pow(tx - x, 2) + pow(ty - y, 2));
          if (dist <= radius) {
            total += (q / (1 + dist)).floor();
          }
        }
        if (total > bestQuality ||
            (total == bestQuality && (x < bestX || (x == bestX && y < bestY)))) {
          bestQuality = total;
          bestX = x;
          bestY = y;
        }
      }
    }

    return [bestX, bestY];
  }
}
```

## Golang

```go
func bestCoordinate(towers [][]int, radius int) []int {
    maxX, maxY := 0, 0
    for _, t := range towers {
        if t[0] > maxX {
            maxX = t[0]
        }
        if t[1] > maxY {
            maxY = t[1]
        }
    }
    limitX := maxX + radius
    limitY := maxY + radius

    bestQ := -1
    bestX, bestY := 0, 0
    rFloat := float64(radius)

    for x := 0; x <= limitX; x++ {
        for y := 0; y <= limitY; y++ {
            total := 0
            for _, t := range towers {
                dx := t[0] - x
                dy := t[1] - y
                distSq := dx*dx + dy*dy
                if float64(distSq) > rFloat*rFloat {
                    continue
                }
                d := math.Sqrt(float64(distSq))
                q := int(math.Floor(float64(t[2]) / (1.0 + d)))
                total += q
            }
            if total > bestQ || (total == bestQ && (x < bestX || (x == bestX && y < bestY))) {
                bestQ = total
                bestX, bestY = x, y
            }
        }
    }
    return []int{bestX, bestY}
}
```

## Ruby

```ruby
def best_coordinate(towers, radius)
  max_x = towers.map { |t| t[0] }.max
  max_y = towers.map { |t| t[1] }.max
  limit_x = max_x + radius
  limit_y = max_y + radius

  best_quality = -1
  best_coord = [0, 0]

  (0..limit_x).each do |x|
    (0..limit_y).each do |y|
      total = 0
      towers.each do |tx, ty, q|
        dx = x - tx
        dy = y - ty
        d = Math.sqrt(dx * dx + dy * dy)
        if d <= radius
          total += (q.to_f / (1 + d)).floor
        end
      end

      if total > best_quality ||
         (total == best_quality && (x < best_coord[0] || (x == best_coord[0] && y < best_coord[1])))
        best_quality = total
        best_coord = [x, y]
      end
    end
  end

  best_coord
end
```

## Scala

```scala
object Solution {
    def bestCoordinate(towers: Array[Array[Int]], radius: Int): Array[Int] = {
        var minX = Int.MaxValue
        var maxX = Int.MinValue
        var minY = Int.MaxValue
        var maxY = Int.MinValue
        for (t <- towers) {
            val x = t(0)
            val y = t(1)
            if (x < minX) minX = x
            if (x > maxX) maxX = x
            if (y < minY) minY = y
            if (y > maxY) maxY = y
        }
        val startX = Math.max(0, minX - radius)
        val endX   = maxX + radius
        val startY = Math.max(0, minY - radius)
        val endY   = maxY + radius

        var bestQuality = -1
        var bestX = 0
        var bestY = 0

        for (x <- startX to endX) {
            for (y <- startY to endY) {
                var total = 0
                for (t <- towers) {
                    val dx = t(0) - x
                    val dy = t(1) - y
                    val dist = Math.sqrt(dx * dx + dy * dy)
                    if (dist <= radius + 1e-9) {
                        val q = t(2)
                        total += Math.floor(q / (1.0 + dist)).toInt
                    }
                }
                if (total > bestQuality || (total == bestQuality && (x < bestX || (x == bestX && y < bestY)))) {
                    bestQuality = total
                    bestX = x
                    bestY = y
                }
            }
        }
        Array(bestX, bestY)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn best_coordinate(towers: Vec<Vec<i32>>, radius: i32) -> Vec<i32> {
        let mut max_x = 0;
        let mut max_y = 0;
        for t in &towers {
            if t[0] > max_x { max_x = t[0]; }
            if t[1] > max_y { max_y = t[1]; }
        }
        let limit_x = max_x + radius;
        let limit_y = max_y + radius;
        let r_f = radius as f64;
        let mut best_total = -1i32;
        let mut best_coord = vec![0, 0];
        for x in 0..=limit_x {
            for y in 0..=limit_y {
                let mut total = 0i32;
                for t in &towers {
                    let dx = (t[0] - x) as i64;
                    let dy = (t[1] - y) as i64;
                    let d = ((dx * dx + dy * dy) as f64).sqrt();
                    if d <= r_f + 1e-9 {
                        total += ((t[2] as f64) / (1.0 + d)).floor() as i32;
                    }
                }
                if total > best_total
                    || (total == best_total
                        && (x < best_coord[0]
                            || (x == best_coord[0] && y < best_coord[1])))
                {
                    best_total = total;
                    best_coord[0] = x;
                    best_coord[1] = y;
                }
            }
        }
        best_coord
    }
}
```

## Racket

```racket
(define/contract (best-coordinate towers radius)
  (-> (listof (listof exact-integer?)) exact-integer? (listof exact-integer?))
  (let* ((max-x (apply max (map first towers)))
         (max-y (apply max (map second towers)))
         (x-limit (+ max-x radius))
         (y-limit (+ max-y radius)))
    (define-values (best-quality best-x best-y)
      (for/fold ([best-quality -1] [best-x 0] [best-y 0])
                ([x (in-range 0 (+ x-limit 1))]
                 [y (in-range 0 (+ y-limit 1))])
        (let ((total
               (apply + 
                      (for/list ([t towers])
                        (define xi (first t))
                        (define yi (second t))
                        (define qi (third t))
                        (define d (sqrt (+ (sqr (- xi x)) (sqr (- yi y)))))
                        (if (<= d radius)
                            (inexact->exact (floor (/ qi (+ 1 d))))
                            0)))))
          (cond [(> total best-quality) (values total x y)]
                [(= total best-quality)
                 (if (or (< x best-x) (and (= x best-x) (< y best-y)))
                     (values total x y)
                     (values best-quality best-x best-y))]
                [else (values best-quality best-x best-y)]))))
    (list best-x best-y)))
```

## Erlang

```erlang
-spec best_coordinate(Towers :: [[integer()]], Radius :: integer()) -> [integer()].
best_coordinate(Towers, Radius) ->
    MaxX = lists:max([X + Radius || [X, _, _] <- Towers]),
    MaxY = lists:max([Y + Radius || [_ , Y, _] <- Towers]),
    {BestCoord, _} =
        lists:foldl(
            fun(X, {BestC, BestQ}) ->
                {NewBestC, NewBestQ} =
                    lists:foldl(
                        fun(Y, {BC, BQ}) ->
                            Q = total_quality(X, Y, Towers, Radius),
                            case (Q > BQ) orelse (Q == BQ andalso lex_less([X, Y], BC)) of
                                true -> {[X, Y], Q};
                                false -> {BC, BQ}
                            end
                        end,
                        {BestC, BestQ},
                        lists:seq(0, MaxY)
                    ),
                {NewBestC, NewBestQ}
            end,
            {[0, 0], 0},
            lists:seq(0, MaxX)
        ),
    BestCoord.

total_quality(X, Y, Towers, Radius) ->
    lists:foldl(
        fun([Tx, Ty, Q], Acc) ->
            Dx = X - Tx,
            Dy = Y - Ty,
            D = math:sqrt(Dx * Dx + Dy * Dy),
            if
                D =< Radius ->
                    Acc + trunc(Q / (1.0 + D));
                true ->
                    Acc
            end
        end,
        0,
        Towers).

lex_less([X1, Y1], [X2, Y2]) when X1 < X2 -> true;
lex_less([X1, Y1], [X2, Y2]) when X1 > X2 -> false;
lex_less([_X1, Y1], [_X2, Y2]) -> Y1 < Y2.
```

## Elixir

```elixir
defmodule Solution do
  @spec best_coordinate(towers :: [[integer]], radius :: integer) :: [integer]
  def best_coordinate(towers, radius) do
    max_x = towers |> Enum.map(fn [x, _, _] -> x end) |> Enum.max()
    max_y = towers |> Enum.map(fn [_x, y, _] -> y end) |> Enum.max()
    limit_x = max_x + radius
    limit_y = max_y + radius

    points = for x <- 0..limit_x, y <- 0..limit_y, do: {x, y}

    %{coord: result} =
      Enum.reduce(points, %{sum: -1, coord: [0, 0]}, fn {x, y}, acc ->
        total =
          Enum.reduce(towers, 0, fn [tx, ty, q], s ->
            dx = tx - x
            dy = ty - y
            d = :math.sqrt(dx * dx + dy * dy)

            if d <= radius do
              val = Float.floor(q / (1.0 + d)) |> trunc()
              s + val
            else
              s
            end
          end)

        cond do
          total > acc.sum ->
            %{sum: total, coord: [x, y]}

          total == acc.sum ->
            [bx, by] = acc.coord

            if x < bx or (x == bx and y < by) do
              %{acc | coord: [x, y]}
            else
              acc
            end

          true ->
            acc
        end
      end)

    result
  end
end
```

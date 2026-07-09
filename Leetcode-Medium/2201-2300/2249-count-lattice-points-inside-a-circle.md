# 2249. Count Lattice Points Inside a Circle

## Cpp

```cpp
class Solution {
public:
    int countLatticePoints(vector<vector<int>>& circles) {
        unordered_set<long long> points;
        for (const auto& c : circles) {
            int x = c[0], y = c[1], r = c[2];
            long long rsq = 1LL * r * r;
            for (int dx = -r; dx <= r; ++dx) {
                long long remain = rsq - 1LL * dx * dx;
                int dyMax = (int)std::sqrt((double)remain);
                for (int dy = -dyMax; dy <= dyMax; ++dy) {
                    long long key = ((long long)(x + dx) << 32) | (unsigned int)(y + dy);
                    points.insert(key);
                }
            }
        }
        return (int)points.size();
    }
};
```

## Java

```java
class Solution {
    public int countLatticePoints(int[][] circles) {
        java.util.HashSet<Long> points = new java.util.HashSet<>();
        for (int[] c : circles) {
            int cx = c[0];
            int cy = c[1];
            int r = c[2];
            int rSq = r * r;
            for (int x = cx - r; x <= cx + r; ++x) {
                int dx = x - cx;
                int dyMaxSq = rSq - dx * dx;
                if (dyMaxSq < 0) continue;
                int dyMax = (int) Math.sqrt(dyMaxSq);
                for (int y = cy - dyMax; y <= cy + dyMax; ++y) {
                    long key = ((long) x << 32) | (y & 0xffffffffL);
                    points.add(key);
                }
            }
        }
        return points.size();
    }
}
```

## Python

```python
class Solution(object):
    def countLatticePoints(self, circles):
        """
        :type circles: List[List[int]]
        :rtype: int
        """
        import math
        points = set()
        for x0, y0, r in circles:
            rsq = r * r
            for x in range(x0 - r, x0 + r + 1):
                dx = x - x0
                dy_max_sq = rsq - dx * dx
                if dy_max_sq < 0:
                    continue
                dy_max = int(math.isqrt(dy_max_sq))
                for y in range(y0 - dy_max, y0 + dy_max + 1):
                    points.add((x, y))
        return len(points)
```

## Python3

```python
from typing import List

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        for cx, cy, r in circles:
            r_sq = r * r
            x_start = cx - r
            x_end = cx + r
            y_start = cy - r
            y_end = cy + r
            for x in range(x_start, x_end + 1):
                dx_sq = (x - cx) * (x - cx)
                if dx_sq > r_sq:
                    continue
                for y in range(y_start, y_end + 1):
                    if dx_sq + (y - cy) * (y - cy) <= r_sq:
                        points.add((x, y))
        return len(points)
```

## C

```c
#include <math.h>
#include <stdbool.h>

int countLatticePoints(int** circles, int circlesSize, int* circlesColSize) {
    const int MAX = 200;               // maximum possible coordinate
    static bool visited[201][201];     // zero‑initialized
    int total = 0;

    for (int i = 0; i < circlesSize; ++i) {
        int x = circles[i][0];
        int y = circles[i][1];
        int r = circles[i][2];
        int rsq = r * r;

        for (int dx = -r; dx <= r; ++dx) {
            int xx = x + dx;
            if (xx < 0 || xx > MAX) continue;

            int dyLimitSq = rsq - dx * dx;
            if (dyLimitSq < 0) continue;
            int maxDy = (int)sqrt((double)dyLimitSq);

            for (int dy = -maxDy; dy <= maxDy; ++dy) {
                int yy = y + dy;
                if (yy < 0 || yy > MAX) continue;

                if (!visited[xx][yy]) {
                    visited[xx][yy] = true;
                    ++total;
                }
            }
        }
    }

    return total;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountLatticePoints(int[][] circles)
    {
        var points = new HashSet<long>();
        foreach (var c in circles)
        {
            int cx = c[0];
            int cy = c[1];
            int r = c[2];
            long rsq = (long)r * r;
            for (int x = cx - r; x <= cx + r; x++)
            {
                long dx = x - cx;
                long dxsq = dx * dx;
                if (dxsq > rsq) continue;
                for (int y = cy - r; y <= cy + r; y++)
                {
                    long dy = y - cy;
                    if (dxsq + dy * dy <= rsq)
                    {
                        long key = ((long)x << 32) | ((uint)y);
                        points.Add(key);
                    }
                }
            }
        }
        return points.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} circles
 * @return {number}
 */
var countLatticePoints = function(circles) {
    const visited = new Set();
    for (const [cx, cy, r] of circles) {
        const rsq = r * r;
        for (let x = cx - r; x <= cx + r; ++x) {
            const dx = x - cx;
            const remain = rsq - dx * dx;
            if (remain < 0) continue;
            const dyMax = Math.floor(Math.sqrt(remain));
            for (let y = cy - dyMax; y <= cy + dyMax; ++y) {
                visited.add(`${x},${y}`);
            }
        }
    }
    return visited.size;
};
```

## Typescript

```typescript
function countLatticePoints(circles: number[][]): number {
    const points = new Set<string>();
    for (const [cx, cy, r] of circles) {
        const r2 = r * r;
        for (let x = cx - r; x <= cx + r; ++x) {
            const dx = x - cx;
            const dx2 = dx * dx;
            const remain = r2 - dx2;
            if (remain < 0) continue;
            const maxDy = Math.floor(Math.sqrt(remain));
            for (let y = cy - maxDy; y <= cy + maxDy; ++y) {
                points.add(`${x},${y}`);
            }
        }
    }
    return points.size;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $circles
     * @return Integer
     */
    function countLatticePoints($circles) {
        $visited = [];
        foreach ($circles as $c) {
            [$xi, $yi, $ri] = $c;
            $r2 = $ri * $ri;
            for ($x = $xi - $ri; $x <= $xi + $ri; $x++) {
                $dx = $x - $xi;
                $dx2 = $dx * $dx;
                for ($y = $yi - $ri; $y <= $yi + $ri; $y++) {
                    $dy = $y - $yi;
                    if ($dx2 + $dy * $dy <= $r2) {
                        $visited[$x . ',' . $y] = true;
                    }
                }
            }
        }
        return count($visited);
    }
}
```

## Swift

```swift
class Solution {
    func countLatticePoints(_ circles: [[Int]]) -> Int {
        var visited = Set<String>()
        for circle in circles {
            let xi = circle[0]
            let yi = circle[1]
            let ri = circle[2]
            let r2 = ri * ri
            for x in (xi - ri)...(xi + ri) {
                for y in (yi - ri)...(yi + ri) {
                    let dx = x - xi
                    let dy = y - yi
                    if dx * dx + dy * dy <= r2 {
                        visited.insert("\(x)#\(y)")
                    }
                }
            }
        }
        return visited.count
    }
}
```

## Kotlin

```kotlin
import kotlin.math.sqrt

class Solution {
    fun countLatticePoints(circles: Array<IntArray>): Int {
        val visited = HashSet<Long>()
        for (c in circles) {
            val cx = c[0]
            val cy = c[1]
            val r = c[2]
            val rSq = r * r
            for (dx in -r..r) {
                val x = cx + dx
                val remaining = rSq - dx * dx
                if (remaining < 0) continue
                val dyLimit = sqrt(remaining.toDouble()).toInt()
                for (dy in -dyLimit..dyLimit) {
                    val y = cy + dy
                    val key = (x.toLong() shl 32) or (y.toLong() and 0xffffffffL)
                    visited.add(key)
                }
            }
        }
        return visited.size
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int countLatticePoints(List<List<int>> circles) {
    final Set<String> points = <String>{};
    for (var circle in circles) {
      int xi = circle[0];
      int yi = circle[1];
      int ri = circle[2];
      int rSq = ri * ri;
      for (int x = xi - ri; x <= xi + ri; ++x) {
        int dx = x - xi;
        int dyMaxSq = rSq - dx * dx;
        if (dyMaxSq < 0) continue;
        int dyMax = sqrt(dyMaxSq).floor();
        for (int y = yi - dyMax; y <= yi + dyMax; ++y) {
          points.add('$x,$y');
        }
      }
    }
    return points.length;
  }
}
```

## Golang

```go
func countLatticePoints(circles [][]int) int {
    points := make(map[[2]int]struct{})
    for _, c := range circles {
        x0, y0, r := c[0], c[1], c[2]
        rsq := r * r
        for x := x0 - r; x <= x0+r; x++ {
            dx := x - x0
            dx2 := dx * dx
            for y := y0 - r; y <= y0+r; y++ {
                dy := y - y0
                if dx2+dy*dy <= rsq {
                    points[[2]int{x, y}] = struct{}{}
                }
            }
        }
    }
    return len(points)
}
```

## Ruby

```ruby
require 'set'

def count_lattice_points(circles)
  points = Set.new
  circles.each do |x, y, r|
    (x - r).upto(x + r) do |cx|
      dx = cx - x
      remaining = r * r - dx * dx
      next if remaining < 0
      max_dy = Math.sqrt(remaining).floor
      (y - max_dy).upto(y + max_dy) do |cy|
        points.add([cx, cy])
      end
    end
  end
  points.size
end
```

## Scala

```scala
object Solution {
    def countLatticePoints(circles: Array[Array[Int]]): Int = {
        val points = scala.collection.mutable.HashSet[(Int, Int)]()
        for (c <- circles) {
            val x0 = c(0)
            val y0 = c(1)
            val r  = c(2)
            var x = x0 - r
            while (x <= x0 + r) {
                val dx = x - x0
                val remain = r * r - dx * dx
                if (remain >= 0) {
                    val dyMax = math.sqrt(remain).toInt
                    var y = y0 - dyMax
                    while (y <= y0 + dyMax) {
                        points.add((x, y))
                        y += 1
                    }
                }
                x += 1
            }
        }
        points.size
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_lattice_points(circles: Vec<Vec<i32>>) -> i32 {
        use std::collections::HashSet;
        let mut points = HashSet::new();
        for c in circles.iter() {
            let cx = c[0];
            let cy = c[1];
            let r = c[2];
            let rsq = (r as i64) * (r as i64);
            for x in (cx - r)..=(cx + r) {
                for y in (cy - r)..=(cy + r) {
                    let dx = (x - cx) as i64;
                    let dy = (y - cy) as i64;
                    if dx * dx + dy * dy <= rsq {
                        points.insert((x, y));
                    }
                }
            }
        }
        points.len() as i32
    }
}
```

## Racket

```racket
#lang racket

(define/contract (count-lattice-points circles)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([min-x (apply min (map (lambda (c) (- (first c) (third c))) circles))]
         [max-x (apply max (map (lambda (c) (+ (first c) (third c))) circles))]
         [min-y (apply min (map (lambda (c) (- (second c) (third c))) circles))]
         [max-y (apply max (map (lambda (c) (+ (second c) (third c))) circles))])
    (for*/fold ([cnt 0]) ([x (in-range min-x (add1 max-x))]
                         [y (in-range min-y (add1 max-y))])
      (if (for/or ([c circles])
            (let* ([cx (first c)]
                   [cy (second c)]
                   [r  (third c)])
              (<= (+ (* (- x cx) (- x cx))
                     (* (- y cy) (- y cy)))
                  (* r r))))
          (add1 cnt)
          cnt))))
```

## Erlang

```erlang
-module(solution).
-export([count_lattice_points/1]).

-spec count_lattice_points(Circles :: [[integer()]]) -> integer().
count_lattice_points(Circles) ->
    PointsMap = lists:foldl(fun process_circle/2, #{}, Circles),
    maps:size(PointsMap).

process_circle([Xi, Yi, Ri], Acc) ->
    XStart = Xi - Ri,
    XEnd   = Xi + Ri,
    YStart = Yi - Ri,
    YEnd   = Yi + Ri,
    Rsq    = Ri * Ri,
    lists:foldl(
        fun(X, Acc1) ->
            lists:foldl(
                fun(Y, Acc2) ->
                    Dx = X - Xi,
                    Dy = Y - Yi,
                    if
                        Dx*Dx + Dy*Dy =< Rsq ->
                            maps:put({X,Y}, true, Acc2);
                        true ->
                            Acc2
                    end
                end,
                Acc1,
                lists:seq(YStart, YEnd)
            )
        end,
        Acc,
        lists:seq(XStart, XEnd)
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_lattice_points(circles :: [[integer]]) :: integer
  def count_lattice_points(circles) do
    circles
    |> Enum.reduce(MapSet.new(), fn [xi, yi, ri], set ->
      r_sq = ri * ri

      Enum.reduce((xi - ri)..(xi + ri), set, fn x, acc ->
        dx = x - xi
        dy_max =
          r_sq
          |> Kernel.-(dx * dx)
          |> max(0)
          |> :math.sqrt()
          |> trunc()

        Enum.reduce((yi - dy_max)..(yi + dy_max), acc, fn y, a2 ->
          MapSet.put(a2, {x, y})
        end)
      end)
    end)
    |> MapSet.size()
  end
end
```

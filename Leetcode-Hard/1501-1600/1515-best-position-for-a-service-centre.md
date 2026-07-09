# 1515. Best Position for a Service Centre

## Cpp

```cpp
class Solution {
public:
    double getMinDistSum(vector<vector<int>>& positions) {
        int n = positions.size();
        vector<double> xs(n), ys(n);
        for (int i = 0; i < n; ++i) {
            xs[i] = positions[i][0];
            ys[i] = positions[i][1];
        }
        if (n == 1) return 0.0;
        double x = 0, y = 0;
        for (int i = 0; i < n; ++i) {
            x += xs[i];
            y += ys[i];
        }
        x /= n;
        y /= n;
        const double epsMove = 1e-7;
        const double epsDist = 1e-12;
        for (int iter = 0; iter < 10000; ++iter) {
            double numX = 0, numY = 0, den = 0;
            bool atPoint = false;
            int pointIdx = -1;
            for (int i = 0; i < n; ++i) {
                double dx = x - xs[i];
                double dy = y - ys[i];
                double d = sqrt(dx * dx + dy * dy);
                if (d < epsDist) {
                    atPoint = true;
                    pointIdx = i;
                    break;
                }
                double w = 1.0 / d;
                numX += xs[i] * w;
                numY += ys[i] * w;
                den += w;
            }
            if (atPoint) {
                x = xs[pointIdx];
                y = ys[pointIdx];
                break;
            }
            double newX = numX / den;
            double newY = numY / den;
            if (hypot(newX - x, newY - y) < epsMove) {
                x = newX;
                y = newY;
                break;
            }
            x = newX;
            y = newY;
        }
        double total = 0.0;
        for (int i = 0; i < n; ++i) {
            double dx = x - xs[i];
            double dy = y - ys[i];
            total += sqrt(dx * dx + dy * dy);
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public double getMinDistSum(int[][] positions) {
        int n = positions.length;
        if (n == 0) return 0.0;
        // Initial guess: centroid
        double x = 0, y = 0;
        for (int[] p : positions) {
            x += p[0];
            y += p[1];
        }
        x /= n;
        y /= n;

        final double EPS = 1e-7;
        for (int iter = 0; iter < 10000; ++iter) {
            double numX = 0, numY = 0, denom = 0;
            boolean coincident = false;
            for (int[] p : positions) {
                double dx = x - p[0];
                double dy = y - p[1];
                double dist = Math.hypot(dx, dy);
                if (dist < 1e-12) { // current point is exactly a data point
                    coincident = true;
                    break;
                }
                double w = 1.0 / dist;
                numX += p[0] * w;
                numY += p[1] * w;
                denom += w;
            }
            if (coincident) {
                // geometric median is at this data point
                break;
            }
            double newX = numX / denom;
            double newY = numY / denom;
            if (Math.hypot(newX - x, newY - y) < EPS) {
                x = newX;
                y = newY;
                break;
            }
            x = newX;
            y = newY;
        }

        double sum = 0.0;
        for (int[] p : positions) {
            sum += Math.hypot(x - p[0], y - p[1]);
        }
        return sum;
    }
}
```

## Python

```python
import math

class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        n = len(positions)
        if n == 0:
            return 0.0
        # initial guess: centroid
        x = sum(p[0] for p in positions) / n
        y = sum(p[1] for p in positions) / n

        eps = 1e-7
        max_iter = 10000
        for _ in range(max_iter):
            num_x = 0.0
            num_y = 0.0
            denom = 0.0
            coincident = False
            for px, py in positions:
                dx = x - px
                dy = y - py
                dist = math.hypot(dx, dy)
                if dist < eps:  # current point is at a data point
                    x, y = px, py
                    coincident = True
                    break
                w = 1.0 / dist
                num_x += px * w
                num_y += py * w
                denom += w
            if coincident:
                break
            new_x = num_x / denom
            new_y = num_y / denom
            if math.hypot(new_x - x, new_y - y) < eps:
                x, y = new_x, new_y
                break
            x, y = new_x, new_y

        total = sum(math.hypot(x - p[0], y - p[1]) for p in positions)
        return total
```

## Python3

```python
from typing import List
import math

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        pts = [(float(x), float(y)) for x, y in positions]
        n = len(pts)
        # start from centroid
        x = sum(p[0] for p in pts) / n
        y = sum(p[1] for p in pts) / n

        eps = 1e-7
        for _ in range(10000):
            num_x = 0.0
            num_y = 0.0
            denom = 0.0
            coincident = False
            for px, py in pts:
                dx = x - px
                dy = y - py
                dist = math.hypot(dx, dy)
                if dist < 1e-12:  # current point is exactly a data point
                    x, y = px, py
                    coincident = True
                    break
                w = 1.0 / dist
                num_x += px * w
                num_y += py * w
                denom += w
            if coincident:
                break
            new_x = num_x / denom
            new_y = num_y / denom
            if (new_x - x) ** 2 + (new_y - y) ** 2 < eps * eps:
                x, y = new_x, new_y
                break
            x, y = new_x, new_y

        total = sum(math.hypot(x - px, y - py) for px, py in pts)
        return total
```

## C

```c
#include <math.h>

double getMinDistSum(int** positions, int positionsSize, int* positionsColSize) {
    int n = positionsSize;
    if (n == 0) return 0.0;

    double x = 0.0, y = 0.0;
    for (int i = 0; i < n; ++i) {
        x += positions[i][0];
        y += positions[i][1];
    }
    x /= n;
    y /= n;

    const double eps = 1e-7;
    for (int iter = 0; iter < 10000; ++iter) {
        double numX = 0.0, numY = 0.0, denom = 0.0;
        int coincidentIdx = -1;
        for (int i = 0; i < n; ++i) {
            double dx = x - positions[i][0];
            double dy = y - positions[i][1];
            double dist = sqrt(dx * dx + dy * dy);
            if (dist < 1e-12) {
                coincidentIdx = i;
                break;
            }
            double w = 1.0 / dist;
            numX += positions[i][0] * w;
            numY += positions[i][1] * w;
            denom += w;
        }
        if (coincidentIdx != -1) {
            x = positions[coincidentIdx][0];
            y = positions[coincidentIdx][1];
            break;
        }
        double newX = numX / denom;
        double newY = numY / denom;
        if (hypot(newX - x, newY - y) < eps) {
            x = newX;
            y = newY;
            break;
        }
        x = newX;
        y = newY;
    }

    double sum = 0.0;
    for (int i = 0; i < n; ++i) {
        double dx = x - positions[i][0];
        double dy = y - positions[i][1];
        sum += sqrt(dx * dx + dy * dy);
    }
    return sum;
}
```

## Csharp

```csharp
public class Solution
{
    public double GetMinDistSum(int[][] positions)
    {
        int n = positions.Length;
        if (n == 0) return 0.0;

        // Initial guess: centroid
        double x = 0, y = 0;
        foreach (var p in positions)
        {
            x += p[0];
            y += p[1];
        }
        x /= n;
        y /= n;

        const double eps = 1e-7;
        for (int iter = 0; iter < 10000; ++iter)
        {
            double numX = 0, numY = 0, denom = 0;
            bool coincident = false;
            foreach (var p in positions)
            {
                double dx = x - p[0];
                double dy = y - p[1];
                double dist = Math.Sqrt(dx * dx + dy * dy);
                if (dist < eps) // current point is at a data point
                {
                    coincident = true;
                    break;
                }
                double w = 1.0 / dist;
                numX += p[0] * w;
                numY += p[1] * w;
                denom += w;
            }

            if (coincident) break; // current point is optimal

            double newX = numX / denom;
            double newY = numY / denom;

            if (Math.Sqrt((newX - x) * (newX - x) + (newY - y) * (newY - y)) < eps)
                { x = newX; y = newY; break; }

            x = newX;
            y = newY;
        }

        double sum = 0.0;
        foreach (var p in positions)
        {
            double dx = x - p[0];
            double dy = y - p[1];
            sum += Math.Sqrt(dx * dx + dy * dy);
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} positions
 * @return {number}
 */
var getMinDistSum = function(positions) {
    const n = positions.length;
    let x = 0, y = 0;
    for (const p of positions) {
        x += p[0];
        y += p[1];
    }
    x /= n;
    y /= n;

    const eps = 1e-7;
    const maxIter = 10000;

    for (let iter = 0; iter < maxIter; ++iter) {
        let numX = 0, numY = 0, denom = 0;
        let coincident = false;

        for (const p of positions) {
            const dx = x - p[0];
            const dy = y - p[1];
            const d = Math.hypot(dx, dy);
            if (d === 0) { // current estimate is exactly at a data point
                coincident = true;
                break;
            }
            const w = 1 / d;
            numX += p[0] * w;
            numY += p[1] * w;
            denom += w;
        }

        if (coincident) {
            let sum = 0;
            for (const p of positions) {
                sum += Math.hypot(x - p[0], y - p[1]);
            }
            return sum;
        }

        const newX = numX / denom;
        const newY = numY / denom;

        if (Math.abs(newX - x) < eps && Math.abs(newY - y) < eps) {
            x = newX;
            y = newY;
            break;
        }
        x = newX;
        y = newY;
    }

    let total = 0;
    for (const p of positions) {
        total += Math.hypot(x - p[0], y - p[1]);
    }
    return total;
};
```

## Typescript

```typescript
function getMinDistSum(positions: number[][]): number {
    const n = positions.length;
    if (n === 0) return 0;

    // start from centroid
    let x = 0, y = 0;
    for (const p of positions) {
        x += p[0];
        y += p[1];
    }
    x /= n;
    y /= n;

    const eps = 1e-7;
    const maxIter = 10000;

    for (let iter = 0; iter < maxIter; ++iter) {
        let numX = 0, numY = 0, denom = 0;
        let coincident = false;

        for (const p of positions) {
            const dx = x - p[0];
            const dy = y - p[1];
            const dist = Math.hypot(dx, dy);
            if (dist < 1e-12) { // current estimate coincides with a data point
                coincident = true;
                break;
            }
            const w = 1 / dist;
            numX += p[0] * w;
            numY += p[1] * w;
            denom += w;
        }

        if (coincident) {
            // the point itself is optimal; compute total distance directly
            let total = 0;
            for (const p of positions) {
                total += Math.hypot(p[0] - x, p[1] - y);
            }
            return total;
        }

        const newX = numX / denom;
        const newY = numY / denom;

        if (Math.hypot(newX - x, newY - y) < eps) {
            x = newX;
            y = newY;
            break;
        }
        x = newX;
        y = newY;
    }

    let total = 0;
    for (const p of positions) {
        total += Math.hypot(p[0] - x, p[1] - y);
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $positions
     * @return Float
     */
    function getMinDistSum($positions) {
        $n = count($positions);
        if ($n <= 1) {
            return 0.0;
        }

        // initial guess: centroid
        $x = 0.0;
        $y = 0.0;
        foreach ($positions as $p) {
            $x += $p[0];
            $y += $p[1];
        }
        $x /= $n;
        $y /= $n;

        $eps = 1e-7;
        for ($iter = 0; $iter < 10000; ++$iter) {
            $numX = 0.0;
            $numY = 0.0;
            $den  = 0.0;
            foreach ($positions as $p) {
                $dx = $x - $p[0];
                $dy = $y - $p[1];
                $dist = sqrt($dx * $dx + $dy * $dy);
                if ($dist < 1e-12) { // coincides with a point
                    $total = 0.0;
                    foreach ($positions as $q) {
                        $dx2 = $p[0] - $q[0];
                        $dy2 = $p[1] - $q[1];
                        $total += sqrt($dx2 * $dx2 + $dy2 * $dy2);
                    }
                    return $total;
                }
                $w = 1.0 / $dist;
                $numX += $p[0] * $w;
                $numY += $p[1] * $w;
                $den  += $w;
            }

            $newX = $numX / $den;
            $newY = $numY / $den;

            if (sqrt(($newX - $x) * ($newX - $x) + ($newY - $y) * ($newY - $y)) < $eps) {
                $x = $newX;
                $y = $newY;
                break;
            }
            $x = $newX;
            $y = $newY;
        }

        // compute total distance
        $total = 0.0;
        foreach ($positions as $p) {
            $dx = $x - $p[0];
            $dy = $y - $p[1];
            $total += sqrt($dx * $dx + $dy * $dy);
        }
        return $total;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func getMinDistSum(_ positions: [[Int]]) -> Double {
        let n = positions.count
        var x = positions.map { Double($0[0]) }.reduce(0, +) / Double(n)
        var y = positions.map { Double($0[1]) }.reduce(0, +) / Double(n)
        
        let eps = 1e-7
        for _ in 0..<10000 {
            var numX = 0.0
            var numY = 0.0
            var denom = 0.0
            var atPoint = false
            
            for p in positions {
                let px = Double(p[0])
                let py = Double(p[1])
                let dx = x - px
                let dy = y - py
                let dist = sqrt(dx * dx + dy * dy)
                
                if dist < eps {
                    atPoint = true
                    break
                }
                
                let w = 1.0 / dist
                numX += px * w
                numY += py * w
                denom += w
            }
            
            if atPoint { break }
            
            let newX = numX / denom
            let newY = numY / denom
            if sqrt((newX - x) * (newX - x) + (newY - y) * (newY - y)) < eps {
                x = newX
                y = newY
                break
            }
            x = newX
            y = newY
        }
        
        var total = 0.0
        for p in positions {
            let dx = x - Double(p[0])
            let dy = y - Double(p[1])
            total += sqrt(dx * dx + dy * dy)
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getMinDistSum(positions: Array<IntArray>): Double {
        val n = positions.size
        if (n == 1) return 0.0

        var x = 0.0
        var y = 0.0
        for (p in positions) {
            x += p[0]
            y += p[1]
        }
        x /= n
        y /= n

        val eps = 1e-7
        repeat(10000) {
            var numX = 0.0
            var numY = 0.0
            var denom = 0.0
            var atPoint = false

            for (p in positions) {
                val dx = x - p[0]
                val dy = y - p[1]
                val dist = Math.hypot(dx, dy)
                if (dist < 1e-12) {
                    atPoint = true
                    break
                }
                val w = 1.0 / dist
                numX += p[0] * w
                numY += p[1] * w
                denom += w
            }

            if (atPoint) {
                var sum = 0.0
                for (p in positions) {
                    sum += Math.hypot(x - p[0], y - p[1])
                }
                return sum
            }

            val newX = numX / denom
            val newY = numY / denom

            if (Math.hypot(newX - x, newY - y) < eps) {
                x = newX
                y = newY
                return run {
                    var total = 0.0
                    for (p in positions) {
                        total += Math.hypot(x - p[0], y - p[1])
                    }
                    total
                }
            }

            x = newX
            y = newY
        }

        var result = 0.0
        for (p in positions) {
            result += Math.hypot(x - p[0], y - p[1])
        }
        return result
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  double getMinDistSum(List<List<int>> positions) {
    int n = positions.length;
    List<double> xs = [];
    List<double> ys = [];
    for (var p in positions) {
      xs.add(p[0].toDouble());
      ys.add(p[1].toDouble());
    }

    double x = xs.reduce((a, b) => a + b) / n;
    double y = ys.reduce((a, b) => a + b) / n;

    const double eps = 1e-7;
    for (int iter = 0; iter < 10000; ++iter) {
      double numX = 0.0, numY = 0.0, denom = 0.0;
      bool coincident = false;

      for (int i = 0; i < n; i++) {
        double dx = x - xs[i];
        double dy = y - ys[i];
        double dist = sqrt(dx * dx + dy * dy);
        if (dist < eps) {
          coincident = true;
          break;
        }
        double w = 1.0 / dist;
        numX += xs[i] * w;
        numY += ys[i] * w;
        denom += w;
      }

      if (coincident) {
        double total = 0.0;
        for (int i = 0; i < n; i++) {
          double dx = x - xs[i];
          double dy = y - ys[i];
          total += sqrt(dx * dx + dy * dy);
        }
        return total;
      }

      double newX = numX / denom;
      double newY = numY / denom;

      if ((newX - x).abs() < eps && (newY - y).abs() < eps) {
        x = newX;
        y = newY;
        break;
      }
      x = newX;
      y = newY;
    }

    double total = 0.0;
    for (int i = 0; i < n; i++) {
      double dx = x - xs[i];
      double dy = y - ys[i];
      total += sqrt(dx * dx + dy * dy);
    }
    return total;
  }
}
```

## Golang

```go
import "math"

func getMinDistSum(positions [][]int) float64 {
    n := len(positions)
    if n == 0 {
        return 0
    }
    var x, y float64
    for _, p := range positions {
        x += float64(p[0])
        y += float64(p[1])
    }
    x /= float64(n)
    y /= float64(n)

    const eps = 1e-7
    for iter := 0; iter < 10000; iter++ {
        var numX, numY, denom float64
        coincident := false
        var candSum float64

        for _, p := range positions {
            dx := x - float64(p[0])
            dy := y - float64(p[1])
            d := math.Hypot(dx, dy)
            if d < 1e-12 {
                coincident = true
                for _, q := range positions {
                    candSum += math.Hypot(float64(q[0])-float64(p[0]), float64(q[1])-float64(p[1]))
                }
                break
            }
            w := 1.0 / d
            numX += float64(p[0]) * w
            numY += float64(p[1]) * w
            denom += w
        }

        if coincident {
            return candSum
        }

        newX := numX / denom
        newY := numY / denom
        if math.Hypot(newX-x, newY-y) < eps {
            x = newX
            y = newY
            break
        }
        x = newX
        y = newY
    }

    var total float64
    for _, p := range positions {
        total += math.Hypot(x-float64(p[0]), y-float64(p[1]))
    }
    return total
}
```

## Ruby

```ruby
def get_min_dist_sum(positions)
  n = positions.size
  return 0.0 if n == 1

  x = positions.map { |p| p[0] }.sum.to_f / n
  y = positions.map { |p| p[1] }.sum.to_f / n

  eps = 1e-7
  max_iter = 10000

  max_iter.times do
    num_x = 0.0
    num_y = 0.0
    denom = 0.0
    coincident = false

    positions.each do |px, py|
      dx = x - px
      dy = y - py
      dist = Math.sqrt(dx * dx + dy * dy)
      if dist < 1e-12
        # current estimate coincides with a data point
        x = px.to_f
        y = py.to_f
        coincident = true
        break
      end
      w = 1.0 / dist
      num_x += px * w
      num_y += py * w
      denom += w
    end

    break if coincident

    new_x = num_x / denom
    new_y = num_y / denom
    move = Math.sqrt((new_x - x) ** 2 + (new_y - y) ** 2)
    x, y = new_x, new_y
    break if move < eps
  end

  sum = 0.0
  positions.each do |px, py|
    dx = x - px
    dy = y - py
    sum += Math.sqrt(dx * dx + dy * dy)
  end
  sum
end
```

## Scala

```scala
object Solution {
  def getMinDistSum(positions: Array[Array[Int]]): Double = {
    val n = positions.length
    if (n == 0) return 0.0

    var x = positions.map(_(0)).sum.toDouble / n
    var y = positions.map(_(1)).sum.toDouble / n

    val eps = 1e-7
    var iter = 0
    while (iter < 10000) {
      var numX = 0.0
      var numY = 0.0
      var denom = 0.0
      var coincident = false

      for (p <- positions) {
        val dx = x - p(0)
        val dy = y - p(1)
        val d = math.hypot(dx, dy)
        if (d < eps) {
          coincident = true
        } else {
          val w = 1.0 / d
          numX += p(0) * w
          numY += p(1) * w
          denom += w
        }
      }

      if (coincident) {
        // Current point is exactly at a data point; treat as converged.
        iter = 10000
      } else {
        val newX = numX / denom
        val newY = numY / denom
        if (math.hypot(newX - x, newY - y) < eps) {
          x = newX
          y = newY
          iter = 10000
        } else {
          x = newX
          y = newY
        }
      }

      iter += 1
    }

    var sum = 0.0
    for (p <- positions) {
      sum += math.hypot(x - p(0), y - p(1))
    }
    sum
  }
}
```

## Rust

```rust
impl Solution {
    pub fn get_min_dist_sum(positions: Vec<Vec<i32>>) -> f64 {
        let n = positions.len();
        if n == 0 {
            return 0.0;
        }
        // Start from the centroid
        let mut x = positions.iter().map(|p| p[0] as f64).sum::<f64>() / n as f64;
        let mut y = positions.iter().map(|p| p[1] as f64).sum::<f64>() / n as f64;

        const EPS: f64 = 1e-7;
        for _ in 0..10000 {
            let mut num_x = 0.0;
            let mut num_y = 0.0;
            let mut denom = 0.0;
            let mut coincident_point = None;

            for p in &positions {
                let px = p[0] as f64;
                let py = p[1] as f64;
                let dx = x - px;
                let dy = y - py;
                let dist = (dx * dx + dy * dy).sqrt();
                if dist < EPS {
                    coincident_point = Some((px, py));
                    break;
                }
                let w = 1.0 / dist;
                num_x += px * w;
                num_y += py * w;
                denom += w;
            }

            if let Some((cx, cy)) = coincident_point {
                x = cx;
                y = cy;
                break;
            }

            let new_x = num_x / denom;
            let new_y = num_y / denom;

            if (new_x - x).abs() < EPS && (new_y - y).abs() < EPS {
                x = new_x;
                y = new_y;
                break;
            }
            x = new_x;
            y = new_y;
        }

        positions
            .iter()
            .map(|p| {
                let dx = x - p[0] as f64;
                let dy = y - p[1] as f64;
                (dx * dx + dy * dy).sqrt()
            })
            .sum()
    }
}
```

## Racket

```racket
(define/contract (get-min-dist-sum positions)
  (-> (listof (listof exact-integer?)) flonet?)
  (let* ((pts
          (map (lambda (p)
                 (list (exact->inexact (first p))
                       (exact->inexact (second p))))
               positions))
         (n (length pts)))
    (if (= n 0)
        0.0
        (if (= n 1)
            0.0
            (let* ((init-x (/ (apply + (map first pts)) n))
                   (init-y (/ (apply + (map second pts)) n))
                   (eps 1e-7)
                   (max-iters 10000))
              (define (total-distance x y)
                (let loop ((lst pts) (sum 0.0))
                  (if (null? lst)
                      sum
                      (let* ((px (first (car lst)))
                             (py (second (car lst)))
                             (dx (- x px))
                             (dy (- y py))
                             (dist (sqrt (+ (* dx dx) (* dy dy)))))
                        (loop (cdr lst) (+ sum dist))))))
              (let loop ((x init-x) (y init-y) (iter 0))
                ;; compute weighted sums
                (define sum-wx 0.0)
                (define sum-wy 0.0)
                (define sum-w 0.0)
                (define zero-point #f)
                (for-each
                 (lambda (pt)
                   (let* ((px (first pt))
                          (py (second pt))
                          (dx (- x px))
                          (dy (- y py))
                          (dist (sqrt (+ (* dx dx) (* dy dy)))))
                     (if (= dist 0.0)
                         (set! zero-point pt)
                         (let ((w (/ 1.0 dist)))
                           (set! sum-wx (+ sum-wx (* w px)))
                           (set! sum-wy (+ sum-wy (* w py)))
                           (set! sum-w (+ sum-w w))))))
                 pts)
                (if zero-point
                    ;; current estimate coincides with a data point; it's optimal
                    (total-distance (first zero-point) (second zero-point))
                    (let ((newx (/ sum-wx sum-w))
                          (newy (/ sum-wy sum-w)))
                      (if (or (< (sqrt (+ (sqr (- newx x)) (sqr (- newy y)))) eps)
                              (>= iter max-iters))
                          (total-distance newx newy)
                          (loop newx newy (+ iter 1))))))))))))
```

## Erlang

```erlang
-module(solution).
-export([get_min_dist_sum/1]).

-spec get_min_dist_sum(Positions :: [[integer()]]) -> float().
get_min_dist_sum(Positions) ->
    Points = [{float(X), float(Y)} || [X, Y] <- Positions],
    {X0, Y0} = avg_point(Points),
    {Xc, Yc} = weiszfeld(Points, X0, Y0, 1.0e-7, 10000),
    total_distance(Points, Xc, Yc).

avg_point(Points) ->
    N = length(Points),
    {SumX, SumY} =
        lists:foldl(
            fun({X, Y}, {AccX, AccY}) -> {AccX + X, AccY + Y} end,
            {0.0, 0.0},
            Points),
    {SumX / N, SumY / N}.

weiszfeld(Points, X, Y, Tol, MaxIter) ->
    weiszfeld_iter(Points, X, Y, Tol, MaxIter, 0).

weiszfeld_iter(_Points, X, Y, _Tol, _MaxIter, _Iter) ->
    {X, Y};
weiszfeld_iter(Points, X, Y, Tol, MaxIter, Iter) when Iter >= MaxIter ->
    {X, Y};
weiszfeld_iter(Points, X, Y, Tol, MaxIter, Iter) ->
    ZeroDist =
        lists:any(
            fun({Xi, Yi}) ->
                Dx = X - Xi,
                Dy = Y - Yi,
                math:sqrt(Dx * Dx + Dy * Dy) < 1.0e-12
            end,
            Points),
    if ZeroDist ->
            {X, Y};
       true ->
            {NumX, NumY, Den} =
                lists:foldl(
                    fun({Xi, Yi}, {AccX, AccY, AccDen}) ->
                        Dx = X - Xi,
                        Dy = Y - Yi,
                        Dist = math:sqrt(Dx * Dx + Dy * Dy),
                        W = 1.0 / Dist,
                        {AccX + Xi * W, AccY + Yi * W, AccDen + W}
                    end,
                    {0.0, 0.0, 0.0},
                    Points),
            NewX = NumX / Den,
            NewY = NumY / Den,
            Shift = math:sqrt((NewX - X) * (NewX - X) + (NewY - Y) * (NewY - Y)),
            if Shift < Tol ->
                    {NewX, NewY};
               true ->
                    weiszfeld_iter(Points, NewX, NewY, Tol, MaxIter, Iter + 1)
            end
    end.

total_distance(Points, X, Y) ->
    lists:foldl(
        fun({Xi, Yi}, Acc) ->
            Dx = X - Xi,
            Dy = Y - Yi,
            Acc + math:sqrt(Dx * Dx + Dy * Dy)
        end,
        0.0,
        Points).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_min_dist_sum(positions :: [[integer]]) :: float
  def get_min_dist_sum(positions) do
    points =
      Enum.map(positions, fn [x, y] ->
        {x * 1.0, y * 1.0}
      end)

    n = length(points)

    {sx, sy} =
      Enum.reduce(points, {0.0, 0.0}, fn {x, y}, {ax, ay} ->
        {ax + x, ay + y}
      end)

    # start from centroid
    init_x = sx / n
    init_y = sy / n

    epsilon = 1.0e-7
    max_iter = 10_000

    {final_x, final_y} =
      Enum.reduce_while(1..max_iter, {init_x, init_y}, fn _, {cx, cy} ->
        {num_x, num_y, denom, zero_point?} =
          Enum.reduce(points, {0.0, 0.0, 0.0, false}, fn {px, py},
                                                       {nx, ny, dz, zp} ->
            dx = cx - px
            dy = cy - py
            dist = :math.sqrt(dx * dx + dy * dy)

            if dist < 1.0e-12 do
              # current estimate coincides with a data point
              {0.0, 0.0, 0.0, true}
            else
              inv = 1.0 / dist
              {nx + px * inv, ny + py * inv, dz + inv, zp}
            end
          end)

        if zero_point? do
          {:halt, {cx, cy}}
        else
          nx = num_x / denom
          ny = num_y / denom

          shift =
            :math.sqrt((nx - cx) * (nx - cx) + (ny - cy) * (ny - cy))

          if shift < epsilon do
            {:halt, {nx, ny}}
          else
            {:cont, {nx, ny}}
          end
        end
      end)

    Enum.reduce(points, 0.0, fn {px, py}, acc ->
      dx = final_x - px
      dy = final_y - py
      acc + :math.sqrt(dx * dx + dy * dy)
    end)
  end
end
```

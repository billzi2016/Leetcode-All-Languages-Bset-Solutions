# 3453. Separate Squares I

## Cpp

```cpp
class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        double total = 0;
        double lo = 1e18, hi = -1e18;
        for (auto &sq : squares) {
            double y = sq[1];
            double l = sq[2];
            total += l * l;
            lo = min(lo, y);
            hi = max(hi, y + l);
        }
        double target = total / 2.0;
        auto areaAbove = [&](double h) -> double {
            double a = 0;
            for (auto &sq : squares) {
                double y = sq[1];
                double l = sq[2];
                if (h <= y) {
                    a += l * l;
                } else if (h < y + l) {
                    a += (y + l - h) * l;
                }
            }
            return a;
        };
        for (int it = 0; it < 100; ++it) {
            double mid = (lo + hi) / 2.0;
            if (areaAbove(mid) > target)
                lo = mid;
            else
                hi = mid;
        }
        return hi;
    }
};
```

## Java

```java
class Solution {
    public double separateSquares(int[][] squares) {
        int n = squares.length;
        double totalArea = 0.0;
        double minY = Double.MAX_VALUE;
        double maxY = -Double.MAX_VALUE;
        for (int[] s : squares) {
            double y = s[1];
            double l = s[2];
            totalArea += l * l;
            if (y < minY) minY = y;
            if (y + l > maxY) maxY = y + l;
        }
        double target = totalArea / 2.0;
        double low = minY, high = maxY;
        for (int iter = 0; iter < 100; ++iter) {
            double mid = (low + high) * 0.5;
            double areaAbove = 0.0;
            for (int[] s : squares) {
                double y0 = s[1];
                double l = s[2];
                double top = y0 + l;
                if (mid <= y0) {
                    areaAbove += l * l;
                } else if (mid < top) {
                    areaAbove += (top - mid) * l;
                }
            }
            if (areaAbove > target) {
                low = mid; // need higher line to reduce above area
            } else {
                high = mid;
            }
        }
        return low;
    }
}
```

## Python

```python
class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        total = 0.0
        lo = float('inf')
        hi = -float('inf')
        for x, y, l in squares:
            area = l * l
            total += area
            if y < lo:
                lo = y
            top = y + l
            if top > hi:
                hi = top

        target = total / 2.0

        for _ in range(80):  # sufficient for 1e-5 precision
            mid = (lo + hi) * 0.5
            above = 0.0
            for x, y, l in squares:
                if mid <= y:
                    above += l * l
                elif mid < y + l:
                    above += (y + l - mid) * l
                # else contributes 0
            if above > target:
                lo = mid
            else:
                hi = mid

        return lo
```

## Python3

```python
class Solution:
    def separateSquares(self, squares):
        # Determine search bounds
        lo = min(y for _, y, _ in squares)
        hi = max(y + l for _, y, l in squares)

        def f(h):
            total = 0.0
            for _, y, l in squares:
                top = y + l
                area = l * l
                if h <= y:
                    total += area
                elif h >= top:
                    total -= area
                else:
                    # portion above minus below
                    total += (top - h) * l - (h - y) * l
            return total

        # Binary search for root where f(h)=0, f is decreasing
        for _ in range(80):  # sufficient for 1e-5 precision
            mid = (lo + hi) / 2.0
            if f(mid) >= 0:
                lo = mid
            else:
                hi = mid
        return lo
```

## C

```c
#include <stddef.h>
#include <float.h>

double separateSquares(int** squares, int squaresSize, int* squaresColSize) {
    if (squaresSize == 0) return 0.0;
    
    double totalArea = 0.0;
    long long minY = LLONG_MAX;
    long long maxTop = LLONG_MIN;
    
    for (int i = 0; i < squaresSize; ++i) {
        long long x = squares[i][0];
        long long y = squares[i][1];
        long long l = squares[i][2];
        totalArea += (double)l * (double)l;
        if (y < minY) minY = y;
        if (y + l > maxTop) maxTop = y + l;
    }
    
    double target = totalArea / 2.0;
    double low = (double)minY;
    double high = (double)maxTop;
    
    for (int iter = 0; iter < 100; ++iter) {
        double mid = (low + high) * 0.5;
        double above = 0.0;
        for (int i = 0; i < squaresSize; ++i) {
            long long y = squares[i][1];
            long long l = squares[i][2];
            if (mid <= y) {
                above += (double)l * (double)l;
            } else if (mid >= y + l) {
                // contributes nothing
            } else {
                double height = (double)(y + l) - mid; // portion above the line
                above += (double)l * height;
            }
        }
        if (above > target) {
            low = mid;
        } else {
            high = mid;
        }
    }
    
    return high;
}
```

## Csharp

```csharp
public class Solution {
    public double SeparateSquares(int[][] squares) {
        int n = squares.Length;
        double totalArea = 0;
        double minY = double.MaxValue;
        double maxTop = double.MinValue;

        foreach (var s in squares) {
            double y = s[1];
            double l = s[2];
            totalArea += l * l;
            if (y < minY) minY = y;
            double top = y + l;
            if (top > maxTop) maxTop = top;
        }

        double target = totalArea / 2.0;
        double low = minY, high = maxTop;

        for (int iter = 0; iter < 100; ++iter) {
            double mid = (low + high) * 0.5;
            double above = 0;

            foreach (var s in squares) {
                double y = s[1];
                double l = s[2];
                if (mid <= y) {
                    above += l * l;
                } else if (mid < y + l) {
                    double aboveHeight = y + l - mid; // height of part above the line
                    above += aboveHeight * l;
                }
            }

            if (above > target) {
                low = mid;   // need to raise the line
            } else {
                high = mid;  // line is too high or just right
            }
        }

        return high;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} squares
 * @return {number}
 */
var separateSquares = function(squares) {
    let totalArea = 0;
    let lo = Infinity, hi = -Infinity;
    for (const [ , y, l] of squares) {
        const area = l * l;
        totalArea += area;
        if (y < lo) lo = y;
        const top = y + l;
        if (top > hi) hi = top;
    }
    const target = totalArea / 2;
    let left = lo, right = hi;
    for (let iter = 0; iter < 100; ++iter) {
        const mid = (left + right) * 0.5;
        let areaAbove = 0;
        for (const [ , y, l] of squares) {
            if (mid <= y) {
                areaAbove += l * l;
            } else if (mid < y + l) {
                areaAbove += (y + l - mid) * l;
            }
        }
        if (areaAbove > target) {
            left = mid; // need higher line to reduce above area
        } else {
            right = mid;
        }
    }
    return (left + right) * 0.5;
};
```

## Typescript

```typescript
function separateSquares(squares: number[][]): number {
    let totalArea = 0;
    let minY = Infinity;
    let maxTop = -Infinity;

    for (const [_, y, l] of squares) {
        const area = l * l;
        totalArea += area;
        if (y < minY) minY = y;
        const top = y + l;
        if (top > maxTop) maxTop = top;
    }

    const target = totalArea / 2;
    let lo = minY;
    let hi = maxTop;

    for (let iter = 0; iter < 80; ++iter) {
        const mid = (lo + hi) / 2;
        let above = 0;

        for (const [_, y, l] of squares) {
            if (mid <= y) {
                above += l * l;
            } else if (mid < y + l) {
                above += l * (y + l - mid);
            }
            // else: contribution is 0
        }

        if (above > target) {
            lo = mid; // need higher line to reduce area above
        } else {
            hi = mid;
        }
    }

    return (lo + hi) / 2;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $squares
     * @return Float
     */
    function separateSquares($squares) {
        $totalArea = 0.0;
        $minY = INF;
        $maxY = -INF;

        foreach ($squares as $sq) {
            $y = $sq[1];
            $l = $sq[2];
            $totalArea += $l * $l;
            if ($y < $minY) $minY = $y;
            $top = $y + $l;
            if ($top > $maxY) $maxY = $top;
        }

        $target = $totalArea / 2.0;
        $low = $minY;
        $high = $maxY;

        for ($iter = 0; $iter < 100; $iter++) {
            $mid = ($low + $high) / 2.0;
            $above = 0.0;

            foreach ($squares as $sq) {
                $y = $sq[1];
                $l = $sq[2];

                if ($mid <= $y) {
                    $above += $l * $l;               // whole square is above
                } elseif ($mid >= $y + $l) {
                    // whole square is below, contributes nothing
                } else {
                    $above += ($y + $l - $mid) * $l; // partial contribution
                }
            }

            if ($above > $target) {
                $low = $mid;   // need to raise the line
            } else {
                $high = $mid;  // need to lower the line
            }
        }

        return $low;
    }
}
```

## Swift

```swift
class Solution {
    func separateSquares(_ squares: [[Int]]) -> Double {
        var totalArea: Double = 0
        var minY = Double.greatestFiniteMagnitude
        var maxTop = -Double.greatestFiniteMagnitude
        
        for sq in squares {
            let y = Double(sq[1])
            let l = Double(sq[2])
            totalArea += l * l
            if y < minY { minY = y }
            let top = y + l
            if top > maxTop { maxTop = top }
        }
        
        let half = totalArea / 2.0
        var low = minY
        var high = maxTop
        
        for _ in 0..<100 {
            let mid = (low + high) / 2.0
            var above: Double = 0
            for sq in squares {
                let y = Double(sq[1])
                let l = Double(sq[2])
                if mid <= y {
                    above += l * l
                } else if mid < y + l {
                    above += (y + l - mid) * l
                }
                // else: contribution is 0
            }
            if above > half {
                low = mid
            } else {
                high = mid
            }
        }
        
        return (low + high) / 2.0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun separateSquares(squares: Array<IntArray>): Double {
        var minY = Long.MAX_VALUE
        var maxTop = Long.MIN_VALUE
        var totalArea = 0L
        for (sq in squares) {
            val y = sq[1].toLong()
            val l = sq[2].toLong()
            if (y < minY) minY = y
            val top = y + l
            if (top > maxTop) maxTop = top
            totalArea += l * l
        }
        var low = minY.toDouble()
        var high = maxTop.toDouble()
        val target = totalArea / 2.0

        repeat(80) {
            val mid = (low + high) / 2.0
            var sumAbove = 0.0
            for (sq in squares) {
                val y = sq[1].toLong()
                val l = sq[2].toLong()
                when {
                    mid <= y -> sumAbove += (l * l).toDouble()
                    mid >= y + l -> { /* nothing */ }
                    else -> {
                        val aboveHeight = (y + l - mid)
                        sumAbove += aboveHeight * l.toDouble()
                    }
                }
            }
            if (sumAbove > target) {
                low = mid
            } else {
                high = mid
            }
        }
        return (low + high) / 2.0
    }
}
```

## Dart

```dart
class Solution {
  double separateSquares(List<List<int>> squares) {
    double totalArea = 0.0;
    double lo = double.infinity;
    double hi = -double.infinity;

    // Preprocess squares: store y, l, top for faster access
    final List<_Sq> data = [];
    for (var s in squares) {
      double y = s[1].toDouble();
      double l = s[2].toDouble();
      double top = y + l;
      totalArea += l * l;
      if (y < lo) lo = y;
      if (top > hi) hi = top;
      data.add(_Sq(y, l, top));
    }

    double target = totalArea / 2.0;

    for (int iter = 0; iter < 80; ++iter) {
      double mid = (lo + hi) * 0.5;
      double above = 0.0;
      for (var sq in data) {
        if (mid <= sq.y) {
          // whole square is above
          above += sq.l * sq.l;
        } else if (mid < sq.top) {
          // partially above
          above += sq.l * (sq.top - mid);
        }
        // else completely below, contributes nothing
      }

      if (above > target) {
        // need to raise the line to reduce area above
        lo = mid;
      } else {
        hi = mid;
      }
    }

    return (lo + hi) * 0.5;
  }
}

class _Sq {
  final double y;
  final double l;
  final double top;
  _Sq(this.y, this.l, this.top);
}
```

## Golang

```go
package main

import (
	"math"
)

func separateSquares(squares [][]int) float64 {
	lo := math.MaxFloat64
	hi := -math.MaxFloat64
	totalArea := 0.0

	for _, s := range squares {
		y := float64(s[1])
		l := float64(s[2])
		if y < lo {
			lo = y
		}
		top := y + l
		if top > hi {
			hi = top
		}
		totalArea += l * l
	}

	target := totalArea / 2.0

	for iter := 0; iter < 80; iter++ {
		mid := (lo + hi) / 2
		above := 0.0
		for _, s := range squares {
			y := float64(s[1])
			l := float64(s[2])
			bottom := y
			top := y + l
			if mid <= bottom {
				above += l * l
			} else if mid < top {
				above += (top - mid) * l
			}
		}
		if above > target {
			lo = mid
		} else {
			hi = mid
		}
	}
	return (lo + hi) / 2
}
```

## Ruby

```ruby
def separate_squares(squares)
  total = 0.0
  min_y = Float::INFINITY
  max_top = -Float::INFINITY

  squares.each do |x, y, l|
    area = l * l
    total += area
    min_y = y if y < min_y
    top = y + l
    max_top = top if top > max_top
  end

  target = total / 2.0
  low = min_y.to_f
  high = max_top.to_f

  80.times do
    mid = (low + high) / 2.0
    above = 0.0
    squares.each do |x, y, l|
      if mid <= y
        above += l * l
      elsif mid < y + l
        above += l * (y + l - mid)
      end
    end

    if above > target
      low = mid
    else
      high = mid
    end
  end

  high
end
```

## Scala

```scala
object Solution {
    def separateSquares(squares: Array[Array[Int]]): Double = {
        var totalArea: Double = 0.0
        var lo = Double.MaxValue
        var hi = Double.MinValue

        for (sq <- squares) {
            val y = sq(1).toLong
            val l = sq(2).toLong
            totalArea += l * l
            if (y < lo) lo = y.toDouble
            val top = y + l
            if (top > hi) hi = top.toDouble
        }

        var left = lo
        var right = hi
        for (_ <- 0 until 100) {
            val mid = (left + right) / 2.0
            var above: Double = 0.0

            for (sq <- squares) {
                val y = sq(1).toDouble
                val l = sq(2).toDouble
                if (mid <= y) {
                    above += l * l
                } else if (mid < y + l) {
                    val topHeight = y + l - mid
                    above += topHeight * l
                }
            }

            if (above > totalArea / 2.0) {
                left = mid
            } else {
                right = mid
            }
        }

        (left + right) / 2.0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn separate_squares(squares: Vec<Vec<i32>>) -> f64 {
        // Determine search interval
        let mut low = std::f64::INFINITY;
        let mut high = std::f64::NEG_INFINITY;
        for sq in &squares {
            let y = sq[1] as f64;
            let l = sq[2] as f64;
            if y < low { low = y; }
            if y + l > high { high = y + l; }
        }

        // Binary search for the root of the monotonic function
        for _ in 0..100 {
            let mid = (low + high) / 2.0;
            let mut diff = 0f64;
            for sq in &squares {
                let y = sq[1] as f64;
                let l = sq[2] as f64;
                if mid <= y {
                    // line below the square
                    diff += l * l;
                } else if mid >= y + l {
                    // line above the square
                    diff -= l * l;
                } else {
                    // line cuts through the square
                    let above = (y + l - mid) * l;
                    let below = (mid - y) * l;
                    diff += above - below; // equals (2*y + l - 2*mid) * l
                }
            }
            if diff > 0.0 {
                low = mid;   // need to raise the line
            } else {
                high = mid;  // need to lower the line
            }
        }

        (low + high) / 2.0
    }
}
```

## Racket

```racket
#lang racket
(require racket/contract)

(define/contract (separate-squares squares)
  (-> (listof (listof exact-integer?)) flonum?)
  (let* ((total-area
           (for/sum ([sq squares])
             (let ((l (list-ref sq 2)))
               (* l l))))
         (target (/ total-area 2.0))
         (min-y (apply min (map (lambda (sq) (list-ref sq 1)) squares)))
         (max-top (apply max (map (lambda (sq) (+ (list-ref sq 1) (list-ref sq 2))) squares))))
    (let loop ((low (exact->inexact min-y))
               (high (exact->inexact max-top))
               (iter 0))
      (if (or (> iter 80) (< (- high low) 1e-7))
          high
          (let* ((mid (/ (+ low high) 2.0))
                 (area-above
                   (for/sum ([sq squares])
                     (let* ((y0 (list-ref sq 1))
                            (l (list-ref sq 2)))
                       (cond
                         [(<= mid y0) (* l l)]
                         [(>= mid (+ y0 l)) 0]
                         [else (* (- (+ y0 l) mid) l)])))))
            (if (> area-above target)
                (loop mid high (+ iter 1))
                (loop low mid (+ iter 1))))))))
```

## Erlang

```erlang
-module(solution).
-export([separate_squares/1]).

-spec separate_squares(Squares :: [[integer()]]) -> float().
separate_squares(Squares) ->
    TotalArea = lists:foldl(fun([_X,_Y,L], Acc) -> Acc + L * L end, 0, Squares),
    Target = TotalArea / 2.0,
    MinY = lists:min([Y || [_X,Y,_L] <- Squares]),
    MaxTop = lists:max([Y+L || [_X,Y,L] <- Squares]),
    binary_search(MinY, MaxTop, Target, Squares, 60).

binary_search(Low, High, Target, Squares, 0) ->
    High;
binary_search(Low, High, Target, Squares, Iter) ->
    Mid = (Low + High) / 2,
    Area = area_above(Mid, Squares),
    if
        Area > Target ->
            binary_search(Mid, High, Target, Squares, Iter - 1);
        true ->
            binary_search(Low, Mid, Target, Squares, Iter - 1)
    end.

area_above(H, Squares) ->
    lists:foldl(fun([_X,Y,L], Acc) ->
        Contribution =
            if
                H =< Y -> L * L * 1.0;
                H >= Y + L -> 0.0;
                true -> (Y + L - H) * L * 1.0
            end,
        Acc + Contribution
    end, 0.0, Squares).
```

## Elixir

```elixir
defmodule Solution do
  @spec separate_squares(squares :: [[integer]]) :: float
  def separate_squares(squares) do
    total = Enum.reduce(squares, 0, fn [_x, _y, l], acc -> acc + l * l end)
    half = total / 2.0

    min_y =
      squares
      |> Enum.map(fn [_x, y, _l] -> y end)
      |> Enum.min()

    max_top =
      squares
      |> Enum.map(fn [_x, y, l] -> y + l end)
      |> Enum.max()

    {low, high} = {min_y * 1.0, max_top * 1.0}

    {result, _} =
      Enum.reduce(1..80, {low, high}, fn _, {lo, hi} ->
        mid = (lo + hi) / 2.0
        above = area_above(squares, mid)

        if above > half do
          {mid, hi}
        else
          {lo, mid}
        end
      end)

    result
  end

  defp area_above(squares, h) do
    Enum.reduce(squares, 0.0, fn [_x, y, l], acc ->
      top = y + l

      contrib =
        if top > h do
          (top - h) * l
        else
          0.0
        end

      acc + contrib
    end)
  end
end
```

# 3047. Find the Largest Area of Square Inside Two Rectangles

## Cpp

```cpp
class Solution {
public:
    long long largestSquareArea(vector<vector<int>>& bottomLeft, vector<vector<int>>& topRight) {
        int n = bottomLeft.size();
        long long bestSide = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int x1 = max(bottomLeft[i][0], bottomLeft[j][0]);
                int y1 = max(bottomLeft[i][1], bottomLeft[j][1]);
                int x2 = min(topRight[i][0], topRight[j][0]);
                int y2 = min(topRight[i][1], topRight[j][1]);
                if (x1 < x2 && y1 < y2) {
                    long long side = min(x2 - x1, y2 - y1);
                    if (side > bestSide) bestSide = side;
                }
            }
        }
        return bestSide * bestSide;
    }
};
```

## Java

```java
class Solution {
    public long largestSquareArea(int[][] bottomLeft, int[][] topRight) {
        int n = bottomLeft.length;
        int maxSide = 0;
        for (int i = 0; i < n; i++) {
            int x1i = bottomLeft[i][0];
            int y1i = bottomLeft[i][1];
            int x2i = topRight[i][0];
            int y2i = topRight[i][1];
            for (int j = i + 1; j < n; j++) {
                int ix1 = Math.max(x1i, bottomLeft[j][0]);
                int iy1 = Math.max(y1i, bottomLeft[j][1]);
                int ix2 = Math.min(x2i, topRight[j][0]);
                int iy2 = Math.min(y2i, topRight[j][1]);
                if (ix1 < ix2 && iy1 < iy2) {
                    int side = Math.min(ix2 - ix1, iy2 - iy1);
                    if (side > maxSide) {
                        maxSide = side;
                    }
                }
            }
        }
        return (long) maxSide * maxSide;
    }
}
```

## Python

```python
class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        n = len(bottomLeft)
        max_side = 0
        for i in range(n):
            x1_i, y1_i = bottomLeft[i]
            x2_i, y2_i = topRight[i]
            for j in range(i + 1, n):
                x1_j, y1_j = bottomLeft[j]
                x2_j, y2_j = topRight[j]

                # intersection rectangle
                ix1 = max(x1_i, x1_j)
                iy1 = max(y1_i, y1_j)
                ix2 = min(x2_i, x2_j)
                iy2 = min(y2_i, y2_j)

                if ix1 < ix2 and iy1 < iy2:
                    side = min(ix2 - ix1, iy2 - iy1)
                    if side > max_side:
                        max_side = side
        return max_side * max_side
```

## Python3

```python
class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        n = len(bottomLeft)
        max_side = 0
        for i in range(n):
            ax1, ay1 = bottomLeft[i]
            ax2, ay2 = topRight[i]
            for j in range(i + 1, n):
                bx1, by1 = bottomLeft[j]
                bx2, by2 = topRight[j]

                left = max(ax1, bx1)
                right = min(ax2, bx2)
                if left >= right:
                    continue

                bottom = max(ay1, by1)
                top = min(ay2, by2)
                if bottom >= top:
                    continue

                side = min(right - left, top - bottom)
                if side > max_side:
                    max_side = side
        return max_side * max_side
```

## C

```c
#include <stddef.h>

long long largestSquareArea(int** bottomLeft, int bottomLeftSize, int* bottomLeftColSize,
                            int** topRight, int topRightSize, int* topRightColSize) {
    int n = bottomLeftSize;
    long long maxSide = 0;
    for (int i = 0; i < n; ++i) {
        int a_i = bottomLeft[i][0];
        int b_i = bottomLeft[i][1];
        int c_i = topRight[i][0];
        int d_i = topRight[i][1];
        for (int j = i + 1; j < n; ++j) {
            int a_j = bottomLeft[j][0];
            int b_j = bottomLeft[j][1];
            int c_j = topRight[j][0];
            int d_j = topRight[j][1];

            int left   = a_i > a_j ? a_i : a_j;
            int right  = c_i < c_j ? c_i : c_j;
            int bottom = b_i > b_j ? b_i : b_j;
            int top    = d_i < d_j ? d_i : d_j;

            int width  = right - left;
            int height = top - bottom;
            if (width > 0 && height > 0) {
                int side = width < height ? width : height;
                if ((long long)side > maxSide) {
                    maxSide = side;
                }
            }
        }
    }
    return maxSide * maxSide;
}
```

## Csharp

```csharp
public class Solution {
    public long LargestSquareArea(int[][] bottomLeft, int[][] topRight) {
        int n = bottomLeft.Length;
        long maxSide = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int x1 = Math.Max(bottomLeft[i][0], bottomLeft[j][0]);
                int y1 = Math.Max(bottomLeft[i][1], bottomLeft[j][1]);
                int x2 = Math.Min(topRight[i][0], topRight[j][0]);
                int y2 = Math.Min(topRight[i][1], topRight[j][1]);

                if (x1 < x2 && y1 < y2) {
                    long side = Math.Min(x2 - x1, y2 - y1);
                    if (side > maxSide) {
                        maxSide = side;
                    }
                }
            }
        }
        return maxSide * maxSide;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} bottomLeft
 * @param {number[][]} topRight
 * @return {number}
 */
var largestSquareArea = function(bottomLeft, topRight) {
    const n = bottomLeft.length;
    let maxSide = 0;
    for (let i = 0; i < n; ++i) {
        const xi1 = bottomLeft[i][0];
        const yi1 = bottomLeft[i][1];
        const xi2 = topRight[i][0];
        const yi2 = topRight[i][1];
        for (let j = i + 1; j < n; ++j) {
            const x1 = Math.max(xi1, bottomLeft[j][0]);
            const y1 = Math.max(yi1, bottomLeft[j][1]);
            const x2 = Math.min(xi2, topRight[j][0]);
            const y2 = Math.min(yi2, topRight[j][1]);
            if (x1 < x2 && y1 < y2) {
                const side = Math.min(x2 - x1, y2 - y1);
                if (side > maxSide) maxSide = side;
            }
        }
    }
    return maxSide * maxSide;
};
```

## Typescript

```typescript
function largestSquareArea(bottomLeft: number[][], topRight: number[][]): number {
    const n = bottomLeft.length;
    let maxSide = 0;
    for (let i = 0; i < n; i++) {
        const [x1i, y1i] = bottomLeft[i];
        const [x2i, y2i] = topRight[i];
        for (let j = i + 1; j < n; j++) {
            const x1 = Math.max(x1i, bottomLeft[j][0]);
            const y1 = Math.max(y1i, bottomLeft[j][1]);
            const x2 = Math.min(x2i, topRight[j][0]);
            const y2 = Math.min(y2i, topRight[j][1]);
            if (x1 < x2 && y1 < y2) {
                const side = Math.min(x2 - x1, y2 - y1);
                if (side > maxSide) maxSide = side;
            }
        }
    }
    return maxSide * maxSide;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $bottomLeft
     * @param Integer[][] $topRight
     * @return Integer
     */
    function largestSquareArea($bottomLeft, $topRight) {
        $n = count($bottomLeft);
        $maxSide = 0;
        for ($i = 0; $i < $n; ++$i) {
            for ($j = $i + 1; $j < $n; ++$j) {
                $x1 = max($bottomLeft[$i][0], $bottomLeft[$j][0]);
                $y1 = max($bottomLeft[$i][1], $bottomLeft[$j][1]);
                $x2 = min($topRight[$i][0], $topRight[$j][0]);
                $y2 = min($topRight[$i][1], $topRight[$j][1]);

                if ($x1 < $x2 && $y1 < $y2) {
                    $side = min($x2 - $x1, $y2 - $y1);
                    if ($side > $maxSide) {
                        $maxSide = $side;
                    }
                }
            }
        }
        return $maxSide * $maxSide;
    }
}
```

## Swift

```swift
class Solution {
    func largestSquareArea(_ bottomLeft: [[Int]], _ topRight: [[Int]]) -> Int {
        let n = bottomLeft.count
        var maxSide = 0
        for i in 0..<n {
            let blI = bottomLeft[i]
            let trI = topRight[i]
            for j in (i + 1)..<n {
                let blJ = bottomLeft[j]
                let trJ = topRight[j]
                
                let x1 = max(blI[0], blJ[0])
                let y1 = max(blI[1], blJ[1])
                let x2 = min(trI[0], trJ[0])
                let y2 = min(trI[1], trJ[1])
                
                if x1 < x2 && y1 < y2 {
                    let side = min(x2 - x1, y2 - y1)
                    if side > maxSide {
                        maxSide = side
                    }
                }
            }
        }
        return maxSide * maxSide
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestSquareArea(bottomLeft: Array<IntArray>, topRight: Array<IntArray>): Long {
        val n = bottomLeft.size
        var maxArea = 0L
        for (i in 0 until n) {
            val blI = bottomLeft[i]
            val trI = topRight[i]
            for (j in i + 1 until n) {
                val x1 = maxOf(blI[0], bottomLeft[j][0])
                val y1 = maxOf(blI[1], bottomLeft[j][1])
                val x2 = minOf(trI[0], topRight[j][0])
                val y2 = minOf(trI[1], topRight[j][1])
                if (x1 < x2 && y1 < y2) {
                    val side = minOf(x2 - x1, y2 - y1).toLong()
                    val area = side * side
                    if (area > maxArea) maxArea = area
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
  int largestSquareArea(List<List<int>> bottomLeft, List<List<int>> topRight) {
    int n = bottomLeft.length;
    int maxSide = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        int x1 = bottomLeft[i][0] > bottomLeft[j][0] ? bottomLeft[i][0] : bottomLeft[j][0];
        int y1 = bottomLeft[i][1] > bottomLeft[j][1] ? bottomLeft[i][1] : bottomLeft[j][1];
        int x2 = topRight[i][0] < topRight[j][0] ? topRight[i][0] : topRight[j][0];
        int y2 = topRight[i][1] < topRight[j][1] ? topRight[i][1] : topRight[j][1];
        if (x1 < x2 && y1 < y2) {
          int sideX = x2 - x1;
          int sideY = y2 - y1;
          int possibleSide = sideX < sideY ? sideX : sideY;
          if (possibleSide > maxSide) maxSide = possibleSide;
        }
      }
    }
    return maxSide * maxSide;
  }
}
```

## Golang

```go
func largestSquareArea(bottomLeft [][]int, topRight [][]int) int64 {
	n := len(bottomLeft)
	maxSide := 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			x1 := bottomLeft[i][0]
			if bottomLeft[j][0] > x1 {
				x1 = bottomLeft[j][0]
			}
			y1 := bottomLeft[i][1]
			if bottomLeft[j][1] > y1 {
				y1 = bottomLeft[j][1]
			}
			x2 := topRight[i][0]
			if topRight[j][0] < x2 {
				x2 = topRight[j][0]
			}
			y2 := topRight[i][1]
			if topRight[j][1] < y2 {
				y2 = topRight[j][1]
			}
			if x1 < x2 && y1 < y2 {
				width := x2 - x1
				height := y2 - y1
				side := width
				if height < side {
					side = height
				}
				if side > maxSide {
					maxSide = side
				}
			}
		}
	}
	return int64(maxSide) * int64(maxSide)
}
```

## Ruby

```ruby
def largest_square_area(bottom_left, top_right)
  n = bottom_left.length
  max_side = 0
  (0...n).each do |i|
    (i + 1...n).each do |j|
      left   = [bottom_left[i][0], bottom_left[j][0]].max
      bottom = [bottom_left[i][1], bottom_left[j][1]].max
      right  = [top_right[i][0], top_right[j][0]].min
      top    = [top_right[i][1], top_right[j][1]].min
      if left < right && bottom < top
        side = [right - left, top - bottom].min
        max_side = side if side > max_side
      end
    end
  end
  max_side * max_side
end
```

## Scala

```scala
object Solution {
    def largestSquareArea(bottomLeft: Array[Array[Int]], topRight: Array[Array[Int]]): Long = {
        val n = bottomLeft.length
        var maxSide: Long = 0L
        var i = 0
        while (i < n) {
            var j = i + 1
            while (j < n) {
                val x1 = math.max(bottomLeft(i)(0), bottomLeft(j)(0))
                val y1 = math.max(bottomLeft(i)(1), bottomLeft(j)(1))
                val x2 = math.min(topRight(i)(0), topRight(j)(0))
                val y2 = math.min(topRight(i)(1), topRight(j)(1))
                if (x1 < x2 && y1 < y2) {
                    val side = math.min(x2 - x1, y2 - y1).toLong
                    if (side > maxSide) maxSide = side
                }
                j += 1
            }
            i += 1
        }
        maxSide * maxSide
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_square_area(bottom_left: Vec<Vec<i32>>, top_right: Vec<Vec<i32>>) -> i64 {
        let n = bottom_left.len();
        let mut max_side: i32 = 0;
        for i in 0..n {
            for j in (i + 1)..n {
                let x1 = bottom_left[i][0].max(bottom_left[j][0]);
                let y1 = bottom_left[i][1].max(bottom_left[j][1]);
                let x2 = top_right[i][0].min(top_right[j][0]);
                let y2 = top_right[i][1].min(top_right[j][1]);
                if x1 < x2 && y1 < y2 {
                    let side = (x2 - x1).min(y2 - y1);
                    if side > max_side {
                        max_side = side;
                    }
                }
            }
        }
        let ms = max_side as i64;
        ms * ms
    }
}
```

## Racket

```racket
(define/contract (largest-square-area bottomLeft topRight)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      exact-integer?)
  (let* ((bl-vec (list->vector bottomLeft))
         (tr-vec (list->vector topRight))
         (n (vector-length bl-vec)))
    (let loop-i ([i 0] [max-side 0])
      (if (= i n)
          (* max-side max-side)
          (let loop-j ([j (add1 i)] [cur-max max-side])
            (if (>= j n)
                (loop-i (add1 i) cur-max)
                (let* ((bl1 (vector-ref bl-vec i))
                       (tr1 (vector-ref tr-vec i))
                       (bl2 (vector-ref bl-vec j))
                       (tr2 (vector-ref tr-vec j))
                       (x1 (max (first bl1) (first bl2)))
                       (y1 (max (second bl1) (second bl2)))
                       (x2 (min (first tr1) (first tr2)))
                       (y2 (min (second tr1) (second tr2))))
                  (if (and (< x1 x2) (< y1 y2))
                      (let ([side (min (- x2 x1) (- y2 y1))])
                        (loop-j (add1 j) (max cur-max side)))
                      (loop-j (add1 j) cur-max))))))))))
```

## Erlang

```erlang
-module(solution).
-export([largest_square_area/2]).

-spec largest_square_area(BottomLeft :: [[integer()]], TopRight :: [[integer()]]) -> integer().
largest_square_area(BottomLeft, TopRight) ->
    Rects = lists:zipwith(fun([X1,Y1], [X2,Y2]) -> {X1,Y1,X2,Y2} end,
                          BottomLeft, TopRight),
    MaxSide = max_side(Rects, 0),
    MaxSide * MaxSide.

max_side([], Max) -> Max;
max_side([R|Rest], Max) ->
    NewMax = max_with_rest(R, Rest, Max),
    max_side(Rest, NewMax).

max_with_rest(_R, [], Max) -> Max;
max_with_rest({X1,Y1,X2,Y2}=R, [{X1b,Y1b,X2b,Y2b}|Tail], Max) ->
    XLeft   = erlang:max(X1,  X1b),
    YBottom = erlang:max(Y1,  Y1b),
    XRight  = erlang:min(X2,  X2b),
    YTop    = erlang:min(Y2,  Y2b),
    case (XRight > XLeft) andalso (YTop > YBottom) of
        true ->
            Side   = erlang:min(XRight - XLeft, YTop - YBottom),
            NewMax = if Side > Max -> Side; true -> Max end,
            max_with_rest(R, Tail, NewMax);
        false ->
            max_with_rest(R, Tail, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_square_area(bottom_left :: [[integer]], top_right :: [[integer]]) :: integer
  def largest_square_area(bottom_left, top_right) do
    rects = Enum.zip(bottom_left, top_right)
    max_side = loop(rects, 0)
    max_side * max_side
  end

  defp loop([], acc), do: acc
  defp loop([_], acc), do: acc
  defp loop([head | tail], acc) do
    new_acc = compare(head, tail, acc)
    loop(tail, new_acc)
  end

  defp compare(_, [], acc), do: acc

  defp compare({bl_i, tr_i}, [{bl_j, tr_j} | rest], acc) do
    [bl_xi, bl_yi] = bl_i
    [tr_xi, tr_yi] = tr_i
    [bl_xj, bl_yj] = bl_j
    [tr_xj, tr_yj] = tr_j

    x1 = max(bl_xi, bl_xj)
    y1 = max(bl_yi, bl_yj)
    x2 = min(tr_xi, tr_xj)
    y2 = min(tr_yi, tr_yj)

    new_acc =
      if x1 < x2 and y1 < y2 do
        side = min(x2 - x1, y2 - y1)
        max(acc, side)
      else
        acc
      end

    compare({bl_i, tr_i}, rest, new_acc)
  end
end
```

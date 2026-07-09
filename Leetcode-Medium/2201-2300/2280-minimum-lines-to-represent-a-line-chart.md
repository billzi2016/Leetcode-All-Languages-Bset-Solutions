# 2280. Minimum Lines to Represent a Line Chart

## Cpp

```cpp
class Solution {
public:
    int minimumLines(vector<vector<int>>& stockPrices) {
        int n = stockPrices.size();
        if (n <= 1) return 0;
        sort(stockPrices.begin(), stockPrices.end(),
             [](const vector<int>& a, const vector<int>& b){ return a[0] < b[0]; });
        
        auto getSlope = [&](int i, int j) -> pair<long long,long long> {
            long long dy = (long long)stockPrices[j][1] - stockPrices[i][1];
            long long dx = (long long)stockPrices[j][0] - stockPrices[i][0];
            long long g = std::gcd(std::llabs(dy), std::llabs(dx));
            dy /= g;
            dx /= g;
            return {dy, dx};
        };
        
        int lines = 1;
        auto prev = getSlope(0, 1);
        for (int i = 2; i < n; ++i) {
            auto cur = getSlope(i - 1, i);
            if (cur != prev) {
                ++lines;
                prev = cur;
            }
        }
        return lines;
    }
};
```

## Java

```java
class Solution {
    public int minimumLines(int[][] stockPrices) {
        int n = stockPrices.length;
        if (n <= 1) return 0;
        java.util.Arrays.sort(stockPrices, (a, b) -> Integer.compare(a[0], b[0]));
        if (n == 2) return 1;

        long prevDy = stockPrices[1][1] - stockPrices[0][1];
        long prevDx = stockPrices[1][0] - stockPrices[0][0];
        long g = gcd(Math.abs(prevDy), Math.abs(prevDx));
        prevDy /= g;
        prevDx /= g;

        int lines = 1;
        for (int i = 2; i < n; ++i) {
            long curDy = stockPrices[i][1] - stockPrices[i - 1][1];
            long curDx = stockPrices[i][0] - stockPrices[i - 1][0];
            g = gcd(Math.abs(curDy), Math.abs(curDx));
            curDy /= g;
            curDx /= g;

            if (curDy != prevDy || curDx != prevDx) {
                lines++;
                prevDy = curDy;
                prevDx = curDx;
            }
        }
        return lines;
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def minimumLines(self, stockPrices):
        """
        :type stockPrices: List[List[int]]
        :rtype: int
        """
        n = len(stockPrices)
        if n <= 2:
            return max(0, n - 1)
        stockPrices.sort(key=lambda p: p[0])
        lines = 1
        prev_dx = stockPrices[1][0] - stockPrices[0][0]
        prev_dy = stockPrices[1][1] - stockPrices[0][1]
        for i in range(2, n):
            cur_dx = stockPrices[i][0] - stockPrices[i-1][0]
            cur_dy = stockPrices[i][1] - stockPrices[i-1][1]
            if prev_dy * cur_dx != cur_dy * prev_dx:
                lines += 1
                prev_dx, prev_dy = cur_dx, cur_dy
        return lines
```

## Python3

```python
import math
from typing import List

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        if n <= 1:
            return 0
        stockPrices.sort(key=lambda p: p[0])
        lines = 0
        prev_slope = None
        for i in range(1, n):
            x1, y1 = stockPrices[i - 1]
            x2, y2 = stockPrices[i]
            dy = y2 - y1
            dx = x2 - x1
            g = math.gcd(dy, dx)
            dy //= g
            dx //= g
            if dx < 0:
                dx = -dx
                dy = -dy
            cur_slope = (dy, dx)
            if cur_slope != prev_slope:
                lines += 1
                prev_slope = cur_slope
        return lines
```

## C

```c
#include <stdlib.h>

static int cmp(const void *a, const void *b) {
    const int *pa = *(const int **)a;
    const int *pb = *(const int **)b;
    if (pa[0] < pb[0]) return -1;
    if (pa[0] > pb[0]) return 1;
    return 0;
}

int minimumLines(int** stockPrices, int stockPricesSize, int* stockPricesColSize) {
    if (stockPricesSize <= 2) return stockPricesSize - 1;

    qsort(stockPrices, stockPricesSize, sizeof(int *), cmp);

    long long lines = 1;
    for (int i = 2; i < stockPricesSize; ++i) {
        long long x1 = stockPrices[i - 2][0];
        long long y1 = stockPrices[i - 2][1];
        long long x2 = stockPrices[i - 1][0];
        long long y2 = stockPrices[i - 1][1];
        long long x3 = stockPrices[i][0];
        long long y3 = stockPrices[i][1];

        long long left  = (y2 - y1) * (x3 - x2);
        long long right = (y3 - y2) * (x2 - x1);

        if (left != right) ++lines;
    }
    return (int)lines;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumLines(int[][] stockPrices) {
        int n = stockPrices.Length;
        if (n <= 2) return n - 1;
        System.Array.Sort(stockPrices, (a, b) => a[0].CompareTo(b[0]));
        int lines = 1;
        for (int i = 2; i < n; i++) {
            long x1 = stockPrices[i - 1][0] - stockPrices[i - 2][0];
            long y1 = stockPrices[i - 1][1] - stockPrices[i - 2][1];
            long x2 = stockPrices[i][0] - stockPrices[i - 1][0];
            long y2 = stockPrices[i][1] - stockPrices[i - 1][1];
            if (y1 * x2 != y2 * x1) {
                lines++;
            }
        }
        return lines;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} stockPrices
 * @return {number}
 */
var minimumLines = function(stockPrices) {
    const n = stockPrices.length;
    if (n <= 1) return 0;
    stockPrices.sort((a, b) => a[0] - b[0]);
    let lines = 1;
    for (let i = 2; i < n; i++) {
        const x1 = stockPrices[i - 2][0], y1 = stockPrices[i - 2][1];
        const x2 = stockPrices[i - 1][0], y2 = stockPrices[i - 1][1];
        const x3 = stockPrices[i][0],     y3 = stockPrices[i][1];
        const left = BigInt(y2 - y1) * BigInt(x3 - x2);
        const right = BigInt(y3 - y2) * BigInt(x2 - x1);
        if (left !== right) lines++;
    }
    return lines;
};
```

## Typescript

```typescript
function minimumLines(stockPrices: number[][]): number {
    const n = stockPrices.length;
    if (n <= 1) return 0;

    // Sort points by day (x-coordinate)
    stockPrices.sort((a, b) => a[0] - b[0]);

    let lines = 1; // At least one line segment when n >= 2
    let prevDy = stockPrices[1][1] - stockPrices[0][1];
    let prevDx = stockPrices[1][0] - stockPrices[0][0];

    for (let i = 2; i < n; ++i) {
        const dy = stockPrices[i][1] - stockPrices[i - 1][1];
        const dx = stockPrices[i][0] - stockPrices[i - 1][0];

        // Compare slopes using cross multiplication with BigInt to avoid precision loss
        if (BigInt(dy) * BigInt(prevDx) !== BigInt(prevDy) * BigInt(dx)) {
            ++lines;
            prevDy = dy;
            prevDx = dx;
        }
    }

    return lines;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $stockPrices
     * @return Integer
     */
    function minimumLines($stockPrices) {
        $n = count($stockPrices);
        if ($n <= 2) {
            return max(0, $n - 1);
        }
        usort($stockPrices, function($a, $b) {
            return $a[0] <=> $b[0];
        });
        // initial slope
        $dxPrev = $stockPrices[1][0] - $stockPrices[0][0];
        $dyPrev = $stockPrices[1][1] - $stockPrices[0][1];
        $g = $this->gcd(abs($dyPrev), $dxPrev);
        $dyPrev /= $g;
        $dxPrev /= $g;

        $lines = 1;
        for ($i = 2; $i < $n; $i++) {
            $dxCurr = $stockPrices[$i][0] - $stockPrices[$i - 1][0];
            $dyCurr = $stockPrices[$i][1] - $stockPrices[$i - 1][1];
            $g = $this->gcd(abs($dyCurr), $dxCurr);
            $dyCurr /= $g;
            $dxCurr /= $g;

            if ($dyCurr !== $dyPrev || $dxCurr !== $dxPrev) {
                $lines++;
                $dyPrev = $dyCurr;
                $dxPrev = $dxCurr;
            }
        }
        return $lines;
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }
}
```

## Swift

```swift
class Solution {
    func minimumLines(_ stockPrices: [[Int]]) -> Int {
        let sorted = stockPrices.sorted { $0[0] < $1[0] }
        let n = sorted.count
        if n <= 2 { return max(0, n - 1) }
        var lines = 1
        for i in 2..<n {
            let x1 = Int64(sorted[i-2][0])
            let y1 = Int64(sorted[i-2][1])
            let x2 = Int64(sorted[i-1][0])
            let y2 = Int64(sorted[i-1][1])
            let x3 = Int64(sorted[i][0])
            let y3 = Int64(sorted[i][1])
            
            let left = (y2 - y1) * (x3 - x2)
            let right = (y3 - y2) * (x2 - x1)
            
            if left != right {
                lines += 1
            }
        }
        return lines
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumLines(stockPrices: Array<IntArray>): Int {
        val n = stockPrices.size
        if (n <= 1) return 0
        val points = stockPrices.map { it[0].toLong() to it[1].toLong() }
            .sortedBy { it.first }

        var count = 1
        var prevDx = points[1].first - points[0].first
        var prevDy = points[1].second - points[0].second
        val g0 = gcd(prevDx, prevDy)
        prevDx /= g0
        prevDy /= g0

        for (i in 2 until n) {
            var dx = points[i].first - points[i - 1].first
            var dy = points[i].second - points[i - 1].second
            val g = gcd(dx, dy)
            dx /= g
            dy /= g
            if (dx != prevDx || dy != prevDy) {
                count++
                prevDx = dx
                prevDy = dy
            }
        }
        return count
    }

    private fun gcd(a: Long, b: Long): Long {
        var x = kotlin.math.abs(a)
        var y = kotlin.math.abs(b)
        while (y != 0L) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return if (x == 0L) 1L else x
    }
}
```

## Dart

```dart
class Solution {
  int minimumLines(List<List<int>> stockPrices) {
    if (stockPrices.length <= 2) return stockPrices.length - 1;
    stockPrices.sort((a, b) => a[0].compareTo(b[0]));
    int count = 1;
    int prevDx = stockPrices[1][0] - stockPrices[0][0];
    int prevDy = stockPrices[1][1] - stockPrices[0][1];
    for (int i = 2; i < stockPrices.length; i++) {
      int curDx = stockPrices[i][0] - stockPrices[i - 1][0];
      int curDy = stockPrices[i][1] - stockPrices[i - 1][1];
      if (prevDy * curDx != prevDx * curDy) {
        count++;
        prevDx = curDx;
        prevDy = curDy;
      }
    }
    return count;
  }
}
```

## Golang

```go
func minimumLines(stockPrices [][]int) int {
    n := len(stockPrices)
    if n <= 2 {
        return n - 1
    }
    sort.Slice(stockPrices, func(i, j int) bool {
        return stockPrices[i][0] < stockPrices[j][0]
    })
    lines := 1
    for i := 2; i < n; i++ {
        x1, y1 := stockPrices[i-2][0], stockPrices[i-2][1]
        x2, y2 := stockPrices[i-1][0], stockPrices[i-1][1]
        x3, y3 := stockPrices[i][0], stockPrices[i][1]
        if int64(y2-y1)*int64(x3-x2) != int64(y3-y2)*int64(x2-x1) {
            lines++
        }
    }
    return lines
}
```

## Ruby

```ruby
def minimum_lines(stock_prices)
  n = stock_prices.length
  return 0 if n <= 1
  stock_prices.sort_by! { |p| p[0] }

  lines = 1
  x1, y1 = stock_prices[0]
  x2, y2 = stock_prices[1]
  dx_prev = x2 - x1
  dy_prev = y2 - y1

  (2...n).each do |i|
    x3, y3 = stock_prices[i]
    dx_curr = x3 - x2
    dy_curr = y3 - y2

    if dy_prev * dx_curr != dy_curr * dx_prev
      lines += 1
      dx_prev = dx_curr
      dy_prev = dy_curr
    end

    x2, y2 = x3, y3
  end

  lines
end
```

## Scala

```scala
object Solution {
    def minimumLines(stockPrices: Array[Array[Int]]): Int = {
        val n = stockPrices.length
        if (n <= 2) return n - 1

        val sorted = stockPrices.sortBy(arr => arr(0))
        var lines = 1
        var i = 2
        while (i < n) {
            val x1 = sorted(i - 2)(0).toLong
            val y1 = sorted(i - 2)(1).toLong
            val x2 = sorted(i - 1)(0).toLong
            val y2 = sorted(i - 1)(1).toLong
            val x3 = sorted(i)(0).toLong
            val y3 = sorted(i)(1).toLong

            if ((y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)) {
                lines += 1
            }
            i += 1
        }
        lines
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_lines(stock_prices: Vec<Vec<i32>>) -> i32 {
        let n = stock_prices.len();
        if n <= 1 {
            return 0;
        }
        // Convert to (day, price) as i64 and sort by day
        let mut points: Vec<(i64, i64)> = stock_prices
            .into_iter()
            .map(|v| (v[0] as i64, v[1] as i64))
            .collect();
        points.sort_by_key(|p| p.0);

        // Greatest common divisor for normalization
        fn gcd(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                let r = a % b;
                a = b;
                b = r;
            }
            a.abs()
        }

        // Initial slope between first two points
        let (x0, y0) = points[0];
        let (x1, y1) = points[1];
        let mut dx = x1 - x0;
        let mut dy = y1 - y0;
        let g = gcd(dy.abs(), dx);
        let mut prev = (dy / g, dx / g); // dx > 0 after sorting

        let mut count: i32 = 1;
        for i in 2..n {
            let (xp, yp) = points[i - 1];
            let (xc, yc) = points[i];
            let dx = xc - xp;
            let dy = yc - yp;
            let g = gcd(dy.abs(), dx);
            let cur = (dy / g, dx / g);
            if cur != prev {
                count += 1;
                prev = cur;
            }
        }

        count
    }
}
```

## Racket

```racket
(define/contract (minimum-lines stockPrices)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((sorted (sort stockPrices
                       (lambda (a b) (< (first a) (first b)))))
         (n (length sorted)))
    (if (<= n 2)
        1
        (let loop ((i 2) (lines 1))
          (if (= i n)
              lines
              (let* ((p0 (list-ref sorted (- i 2)))
                     (p1 (list-ref sorted (- i 1)))
                     (p2 (list-ref sorted i))
                     (x0 (first p0)) (y0 (second p0))
                     (x1 (first p1)) (y1 (second p1))
                     (x2 (first p2)) (y2 (second p2))
                     (left (* (- y1 y0) (- x2 x1)))
                     (right (* (- y2 y1) (- x1 x0))))
                (if (= left right)
                    (loop (+ i 1) lines)
                    (loop (+ i 1) (+ lines 1)))))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_lines/1]).

-spec minimum_lines(StockPrices :: [[integer()]]) -> integer().
minimum_lines(StockPrices) ->
    Points = [{D, P} || [D, P] <- StockPrices],
    Sorted = lists:keysort(1, Points),
    case Sorted of
        [] -> 0;
        [_] -> 0;
        [First | Rest] ->
            count_lines(none, First, Rest, 0)
    end.

count_lines(_PrevSlope, _PrevPoint, [], Count) ->
    Count;
count_lines(PrevSlope, {D1, P1}, [{D2, P2} | Rest], Count) ->
    Dy = P2 - P1,
    Dx = D2 - D1,
    G = gcd(abs(Dy), Dx),
    Slope = {Dy div G, Dx div G},
    case PrevSlope of
        none ->
            count_lines(Slope, {D2, P2}, Rest, Count + 1);
        _ when Slope =:= PrevSlope ->
            count_lines(PrevSlope, {D2, P2}, Rest, Count);
        _ ->
            count_lines(Slope, {D2, P2}, Rest, Count + 1)
    end.

gcd(A, 0) -> abs(A);
gcd(A, B) -> gcd(B, A rem B).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_lines(stock_prices :: [[integer]]) :: integer
  def minimum_lines(stock_prices) do
    points = Enum.sort_by(stock_prices, fn [day, _price] -> day end)
    n = length(points)

    cond do
      n <= 2 ->
        if n == 1, do: 0, else: 1

      true ->
        slopes =
          points
          |> Enum.chunk_every(2, 1, [])
          |> Enum.map(fn [[x1, y1], [x2, y2]] -> reduce_slope(y2 - y1, x2 - x1) end)

        {lines, _} =
          Enum.reduce(slopes, {1, hd(slopes)}, fn slope, {cnt, prev} ->
            if slope == prev do
              {cnt, prev}
            else
              {cnt + 1, slope}
            end
          end)

        lines
    end
  end

  defp reduce_slope(dy, dx) do
    g = Integer.gcd(dy, dx)
    dy = div(dy, g)
    dx = div(dx, g)

    if dx < 0 do
      {-dy, -dx}
    else
      {dy, dx}
    end
  end
end
```

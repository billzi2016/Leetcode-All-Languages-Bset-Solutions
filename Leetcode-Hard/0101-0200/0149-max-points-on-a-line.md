# 0149. Max Points on a Line

## Cpp

```cpp
class Solution {
public:
    struct PairHash {
        size_t operator()(const std::pair<int,int>& p) const noexcept {
            return (static_cast<uint64_t>(p.first) << 32) ^ static_cast<uint64_t>(p.second);
        }
    };
    
    int maxPoints(std::vector<std::vector<int>>& points) {
        int n = points.size();
        if (n <= 2) return n;
        int result = 0;
        for (int i = 0; i < n; ++i) {
            std::unordered_map<std::pair<int,int>, int, PairHash> cnt;
            int duplicates = 1;
            int curMax = 0;
            for (int j = i + 1; j < n; ++j) {
                long long dx = static_cast<long long>(points[j][0]) - points[i][0];
                long long dy = static_cast<long long>(points[j][1]) - points[i][1];
                if (dx == 0 && dy == 0) {
                    ++duplicates;
                } else {
                    long long g = std::gcd(dx, dy);
                    dx /= g;
                    dy /= g;
                    if (dx < 0) {
                        dx = -dx;
                        dy = -dy;
                    } else if (dx == 0) { // vertical line
                        dy = 1;
                    }
                    std::pair<int,int> slope{static_cast<int>(dx), static_cast<int>(dy)};
                    ++cnt[slope];
                    curMax = std::max(curMax, cnt[slope]);
                }
            }
            result = std::max(result, curMax + duplicates);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int maxPoints(int[][] points) {
        int n = points.length;
        if (n <= 2) return n;
        int result = 0;
        for (int i = 0; i < n; i++) {
            java.util.Map<String, Integer> map = new java.util.HashMap<>();
            int duplicates = 0;
            int localMax = 0;
            int[] base = points[i];
            for (int j = i + 1; j < n; j++) {
                int dx = points[j][0] - base[0];
                int dy = points[j][1] - base[1];
                if (dx == 0 && dy == 0) {
                    duplicates++;
                } else {
                    int g = gcd(dx, dy);
                    dx /= g;
                    dy /= g;
                    if (dx < 0) {
                        dx = -dx;
                        dy = -dy;
                    } else if (dx == 0) { // vertical line
                        dy = 1;
                    }
                    String key = dx + "/" + dy;
                    int cnt = map.getOrDefault(key, 0) + 1;
                    map.put(key, cnt);
                    localMax = Math.max(localMax, cnt);
                }
            }
            result = Math.max(result, localMax + duplicates + 1);
        }
        return result;
    }

    private int gcd(int a, int b) {
        if (a == 0) return Math.abs(b);
        if (b == 0) return Math.abs(a);
        a = Math.abs(a);
        b = Math.abs(b);
        while (b != 0) {
            int tmp = a % b;
            a = b;
            b = tmp;
        }
        return a;
    }
}
```

## Python

```python
import math

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n <= 2:
            return n
        result = 0
        for i in range(n):
            slopes = {}
            same = 1
            xi, yi = points[i]
            cur_max = 0
            for j in range(i + 1, n):
                xj, yj = points[j]
                dx = xj - xi
                dy = yj - yi
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                g = math.gcd(dx, dy)
                dx //= g
                dy //= g
                # Normalize direction
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                key = (dx, dy)
                slopes[key] = slopes.get(key, 0) + 1
                cur_max = max(cur_max, slopes[key])
            result = max(result, cur_max + same)
        return result
```

## Python3

```python
from typing import List
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        result = 0
        for i in range(n):
            slopes = {}
            duplicates = 0
            xi, yi = points[i]
            local_max = 0
            for j in range(i + 1, n):
                xj, yj = points[j]
                dx = xj - xi
                dy = yj - yi
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue
                g = math.gcd(dx, dy)
                dx //= g
                dy //= g
                # Normalize direction to have a unique representation
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0 and dy < 0:
                    dy = -dy
                key = (dx, dy)
                slopes[key] = slopes.get(key, 0) + 1
                local_max = max(local_max, slopes[key])
            result = max(result, local_max + duplicates + 1)
        return result
```

## C

```c
#include <stdlib.h>

struct Slope {
    int dx;
    int dy;
};

static int gcd(int a, int b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

static int cmpSlope(const void *a, const void *b) {
    const struct Slope *s1 = (const struct Slope *)a;
    const struct Slope *s2 = (const struct Slope *)b;
    if (s1->dx != s2->dx)
        return s1->dx - s2->dx;
    return s1->dy - s2->dy;
}

int maxPoints(int** points, int pointsSize, int* pointsColSize) {
    if (pointsSize <= 2) return pointsSize;

    int result = 0;
    struct Slope slopes[300]; // maximum possible per iteration

    for (int i = 0; i < pointsSize; ++i) {
        int m = 0;
        for (int j = i + 1; j < pointsSize; ++j) {
            int dx = points[j][0] - points[i][0];
            int dy = points[j][1] - points[i][1];

            if (dx == 0) {               // vertical line
                dy = 1;
            } else if (dy == 0) {        // horizontal line
                dx = 1; dy = 0;
            } else {
                int g = gcd(dx, dy);
                dx /= g;
                dy /= g;
                if (dx < 0) {            // normalize sign
                    dx = -dx;
                    dy = -dy;
                }
            }

            slopes[m].dx = dx;
            slopes[m].dy = dy;
            ++m;
        }

        if (m == 0) {
            if (result < 1) result = 1;
            continue;
        }

        qsort(slopes, m, sizeof(struct Slope), cmpSlope);

        int localMax = 1, cur = 1;
        for (int k = 1; k < m; ++k) {
            if (slopes[k].dx == slopes[k - 1].dx && slopes[k].dy == slopes[k - 1].dy) {
                ++cur;
            } else {
                if (cur > localMax) localMax = cur;
                cur = 1;
            }
        }
        if (cur > localMax) localMax = cur;

        if (localMax + 1 > result) result = localMax + 1; // include point i
    }

    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxPoints(int[][] points) {
        int n = points.Length;
        if (n <= 2) return n;
        int result = 0;
        for (int i = 0; i < n; i++) {
            var slopes = new Dictionary<(int, int), int>();
            int duplicates = 0;
            int localMax = 0;
            int xi = points[i][0];
            int yi = points[i][1];
            for (int j = i + 1; j < n; j++) {
                int xj = points[j][0];
                int yj = points[j][1];
                int dx = xj - xi;
                int dy = yj - yi;
                if (dx == 0 && dy == 0) {
                    duplicates++;
                    continue;
                }
                int g = Gcd(Math.Abs(dx), Math.Abs(dy));
                if (g != 0) {
                    dx /= g;
                    dy /= g;
                }
                // Normalize sign: keep dx positive; if dx==0, make dy positive
                if (dx < 0) {
                    dx = -dx;
                    dy = -dy;
                } else if (dx == 0 && dy < 0) {
                    dy = -dy;
                }
                var key = (dx, dy);
                if (!slopes.ContainsKey(key)) slopes[key] = 0;
                slopes[key]++;
                localMax = Math.Max(localMax, slopes[key]);
            }
            result = Math.Max(result, localMax + duplicates + 1);
        }
        return result;
    }

    private int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var maxPoints = function(points) {
    const n = points.length;
    if (n <= 2) return n;

    const gcd = (a, b) => {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    let result = 0;

    for (let i = 0; i < n; i++) {
        const slopes = new Map();
        let duplicates = 1; // count the point itself
        let localMax = 0;

        for (let j = i + 1; j < n; j++) {
            let dx = points[j][0] - points[i][0];
            let dy = points[j][1] - points[i][1];

            if (dx === 0 && dy === 0) {
                duplicates++;
                continue;
            }

            const g = gcd(dx, dy);
            dx /= g;
            dy /= g;

            // Normalize sign: make dx positive; if dx == 0 keep dy positive
            if (dx < 0) {
                dx = -dx;
                dy = -dy;
            } else if (dx === 0) {
                dy = 1; // vertical line representation
            }

            const key = `${dy}/${dx}`;
            const cnt = (slopes.get(key) || 0) + 1;
            slopes.set(key, cnt);
            localMax = Math.max(localMax, cnt);
        }

        result = Math.max(result, localMax + duplicates);
    }

    return result;
};
```

## Typescript

```typescript
function maxPoints(points: number[][]): number {
    const n = points.length;
    if (n <= 2) return n;

    const gcd = (a: number, b: number): number => {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    let result = 0;

    for (let i = 0; i < n; i++) {
        const slopes = new Map<string, number>();
        let same = 1; // count of points identical to points[i] (including itself)
        let localMax = 0;
        const [x1, y1] = points[i];

        for (let j = i + 1; j < n; j++) {
            const [x2, y2] = points[j];
            let dx = x2 - x1;
            let dy = y2 - y1;

            if (dx === 0 && dy === 0) {
                same++;
                continue;
            }

            const g = gcd(dx, dy);
            dx /= g;
            dy /= g;

            // Normalize sign: keep denominator positive
            if (dx < 0) {
                dx = -dx;
                dy = -dy;
            } else if (dx === 0) { // vertical line, unify representation
                dy = 1;
            }

            const key = `${dy}/${dx}`;
            const cnt = (slopes.get(key) ?? 0) + 1;
            slopes.set(key, cnt);
            localMax = Math.max(localMax, cnt);
        }

        result = Math.max(result, localMax + same);
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function maxPoints($points) {
        $n = count($points);
        if ($n <= 2) return $n;

        $globalMax = 0;
        for ($i = 0; $i < $n; $i++) {
            $slopes = [];
            $duplicates = 1; // count the point itself
            $localMax = 0;
            for ($j = $i + 1; $j < $n; $j++) {
                $dx = $points[$j][0] - $points[$i][0];
                $dy = $points[$j][1] - $points[$i][1];

                if ($dx == 0 && $dy == 0) {
                    $duplicates++;
                    continue;
                }

                if ($dx == 0) {
                    $key = 'v'; // vertical line
                } elseif ($dy == 0) {
                    $key = 'h'; // horizontal line
                } else {
                    $g = $this->gcd(abs($dx), abs($dy));
                    $dx /= $g;
                    $dy /= $g;

                    // normalize sign: keep dx positive
                    if ($dx < 0) {
                        $dx = -$dx;
                        $dy = -$dy;
                    }

                    $key = $dy . '/' . $dx;
                }

                if (!isset($slopes[$key])) {
                    $slopes[$key] = 1;
                } else {
                    $slopes[$key]++;
                }
                $localMax = max($localMax, $slopes[$key]);
            }
            $globalMax = max($globalMax, $localMax + $duplicates);
        }

        return $globalMax;
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
    func maxPoints(_ points: [[Int]]) -> Int {
        let n = points.count
        if n <= 2 { return n }
        
        func gcd(_ a: Int, _ b: Int) -> Int {
            var x = abs(a)
            var y = abs(b)
            while y != 0 {
                let temp = x % y
                x = y
                y = temp
            }
            return x
        }
        
        struct Slope: Hashable {
            let dy: Int
            let dx: Int
        }
        
        var result = 0
        
        for i in 0..<n {
            var map = [Slope: Int]()
            var same = 0
            var localMax = 0
            let xi = points[i][0]
            let yi = points[i][1]
            
            for j in 0..<n where j != i {
                let xj = points[j][0]
                let yj = points[j][1]
                
                if xj == xi && yj == yi {
                    same += 1
                } else {
                    var dy = yj - yi
                    var dx = xj - xi
                    let g = gcd(dy, dx)
                    dy /= g
                    dx /= g
                    if dx < 0 {
                        dx = -dx
                        dy = -dy
                    } else if dx == 0 {
                        dy = 1
                    }
                    let slope = Slope(dy: dy, dx: dx)
                    map[slope, default: 0] += 1
                    localMax = max(localMax, map[slope]!)
                }
            }
            result = max(result, localMax + same + 1)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxPoints(points: Array<IntArray>): Int {
        val n = points.size
        if (n <= 2) return n
        var result = 0
        for (i in 0 until n) {
            val map = HashMap<Pair<Int, Int>, Int>()
            var localMax = 0
            var duplicate = 0
            for (j in i + 1 until n) {
                var dx = points[j][0] - points[i][0]
                var dy = points[j][1] - points[i][1]
                if (dx == 0 && dy == 0) {
                    duplicate++
                    continue
                }
                val g = gcd(dx, dy)
                dx /= g
                dy /= g
                if (dx < 0) {
                    dx = -dx
                    dy = -dy
                } else if (dx == 0 && dy < 0) {
                    dy = -dy
                }
                val key = Pair(dx, dy)
                map[key] = map.getOrDefault(key, 0) + 1
                localMax = maxOf(localMax, map[key]!!)
            }
            result = maxOf(result, localMax + duplicate + 1)
        }
        return result
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = kotlin.math.abs(a)
        var y = kotlin.math.abs(b)
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return if (x == 0) 1 else x
    }
}
```

## Dart

```dart
class Solution {
  int maxPoints(List<List<int>> points) {
    int n = points.length;
    if (n <= 2) return n;

    int globalMax = 0;

    int gcd(int a, int b) {
      a = a.abs();
      b = b.abs();
      while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
      }
      return a;
    }

    for (int i = 0; i < n; ++i) {
      Map<String, int> slopeCount = {};
      int samePoint = 0;
      int localMax = 0;

      for (int j = i + 1; j < n; ++j) {
        int dx = points[j][0] - points[i][0];
        int dy = points[j][1] - points[i][1];

        if (dx == 0 && dy == 0) {
          samePoint++;
          continue;
        }

        if (dx == 0) {
          // vertical line
          dy = 1;
        } else if (dy == 0) {
          // horizontal line
          dx = 1;
        } else {
          int g = gcd(dx, dy);
          dx ~/= g;
          dy ~/= g;
          // keep denominator positive
          if (dx < 0) {
            dx = -dx;
            dy = -dy;
          }
        }

        String key = '$dy/$dx';
        slopeCount[key] = (slopeCount[key] ?? 0) + 1;
        localMax = localMax > slopeCount[key]! ? localMax : slopeCount[key]!;
      }

      globalMax = globalMax > (localMax + samePoint + 1)
          ? globalMax
          : (localMax + samePoint + 1);
    }

    return globalMax;
  }
}
```

## Golang

```go
func maxPoints(points [][]int) int {
    n := len(points)
    if n <= 2 {
        return n
    }
    ans := 0
    for i := 0; i < n; i++ {
        slopes := make(map[[2]int]int)
        duplicates := 1
        localMax := 0
        xi, yi := points[i][0], points[i][1]
        for j := i + 1; j < n; j++ {
            xj, yj := points[j][0], points[j][1]
            dx := xj - xi
            dy := yj - yi
            if dx == 0 && dy == 0 {
                duplicates++
                continue
            }
            g := gcd(abs(dx), abs(dy))
            if g != 0 {
                dx /= g
                dy /= g
            }
            if dx < 0 {
                dx = -dx
                dy = -dy
            } else if dx == 0 {
                dy = 1
            } else if dy == 0 {
                dx = 1
            }
            key := [2]int{dx, dy}
            slopes[key]++
            if slopes[key] > localMax {
                localMax = slopes[key]
            }
        }
        if localMax+duplicates > ans {
            ans = localMax + duplicates
        }
    }
    return ans
}

func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    if a < 0 {
        return -a
    }
    return a
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
def max_points(points)
  n = points.length
  return n if n <= 2

  result = 0
  (0...n).each do |i|
    slopes = Hash.new(0)
    duplicate = 0
    xi, yi = points[i]

    ((i + 1)...n).each do |j|
      xj, yj = points[j]
      dx = xj - xi
      dy = yj - yi

      if dx == 0 && dy == 0
        duplicate += 1
        next
      end

      g = dx.gcd(dy)
      ndx = dx / g
      ndy = dy / g

      if ndx < 0
        ndx = -ndx
        ndy = -ndy
      elsif ndx == 0 && ndy < 0
        ndy = -ndy
      end

      slopes[[ndx, ndy]] += 1
    end

    local_max = slopes.values.max || 0
    result = [result, local_max + duplicate + 1].max
  end

  result
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable

    def maxPoints(points: Array[Array[Int]]): Int = {
        val n = points.length
        if (n <= 2) return n

        def gcd(a: Int, b: Int): Int = {
            var x = math.abs(a)
            var y = math.abs(b)
            while (y != 0) {
                val tmp = x % y
                x = y
                y = tmp
            }
            x
        }

        var result = 0

        for (i <- 0 until n) {
            val slopes = mutable.Map[(Int, Int), Int]().withDefaultValue(0)
            var same = 0
            var localMax = 0

            val xi = points(i)(0)
            val yi = points(i)(1)

            for (j <- i + 1 until n) {
                val xj = points(j)(0)
                val yj = points(j)(1)
                var dx = xj - xi
                var dy = yj - yi

                if (dx == 0 && dy == 0) {
                    same += 1
                } else {
                    if (dx == 0) {
                        // vertical line
                        dy = 1
                        dx = 0
                    } else if (dy == 0) {
                        // horizontal line
                        dy = 0
                        dx = 1
                    } else {
                        val g = gcd(dy, dx)
                        dy /= g
                        dx /= g
                        // normalize sign: make dx positive
                        if (dx < 0) {
                            dx = -dx
                            dy = -dy
                        }
                    }
                    val key = (dy, dx)
                    slopes(key) += 1
                    localMax = math.max(localMax, slopes(key))
                }
            }

            // points on a line through i: localMax + same duplicates + the point itself
            result = math.max(result, localMax + same + 1)
        }

        result
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn max_points(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        if n <= 2 {
            return n as i32;
        }
        let pts: Vec<(i64, i64)> = points
            .iter()
            .map(|p| (p[0] as i64, p[1] as i64))
            .collect();

        fn gcd(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                let r = a % b;
                a = b;
                b = r;
            }
            a.abs()
        }

        let mut result = 0i32;

        for i in 0..n {
            let (xi, yi) = pts[i];
            let mut map: HashMap<(i64, i64), i32> = HashMap::new();
            let mut same = 1i32; // count of points identical to i (including itself)
            let mut local_max = 0i32;

            for j in (i + 1)..n {
                let (xj, yj) = pts[j];
                if xi == xj && yi == yj {
                    same += 1;
                    continue;
                }
                let dy = yj - yi;
                let dx = xj - xi;

                let key = if dx == 0 {
                    // vertical line
                    (1i64, 0i64)
                } else if dy == 0 {
                    // horizontal line
                    (0i64, 1i64)
                } else {
                    let g = gcd(dy, dx);
                    let mut ndy = dy / g;
                    let mut ndx = dx / g;
                    // normalize sign: make denominator positive
                    if ndx < 0 {
                        ndx = -ndx;
                        ndy = -ndy;
                    }
                    (ndy, ndx)
                };

                let cnt = map.entry(key).or_insert(0);
                *cnt += 1;
                if *cnt > local_max {
                    local_max = *cnt;
                }
            }

            // points on a line through i: local_max points sharing same slope + duplicates (same)
            let current = local_max + same;
            if current > result {
                result = current;
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (max-points points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((pts (list->vector points))
         (n (vector-length pts)))
    (if (<= n 2)
        n
        (let ((global-max 0))
          (for ([i (in-range n)])
            (define xi (first (vector-ref pts i)))
            (define yi (second (vector-ref pts i)))
            (define ht (make-hash))
            (define local-max 0)
            (for ([j (in-range (+ i 1) n)])
              (define xj (first (vector-ref pts j)))
              (define yj (second (vector-ref pts j)))
              (define dx (- xj xi))
              (define dy (- yj yi))
              (define key
                (if (zero? dx)
                    'vertical
                    (let* ((g (gcd (abs dx) (abs dy)))
                           (dxr (/ dx g))
                           (dyr (/ dy g)))
                      (when (< dxr 0)
                        (set! dxr (- dxr))
                        (set! dyr (- dyr)))
                      (cons dyr dxr))))
              (define cnt (+ 1 (hash-ref ht key 0)))
              (hash-set! ht key cnt)
              (when (> cnt local-max) (set! local-max cnt)))
            (when (> (+ local-max 1) global-max)
              (set! global-max (+ local-max 1)))))
          global-max))))
```

## Erlang

```erlang
-module(solution).
-export([max_points/1]).

-spec max_points(Points :: [[integer()]]) -> integer().
max_points(Points) ->
    case length(Points) of
        L when L =< 2 -> L;
        _ ->
            Tuple = list_to_tuple(Points),
            N = tuple_size(Tuple),
            max_points_loop(1, N, Tuple, 0)
    end.

max_points_loop(I, N, Tuple, GlobalMax) when I > N ->
    GlobalMax;
max_points_loop(I, N, Tuple, GlobalMax) ->
    {Xi, Yi} = element(I, Tuple),
    MaxForI = inner_loop(I + 1, N, Tuple, Xi, Yi, maps:new(), 0),
    NewGlobal = max(GlobalMax, MaxForI + 1),
    max_points_loop(I + 1, N, Tuple, NewGlobal).

inner_loop(J, N, _Tuple, _Xi, _Yi, _Map, LocalMax) when J > N ->
    LocalMax;
inner_loop(J, N, Tuple, Xi, Yi, Map, LocalMax) ->
    {Xj, Yj} = element(J, Tuple),
    Dx = Xj - Xi,
    Dy = Yj - Yi,
    Key = slope_key(Dx, Dy),
    Count = maps:get(Key, Map, 0) + 1,
    NewMap = maps:put(Key, Count, Map),
    NewLocalMax = max(LocalMax, Count),
    inner_loop(J + 1, N, Tuple, Xi, Yi, NewMap, NewLocalMax).

slope_key(0, _Dy) ->
    {1, 0}; % vertical line
slope_key(_Dx, 0) ->
    {0, 1}; % horizontal line
slope_key(Dx, Dy) ->
    G = gcd(abs(Dx), abs(Dy)),
    Dx1 = Dx div G,
    Dy1 = Dy div G,
    case Dx1 < 0 of
        true -> {-Dy1, -Dx1};
        false -> {Dy1, Dx1}
    end.

gcd(A, 0) ->
    A;
gcd(A, B) ->
    gcd(B, A rem B).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_points(points :: [[integer]]) :: integer
  def max_points(points) do
    n = length(points)

    if n <= 2 do
      n
    else
      compute_max(points, n)
    end
  end

  defp compute_max(points, n) do
    Enum.reduce(0..(n - 1), 0, fn i, global_max ->
      {dup, slope_map} =
        Enum.reduce((i + 1)..(n - 1), {1, %{}}, fn j, {dup_acc, map_acc} ->
          [xi, yi] = Enum.at(points, i)
          [xj, yj] = Enum.at(points, j)

          dx = xj - xi
          dy = yj - yi

          if dx == 0 and dy == 0 do
            {dup_acc + 1, map_acc}
          else
            key = normalize(dx, dy)
            new_map = Map.update(map_acc, key, 1, &(&1 + 1))
            {dup_acc, new_map}
          end
        end)

      local_max =
        if map_size(slope_map) == 0 do
          dup
        else
          max_on_line = slope_map |> Map.values() |> Enum.max()
          dup + max_on_line
        end

      if local_max > global_max, do: local_max, else: global_max
    end)
  end

  defp normalize(dx, dy) do
    g = gcd(abs(dx), abs(dy))
    ndx = div(dx, g)
    ndy = div(dy, g)

    cond do
      ndx < 0 -> {-ndy, -ndx}
      ndx == 0 -> {1, 0}
      true -> {ndy, ndx}
    end
  end

  defp gcd(0, b), do: b
  defp gcd(a, 0), do: a
  defp gcd(a, b) do
    if b == 0, do: a, else: gcd(b, rem(a, b))
  end
end
```

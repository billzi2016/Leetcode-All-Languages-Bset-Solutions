# 1610. Maximum Number of Visible Points

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int visiblePoints(vector<vector<int>>& points, int angle, vector<int>& location) {
        const double PI = acos(-1.0);
        int same = 0;
        vector<double> angs;
        for (const auto& p : points) {
            long long dx = (long long)p[0] - location[0];
            long long dy = (long long)p[1] - location[1];
            if (dx == 0 && dy == 0) {
                ++same;
            } else {
                double a = atan2((double)dy, (double)dx) * 180.0 / PI;
                if (a < 0) a += 360.0;
                angs.push_back(a);
            }
        }
        int n = angs.size();
        if (n == 0) return same;
        sort(angs.begin(), angs.end());
        vector<double> all;
        all.reserve(2 * n);
        for (double a : angs) all.push_back(a);
        for (double a : angs) all.push_back(a + 360.0);
        int maxCnt = 0, j = 0;
        double limit = angle + 1e-9; // inclusive tolerance
        for (int i = 0; i < n; ++i) {
            while (j < i + n && all[j] - all[i] <= limit) ++j;
            maxCnt = max(maxCnt, j - i);
        }
        return same + maxCnt;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int visiblePoints(List<List<Integer>> points, int angle, List<Integer> location) {
        int sameLocation = 0;
        List<Double> angles = new ArrayList<>();
        int locX = location.get(0);
        int locY = location.get(1);
        for (List<Integer> p : points) {
            int x = p.get(0);
            int y = p.get(1);
            int dx = x - locX;
            int dy = y - locY;
            if (dx == 0 && dy == 0) {
                sameLocation++;
            } else {
                double a = Math.toDegrees(Math.atan2(dy, dx));
                if (a < 0) a += 360.0;
                angles.add(a);
            }
        }
        int n = angles.size();
        if (n == 0) return sameLocation;

        Collections.sort(angles);
        double[] ext = new double[2 * n];
        for (int i = 0; i < n; i++) {
            ext[i] = angles.get(i);
            ext[i + n] = ext[i] + 360.0;
        }

        int maxVisible = 0;
        int j = 0;
        double view = angle + 1e-9; // inclusive tolerance
        for (int i = 0; i < n; i++) {
            while (j < i + n && ext[j] - ext[i] <= view) {
                j++;
            }
            maxVisible = Math.max(maxVisible, j - i);
        }

        return maxVisible + sameLocation;
    }
}
```

## Python

```python
class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        import math
        same = 0
        angles = []
        lx, ly = location
        for x, y in points:
            dx = x - lx
            dy = y - ly
            if dx == 0 and dy == 0:
                same += 1
            else:
                a = math.degrees(math.atan2(dy, dx))
                if a < 0:
                    a += 360.0
                angles.append(a)
        if not angles:
            return same
        angles.sort()
        # duplicate with +360 to handle circular wrap
        ext = angles + [a + 360.0 for a in angles]
        max_cnt = 0
        j = 0
        n = len(angles)
        limit = float(angle) + 1e-9  # inclusive tolerance
        for i in range(n):
            while j < i + n and ext[j] - angles[i] <= limit:
                j += 1
            max_cnt = max(max_cnt, j - i)
        return max_cnt + same
```

## Python3

```python
import math
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        same = 0
        angles = []
        lx, ly = location
        for x, y in points:
            if x == lx and y == ly:
                same += 1
            else:
                a = math.degrees(math.atan2(y - ly, x - lx))
                if a < 0:
                    a += 360.0
                angles.append(a)
        if not angles:
            return same
        angles.sort()
        extended = angles + [a + 360.0 for a in angles]
        max_cnt = 0
        j = 0
        eps = 1e-9
        n = len(angles)
        for i in range(n):
            while j < i + n and extended[j] - extended[i] <= angle + eps:
                j += 1
            max_cnt = max(max_cnt, j - i)
        return same + max_cnt
```

## C

```c
#include <math.h>
#include <stdlib.h>

static int cmp_double(const void *a, const void *b) {
    double da = *(const double *)a;
    double db = *(const double *)b;
    if (da < db) return -1;
    if (da > db) return 1;
    return 0;
}

int visiblePoints(int** points, int pointsSize, int* pointsColSize, int angle, int* location, int locationSize) {
    int base = 0;
    int n = 0;
    double *angles = (double *)malloc(sizeof(double) * pointsSize);
    if (!angles) return 0; // safety
    
    for (int i = 0; i < pointsSize; ++i) {
        int x = points[i][0];
        int y = points[i][1];
        if (x == location[0] && y == location[1]) {
            base++;
        } else {
            double rad = atan2((double)(y - location[1]), (double)(x - location[0]));
            double deg = rad * 180.0 / M_PI;
            if (deg < 0) deg += 360.0;
            angles[n++] = deg;
        }
    }
    
    if (n == 0) {
        free(angles);
        return base;
    }
    
    qsort(angles, n, sizeof(double), cmp_double);
    
    double *ext = (double *)malloc(sizeof(double) * (2 * n));
    for (int i = 0; i < n; ++i) {
        ext[i] = angles[i];
        ext[i + n] = angles[i] + 360.0;
    }
    free(angles);
    
    int maxCnt = 0;
    int j = 0;
    double limit = (double)angle + 1e-9; // epsilon for inclusivity
    for (int i = 0; i < n; ++i) {
        if (j < i) j = i;
        while (j < i + n && ext[j] - ext[i] <= limit) {
            ++j;
        }
        int cnt = j - i;
        if (cnt > maxCnt) maxCnt = cnt;
    }
    
    free(ext);
    return base + maxCnt;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int VisiblePoints(IList<IList<int>> points, int angle, IList<int> location) {
        int sameLocation = 0;
        List<double> angles = new List<double>();
        double locX = location[0];
        double locY = location[1];

        foreach (var p in points) {
            double x = p[0], y = p[1];
            if (x == locX && y == locY) {
                sameLocation++;
                continue;
            }
            double rad = Math.Atan2(y - locY, x - locX);
            double deg = rad * 180.0 / Math.PI;
            if (deg < 0) deg += 360.0;
            angles.Add(deg);
        }

        int n = angles.Count;
        if (n == 0) return sameLocation;

        angles.Sort();
        // duplicate with +360
        double[] dup = new double[2 * n];
        for (int i = 0; i < n; i++) {
            dup[i] = angles[i];
            dup[i + n] = angles[i] + 360.0;
        }

        int maxVisible = 0;
        int right = 0;
        double limit = angle + 1e-9; // inclusive tolerance

        for (int left = 0; left < n; left++) {
            while (right < left + n && dup[right] - dup[left] <= limit) {
                right++;
            }
            int count = right - left;
            if (count > maxVisible) maxVisible = count;
        }

        return maxVisible + sameLocation;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @param {number} angle
 * @param {number[]} location
 * @return {number}
 */
var visiblePoints = function(points, angle, location) {
    const [lx, ly] = location;
    let samePosCount = 0;
    const angles = [];
    
    for (const [x, y] of points) {
        if (x === lx && y === ly) {
            samePosCount++;
        } else {
            let deg = Math.atan2(y - ly, x - lx) * 180 / Math.PI;
            if (deg < 0) deg += 360;
            angles.push(deg);
        }
    }
    
    const n = angles.length;
    if (n === 0) return samePosCount;
    
    angles.sort((a, b) => a - b);
    const ext = angles.concat(angles.map(v => v + 360));
    
    let maxInWindow = 0;
    let j = 0;
    const eps = 1e-9;
    
    for (let i = 0; i < n; i++) {
        if (j < i) j = i;
        while (j < i + n && ext[j] - ext[i] <= angle + eps) {
            j++;
        }
        maxInWindow = Math.max(maxInWindow, j - i);
    }
    
    return samePosCount + maxInWindow;
};
```

## Typescript

```typescript
function visiblePoints(points: number[][], angle: number, location: number[]): number {
    const [x0, y0] = location;
    let same = 0;
    const angs: number[] = [];
    for (const p of points) {
        const dx = p[0] - x0;
        const dy = p[1] - y0;
        if (dx === 0 && dy === 0) {
            ++same;
        } else {
            let deg = Math.atan2(dy, dx) * 180 / Math.PI;
            if (deg < 0) deg += 360;
            angs.push(deg);
        }
    }
    const n = angs.length;
    if (n === 0) return same;

    angs.sort((a, b) => a - b);
    const ext: number[] = new Array(2 * n);
    for (let i = 0; i < n; ++i) {
        ext[i] = angs[i];
        ext[i + n] = angs[i] + 360;
    }

    let maxCnt = 0;
    let j = 0;
    const eps = 1e-9;
    for (let i = 0; i < n; ++i) {
        while (j < i + n && ext[j] - ext[i] <= angle + eps) {
            ++j;
        }
        maxCnt = Math.max(maxCnt, j - i);
    }

    return maxCnt + same;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @param Integer $angle
     * @param Integer[] $location
     * @return Integer
     */
    function visiblePoints($points, $angle, $location) {
        $same = 0;
        $angles = [];

        foreach ($points as $p) {
            if ($p[0] == $location[0] && $p[1] == $location[1]) {
                $same++;
                continue;
            }
            $dx = $p[0] - $location[0];
            $dy = $p[1] - $location[1];
            $theta = rad2deg(atan2($dy, $dx));
            if ($theta < 0) {
                $theta += 360.0;
            }
            $angles[] = $theta;
        }

        $n = count($angles);
        if ($n == 0) {
            return $same;
        }

        sort($angles, SORT_NUMERIC);

        $extended = $angles;
        foreach ($angles as $a) {
            $extended[] = $a + 360.0;
        }

        $max = 0;
        $j = 0;
        $eps = 1e-9;

        for ($i = 0; $i < $n; $i++) {
            if ($j < $i) {
                $j = $i;
            }
            while ($j < $i + $n && $extended[$j] - $extended[$i] <= $angle + $eps) {
                $j++;
            }
            $max = max($max, $j - $i);
        }

        return $max + $same;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func visiblePoints(_ points: [[Int]], _ angle: Int, _ location: [Int]) -> Int {
        let locX = location[0]
        let locY = location[1]
        var sameCount = 0
        var angles = [Double]()
        
        for p in points {
            let x = p[0], y = p[1]
            if x == locX && y == locY {
                sameCount += 1
            } else {
                let dy = Double(y - locY)
                let dx = Double(x - locX)
                var a = atan2(dy, dx) * 180.0 / Double.pi
                if a < 0 { a += 360.0 }
                angles.append(a)
            }
        }
        
        if angles.isEmpty {
            return sameCount
        }
        
        angles.sort()
        let m = angles.count
        var extended = angles
        extended.reserveCapacity(m * 2)
        for a in angles {
            extended.append(a + 360.0)
        }
        
        var maxVisible = 0
        var j = 0
        let limitAngle = Double(angle) + 1e-9
        
        for i in 0..<m {
            if j < i { j = i }
            while j < i + m && extended[j] - extended[i] <= limitAngle {
                j += 1
            }
            let cnt = j - i
            if cnt > maxVisible { maxVisible = cnt }
        }
        
        return sameCount + maxVisible
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun visiblePoints(points: List<List<Int>>, angle: Int, location: List<Int>): Int {
        val x0 = location[0]
        val y0 = location[1]
        var sameLocationCount = 0
        val angles = mutableListOf<Double>()
        for (p in points) {
            val x = p[0]
            val y = p[1]
            if (x == x0 && y == y0) {
                sameLocationCount++
            } else {
                val rad = Math.atan2((y - y0).toDouble(), (x - x0).toDouble())
                var deg = Math.toDegrees(rad)
                if (deg < 0) deg += 360.0
                angles.add(deg)
            }
        }
        if (angles.isEmpty()) return sameLocationCount
        angles.sort()
        val n = angles.size
        val extended = DoubleArray(2 * n)
        for (i in 0 until n) {
            extended[i] = angles[i]
            extended[i + n] = angles[i] + 360.0
        }
        var maxVisible = 0
        var j = 0
        val view = angle.toDouble()
        val eps = 1e-9
        for (i in 0 until n) {
            if (j < i) j = i
            while (j < i + n && extended[j] - extended[i] <= view + eps) {
                j++
            }
            maxVisible = kotlin.math.max(maxVisible, j - i)
        }
        return maxVisible + sameLocationCount
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int visiblePoints(List<List<int>> points, int angle, List<int> location) {
    const double eps = 1e-9;
    int sameLocation = 0;
    List<double> angles = [];
    final locX = location[0];
    final locY = location[1];

    for (var p in points) {
      int x = p[0], y = p[1];
      if (x == locX && y == locY) {
        sameLocation++;
      } else {
        double a = atan2(y - locY, x - locX) * 180 / pi;
        if (a < 0) a += 360.0;
        angles.add(a);
      }
    }

    if (angles.isEmpty) return sameLocation;

    angles.sort();
    int n = angles.length;
    List<double> ext = List<double>.filled(n * 2, 0);
    for (int i = 0; i < n; i++) {
      ext[i] = angles[i];
      ext[i + n] = angles[i] + 360.0;
    }

    int maxCnt = 0;
    int j = 0;
    for (int i = 0; i < n; i++) {
      while (j < i + n && ext[j] - ext[i] <= angle + eps) {
        j++;
      }
      int cnt = j - i;
      if (cnt > maxCnt) maxCnt = cnt;
    }

    return sameLocation + maxCnt;
  }
}
```

## Golang

```go
package main

import (
	"math"
	"sort"
)

func visiblePoints(points [][]int, angle int, location []int) int {
	locX, locY := location[0], location[1]
	same := 0
	var angs []float64

	for _, p := range points {
		x, y := p[0], p[1]
		if x == locX && y == locY {
			same++
			continue
		}
		dy := float64(y - locY)
		dx := float64(x - locX)
		rad := math.Atan2(dy, dx) // [-π, π]
		deg := rad * 180.0 / math.Pi
		if deg < 0 {
			deg += 360.0
		}
		angs = append(angs, deg)
	}

	n := len(angs)
	if n == 0 {
		return same
	}
	sort.Float64s(angs)

	// duplicate with +360 to handle circular wrap
	m := make([]float64, 2*n)
	copy(m, angs)
	for i := 0; i < n; i++ {
		m[n+i] = angs[i] + 360.0
	}

	maxCnt := 0
	j := 0
	limit := float64(angle) + 1e-9 // tolerance for floating point

	for i := 0; i < n; i++ {
		if j < i {
			j = i
		}
		for j+1 < i+n && m[j+1]-m[i] <= limit {
			j++
		}
		cnt := j - i + 1
		if cnt > maxCnt {
			maxCnt = cnt
		}
	}

	return maxCnt + same
}
```

## Ruby

```ruby
def visible_points(points, angle, location)
  x0, y0 = location
  same = 0
  angles = []

  points.each do |x, y|
    if x == x0 && y == y0
      same += 1
    else
      rad = Math.atan2(y - y0, x - x0)
      deg = rad * 180.0 / Math::PI
      deg += 360.0 if deg < 0
      angles << deg
    end
  end

  return same if angles.empty?

  angles.sort!
  n = angles.size
  extended = angles + angles.map { |a| a + 360.0 }

  max_visible = 0
  j = 0
  eps = 1e-9

  (0...n).each do |i|
    while j < i + n && extended[j] - extended[i] <= angle + eps
      j += 1
    end
    max_visible = [max_visible, j - i].max
  end

  max_visible + same
end
```

## Scala

```scala
object Solution {
    def visiblePoints(points: List[List[Int]], angle: Int, location: List[Int]): Int = {
        val locX = location(0)
        val locY = location(1)
        var sameLocationCount = 0
        val angles = scala.collection.mutable.ArrayBuffer[Double]()

        for (p <- points) {
            val x = p(0)
            val y = p(1)
            if (x == locX && y == locY) {
                sameLocationCount += 1
            } else {
                val dy = y - locY
                val dx = x - locX
                var deg = Math.toDegrees(Math.atan2(dy, dx))
                if (deg < 0) deg += 360.0
                angles += deg
            }
        }

        if (angles.isEmpty) return sameLocationCount

        val sorted = angles.sorted
        val m = sorted.length
        val ext = new Array[Double](m * 2)
        for (i <- 0 until m) {
            ext(i) = sorted(i)
            ext(i + m) = sorted(i) + 360.0
        }

        var maxVisible = 0
        var j = 0
        val eps = 1e-9
        for (i <- 0 until m) {
            while (j < i + m && ext(j) - ext(i) <= angle.toDouble + eps) {
                j += 1
            }
            val cnt = j - i
            if (cnt > maxVisible) maxVisible = cnt
        }

        sameLocationCount + maxVisible
    }
}
```

## Rust

```rust
impl Solution {
    pub fn visible_points(points: Vec<Vec<i32>>, angle: i32, location: Vec<i32>) -> i32 {
        let (lx, ly) = (location[0] as f64, location[1] as f64);
        let mut same = 0i32;
        let mut angles: Vec<f64> = Vec::new();
        for p in points.iter() {
            let x = p[0] as f64;
            let y = p[1] as f64;
            if (x - lx).abs() < 1e-9 && (y - ly).abs() < 1e-9 {
                same += 1;
            } else {
                let mut a = (y - ly).atan2(x - lx) * 180.0 / std::f64::consts::PI;
                if a < 0.0 {
                    a += 360.0;
                }
                angles.push(a);
            }
        }
        if angles.is_empty() {
            return same;
        }
        angles.sort_by(|a, b| a.partial_cmp(b).unwrap());
        let n = angles.len();
        let mut ext: Vec<f64> = Vec::with_capacity(n * 2);
        for &a in &angles {
            ext.push(a);
        }
        for &a in &angles {
            ext.push(a + 360.0);
        }

        let angle_f = angle as f64;
        let eps = 1e-9;
        let mut max_cnt = 0usize;
        let mut left = 0usize;
        for right in 0..ext.len() {
            while ext[right] - ext[left] > angle_f + eps {
                left += 1;
            }
            if left < n {
                let cnt = right - left + 1;
                if cnt > max_cnt {
                    max_cnt = cnt;
                }
            }
        }

        (max_cnt as i32) + same
    }
}
```

## Racket

```racket
(define/contract (visible-points points angle location)
  (-> (listof (listof exact-integer?)) exact-integer? (listof exact-integer?) exact-integer?)
  (let* ((px (first location))
         (py (second location))
         (same-count
          (for/sum ([pt points])
            (if (and (= (first pt) px) (= (second pt) py)) 1 0)))
         (angles
          (for/list ([pt points]
                     #:when (not (and (= (first pt) px) (= (second pt) py))))
            (let* ((dx (- (first pt) px))
                   (dy (- (second pt) py))
                   (rad (atan dy dx))                ; -π .. π
                   (deg (* 180 (/ rad pi))))        ; convert to degrees
              (if (< deg 0) (+ deg 360) deg)))))
    (if (null? angles)
        same-count
        (let* ((sorted (sort angles <))
               (n (length sorted))
               (sorted-vec (list->vector sorted))
               (ext (make-vector (* 2 n))))
          ;; duplicate with +360 for circular handling
          (for ([i (in-range n)])
            (vector-set! ext i (vector-ref sorted-vec i)))
          (for ([i (in-range n)])
            (vector-set! ext (+ i n) (+ (vector-ref sorted-vec i) 360.0)))
          (let ((max-win 0)
                (j 0))
            (for ([i (in-range n)])
              (when (< j i) (set! j i))
              ;; advance j while the angular difference is within 'angle'
              (let loop ((jj j))
                (if (and (< jj (* 2 n))
                         (<= (- (vector-ref ext jj)
                                (vector-ref ext i))
                             angle))
                    (loop (+ jj 1))
                    (begin
                      (set! j jj))))
              (let ((cnt (- j i)))
                (when (> cnt max-win)
                  (set! max-win cnt))))
            (+ same-count max-win))))))
```

## Erlang

```erlang
-module(solution).
-export([visible_points/3]).

-spec visible_points(Points :: [[integer()]], Angle :: integer(), Location :: [integer()]) -> integer().
visible_points(Points, Angle, Location) ->
    {SameCnt, Angles} = compute_angles(Points, Location),
    case Angle >= 360 of
        true -> length(Points);
        false ->
            MaxInWindow = max_visible_in_window(Angles, Angle),
            SameCnt + MaxInWindow
    end.

compute_angles(Points, [PosX, PosY]) ->
    lists:foldl(
      fun([X, Y], {Cnt, Acc}) ->
              Dx = X - PosX,
              Dy = Y - PosY,
              if Dx == 0 andalso Dy == 0 ->
                     {Cnt + 1, Acc};
                 true ->
                     Rad = math:atan2(Dy, Dx),
                     Deg = Rad * 180.0 / math:pi(),
                     AngleDeg = if Deg < 0 -> Deg + 360; true -> Deg end,
                     {Cnt, [AngleDeg | Acc]}
              end
      end,
      {0, []},
      Points).

max_visible_in_window([], _) ->
    0;
max_visible_in_window(AnglesList, Angle) ->
    Sorted = lists:sort(AnglesList),
    N = length(Sorted),
    Duplicated = Sorted ++ [A + 360.0 || A <- Sorted],
    AnglesTuple = list_to_tuple(Duplicated),
    Limit = Angle + 1e-9,
    slide_window(1, 1, N, 2 * N, AnglesTuple, Limit, 0).

slide_window(I, J, N, Total, Tuple, Limit, Max) when I > N ->
    Max;
slide_window(I, J, N, Total, Tuple, Limit, Max) ->
    AngleI = element(I, Tuple),
    NewJ = advance(J, AngleI, Tuple, Total, Limit),
    Count = NewJ - I,
    NewMax = if Count > Max -> Count; true -> Max end,
    slide_window(I + 1, NewJ, N, Total, Tuple, Limit, NewMax).

advance(J, AngleI, Tuple, Total, Limit) when J =< Total ->
    Diff = element(J, Tuple) - AngleI,
    if Diff =< Limit ->
            advance(J + 1, AngleI, Tuple, Total, Limit);
       true -> J
    end;
advance(J, _, _, _, _) ->
    J.
```

## Elixir

```elixir
defmodule Solution do
  @spec visible_points(points :: [[integer]], angle :: integer, location :: [integer]) :: integer
  def visible_points(points, angle, location) do
    [lx, ly] = location

    {same_cnt, angles} =
      Enum.reduce(points, {0, []}, fn [x, y], {cnt, acc} ->
        if x == lx and y == ly do
          {cnt + 1, acc}
        else
          dy = y - ly
          dx = x - lx
          rad = :math.atan2(dy, dx)
          deg = rad * 180.0 / :math.pi()
          deg = if deg < 0.0, do: deg + 360.0, else: deg
          {cnt, [deg | acc]}
        end
      end)

    # All points are at the location
    if angles == [] do
      same_cnt
    else
      sorted = Enum.sort(angles)
      max_in_window = max_visible(sorted, angle * 1.0)
      same_cnt + max_in_window
    end
  end

  defp max_visible(sorted, angle_limit) do
    n = length(sorted)

    # duplicate with +360 to handle circular wrap
    dup_list = sorted ++ Enum.map(sorted, fn x -> x + 360.0 end)
    dup_tuple = List.to_tuple(dup_list)

    sliding_window(dup_tuple, n, angle_limit, 0, 0, 0)
  end

  defp sliding_window(_dup_t, n, _angle, i, _j, max) when i >= n, do: max

  defp sliding_window(dup_t, n, angle, i, j, max) do
    j = advance_j(dup_t, i, j, n, angle)
    count = j - i
    new_max = if count > max, do: count, else: max
    sliding_window(dup_t, n, angle, i + 1, j, new_max)
  end

  defp advance_j(_dup_t, _i, j, n, _angle) when j >= _i + n, do: j

  defp advance_j(dup_t, i, j, n, angle) do
    limit = i + n

    if j < limit and (elem(dup_t, j) - elem(dup_t, i)) <= angle + 1.0e-9 do
      advance_j(dup_t, i, j + 1, n, angle)
    else
      j
    end
  end
end
```

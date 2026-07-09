# 1401. Circle and Rectangle Overlapping

## Cpp

```cpp
class Solution {
public:
    bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        long long closestX = xCenter;
        if (closestX < x1) closestX = x1;
        else if (closestX > x2) closestX = x2;
        
        long long closestY = yCenter;
        if (closestY < y1) closestY = y1;
        else if (closestY > y2) closestY = y2;
        
        long long dx = closestX - xCenter;
        long long dy = closestY - yCenter;
        return dx * dx + dy * dy <= 1LL * radius * radius;
    }
};
```

## Java

```java
class Solution {
    public boolean checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        int closestX = Math.max(x1, Math.min(xCenter, x2));
        int closestY = Math.max(y1, Math.min(yCenter, y2));
        long dx = (long)closestX - xCenter;
        long dy = (long)closestY - yCenter;
        return dx * dx + dy * dy <= (long)radius * radius;
    }
}
```

## Python

```python
class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        # Clamp the circle center coordinates to the rectangle bounds
        nearest_x = max(x1, min(xCenter, x2))
        nearest_y = max(y1, min(yCenter, y2))
        
        dx = xCenter - nearest_x
        dy = yCenter - nearest_y
        
        return dx * dx + dy * dy <= radius * radius
```

## Python3

```python
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest point on the rectangle to the circle's center
        nearest_x = min(max(xCenter, x1), x2)
        nearest_y = min(max(yCenter, y1), y2)
        dx = xCenter - nearest_x
        dy = yCenter - nearest_y
        return dx * dx + dy * dy <= radius * radius
```

## C

```c
#include <stdbool.h>

bool checkOverlap(int radius, int xCenter, int yCenter,
                  int x1, int y1, int x2, int y2) {
    int nearestX = xCenter;
    if (nearestX < x1) nearestX = x1;
    else if (nearestX > x2) nearestX = x2;

    int nearestY = yCenter;
    if (nearestY < y1) nearestY = y1;
    else if (nearestY > y2) nearestY = y2;

    long long dx = (long long)xCenter - nearestX;
    long long dy = (long long)yCenter - nearestY;
    long long distSq = dx * dx + dy * dy;
    long long radSq = (long long)radius * radius;

    return distSq <= radSq;
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        int closestX = Math.Max(x1, Math.Min(xCenter, x2));
        int closestY = Math.Max(y1, Math.Min(yCenter, y2));
        long dx = (long)closestX - xCenter;
        long dy = (long)closestY - yCenter;
        return dx * dx + dy * dy <= (long)radius * radius;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} radius
 * @param {number} xCenter
 * @param {number} yCenter
 * @param {number} x1
 * @param {number} y1
 * @param {number} x2
 * @param {number} y2
 * @return {boolean}
 */
var checkOverlap = function(radius, xCenter, yCenter, x1, y1, x2, y2) {
    const clamp = (val, low, high) => Math.max(low, Math.min(high, val));
    const closestX = clamp(xCenter, x1, x2);
    const closestY = clamp(yCenter, y1, y2);
    const dx = xCenter - closestX;
    const dy = yCenter - closestY;
    return dx * dx + dy * dy <= radius * radius;
};
```

## Typescript

```typescript
function checkOverlap(radius: number, xCenter: number, yCenter: number, x1: number, y1: number, x2: number, y2: number): boolean {
    // Clamp the circle center to the rectangle bounds to find the closest point
    const nearestX = Math.max(x1, Math.min(xCenter, x2));
    const nearestY = Math.max(y1, Math.min(yCenter, y2));

    const dx = xCenter - nearestX;
    const dy = yCenter - nearestY;

    return dx * dx + dy * dy <= radius * radius;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $radius
     * @param Integer $xCenter
     * @param Integer $yCenter
     * @param Integer $x1
     * @param Integer $y1
     * @param Integer $x2
     * @param Integer $y2
     * @return Boolean
     */
    function checkOverlap($radius, $xCenter, $yCenter, $x1, $y1, $x2, $y2) {
        $closestX = max($x1, min($xCenter, $x2));
        $closestY = max($y1, min($yCenter, $y2));
        $dx = $closestX - $xCenter;
        $dy = $closestY - $yCenter;
        return ($dx * $dx + $dy * $dy) <= ($radius * $radius);
    }
}
```

## Swift

```swift
class Solution {
    func checkOverlap(_ radius: Int, _ xCenter: Int, _ yCenter: Int, _ x1: Int, _ y1: Int, _ x2: Int, _ y2: Int) -> Bool {
        let closestX = max(x1, min(xCenter, x2))
        let closestY = max(y1, min(yCenter, y2))
        let dx = closestX - xCenter
        let dy = closestY - yCenter
        return dx * dx + dy * dy <= radius * radius
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkOverlap(radius: Int, xCenter: Int, yCenter: Int, x1: Int, y1: Int, x2: Int, y2: Int): Boolean {
        val nearestX = when {
            xCenter < x1 -> x1
            xCenter > x2 -> x2
            else -> xCenter
        }
        val nearestY = when {
            yCenter < y1 -> y1
            yCenter > y2 -> y2
            else -> yCenter
        }
        val dx = (xCenter - nearestX).toLong()
        val dy = (yCenter - nearestY).toLong()
        return dx * dx + dy * dy <= radius.toLong() * radius.toLong()
    }
}
```

## Dart

```dart
class Solution {
  bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
    int closestX = xCenter;
    if (xCenter < x1) {
      closestX = x1;
    } else if (xCenter > x2) {
      closestX = x2;
    }

    int closestY = yCenter;
    if (yCenter < y1) {
      closestY = y1;
    } else if (yCenter > y2) {
      closestY = y2;
    }

    int dx = xCenter - closestX;
    int dy = yCenter - closestY;
    return dx * dx + dy * dy <= radius * radius;
  }
}
```

## Golang

```go
func checkOverlap(radius int, xCenter int, yCenter int, x1 int, y1 int, x2 int, y2 int) bool {
	nearestX := xCenter
	if nearestX < x1 {
		nearestX = x1
	} else if nearestX > x2 {
		nearestX = x2
	}
	nearestY := yCenter
	if nearestY < y1 {
		nearestY = y1
	} else if nearestY > y2 {
		nearestY = y2
	}
	dx := xCenter - nearestX
	dy := yCenter - nearestY
	distSq := int64(dx*dx + dy*dy)
	rSq := int64(radius * radius)
	return distSq <= rSq
}
```

## Ruby

```ruby
def check_overlap(radius, x_center, y_center, x1, y1, x2, y2)
  closest_x = [[x_center, x1].max, x2].min
  closest_y = [[y_center, y1].max, y2].min
  dx = closest_x - x_center
  dy = closest_y - y_center
  dx * dx + dy * dy <= radius * radius
end
```

## Scala

```scala
object Solution {
    def checkOverlap(radius: Int, xCenter: Int, yCenter: Int, x1: Int, y1: Int, x2: Int, y2: Int): Boolean = {
        val nearestX = 
            if (xCenter < x1) x1
            else if (xCenter > x2) x2
            else xCenter
        val nearestY = 
            if (yCenter < y1) y1
            else if (yCenter > y2) y2
            else yCenter

        val dx = xCenter - nearestX
        val dy = yCenter - nearestY
        dx * dx + dy * dy <= radius * radius
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_overlap(radius: i32, x_center: i32, y_center: i32, x1: i32, y1: i32, x2: i32, y2: i32) -> bool {
        let closest_x = if x_center < x1 {
            x1
        } else if x_center > x2 {
            x2
        } else {
            x_center
        };
        let closest_y = if y_center < y1 {
            y1
        } else if y_center > y2 {
            y2
        } else {
            y_center
        };
        let dx = (closest_x - x_center) as i64;
        let dy = (closest_y - y_center) as i64;
        let dist_sq = dx * dx + dy * dy;
        let r_sq = (radius as i64) * (radius as i64);
        dist_sq <= r_sq
    }
}
```

## Racket

```racket
(define/contract (check-overlap radius xCenter yCenter x1 y1 x2 y2)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? boolean?)
  (let* ([nearest-x (max x1 (min xCenter x2))]
         [nearest-y (max y1 (min yCenter y2))]
         [dx (- xCenter nearest-x)]
         [dy (- yCenter nearest-y)])
    (<= (+ (* dx dx) (* dy dy)) (* radius radius))))
```

## Erlang

```erlang
-spec check_overlap(Radius :: integer(), XCenter :: integer(), YCenter :: integer(),
                    X1 :: integer(), Y1 :: integer(), X2 :: integer(), Y2 :: integer()) -> boolean().
check_overlap(Radius, Xc, Yc, X1, Y1, X2, Y2) ->
    ClosestX = clamp(Xc, X1, X2),
    ClosestY = clamp(Yc, Y1, Y2),
    Dx = Xc - ClosestX,
    Dy = Yc - ClosestY,
    DistSq = Dx*Dx + Dy*Dy,
    Radius*Radius >= DistSq.

clamp(V, Low, High) when V < Low -> Low;
clamp(V, Low, High) when V > High -> High;
clamp(V, _Low, _High) -> V.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_overlap(radius :: integer, x_center :: integer, y_center :: integer, x1 :: integer, y1 :: integer, x2 :: integer, y2 :: integer) :: boolean
  def check_overlap(radius, x_center, y_center, x1, y1, x2, y2) do
    closest_x =
      cond do
        x_center < x1 -> x1
        x_center > x2 -> x2
        true -> x_center
      end

    closest_y =
      cond do
        y_center < y1 -> y1
        y_center > y2 -> y2
        true -> y_center
      end

    dx = x_center - closest_x
    dy = y_center - closest_y
    dx * dx + dy * dy <= radius * radius
  end
end
```

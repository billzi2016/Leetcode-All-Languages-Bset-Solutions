# 0223. Rectangle Area

## Cpp

```cpp
class Solution {
public:
    int computeArea(int ax1, int ay1, int ax2, int ay2,
                    int bx1, int by1, int bx2, int by2) {
        long long areaA = static_cast<long long>(ax2 - ax1) * (ay2 - ay1);
        long long areaB = static_cast<long long>(bx2 - bx1) * (by2 - by1);
        
        int overlapWidth = max(0, min(ax2, bx2) - max(ax1, bx1));
        int overlapHeight = max(0, min(ay2, by2) - max(ay1, by1));
        long long overlapArea = static_cast<long long>(overlapWidth) * overlapHeight;
        
        return static_cast<int>(areaA + areaB - overlapArea);
    }
};
```

## Java

```java
class Solution {
    public int computeArea(int ax1, int ay1, int ax2, int ay2,
                           int bx1, int by1, int bx2, int by2) {
        int areaA = (ax2 - ax1) * (ay2 - ay1);
        int areaB = (bx2 - bx1) * (by2 - by1);
        
        int overlapWidth = Math.min(ax2, bx2) - Math.max(ax1, bx1);
        int overlapHeight = Math.min(ay2, by2) - Math.max(ay1, by1);
        if (overlapWidth < 0) overlapWidth = 0;
        if (overlapHeight < 0) overlapHeight = 0;
        
        int overlapArea = overlapWidth * overlapHeight;
        return areaA + areaB - overlapArea;
    }
}
```

## Python

```python
class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))

        return area1 + area2 - overlap_width * overlap_height
```

## Python3

```python
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int,
                    bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)

        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
        overlap_area = overlap_width * overlap_height

        return area_a + area_b - overlap_area
```

## C

```c
int computeArea(int ax1, int ay1, int ax2, int ay2,
                int bx1, int by1, int bx2, int by2) {
    long areaA = (long)(ax2 - ax1) * (ay2 - ay1);
    long areaB = (long)(bx2 - bx1) * (by2 - by1);
    
    int overlapWidth = (ax2 < bx2 ? ax2 : bx2) - (ax1 > bx1 ? ax1 : bx1);
    if (overlapWidth < 0) overlapWidth = 0;
    
    int overlapHeight = (ay2 < by2 ? ay2 : by2) - (ay1 > by1 ? ay1 : by1);
    if (overlapHeight < 0) overlapHeight = 0;
    
    long overlapArea = (long)overlapWidth * overlapHeight;
    
    return (int)(areaA + areaB - overlapArea);
}
```

## Csharp

```csharp
public class Solution {
    public int ComputeArea(int ax1, int ay1, int ax2, int ay2,
                           int bx1, int by1, int bx2, int by2) {
        int areaA = (ax2 - ax1) * (ay2 - ay1);
        int areaB = (bx2 - bx1) * (by2 - by1);

        int overlapWidth = Math.Max(0, Math.Min(ax2, bx2) - Math.Max(ax1, bx1));
        int overlapHeight = Math.Max(0, Math.Min(ay2, by2) - Math.Max(ay1, by1));
        int overlapArea = overlapWidth * overlapHeight;

        return areaA + areaB - overlapArea;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} ax1
 * @param {number} ay1
 * @param {number} ax2
 * @param {number} ay2
 * @param {number} bx1
 * @param {number} by1
 * @param {number} bx2
 * @param {number} by2
 * @return {number}
 */
var computeArea = function(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) {
    const areaA = (ax2 - ax1) * (ay2 - ay1);
    const areaB = (bx2 - bx1) * (by2 - by1);
    
    const overlapWidth = Math.max(0, Math.min(ax2, bx2) - Math.max(ax1, bx1));
    const overlapHeight = Math.max(0, Math.min(ay2, by2) - Math.max(ay1, by1));
    const overlapArea = overlapWidth * overlapHeight;
    
    return areaA + areaB - overlapArea;
};
```

## Typescript

```typescript
function computeArea(ax1: number, ay1: number, ax2: number, ay2: number, bx1: number, by1: number, bx2: number, by2: number): number {
    const areaA = (ax2 - ax1) * (ay2 - ay1);
    const areaB = (bx2 - bx1) * (by2 - by1);
    const overlapWidth = Math.max(0, Math.min(ax2, bx2) - Math.max(ax1, bx1));
    const overlapHeight = Math.max(0, Math.min(ay2, by2) - Math.max(ay1, by1));
    const overlapArea = overlapWidth * overlapHeight;
    return areaA + areaB - overlapArea;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $ax1
     * @param Integer $ay1
     * @param Integer $ax2
     * @param Integer $ay2
     * @param Integer $bx1
     * @param Integer $by1
     * @param Integer $bx2
     * @param Integer $by2
     * @return Integer
     */
    function computeArea($ax1, $ay1, $ax2, $ay2, $bx1, $by1, $bx2, $by2) {
        $areaA = ($ax2 - $ax1) * ($ay2 - $ay1);
        $areaB = ($bx2 - $bx1) * ($by2 - $by1);

        $overlapWidth = max(0, min($ax2, $bx2) - max($ax1, $bx1));
        $overlapHeight = max(0, min($ay2, $by2) - max($ay1, $by1));
        $overlapArea = $overlapWidth * $overlapHeight;

        return $areaA + $areaB - $overlapArea;
    }
}
```

## Swift

```swift
class Solution {
    func computeArea(_ ax1: Int, _ ay1: Int, _ ax2: Int, _ ay2: Int,
                    _ bx1: Int, _ by1: Int, _ bx2: Int, _ by2: Int) -> Int {
        let areaA = (ax2 - ax1) * (ay2 - ay1)
        let areaB = (bx2 - bx1) * (by2 - by1)
        
        let overlapWidth = max(0, min(ax2, bx2) - max(ax1, bx1))
        let overlapHeight = max(0, min(ay2, by2) - max(ay1, by1))
        let overlapArea = overlapWidth * overlapHeight
        
        return areaA + areaB - overlapArea
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun computeArea(ax1: Int, ay1: Int, ax2: Int, ay2: Int,
                    bx1: Int, by1: Int, bx2: Int, by2: Int): Int {
        val areaA = (ax2 - ax1).toLong() * (ay2 - ay1)
        val areaB = (bx2 - bx1).toLong() * (by2 - by1)

        val overlapWidth = kotlin.math.max(0, kotlin.math.min(ax2, bx2) - kotlin.math.max(ax1, bx1))
        val overlapHeight = kotlin.math.max(0, kotlin.math.min(ay2, by2) - kotlin.math.max(ay1, by1))

        val overlapArea = overlapWidth.toLong() * overlapHeight

        return (areaA + areaB - overlapArea).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int computeArea(int ax1, int ay1, int ax2, int ay2,
      int bx1, int by1, int bx2, int by2) {
    int areaA = (ax2 - ax1) * (ay2 - ay1);
    int areaB = (bx2 - bx1) * (by2 - by1);

    int overlapWidth = (ax2 < bx2 ? ax2 : bx2) -
        (ax1 > bx1 ? ax1 : bx1);
    if (overlapWidth < 0) overlapWidth = 0;

    int overlapHeight = (ay2 < by2 ? ay2 : by2) -
        (ay1 > by1 ? ay1 : by1);
    if (overlapHeight < 0) overlapHeight = 0;

    int overlapArea = overlapWidth * overlapHeight;
    return areaA + areaB - overlapArea;
  }
}
```

## Golang

```go
func computeArea(ax1 int, ay1 int, ax2 int, ay2 int, bx1 int, by1 int, bx2 int, by2 int) int {
	areaA := (ax2 - ax1) * (ay2 - ay1)
	areaB := (bx2 - bx1) * (by2 - by1)

	overlapW := min(ax2, bx2) - max(ax1, bx1)
	if overlapW < 0 {
		overlapW = 0
	}
	overlapH := min(ay2, by2) - max(ay1, by1)
	if overlapH < 0 {
		overlapH = 0
	}

	return areaA + areaB - overlapW*overlapH
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

## Ruby

```ruby
def compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
  area_a = (ax2 - ax1) * (ay2 - ay1)
  area_b = (bx2 - bx1) * (by2 - by1)
  overlap_width = [[ax2, bx2].min - [ax1, bx1].max, 0].max
  overlap_height = [[ay2, by2].min - [ay1, by1].max, 0].max
  area_a + area_b - overlap_width * overlap_height
end
```

## Scala

```scala
object Solution {
    def computeArea(ax1: Int, ay1: Int, ax2: Int, ay2: Int,
                    bx1: Int, by1: Int, bx2: Int, by2: Int): Int = {
        val areaA = (ax2 - ax1) * (ay2 - ay1)
        val areaB = (bx2 - bx1) * (by2 - by1)

        val overlapWidth = Math.max(0, Math.min(ax2, bx2) - Math.max(ax1, bx1))
        val overlapHeight = Math.max(0, Math.min(ay2, by2) - Math.max(ay1, by1))
        val overlapArea = overlapWidth * overlapHeight

        areaA + areaB - overlapArea
    }
}
```

## Rust

```rust
impl Solution {
    pub fn compute_area(ax1: i32, ay1: i32, ax2: i32, ay2: i32,
                       bx1: i32, by1: i32, bx2: i32, by2: i32) -> i32 {
        let area1 = (ax2 - ax1) * (ay2 - ay1);
        let area2 = (bx2 - bx1) * (by2 - by1);

        let overlap_width = std::cmp::max(0, std::cmp::min(ax2, bx2) - std::cmp::max(ax1, bx1));
        let overlap_height = std::cmp::max(0, std::cmp::min(ay2, by2) - std::cmp::max(ay1, by1));

        let overlap_area = overlap_width * overlap_height;

        area1 + area2 - overlap_area
    }
}
```

## Racket

```racket
(define/contract (compute-area ax1 ay1 ax2 ay2 bx1 by1 bx2 by2)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?
      exact-integer? exact-integer? exact-integer? exact-integer?
      exact-integer?)
  (let* ([area1 (* (- ax2 ax1) (- ay2 ay1))]
         [area2 (* (- bx2 bx1) (- by2 by1))]
         [overlap-w (max 0 (- (min ax2 bx2) (max ax1 bx1)))]
         [overlap-h (max 0 (- (min ay2 by2) (max ay1 by1)))]
         [overlap (* overlap-w overlap-h)])
    (+ area1 area2 (- overlap))))
```

## Erlang

```erlang
-spec compute_area(Ax1 :: integer(), Ay1 :: integer(), Ax2 :: integer(), Ay2 :: integer(),
                  Bx1 :: integer(), By1 :: integer(), Bx2 :: integer(), By2 :: integer()) -> integer().
compute_area(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2) ->
    Area1 = (Ax2 - Ax1) * (Ay2 - Ay1),
    Area2 = (Bx2 - Bx1) * (By2 - By1),
    OverlapW = max(0, min(Ax2, Bx2) - max(Ax1, Bx1)),
    OverlapH = max(0, min(Ay2, By2) - max(Ay1, By1)),
    Area1 + Area2 - OverlapW * OverlapH.
```

## Elixir

```elixir
defmodule Solution do
  @spec compute_area(ax1 :: integer, ay1 :: integer, ax2 :: integer, ay2 :: integer, bx1 :: integer, by1 :: integer, bx2 :: integer, by2 :: integer) :: integer
  def compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) do
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)

    overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
    overlap_height = max(0, min(ay2, by2) - max(ay1, by1))

    area1 + area2 - overlap_width * overlap_height
  end
end
```

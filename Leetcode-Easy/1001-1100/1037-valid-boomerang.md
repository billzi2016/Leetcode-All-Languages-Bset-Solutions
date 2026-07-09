# 1037. Valid Boomerang

## Cpp

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool isBoomerang(vector<vector<int>>& points) {
        long long x1 = points[0][0], y1 = points[0][1];
        long long x2 = points[1][0], y2 = points[1][1];
        long long x3 = points[2][0], y3 = points[2][1];
        return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1);
    }
};
```

## Java

```java
class Solution {
    public boolean isBoomerang(int[][] points) {
        int x1 = points[0][0], y1 = points[0][1];
        int x2 = points[1][0], y2 = points[1][1];
        int x3 = points[2][0], y3 = points[2][1];
        // Check if the area (cross product) is non-zero
        return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1);
    }
}
```

## Python

```python
class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        (x1, y1), (x2, y2), (x3, y3) = points
        return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)
```

## Python3

```python
from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points
        # Check distinctness
        if (x1 == x2 and y1 == y2) or (x1 == x3 and y1 == y3) or (x2 == x3 and y2 == y3):
            return False
        # Non-collinear check using cross product
        return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)
```

## C

```c
#include <stdbool.h>

bool isBoomerang(int** points, int pointsSize, int* pointsColSize) {
    int x1 = points[0][0];
    int y1 = points[0][1];
    int x2 = points[1][0];
    int y2 = points[1][1];
    int x3 = points[2][0];
    int y3 = points[2][1];

    if ((x1 == x2 && y1 == y2) ||
        (x1 == x3 && y1 == y3) ||
        (x2 == x3 && y2 == y3))
        return false;

    long long cross = (long long)(x2 - x1) * (y3 - y1) -
                      (long long)(y2 - y1) * (x3 - x1);
    return cross != 0;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsBoomerang(int[][] points) {
        int x1 = points[0][0], y1 = points[0][1];
        int x2 = points[1][0], y2 = points[1][1];
        int x3 = points[2][0], y3 = points[2][1];
        return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {boolean}
 */
var isBoomerang = function(points) {
    const [x1, y1] = points[0];
    const [x2, y2] = points[1];
    const [x3, y3] = points[2];
    // Check if the cross product of vectors (p2-p1) and (p3-p1) is non-zero
    return (x2 - x1) * (y3 - y1) !== (y2 - y1) * (x3 - x1);
};
```

## Typescript

```typescript
function isBoomerang(points: number[][]): boolean {
    const [p1, p2, p3] = points;
    const [x1, y1] = p1;
    const [x2, y2] = p2;
    const [x3, y3] = p3;
    return (x2 - x1) * (y3 - y1) !== (y2 - y1) * (x3 - x1);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Boolean
     */
    function isBoomerang($points) {
        $x1 = $points[0][0];
        $y1 = $points[0][1];
        $x2 = $points[1][0];
        $y2 = $points[1][1];
        $x3 = $points[2][0];
        $y3 = $points[2][1];

        return ($x2 - $x1) * ($y3 - $y1) !== ($y2 - $y1) * ($x3 - $x1);
    }
}
```

## Swift

```swift
class Solution {
    func isBoomerang(_ points: [[Int]]) -> Bool {
        let p0 = points[0]
        let p1 = points[1]
        let p2 = points[2]
        
        // Ensure all three points are distinct
        if (p0[0] == p1[0] && p0[1] == p1[1]) ||
           (p0[0] == p2[0] && p0[1] == p2[1]) ||
           (p1[0] == p2[0] && p1[1] == p2[1]) {
            return false
        }
        
        let x1 = p0[0], y1 = p0[1]
        let x2 = p1[0], y2 = p1[1]
        let x3 = p2[0], y3 = p2[1]
        
        // Check for collinearity using cross product
        return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isBoomerang(points: Array<IntArray>): Boolean {
        val x0 = points[0][0]
        val y0 = points[0][1]
        val x1 = points[1][0]
        val y1 = points[1][1]
        val x2 = points[2][0]
        val y2 = points[2][1]

        return (x1 - x0).toLong() * (y2 - y0) != (y1 - y0).toLong() * (x2 - x0)
    }
}
```

## Dart

```dart
class Solution {
  bool isBoomerang(List<List<int>> points) {
    int x1 = points[0][0];
    int y1 = points[0][1];
    int x2 = points[1][0];
    int y2 = points[1][1];
    int x3 = points[2][0];
    int y3 = points[2][1];
    return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1);
  }
}
```

## Golang

```go
func isBoomerang(points [][]int) bool {
    x1, y1 := points[0][0], points[0][1]
    x2, y2 := points[1][0], points[1][1]
    x3, y3 := points[2][0], points[2][1]
    return (x2-x1)*(y3-y1) != (y2-y1)*(x3-x1)
}
```

## Ruby

```ruby
def is_boomerang(points)
  x1, y1 = points[0]
  x2, y2 = points[1]
  x3, y3 = points[2]
  (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)
end
```

## Scala

```scala
object Solution {
    def isBoomerang(points: Array[Array[Int]]): Boolean = {
        val x1 = points(0)(0)
        val y1 = points(0)(1)
        val x2 = points(1)(0)
        val y2 = points(1)(1)
        val x3 = points(2)(0)
        val y3 = points(2)(1)

        (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_boomerang(points: Vec<Vec<i32>>) -> bool {
        let x1 = points[0][0] as i64;
        let y1 = points[0][1] as i64;
        let x2 = points[1][0] as i64;
        let y2 = points[1][1] as i64;
        let x3 = points[2][0] as i64;
        let y3 = points[2][1] as i64;

        (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)
    }
}
```

## Racket

```racket
(define/contract (is-boomerang points)
  (-> (listof (listof exact-integer?)) boolean?)
  (let* ([p1 (list-ref points 0)]
         [p2 (list-ref points 1)]
         [p3 (list-ref points 2)]
         [x1 (first p1)] [y1 (second p1)]
         [x2 (first p2)] [y2 (second p2)]
         [x3 (first p3)] [y3 (second p3)])
    (and (not (or (equal? p1 p2) (equal? p1 p3) (equal? p2 p3)))
         (not (= (- (* (- x2 x1) (- y3 y1))
                    (* (- x3 x1) (- y2 y1))) 0)))))
```

## Erlang

```erlang
-spec is_boomerang(Points :: [[integer()]]) -> boolean().
is_boomerang(Points) when is_list(Points), length(Points) =:= 3 ->
    [[X1,Y1],[X2,Y2],[X3,Y3]] = Points,
    Distinct = not ((X1 == X2 andalso Y1 == Y2) orelse
                   (X1 == X3 andalso Y1 == Y3) orelse
                   (X2 == X3 andalso Y2 == Y3)),
    AreaNonZero = ((X2 - X1)*(Y3 - Y1)) =/= ((X3 - X1)*(Y2 - Y1)),
    Distinct andalso AreaNonZero;
is_boomerang(_) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_boomerang(points :: [[integer]]) :: boolean
  def is_boomerang([[x1, y1], [x2, y2], [x3, y3]]) do
    (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)
  end
end
```

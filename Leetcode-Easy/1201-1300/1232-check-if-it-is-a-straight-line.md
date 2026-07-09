# 1232. Check If It Is a Straight Line

## Cpp

```cpp
class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        if (coordinates.size() <= 2) return true;
        long long x0 = coordinates[0][0];
        long long y0 = coordinates[0][1];
        long long x1 = coordinates[1][0];
        long long y1 = coordinates[1][1];
        long long dx = x1 - x0;
        long long dy = y1 - y0;
        for (size_t i = 2; i < coordinates.size(); ++i) {
            long long xi = coordinates[i][0];
            long long yi = coordinates[i][1];
            if (dx * (yi - y0) != dy * (xi - x0))
                return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        if (coordinates.length <= 2) return true;
        long x0 = coordinates[0][0];
        long y0 = coordinates[0][1];
        long dx = coordinates[1][0] - x0;
        long dy = coordinates[1][1] - y0;
        for (int i = 2; i < coordinates.length; i++) {
            long xi = coordinates[i][0];
            long yi = coordinates[i][1];
            if ((xi - x0) * dy != (yi - y0) * dx) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) <= 2:
            return True
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx = x1 - x0
        dy = y1 - y0
        for x, y in coordinates[2:]:
            if dx * (y - y0) != dy * (x - x0):
                return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx = x1 - x0
        dy = y1 - y0
        for x, y in coordinates[2:]:
            if dy * (x - x0) != dx * (y - y0):
                return False
        return True
```

## C

```c
#include <stdbool.h>

bool checkStraightLine(int** coordinates, int coordinatesSize, int* coordinatesColSize) {
    if (coordinatesSize <= 2) return true;
    long long x0 = coordinates[0][0];
    long long y0 = coordinates[0][1];
    long long x1 = coordinates[1][0];
    long long y1 = coordinates[1][1];
    long long dx = x1 - x0;
    long long dy = y1 - y0;
    for (int i = 2; i < coordinatesSize; ++i) {
        long long xi = coordinates[i][0];
        long long yi = coordinates[i][1];
        if ((xi - x0) * dy != (yi - y0) * dx)
            return false;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckStraightLine(int[][] coordinates) {
        int n = coordinates.Length;
        if (n <= 2) return true;

        long x0 = coordinates[0][0];
        long y0 = coordinates[0][1];
        long x1 = coordinates[1][0];
        long y1 = coordinates[1][1];

        long dx = x1 - x0;
        long dy = y1 - y0;

        for (int i = 2; i < n; i++) {
            long xi = coordinates[i][0];
            long yi = coordinates[i][1];
            if (dx * (yi - y0) != dy * (xi - x0))
                return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */
var checkStraightLine = function(coordinates) {
    if (coordinates.length <= 2) return true;
    const [x0, y0] = coordinates[0];
    const [x1, y1] = coordinates[1];
    const dx = x1 - x0;
    const dy = y1 - y0;
    for (let i = 2; i < coordinates.length; i++) {
        const [xi, yi] = coordinates[i];
        if ((xi - x0) * dy !== (yi - y0) * dx) {
            return false;
        }
    }
    return true;
};
```

## Typescript

```typescript
function checkStraightLine(coordinates: number[][]): boolean {
    const [x0, y0] = coordinates[0];
    const [x1, y1] = coordinates[1];
    const dx = x1 - x0;
    const dy = y1 - y0;
    for (let i = 2; i < coordinates.length; i++) {
        const [xi, yi] = coordinates[i];
        if ((xi - x0) * dy !== (yi - y0) * dx) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $coordinates
     * @return Boolean
     */
    function checkStraightLine($coordinates) {
        $n = count($coordinates);
        if ($n <= 2) {
            return true;
        }
        $x0 = $coordinates[0][0];
        $y0 = $coordinates[0][1];
        $x1 = $coordinates[1][0];
        $y1 = $coordinates[1][1];
        $dx = $x1 - $x0;
        $dy = $y1 - $y0;

        for ($i = 2; $i < $n; $i++) {
            $xi = $coordinates[$i][0];
            $yi = $coordinates[$i][1];
            if (($xi - $x0) * $dy !== ($yi - $y0) * $dx) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func checkStraightLine(_ coordinates: [[Int]]) -> Bool {
        if coordinates.count <= 2 { return true }
        let x0 = coordinates[0][0]
        let y0 = coordinates[0][1]
        let x1 = coordinates[1][0]
        let y1 = coordinates[1][1]
        let dx = x1 - x0
        let dy = y1 - y0
        for i in 2..<coordinates.count {
            let xi = coordinates[i][0]
            let yi = coordinates[i][1]
            if (xi - x0) * dy != (yi - y0) * dx {
                return false
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkStraightLine(coordinates: Array<IntArray>): Boolean {
        if (coordinates.size <= 2) return true
        val x0 = coordinates[0][0]
        val y0 = coordinates[0][1]
        val x1 = coordinates[1][0]
        val y1 = coordinates[1][1]
        val dx = x1 - x0
        val dy = y1 - y0
        for (i in 2 until coordinates.size) {
            val xi = coordinates[i][0]
            val yi = coordinates[i][1]
            if ((xi - x0).toLong() * dy != (yi - y0).toLong() * dx) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool checkStraightLine(List<List<int>> coordinates) {
    if (coordinates.length <= 2) return true;
    int x0 = coordinates[0][0];
    int y0 = coordinates[0][1];
    int x1 = coordinates[1][0];
    int y1 = coordinates[1][1];
    int dx = x1 - x0;
    int dy = y1 - y0;
    for (int i = 2; i < coordinates.length; ++i) {
      int xi = coordinates[i][0];
      int yi = coordinates[i][1];
      if ((xi - x0) * dy != (yi - y0) * dx) return false;
    }
    return true;
  }
}
```

## Golang

```go
func checkStraightLine(coordinates [][]int) bool {
	if len(coordinates) <= 2 {
		return true
	}
	x0, y0 := coordinates[0][0], coordinates[0][1]
	x1, y1 := coordinates[1][0], coordinates[1][1]
	dx := int64(x1 - x0)
	dy := int64(y1 - y0)

	for i := 2; i < len(coordinates); i++ {
		xi, yi := coordinates[i][0], coordinates[i][1]
		if int64(xi-x0)*dy != int64(yi-y0)*dx {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def check_straight_line(coordinates)
  return true if coordinates.size <= 2
  x0, y0 = coordinates[0]
  x1, y1 = coordinates[1]
  dx = x1 - x0
  dy = y1 - y0
  coordinates.each do |x, y|
    return false unless (y - y0) * dx == (x - x0) * dy
  end
  true
end
```

## Scala

```scala
object Solution {
    def checkStraightLine(coordinates: Array[Array[Int]]): Boolean = {
        if (coordinates.length <= 2) return true
        val x0 = coordinates(0)(0)
        val y0 = coordinates(0)(1)
        val x1 = coordinates(1)(0)
        val y1 = coordinates(1)(1)
        val dx = x1 - x0
        val dy = y1 - y0
        for (i <- 2 until coordinates.length) {
            val xi = coordinates(i)(0)
            val yi = coordinates(i)(1)
            if ((yi - y0).toLong * dx != (xi - x0).toLong * dy) return false
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_straight_line(coordinates: Vec<Vec<i32>>) -> bool {
        if coordinates.len() <= 2 {
            return true;
        }
        let x0 = coordinates[0][0] as i64;
        let y0 = coordinates[0][1] as i64;
        let x1 = coordinates[1][0] as i64;
        let y1 = coordinates[1][1] as i64;

        let dx = x1 - x0;
        let dy = y1 - y0;

        for point in coordinates.iter().skip(2) {
            let xi = point[0] as i64;
            let yi = point[1] as i64;
            if (xi - x0) * dy != (yi - y0) * dx {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (check-straight-line coordinates)
  (-> (listof (listof exact-integer?)) boolean?)
  (let* ([p0 (first coordinates)]
         [p1 (second coordinates)]
         [x0 (first p0)] [y0 (second p0)]
         [x1 (first p1)] [y1 (second p1)]
         [dx (- x1 x0)]
         [dy (- y1 y0)])
    (if (= (length coordinates) 2)
        #t
        (for/and ([p (cddr coordinates)])
          (= (* (- (second p) y0) dx)
             (* (- (first p) x0) dy))))))
```

## Erlang

```erlang
-spec check_straight_line(Coordinates :: [[integer()]]) -> boolean().
check_straight_line(Coordinates) ->
    case Coordinates of
        [_] -> true;
        [_, _] -> true;
        [[X1, Y1], [X2, Y2] | Rest] ->
            Dx = X2 - X1,
            Dy = Y2 - Y1,
            check_rest(Rest, X1, Y1, Dx, Dy)
    end.

-spec check_rest([[integer()]], integer(), integer(), integer(), integer()) -> boolean().
check_rest([], _X0, _Y0, _Dx, _Dy) ->
    true;
check_rest([[X, Y] | Tail], X0, Y0, Dx, Dy) ->
    case (Y - Y0) * Dx =:= (X - X0) * Dy of
        true -> check_rest(Tail, X0, Y0, Dx, Dy);
        false -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_straight_line(coordinates :: [[integer]]) :: boolean
  def check_straight_line([[x1, y1], [x2, y2] | rest]) do
    dx = x2 - x1
    dy = y2 - y1

    Enum.all?(rest, fn [x, y] ->
      (x - x1) * dy == (y - y1) * dx
    end)
  end
end
```

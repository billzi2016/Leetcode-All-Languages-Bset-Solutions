# 3516. Find Closest Person

## Cpp

```cpp
class Solution {
public:
    int findClosest(int x, int y, int z) {
        int d1 = std::abs(x - z);
        int d2 = std::abs(y - z);
        if (d1 < d2) return 1;
        if (d1 > d2) return 2;
        return 0;
    }
};
```

## Java

```java
class Solution {
    public int findClosest(int x, int y, int z) {
        int d1 = Math.abs(x - z);
        int d2 = Math.abs(y - z);
        if (d1 < d2) return 1;
        if (d1 > d2) return 2;
        return 0;
    }
}
```

## Python

```python
class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        d1 = abs(x - z)
        d2 = abs(y - z)
        if d1 < d2:
            return 1
        elif d2 < d1:
            return 2
        else:
            return 0
```

## Python3

```python
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1 = abs(x - z)
        d2 = abs(y - z)
        if d1 < d2:
            return 1
        elif d1 > d2:
            return 2
        else:
            return 0
```

## C

```c
int findClosest(int x, int y, int z) {
    int d1 = x > z ? x - z : z - x;
    int d2 = y > z ? y - z : z - y;
    if (d1 < d2) return 1;
    if (d2 < d1) return 2;
    return 0;
}
```

## Csharp

```csharp
public class Solution {
    public int FindClosest(int x, int y, int z) {
        int d1 = Math.Abs(x - z);
        int d2 = Math.Abs(y - z);
        if (d1 < d2) return 1;
        if (d2 < d1) return 2;
        return 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} x
 * @param {number} y
 * @param {number} z
 * @return {number}
 */
var findClosest = function(x, y, z) {
    const d1 = Math.abs(x - z);
    const d2 = Math.abs(y - z);
    if (d1 < d2) return 1;
    if (d2 < d1) return 2;
    return 0;
};
```

## Typescript

```typescript
function findClosest(x: number, y: number, z: number): number {
    const d1 = Math.abs(x - z);
    const d2 = Math.abs(y - z);
    if (d1 < d2) return 1;
    if (d2 < d1) return 2;
    return 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $x
     * @param Integer $y
     * @param Integer $z
     * @return Integer
     */
    function findClosest($x, $y, $z) {
        $d1 = abs($x - $z);
        $d2 = abs($y - $z);
        if ($d1 < $d2) {
            return 1;
        } elseif ($d1 > $d2) {
            return 2;
        } else {
            return 0;
        }
    }
}
```

## Swift

```swift
class Solution {
    func findClosest(_ x: Int, _ y: Int, _ z: Int) -> Int {
        let d1 = abs(x - z)
        let d2 = abs(y - z)
        if d1 < d2 {
            return 1
        } else if d1 > d2 {
            return 2
        } else {
            return 0
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findClosest(x: Int, y: Int, z: Int): Int {
        val d1 = kotlin.math.abs(x - z)
        val d2 = kotlin.math.abs(y - z)
        return when {
            d1 < d2 -> 1
            d1 > d2 -> 2
            else -> 0
        }
    }
}
```

## Dart

```dart
class Solution {
  int findClosest(int x, int y, int z) {
    int d1 = (x - z).abs();
    int d2 = (y - z).abs();
    if (d1 < d2) return 1;
    if (d2 < d1) return 2;
    return 0;
  }
}
```

## Golang

```go
func findClosest(x int, y int, z int) int {
    d1 := x - z
    if d1 < 0 {
        d1 = -d1
    }
    d2 := y - z
    if d2 < 0 {
        d2 = -d2
    }
    if d1 < d2 {
        return 1
    } else if d2 < d1 {
        return 2
    }
    return 0
}
```

## Ruby

```ruby
def find_closest(x, y, z)
  d1 = (x - z).abs
  d2 = (y - z).abs
  return 0 if d1 == d2
  d1 < d2 ? 1 : 2
end
```

## Scala

```scala
object Solution {
    def findClosest(x: Int, y: Int, z: Int): Int = {
        val d1 = math.abs(x - z)
        val d2 = math.abs(y - z)
        if (d1 < d2) 1
        else if (d1 > d2) 2
        else 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_closest(x: i32, y: i32, z: i32) -> i32 {
        let d1 = (x - z).abs();
        let d2 = (y - z).abs();
        if d1 < d2 {
            1
        } else if d1 > d2 {
            2
        } else {
            0
        }
    }
}
```

## Racket

```racket
(define/contract (find-closest x y z)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let ([d1 (abs (- x z))]
        [d2 (abs (- y z))])
    (cond [(< d1 d2) 1]
          [(> d1 d2) 2]
          [else 0])))
```

## Erlang

```erlang
-spec find_closest(X :: integer(), Y :: integer(), Z :: integer()) -> integer().
find_closest(X, Y, Z) ->
    D1 = abs(X - Z),
    D2 = abs(Y - Z),
    case D1 < D2 of
        true -> 1;
        false ->
            case D1 > D2 of
                true -> 2;
                false -> 0
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_closest(x :: integer, y :: integer, z :: integer) :: integer
  def find_closest(x, y, z) do
    d1 = abs(x - z)
    d2 = abs(y - z)

    cond do
      d1 < d2 -> 1
      d1 > d2 -> 2
      true -> 0
    end
  end
end
```

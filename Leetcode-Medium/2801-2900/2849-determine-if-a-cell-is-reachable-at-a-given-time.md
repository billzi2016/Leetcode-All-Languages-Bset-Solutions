# 2849. Determine if a Cell Is Reachable at a Given Time

## Cpp

```cpp
class Solution {
public:
    bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        long long dx = llabs((long long)sx - fx);
        long long dy = llabs((long long)sy - fy);
        if (dx == 0 && dy == 0 && t == 1) return false;
        long long minTime = max(dx, dy);
        return t >= minTime;
    }
};
```

## Java

```java
class Solution {
    public boolean isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        if (sx == fx && sy == fy && t == 1) {
            return false;
        }
        int dx = Math.abs(sx - fx);
        int dy = Math.abs(sy - fy);
        int minTime = Math.max(dx, dy);
        return t >= minTime;
    }
}
```

## Python

```python
class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """
        if sx == fx and sy == fy:
            return t != 1
        min_time = max(abs(sx - fx), abs(sy - fy))
        return t >= min_time
```

## Python3

```python
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return t != 1
        min_time = max(abs(sx - fx), abs(sy - fy))
        return t >= min_time
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
    long long dx = llabs((long long)sx - (long long)fx);
    long long dy = llabs((long long)sy - (long long)fy);
    if (dx == 0 && dy == 0 && t == 1) return false;
    long long minTime = dx > dy ? dx : dy;
    return t >= minTime;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        if (sx == fx && sy == fy && t == 1) return false;
        int dx = Math.Abs(sx - fx);
        int dy = Math.Abs(sy - fy);
        int minTime = Math.Max(dx, dy);
        return t >= minTime;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} sx
 * @param {number} sy
 * @param {number} fx
 * @param {number} fy
 * @param {number} t
 * @return {boolean}
 */
var isReachableAtTime = function(sx, sy, fx, fy, t) {
    const dx = Math.abs(fx - sx);
    const dy = Math.abs(fy - sy);
    // Edge case: same cell and exactly 1 second cannot return.
    if (dx === 0 && dy === 0 && t === 1) return false;
    const minTime = Math.max(dx, dy);
    return t >= minTime;
};
```

## Typescript

```typescript
function isReachableAtTime(sx: number, sy: number, fx: number, fy: number, t: number): boolean {
    const dx = Math.abs(sx - fx);
    const dy = Math.abs(sy - fy);
    if (dx === 0 && dy === 0 && t === 1) return false;
    const minTime = Math.max(dx, dy);
    return t >= minTime;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $sx
     * @param Integer $sy
     * @param Integer $fx
     * @param Integer $fy
     * @param Integer $t
     * @return Boolean
     */
    function isReachableAtTime($sx, $sy, $fx, $fy, $t) {
        $dx = abs($sx - $fx);
        $dy = abs($sy - $fy);
        if ($dx == 0 && $dy == 0 && $t == 1) {
            return false;
        }
        $minTime = max($dx, $dy);
        return $t >= $minTime;
    }
}
```

## Swift

```swift
class Solution {
    func isReachableAtTime(_ sx: Int, _ sy: Int, _ fx: Int, _ fy: Int, _ t: Int) -> Bool {
        if sx == fx && sy == fy && t == 1 {
            return false
        }
        let dx = abs(sx - fx)
        let dy = abs(sy - fy)
        let minTime = max(dx, dy)
        return t >= minTime
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isReachableAtTime(sx: Int, sy: Int, fx: Int, fy: Int, t: Int): Boolean {
        val dx = kotlin.math.abs(sx - fx)
        val dy = kotlin.math.abs(sy - fy)
        if (dx == 0 && dy == 0 && t == 1) return false
        val minTime = maxOf(dx, dy)
        return t >= minTime
    }
}
```

## Dart

```dart
class Solution {
  bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
    int dx = (sx - fx).abs();
    int dy = (sy - fy).abs();
    if (dx == 0 && dy == 0 && t == 1) return false;
    int minTime = dx > dy ? dx : dy;
    return t >= minTime;
  }
}
```

## Golang

```go
func isReachableAtTime(sx int, sy int, fx int, fy int, t int) bool {
	if sx == fx && sy == fy {
		return t != 1
	}
	dx := sx - fx
	if dx < 0 {
		dx = -dx
	}
	dy := sy - fy
	if dy < 0 {
		dy = -dy
	}
	dist := dx
	if dy > dist {
		dist = dy
	}
	return t >= dist
}
```

## Ruby

```ruby
# @param {Integer} sx
# @param {Integer} sy
# @param {Integer} fx
# @param {Integer} fy
# @param {Integer} t
# @return {Boolean}
def is_reachable_at_time(sx, sy, fx, fy, t)
  if sx == fx && sy == fy
    return t != 1
  end
  dx = (sx - fx).abs
  dy = (sy - fy).abs
  min_time = [dx, dy].max
  t >= min_time
end
```

## Scala

```scala
object Solution {
    def isReachableAtTime(sx: Int, sy: Int, fx: Int, fy: Int, t: Int): Boolean = {
        if (sx == fx && sy == fy) {
            t != 1
        } else {
            val dx = Math.abs(sx - fx)
            val dy = Math.abs(sy - fy)
            val minTime = Math.max(dx, dy)
            t >= minTime
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_reachable_at_time(sx: i32, sy: i32, fx: i32, fy: i32, t: i32) -> bool {
        let dx = (sx - fx).abs();
        let dy = (sy - fy).abs();
        if dx == 0 && dy == 0 {
            return t != 1;
        }
        let min_time = std::cmp::max(dx, dy);
        t >= min_time
    }
}
```

## Racket

```racket
(define/contract (is-reachable-at-time sx sy fx fy t)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? boolean?)
  (let ((dx (abs (- sx fx)))
        (dy (abs (- sy fy))))
    (if (and (= dx 0) (= dy 0) (= t 1))
        #f
        (>= t (max dx dy)))))
```

## Erlang

```erlang
-spec is_reachable_at_time(Sx :: integer(), Sy :: integer(), Fx :: integer(), Fy :: integer(), T :: integer()) -> boolean().
is_reachable_at_time(Sx, Sy, Fx, Fy, T) ->
    Dx = abs(Sx - Fx),
    Dy = abs(Sy - Fy),
    case {Dx, Dy} of
        {0, 0} ->
            T =/= 1;
        _ ->
            MinTime = erlang:max(Dx, Dy),
            T >= MinTime
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_reachable_at_time(sx :: integer, sy :: integer, fx :: integer, fy :: integer, t :: integer) :: boolean
  def is_reachable_at_time(sx, sy, fx, fy, t) do
    dx = abs(fx - sx)
    dy = abs(fy - sy)

    if dx == 0 and dy == 0 do
      t != 1
    else
      t >= max(dx, dy)
    end
  end
end
```

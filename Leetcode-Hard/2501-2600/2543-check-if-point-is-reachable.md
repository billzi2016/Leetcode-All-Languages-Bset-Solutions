# 2543. Check if Point Is Reachable

## Cpp

```cpp
class Solution {
public:
    bool isReachable(int targetX, int targetY) {
        long long g = std::gcd((long long)targetX, (long long)targetY);
        while ((g & 1LL) == 0 && g > 0) {
            g >>= 1;
        }
        return g == 1;
    }
};
```

## Java

```java
class Solution {
    public boolean isReachable(int targetX, int targetY) {
        return gcd(targetX, targetY) == 1;
    }
    
    private int gcd(int a, int b) {
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
class Solution(object):
    def isReachable(self, targetX, targetY):
        """
        :type targetX: int
        :type targetY: int
        :rtype: bool
        """
        import math
        g = math.gcd(targetX, targetY)
        return (g & (g - 1)) == 0
```

## Python3

```python
import math

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        while targetX % 2 == 0:
            targetX //= 2
        while targetY % 2 == 0:
            targetY //= 2
        return math.gcd(targetX, targetY) == 1
```

## C

```c
bool isReachable(int targetX, int targetY) {
    long long x = targetX;
    long long y = targetY;
    // Compute GCD
    while (y != 0) {
        long long tmp = x % y;
        x = y;
        y = tmp;
    }
    long long g = x; // gcd
    
    // Remove all factors of 2 from the GCD
    while ((g & 1LL) == 0 && g > 0) {
        g >>= 1;
    }
    
    return g == 1;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsReachable(int targetX, int targetY) {
        long a = targetX;
        long b = targetY;
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        // a is the GCD
        return (a & (a - 1)) == 0;
    }
}
```

## Javascript

```javascript
var isReachable=function(targetX,targetY){const gcd=(a,b)=>{while(b!==0){let t=a%b;a=b;b=t;}return a;};let g=gcd(targetX,targetY);return (g&(g-1))===0;};
```

## Typescript

```typescript
function isReachable(targetX: number, targetY: number): boolean {
    let x = targetX;
    let y = targetY;
    while (true) {
        if (x === 1 && y === 1) return true;
        if (x === 0 || y === 0) return false;

        if (x % 2 === 0) {
            x /= 2;
            continue;
        }
        if (y % 2 === 0) {
            y /= 2;
            continue;
        }

        // both odd
        if (x === y) return false; // cannot reduce further

        if (x > y) {
            x = x - y;
        } else {
            y = y - x;
        }
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $targetX
     * @param Integer $targetY
     * @return Boolean
     */
    function isReachable($targetX, $targetY) {
        $g = $this->gcd($targetX, $targetY);
        // true if gcd is a power of two (including 1)
        return ($g & ($g - 1)) == 0;
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
    func isReachable(_ targetX: Int, _ targetY: Int) -> Bool {
        var x = targetX
        var y = targetY
        while y != 0 {
            let r = x % y
            x = y
            y = r
        }
        // x now holds gcd(targetX, targetY)
        return (x & (x - 1)) == 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isReachable(targetX: Int, targetY: Int): Boolean {
        var a = targetX.toLong()
        var b = targetY.toLong()
        fun gcd(x: Long, y: Long): Long {
            var xx = x
            var yy = y
            while (yy != 0L) {
                val tmp = xx % yy
                xx = yy
                yy = tmp
            }
            return kotlin.math.abs(xx)
        }
        var g = gcd(a, b)
        while (g % 2L == 0L && g > 1L) {
            g /= 2L
        }
        return g == 1L
    }
}
```

## Dart

```dart
class Solution {
  bool isReachable(int targetX, int targetY) {
    int g = _gcd(targetX, targetY);
    return (g & (g - 1)) == 0;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int tmp = a % b;
      a = b;
      b = tmp;
    }
    return a;
  }
}
```

## Golang

```go
func isReachable(targetX int, targetY int) bool {
    // Compute GCD of the two coordinates
    a, b := targetX, targetY
    for b != 0 {
        a, b = b, a%b
    }
    g := a
    // Check if the GCD is a power of two
    return (g & (g - 1)) == 0
}
```

## Ruby

```ruby
def is_reachable(target_x, target_y)
  g = target_x.gcd(target_y)
  (g & (g - 1)).zero?
end
```

## Scala

```scala
object Solution {
    def isReachable(targetX: Int, targetY: Int): Boolean = {
        var a = targetX.toLong
        var b = targetY.toLong
        while (b != 0) {
            val tmp = a % b
            a = b
            b = tmp
        }
        val g = a
        (g & (g - 1)) == 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_reachable(target_x: i32, target_y: i32) -> bool {
        fn gcd(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                let r = a % b;
                a = b;
                b = r;
            }
            a
        }

        let mut g = gcd(target_x as i64, target_y as i64);
        while g % 2 == 0 && g > 0 {
            g /= 2;
        }
        g == 1
    }
}
```

## Racket

```racket
#lang racket

(provide is-reachable)

(define/contract (is-reachable targetX targetY)
  (-> exact-integer? exact-integer? boolean?)
  (letrec ((gcd
            (lambda (a b)
              (if (= b 0) a (gcd b (remainder a b))))))
    (let loop ((g (gcd targetX targetY)))
      (cond [(= g 1) #t]
            [(even? g) (loop (/ g 2))]
            [else #f]))))
```

## Erlang

```erlang
-module(solution).
-export([is_reachable/2]).

-spec is_reachable(TargetX :: integer(), TargetY :: integer()) -> boolean().
is_reachable(TargetX, TargetY) ->
    G = erlang:gcd(TargetX, TargetY),
    (G band (G - 1)) == 0.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec is_reachable(target_x :: integer, target_y :: integer) :: boolean
  def is_reachable(target_x, target_y) do
    g = Integer.gcd(target_x, target_y)
    power_of_two?(g)
  end

  defp power_of_two?(n) when n > 0 do
    (n &&& (n - 1)) == 0
  end
end
```

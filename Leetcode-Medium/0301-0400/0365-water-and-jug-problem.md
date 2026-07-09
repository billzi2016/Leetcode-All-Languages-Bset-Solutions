# 0365. Water and Jug Problem

## Cpp

```cpp
class Solution {
public:
    bool canMeasureWater(int x, int y, int target) {
        if (target == 0) return true;
        if (x + y < target) return false;
        int g = std::gcd(x, y);
        return target % g == 0;
    }
};
```

## Java

```java
class Solution {
    public boolean canMeasureWater(int x, int y, int target) {
        if (target == 0) return true;
        if (x + y < target) return false;
        return target % gcd(x, y) == 0;
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
    def canMeasureWater(self, x, y, target):
        """
        :type x: int
        :type y: int
        :type target: int
        :rtype: bool
        """
        if target == 0:
            return True
        if x + y < target:
            return False
        import math
        return target % math.gcd(x, y) == 0
```

## Python3

```python
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target == 0:
            return True
        if target > x + y:
            return False
        from math import gcd
        return target % gcd(x, y) == 0
```

## C

```c
#include <stdbool.h>

static int gcd(int a, int b) {
    while (b != 0) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

bool canMeasureWater(int x, int y, int target) {
    if (target < 0) return false;
    if (target == 0) return true;
    int g = gcd(x, y);
    return target <= x + y && target % g == 0;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CanMeasureWater(int x, int y, int target)
    {
        if (target == 0) return true;
        if (x + y < target) return false;
        int g = Gcd(x, y);
        return target % g == 0;
    }

    private int Gcd(int a, int b)
    {
        while (b != 0)
        {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} x
 * @param {number} y
 * @param {number} target
 * @return {boolean}
 */
var canMeasureWater = function(x, y, target) {
    if (target === 0) return true;
    if (x + y < target) return false;
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    return target % gcd(x, y) === 0;
};
```

## Typescript

```typescript
function canMeasureWater(x: number, y: number, target: number): boolean {
    if (target === 0) return true;
    const total = x + y;
    if (target > total) return false;

    function gcd(a: number, b: number): number {
        while (b !== 0) {
            const temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }

    const g = gcd(x, y);
    return target % g === 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $x
     * @param Integer $y
     * @param Integer $target
     * @return Boolean
     */
    function canMeasureWater($x, $y, $target) {
        if ($target == 0) return true;
        if ($x + $y < $target) return false;

        // Compute GCD of x and y
        $a = $x;
        $b = $y;
        while ($b != 0) {
            $temp = $a % $b;
            $a = $b;
            $b = $temp;
        }
        $gcd = $a;

        return $target % $gcd == 0;
    }
}
```

## Swift

```swift
class Solution {
    func canMeasureWater(_ x: Int, _ y: Int, _ target: Int) -> Bool {
        if target == 0 { return true }
        let sum = x + y
        if sum < target { return false }
        
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a
            var b = b
            while b != 0 {
                let temp = a % b
                a = b
                b = temp
            }
            return a
        }
        
        return target % gcd(x, y) == 0
    }
}
```

## Kotlin

```kotlin
import kotlin.math.abs

class Solution {
    fun canMeasureWater(x: Int, y: Int, target: Int): Boolean {
        if (target < 0) return false
        val total = x + y
        if (target > total) return false
        val g = gcd(x, y)
        return target % g == 0
    }

    private fun gcd(a: Int, b: Int): Int {
        var aa = abs(a)
        var bb = abs(b)
        while (bb != 0) {
            val tmp = aa % bb
            aa = bb
            bb = tmp
        }
        return if (aa == 0) 1 else aa
    }
}
```

## Dart

```dart
class Solution {
  bool canMeasureWater(int x, int y, int target) {
    if (target == 0) return true;
    if (x + y < target) return false;
    return target % _gcd(x, y) == 0;
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
func canMeasureWater(x int, y int, target int) bool {
	if target < 0 || target > x+y {
		return false
	}
	if target == 0 {
		return true
	}
	g := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}(x, y)
	return target%g == 0
}
```

## Ruby

```ruby
# @param {Integer} x
# @param {Integer} y
# @param {Integer} target
# @return {Boolean}
def can_measure_water(x, y, target)
  return false if target > x + y
  g = x.gcd(y)
  target % g == 0
end
```

## Scala

```scala
object Solution {
    def canMeasureWater(x: Int, y: Int, target: Int): Boolean = {
        if (target == 0) return true
        val sum = x + y
        if (sum < target) return false
        if (x == 0 && y == 0) return false

        def gcd(a: Int, b: Int): Int = {
            var aa = a
            var bb = b
            while (bb != 0) {
                val tmp = aa % bb
                aa = bb
                bb = tmp
            }
            Math.abs(aa)
        }

        val g = gcd(x, y)
        if (g == 0) target == 0 else target % g == 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_measure_water(x: i32, y: i32, target: i32) -> bool {
        if target == 0 {
            return true;
        }
        let total = x + y;
        if target > total {
            return false;
        }
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let r = a % b;
                a = b;
                b = r;
            }
            a.abs()
        }
        target % gcd(x, y) == 0
    }
}
```

## Racket

```racket
(define/contract (can-measure-water x y target)
  (-> exact-integer? exact-integer? exact-integer? boolean?)
  (and (<= target (+ x y))
       (= (remainder target (gcd x y)) 0)))
```

## Erlang

```erlang
-spec can_measure_water(integer(), integer(), integer()) -> boolean().
can_measure_water(X, Y, Target) ->
    if
        Target =:= 0 -> true;
        Target > X + Y -> false;
        true ->
            G = gcd(X, Y),
            Target rem G =:= 0
    end.

gcd(A, 0) -> A;
gcd(0, B) -> B;
gcd(A, B) ->
    R = A rem B,
    if R =:= 0 -> B; true -> gcd(B, R) end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_measure_water(x :: integer, y :: integer, target :: integer) :: boolean
  def can_measure_water(x, y, target) do
    cond do
      target == 0 -> true
      target > x + y -> false
      rem(target, Integer.gcd(x, y)) == 0 -> true
      true -> false
    end
  end
end
```

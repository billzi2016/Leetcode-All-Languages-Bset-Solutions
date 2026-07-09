# 2745. Construct the Longest New String

## Cpp

```cpp
class Solution {
public:
    int longestString(int x, int y, int z) {
        int m = std::min(x, y);
        int extraA = (x > y) ? 1 : 0;
        int extraB = (y > x) ? 1 : 0;
        return 2 * z + 4 * m + 2 * extraA + 2 * extraB;
    }
};
```

## Java

```java
class Solution {
    public int longestString(int x, int y, int z) {
        int usedAA, usedBB;
        if (x > y) {
            usedBB = y;
            usedAA = Math.min(x, y + 1);
        } else if (y > x) {
            usedAA = x;
            usedBB = Math.min(y, x + 1);
        } else { // x == y
            usedAA = x;
            usedBB = y;
        }
        return 2 * (z + usedAA + usedBB);
    }
}
```

## Python

```python
class Solution(object):
    def longestString(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        if x > y:
            total_blocks = 2 * y + 1
        elif y > x:
            total_blocks = 2 * x + 1
        else:
            total_blocks = 2 * x
        return 2 * (z + total_blocks)
```

## Python3

```python
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        ans = 2 * z + 4 * min(x, y)
        if x != y:
            ans += 2
        return ans
```

## C

```c
int longestString(int x, int y, int z) {
    int usedAA = (x < y + 1) ? x : y + 1;
    int usedBB = (y < x + 1) ? y : x + 1;
    return 2 * z + 2 * usedAA + 2 * usedBB;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestString(int x, int y, int z) {
        int baseLen = 2 * z; // all "AB" strings can be used
        int ans = baseLen;

        // Pattern starting with "AA"
        int a = Math.Min(x, y + 1);
        if (a > 0) {
            int lenA = baseLen + 4 * a - 2;
            ans = Math.Max(ans, lenA);
        }

        // Pattern starting with "BB"
        int b = Math.Min(y, x + 1);
        if (b > 0) {
            int lenB = baseLen + 4 * b - 2;
            ans = Math.Max(ans, lenB);
        }

        return ans;
    }
}
```

## Javascript

```javascript
var longestString=function(x,y,z){const m=Math.min(x,y);let ans=2*z;if(x===y)ans+=4*m;else ans+=4*m+2;return ans};
```

## Typescript

```typescript
function longestString(x: number, y: number, z: number): number {
    const usableAA = Math.min(x, y + 1);
    const usableBB = Math.min(y, x + 1);
    return 2 * z + 2 * (usableAA + usableBB);
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
    function longestString($x, $y, $z) {
        if ($x > $y) {
            $usedAA = min($x, $y + 1);
            $usedBB = $y;
        } elseif ($y > $x) {
            $usedBB = min($y, $x + 1);
            $usedAA = $x;
        } else {
            $usedAA = $x;
            $usedBB = $y;
        }
        return 2 * ($z + $usedAA + $usedBB);
    }
}
```

## Swift

```swift
class Solution {
    func longestString(_ x: Int, _ y: Int, _ z: Int) -> Int {
        let minXY = min(x, y)
        if x == y {
            return 4 * x + 2 * z
        } else {
            return 4 * minXY + 2 + 2 * z
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestString(x: Int, y: Int, z: Int): Int {
        val common = kotlin.math.min(x, y)
        var ans = 2 * z + 4 * common
        if (x != y) ans += 2
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int longestString(int x, int y, int z) {
    int ans = 2 * z;
    int m = x < y ? x : y;
    ans += 4 * m;
    if (x != y) ans += 2;
    return ans;
  }
}
```

## Golang

```go
func longestString(x int, y int, z int) int {
	usedA, usedB := 0, 0
	if x > y {
		if x < y+1 {
			usedA = x
		} else {
			usedA = y + 1
		}
		usedB = y
	} else if y > x {
		if y < x+1 {
			usedB = y
		} else {
			usedB = x + 1
		}
		usedA = x
	} else { // x == y
		usedA = x
		usedB = y
	}
	return 2*z + 2*(usedA+usedB)
}
```

## Ruby

```ruby
def longest_string(x, y, z)
  if x == y
    4 * x + 2 * z
  else
    m = [x, y].min
    4 * m + 2 + 2 * z
  end
end
```

## Scala

```scala
object Solution {
    def longestString(x: Int, y: Int, z: Int): Int = {
        val a = Math.min(x, y)
        var usedA = a
        var usedB = a
        if (x > y) usedA += 1
        else if (y > x) usedB += 1
        2 * z + 2 * usedA + 2 * usedB
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_string(x: i32, y: i32, z: i32) -> i32 {
        let used_doubles = if x > y {
            2 * y + 1
        } else if y > x {
            2 * x + 1
        } else {
            2 * x
        };
        2 * z + 2 * used_doubles
    }
}
```

## Racket

```racket
(define/contract (longest-string x y z)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ([minxy (if (< x y) x y)]
         [extra (if (= x y) 0 2)])
    (+ (* 2 z) (* 4 minxy) extra)))
```

## Erlang

```erlang
-spec longest_string(integer(), integer(), integer()) -> integer().
longest_string(X, Y, Z) ->
    AA = erlang:min(X, Y + 1),
    BB = erlang:min(Y, X + 1),
    (AA + BB + Z) * 2.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_string(x :: integer, y :: integer, z :: integer) :: integer
  def longest_string(x, y, z) do
    m = min(x, y)
    extra = if x != y, do: 1, else: 0
    total_strings = z + 2 * m + extra
    total_strings * 2
  end
end
```

# 0201. Bitwise AND of Numbers Range

## Cpp

```cpp
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int shift = 0;
        while (left < right) {
            left >>= 1;
            right >>= 1;
            ++shift;
        }
        return left << shift;
    }
};
```

## Java

```java
class Solution {
    public int rangeBitwiseAnd(int left, int right) {
        int shift = 0;
        while (left < right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        return left << shift;
    }
}
```

## Python

```python
class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
```

## Python3

```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
```

## C

```c
int rangeBitwiseAnd(int left, int right) {
    int shift = 0;
    while (left < right) {
        left >>= 1;
        right >>= 1;
        ++shift;
    }
    return left << shift;
}
```

## Csharp

```csharp
public class Solution {
    public int RangeBitwiseAnd(int left, int right) {
        int shift = 0;
        while (left < right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        return left << shift;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var rangeBitwiseAnd = function(left, right) {
    let shift = 0;
    while (left < right) {
        left >>>= 1;
        right >>>= 1;
        ++shift;
    }
    return left << shift;
};
```

## Typescript

```typescript
function rangeBitwiseAnd(left: number, right: number): number {
    let shift = 0;
    while (left !== right) {
        left >>>= 1;
        right >>>= 1;
        shift++;
    }
    return left << shift;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function rangeBitwiseAnd($left, $right) {
        $shift = 0;
        while ($left != $right) {
            $left >>= 1;
            $right >>= 1;
            $shift++;
        }
        return $left << $shift;
    }
}
```

## Swift

```swift
class Solution {
    func rangeBitwiseAnd(_ left: Int, _ right: Int) -> Int {
        var l = left
        var r = right
        var shift = 0
        while l != r {
            l >>= 1
            r >>= 1
            shift += 1
        }
        return l << shift
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rangeBitwiseAnd(left: Int, right: Int): Int {
        var l = left
        var r = right
        var shift = 0
        while (l != r) {
            l = l ushr 1
            r = r ushr 1
            shift++
        }
        return l shl shift
    }
}
```

## Dart

```dart
class Solution {
  int rangeBitwiseAnd(int left, int right) {
    int shift = 0;
    while (left < right) {
      left >>= 1;
      right >>= 1;
      shift++;
    }
    return left << shift;
  }
}
```

## Golang

```go
func rangeBitwiseAnd(left int, right int) int {
	shift := 0
	for left < right {
		left >>= 1
		right >>= 1
		shift++
	}
	return left << shift
}
```

## Ruby

```ruby
def range_bitwise_and(left, right)
  shift = 0
  while left < right
    left >>= 1
    right >>= 1
    shift += 1
  end
  left << shift
end
```

## Scala

```scala
object Solution {
    def rangeBitwiseAnd(left: Int, right: Int): Int = {
        var l = left
        var r = right
        var shift = 0
        while (l < r) {
            l >>= 1
            r >>= 1
            shift += 1
        }
        l << shift
    }
}
```

## Rust

```rust
impl Solution {
    pub fn range_bitwise_and(left: i32, right: i32) -> i32 {
        let mut l = left as u32;
        let mut r = right as u32;
        let mut shift = 0;
        while l != r {
            l >>= 1;
            r >>= 1;
            shift += 1;
        }
        (l << shift) as i32
    }
}
```

## Racket

```racket
(define/contract (range-bitwise-and left right)
  (-> exact-integer? exact-integer? exact-integer?)
  (let loop ((l left) (r right) (shift 0))
    (if (= l r)
        (arithmetic-shift l shift)
        (loop (arithmetic-shift l -1)
              (arithmetic-shift r -1)
              (+ shift 1)))))
```

## Erlang

```erlang
-spec range_bitwise_and(Left :: integer(), Right :: integer()) -> integer().
range_bitwise_and(Left, Right) ->
    range_bitwise_and(Left, Right, 0).

range_bitwise_and(L, R, Shift) when L =:= R ->
    L bsl Shift;
range_bitwise_and(L, R, Shift) ->
    range_bitwise_and(L bsr 1, R bsr 1, Shift + 1).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec range_bitwise_and(left :: integer, right :: integer) :: integer
  def range_bitwise_and(left, right) do
    do_range_bitwise_and(left, right, 0)
  end

  defp do_range_bitwise_and(l, r, shift) when l != r do
    do_range_bitwise_and(bsr(l, 1), bsr(r, 1), shift + 1)
  end

  defp do_range_bitwise_and(l, _r, shift) do
    shiftl(l, shift)
  end
end
```

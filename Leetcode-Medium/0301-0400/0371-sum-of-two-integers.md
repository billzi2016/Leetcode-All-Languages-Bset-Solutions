# 0371. Sum of Two Integers

## Cpp

```cpp
class Solution {
public:
    int getSum(int a, int b) {
        unsigned int ua = static_cast<unsigned int>(a);
        unsigned int ub = static_cast<unsigned int>(b);
        while (ub != 0) {
            unsigned int carry = (ua & ub) << 1;
            ua ^= ub;
            ub = carry;
        }
        return static_cast<int>(ua);
    }
};
```

## Java

```java
class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a ^= b;
            b = carry;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0xffffffff
        MAX_INT = 0x7fffffff
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK
        return a if a <= MAX_INT else ~(a ^ MASK)
```

## Python3

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK
        return a if a <= MAX_INT else ~(a ^ MASK)
```

## C

```c
int getSum(int a, int b) {
    while (b != 0) {
        unsigned int carry = ((unsigned int)(a & b)) << 1;
        a ^= b;
        b = (int)carry;
    }
    return a;
}
```

## Csharp

```csharp
public class Solution
{
    public int GetSum(int a, int b)
    {
        while (b != 0)
        {
            int carry = (a & b) << 1;
            a ^= b;
            b = carry;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
    while (b !== 0) {
        const carry = a & b;
        a = a ^ b;
        b = carry << 1;
    }
    return a;
};
```

## Typescript

```typescript
function getSum(a: number, b: number): number {
    while (b !== 0) {
        const carry = (a & b) << 1;
        a = a ^ b;
        b = carry;
    }
    return a;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @return Integer
     */
    function getSum($a, $b) {
        while ($b != 0) {
            $carry = ($a & $b) << 1;
            $a ^= $b;
            $b = $carry;
        }
        return $a;
    }
}
```

## Swift

```swift
class Solution {
    func getSum(_ a: Int, _ b: Int) -> Int {
        var x = a
        var y = b
        while y != 0 {
            let carry = (x & y) << 1
            x = x ^ y
            y = carry
        }
        return x
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getSum(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val carry = x and y
            x = x xor y
            y = carry shl 1
        }
        return x
    }
}
```

## Dart

```dart
class Solution {
  int getSum(int a, int b) {
    const int mask = 0xffffffff;
    const int maxInt = 0x7fffffff;
    while ((b & mask) != 0) {
      int carry = (a & b) << 1;
      a = (a ^ b) & mask;
      b = carry & mask;
    }
    return a > maxInt ? ~(a ^ mask) : a;
  }
}
```

## Golang

```go
func getSum(a int, b int) int {
	var x uint32 = uint32(a)
	var y uint32 = uint32(b)
	for y != 0 {
		carry := (x & y) << 1
		x ^= y
		y = carry
	}
	return int(int32(x))
}
```

## Ruby

```ruby
def get_sum(a, b)
  mask = 0xffffffff
  while b != 0
    carry = (a & b) << 1
    a = (a ^ b) & mask
    b = carry & mask
  end
  a > 0x7fffffff ? a - 0x100000000 : a
end
```

## Scala

```scala
object Solution {
    def getSum(a: Int, b: Int): Int = {
        var x = a
        var y = b
        while (y != 0) {
            val carry = x & y
            x = x ^ y
            y = carry << 1
        }
        x
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_sum(mut a: i32, mut b: i32) -> i32 {
        while b != 0 {
            let carry = (a & b) << 1;
            a ^= b;
            b = carry;
        }
        a
    }
}
```

## Racket

```racket
(define/contract (get-sum a b)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ((MASK #xffffffff)
         (MAX-INT #x7fffffff))
    (let loop ((a (bitwise-and a MASK)) (b (bitwise-and b MASK)))
      (if (= b 0)
          (let ((res a))
            (if (> res MAX-INT)
                (- res (arithmetic-shift 1 32))
                res))
          (let* ((carry (bitwise-and a b))
                 (new-a (bitwise-xor a b))
                 (new-b (arithmetic-shift carry 1)))
            (loop (bitwise-and new-a MASK) (bitwise-and new-b MASK)))))))
```

## Erlang

```erlang
-spec get_sum(A :: integer(), B :: integer()) -> integer().
get_sum(A, B) ->
    Mask = 16#FFFFFFFF,
    Sum = sum_loop(A band Mask, B band Mask, Mask),
    case Sum > 16#7FFFFFFF of
        true -> Sum - 16#100000000;
        false -> Sum
    end.

sum_loop(A, 0, _Mask) ->
    A;
sum_loop(A, B, Mask) ->
    Carry = (A band B) band Mask,
    NewA = (A bxor B) band Mask,
    NewB = (Carry bsl 1) band Mask,
    sum_loop(NewA, NewB, Mask).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec get_sum(a :: integer, b :: integer) :: integer
  def get_sum(a, b) do
    mask = 0xFFFFFFFF
    max_int = 0x7FFFFFFF

    result = add(a &&& mask, b &&& mask, mask)

    if result <= max_int do
      result
    else
      Bitwise.bnot(Bitwise.bxor(result, mask))
    end
  end

  defp add(x, 0, _mask), do: x

  defp add(x, y, mask) do
    carry = Bitwise.band(x, y)
    sum = Bitwise.bxor(x, y)
    add(sum &&& mask, Bitwise.shift_left(carry, 1) &&& mask, mask)
  end
end
```

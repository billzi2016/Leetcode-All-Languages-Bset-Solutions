# 0190. Reverse Bits

## Cpp

```cpp
class Solution {
public:
    int reverseBits(int n) {
        uint32_t x = static_cast<uint32_t>(n);
        uint32_t rev = 0;
        for (int i = 0; i < 32; ++i) {
            rev = (rev << 1) | (x & 1u);
            x >>= 1;
        }
        return static_cast<int>(rev);
    }
};
```

## Java

```java
class Solution {
    public int reverseBits(int n) {
        int rev = 0;
        for (int i = 0; i < 32; i++) {
            rev <<= 1;
            rev |= (n & 1);
            n >>>= 1;
        }
        return rev;
    }
}
```

## Python

```python
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        rev = 0
        for _ in range(32):
            rev = (rev << 1) | (n & 1)
            n >>= 1
        return rev
```

## Python3

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for _ in range(32):
            rev = (rev << 1) | (n & 1)
            n >>= 1
        return rev
```

## C

```c
int reverseBits(int n) {
    unsigned int x = (unsigned int)n;
    x = ((x >> 1) & 0x55555555U) | ((x & 0x55555555U) << 1);
    x = ((x >> 2) & 0x33333333U) | ((x & 0x33333333U) << 2);
    x = ((x >> 4) & 0x0F0F0F0FU) | ((x & 0x0F0F0F0FU) << 4);
    x = ((x >> 8) & 0x00FF00FFU) | ((x & 0x00FF00FFU) << 8);
    x = (x >> 16) | (x << 16);
    return (int)x;
}
```

## Csharp

```csharp
public class Solution {
    public int ReverseBits(int n) {
        uint x = (uint)n;
        uint rev = 0;
        for (int i = 0; i < 32; i++) {
            rev = (rev << 1) | (x & 1);
            x >>= 1;
        }
        return (int)rev;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var reverseBits = function(n) {
    let rev = 0;
    for (let i = 0; i < 32; i++) {
        rev = (rev << 1) | (n & 1);
        n >>>= 1;
    }
    return rev >>> 0;
};
```

## Typescript

```typescript
function reverseBits(n: number): number {
    let rev = 0;
    for (let i = 0; i < 32; i++) {
        rev = (rev << 1) | (n & 1);
        n >>>= 1;
    }
    return rev >>> 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function reverseBits($n) {
        $rev = 0;
        for ($i = 0; $i < 32; $i++) {
            $rev = ($rev << 1) | ($n & 1);
            $n >>= 1;
        }
        // Ensure unsigned 32-bit result
        return $rev & 0xFFFFFFFF;
    }
}
```

## Swift

```swift
class Solution {
    func reverseBits(_ n: Int) -> Int {
        var x = UInt32(n)
        var result: UInt32 = 0
        for _ in 0..<32 {
            result <<= 1
            result |= (x & 1)
            x >>= 1
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reverseBits(n: Int): Int {
        var rev = 0
        var num = n
        repeat(32) {
            rev = rev shl 1
            rev = rev or (num and 1)
            num = num ushr 1
        }
        return rev
    }
}
```

## Dart

```dart
class Solution {
  int reverseBits(int n) {
    int rev = 0;
    for (int i = 0; i < 32; i++) {
      rev = (rev << 1) | (n & 1);
      n = n >>> 1;
    }
    return rev & 0xFFFFFFFF;
  }
}
```

## Golang

```go
func reverseBits(n int) int {
    var rev uint32 = 0
    x := uint32(n)
    for i := 0; i < 32; i++ {
        rev <<= 1
        rev |= x & 1
        x >>= 1
    }
    return int(rev)
}
```

## Ruby

```ruby
def reverse_bits(n)
  rev = 0
  32.times do
    rev = (rev << 1) | (n & 1)
    n >>= 1
  end
  rev
end
```

## Scala

```scala
object Solution {
    def reverseBits(n: Int): Int = {
        var rev = 0
        var x = n
        for (_ <- 0 until 32) {
            rev = (rev << 1) | (x & 1)
            x = x >>> 1
        }
        rev
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reverse_bits(n: i32) -> i32 {
        (n as u32).reverse_bits() as i32
    }
}
```

## Racket

```racket
(require racket/bitwise)

(define/contract (reverse-bits n)
  (-> exact-integer? exact-integer?)
  (let loop ((i 0) (src n) (rev 0))
    (if (= i 32)
        rev
        (loop (+ i 1)
              (arithmetic-shift src -1)
              (bitwise-ior (arithmetic-shift rev 1)
                           (bitwise-and src 1))))))
```

## Erlang

```erlang
-spec reverse_bits(N :: integer()) -> integer().
reverse_bits(N) ->
    reverse_bits(N, 0, 32).

reverse_bits(_, Acc, 0) ->
    Acc;
reverse_bits(N, Acc, Count) ->
    Bit = N band 1,
    NewAcc = (Acc bsl 1) bor Bit,
    NewN = N bsr 1,
    reverse_bits(NewN, NewAcc, Count - 1).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec reverse_bits(n :: integer) :: integer
  def reverse_bits(n) do
    Enum.reduce(0..31, {n, 0}, fn _, {num, rev} ->
      rev = (rev <<< 1) ||| (num &&& 1)
      num = num >>> 1
      {num, rev}
    end)
    |> elem(1)
  end
end
```

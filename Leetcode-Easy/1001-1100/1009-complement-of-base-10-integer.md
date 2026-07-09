# 1009. Complement of Base 10 Integer

## Cpp

```cpp
class Solution {
public:
    int bitwiseComplement(int n) {
        if (n == 0) return 1;
        int mask = 0;
        int temp = n;
        while (temp) {
            mask = (mask << 1) | 1;
            temp >>= 1;
        }
        return n ^ mask;
    }
};
```

## Java

```java
class Solution {
    public int bitwiseComplement(int n) {
        if (n == 0) return 1;
        int mask = 0;
        while (mask < n) {
            mask = (mask << 1) | 1;
        }
        return mask ^ n;
    }
}
```

## Python

```python
class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        mask = (1 << n.bit_length()) - 1
        return mask ^ n
```

## Python3

```python
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        mask = (1 << n.bit_length()) - 1
        return mask ^ n
```

## C

```c
int bitwiseComplement(int n) {
    if (n == 0) return 1;
    int mask = 0, t = n;
    while (t) {
        mask = (mask << 1) | 1;
        t >>= 1;
    }
    return (~n) & mask;
}
```

## Csharp

```csharp
public class Solution {
    public int BitwiseComplement(int n) {
        if (n == 0) return 1;
        int mask = 0, t = n;
        while (t > 0) {
            mask = (mask << 1) | 1;
            t >>= 1;
        }
        return n ^ mask;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var bitwiseComplement = function(n) {
    if (n === 0) return 1;
    let mask = 1;
    while (mask <= n) {
        mask <<= 1;
    }
    mask -= 1;
    return n ^ mask;
};
```

## Typescript

```typescript
function bitwiseComplement(n: number): number {
    if (n === 0) return 1;
    let mask = 0;
    while (mask < n) {
        mask = (mask << 1) | 1;
    }
    return mask ^ n;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function bitwiseComplement($n) {
        if ($n == 0) {
            return 1;
        }
        $mask = 1;
        while ($mask <= $n) {
            $mask <<= 1;
        }
        $mask -= 1;
        return $mask ^ $n;
    }
}
```

## Swift

```swift
class Solution {
    func bitwiseComplement(_ n: Int) -> Int {
        if n == 0 { return 1 }
        var mask = 0
        var temp = n
        while temp > 0 {
            mask = (mask << 1) | 1
            temp >>= 1
        }
        return (~n) & mask
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun bitwiseComplement(n: Int): Int {
        if (n == 0) return 1
        val msb = Integer.highestOneBit(n)
        val mask = (msb shl 1) - 1
        return n xor mask
    }
}
```

## Dart

```dart
class Solution {
  int bitwiseComplement(int n) {
    if (n == 0) return 1;
    int mask = (1 << n.bitLength) - 1;
    return n ^ mask;
  }
}
```

## Golang

```go
func bitwiseComplement(n int) int {
	if n == 0 {
		return 1
	}
	mask := 1
	for mask <= n {
		mask <<= 1
	}
	return (^n) & (mask - 1)
}
```

## Ruby

```ruby
def bitwise_complement(n)
  return 1 if n == 0
  bits = n.bit_length
  mask = (1 << bits) - 1
  mask ^ n
end
```

## Scala

```scala
object Solution {
    def bitwiseComplement(n: Int): Int = {
        if (n == 0) 1
        else {
            val mask = (Integer.highestOneBit(n) << 1) - 1
            mask ^ n
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn bitwise_complement(n: i32) -> i32 {
        if n == 0 {
            return 1;
        }
        let mut mask = 0i32;
        let mut temp = n;
        while temp > 0 {
            mask = (mask << 1) | 1;
            temp >>= 1;
        }
        (!n) & mask
    }
}
```

## Racket

```racket
(define/contract (bitwise-complement n)
  (-> exact-integer? exact-integer?)
  (if (= n 0)
      1
      (let loop ((mask 1))
        (if (> mask n)
            (bitwise-xor n (- mask 1))
            (loop (* mask 2))))))
```

## Erlang

```erlang
-spec bitwise_complement(N :: integer()) -> integer().
bitwise_complement(0) ->
    1;
bitwise_complement(N) when N > 0 ->
    Mask = make_mask(N, 0),
    bxor(N, Mask).

make_mask(0, Acc) ->
    Acc;
make_mask(N, Acc) ->
    make_mask(N bsr 1, (Acc bsl 1) bor 1).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec bitwise_complement(n :: integer) :: integer
  def bitwise_complement(0), do: 1

  def bitwise_complement(n) when n > 0 do
    bits = :math.log2(n) |> trunc() + 1
    mask = (1 <<< bits) - 1
    mask ^^^ n
  end
end
```

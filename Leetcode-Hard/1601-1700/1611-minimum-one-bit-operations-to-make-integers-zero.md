# 1611. Minimum One Bit Operations to Make Integers Zero

## Cpp

```cpp
class Solution {
public:
    int minimumOneBitOperations(int n) {
        int ans = n;
        for (int shift = 1; shift < 32; shift <<= 1) {
            ans ^= ans >> shift;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumOneBitOperations(int n) {
        int ans = n;
        for (int shift = n >> 1; shift > 0; shift >>= 1) {
            ans ^= shift;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = n
        x = n
        while x:
            x >>= 1
            ans ^= x
        return ans
```

## Python3

```python
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = n
        shift = n >> 1
        while shift:
            ans ^= shift
            shift >>= 1
        return ans
```

## C

```c
int minimumOneBitOperations(int n) {
    int ans = n;
    while (n > 0) {
        n >>= 1;
        ans ^= n;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumOneBitOperations(int n)
    {
        int ans = n;
        while (n > 0)
        {
            n >>= 1;
            ans ^= n;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var minimumOneBitOperations = function(n) {
    let ans = n;
    while (n > 0) {
        n >>= 1;
        ans ^= n;
    }
    return ans;
};
```

## Typescript

```typescript
function minimumOneBitOperations(n: number): number {
    let ans = n;
    while (n > 0) {
        n = n >>> 1;
        ans ^= n;
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function minimumOneBitOperations($n) {
        $ans = $n;
        while ($n > 0) {
            $n >>= 1;
            $ans ^= $n;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumOneBitOperations(_ n: Int) -> Int {
        var ans = n
        ans ^= ans >> 16
        ans ^= ans >> 8
        ans ^= ans >> 4
        ans ^= ans >> 2
        ans ^= ans >> 1
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumOneBitOperations(n: Int): Int {
        var ans = n
        ans = ans xor (ans ushr 1)
        ans = ans xor (ans ushr 2)
        ans = ans xor (ans ushr 4)
        ans = ans xor (ans ushr 8)
        ans = ans xor (ans ushr 16)
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minimumOneBitOperations(int n) {
    int ans = n;
    while (n > 0) {
      n >>= 1;
      ans ^= n;
    }
    return ans;
  }
}
```

## Golang

```go
func minimumOneBitOperations(n int) int {
    ans := n
    for shift := 1; shift < 32; shift <<= 1 {
        ans ^= ans >> shift
    }
    return ans
}
```

## Ruby

```ruby
def minimum_one_bit_operations(n)
  ans = n
  shift = n >> 1
  while shift > 0
    ans ^= shift
    shift >>= 1
  end
  ans
end
```

## Scala

```scala
object Solution {
    def minimumOneBitOperations(n: Int): Int = {
        var ans = n
        ans ^= ans >>> 1
        ans ^= ans >>> 2
        ans ^= ans >>> 4
        ans ^= ans >>> 8
        ans ^= ans >>> 16
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_one_bit_operations(n: i32) -> i32 {
        let mut ans = n as u32;
        ans ^= ans >> 16;
        ans ^= ans >> 8;
        ans ^= ans >> 4;
        ans ^= ans >> 2;
        ans ^= ans >> 1;
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-one-bit-operations n)
  (-> exact-integer? exact-integer?)
  (let loop ((m n) (ans n))
    (if (= m 0)
        ans
        (let ((next (arithmetic-shift m -1)))
          (loop next (bitwise-xor ans next))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_one_bit_operations/1]).

-spec minimum_one_bit_operations(N :: integer()) -> integer().
minimum_one_bit_operations(N) ->
    G1 = N bxor (N bsr 16),
    G2 = G1 bxor (G1 bsr 8),
    G3 = G2 bxor (G2 bsr 4),
    G4 = G3 bxor (G3 bsr 2),
    G5 = G4 bxor (G4 bsr 1),
    G5.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_one_bit_operations(n :: integer) :: integer
  def minimum_one_bit_operations(n) do
    compute(n, n)
  end

  defp compute(0, acc), do: acc
  defp compute(x, acc) do
    x = x >>> 1
    compute(x, acc ^^^ x)
  end
end
```

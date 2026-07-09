# 3133. Minimum Array End

## Cpp

```cpp
class Solution {
public:
    long long minEnd(int n, int x) {
        long long ans = x;
        long long v = (long long)n - 1; // number of increments needed
        int pos = 0;
        while (v > 0) {
            // skip positions where ans already has a set bit
            while ((ans >> pos) & 1LL) ++pos;
            // place current lowest bit of v into this zero position
            if (v & 1LL) ans |= (1LL << pos);
            v >>= 1;
            ++pos;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long minEnd(int n, int x) {
        long need = (long) n - 1L; // number of increments needed
        long result = x;
        int pos = 0;
        while (need > 0) {
            // skip positions where x already has a 1
            while (((result >> pos) & 1L) == 1L) {
                pos++;
            }
            // place the lowest bit of need into this zero position
            if ((need & 1L) == 1L) {
                result |= (1L << pos);
            }
            need >>= 1;
            pos++;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def minEnd(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        v = n - 1
        res = x
        bit = 1
        while v:
            if (x & bit) == 0:
                if v & 1:
                    res |= bit
                v >>= 1
            bit <<= 1
        return res
```

## Python3

```python
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # Number of increments needed beyond the first element
        need = n - 1
        res = x
        bit = 1
        while need:
            if (x & bit) == 0:
                if need & 1:
                    res |= bit
                need >>= 1
            bit <<= 1
        return res
```

## C

```c
#include <stdint.h>

long long minEnd(int n, int x) {
    long long result = (long long)x;
    long long need = (long long)n - 1;
    for (int i = 0; need > 0; ++i) {
        long long mask = 1LL << i;
        if ((x & mask) == 0) {
            if (need & 1LL) result |= mask;
            need >>= 1;
        }
    }
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public long MinEnd(int n, int x)
    {
        long ans = x;
        long k = (long)n - 1;
        int pos = 0;
        while (k > 0)
        {
            if ((((long)x >> pos) & 1L) == 0)
            {
                if ((k & 1L) == 1L)
                    ans |= (1L << pos);
                k >>= 1;
            }
            pos++;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} x
 * @return {number}
 */
var minEnd = function(n, x) {
    let result = x;
    let need = n - 1; // number of increments to distribute into zero bits of x
    for (let bit = 0; need > 0; ++bit) {
        if ((x & (1 << bit)) === 0) {          // this position is free in x
            if (need & 1) {
                result |= (1 << bit);         // take the lowest remaining bit from need
            }
            need >>= 1;                        // move to next bit of need
        }
    }
    return result;
};
```

## Typescript

```typescript
function minEnd(n: number, x: number): number {
    let remaining = BigInt(n - 1);
    const base = BigInt(x);
    let result = base;
    let bitPos = 0n;

    while (remaining > 0n) {
        const mask = 1n << bitPos;
        if ((base & mask) === 0n) {
            if ((remaining & 1n) === 1n) {
                result |= mask;
            }
            remaining >>= 1n;
        }
        bitPos++;
    }

    return Number(result);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $x
     * @return Integer
     */
    function minEnd($n, $x) {
        $m = $n - 1;          // number of increments needed
        $res = $x;
        $pos = 0;
        while ($m > 0) {
            if ((($x >> $pos) & 1) == 0) {   // free bit in x
                if (($m & 1) == 1) {
                    $res |= (1 << $pos);
                }
                $m >>= 1;
            }
            $pos++;
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func minEnd(_ n: Int, _ x: Int) -> Int {
        var remaining = Int64(n - 1)
        var result = Int64(x)
        let xx = Int64(x)
        var mask: Int64 = 1
        while remaining > 0 {
            if (xx & mask) == 0 {
                if (remaining & 1) == 1 {
                    result |= mask
                }
                remaining >>= 1
            }
            mask <<= 1
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minEnd(n: Int, x: Int): Long {
        var result = x.toLong()
        var need = (n - 1).toLong()
        val xLong = x.toLong()
        var bit = 0
        while (need > 0) {
            // skip positions where x already has a set bit
            while (((xLong shr bit) and 1L) == 1L) {
                bit++
            }
            if ((need and 1L) == 1L) {
                result = result or (1L shl bit)
            }
            need = need shr 1
            bit++
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int minEnd(int n, int x) {
    int need = n - 1;
    int result = x;
    int mask = 1;
    while (need > 0) {
      if ((x & mask) == 0) {
        if ((need & 1) == 1) {
          result |= mask;
        }
        need >>= 1;
      }
      mask <<= 1;
    }
    return result;
  }
}
```

## Golang

```go
func minEnd(n int, x int) int64 {
    ans := int64(x)
    v := int64(n - 1)

    for i := 0; v > 0; i++ {
        if (ans>>i)&1 == 0 {
            if v&1 == 1 {
                ans |= 1 << i
            }
            v >>= 1
        }
    }
    return ans
}
```

## Ruby

```ruby
def min_end(n, x)
  v = n - 1
  ans = x
  bit = 1
  while v > 0
    if (x & bit) == 0
      ans |= bit if (v & 1) == 1
      v >>= 1
    end
    bit <<= 1
  end
  ans
end
```

## Scala

```scala
object Solution {
  def minEnd(n: Int, x: Int): Long = {
    var res: Long = x.toLong
    var k: Long = (n - 1).toLong
    var pos = 0
    while (k > 0) {
      if ((x & (1L << pos)) == 0) {
        if ((k & 1L) == 1L) {
          res |= (1L << pos)
        }
        k >>= 1
      }
      pos += 1
    }
    res
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_end(n: i32, x: i32) -> i64 {
        let mut ans: i64 = x as i64;
        let mut k: u64 = (n - 1) as u64;
        let mut pos: u32 = 0;
        while k > 0 {
            if ((x as u64) >> pos) & 1 == 0 {
                ans |= ((k & 1) << pos) as i64;
                k >>= 1;
            }
            pos += 1;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-end n x)
  (-> exact-integer? exact-integer? exact-integer?)
  (let ((m (- n 1)))
    (let loop ((i 0) (rem m) (res x))
      (if (= rem 0)
          res
          (if (= (bitwise-and (arithmetic-shift x (- i)) 1) 1)
              (loop (+ i 1) rem res)
              (let* ((bit (bitwise-and rem 1))
                     (new-res (if (= bit 1)
                                 (bitwise-ior res (arithmetic-shift 1 i))
                                 res)))
                (loop (+ i 1) (arithmetic-shift rem -1) new-res)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_end/2]).

-spec min_end(integer(), integer()) -> integer().
min_end(N, X) ->
    K = N - 1,
    loop(K, X, 0, X).

loop(0, Res, _Pos, _X) ->
    Res;
loop(K, Res, Pos, X) ->
    case (X bsr Pos) band 1 of
        1 ->
            loop(K, Res, Pos + 1, X);
        0 ->
            Bit = K band 1,
            NewRes = if Bit =:= 1 -> Res bor (1 bsl Pos); true -> Res end,
            NewK = K bsr 1,
            loop(NewK, NewRes, Pos + 1, X)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec min_end(n :: integer, x :: integer) :: integer
  def min_end(n, x) do
    merge(x, n - 1, x, 1)
  end

  defp merge(_x, 0, res, _mask), do: res

  defp merge(x, rem, res, mask) do
    if band(x, mask) == 0 do
      new_res = if band(rem, 1) == 1, do: bor(res, mask), else: res
      merge(x, bsr(rem, 1), new_res, mask <<< 1)
    else
      merge(x, rem, res, mask <<< 1)
    end
  end
end
```

# 1529. Minimum Suffix Flips

## Cpp

```cpp
class Solution {
public:
    int minFlips(string target) {
        int flips = 0;
        int cur = 0; // current bit after applied suffix flips
        for (char c : target) {
            int t = c - '0';
            if (t != cur) {
                ++flips;
                cur ^= 1;
            }
        }
        return flips;
    }
};
```

## Java

```java
class Solution {
    public int minFlips(String target) {
        int flips = 0;
        int cur = 0; // current effective bit after previous suffix flips
        for (int i = 0; i < target.length(); i++) {
            int desired = target.charAt(i) - '0';
            if (desired != cur) {
                flips++;
                cur ^= 1;
            }
        }
        return flips;
    }
}
```

## Python

```python
class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        flips = 0
        cur = '0'
        for ch in target:
            if ch != cur:
                flips += 1
                cur = '1' if cur == '0' else '0'
        return flips
```

## Python3

```python
class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        prev = '0'
        for ch in target:
            if ch != prev:
                flips += 1
                prev = ch
        return flips
```

## C

```c
int minFlips(char* target) {
    int flips = 0;
    char prev = '0';
    for (int i = 0; target[i] != '\0'; ++i) {
        if (target[i] != prev) {
            ++flips;
            prev = target[i];
        }
    }
    return flips;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinFlips(string target)
    {
        char prev = '0';
        int flips = 0;
        foreach (char c in target)
        {
            if (c != prev)
            {
                flips++;
                prev = c;
            }
        }
        return flips;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} target
 * @return {number}
 */
var minFlips = function(target) {
    let flips = 0;
    let cur = 0; // current bit value after applied suffix flips
    for (let i = 0; i < target.length; ++i) {
        const desired = target.charCodeAt(i) - 48; // '0' -> 0, '1' -> 1
        if (desired !== cur) {
            flips++;
            cur ^= 1;
        }
    }
    return flips;
};
```

## Typescript

```typescript
function minFlips(target: string): number {
    let flips = 0;
    let cur = '0';
    for (let i = 0; i < target.length; ++i) {
        if (target[i] !== cur) {
            ++flips;
            cur = cur === '0' ? '1' : '0';
        }
    }
    return flips;
}
```

## Php

```php
class Solution {

    /**
     * @param String $target
     * @return Integer
     */
    function minFlips($target) {
        $flips = 0;
        $parity = 0; // 0 means no flip effect, 1 means bits are inverted
        $n = strlen($target);
        for ($i = 0; $i < $n; $i++) {
            $bit = intval($target[$i]); // current target bit as integer 0 or 1
            $effective = $bit ^ $parity;
            if ($effective === 1) {
                $flips++;
                $parity ^= 1; // toggle inversion state
            }
        }
        return $flips;
    }
}
```

## Swift

```swift
class Solution {
    func minFlips(_ target: String) -> Int {
        var flips = 0
        var current: Character = "0"
        for ch in target {
            if ch != current {
                flips += 1
                current = ch
            }
        }
        return flips
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minFlips(target: String): Int {
        var flips = 0
        var parity = 0 // 0 means even number of flips applied so far
        for (c in target) {
            val current = if (parity == 0) '0' else '1'
            if (current != c) {
                flips++
                parity = parity xor 1
            }
        }
        return flips
    }
}
```

## Dart

```dart
class Solution {
  int minFlips(String target) {
    int flips = 0;
    int parity = 0; // 0 means no inversion, 1 means bits are inverted
    for (int i = 0; i < target.length; i++) {
      int bit = target.codeUnitAt(i) - 48; // '0' -> 0, '1' -> 1
      if ((bit ^ parity) == 1) {
        flips++;
        parity ^= 1;
      }
    }
    return flips;
  }
}
```

## Golang

```go
func minFlips(target string) int {
    flips, parity := 0, 0
    for i := 0; i < len(target); i++ {
        expected := byte('0')
        if parity == 1 {
            expected = '1'
        }
        if target[i] != expected {
            flips++
            parity ^= 1
        }
    }
    return flips
}
```

## Ruby

```ruby
def min_flips(target)
  flips = 0
  parity = 0
  target.each_byte do |b|
    bit = b - 48
    if bit != parity
      flips += 1
      parity ^= 1
    end
  end
  flips
end
```

## Scala

```scala
object Solution {
    def minFlips(target: String): Int = {
        var flips = 0
        var parity = 0 // 0 means current bits are as original zeros, 1 means flipped
        val n = target.length
        var i = 0
        while (i < n) {
            val curBit = if (parity == 0) '0' else '1'
            if (target.charAt(i) != curBit) {
                flips += 1
                parity ^= 1
            }
            i += 1
        }
        flips
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_flips(target: String) -> i32 {
        let mut flips = 0usize;
        for ch in target.chars() {
            let current = if flips % 2 == 0 { '0' } else { '1' };
            if current != ch {
                flips += 1;
            }
        }
        flips as i32
    }
}
```

## Racket

```racket
(define/contract (min-flips target)
  (-> string? exact-integer?)
  (let loop ((i 0) (parity 0) (cnt 0))
    (if (= i (string-length target))
        cnt
        (let ((c (string-ref target i)))
          (if (char=? c (if (= parity 0) #\0 #\1))
              (loop (+ i 1) parity cnt)
              (loop (+ i 1) (if (= parity 0) 1 0) (+ cnt 1)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_flips/1]).

-spec min_flips(unicode:unicode_binary()) -> integer().
min_flips(Target) ->
    min_flips_binary(Target, $0, 0).

min_flips_binary(<<>>, _Cur, Count) ->
    Count;
min_flips_binary(<<Char:8, Rest/binary>>, Cur, Count) ->
    if Char =:= Cur ->
            min_flips_binary(Rest, Cur, Count);
       true ->
            NewCur = case Cur of
                        $0 -> $1;
                        $1 -> $0
                     end,
            min_flips_binary(Rest, NewCur, Count + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_flips(target :: String.t()) :: integer()
  def min_flips(target) do
    do_min_flips(target, 0, 0)
  end

  defp do_min_flips(<<>>, _parity, ans), do: ans

  defp do_min_flips(<<c, rest::binary>>, parity, ans) do
    expected = if parity == 0, do: ?0, else: ?1

    if c != expected do
      do_min_flips(rest, 1 - parity, ans + 1)
    else
      do_min_flips(rest, parity, ans)
    end
  end
end
```

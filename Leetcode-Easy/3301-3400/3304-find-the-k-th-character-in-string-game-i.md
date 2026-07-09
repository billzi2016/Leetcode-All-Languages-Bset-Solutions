# 3304. Find the K-th Character in String Game I

## Cpp

```cpp
class Solution {
public:
    char kthCharacter(int k) {
        int cnt = __builtin_popcount(k - 1);
        return 'a' + (cnt % 26);
    }
};
```

## Java

```java
class Solution {
    public char kthCharacter(int k) {
        int offset = Integer.bitCount(k - 1) % 26;
        return (char) ('a' + offset);
    }
}
```

## Python

```python
class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        cnt = bin(k - 1).count('1')
        return chr(ord('a') + (cnt % 26))
```

## Python3

```python
class Solution:
    def kthCharacter(self, k: int) -> str:
        inc = (k - 1).bit_count()
        return chr((inc % 26) + ord('a'))
```

## C

```c
char kthCharacter(int k) {
    int cnt = 0;
    int x = k - 1;
    while (x) {
        cnt += x & 1;
        x >>= 1;
    }
    cnt %= 26;
    return (char)('a' + cnt);
}
```

## Csharp

```csharp
public class Solution
{
    public char KthCharacter(int k)
    {
        int count = 0;
        int x = k - 1;
        while (x > 0)
        {
            count += x & 1;
            x >>= 1;
        }
        count %= 26;
        return (char)('a' + count);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} k
 * @return {character}
 */
var kthCharacter = function(k) {
    let cnt = 0;
    let x = k - 1;
    while (x > 0) {
        cnt += x & 1;
        x >>>= 1;
    }
    const code = 'a'.charCodeAt(0) + (cnt % 26);
    return String.fromCharCode(code);
};
```

## Typescript

```typescript
function kthCharacter(k: number): string {
    let cnt = 0;
    let x = k - 1;
    while (x > 0) {
        cnt += x & 1;
        x >>= 1;
    }
    const charCode = 'a'.charCodeAt(0) + (cnt % 26);
    return String.fromCharCode(charCode);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $k
     * @return String
     */
    function kthCharacter($k) {
        $steps = 0;
        $x = $k - 1;
        while ($x > 0) {
            $steps += $x & 1;
            $x >>= 1;
        }
        return chr((ord('a') + $steps) % 26);
    }
}
```

## Swift

```swift
class Solution {
    func kthCharacter(_ k: Int) -> Character {
        var n = k - 1
        var cnt = 0
        while n > 0 {
            cnt += n & 1
            n >>= 1
        }
        let offset = cnt % 26
        let base = Int(("a" as UnicodeScalar).value)
        let ascii = base + offset
        return Character(UnicodeScalar(ascii)!)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kthCharacter(k: Int): Char {
        var pos = k
        var len = 1
        while (len < pos) {
            len = len shl 1
        }
        var offset = 0
        while (len > 1) {
            val half = len shr 1
            if (pos > half) {
                pos -= half
                offset++
            }
            len = half
        }
        offset %= 26
        return ('a'.code + offset).toChar()
    }
}
```

## Dart

```dart
class Solution {
  String kthCharacter(int k) {
    int n = k - 1;
    int cnt = 0;
    while (n > 0) {
      cnt += n & 1;
      n >>= 1;
    }
    int chCode = 'a'.codeUnitAt(0) + (cnt % 26);
    return String.fromCharCode(chCode);
  }
}
```

## Golang

```go
import "math/bits"

func kthCharacter(k int) byte {
	cnt := bits.OnesCount(uint(k - 1))
	return byte('a' + cnt%26)
}
```

## Ruby

```ruby
def kth_character(k)
  cnt = (k - 1).to_s(2).count('1')
  ((?a.ord + cnt) % 26 + ?a.ord).chr
end
```

## Scala

```scala
object Solution {
    def kthCharacter(k: Int): Char = {
        val steps = Integer.bitCount(k - 1)
        ((('a'.toInt + steps) % 26) + 'a'.toInt).toChar
    }
}
```

## Rust

```rust
impl Solution {
    pub fn kth_character(k: i32) -> char {
        let cnt = (k - 1).count_ones();
        let shift = (cnt % 26) as u8;
        (b'a' + shift) as char
    }
}
```

## Racket

```racket
(require racket/bitwise)

(define/contract (kth-character k)
  (-> exact-integer? char?)
  (let* ((n (- k 1))
         (cnt (bitwise-bit-count n)))
    (integer->char (+ (char->integer #\a) (modulo cnt 26)))))
```

## Erlang

```erlang
-spec kth_character(K :: integer()) -> char().
kth_character(K) ->
    Count = bit_count(K - 1),
    $a + Count.

bit_count(0) -> 0;
bit_count(N) -> (N band 1) + bit_count(N bsr 1).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec kth_character(k :: integer) :: char
  def kth_character(k) do
    shifts = popcount(k - 1)
    ?a + rem(shifts, 26)
  end

  defp popcount(0), do: 0
  defp popcount(n) do
    (n &&& 1) + popcount(n >>> 1)
  end
end
```

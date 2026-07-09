# 3498. Reverse Degree of a String

## Cpp

```cpp
class Solution {
public:
    int reverseDegree(string s) {
        long long total = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            int origPos = s[i] - 'a' + 1;          // 1..26
            int revVal = 27 - origPos;             // reverse alphabetical value
            total += 1LL * revVal * (i + 1);
        }
        return (int)total;
    }
};
```

## Java

```java
class Solution {
    public int reverseDegree(String s) {
        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            int reverseIdx = 'z' - s.charAt(i) + 1;
            total += (i + 1) * reverseIdx;
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i, ch in enumerate(s, 1):  # i starts from 1
            rev_val = ord('z') - ord(ch) + 1
            total += rev_val * i
        return total
```

## Python3

```python
class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s):
            val = ord(ch) - ord('a') + 1          # alphabetical position (1-26)
            rev_val = 27 - val                    # reverse alphabetical value
            total += (i + 1) * rev_val
        return total
```

## C

```c
int reverseDegree(char* s) {
    long long total = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        int val = s[i] - 'a' + 1;          // alphabet position (1-26)
        int revPos = 27 - val;             // reverse position
        total += (long long)revPos * (i + 1);
    }
    return (int)total;
}
```

## Csharp

```csharp
public class Solution {
    public int ReverseDegree(string s) {
        int total = 0;
        for (int i = 0; i < s.Length; i++) {
            int originalPos = s[i] - 'a' + 1;          // 1 to 26
            int reversePos = 27 - originalPos;        // reversed position
            total += reversePos * (i + 1);
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var reverseDegree = function(s) {
    let total = 0;
    const base = 'z'.charCodeAt(0);
    for (let i = 0; i < s.length; i++) {
        const revPos = base - s.charCodeAt(i) + 1; // reverse alphabetical position
        total += revPos * (i + 1);
    }
    return total;
};
```

## Typescript

```typescript
function reverseDegree(s: string): number {
    let total = 0;
    for (let i = 0; i < s.length; i++) {
        const pos = s.charCodeAt(i) - 96; // 'a' -> 1, ..., 'z' -> 26
        const revPos = 27 - pos;          // reverse alphabet position
        total += revPos * (i + 1);
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function reverseDegree($s) {
        $len = strlen($s);
        $total = 0;
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            $revPos = ord('z') - ord($c) + 1;
            $total += $revPos * ($i + 1);
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func reverseDegree(_ s: String) -> Int {
        var total = 0
        var index = 1
        let aValue = UnicodeScalar("a").value
        for scalar in s.unicodeScalars {
            let pos = Int(scalar.value - aValue) + 1          // alphabetical position (1..26)
            let revPos = 27 - pos                              // reverse alphabetical position
            total += revPos * index
            index += 1
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reverseDegree(s: String): Int {
        var total = 0
        for ((idx, ch) in s.withIndex()) {
            val revVal = 'z' - ch + 1
            total += (idx + 1) * revVal
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int reverseDegree(String s) {
    int total = 0;
    const int aCode = 97; // 'a'
    const int zCode = 122; // 'z'
    for (int i = 0; i < s.length; ++i) {
      int revPos = zCode - s.codeUnitAt(i) + 1;
      total += revPos * (i + 1);
    }
    return total;
  }
}
```

## Golang

```go
func reverseDegree(s string) int {
    total := 0
    for i, ch := range s {
        revPos := int('z'-ch+1)
        total += (i + 1) * revPos
    }
    return total
}
```

## Ruby

```ruby
def reverse_degree(s)
  total = 0
  s.each_char.with_index(1) do |ch, i|
    rev = ('z'.ord - ch.ord) + 1
    total += i * rev
  end
  total
end
```

## Scala

```scala
object Solution {
    def reverseDegree(s: String): Int = {
        var total = 0
        for (i <- s.indices) {
            val revPos = 'z' - s.charAt(i) + 1
            total += revPos * (i + 1)
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reverse_degree(s: String) -> i32 {
        let mut total: i32 = 0;
        for (i, ch) in s.bytes().enumerate() {
            let rev = (b'z' - ch + 1) as i32;
            total += rev * ((i as i32) + 1);
        }
        total
    }
}
```

## Racket

```racket
(define/contract (reverse-degree s)
  (-> string? exact-integer?)
  (let ([len (string-length s)])
    (let loop ((i 0) (acc 0))
      (if (= i len)
          acc
          (let* ([ch (string-ref s i)]
                 [pos (+ (- (char->integer ch) (char->integer #\a)) 1)]
                 [revPos (- 27 pos)]
                 [factor (+ i 1)])
            (loop (+ i 1) (+ acc (* revPos factor))))))))
```

## Erlang

```erlang
-spec reverse_degree(S :: unicode:unicode_binary()) -> integer().
reverse_degree(S) ->
    reverse_degree(S, 1, 0).

reverse_degree(<<>>, _Pos, Acc) ->
    Acc;
reverse_degree(<<Char, Rest/binary>>, Pos, Acc) ->
    Index = Char - $a + 1,
    Rev = 27 - Index,
    NewAcc = Acc + Rev * Pos,
    reverse_degree(Rest, Pos + 1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec reverse_degree(s :: String.t()) :: integer()
  def reverse_degree(s) do
    s
    |> String.to_charlist()
    |> Enum.with_index()
    |> Enum.reduce(0, fn {c, i}, acc ->
      pos = c - ?a + 1
      rev = 27 - pos
      acc + (i + 1) * rev
    end)
  end
end
```

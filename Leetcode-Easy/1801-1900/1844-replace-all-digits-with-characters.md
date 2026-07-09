# 1844. Replace All Digits with Characters

## Cpp

```cpp
class Solution {
public:
    string replaceDigits(string s) {
        int n = s.size();
        for (int i = 1; i < n; i += 2) {
            char prev = s[i - 1];
            int shift = s[i] - '0';
            s[i] = static_cast<char>(prev + shift);
        }
        return s;
    }
};
```

## Java

```java
class Solution {
    public String replaceDigits(String s) {
        char[] chars = s.toCharArray();
        for (int i = 1; i < chars.length; i += 2) {
            int shift = chars[i] - '0';
            chars[i] = (char) (chars[i - 1] + shift);
        }
        return new String(chars);
    }
}
```

## Python

```python
class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        for i in range(1, len(chars), 2):
            shift = int(chars[i])
            chars[i] = chr(ord(chars[i-1]) + shift)
        return "".join(chars)
```

## Python3

```python
class Solution:
    def replaceDigits(self, s: str) -> str:
        chars = list(s)
        for i in range(1, len(chars), 2):
            shift = int(chars[i])
            chars[i] = chr(ord(chars[i - 1]) + shift)
        return "".join(chars)
```

## C

```c
#include <string.h>

char* replaceDigits(char* s) {
    for (int i = 1; s[i] != '\0'; i += 2) {
        int shift = s[i] - '0';
        s[i] = s[i - 1] + shift;
    }
    return s;
}
```

## Csharp

```csharp
public class Solution
{
    public string ReplaceDigits(string s)
    {
        char[] chars = s.ToCharArray();
        for (int i = 1; i < chars.Length; i += 2)
        {
            int shift = chars[i] - '0';
            chars[i] = (char)(chars[i - 1] + shift);
        }
        return new string(chars);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var replaceDigits = function(s) {
    const chars = s.split('');
    for (let i = 1; i < chars.length; i += 2) {
        const prevCharCode = chars[i - 1].charCodeAt(0);
        const shift = Number(chars[i]);
        chars[i] = String.fromCharCode(prevCharCode + shift);
    }
    return chars.join('');
};
```

## Typescript

```typescript
function replaceDigits(s: string): string {
    const chars = s.split('');
    for (let i = 1; i < chars.length; i += 2) {
        const shift = chars[i].charCodeAt(0) - 48;
        const base = chars[i - 1].charCodeAt(0);
        chars[i] = String.fromCharCode(base + shift);
    }
    return chars.join('');
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return String
     */
    function replaceDigits($s) {
        $chars = str_split($s);
        $n = count($chars);
        for ($i = 1; $i < $n; $i += 2) {
            $prev = $chars[$i - 1];
            $digit = intval($chars[$i]);
            $chars[$i] = chr(ord($prev) + $digit);
        }
        return implode('', $chars);
    }
}
```

## Swift

```swift
class Solution {
    func replaceDigits(_ s: String) -> String {
        var chars = Array(s)
        for i in stride(from: 1, to: chars.count, by: 2) {
            let prevChar = chars[i - 1]
            guard let prevAscii = prevChar.asciiValue,
                  let digit = Int(String(chars[i])) else { continue }
            let newAscii = prevAscii + UInt8(digit)
            chars[i] = Character(UnicodeScalar(newAscii))
        }
        return String(chars)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun replaceDigits(s: String): String {
        val chars = s.toCharArray()
        var i = 1
        while (i < chars.size) {
            val prev = chars[i - 1]
            val shift = chars[i] - '0'
            chars[i] = ((prev - 'a' + shift) % 26 + 'a'.code).toChar()
            i += 2
        }
        return String(chars)
    }
}
```

## Dart

```dart
class Solution {
  String replaceDigits(String s) {
    var sb = StringBuffer();
    for (int i = 0; i < s.length; i++) {
      if (i % 2 == 0) {
        sb.write(s[i]);
      } else {
        int prevCode = s.codeUnitAt(i - 1);
        int shift = s.codeUnitAt(i) - '0'.codeUnitAt(0);
        sb.write(String.fromCharCode(prevCode + shift));
      }
    }
    return sb.toString();
  }
}
```

## Golang

```go
func replaceDigits(s string) string {
    b := []byte(s)
    for i := 1; i < len(b); i += 2 {
        shift := b[i] - '0'
        b[i] = b[i-1] + shift
    }
    return string(b)
}
```

## Ruby

```ruby
def replace_digits(s)
  chars = s.chars
  (1...chars.length).step(2) do |i|
    shift = chars[i].ord - '0'.ord
    prev = chars[i - 1]
    chars[i] = (prev.ord + shift).chr
  end
  chars.join
end
```

## Scala

```scala
object Solution {
    def replaceDigits(s: String): String = {
        val sb = new StringBuilder
        var i = 0
        while (i < s.length) {
            if (i % 2 == 0) {
                sb.append(s.charAt(i))
            } else {
                val prevChar = sb.charAt(sb.length - 1)
                val shift = s.charAt(i).asDigit
                val newChar = (prevChar + shift).toChar
                sb.append(newChar)
            }
            i += 1
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn replace_digits(s: String) -> String {
        let mut bytes = s.into_bytes();
        for i in (1..bytes.len()).step_by(2) {
            let shift = (bytes[i] - b'0') as u8;
            bytes[i] = bytes[i - 1] + shift;
        }
        unsafe { String::from_utf8_unchecked(bytes) }
    }
}
```

## Racket

```racket
(define/contract (replace-digits s)
  (-> string? string?)
  (let* ([len (string-length s)]
         [vec (make-vector len)])
    (for ([i (in-range len)])
      (if (odd? i)
          (let* ([prev (vector-ref vec (- i 1))]
                 [digit-char (string-ref s i)]
                 [offset (- (char->integer digit-char) (char->integer #\0))]
                 [new-char (integer->char (+ (char->integer prev) offset))])
            (vector-set! vec i new-char))
          (vector-set! vec i (string-ref s i))))
    (list->string (vector->list vec))))
```

## Erlang

```erlang
-module(solution).
-export([replace_digits/1]).

-spec replace_digits(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
replace_digits(S) ->
    L = binary_to_list(S),
    RevRes = replace(L, []),
    list_to_binary(lists:reverse(RevRes)).

replace([], Acc) -> Acc;
replace([C], Acc) -> [C | Acc];
replace([Prev, DigitChar | Rest], Acc) when DigitChar >= $0, DigitChar =< $9 ->
    Shifted = Prev + (DigitChar - $0),
    replace(Rest, [Shifted, Prev | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec replace_digits(s :: String.t) :: String.t
  def replace_digits(s) do
    chars = String.to_charlist(s)

    new_chars =
      Enum.with_index(chars)
      |> Enum.map(fn {c, i} ->
        if rem(i, 2) == 1 do
          prev = Enum.at(chars, i - 1)
          shift = c - ?0
          prev + shift
        else
          c
        end
      end)

    List.to_string(new_chars)
  end
end
```

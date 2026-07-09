# 0709. To Lower Case

## Cpp

```cpp
class Solution {
public:
    string toLowerCase(string s) {
        for (char &c : s) {
            if (c >= 'A' && c <= 'Z') {
                c = c + ('a' - 'A');
            }
        }
        return s;
    }
};
```

## Java

```java
class Solution {
    public String toLowerCase(String s) {
        StringBuilder sb = new StringBuilder(s.length());
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'A' && c <= 'Z') {
                c = (char)(c + ('a' - 'A'));
            }
            sb.append(c);
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Convert each character using ASCII manipulation for uppercase letters
        result = []
        for ch in s:
            ascii_code = ord(ch)
            if 65 <= ascii_code <= 90:  # 'A' to 'Z'
                ascii_code += 32  # convert to lowercase
            result.append(chr(ascii_code))
        return ''.join(result)
```

## Python3

```python
class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []
        for ch in s:
            o = ord(ch)
            if 65 <= o <= 90:  # 'A' to 'Z'
                o += 32
            res.append(chr(o))
        return ''.join(res)
```

## C

```c
char* toLowerCase(char* s) {
    if (!s) return NULL;
    for (int i = 0; s[i] != '\0'; ++i) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            s[i] += ('a' - 'A');
        }
    }
    return s;
}
```

## Csharp

```csharp
public class Solution {
    public string ToLowerCase(string s) {
        var sb = new System.Text.StringBuilder(s.Length);
        foreach (char c in s) {
            if (c >= 'A' && c <= 'Z')
                sb.Append((char)(c + ('a' - 'A')));
            else
                sb.Append(c);
        }
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var toLowerCase = function(s) {
    let result = '';
    for (let i = 0; i < s.length; i++) {
        const code = s.charCodeAt(i);
        if (code >= 65 && code <= 90) {
            result += String.fromCharCode(code + 32);
        } else {
            result += s[i];
        }
    }
    return result;
};
```

## Typescript

```typescript
function toLowerCase(s: string): string {
    const n = s.length;
    let result = '';
    for (let i = 0; i < n; i++) {
        const code = s.charCodeAt(i);
        if (code >= 65 && code <= 90) { // 'A' to 'Z'
            result += String.fromCharCode(code + 32);
        } else {
            result += s[i];
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function toLowerCase($s) {
        $len = strlen($s);
        $result = '';
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            $code = ord($ch);
            if ($code >= 65 && $code <= 90) { // 'A' to 'Z'
                $ch = chr($code + 32); // convert to lowercase
            }
            $result .= $ch;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func toLowerCase(_ s: String) -> String {
        return s.lowercased()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun toLowerCase(s: String): String {
        val chars = s.toCharArray()
        for (i in chars.indices) {
            val c = chars[i]
            if (c >= 'A' && c <= 'Z') {
                chars[i] = (c.code + 32).toChar()
            }
        }
        return String(chars)
    }
}
```

## Dart

```dart
class Solution {
  String toLowerCase(String s) {
    final buffer = StringBuffer();
    for (int i = 0; i < s.length; i++) {
      int code = s.codeUnitAt(i);
      if (code >= 65 && code <= 90) {
        code += 32;
      }
      buffer.writeCharCode(code);
    }
    return buffer.toString();
  }
}
```

## Golang

```go
func toLowerCase(s string) string {
	b := []byte(s)
	for i, c := range b {
		if c >= 'A' && c <= 'Z' {
			b[i] = c + ('a' - 'A')
		}
	}
	return string(b)
}
```

## Ruby

```ruby
# @param {String} s
# @return {String}
def to_lower_case(s)
  result = []
  s.each_byte do |b|
    if b >= 65 && b <= 90 # 'A'..'Z'
      result << (b + 32).chr
    else
      result << b.chr
    end
  end
  result.join
end
```

## Scala

```scala
object Solution {
    def toLowerCase(s: String): String = {
        val sb = new StringBuilder(s.length)
        for (ch <- s) {
            if (ch >= 'A' && ch <= 'Z')
                sb.append((ch + 32).toChar)
            else
                sb.append(ch)
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn to_lower_case(s: String) -> String {
        let lower_bytes: Vec<u8> = s
            .into_bytes()
            .into_iter()
            .map(|b| if b >= b'A' && b <= b'Z' { b + 32 } else { b })
            .collect();
        unsafe { String::from_utf8_unchecked(lower_bytes) }
    }
}
```

## Racket

```racket
(define/contract (to-lower-case s)
  (-> string? string?)
  (let* ([chars (string->list s)]
         [lowered (map (lambda (c)
                         (if (and (char>=? c #\A) (char<=? c #\Z))
                             (integer->char (+ (char->integer c) 32))
                             c))
                       chars)])
    (list->string lowered)))
```

## Erlang

```erlang
-spec to_lower_case(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
to_lower_case(S) ->
    << (if C >= $A, C =< $Z -> C + 32; true -> C end) || <<C>> <= S >>.
```

## Elixir

```elixir
defmodule Solution do
  @spec to_lower_case(s :: String.t()) :: String.t()
  def to_lower_case(s) do
    s
    |> String.to_charlist()
    |> Enum.map(fn c ->
      if c >= ?A and c <= ?Z, do: c + 32, else: c
    end)
    |> List.to_string()
  end
end
```

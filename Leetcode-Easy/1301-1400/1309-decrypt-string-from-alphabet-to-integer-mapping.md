# 1309. Decrypt String from Alphabet to Integer Mapping

## Cpp

```cpp
class Solution {
public:
    string freqAlphabets(string s) {
        string res;
        for (int i = (int)s.size() - 1; i >= 0; ) {
            if (s[i] == '#') {
                int num = (s[i-2] - '0') * 10 + (s[i-1] - '0');
                res.push_back('a' + num - 1);
                i -= 3;
            } else {
                int num = s[i] - '0';
                res.push_back('a' + num - 1);
                --i;
            }
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

## Java

```java
class Solution {
    public String freqAlphabets(String s) {
        StringBuilder sb = new StringBuilder();
        int i = s.length() - 1;
        while (i >= 0) {
            if (s.charAt(i) == '#') {
                int num = Integer.parseInt(s.substring(i - 2, i));
                sb.append((char) ('a' + num - 1));
                i -= 3;
            } else {
                int num = s.charAt(i) - '0';
                sb.append((char) ('a' + num - 1));
                i--;
            }
        }
        return sb.reverse().toString();
    }
}
```

## Python

```python
class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])
                res.append(chr(ord('a') + num - 1))
                i -= 3
            else:
                num = int(s[i])
                res.append(chr(ord('a') + num - 1))
                i -= 1
        return ''.join(reversed(res))
```

## Python3

```python
class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])
                res.append(chr(ord('a') + num - 1))
                i -= 3
            else:
                num = int(s[i])
                res.append(chr(ord('a') + num - 1))
                i -= 1
        return ''.join(reversed(res))
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* freqAlphabets(char* s) {
    int n = strlen(s);
    char *res = (char*)malloc(n + 1);
    int idx = 0;
    for (int i = 0; i < n;) {
        if (i + 2 < n && s[i + 2] == '#') {
            int num = (s[i] - '0') * 10 + (s[i + 1] - '0');
            res[idx++] = 'a' + num - 1;
            i += 3;
        } else {
            int num = s[i] - '0';
            res[idx++] = 'a' + num - 1;
            i++;
        }
    }
    res[idx] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string FreqAlphabets(string s) {
        var sb = new System.Text.StringBuilder();
        for (int i = s.Length - 1; i >= 0;) {
            if (s[i] == '#') {
                int num = (s[i - 2] - '0') * 10 + (s[i - 1] - '0');
                sb.Append((char)('a' + num - 1));
                i -= 3;
            } else {
                int num = s[i] - '0';
                sb.Append((char)('a' + num - 1));
                i--;
            }
        }
        var arr = sb.ToString().ToCharArray();
        System.Array.Reverse(arr);
        return new string(arr);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var freqAlphabets = function(s) {
    const result = [];
    for (let i = s.length - 1; i >= 0;) {
        if (s[i] === '#') {
            const num = parseInt(s.slice(i - 2, i));
            result.push(String.fromCharCode(96 + num));
            i -= 3;
        } else {
            const num = parseInt(s[i]);
            result.push(String.fromCharCode(96 + num));
            i--;
        }
    }
    return result.reverse().join('');
};
```

## Typescript

```typescript
function freqAlphabets(s: string): string {
    const result: string[] = [];
    for (let i = s.length - 1; i >= 0;) {
        if (s[i] === '#') {
            const num = parseInt(s.substring(i - 2, i));
            result.push(String.fromCharCode(96 + num));
            i -= 3;
        } else {
            const num = parseInt(s[i]);
            result.push(String.fromCharCode(96 + num));
            i--;
        }
    }
    return result.reverse().join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function freqAlphabets($s) {
        $n = strlen($s);
        $res = '';
        for ($i = $n - 1; $i >= 0;) {
            if ($s[$i] === '#') {
                $num = intval(substr($s, $i - 2, 2));
                $res .= chr(ord('a') + $num - 1);
                $i -= 3;
            } else {
                $num = intval($s[$i]);
                $res .= chr(ord('a') + $num - 1);
                $i--;
            }
        }
        return strrev($res);
    }
}
```

## Swift

```swift
class Solution {
    func freqAlphabets(_ s: String) -> String {
        let chars = Array(s)
        var i = chars.count - 1
        var result = [Character]()
        while i >= 0 {
            if chars[i] == "#" {
                let tens = Int(String(chars[i - 2]))!
                let ones = Int(String(chars[i - 1]))!
                let num = tens * 10 + ones
                let ch = Character(UnicodeScalar(UInt32(num + 96))!)
                result.append(ch)
                i -= 3
            } else {
                let num = Int(String(chars[i]))!
                let ch = Character(UnicodeScalar(UInt32(num + 96))!)
                result.append(ch)
                i -= 1
            }
        }
        return String(result.reversed())
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun freqAlphabets(s: String): String {
        val sb = StringBuilder()
        var i = s.length - 1
        while (i >= 0) {
            if (s[i] == '#') {
                val num = (s[i - 2] - '0') * 10 + (s[i - 1] - '0')
                sb.append(('a'.code + num - 1).toChar())
                i -= 3
            } else {
                val num = s[i] - '0'
                sb.append(('a'.code + num - 1).toChar())
                i--
            }
        }
        return sb.reverse().toString()
    }
}
```

## Dart

```dart
class Solution {
  String freqAlphabets(String s) {
    int i = s.length - 1;
    List<int> codes = [];
    while (i >= 0) {
      if (s[i] == '#') {
        int num = int.parse(s.substring(i - 2, i));
        codes.add(num + 96);
        i -= 3;
      } else {
        int num = s.codeUnitAt(i) - 48; // '0' ascii is 48
        codes.add(num + 96);
        i--;
      }
    }
    StringBuffer sb = StringBuffer();
    for (int j = codes.length - 1; j >= 0; --j) {
      sb.writeCharCode(codes[j]);
    }
    return sb.toString();
  }
}
```

## Golang

```go
func freqAlphabets(s string) string {
	n := len(s)
	res := make([]byte, 0, n)
	for i := n - 1; i >= 0; {
		if s[i] == '#' {
			num := int(s[i-2]-'0')*10 + int(s[i-1]-'0')
			res = append(res, byte('a'+num-1))
			i -= 3
		} else {
			num := int(s[i] - '0')
			res = append(res, byte('a'+num-1))
			i--
		}
	}
	for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}
	return string(res)
}
```

## Ruby

```ruby
def freq_alphabets(s)
  res = []
  i = s.length - 1
  while i >= 0
    if s[i] == '#'
      num = s[i - 2, 2].to_i
      res << (('a'.ord + num - 1).chr)
      i -= 3
    else
      num = s[i].to_i
      res << (('a'.ord + num - 1).chr)
      i -= 1
    end
  end
  res.reverse.join
end
```

## Scala

```scala
object Solution {
    def freqAlphabets(s: String): String = {
        val sb = new StringBuilder
        var i = s.length - 1
        while (i >= 0) {
            if (s(i) == '#') {
                val num = (s(i - 2) - '0') * 10 + (s(i - 1) - '0')
                sb.append(('a' + num - 1).toChar)
                i -= 3
            } else {
                val num = s(i) - '0'
                sb.append(('a' + num - 1).toChar)
                i -= 1
            }
        }
        sb.reverse.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn freq_alphabets(s: String) -> String {
        let bytes = s.as_bytes();
        let mut i: i32 = (bytes.len() as i32) - 1;
        let mut chars: Vec<char> = Vec::new();

        while i >= 0 {
            if bytes[i as usize] == b'#' {
                // take the two digits before '#'
                let tens = bytes[(i - 2) as usize] - b'0';
                let ones = bytes[(i - 1) as usize] - b'0';
                let num = tens * 10 + ones;
                chars.push((b'a' + num - 1) as char);
                i -= 3;
            } else {
                let num = bytes[i as usize] - b'0';
                chars.push((b'a' + num - 1) as char);
                i -= 1;
            }
        }

        chars.iter().rev().collect()
    }
}
```

## Racket

```racket
(define/contract (freq-alphabets s)
  (-> string? string?)
  (let loop ((i (- (string-length s) 1)) (acc '()))
    (if (< i 0)
        (list->string (reverse acc))
        (let ((ch (string-ref s i)))
          (if (char=? ch #\#)
              (let* ((d1 (string-ref s (- i 2))) ; tens digit
                     (d2 (string-ref s (- i 1))) ; ones digit
                     (num (+ (* 10 (- (char->integer d1) (char->integer #\0)))
                             (- (char->integer d2) (char->integer #\0)))))
                (loop (- i 3)
                      (cons (integer->char (+ num (char->integer #\a) -1)) acc)))
              (let* ((num (- (char->integer ch) (char->integer #\0)))
                     (c   (integer->char (+ num (char->integer #\a) -1))))
                (loop (- i 1)
                      (cons c acc))))))))
```

## Erlang

```erlang
-module(solution).
-export([freq_alphabets/1]).
-spec freq_alphabets(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
freq_alphabets(S) ->
    Rev = lists:reverse(binary_to_list(S)),
    Decoded = decode_rev(Rev, []),
    list_to_binary(Decoded).

decode_rev([], Acc) -> Acc;
decode_rev([C|Rest], Acc) when C == $# ->
    [D1, D2 | Rest2] = Rest,
    Num = (D2 - $0) * 10 + (D1 - $0),
    Char = $a + Num - 1,
    decode_rev(Rest2, [Char|Acc]);
decode_rev([C|Rest], Acc) ->
    Num = C - $0,
    Char = $a + Num - 1,
    decode_rev(Rest, [Char|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec freq_alphabets(s :: String.t()) :: String.t()
  def freq_alphabets(s) do
    s
    |> String.to_charlist()
    |> Enum.reverse()
    |> decode_rev([])
  end

  defp decode_rev([], acc), do: :lists.reverse(acc) |> IO.iodata_to_binary()

  # pattern for a '#', followed by two digits (the original number)
  defp decode_rev([?#, d2, d1 | rest], acc) when d1 in ?0..?9 and d2 in ?0..?9 do
    num = (d1 - ?0) * 10 + (d2 - ?0)
    char = <<(?a + num - 1)::utf8>>
    decode_rev(rest, [char | acc])
  end

  # pattern for a single digit mapping to a letter
  defp decode_rev([digit | rest], acc) when digit in ?0..?9 do
    num = digit - ?0
    char = <<(?a + num - 1)::utf8>>
    decode_rev(rest, [char | acc])
  end
end
```

# 1694. Reformat Phone Number

## Cpp

```cpp
class Solution {
public:
    string reformatNumber(string number) {
        string digits;
        for (char c : number) {
            if (isdigit(c)) digits.push_back(c);
        }
        vector<string> groups;
        int n = digits.size();
        int i = 0;
        while (i < n) {
            int remain = n - i;
            if (remain > 4) {
                groups.emplace_back(digits.substr(i, 3));
                i += 3;
            } else if (remain == 4) {
                groups.emplace_back(digits.substr(i, 2));
                groups.emplace_back(digits.substr(i + 2, 2));
                break;
            } else { // remain is 2 or 3
                groups.emplace_back(digits.substr(i, remain));
                break;
            }
        }
        string result;
        for (size_t j = 0; j < groups.size(); ++j) {
            if (j) result.push_back('-');
            result += groups[j];
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public String reformatNumber(String number) {
        StringBuilder digits = new StringBuilder();
        for (char c : number.toCharArray()) {
            if (Character.isDigit(c)) {
                digits.append(c);
            }
        }
        int n = digits.length();
        StringBuilder res = new StringBuilder();
        int i = 0;
        while (n - i > 4) {
            res.append(digits, i, i + 3).append('-');
            i += 3;
        }
        int remain = n - i;
        if (remain == 4) {
            res.append(digits, i, i + 2).append('-')
               .append(digits, i + 2, i + 4);
        } else {
            // remain is 2 or 3
            res.append(digits, i, n);
        }
        return res.toString();
    }
}
```

## Python

```python
class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        # Remove spaces and dashes
        digits = [c for c in number if c.isdigit()]
        s = ''.join(digits)
        groups = []
        i = 0
        n = len(s)
        while n - i > 0:
            remaining = n - i
            if remaining > 4:
                groups.append(s[i:i+3])
                i += 3
            elif remaining == 4:
                groups.append(s[i:i+2])
                groups.append(s[i+2:i+4])
                break
            else:  # 2 or 3 digits left
                groups.append(s[i:])
                break
        return '-'.join(groups)
```

## Python3

```python
class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = [c for c in number if c.isdigit()]
        n = len(digits)
        groups = []
        i = 0
        while n - i > 4:
            groups.append(''.join(digits[i:i+3]))
            i += 3
        remaining = n - i
        if remaining == 4:
            groups.append(''.join(digits[i:i+2]))
            groups.append(''.join(digits[i+2:i+4]))
        else:
            groups.append(''.join(digits[i:]))
        return '-'.join(groups)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* reformatNumber(char* number) {
    char digits[101];
    int n = 0;
    for (int i = 0; number[i] != '\0'; ++i) {
        if (number[i] >= '0' && number[i] <= '9') {
            digits[n++] = number[i];
        }
    }

    // Allocate enough space: max digits + possible dashes + null terminator
    int maxSize = n + n / 2 + 2;
    char *out = (char *)malloc(maxSize);
    if (!out) return NULL;

    int pos = 0;
    int i = 0;
    while (i < n) {
        int remain = n - i;
        int take;
        if (remain > 4) {
            take = 3;
        } else if (remain == 4) {
            take = 2;
        } else {
            take = remain; // 2 or 3
        }
        for (int k = 0; k < take; ++k) {
            out[pos++] = digits[i++];
        }
        if (i < n) {
            out[pos++] = '-';
        }
    }
    out[pos] = '\0';
    return out;
}
```

## Csharp

```csharp
public class Solution {
    public string ReformatNumber(string number) {
        // Remove spaces and dashes
        var digitsBuilder = new System.Text.StringBuilder();
        foreach (char c in number) {
            if (c >= '0' && c <= '9') {
                digitsBuilder.Append(c);
            }
        }
        string digits = digitsBuilder.ToString();
        int n = digits.Length;
        var parts = new System.Collections.Generic.List<string>();
        int i = 0;
        while (i < n) {
            int remain = n - i;
            if (remain == 4) {
                parts.Add(digits.Substring(i, 2));
                parts.Add(digits.Substring(i + 2, 2));
                break;
            } else if (remain >= 3) {
                parts.Add(digits.Substring(i, 3));
                i += 3;
            } else { // remain is 2
                parts.Add(digits.Substring(i, 2));
                break;
            }
        }
        return string.Join("-", parts);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} number
 * @return {string}
 */
var reformatNumber = function(number) {
    // Remove spaces and dashes, keep only digits
    const digits = number.replace(/[^0-9]/g, '');
    const parts = [];
    let i = 0;
    while (i < digits.length) {
        const remaining = digits.length - i;
        if (remaining > 4) {
            parts.push(digits.substr(i, 3));
            i += 3;
        } else if (remaining === 4) {
            parts.push(digits.substr(i, 2));
            parts.push(digits.substr(i + 2, 2));
            break;
        } else { // remaining is 2 or 3
            parts.push(digits.substr(i));
            break;
        }
    }
    return parts.join('-');
};
```

## Typescript

```typescript
function reformatNumber(number: string): string {
    const digits = number.replace(/[ -]/g, '');
    const parts: string[] = [];
    let i = 0;
    while (digits.length - i > 4) {
        parts.push(digits.substring(i, i + 3));
        i += 3;
    }
    const remaining = digits.length - i;
    if (remaining === 4) {
        parts.push(digits.substring(i, i + 2));
        parts.push(digits.substring(i + 2, i + 4));
    } else if (remaining > 0) {
        parts.push(digits.substring(i));
    }
    return parts.join('-');
}
```

## Php

```php
class Solution {

    /**
     * @param String $number
     * @return String
     */
    function reformatNumber($number) {
        // Remove all non-digit characters
        $digits = preg_replace('/\D/', '', $number);
        $n = strlen($digits);
        $i = 0;
        $blocks = [];

        while ($i < $n) {
            $remain = $n - $i;
            if ($remain > 4) {
                $blocks[] = substr($digits, $i, 3);
                $i += 3;
            } elseif ($remain == 4) {
                $blocks[] = substr($digits, $i, 2);
                $blocks[] = substr($digits, $i + 2, 2);
                break;
            } else { // remain is 2 or 3
                $blocks[] = substr($digits, $i);
                break;
            }
        }

        return implode('-', $blocks);
    }
}
```

## Swift

```swift
class Solution {
    func reformatNumber(_ number: String) -> String {
        // Remove spaces and dashes, keep only digits
        let digits = number.filter { $0.isNumber }
        let chars = Array(digits)
        var groups = [String]()
        var i = 0
        while i < chars.count {
            let remaining = chars.count - i
            if remaining > 4 {
                groups.append(String(chars[i..<i+3]))
                i += 3
            } else if remaining == 4 {
                groups.append(String(chars[i..<i+2]))
                groups.append(String(chars[i+2..<i+4]))
                break
            } else { // remaining is 2 or 3
                groups.append(String(chars[i..<chars.count]))
                break
            }
        }
        return groups.joined(separator: "-")
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reformatNumber(number: String): String {
        val digits = number.filter { it.isDigit() }
        val groups = mutableListOf<String>()
        var i = 0
        while (i < digits.length) {
            val remaining = digits.length - i
            when {
                remaining > 4 -> {
                    groups.add(digits.substring(i, i + 3))
                    i += 3
                }
                remaining == 4 -> {
                    groups.add(digits.substring(i, i + 2))
                    groups.add(digits.substring(i + 2, i + 4))
                    break
                }
                else -> { // 2 or 3 digits left
                    groups.add(digits.substring(i))
                    break
                }
            }
        }
        return groups.joinToString("-")
    }
}
```

## Dart

```dart
class Solution {
  String reformatNumber(String number) {
    // Remove spaces and dashes
    final cleaned = number.replaceAll(RegExp(r'[\s-]'), '');
    final parts = <String>[];
    int i = 0;
    while (cleaned.length - i > 4) {
      parts.add(cleaned.substring(i, i + 3));
      i += 3;
    }
    final remaining = cleaned.length - i;
    if (remaining == 4) {
      parts.add(cleaned.substring(i, i + 2));
      parts.add(cleaned.substring(i + 2, i + 4));
    } else if (remaining > 0) {
      parts.add(cleaned.substring(i));
    }
    return parts.join('-');
  }
}
```

## Golang

```go
import "strings"

func reformatNumber(number string) string {
    digits := make([]byte, 0, len(number))
    for i := 0; i < len(number); i++ {
        c := number[i]
        if c >= '0' && c <= '9' {
            digits = append(digits, c)
        }
    }

    var sb strings.Builder
    n := len(digits)
    i := 0
    for i < n {
        remaining := n - i
        var blockSize int
        if remaining > 4 {
            blockSize = 3
        } else if remaining == 4 {
            blockSize = 2
        } else {
            blockSize = remaining
        }
        sb.Write(digits[i : i+blockSize])
        i += blockSize
        if i < n {
            sb.WriteByte('-')
        }
    }
    return sb.String()
}
```

## Ruby

```ruby
def reformat_number(number)
  digits = number.delete(' -')
  parts = []
  i = 0
  while digits.length - i > 4
    parts << digits[i, 3]
    i += 3
  end
  remaining = digits.length - i
  if remaining == 4
    parts << digits[i, 2]
    parts << digits[i + 2, 2]
  else
    parts << digits[i, remaining] unless remaining.zero?
  end
  parts.join('-')
end
```

## Scala

```scala
object Solution {
    def reformatNumber(number: String): String = {
        val digits = number.filter(_.isDigit)
        val blocks = scala.collection.mutable.ListBuffer[String]()
        var i = 0
        val n = digits.length
        while (i < n) {
            val remaining = n - i
            if (remaining > 4) {
                blocks += digits.substring(i, i + 3)
                i += 3
            } else if (remaining == 4) {
                blocks += digits.substring(i, i + 2)
                blocks += digits.substring(i + 2, i + 4)
                i = n
            } else {
                blocks += digits.substring(i, n)
                i = n
            }
        }
        blocks.mkString("-")
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reformat_number(number: String) -> String {
        let digits: Vec<char> = number.chars().filter(|c| c.is_ascii_digit()).collect();
        let n = digits.len();
        let mut res = String::new();
        let mut i = 0;

        while i < n {
            let remaining = n - i;
            if remaining > 4 {
                for j in 0..3 {
                    res.push(digits[i + j]);
                }
                i += 3;
                res.push('-');
            } else {
                if remaining == 4 {
                    // two groups of 2
                    for j in 0..2 {
                        res.push(digits[i + j]);
                    }
                    res.push('-');
                    for j in 2..4 {
                        res.push(digits[i + j]);
                    }
                } else {
                    // remaining is 2 or 3
                    for j in 0..remaining {
                        res.push(digits[i + j]);
                    }
                }
                break;
            }
        }

        res
    }
}
```

## Racket

```racket
(define/contract (reformat-number number)
  (-> string? string?)
  (let* ((digits (list->string
                  (filter char-digit?
                          (string->list number))))
         (len (string-length digits)))
    (let loop ((i 0) (blocks '()))
      (let ((rem (- len i)))
        (cond
          [(= rem 0)
           (string-join (reverse blocks) "-")]
          [(> rem 4)
           (loop (+ i 3)
                 (cons (substring digits i (+ i 3)) blocks))]
          [(= rem 4)
           (let ((b1 (substring digits i (+ i 2)))
                 (b2 (substring digits (+ i 2) (+ i 4))))
             (string-join (reverse (cons b2 (cons b1 blocks))) "-"))]
          [else
           (let ((b (substring digits i len)))
             (string-join (reverse (cons b blocks)) "-"))])))))
```

## Erlang

```erlang
-module(solution).
-export([reformat_number/1]).

-spec reformat_number(Number :: unicode:unicode_binary()) -> unicode:unicode_binary().
reformat_number(Number) ->
    Digits = re:replace(Number, "[^0-9]", "", [{return,binary}, global]),
    Parts = format(Digits),
    binary:join(Parts, <<"-">>).

-spec format(binary()) -> [binary()].
format(Bin) when byte_size(Bin) > 4 ->
    <<Part:3/binary, Rest/binary>> = Bin,
    [Part | format(Rest)];
format(Bin) when byte_size(Bin) == 4 ->
    <<A:2/binary, B:2/binary>> = Bin,
    [A, B];
format(Bin) -> % size 2 or 3
    [Bin].
```

## Elixir

```elixir
defmodule Solution do
  @spec reformat_number(number :: String.t) :: String.t
  def reformat_number(number) do
    cleaned = String.replace(number, ~r/[\s-]/, "")
    format_blocks(cleaned, [])
  end

  defp format_blocks("", acc), do: Enum.reverse(acc) |> Enum.join("-")

  defp format_blocks(remaining, acc) do
    len = String.length(remaining)

    cond do
      len > 4 ->
        {block, rest} = String.split_at(remaining, 3)
        format_blocks(rest, [block | acc])

      len == 4 ->
        {first, second} = String.split_at(remaining, 2)
        Enum.reverse([second, first] ++ acc) |> Enum.join("-")

      true -> # len is 3 or 2
        Enum.reverse([remaining | acc]) |> Enum.join("-")
    end
  end
end
```

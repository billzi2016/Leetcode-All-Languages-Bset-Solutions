# 1881. Maximum Value after Insertion

## Cpp

```cpp
class Solution {
public:
    string maxValue(string n, int x) {
        char cx = '0' + x;
        if (n[0] != '-') {
            for (size_t i = 0; i < n.size(); ++i) {
                if (n[i] < cx) {
                    return n.substr(0, i) + cx + n.substr(i);
                }
            }
            return n + cx;
        } else {
            for (size_t i = 1; i < n.size(); ++i) {
                if (n[i] > cx) {
                    return n.substr(0, i) + cx + n.substr(i);
                }
            }
            return n + cx;
        }
    }
};
```

## Java

```java
class Solution {
    public String maxValue(String n, int x) {
        char xc = (char) ('0' + x);
        if (n.charAt(0) == '-') {
            StringBuilder sb = new StringBuilder();
            sb.append('-');
            boolean inserted = false;
            for (int i = 1; i < n.length(); i++) {
                char c = n.charAt(i);
                if (!inserted && c > xc) {
                    sb.append(xc);
                    inserted = true;
                }
                sb.append(c);
            }
            if (!inserted) {
                sb.append(xc);
            }
            return sb.toString();
        } else {
            StringBuilder sb = new StringBuilder();
            boolean inserted = false;
            for (int i = 0; i < n.length(); i++) {
                char c = n.charAt(i);
                if (!inserted && c < xc) {
                    sb.append(xc);
                    inserted = true;
                }
                sb.append(c);
            }
            if (!inserted) {
                sb.append(xc);
            }
            return sb.toString();
        }
    }
}
```

## Python

```python
class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        xs = str(x)
        if not n or n[0] != '-':
            # positive number
            for i, ch in enumerate(n):
                if int(ch) < x:
                    return n[:i] + xs + n[i:]
            return n + xs
        else:
            # negative number: minimize magnitude
            for i in range(1, len(n)):
                if int(n[i]) > x:
                    return n[:i] + xs + n[i:]
            return n + xs
```

## Python3

```python
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        xs = str(x)
        if n[0] != '-':
            for i, ch in enumerate(n):
                if ch < xs:
                    return n[:i] + xs + n[i:]
            return n + xs
        else:
            s = n[1:]  # digits after the minus sign
            for i, ch in enumerate(s):
                if ch > xs:
                    return '-' + s[:i] + xs + s[i:]
            return n + xs
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* maxValue(char* n, int x) {
    int len = strlen(n);
    char c = (char)('0' + x);
    int insertPos;
    
    if (n[0] != '-') { // positive number
        insertPos = 0;
        while (insertPos < len && n[insertPos] >= c) {
            insertPos++;
        }
    } else { // negative number
        insertPos = 1; // start after '-'
        while (insertPos < len && n[insertPos] <= c) {
            insertPos++;
        }
    }
    
    char* res = (char*)malloc(len + 2); // one extra char and null terminator
    int k = 0;
    for (int i = 0; i < insertPos; ++i) {
        res[k++] = n[i];
    }
    res[k++] = c;
    for (int i = insertPos; i < len; ++i) {
        res[k++] = n[i];
    }
    res[k] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string MaxValue(string n, int x) {
        char xc = (char)('0' + x);
        if (n[0] != '-') {
            for (int i = 0; i < n.Length; ++i) {
                if (n[i] < xc) {
                    return n.Substring(0, i) + xc + n.Substring(i);
                }
            }
            return n + xc;
        } else {
            for (int i = 1; i < n.Length; ++i) {
                if (n[i] > xc) {
                    return n.Substring(0, i) + xc + n.Substring(i);
                }
            }
            return n + xc;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} n
 * @param {number} x
 * @return {string}
 */
var maxValue = function(n, x) {
    const digit = String(x);
    if (n[0] !== '-') {
        // Positive number: insert before first smaller digit
        for (let i = 0; i < n.length; ++i) {
            if (n[i] < digit) {
                return n.slice(0, i) + digit + n.slice(i);
            }
        }
        return n + digit;
    } else {
        // Negative number: insert before first larger digit to minimize magnitude
        for (let i = 1; i < n.length; ++i) {
            if (n[i] > digit) {
                return n.slice(0, i) + digit + n.slice(i);
            }
        }
        return n + digit;
    }
};
```

## Typescript

```typescript
function maxValue(n: string, x: number): string {
    const isNegative = n[0] === '-';
    const s = isNegative ? n.slice(1) : n;
    const xs = x.toString();
    let i = 0;
    const len = s.length;
    while (i < len) {
        const digit = s.charCodeAt(i) - 48; // convert char to number
        if (!isNegative && digit < x) break;
        if (isNegative && digit > x) break;
        i++;
    }
    const inserted = s.slice(0, i) + xs + s.slice(i);
    return isNegative ? '-' + inserted : inserted;
}
```

## Php

```php
class Solution {

    /**
     * @param String $n
     * @param Integer $x
     * @return String
     */
    function maxValue($n, $x) {
        $digit = strval($x);
        if ($n[0] === '-') {
            $len = strlen($n);
            for ($i = 1; $i < $len; $i++) {
                if ($n[$i] > $digit) {
                    return substr($n, 0, $i) . $digit . substr($n, $i);
                }
            }
            return $n . $digit;
        } else {
            $len = strlen($n);
            for ($i = 0; $i < $len; $i++) {
                if ($n[$i] < $digit) {
                    return substr($n, 0, $i) . $digit . substr($n, $i);
                }
            }
            return $n . $digit;
        }
    }
}
```

## Swift

```swift
class Solution {
    func maxValue(_ n: String, _ x: Int) -> String {
        let xc = Character(String(x))
        let chars = Array(n)
        if n.first != "-" {
            var inserted = false
            var result = ""
            for c in chars {
                if !inserted && c < xc {
                    result.append(xc)
                    inserted = true
                }
                result.append(c)
            }
            if !inserted {
                result.append(xc)
            }
            return result
        } else {
            var inserted = false
            var result = "-"
            for i in 1..<chars.count {
                let c = chars[i]
                if !inserted && c > xc {
                    result.append(xc)
                    inserted = true
                }
                result.append(c)
            }
            if !inserted {
                result.append(xc)
            }
            return result
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxValue(n: String, x: Int): String {
        val xc = ('0'.code + x).toChar()
        if (n[0] != '-') {
            for (i in n.indices) {
                if (n[i] < xc) {
                    return n.substring(0, i) + xc + n.substring(i)
                }
            }
            return n + xc
        } else {
            for (i in 1 until n.length) {
                if (n[i] > xc) {
                    return n.substring(0, i) + xc + n.substring(i)
                }
            }
            return n + xc
        }
    }
}
```

## Dart

```dart
class Solution {
  String maxValue(String n, int x) {
    String xs = x.toString();
    if (!n.startsWith('-')) {
      for (int i = 0; i < n.length; ++i) {
        int d = n.codeUnitAt(i) - 48;
        if (d < x) {
          return n.substring(0, i) + xs + n.substring(i);
        }
      }
      return n + xs;
    } else {
      for (int i = 1; i < n.length; ++i) {
        int d = n.codeUnitAt(i) - 48;
        if (d > x) {
          return n.substring(0, i) + xs + n.substring(i);
        }
      }
      return n + xs;
    }
  }
}
```

## Golang

```go
func maxValue(n string, x int) string {
    c := byte('0' + x)
    if n[0] != '-' {
        for i := 0; i < len(n); i++ {
            if n[i] < c {
                return n[:i] + string(c) + n[i:]
            }
        }
        return n + string(c)
    } else {
        s := n[1:] // without the negative sign
        for i := 0; i < len(s); i++ {
            if s[i] > c {
                return "-" + s[:i] + string(c) + s[i:]
            }
        }
        return n + string(c)
    }
}
```

## Ruby

```ruby
def max_value(n, x)
  s = n
  d = x.to_s
  if s[0] != '-'
    i = 0
    while i < s.length && s[i] >= d
      i += 1
    end
    s[0...i] + d + s[i..-1]
  else
    i = 1
    while i < s.length && s[i] <= d
      i += 1
    end
    s[0...i] + d + s[i..-1]
  end
end
```

## Scala

```scala
object Solution {
    def maxValue(n: String, x: Int): String = {
        val xs = (x + '0').toChar
        if (!n.startsWith("-")) {
            val sb = new StringBuilder()
            var inserted = false
            for (c <- n) {
                if (!inserted && c < xs) {
                    sb.append(xs)
                    inserted = true
                }
                sb.append(c)
            }
            if (!inserted) sb.append(xs)
            sb.toString()
        } else {
            val sb = new StringBuilder()
            sb.append('-')
            var inserted = false
            for (i <- 1 until n.length) {
                val c = n.charAt(i)
                if (!inserted && c > xs) {
                    sb.append(xs)
                    inserted = true
                }
                sb.append(c)
            }
            if (!inserted) sb.append(xs)
            sb.toString()
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_value(n: String, x: i32) -> String {
        let mut chars: Vec<char> = n.chars().collect();
        let xc = std::char::from_digit(x as u32, 10).unwrap();

        if chars[0] != '-' {
            // Positive number: insert before first digit smaller than x
            for i in 0..chars.len() {
                if chars[i] < xc {
                    let mut res = String::with_capacity(chars.len() + 1);
                    for j in 0..i {
                        res.push(chars[j]);
                    }
                    res.push(xc);
                    for j in i..chars.len() {
                        res.push(chars[j]);
                    }
                    return res;
                }
            }
            // Append at the end if no smaller digit found
            let mut res = n.clone();
            res.push(xc);
            res
        } else {
            // Negative number: insert before first digit greater than x
            for i in 1..chars.len() {
                if chars[i] > xc {
                    let mut res = String::with_capacity(chars.len() + 1);
                    for j in 0..i {
                        res.push(chars[j]);
                    }
                    res.push(xc);
                    for j in i..chars.len() {
                        res.push(chars[j]);
                    }
                    return res;
                }
            }
            // Append at the end if no greater digit found
            let mut res = n.clone();
            res.push(xc);
            res
        }
    }
}
```

## Racket

```racket
(define/contract (max-value n x)
  (-> string? exact-integer? string?)
  (let* ((xs (number->string x))
         (xch (string-ref xs 0)))
    (if (and (> (string-length n) 0)
             (char=? (string-ref n 0) #\-))
        ;; negative number: insert before first digit greater than x
        (let loop ((i 1) (len (string-length n)))
          (cond [(= i len) (string-append n xs)]
                [else (define cur (string-ref n i))
                      (if (> (char->integer cur) (char->integer xch))
                          (string-append (substring n 0 i) xs (substring n i))
                          (loop (+ i 1) len))]))
        ;; positive number: insert before first digit less than x
        (let loop ((i 0) (len (string-length n)))
          (cond [(= i len) (string-append n xs)]
                [else (define cur (string-ref n i))
                      (if (< (char->integer cur) (char->integer xch))
                          (string-append (substring n 0 i) xs (substring n i))
                          (loop (+ i 1) len))])))))
```

## Erlang

```erlang
-spec max_value(N :: unicode:unicode_binary(), X :: integer()) -> unicode:unicode_binary().
max_value(N, X) ->
    XChar = $0 + X,
    case binary_to_list(N) of
        [$- | Rest] ->
            NewDigits = insert_negative(Rest, XChar),
            list_to_binary([$- | NewDigits]);
        Digits ->
            NewDigits = insert_positive(Digits, XChar),
            list_to_binary(NewDigits)
    end.

insert_positive([], X) -> [X];
insert_positive([H|T]=List, X) when H < X ->
    [X | List];
insert_positive([H|T], X) ->
    [H | insert_positive(T, X)].

insert_negative([], X) -> [X];
insert_negative([H|T]=List, X) when H > X ->
    [X | List];
insert_negative([H|T], X) ->
    [H | insert_negative(T, X)].
```

## Elixir

```elixir
defmodule Solution do
  @spec max_value(n :: String.t(), x :: integer()) :: String.t()
  def max_value(n, x) do
    xs = Integer.to_string(x)

    if String.starts_with?(n, "-") do
      rest = String.slice(n, 1..-1)

      case find_insert_position_negative(rest, xs) do
        {:found, idx} ->
          prefix = String.slice(rest, 0, idx)
          suffix = String.slice(rest, idx..-1)
          "-" <> prefix <> xs <> suffix

        :not_found ->
          "-" <> rest <> xs
      end
    else
      case find_insert_position_positive(n, xs) do
        {:found, idx} ->
          prefix = String.slice(n, 0, idx)
          suffix = String.slice(n, idx..-1)
          prefix <> xs <> suffix

        :not_found ->
          n <> xs
      end
    end
  end

  defp find_insert_position_positive(str, xs) do
    str
    |> String.graphemes()
    |> Enum.with_index()
    |> Enum.reduce_while(:not_found, fn {ch, idx}, _acc ->
      if ch < xs do
        {:halt, {:found, idx}}
      else
        {:cont, :not_found}
      end
    end)
  end

  defp find_insert_position_negative(str, xs) do
    str
    |> String.graphemes()
    |> Enum.with_index()
    |> Enum.reduce_while(:not_found, fn {ch, idx}, _acc ->
      if ch > xs do
        {:halt, {:found, idx}}
      else
        {:cont, :not_found}
      end
    end)
  end
end
```

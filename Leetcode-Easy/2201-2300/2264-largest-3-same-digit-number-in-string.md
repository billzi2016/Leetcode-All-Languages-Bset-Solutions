# 2264. Largest 3-Same-Digit Number in String

## Cpp

```cpp
class Solution {
public:
    std::string largestGoodInteger(std::string num) {
        char maxDigit = '\0';
        int n = num.size();
        for (int i = 0; i + 2 < n; ++i) {
            if (num[i] == num[i+1] && num[i] == num[i+2]) {
                if (maxDigit == '\0' || num[i] > maxDigit)
                    maxDigit = num[i];
            }
        }
        return maxDigit == '\0' ? "" : std::string(3, maxDigit);
    }
};
```

## Java

```java
class Solution {
    public String largestGoodInteger(String num) {
        char maxDigit = 0;
        int n = num.length();
        for (int i = 0; i + 2 < n; i++) {
            char c = num.charAt(i);
            if (c == num.charAt(i + 1) && c == num.charAt(i + 2)) {
                if (c > maxDigit) {
                    maxDigit = c;
                }
            }
        }
        return maxDigit == 0 ? "" : "" + maxDigit + maxDigit + maxDigit;
    }
}
```

## Python

```python
class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        max_digit = ''
        n = len(num)
        for i in range(n - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if not max_digit or num[i] > max_digit:
                    max_digit = num[i]
        return max_digit * 3 if max_digit else ""
```

## Python3

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_digit = ''
        n = len(num)
        for i in range(n - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if not max_digit or num[i] > max_digit:
                    max_digit = num[i]
        return max_digit * 3 if max_digit else ""
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* largestGoodInteger(char* num) {
    int n = strlen(num);
    char maxDigit = 0;
    for (int i = 0; i + 2 < n; ++i) {
        if (num[i] == num[i + 1] && num[i] == num[i + 2]) {
            if (num[i] > maxDigit) {
                maxDigit = num[i];
            }
        }
    }
    if (maxDigit == 0) {
        char* res = (char*)malloc(1);
        res[0] = '\0';
        return res;
    } else {
        char* res = (char*)malloc(4);
        res[0] = res[1] = res[2] = maxDigit;
        res[3] = '\0';
        return res;
    }
}
```

## Csharp

```csharp
public class Solution
{
    public string LargestGoodInteger(string num)
    {
        char maxDigit = '\0';
        for (int i = 0; i + 2 < num.Length; i++)
        {
            if (num[i] == num[i + 1] && num[i] == num[i + 2])
            {
                if (maxDigit < num[i])
                    maxDigit = num[i];
            }
        }
        return maxDigit == '\0' ? "" : new string(maxDigit, 3);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @return {string}
 */
var largestGoodInteger = function(num) {
    let maxDigit = '';
    for (let i = 0; i + 2 < num.length; ++i) {
        if (num[i] === num[i + 1] && num[i] === num[i + 2]) {
            if (maxDigit === '' || num[i] > maxDigit) {
                maxDigit = num[i];
            }
        }
    }
    return maxDigit ? maxDigit.repeat(3) : "";
};
```

## Typescript

```typescript
function largestGoodInteger(num: string): string {
    let maxDigit = "";
    for (let i = 0; i + 2 < num.length; i++) {
        const c = num[i];
        if (c === num[i + 1] && c === num[i + 2]) {
            if (maxDigit === "" || c > maxDigit) {
                maxDigit = c;
            }
        }
    }
    return maxDigit ? maxDigit.repeat(3) : "";
}
```

## Php

```php
<?php
class Solution {

    /**
     * @param String $num
     * @return String
     */
    function largestGoodInteger($num) {
        $n = strlen($num);
        $maxDigit = '';
        for ($i = 0; $i <= $n - 3; $i++) {
            if ($num[$i] === $num[$i + 1] && $num[$i] === $num[$i + 2]) {
                if ($maxDigit === '' || $num[$i] > $maxDigit) {
                    $maxDigit = $num[$i];
                }
            }
        }
        return $maxDigit === '' ? "" : str_repeat($maxDigit, 3);
    }
}
?>
```

## Swift

```swift
class Solution {
    func largestGoodInteger(_ num: String) -> String {
        let chars = Array(num)
        var maxChar: Character = "0"
        var found = false
        for i in 0..<(chars.count - 2) {
            if chars[i] == chars[i + 1] && chars[i] == chars[i + 2] {
                if !found || chars[i] > maxChar {
                    maxChar = chars[i]
                    found = true
                }
            }
        }
        return found ? String(repeating: maxChar, count: 3) : ""
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestGoodInteger(num: String): String {
        var maxChar = '\u0000'
        for (i in 0 until num.length - 2) {
            val c = num[i]
            if (c == num[i + 1] && c == num[i + 2]) {
                if (c > maxChar) {
                    maxChar = c
                }
            }
        }
        return if (maxChar == '\u0000') "" else "$maxChar$maxChar$maxChar"
    }
}
```

## Dart

```dart
class Solution {
  String largestGoodInteger(String num) {
    String maxDigit = '';
    for (int i = 0; i <= num.length - 3; i++) {
      if (num[i] == num[i + 1] && num[i] == num[i + 2]) {
        if (maxDigit.isEmpty || num[i].compareTo(maxDigit) > 0) {
          maxDigit = num[i];
        }
      }
    }
    return maxDigit.isEmpty ? '' : '${maxDigit}${maxDigit}${maxDigit}';
  }
}
```

## Golang

```go
func largestGoodInteger(num string) string {
    var max byte = 0
    n := len(num)
    for i := 0; i+2 < n; i++ {
        if num[i] == num[i+1] && num[i] == num[i+2] {
            if num[i] > max {
                max = num[i]
            }
        }
    }
    if max == 0 {
        return ""
    }
    return string([]byte{max, max, max})
}
```

## Ruby

```ruby
def largest_good_integer(num)
  max_byte = -1
  i = 0
  limit = num.length - 2
  while i < limit
    b = num.getbyte(i)
    if b == num.getbyte(i + 1) && b == num.getbyte(i + 2)
      max_byte = b if b > max_byte
    end
    i += 1
  end
  max_byte == -1 ? "" : (max_byte.chr * 3)
end
```

## Scala

```scala
object Solution {
    def largestGoodInteger(num: String): String = {
        var maxChar: Char = 0
        val n = num.length
        var i = 0
        while (i <= n - 3) {
            val c = num.charAt(i)
            if (c == num.charAt(i + 1) && c == num.charAt(i + 2)) {
                if (c > maxChar) maxChar = c
            }
            i += 1
        }
        if (maxChar == 0) "" else s"$maxChar$maxChar$maxChar"
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_good_integer(num: String) -> String {
        let bytes = num.as_bytes();
        let n = bytes.len();
        if n < 3 {
            return String::new();
        }
        let mut max_digit: u8 = 0; // 0 indicates no digit found yet
        for i in 0..n - 2 {
            let b = bytes[i];
            if b == bytes[i + 1] && b == bytes[i + 2] {
                if b > max_digit {
                    max_digit = b;
                }
            }
        }
        if max_digit == 0 {
            String::new()
        } else {
            let ch = max_digit as char;
            std::iter::repeat(ch).take(3).collect()
        }
    }
}
```

## Racket

```racket
(define/contract (largest-good-integer num)
  (-> string? string?)
  (let* ((n (string-length num))
         (sentinel #\0))
    (let loop ((i 0) (max-digit sentinel))
      (if (> i (- n 3))
          (if (char=? max-digit sentinel)
              ""
              (make-string 3 max-digit))
          (let ((c (string-ref num i)))
            (if (and (char=? c (string-ref num (+ i 1)))
                     (char=? c (string-ref num (+ i 2))))
                (loop (+ i 1) (if (char>? c max-digit) c max-digit))
                (loop (+ i 1) max-digit)))))))
```

## Erlang

```erlang
-spec largest_good_integer(Num :: unicode:unicode_binary()) -> unicode:unicode_binary().
largest_good_integer(Num) ->
    Max = find_max(Num, -1),
    case Max of
        -1 -> <<>>;
        D  -> <<D,D,D>>
    end.

find_max(Binary, Max) when byte_size(Binary) < 3 ->
    Max;
find_max(<<C,C,C,Rest/binary>>, Max) ->
    NewMax = if C > Max -> C; true -> Max end,
    find_max(<<C,Rest/binary>>, NewMax);
find_max(<<_,Rest/binary>>, Max) ->
    find_max(Rest, Max).
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_good_integer(num :: String.t()) :: String.t()
  def largest_good_integer(num) do
    chars = String.to_charlist(num)
    len = length(chars)

    max_digit = find_max(chars, len, 0, nil)

    case max_digit do
      nil -> ""
      digit -> List.duplicate(digit, 3) |> to_string()
    end
  end

  defp find_max(_chars, len, idx, max) when idx > len - 3, do: max

  defp find_max(chars, len, idx, max) do
    c = Enum.at(chars, idx)

    new_max =
      if c == Enum.at(chars, idx + 1) and c == Enum.at(chars, idx + 2) do
        cond do
          max == nil -> c
          c > max -> c
          true -> max
        end
      else
        max
      end

    find_max(chars, len, idx + 1, new_max)
  end
end
```

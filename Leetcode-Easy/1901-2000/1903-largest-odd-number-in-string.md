# 1903. Largest Odd Number in String

## Cpp

```cpp
class Solution {
public:
    string largestOddNumber(string num) {
        for (int i = (int)num.size() - 1; i >= 0; --i) {
            if ((num[i] - '0') % 2 == 1) {
                return num.substr(0, i + 1);
            }
        }
        return "";
    }
};
```

## Java

```java
class Solution {
    public String largestOddNumber(String num) {
        for (int i = num.length() - 1; i >= 0; i--) {
            if (((num.charAt(i) - '0') & 1) == 1) {
                return num.substring(0, i + 1);
            }
        }
        return "";
    }
}
```

## Python

```python
class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in range(len(num) - 1, -1, -1):
            if (ord(num[i]) - ord('0')) % 2 == 1:
                return num[:i + 1]
        return ""
```

## Python3

```python
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if (ord(num[i]) - ord('0')) % 2 == 1:
                return num[:i + 1]
        return ""
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* largestOddNumber(char* num) {
    int len = strlen(num);
    for (int i = len - 1; i >= 0; --i) {
        if ((num[i] - '0') % 2 == 1) {
            char *res = (char *)malloc(i + 2);
            memcpy(res, num, i + 1);
            res[i + 1] = '\0';
            return res;
        }
    }
    char *empty = (char *)malloc(1);
    empty[0] = '\0';
    return empty;
}
```

## Csharp

```csharp
public class Solution {
    public string LargestOddNumber(string num) {
        for (int i = num.Length - 1; i >= 0; i--) {
            if (((num[i] - '0') & 1) == 1) {
                return num.Substring(0, i + 1);
            }
        }
        return "";
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @return {string}
 */
var largestOddNumber = function(num) {
    for (let i = num.length - 1; i >= 0; --i) {
        const digit = num.charCodeAt(i) - 48; // '0' char code is 48
        if ((digit & 1) === 1) { // odd check
            return num.slice(0, i + 1);
        }
    }
    return "";
};
```

## Typescript

```typescript
function largestOddNumber(num: string): string {
    for (let i = num.length - 1; i >= 0; i--) {
        const digit = num.charCodeAt(i) - 48;
        if ((digit & 1) === 1) {
            return num.substring(0, i + 1);
        }
    }
    return "";
}
```

## Php

```php
class Solution {

    /**
     * @param String $num
     * @return String
     */
    function largestOddNumber($num) {
        $len = strlen($num);
        for ($i = $len - 1; $i >= 0; $i--) {
            if (((int)$num[$i]) % 2 === 1) {
                return substr($num, 0, $i + 1);
            }
        }
        return "";
    }
}
```

## Swift

```swift
class Solution {
    func largestOddNumber(_ num: String) -> String {
        let bytes = Array(num.utf8)
        for i in stride(from: bytes.count - 1, through: 0, by: -1) {
            let digit = Int(bytes[i] - 48)
            if digit % 2 == 1 {
                return String(decoding: bytes[0...i], as: UTF8.self)
            }
        }
        return ""
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestOddNumber(num: String): String {
        for (i in num.length - 1 downTo 0) {
            val digit = num[i] - '0'
            if ((digit and 1) == 1) {
                return num.substring(0, i + 1)
            }
        }
        return ""
    }
}
```

## Dart

```dart
class Solution {
  String largestOddNumber(String num) {
    for (int i = num.length - 1; i >= 0; i--) {
      int digit = num.codeUnitAt(i) - 48; // '0' ASCII is 48
      if ((digit & 1) == 1) {
        return num.substring(0, i + 1);
      }
    }
    return "";
  }
}
```

## Golang

```go
func largestOddNumber(num string) string {
    for i := len(num) - 1; i >= 0; i-- {
        if (num[i]-'0')%2 == 1 {
            return num[:i+1]
        }
    }
    return ""
}
```

## Ruby

```ruby
def largest_odd_number(num)
  (num.length - 1).downto(0) do |i|
    return num[0..i] if num.getbyte(i).odd?
  end
  ""
end
```

## Scala

```scala
object Solution {
    def largestOddNumber(num: String): String = {
        var i = num.length - 1
        while (i >= 0) {
            val ch = num.charAt(i)
            if ((ch - '0') % 2 == 1) return num.substring(0, i + 1)
            i -= 1
        }
        ""
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_odd_number(num: String) -> String {
        let bytes = num.as_bytes();
        for i in (0..bytes.len()).rev() {
            if (bytes[i] - b'0') % 2 == 1 {
                return num[..=i].to_string();
            }
        }
        String::new()
    }
}
```

## Racket

```racket
(define/contract (largest-odd-number num)
  (-> string? string?)
  (let* ((len (string-length num))
         (idx
          (let loop ((i (- len 1)))
            (cond [(< i 0) #f]
                  [(= (modulo (char->integer (string-ref num i)) 2) 1) i]
                  [else (loop (- i 1))]))))
    (if idx
        (substring num 0 (+ idx 1))
        "")))
```

## Erlang

```erlang
-spec largest_odd_number(Num :: unicode:unicode_binary()) -> unicode:unicode_binary().
largest_odd_number(Num) ->
    Len = byte_size(Num),
    find_rightmost_odd(Num, Len - 1).

find_rightmost_odd(_Num, -1) ->
    <<>>;
find_rightmost_odd(Num, Index) ->
    Digit = binary:at(Num, Index),
    case (Digit band 1) of
        1 -> binary:part(Num, {0, Index + 1});
        _ -> find_rightmost_odd(Num, Index - 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_odd_number(num :: String.t()) :: String.t()
  def largest_odd_number(num) do
    len = byte_size(num)
    find_odd(num, len - 1)
  end

  defp find_odd(_num, -1), do: ""

  defp find_odd(num, idx) do
    digit = :binary.at(num, idx)

    if rem(digit - ?0, 2) == 1 do
      :binary.part(num, 0, idx + 1)
    else
      find_odd(num, idx - 1)
    end
  end
end
```

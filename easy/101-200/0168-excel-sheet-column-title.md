# 0168. Excel Sheet Column Title

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string convertToTitle(int columnNumber) {
        string res;
        while (columnNumber > 0) {
            columnNumber--; // adjust to 0-indexed
            char c = 'A' + (columnNumber % 26);
            res.push_back(c);
            columnNumber /= 26;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

## Java

```java
class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder sb = new StringBuilder();
        while (columnNumber > 0) {
            columnNumber--; // adjust to 0-indexed
            int rem = columnNumber % 26;
            sb.append((char) ('A' + rem));
            columnNumber /= 26;
        }
        return sb.reverse().toString();
    }
}
```

## Python

```python
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ans = []
        while columnNumber > 0:
            columnNumber -= 1
            ans.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26
        return ''.join(reversed(ans))
```

## Python3

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            res.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26
        return ''.join(reversed(res))
```

## C

```c
#include <stdlib.h>

char* convertToTitle(int columnNumber) {
    char *buf = (char *)malloc(8); // max 7 letters + null terminator
    int idx = 0;
    while (columnNumber > 0) {
        columnNumber--;                     // adjust to 0-indexed
        int rem = columnNumber % 26;        // current character
        buf[idx++] = 'A' + rem;
        columnNumber /= 26;
    }
    // reverse the collected characters
    for (int i = 0; i < idx / 2; ++i) {
        char tmp = buf[i];
        buf[i] = buf[idx - 1 - i];
        buf[idx - 1 - i] = tmp;
    }
    buf[idx] = '\0';
    return buf;
}
```

## Csharp

```csharp
using System;
using System.Text;

public class Solution {
    public string ConvertToTitle(int columnNumber) {
        StringBuilder sb = new StringBuilder();
        while (columnNumber > 0) {
            columnNumber--; // adjust to 0-index
            int rem = columnNumber % 26;
            sb.Append((char)('A' + rem));
            columnNumber /= 26;
        }
        char[] chars = sb.ToString().ToCharArray();
        Array.Reverse(chars);
        return new string(chars);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} columnNumber
 * @return {string}
 */
var convertToTitle = function(columnNumber) {
    let result = [];
    while (columnNumber > 0) {
        columnNumber--; // adjust to 0-indexed
        const charCode = (columnNumber % 26) + 65; // 'A' is 65
        result.push(String.fromCharCode(charCode));
        columnNumber = Math.floor(columnNumber / 26);
    }
    return result.reverse().join('');
};
```

## Typescript

```typescript
function convertToTitle(columnNumber: number): string {
    let result = "";
    while (columnNumber > 0) {
        columnNumber--; // adjust to 0-indexed
        const charCode = 65 + (columnNumber % 26);
        result = String.fromCharCode(charCode) + result;
        columnNumber = Math.floor(columnNumber / 26);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $columnNumber
     * @return String
     */
    function convertToTitle($columnNumber) {
        $result = '';
        while ($columnNumber > 0) {
            $columnNumber--;
            $rem = $columnNumber % 26;
            $result = chr(ord('A') + $rem) . $result;
            $columnNumber = intdiv($columnNumber, 26);
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func convertToTitle(_ columnNumber: Int) -> String {
        var n = columnNumber
        var chars: [Character] = []
        while n > 0 {
            n -= 1
            let remainder = n % 26
            let ch = Character(UnicodeScalar(remainder + 65)!)
            chars.append(ch)
            n /= 26
        }
        return String(chars.reversed())
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun convertToTitle(columnNumber: Int): String {
        var n = columnNumber
        val sb = StringBuilder()
        while (n > 0) {
            n--
            sb.append(('A'.code + n % 26).toChar())
            n /= 26
        }
        return sb.reverse().toString()
    }
}
```

## Dart

```dart
class Solution {
  String convertToTitle(int columnNumber) {
    final List<int> codes = [];
    while (columnNumber > 0) {
      columnNumber--;
      int rem = columnNumber % 26;
      codes.add(65 + rem);
      columnNumber ~/= 26;
    }
    return String.fromCharCodes(codes.reversed);
  }
}
```

## Golang

```go
func convertToTitle(columnNumber int) string {
	var chars []byte
	for columnNumber > 0 {
		columnNumber--
		rem := columnNumber % 26
		chars = append(chars, byte('A'+rem))
		columnNumber /= 26
	}
	for i, j := 0, len(chars)-1; i < j; i, j = i+1, j-1 {
		chars[i], chars[j] = chars[j], chars[i]
	}
	return string(chars)
}
```

## Ruby

```ruby
def convert_to_title(column_number)
  result = ''
  while column_number > 0
    column_number -= 1
    result << ((column_number % 26) + 65).chr
    column_number /= 26
  end
  result.reverse
end
```

## Scala

```scala
object Solution {
    def convertToTitle(columnNumber: Int): String = {
        var n = columnNumber
        val sb = new StringBuilder
        while (n > 0) {
            n -= 1
            sb.append(('A'.toInt + (n % 26)).toChar)
            n /= 26
        }
        sb.reverse.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn convert_to_title(column_number: i32) -> String {
        let mut n = column_number as i64;
        let mut chars = Vec::new();
        while n > 0 {
            n -= 1;
            let rem = (n % 26) as u8;
            chars.push((b'A' + rem) as char);
            n /= 26;
        }
        chars.iter().rev().collect()
    }
}
```

## Racket

```racket
(define/contract (convert-to-title columnNumber)
  (-> exact-integer? string?)
  (let loop ((n columnNumber) (chars '()))
    (if (= n 0)
        (list->string (reverse chars))
        (let* ((n1 (- n 1))
               (rem (modulo n1 26))
               (ch (integer->char (+ (char->integer #\A) rem))))
          (loop (quotient n1 26) (cons ch chars))))))
```

## Erlang

```erlang
-module(solution).
-export([convert_to_title/1]).

-spec convert_to_title(integer()) -> unicode:unicode_binary().
convert_to_title(ColumnNumber) ->
    convert_to_title(ColumnNumber, []).

convert_to_title(0, Acc) ->
    list_to_binary(lists:reverse(Acc));
convert_to_title(N, Acc) ->
    N1 = N - 1,
    Rem = N1 rem 26,
    Char = $A + Rem,
    convert_to_title(N1 div 26, [Char | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec convert_to_title(column_number :: integer) :: String.t()
  def convert_to_title(column_number) when column_number > 0 do
    build_title(column_number, [])
    |> List.to_string()
  end

  defp build_title(0, acc), do: acc

  defp build_title(n, acc) do
    n = n - 1
    r = rem(n, 26)
    char = <<?A + r>>
    build_title(div(n, 26), [char | acc])
  end
end
```

# 2710. Remove Trailing Zeros From a String

## Cpp

```cpp
class Solution {
public:
    string removeTrailingZeros(string num) {
        int i = (int)num.size() - 1;
        while (i >= 0 && num[i] == '0') {
            --i;
        }
        return num.substr(0, i + 1);
    }
};
```

## Java

```java
class Solution {
    public String removeTrailingZeros(String num) {
        int i = num.length() - 1;
        while (i >= 0 && num.charAt(i) == '0') {
            i--;
        }
        return num.substring(0, i + 1);
    }
}
```

## Python

```python
class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        trimmed = num.rstrip('0')
        return trimmed if trimmed else "0")
```

## Python3

```python
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        trimmed = num.rstrip('0')
        return trimmed if trimmed else "0"
```

## C

```c
#include <string.h>

char* removeTrailingZeros(char* num) {
    int len = strlen(num);
    int i = len - 1;
    while (i >= 0 && num[i] == '0') {
        i--;
    }
    num[i + 1] = '\0';
    return num;
}
```

## Csharp

```csharp
public class Solution {
    public string RemoveTrailingZeros(string num) {
        int i = num.Length - 1;
        while (i >= 0 && num[i] == '0') {
            i--;
        }
        // Since the input represents a positive integer without leading zeros,
        // there will always be at least one non-zero digit.
        return num.Substring(0, i + 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @return {string}
 */
var removeTrailingZeros = function(num) {
    let i = num.length - 1;
    while (i >= 0 && num[i] === '0') {
        i--;
    }
    // If all characters are zeros, return "0"
    if (i < 0) return "0";
    return num.slice(0, i + 1);
};
```

## Typescript

```typescript
function removeTrailingZeros(num: string): string {
    let i = num.length - 1;
    while (i >= 0 && num[i] === '0') {
        i--;
    }
    return num.slice(0, i + 1);
}
```

## Php

```php
class Solution {

    /**
     * @param String $num
     * @return String
     */
    function removeTrailingZeros($num) {
        $i = strlen($num) - 1;
        while ($i >= 0 && $num[$i] === '0') {
            $i--;
        }
        return substr($num, 0, $i + 1);
    }
}
```

## Swift

```swift
class Solution {
    func removeTrailingZeros(_ num: String) -> String {
        if let lastNonZero = num.lastIndex(where: { $0 != "0" }) {
            return String(num[..<num.index(after: lastNonZero)])
        }
        return "0"
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeTrailingZeros(num: String): String {
        var i = num.length - 1
        while (i >= 0 && num[i] == '0') {
            i--
        }
        return if (i < 0) "0" else num.substring(0, i + 1)
    }
}
```

## Dart

```dart
class Solution {
  String removeTrailingZeros(String num) {
    int i = num.length - 1;
    while (i >= 0 && num[i] == '0') {
      i--;
    }
    return num.substring(0, i + 1);
  }
}
```

## Golang

```go
func removeTrailingZeros(num string) string {
    i := len(num) - 1
    for i >= 0 && num[i] == '0' {
        i--
    }
    if i < 0 {
        return "0"
    }
    return num[:i+1]
}
```

## Ruby

```ruby
def remove_trailing_zeros(num)
  result = num.sub(/0+$/, '')
  result.empty? ? "0" : result
end
```

## Scala

```scala
object Solution {
    def removeTrailingZeros(num: String): String = {
        var i = num.length - 1
        while (i >= 0 && num.charAt(i) == '0') {
            i -= 1
        }
        if (i < 0) "0" else num.substring(0, i + 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_trailing_zeros(num: String) -> String {
        let mut idx = num.len();
        let bytes = num.as_bytes();
        while idx > 0 && bytes[idx - 1] == b'0' {
            idx -= 1;
        }
        num[..idx].to_string()
    }
}
```

## Racket

```racket
(define/contract (remove-trailing-zeros num)
  (-> string? string?)
  (let* ((len (string-length num))
         (new-end
          (let loop ((i (- len 1)))
            (if (or (< i 0) (not (char=? (string-ref num i) #\0)))
                (+ i 1)
                (loop (- i 1))))))
    (substring num 0 new-end)))
```

## Erlang

```erlang
-module(solution).
-export([remove_trailing_zeros/1]).

-spec remove_trailing_zeros(Num :: unicode:unicode_binary()) -> unicode:unicode_binary().
remove_trailing_zeros(Num) ->
    binary:reverse(drop_leading_zeros(binary:reverse(Num))).

drop_leading_zeros(<<$0, Rest/binary>>) ->
    drop_leading_zeros(Rest);
drop_leading_zeros(Bin) ->
    Bin.
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_trailing_zeros(num :: String.t) :: String.t
  def remove_trailing_zeros(num) do
    String.replace(num, ~r/0+$/, "")
  end
end
```

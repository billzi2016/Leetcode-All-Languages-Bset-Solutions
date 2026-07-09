# 3174. Clear Digits

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string clearDigits(string s) {
        string res;
        res.reserve(s.size());
        for (char c : s) {
            if (isdigit(static_cast<unsigned char>(c))) {
                if (!res.empty()) res.pop_back();
            } else {
                res.push_back(c);
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String clearDigits(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= '0' && c <= '9') {
                sb.deleteCharAt(sb.length() - 1);
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if ch.isdigit():
                # guaranteed there is a non-digit to the left
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
```

## Python3

```python
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* clearDigits(char* s) {
    int n = strlen(s);
    char *res = (char *)malloc(n + 1);
    int top = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] >= '0' && s[i] <= '9') {
            if (top > 0) --top; // remove the last non-digit character
        } else {
            res[top++] = s[i];
        }
    }
    res[top] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string ClearDigits(string s)
    {
        var sb = new System.Text.StringBuilder();
        foreach (char c in s)
        {
            if (c >= '0' && c <= '9')
            {
                if (sb.Length > 0) sb.Length--;
            }
            else
            {
                sb.Append(c);
            }
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
var clearDigits = function(s) {
    const stack = [];
    for (const ch of s) {
        if (ch >= '0' && ch <= '9') {
            // Remove the nearest non-digit character to the left.
            if (stack.length > 0) stack.pop();
        } else {
            stack.push(ch);
        }
    }
    return stack.join('');
};
```

## Typescript

```typescript
function clearDigits(s: string): string {
    const stack: string[] = [];
    for (const ch of s) {
        if (ch >= '0' && ch <= '9') {
            stack.pop();
        } else {
            stack.push(ch);
        }
    }
    return stack.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function clearDigits($s) {
        $stack = [];
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if (ctype_digit($ch)) {
                array_pop($stack);
            } else {
                $stack[] = $ch;
            }
        }
        return implode('', $stack);
    }
}
```

## Swift

```swift
class Solution {
    func clearDigits(_ s: String) -> String {
        var stack = [Character]()
        for ch in s {
            if ch.isNumber {
                if !stack.isEmpty {
                    stack.removeLast()
                }
            } else {
                stack.append(ch)
            }
        }
        return String(stack)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun clearDigits(s: String): String {
        val sb = StringBuilder()
        for (ch in s) {
            if (ch.isDigit()) {
                // Remove the last non-digit character
                sb.deleteCharAt(sb.length - 1)
            } else {
                sb.append(ch)
            }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String clearDigits(String s) {
    List<String> stack = [];
    for (int i = 0; i < s.length; i++) {
      String ch = s[i];
      int code = ch.codeUnitAt(0);
      if (code >= 48 && code <= 57) { // digit
        if (stack.isNotEmpty) {
          stack.removeLast();
        }
      } else {
        stack.add(ch);
      }
    }
    return stack.join();
  }
}
```

## Golang

```go
func clearDigits(s string) string {
    stack := make([]byte, 0, len(s))
    for i := 0; i < len(s); i++ {
        c := s[i]
        if c >= '0' && c <= '9' {
            // Remove the last non-digit character
            if len(stack) > 0 {
                stack = stack[:len(stack)-1]
            }
        } else {
            stack = append(stack, c)
        }
    }
    return string(stack)
}
```

## Ruby

```ruby
def clear_digits(s)
  stack = []
  s.each_char do |ch|
    if ch >= '0' && ch <= '9'
      stack.pop
    else
      stack << ch
    end
  end
  stack.join
end
```

## Scala

```scala
object Solution {
    def clearDigits(s: String): String = {
        val sb = new java.lang.StringBuilder
        for (c <- s) {
            if (c.isDigit) {
                sb.setLength(sb.length - 1)
            } else {
                sb.append(c)
            }
        }
        sb.toString
    }
}
```

## Rust

```rust
impl Solution {
    pub fn clear_digits(s: String) -> String {
        let mut stack = Vec::new();
        for c in s.chars() {
            if c.is_ascii_digit() {
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        stack.iter().collect()
    }
}
```

## Racket

```racket
(define/contract (clear-digits s)
  (-> string? string?)
  (let loop ((chars (string->list s))
             (stack '()))
    (if (null? chars)
        (list->string (reverse stack))
        (let ((c (car chars)))
          (if (char-numeric? c)
              (loop (cdr chars) (if (null? stack) stack (cdr stack)))
              (loop (cdr chars) (cons c stack)))))))
```

## Erlang

```erlang
-spec clear_digits(unicode:unicode_binary()) -> unicode:unicode_binary().
clear_digits(S) ->
    Result = clear_digits_bin(S, []),
    list_to_binary(lists:reverse(Result)).

clear_digits_bin(<<>>, Acc) -> Acc;
clear_digits_bin(<<C, Rest/binary>>, Acc) when C >= $0, C =< $9 ->
    case Acc of
        [_|Tail] -> clear_digits_bin(Rest, Tail);
        [] -> clear_digits_bin(Rest, [])
    end;
clear_digits_bin(<<C, Rest/binary>>, Acc) ->
    clear_digits_bin(Rest, [C|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec clear_digits(s :: String.t) :: String.t
  def clear_digits(s) do
    s
    |> String.graphemes()
    |> Enum.reduce([], fn ch, acc ->
      if ch =~ ~r/^\d$/ do
        case acc do
          [_ | rest] -> rest
          [] -> []
        end
      else
        [ch | acc]
      end
    end)
    |> Enum.reverse()
    |> Enum.join()
  end
end
```

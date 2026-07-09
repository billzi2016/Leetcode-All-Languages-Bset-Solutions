# 1544. Make The String Great

## Cpp

```cpp
class Solution {
public:
    string makeGood(string s) {
        string st;
        for (char c : s) {
            if (!st.empty() && abs(st.back() - c) == 32) {
                st.pop_back();
            } else {
                st.push_back(c);
            }
        }
        return st;
    }
};
```

## Java

```java
class Solution {
    public String makeGood(String s) {
        StringBuilder stack = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int len = stack.length();
            if (len > 0 && Math.abs(stack.charAt(len - 1) - c) == 32) {
                stack.deleteCharAt(len - 1);
            } else {
                stack.append(c);
            }
        }
        return stack.toString();
    }
}
```

## Python

```python
class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
```

## Python3

```python
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* makeGood(char* s) {
    int n = strlen(s);
    char *stack = (char*)malloc(n + 1);
    int top = -1;
    for (int i = 0; i < n; ++i) {
        char c = s[i];
        if (top >= 0 && ((stack[top] ^ c) == 32)) {
            --top;
        } else {
            stack[++top] = c;
        }
    }
    stack[top + 1] = '\0';
    return stack;
}
```

## Csharp

```csharp
public class Solution
{
    public string MakeGood(string s)
    {
        char[] stack = new char[s.Length];
        int top = 0;
        foreach (char c in s)
        {
            if (top > 0 && Math.Abs(stack[top - 1] - c) == 32)
                top--;
            else
                stack[top++] = c;
        }
        return new string(stack, 0, top);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var makeGood = function(s) {
    const stack = [];
    for (let ch of s) {
        if (stack.length && Math.abs(stack[stack.length - 1].charCodeAt(0) - ch.charCodeAt(0)) === 32) {
            stack.pop();
        } else {
            stack.push(ch);
        }
    }
    return stack.join('');
};
```

## Typescript

```typescript
function makeGood(s: string): string {
    const stack: string[] = [];
    for (const ch of s) {
        if (stack.length && Math.abs(stack[stack.length - 1].charCodeAt(0) - ch.charCodeAt(0)) === 32) {
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
    function makeGood($s) {
        $stack = [];
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (!empty($stack)) {
                $top = end($stack);
                // Check if they are same letter different case
                if (ord($c) ^ ord($top) == 32) { // ASCII difference between cases is 32
                    array_pop($stack);
                    continue;
                }
            }
            $stack[] = $c;
        }
        return implode('', $stack);
    }
}
```

## Swift

```swift
class Solution {
    func makeGood(_ s: String) -> String {
        var stack = [Character]()
        for ch in s {
            if let last = stack.last,
               last != ch,
               String(last).lowercased() == String(ch).lowercased() {
                stack.removeLast()
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
    fun makeGood(s: String): String {
        val sb = StringBuilder()
        for (c in s) {
            if (sb.isNotEmpty()) {
                val last = sb[sb.length - 1]
                if (last != c && last.equals(c, ignoreCase = true)) {
                    sb.deleteCharAt(sb.length - 1)
                    continue
                }
            }
            sb.append(c)
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String makeGood(String s) {
    List<int> stack = [];
    for (int i = 0; i < s.length; i++) {
      int ch = s.codeUnitAt(i);
      if (stack.isNotEmpty && (stack.last - ch).abs() == 32) {
        stack.removeLast();
      } else {
        stack.add(ch);
      }
    }
    return String.fromCharCodes(stack);
  }
}
```

## Golang

```go
func makeGood(s string) string {
    stack := []rune{}
    for _, ch := range s {
        if len(stack) > 0 && (stack[len(stack)-1]-ch == 32 || stack[len(stack)-1]-ch == -32) {
            stack = stack[:len(stack)-1]
        } else {
            stack = append(stack, ch)
        }
    }
    return string(stack)
}
```

## Ruby

```ruby
def make_good(s)
  stack = []
  s.each_char do |ch|
    if !stack.empty? && stack[-1] != ch && stack[-1].downcase == ch.downcase
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
    def makeGood(s: String): String = {
        val stack = new scala.collection.mutable.ArrayBuffer[Char]()
        for (c <- s) {
            if (stack.nonEmpty && (stack.last ^ c) == 32) {
                stack.remove(stack.size - 1)
            } else {
                stack += c
            }
        }
        stack.mkString
    }
}
```

## Rust

```rust
impl Solution {
    pub fn make_good(s: String) -> String {
        let mut stack: Vec<char> = Vec::new();
        for ch in s.chars() {
            if let Some(&last) = stack.last() {
                if last != ch && last.eq_ignore_ascii_case(&ch) {
                    stack.pop();
                    continue;
                }
            }
            stack.push(ch);
        }
        stack.iter().collect()
    }
}
```

## Racket

```racket
(define/contract (make-good s)
  (-> string? string?)
  (letrec ((opposite?
            (lambda (a b)
              (and (char=? (char-downcase a) (char-downcase b))
                   (not (char=? a b))))))
    (let loop ((i 0) (stack '()))
      (if (= i (string-length s))
          (list->string (reverse stack))
          (let ((c (string-ref s i)))
            (if (and (pair? stack)
                     (opposite? c (car stack)))
                (loop (+ i 1) (cdr stack))   ; remove the pair
                (loop (+ i 1) (cons c stack)))))))
```

## Erlang

```erlang
-module(solution).
-export([make_good/1]).

-spec make_good(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
make_good(S) ->
    Stack = lists:foldl(
        fun(C, Acc) ->
            case Acc of
                [] -> [C];
                [H|T] when is_opposite(H, C) -> T;
                _ -> [C|Acc]
            end
        end,
        [],
        unicode:characters_to_list(S)
    ),
    Result = lists:reverse(Stack),
    unicode:characters_to_binary(Result).

is_opposite(C1, C2) ->
    erlang:abs(C1 - C2) =:= 32.
```

## Elixir

```elixir
defmodule Solution do
  @spec make_good(s :: String.t()) :: String.t()
  def make_good(s) do
    s
    |> String.to_charlist()
    |> Enum.reduce([], fn c, stack ->
      case stack do
        [h | t] when bad_pair?(h, c) -> t
        _ -> [c | stack]
      end
    end)
    |> Enum.reverse()
    |> List.to_string()
  end

  defp bad_pair?(a, b) do
    diff = a - b
    diff == 32 or diff == -32
  end
end
```

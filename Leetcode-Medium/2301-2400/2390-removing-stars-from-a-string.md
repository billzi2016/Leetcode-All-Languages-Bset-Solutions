# 2390. Removing Stars From a String

## Cpp

```cpp
class Solution {
public:
    string removeStars(string s) {
        string stack;
        stack.reserve(s.size());
        for (char c : s) {
            if (c == '*') {
                if (!stack.empty()) stack.pop_back();
            } else {
                stack.push_back(c);
            }
        }
        return stack;
    }
};
```

## Java

```java
class Solution {
    public String removeStars(String s) {
        int n = s.length();
        char[] stack = new char[n];
        int top = 0;
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '*') {
                if (top > 0) top--;
            } else {
                stack[top++] = c;
            }
        }
        return new String(stack, 0, top);
    }
}
```

## Python

```python
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if ch == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
```

## Python3

```python
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* removeStars(char* s) {
    int n = strlen(s);
    char *stack = (char*)malloc(n * sizeof(char));
    int top = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == '*') {
            if (top > 0) --top;
        } else {
            stack[top++] = s[i];
        }
    }
    char *res = (char*)malloc((top + 1) * sizeof(char));
    memcpy(res, stack, top);
    res[top] = '\0';
    free(stack);
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string RemoveStars(string s)
    {
        var sb = new System.Text.StringBuilder(s.Length);
        foreach (char c in s)
        {
            if (c == '*')
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
var removeStars = function(s) {
    const stack = [];
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (ch === '*') {
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
function removeStars(s: string): string {
    const stack: string[] = [];
    for (const ch of s) {
        if (ch === '*') {
            if (stack.length > 0) {
                stack.pop();
            }
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
    function removeStars($s) {
        $stack = [];
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if ($c === '*') {
                array_pop($stack);
            } else {
                $stack[] = $c;
            }
        }
        return implode('', $stack);
    }
}
```

## Swift

```swift
class Solution {
    func removeStars(_ s: String) -> String {
        var stack = [Character]()
        for ch in s {
            if ch == "*" {
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
    fun removeStars(s: String): String {
        val sb = StringBuilder()
        for (ch in s) {
            if (ch == '*') {
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
  String removeStars(String s) {
    List<String> stack = [];
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '*') {
        if (stack.isNotEmpty) {
          stack.removeLast();
        }
      } else {
        stack.add(s[i]);
      }
    }
    return stack.join('');
  }
}
```

## Golang

```go
func removeStars(s string) string {
    stack := make([]byte, 0, len(s))
    for i := 0; i < len(s); i++ {
        c := s[i]
        if c == '*' {
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
def remove_stars(s)
  stack = []
  s.each_char do |ch|
    if ch == '*'
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
    def removeStars(s: String): String = {
        val sb = new java.lang.StringBuilder()
        for (ch <- s) {
            if (ch == '*') {
                if (sb.length > 0) sb.setLength(sb.length - 1)
            } else {
                sb.append(ch)
            }
        }
        sb.toString
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_stars(s: String) -> String {
        let mut stack = Vec::with_capacity(s.len());
        for c in s.chars() {
            if c == '*' {
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
(define/contract (remove-stars s)
  (-> string? string?)
  (let loop ((chars (string->list s))
             (stack '()))
    (if (null? chars)
        (list->string (reverse stack))
        (let ((c (car chars)))
          (if (char=? c #\*)
              (loop (cdr chars) (if (null? stack) stack (cdr stack)))
              (loop (cdr chars) (cons c stack)))))))
```

## Erlang

```erlang
-module(solution).
-export([remove_stars/1]).

-spec remove_stars(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
remove_stars(S) ->
    List = binary_to_list(S),
    Processed = process(List, []),
    list_to_binary(lists:reverse(Processed)).

process([], Acc) -> Acc;
process([H|T], Acc) when H =:= $* ->
    case Acc of
        [_|Rest] -> process(T, Rest);
        [] -> process(T, [])
    end;
process([H|T], Acc) ->
    process(T, [H|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_stars(String.t()) :: String.t()
  def remove_stars(s) do
    s
    |> String.graphemes()
    |> Enum.reduce([], fn
      "*", [_ | rest] -> rest
      char, acc -> [char | acc]
    end)
    |> Enum.reverse()
    |> Enum.join()
  end
end
```

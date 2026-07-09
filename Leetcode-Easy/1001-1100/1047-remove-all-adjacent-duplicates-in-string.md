# 1047. Remove All Adjacent Duplicates In String

## Cpp

```cpp
class Solution {
public:
    std::string removeDuplicates(std::string s) {
        std::string stack;
        stack.reserve(s.size());
        for (char c : s) {
            if (!stack.empty() && stack.back() == c) {
                stack.pop_back();
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
    public String removeDuplicates(String s) {
        int n = s.length();
        char[] stack = new char[n];
        int top = -1;
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (top >= 0 && stack[top] == c) {
                top--;
            } else {
                stack[++top] = c;
            }
        }
        return new String(stack, 0, top + 1);
    }
}
```

## Python

```python
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
```

## Python3

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* removeDuplicates(char* s) {
    int n = strlen(s);
    char *stack = (char*)malloc(n + 1);
    if (!stack) return NULL;
    int top = 0;
    for (int i = 0; i < n; ++i) {
        if (top > 0 && stack[top - 1] == s[i]) {
            --top;
        } else {
            stack[top++] = s[i];
        }
    }
    stack[top] = '\0';
    return stack;
}
```

## Csharp

```csharp
public class Solution {
    public string RemoveDuplicates(string s) {
        int n = s.Length;
        char[] stack = new char[n];
        int top = 0;
        foreach (char c in s) {
            if (top > 0 && stack[top - 1] == c) {
                top--;
            } else {
                stack[top++] = c;
            }
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
var removeDuplicates = function(s) {
    const stack = [];
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (stack.length && stack[stack.length - 1] === ch) {
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
function removeDuplicates(s: string): string {
    const stack: string[] = [];
    for (const ch of s) {
        if (stack.length && stack[stack.length - 1] === ch) {
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
    function removeDuplicates($s) {
        $stack = [];
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (!empty($stack) && end($stack) === $c) {
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
    func removeDuplicates(_ s: String) -> String {
        var stack = [Character]()
        stack.reserveCapacity(s.count)
        for ch in s {
            if let last = stack.last, last == ch {
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
    fun removeDuplicates(s: String): String {
        val n = s.length
        val stack = CharArray(n)
        var idx = 0
        for (ch in s) {
            if (idx > 0 && stack[idx - 1] == ch) {
                idx--
            } else {
                stack[idx++] = ch
            }
        }
        return String(stack, 0, idx)
    }
}
```

## Dart

```dart
class Solution {
  String removeDuplicates(String s) {
    List<String> stack = [];
    for (int i = 0; i < s.length; i++) {
      String ch = s[i];
      if (stack.isNotEmpty && stack.last == ch) {
        stack.removeLast();
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
func removeDuplicates(s string) string {
    stack := make([]byte, 0, len(s))
    for i := 0; i < len(s); i++ {
        c := s[i]
        if len(stack) > 0 && stack[len(stack)-1] == c {
            stack = stack[:len(stack)-1]
        } else {
            stack = append(stack, c)
        }
    }
    return string(stack)
}
```

## Ruby

```ruby
def remove_duplicates(s)
  stack = []
  s.each_char do |ch|
    if !stack.empty? && stack[-1] == ch
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
    def removeDuplicates(s: String): String = {
        val n = s.length
        val stack = new Array[Char](n)
        var top = -1
        for (ch <- s) {
            if (top >= 0 && stack(top) == ch) {
                top -= 1
            } else {
                top += 1
                stack(top) = ch
            }
        }
        new String(stack, 0, top + 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_duplicates(s: String) -> String {
        let mut stack: Vec<char> = Vec::with_capacity(s.len());
        for ch in s.chars() {
            if matches!(stack.last(), Some(&last) if last == ch) {
                stack.pop();
            } else {
                stack.push(ch);
            }
        }
        stack.iter().collect()
    }
}
```

## Racket

```racket
(define/contract (remove-duplicates s)
  (-> string? string?)
  (let loop ((chars (string->list s)) (stack '()))
    (if (null? chars)
        (list->string (reverse stack))
        (let ((c (car chars)))
          (if (and (not (null? stack)) (char=? (car stack) c))
              (loop (cdr chars) (cdr stack))
              (loop (cdr chars) (cons c stack)))))))
```

## Erlang

```erlang
-module(solution).
-export([remove_duplicates/1]).

-spec remove_duplicates(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
remove_duplicates(S) ->
    List = binary_to_list(S),
    Stack = process(List, []),
    list_to_binary(lists:reverse(Stack)).

process([], Stack) -> Stack;
process([C|Rest], [Top|Tail]) when C =:= Top ->
    process(Rest, Tail);
process([C|Rest], Stack) ->
    process(Rest, [C|Stack]).
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_duplicates(s :: String.t) :: String.t
  def remove_duplicates(s) do
    s
    |> String.graphemes()
    |> Enum.reduce([], fn ch, acc ->
      case acc do
        [^ch | rest] -> rest
        _ -> [ch | acc]
      end
    end)
    |> Enum.reverse()
    |> Enum.join()
  end
end
```

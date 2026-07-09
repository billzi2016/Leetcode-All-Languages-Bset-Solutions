# 1003. Check If Word Is Valid After Substitutions

## Cpp

```cpp
class Solution {
public:
    bool isValid(string s) {
        vector<char> st;
        for (char ch : s) {
            st.push_back(ch);
            int n = st.size();
            if (n >= 3 && st[n-3] == 'a' && st[n-2] == 'b' && st[n-1] == 'c') {
                st.pop_back();
                st.pop_back();
                st.pop_back();
            }
        }
        return st.empty();
    }
};
```

## Java

```java
class Solution {
    public boolean isValid(String s) {
        int n = s.length();
        char[] stack = new char[n];
        int idx = 0;
        for (int i = 0; i < n; i++) {
            stack[idx++] = s.charAt(i);
            if (idx >= 3 &&
                stack[idx - 3] == 'a' &&
                stack[idx - 2] == 'b' &&
                stack[idx - 1] == 'c') {
                idx -= 3;
            }
        }
        return idx == 0;
    }
}
```

## Python

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= 3 and stack[-3] == 'a' and stack[-2] == 'b' and stack[-1] == 'c':
                stack.pop()
                stack.pop()
                stack.pop()
        return not stack
```

## Python3

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= 3 and stack[-3] == 'a' and stack[-2] == 'b' and stack[-1] == 'c':
                stack.pop()
                stack.pop()
                stack.pop()
        return not stack
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool isValid(char* s) {
    int n = strlen(s);
    char stack[20005];
    int top = 0;
    for (int i = 0; i < n; ++i) {
        stack[top++] = s[i];
        while (top >= 3 &&
               stack[top - 3] == 'a' &&
               stack[top - 2] == 'b' &&
               stack[top - 1] == 'c') {
            top -= 3;
        }
    }
    return top == 0;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsValid(string s)
    {
        char[] stack = new char[s.Length];
        int top = 0;
        foreach (char ch in s)
        {
            stack[top++] = ch;
            if (top >= 3 && stack[top - 3] == 'a' && stack[top - 2] == 'b' && stack[top - 1] == 'c')
            {
                top -= 3;
            }
        }
        return top == 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];
    for (const ch of s) {
        stack.push(ch);
        if (stack.length >= 3) {
            const n = stack.length;
            if (stack[n - 3] === 'a' && stack[n - 2] === 'b' && stack[n - 1] === 'c') {
                stack.pop();
                stack.pop();
                stack.pop();
            }
        }
    }
    return stack.length === 0;
};
```

## Typescript

```typescript
function isValid(s: string): boolean {
    const stack: string[] = [];
    for (const ch of s) {
        stack.push(ch);
        const n = stack.length;
        if (n >= 3 && stack[n - 3] === 'a' && stack[n - 2] === 'b' && stack[n - 1] === 'c') {
            stack.pop();
            stack.pop();
            stack.pop();
        }
    }
    return stack.length === 0;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isValid($s) {
        $stack = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $stack[] = $s[$i];
            $cnt = count($stack);
            if ($cnt >= 3 &&
                $stack[$cnt - 3] === 'a' &&
                $stack[$cnt - 2] === 'b' &&
                $stack[$cnt - 1] === 'c') {
                array_pop($stack);
                array_pop($stack);
                array_pop($stack);
            }
        }
        return empty($stack);
    }
}
```

## Swift

```swift
class Solution {
    func isValid(_ s: String) -> Bool {
        var stack = [Character]()
        for ch in s {
            stack.append(ch)
            if stack.count >= 3,
               stack[stack.count - 3] == "a",
               stack[stack.count - 2] == "b",
               stack[stack.count - 1] == "c" {
                stack.removeLast(3)
            }
        }
        return stack.isEmpty
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isValid(s: String): Boolean {
        val stack = StringBuilder()
        for (ch in s) {
            stack.append(ch)
            if (stack.length >= 3 &&
                stack[stack.length - 3] == 'a' &&
                stack[stack.length - 2] == 'b' &&
                stack[stack.length - 1] == 'c') {
                stack.delete(stack.length - 3, stack.length)
            }
        }
        return stack.isEmpty()
    }
}
```

## Dart

```dart
class Solution {
  bool isValid(String s) {
    List<String> stack = [];
    for (int i = 0; i < s.length; i++) {
      String ch = s[i];
      stack.add(ch);
      int n = stack.length;
      if (n >= 3 &&
          stack[n - 3] == 'a' &&
          stack[n - 2] == 'b' &&
          stack[n - 1] == 'c') {
        stack.removeRange(n - 3, n);
      }
    }
    return stack.isEmpty;
  }
}
```

## Golang

```go
func isValid(s string) bool {
	stack := make([]byte, 0, len(s))
	for i := 0; i < len(s); i++ {
		c := s[i]
		stack = append(stack, c)
		if len(stack) >= 3 &&
			stack[len(stack)-3] == 'a' &&
			stack[len(stack)-2] == 'b' &&
			stack[len(stack)-1] == 'c' {
			stack = stack[:len(stack)-3]
		}
	}
	return len(stack) == 0
}
```

## Ruby

```ruby
def is_valid(s)
  stack = []
  s.each_char do |ch|
    stack << ch
    if stack.size >= 3 && stack[-3] == 'a' && stack[-2] == 'b' && stack[-1] == 'c'
      stack.pop(3)
    end
  end
  stack.empty?
end
```

## Scala

```scala
object Solution {
    def isValid(s: String): Boolean = {
        val n = s.length
        val stack = new Array[Char](n)
        var top = 0
        for (ch <- s) {
            stack(top) = ch
            top += 1
            if (top >= 3 && stack(top - 3) == 'a' && stack(top - 2) == 'b' && stack(top - 1) == 'c') {
                top -= 3
            }
        }
        top == 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = Vec::new();
        for ch in s.chars() {
            stack.push(ch);
            while stack.len() >= 3 {
                let len = stack.len();
                if stack[len - 3] == 'a' && stack[len - 2] == 'b' && stack[len - 1] == 'c' {
                    stack.pop();
                    stack.pop();
                    stack.pop();
                } else {
                    break;
                }
            }
        }
        stack.is_empty()
    }
}
```

## Racket

```racket
(define/contract (is-valid s)
  (-> string? boolean?)
  (let loop ((chars (string->list s))
             (stack '()))
    (if (null? chars)
        (null? stack)
        (let ((new-stack (cons (car chars) stack)))
          (if (and (pair? new-stack)
                   (pair? (cdr new-stack))
                   (pair? (cddr new-stack))
                   (eq? (first new-stack) #\c)
                   (eq? (cadr new-stack) #\b)
                   (eq? (caddr new-stack) #\a))
              (loop (cdr chars) (cdddr new-stack))
              (loop (cdr chars) new-stack))))))
```

## Erlang

```erlang
-module(solution).
-export([is_valid/1]).

-spec is_valid(S :: unicode:unicode_binary()) -> boolean().
is_valid(S) ->
    case process(S, []) of
        [] -> true;
        _  -> false
    end.

process(<<>>, Stack) ->
    Stack;
process(<<C, Rest/binary>>, Stack) ->
    NewStack = [C | Stack],
    case NewStack of
        [$c, $b, $a | Tail] ->
            process(Rest, Tail);
        _ ->
            process(Rest, NewStack)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_valid(s :: String.t) :: boolean
  def is_valid(s) do
    s
    |> String.graphemes()
    |> Enum.reduce([], fn ch, stack ->
      case [ch | stack] do
        ["c", "b", "a" | rest] -> rest
        new_stack -> new_stack
      end
    end)
    |> Enum.empty?()
  end
end
```

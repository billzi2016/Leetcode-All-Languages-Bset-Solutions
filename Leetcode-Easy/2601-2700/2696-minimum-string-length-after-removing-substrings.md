# 2696. Minimum String Length After Removing Substrings

## Cpp

```cpp
class Solution {
public:
    int minLength(string s) {
        vector<char> st;
        for (char c : s) {
            if (!st.empty() && ((c == 'B' && st.back() == 'A') || (c == 'D' && st.back() == 'C'))) {
                st.pop_back();
            } else {
                st.push_back(c);
            }
        }
        return (int)st.size();
    }
};
```

## Java

```java
class Solution {
    public int minLength(String s) {
        char[] stack = new char[s.length()];
        int top = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (top > 0 && ((c == 'B' && stack[top - 1] == 'A') || (c == 'D' && stack[top - 1] == 'C'))) {
                top--; // remove the pair
            } else {
                stack[top++] = c;
            }
        }
        return top;
    }
}
```

## Python

```python
class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for ch in s:
            if (ch == 'B' and stack and stack[-1] == 'A') or (ch == 'D' and stack and stack[-1] == 'C'):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)
```

## Python3

```python
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for ch in s:
            if stack:
                top = stack[-1]
                if (top == 'A' and ch == 'B') or (top == 'C' and ch == 'D'):
                    stack.pop()
                    continue
            stack.append(ch)
        return len(stack)
```

## C

```c
int minLength(char* s) {
    int n = 0;
    while (s[n] != '\0') ++n;
    int sz = 0;
    for (int i = 0; i < n; ++i) {
        char c = s[i];
        if (sz > 0 && ((s[sz - 1] == 'A' && c == 'B') ||
                       (s[sz - 1] == 'C' && c == 'D'))) {
            --sz; // remove the matching pair
        } else {
            s[sz++] = c;
        }
    }
    return sz;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinLength(string s)
    {
        char[] stack = new char[s.Length];
        int top = -1;
        foreach (char c in s)
        {
            if (top >= 0 && ((stack[top] == 'A' && c == 'B') || (stack[top] == 'C' && c == 'D')))
            {
                top--;
            }
            else
            {
                stack[++top] = c;
            }
        }
        return top + 1;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minLength = function(s) {
    const stack = [];
    for (const ch of s) {
        if (stack.length > 0) {
            const top = stack[stack.length - 1];
            if ((ch === 'B' && top === 'A') || (ch === 'D' && top === 'C')) {
                stack.pop();
                continue;
            }
        }
        stack.push(ch);
    }
    return stack.length;
};
```

## Typescript

```typescript
function minLength(s: string): number {
    const stack: string[] = [];
    for (const ch of s) {
        if (
            stack.length > 0 &&
            ((ch === 'B' && stack[stack.length - 1] === 'A') ||
             (ch === 'D' && stack[stack.length - 1] === 'C'))
        ) {
            stack.pop();
        } else {
            stack.push(ch);
        }
    }
    return stack.length;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function minLength($s) {
        $stack = [];
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (!empty($stack)) {
                $top = end($stack);
                if (($c === 'B' && $top === 'A') || ($c === 'D' && $top === 'C')) {
                    array_pop($stack);
                    continue;
                }
            }
            $stack[] = $c;
        }
        return count($stack);
    }
}
```

## Swift

```swift
class Solution {
    func minLength(_ s: String) -> Int {
        var stack = [Character]()
        for ch in s {
            if let last = stack.last, (last == "A" && ch == "B") || (last == "C" && ch == "D") {
                stack.removeLast()
            } else {
                stack.append(ch)
            }
        }
        return stack.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minLength(s: String): Int {
        val stack = CharArray(s.length)
        var top = 0
        for (ch in s) {
            if (top > 0 && ((ch == 'B' && stack[top - 1] == 'A') || (ch == 'D' && stack[top - 1] == 'C'))) {
                top--
            } else {
                stack[top++] = ch
            }
        }
        return top
    }
}
```

## Dart

```dart
class Solution {
  int minLength(String s) {
    List<String> stack = [];
    for (int i = 0; i < s.length; i++) {
      String ch = s[i];
      if (stack.isNotEmpty) {
        String top = stack.last;
        if ((top == 'A' && ch == 'B') || (top == 'C' && ch == 'D')) {
          stack.removeLast();
          continue;
        }
      }
      stack.add(ch);
    }
    return stack.length;
  }
}
```

## Golang

```go
func minLength(s string) int {
	stack := make([]byte, 0, len(s))
	for i := 0; i < len(s); i++ {
		c := s[i]
		if len(stack) > 0 && ((c == 'B' && stack[len(stack)-1] == 'A') || (c == 'D' && stack[len(stack)-1] == 'C')) {
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, c)
		}
	}
	return len(stack)
}
```

## Ruby

```ruby
# @param {String} s
# @return {Integer}
def min_length(s)
  stack = []
  s.each_char do |ch|
    if !stack.empty? && ((ch == 'B' && stack[-1] == 'A') || (ch == 'D' && stack[-1] == 'C'))
      stack.pop
    else
      stack << ch
    end
  end
  stack.size
end
```

## Scala

```scala
object Solution {
  def minLength(s: String): Int = {
    val sb = new java.lang.StringBuilder
    for (c <- s) {
      if (sb.length > 0 && ((c == 'B' && sb.charAt(sb.length - 1) == 'A') ||
                            (c == 'D' && sb.charAt(sb.length - 1) == 'C'))) {
        sb.setLength(sb.length - 1)
      } else {
        sb.append(c)
      }
    }
    sb.length
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_length(s: String) -> i32 {
        let mut stack: Vec<char> = Vec::new();
        for ch in s.chars() {
            if let Some(&last) = stack.last() {
                if (last == 'A' && ch == 'B') || (last == 'C' && ch == 'D') {
                    stack.pop();
                    continue;
                }
            }
            stack.push(ch);
        }
        stack.len() as i32
    }
}
```

## Racket

```racket
(define/contract (min-length s)
  (-> string? exact-integer?)
  (let loop ((chars (string->list s)) (stack '()))
    (if (null? chars)
        (length stack)
        (let ((ch (car chars)))
          (if (and (not (null? stack))
                   (or (and (char=? (car stack) #\A) (char=? ch #\B))
                       (and (char=? (car stack) #\C) (char=? ch #\D))))
              (loop (cdr chars) (cdr stack)) ; remove the pair
              (loop (cdr chars) (cons ch stack)))))))
```

## Erlang

```erlang
-spec min_length(S :: unicode:unicode_binary()) -> integer().
min_length(S) ->
    List = binary_to_list(S),
    Stack = lists:foldl(
        fun(C, Acc) ->
            case Acc of
                [] -> [C];
                [Prev|Rest] ->
                    if (Prev == $A andalso C == $B) orelse (Prev == $C andalso C == $D) ->
                            Rest;
                       true ->
                            [C|Acc]
                    end
            end
        end,
        [],
        List),
    length(Stack).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_length(s :: String.t()) :: integer()
  def min_length(s) do
    s
    |> String.to_charlist()
    |> Enum.reduce([], fn c, stack ->
      case {c, stack} do
        {?B, [?A | rest]} -> rest
        {?D, [?C | rest]} -> rest
        _ -> [c | stack]
      end
    end)
    |> length()
  end
end
```

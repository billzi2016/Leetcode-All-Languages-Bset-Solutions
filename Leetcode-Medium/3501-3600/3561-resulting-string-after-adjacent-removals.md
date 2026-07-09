# 3561. Resulting String After Adjacent Removals

## Cpp

```cpp
class Solution {
public:
    bool consecutive(char a, char b) {
        int diff = abs(a - b);
        return diff == 1 || (a == 'a' && b == 'z') || (a == 'z' && b == 'a');
    }
    
    string resultingString(string s) {
        vector<char> st;
        st.reserve(s.size());
        for (char c : s) {
            st.push_back(c);
            while (st.size() >= 2 && consecutive(st[st.size() - 1], st[st.size() - 2])) {
                st.pop_back();
                st.pop_back();
            }
        }
        return string(st.begin(), st.end());
    }
};
```

## Java

```java
class Solution {
    public String resultingString(String s) {
        char[] stack = new char[s.length()];
        int top = -1;
        for (int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            if (top >= 0) {
                char prev = stack[top];
                int diff = Math.abs(prev - cur);
                if (diff == 1 || diff == 25) { // consecutive letters (circular)
                    top--; // remove the previous character, skip current
                    continue;
                }
            }
            stack[++top] = cur;
        }
        return new String(stack, 0, top + 1);
    }
}
```

## Python

```python
class Solution(object):
    def resultingString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if stack:
                top = stack[-1]
                diff = abs(ord(top) - ord(ch))
                if diff == 1 or (top == 'a' and ch == 'z') or (top == 'z' and ch == 'a'):
                    stack.pop()
                    continue
            stack.append(ch)
        return ''.join(stack)
```

## Python3

```python
class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack:
                prev = stack[-1]
                diff = abs(ord(prev) - ord(ch))
                if diff == 1 or diff == 25:  # consecutive letters (circular)
                    stack.pop()
                    continue
            stack.append(ch)
        return ''.join(stack)
```

## C

```c
#include <stdlib.h>
#include <string.h>

static inline int isConsecutive(char a, char b) {
    if ((a == 'a' && b == 'z') || (a == 'z' && b == 'a')) return 1;
    return abs(a - b) == 1;
}

char* resultingString(char* s) {
    size_t n = strlen(s);
    char *stack = (char*)malloc(n);
    size_t top = 0;

    for (size_t i = 0; i < n; ++i) {
        char c = s[i];
        if (top > 0 && isConsecutive(stack[top - 1], c)) {
            --top; // remove the previous character, discard current
        } else {
            stack[top++] = c;
        }
    }

    char *res = (char*)malloc(top + 1);
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
    public string ResultingString(string s)
    {
        int n = s.Length;
        char[] stack = new char[n];
        int top = 0;

        foreach (char ch in s)
        {
            stack[top++] = ch;
            while (top >= 2 && IsConsecutive(stack[top - 2], stack[top - 1]))
            {
                top -= 2;
            }
        }

        return new string(stack, 0, top);
    }

    private bool IsConsecutive(char a, char b)
    {
        int diff = Math.Abs(a - b);
        if (diff == 1) return true;
        return (a == 'a' && b == 'z') || (a == 'z' && b == 'a');
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var resultingString = function(s) {
    const stack = [];
    for (let i = 0; i < s.length; ++i) {
        const cur = s[i];
        if (stack.length) {
            const top = stack[stack.length - 1];
            const diff = Math.abs(top.charCodeAt(0) - cur.charCodeAt(0));
            if (diff === 1 || (top === 'a' && cur === 'z') || (top === 'z' && cur === 'a')) {
                stack.pop(); // remove both top and current
                continue;
            }
        }
        stack.push(cur);
    }
    return stack.join('');
};
```

## Typescript

```typescript
function resultingString(s: string): string {
    const stack: string[] = [];
    const isConsecutive = (a: string, b: string): boolean => {
        const diff = Math.abs(a.charCodeAt(0) - b.charCodeAt(0));
        return diff === 1 || diff === 25;
    };
    for (const ch of s) {
        if (stack.length && isConsecutive(stack[stack.length - 1], ch)) {
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
    function resultingString($s) {
        $stack = [];
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if (!empty($stack)) {
                $top = end($stack);
                $diff = abs(ord($top) - ord($ch));
                if ($diff == 1 || $diff == 25) { // consecutive (including circular a-z)
                    array_pop($stack);
                    continue;
                }
            }
            $stack[] = $ch;
        }
        return implode('', $stack);
    }
}
```

## Swift

```swift
class Solution {
    func resultingString(_ s: String) -> String {
        var stack = [UInt8]()
        for ch in s.utf8 {
            if let last = stack.last, isConsecutive(last, ch) {
                stack.removeLast()
            } else {
                stack.append(ch)
            }
        }
        return String(bytes: stack, encoding: .utf8)!
    }
    
    private func isConsecutive(_ a: UInt8, _ b: UInt8) -> Bool {
        if (a == 97 && b == 122) || (a == 122 && b == 97) { // 'a' and 'z'
            return true
        }
        let diff = Int(a) - Int(b)
        return abs(diff) == 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun resultingString(s: String): String {
        val stack = CharArray(s.length)
        var top = 0
        for (ch in s) {
            if (top > 0 && isConsecutive(stack[top - 1], ch)) {
                top--
            } else {
                stack[top++] = ch
            }
        }
        return String(stack, 0, top)
    }

    private fun isConsecutive(a: Char, b: Char): Boolean {
        val diff = kotlin.math.abs(a - b)
        return diff == 1 || diff == 25
    }
}
```

## Dart

```dart
class Solution {
  String resultingString(String s) {
    List<int> stack = [];
    for (int i = 0; i < s.length; i++) {
      int cur = s.codeUnitAt(i);
      if (stack.isNotEmpty && _isAdjacent(stack.last, cur)) {
        stack.removeLast();
      } else {
        stack.add(cur);
      }
    }
    return String.fromCharCodes(stack);
  }

  bool _isAdjacent(int a, int b) {
    if ((a - b).abs() == 1) return true;
    // circular adjacency between 'a' (97) and 'z' (122)
    return (a == 97 && b == 122) || (a == 122 && b == 97);
  }
}
```

## Golang

```go
func resultingString(s string) string {
    stack := make([]byte, 0, len(s))
    for i := 0; i < len(s); i++ {
        c := s[i]
        if n := len(stack); n > 0 {
            top := stack[n-1]
            diff := (int(top) - int(c) + 26) % 26
            if diff == 1 || diff == 25 {
                stack = stack[:n-1]
                continue
            }
        }
        stack = append(stack, c)
    }
    return string(stack)
}
```

## Ruby

```ruby
def resulting_string(s)
  stack = []
  s.each_char do |c|
    if !stack.empty? && ((stack[-1].ord - c.ord).abs == 1 || (stack[-1].ord - c.ord).abs == 25)
      stack.pop
    else
      stack << c
    end
  end
  stack.join
end
```

## Scala

```scala
object Solution {
    def resultingString(s: String): String = {
        val sb = new java.lang.StringBuilder
        for (ch <- s) {
            if (sb.length > 0) {
                val last = sb.charAt(sb.length - 1)
                val diff = Math.abs(last - ch)
                if (diff == 1 || diff == 25) {
                    sb.setLength(sb.length - 1) // remove the pair
                } else {
                    sb.append(ch)
                }
            } else {
                sb.append(ch)
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn resulting_string(s: String) -> String {
        fn consecutive(a: char, b: char) -> bool {
            (a == 'a' && b == 'z') || (a == 'z' && b == 'a') || ((a as i32 - b as i32).abs() == 1)
        }

        let mut stack: Vec<char> = Vec::new();
        for ch in s.chars() {
            if let Some(&last) = stack.last() {
                if consecutive(last, ch) {
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
(define/contract (resulting-string s)
  (-> string? string?)
  (let* ((len (string-length s))
         (stack (make-vector len))
         (top -1))
    (for ([i (in-range len)])
      (let ((c (string-ref s i)))
        (if (and (> top -1)
                 (let ((t (vector-ref stack top)))
                   (or (= (abs (- (char->integer t) (char->integer c))) 1)
                       (or (and (char=? t #\a) (char=? c #\z))
                           (and (char=? t #\z) (char=? c #\a))))))
            (set! top (- top 1))
            (begin
              (set! top (+ top 1))
              (vector-set! stack top c)))))
    (let ((result (make-string (+ top 1) #\space)))
      (for ([i (in-range (+ top 1))])
        (string-set! result i (vector-ref stack i)))
      result)))
```

## Erlang

```erlang
-spec resulting_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
resulting_string(S) ->
    Stack = process(S, []),
    list_to_binary(lists:reverse(Stack)).

process(<<>>, Stack) ->
    Stack;
process(<<C, Rest/binary>>, []) ->
    process(Rest, [C]);
process(<<C, Rest/binary>>, [Top|Tail]) ->
    case consecutive(C, Top) of
        true  -> process(Rest, Tail);
        false -> process(Rest, [C, Top | Tail])
    end.

consecutive(A, B) ->
    D = ((A - B) + 26) rem 26,
    D == 1 orelse D == 25.
```

## Elixir

```elixir
defmodule Solution do
  @spec resulting_string(s :: String.t()) :: String.t()
  def resulting_string(s) do
    s
    |> String.to_charlist()
    |> Enum.reduce([], fn c, stack ->
      case stack do
        [top | rest] when adjacent?(c, top) -> rest
        _ -> [c | stack]
      end
    end)
    |> Enum.reverse()
    |> List.to_string()
  end

  defp adjacent?(a, b) do
    diff = abs(a - b)
    diff == 1 or diff == 25
  end
end
```

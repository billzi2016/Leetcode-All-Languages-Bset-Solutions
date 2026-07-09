# 1910. Remove All Occurrences of a Substring

## Cpp

```cpp
class Solution {
public:
    string removeOccurrences(string s, string part) {
        int m = part.size();
        vector<char> stk;
        stk.reserve(s.size());
        for (char c : s) {
            stk.push_back(c);
            if ((int)stk.size() >= m) {
                bool match = true;
                for (int i = 0; i < m; ++i) {
                    if (stk[stk.size() - m + i] != part[i]) {
                        match = false;
                        break;
                    }
                }
                if (match) {
                    for (int i = 0; i < m; ++i) stk.pop_back();
                }
            }
        }
        return string(stk.begin(), stk.end());
    }
};
```

## Java

```java
class Solution {
    public String removeOccurrences(String s, String part) {
        int n = s.length();
        int m = part.length();
        char[] stack = new char[n];
        int top = 0;
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            stack[top++] = c;
            if (top >= m) {
                boolean match = true;
                for (int j = 0; j < m; j++) {
                    if (stack[top - m + j] != part.charAt(j)) {
                        match = false;
                        break;
                    }
                }
                if (match) {
                    top -= m;
                }
            }
        }
        return new String(stack, 0, top);
    }
}
```

## Python

```python
class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        stack = []
        plen = len(part)
        last_char = part[-1]
        for ch in s:
            stack.append(ch)
            if ch == last_char and len(stack) >= plen:
                match = True
                start = len(stack) - plen
                for i in range(plen):
                    if stack[start + i] != part[i]:
                        match = False
                        break
                if match:
                    del stack[-plen:]
        return ''.join(stack)
```

## Python3

```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= n and ''.join(stack[-n:]) == part:
                del stack[-n:]
        return ''.join(stack)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* removeOccurrences(char* s, char* part) {
    int n = strlen(s);
    int m = strlen(part);
    char *stack = (char *)malloc(n + 1); // maximum possible length
    int top = 0;

    for (int i = 0; i < n; ++i) {
        stack[top++] = s[i];
        if (top >= m && stack[top - 1] == part[m - 1]) {
            int j;
            for (j = 0; j < m; ++j) {
                if (stack[top - m + j] != part[j])
                    break;
            }
            if (j == m) {
                top -= m; // remove the matched substring
            }
        }
    }

    stack[top] = '\0';
    return stack;
}
```

## Csharp

```csharp
public class Solution
{
    public string RemoveOccurrences(string s, string part)
    {
        int m = part.Length;
        var sb = new System.Text.StringBuilder();

        foreach (char c in s)
        {
            sb.Append(c);
            if (sb.Length >= m && sb[sb.Length - 1] == part[m - 1])
            {
                bool match = true;
                for (int i = 0; i < m; i++)
                {
                    if (sb[sb.Length - m + i] != part[i])
                    {
                        match = false;
                        break;
                    }
                }
                if (match)
                {
                    sb.Length -= m;
                }
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
 * @param {string} part
 * @return {string}
 */
var removeOccurrences = function(s, part) {
    const m = part.length;
    const stack = [];
    for (let ch of s) {
        stack.push(ch);
        if (stack.length >= m) {
            let match = true;
            for (let i = 0; i < m; i++) {
                if (stack[stack.length - m + i] !== part[i]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                stack.splice(stack.length - m, m);
            }
        }
    }
    return stack.join('');
};
```

## Typescript

```typescript
function removeOccurrences(s: string, part: string): string {
    const stack: string[] = [];
    const m = part.length;
    for (const ch of s) {
        stack.push(ch);
        if (stack.length >= m) {
            let match = true;
            for (let i = 0; i < m; i++) {
                if (stack[stack.length - m + i] !== part[i]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                for (let i = 0; i < m; i++) stack.pop();
            }
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
     * @param String $part
     * @return String
     */
    function removeOccurrences($s, $part) {
        $lenPart = strlen($part);
        if ($lenPart == 0) return $s;
        $stack = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $stack[] = $s[$i];
            if (count($stack) >= $lenPart) {
                $match = true;
                $startIdx = count($stack) - $lenPart;
                for ($j = 0; $j < $lenPart; $j++) {
                    if ($stack[$startIdx + $j] !== $part[$j]) {
                        $match = false;
                        break;
                    }
                }
                if ($match) {
                    for ($j = 0; $j < $lenPart; $j++) {
                        array_pop($stack);
                    }
                }
            }
        }
        return implode('', $stack);
    }
}
```

## Swift

```swift
class Solution {
    func removeOccurrences(_ s: String, _ part: String) -> String {
        let pattern = Array(part)
        var stack = [Character]()
        
        for ch in s {
            stack.append(ch)
            if stack.count >= pattern.count {
                var isMatch = true
                for i in 0..<pattern.count {
                    if stack[stack.count - pattern.count + i] != pattern[i] {
                        isMatch = false
                        break
                    }
                }
                if isMatch {
                    for _ in 0..<pattern.count {
                        stack.removeLast()
                    }
                }
            }
        }
        
        return String(stack)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeOccurrences(s: String, part: String): String {
        val m = part.length
        val sb = StringBuilder()
        for (ch in s) {
            sb.append(ch)
            if (sb.length >= m && sb.substring(sb.length - m) == part) {
                sb.delete(sb.length - m, sb.length)
            }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String removeOccurrences(String s, String part) {
    int m = part.length;
    List<String> stack = [];
    for (int i = 0; i < s.length; i++) {
      stack.add(s[i]);
      if (stack.length >= m) {
        bool match = true;
        for (int j = 0; j < m; j++) {
          if (stack[stack.length - m + j] != part[j]) {
            match = false;
            break;
          }
        }
        if (match) {
          for (int j = 0; j < m; j++) {
            stack.removeLast();
          }
        }
      }
    }
    return stack.join('');
  }
}
```

## Golang

```go
func removeOccurrences(s string, part string) string {
    n := len(s)
    m := len(part)
    if m == 0 || n < m {
        return s
    }
    stack := make([]byte, 0, n)
    pbytes := []byte(part)

    for i := 0; i < n; i++ {
        stack = append(stack, s[i])
        if len(stack) >= m {
            match := true
            start := len(stack) - m
            for j := 0; j < m; j++ {
                if stack[start+j] != pbytes[j] {
                    match = false
                    break
                }
            }
            if match {
                stack = stack[:start]
            }
        }
    }
    return string(stack)
}
```

## Ruby

```ruby
def remove_occurrences(s, part)
  p_len = part.length
  stack = []
  s.each_char do |ch|
    stack << ch
    if stack.size >= p_len && stack[-p_len, p_len].join == part
      p_len.times { stack.pop }
    end
  end
  stack.join
end
```

## Scala

```scala
object Solution {
    def removeOccurrences(s: String, part: String): String = {
        val m = part.length
        val sb = new java.lang.StringBuilder()
        for (c <- s) {
            sb.append(c)
            if (sb.length >= m && sb.substring(sb.length - m) == part) {
                sb.setLength(sb.length - m)
            }
        }
        sb.toString
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_occurrences(s: String, part: String) -> String {
        let mut stack: Vec<char> = Vec::new();
        let p: Vec<char> = part.chars().collect();
        let m = p.len();

        for ch in s.chars() {
            stack.push(ch);
            if stack.len() >= m {
                let start = stack.len() - m;
                if stack[start..].iter().zip(p.iter()).all(|(a, b)| a == b) {
                    for _ in 0..m {
                        stack.pop();
                    }
                }
            }
        }

        stack.iter().collect()
    }
}
```

## Racket

```racket
(define/contract (remove-occurrences s part)
  (-> string? string? string?)
  (let* ((n (string-length s))
         (m (string-length part)))
    (if (= m 0)
        s
        (let* ((rev-part (list->vector (reverse (string->list part))))
               (stack (make-vector n))
               (top 0))
          (for ([i (in-range n)])
            (vector-set! stack top (string-ref s i))
            (set! top (+ top 1))
            (when (>= top m)
              (let ((match? #t))
                (for ([k (in-range m)])
                  (when match?
                    (unless (char=? (vector-ref stack (- top k 1))
                                    (vector-ref rev-part k))
                      (set! match? #f))))
                (when match?
                  (set! top (- top m))))))
          (let ((result (make-string top)))
            (for ([j (in-range top)])
              (string-set! result j (vector-ref stack j)))
            result)))))
```

## Erlang

```erlang
-module(solution).
-export([remove_occurrences/2]).

-spec remove_occurrences(S :: unicode:unicode_binary(), Part :: unicode:unicode_binary()) ->
    unicode:unicode_binary().
remove_occurrences(S, Part) ->
    PartList = unicode:characters_to_list(Part),
    LenP = length(PartList),
    case LenP of
        0 -> S;
        _ ->
            PartRev = lists:reverse(PartList),
            Stack = process(unicode:characters_to_list(S), [], 0, PartRev, LenP),
            unicode:characters_to_binary(lists:reverse(Stack))
    end.

process([], Stack, _Size, _PartRev, _Len) -> Stack;
process([C|Rest], Stack, Size, PartRev, Len) ->
    NewStack = [C | Stack],
    NewSize = Size + 1,
    if
        NewSize >= Len,
        lists:sublist(NewStack, 1, Len) == PartRev ->
            process(Rest, drop(Len, NewStack), NewSize - Len, PartRev, Len);
        true ->
            process(Rest, NewStack, NewSize, PartRev, Len)
    end.

drop(0, L) -> L;
drop(N, [_|T]) when N > 0 -> drop(N-1, T).
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_occurrences(s :: String.t(), part :: String.t()) :: String.t()
  def remove_occurrences(s, part) do
    s_chars = String.to_charlist(s)
    p_chars = String.to_charlist(part)
    p_len = length(p_chars)

    if p_len == 0 do
      s
    else
      p_rev = Enum.reverse(p_chars)

      stack =
        Enum.reduce(s_chars, [], fn c, acc ->
          new_acc = [c | acc]

          if length(new_acc) >= p_len and Enum.take(new_acc, p_len) == p_rev do
            Enum.drop(new_acc, p_len)
          else
            new_acc
          end
        end)

      stack |> Enum.reverse() |> List.to_string()
    end
  end
end
```

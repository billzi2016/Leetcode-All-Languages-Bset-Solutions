# 1021. Remove Outermost Parentheses

## Cpp

```cpp
class Solution {
public:
    string removeOuterParentheses(string s) {
        string res;
        int depth = 0;
        for (char c : s) {
            if (c == '(') {
                if (depth > 0) res.push_back(c);
                ++depth;
            } else { // ')'
                --depth;
                if (depth > 0) res.push_back(c);
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder sb = new StringBuilder();
        int depth = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                if (depth > 0) {
                    sb.append(c);
                }
                depth++;
            } else { // c == ')'
                depth--;
                if (depth > 0) {
                    sb.append(c);
                }
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        depth = 0
        for ch in s:
            if ch == '(':
                if depth > 0:
                    result.append(ch)
                depth += 1
            else:  # ch == ')'
                depth -= 1
                if depth > 0:
                    result.append(ch)
        return ''.join(result)
```

## Python3

```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance = 0
        result = []
        for ch in s:
            if ch == '(':
                if balance > 0:
                    result.append(ch)
                balance += 1
            else:  # ch == ')'
                balance -= 1
                if balance > 0:
                    result.append(ch)
        return ''.join(result)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* removeOuterParentheses(char* s) {
    int n = strlen(s);
    char *res = (char*)malloc(n + 1);
    int bal = 0, idx = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == '(') {
            if (bal > 0) res[idx++] = s[i];
            ++bal;
        } else { // ')'
            --bal;
            if (bal > 0) res[idx++] = s[i];
        }
    }
    res[idx] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string RemoveOuterParentheses(string s)
    {
        var sb = new System.Text.StringBuilder();
        int depth = 0;
        foreach (char c in s)
        {
            if (c == '(')
            {
                if (depth > 0) sb.Append(c);
                depth++;
            }
            else // ')'
            {
                depth--;
                if (depth > 0) sb.Append(c);
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
var removeOuterParentheses = function(s) {
    let result = '';
    let depth = 0;
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (ch === '(') {
            if (depth > 0) result += ch;
            depth++;
        } else { // ')'
            depth--;
            if (depth > 0) result += ch;
        }
    }
    return result;
};
```

## Typescript

```typescript
function removeOuterParentheses(s: string): string {
    let result = "";
    let depth = 0;
    for (const ch of s) {
        if (ch === '(') {
            if (depth > 0) result += ch;
            depth++;
        } else { // ')'
            depth--;
            if (depth > 0) result += ch;
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function removeOuterParentheses($s) {
        $balance = 0;
        $result = '';
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if ($ch === '(') {
                if ($balance > 0) {
                    $result .= '(';
                }
                $balance++;
            } else { // ')'
                $balance--;
                if ($balance > 0) {
                    $result .= ')';
                }
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func removeOuterParentheses(_ s: String) -> String {
        var result = ""
        var depth = 0
        for ch in s {
            if ch == "(" {
                if depth > 0 { result.append(ch) }
                depth += 1
            } else { // ')'
                depth -= 1
                if depth > 0 { result.append(ch) }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeOuterParentheses(s: String): String {
        val sb = StringBuilder()
        var balance = 0
        for (ch in s) {
            if (ch == '(') {
                if (balance > 0) sb.append(ch)
                balance++
            } else { // ')'
                balance--
                if (balance > 0) sb.append(ch)
            }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String removeOuterParentheses(String s) {
    StringBuffer result = StringBuffer();
    int balance = 0;
    for (int i = 0; i < s.length; i++) {
      var ch = s[i];
      if (ch == '(') {
        if (balance > 0) result.write(ch);
        balance++;
      } else { // ')'
        balance--;
        if (balance > 0) result.write(ch);
      }
    }
    return result.toString();
  }
}
```

## Golang

```go
import "strings"

func removeOuterParentheses(s string) string {
	var sb strings.Builder
	balance := 0
	for _, ch := range s {
		if ch == '(' {
			if balance > 0 {
				sb.WriteByte('(')
			}
			balance++
		} else { // ')'
			balance--
			if balance > 0 {
				sb.WriteByte(')')
			}
		}
	}
	return sb.String()
}
```

## Ruby

```ruby
def remove_outer_parentheses(s)
  res = +''
  depth = 0
  s.each_char do |ch|
    if ch == '('
      res << ch if depth > 0
      depth += 1
    else # ')'
      depth -= 1
      res << ch if depth > 0
    end
  end
  res
end
```

## Scala

```scala
object Solution {
    def removeOuterParentheses(s: String): String = {
        val sb = new StringBuilder
        var depth = 0
        for (ch <- s) {
            if (ch == '(') {
                if (depth > 0) sb.append(ch)
                depth += 1
            } else { // ch == ')'
                depth -= 1
                if (depth > 0) sb.append(ch)
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_outer_parentheses(s: String) -> String {
        let mut result = String::with_capacity(s.len());
        let mut depth = 0;
        for ch in s.chars() {
            if ch == '(' {
                if depth > 0 {
                    result.push(ch);
                }
                depth += 1;
            } else { // ')'
                depth -= 1;
                if depth > 0 {
                    result.push(ch);
                }
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (remove-outer-parentheses s)
  (-> string? string?)
  (let loop ((chars (string->list s))
             (depth 0)
             (acc '()))
    (if (null? chars)
        (list->string (reverse acc))
        (let* ((c (car chars))
               (rest (cdr chars)))
          (cond
            [(char=? c #\()
             (if (> depth 0)
                 (loop rest (+ depth 1) (cons c acc))
                 (loop rest (+ depth 1) acc))]
            [(char=? c #\))
             (let ((new-depth (- depth 1)))
               (if (> new-depth 0)
                   (loop rest new-depth (cons c acc))
                   (loop rest new-depth acc)))]
            [else
             (loop rest depth acc)]))))))
```

## Erlang

```erlang
-spec remove_outer_parentheses(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
remove_outer_parentheses(S) ->
    List = binary_to_list(S),
    RevResult = go(List, 0, []),
    list_to_binary(lists:reverse(RevResult)).

go([], _Depth, Acc) ->
    Acc;
go([$\( | Rest], Depth, Acc) ->
    NewDepth = Depth + 1,
    case NewDepth of
        1 -> go(Rest, NewDepth, Acc);
        _ -> go(Rest, NewDepth, [$\( | Acc])
    end;
go([$\\) | Rest], Depth, Acc) ->
    case Depth of
        1 ->
            NewDepth = Depth - 1,
            go(Rest, NewDepth, Acc);
        _ ->
            NewDepth = Depth - 1,
            go(Rest, NewDepth, [$\\) | Acc])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_outer_parentheses(s :: String.t) :: String.t
  def remove_outer_parentheses(s) do
    {_, rev_chars} =
      String.graphemes(s)
      |> Enum.reduce({0, []}, fn
        "(", {bal, acc} ->
          new_bal = bal + 1
          if bal > 0, do: {new_bal, ["(" | acc]}, else: {new_bal, acc}

        ")", {bal, acc} ->
          new_bal = bal - 1
          if new_bal > 0, do: {new_bal, [")" | acc]}, else: {new_bal, acc}
      end)

    rev_chars |> Enum.reverse() |> Enum.join()
  end
end
```

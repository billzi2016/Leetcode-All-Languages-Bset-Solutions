# 1249. Minimum Remove to Make Valid Parentheses

## Cpp

```cpp
class Solution {
public:
    string minRemoveToMakeValid(string s) {
        int n = s.size();
        vector<bool> keep(n, true);
        vector<int> st;
        for (int i = 0; i < n; ++i) {
            if (s[i] == '(') {
                st.push_back(i);
            } else if (s[i] == ')') {
                if (!st.empty()) {
                    st.pop_back();
                } else {
                    keep[i] = false;
                }
            }
        }
        for (int idx : st) keep[idx] = false;
        string res;
        res.reserve(n);
        for (int i = 0; i < n; ++i) {
            if (keep[i]) res.push_back(s[i]);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String minRemoveToMakeValid(String s) {
        int n = s.length();
        char[] chars = s.toCharArray();
        boolean[] keep = new boolean[n];
        java.util.Stack<Integer> stack = new java.util.Stack<>();
        for (int i = 0; i < n; i++) {
            if (chars[i] == '(') {
                stack.push(i);
                keep[i] = true;
            } else if (chars[i] == ')') {
                if (!stack.isEmpty()) {
                    stack.pop();
                    keep[i] = true;
                } else {
                    keep[i] = false; // unmatched ')'
                }
            } else {
                keep[i] = true; // letters are always kept
            }
        }
        while (!stack.isEmpty()) {
            int idx = stack.pop();
            keep[idx] = false; // unmatched '('
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (keep[i]) {
                sb.append(chars[i]);
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        # First pass: remove invalid ')'
        filtered = []
        open_cnt = 0
        for ch in s:
            if ch == '(':
                open_cnt += 1
                filtered.append(ch)
            elif ch == ')':
                if open_cnt > 0:
                    open_cnt -= 1
                    filtered.append(ch)
                # else skip invalid ')'
            else:
                filtered.append(ch)

        # Second pass: remove extra '(' from the end
        result = []
        to_remove = open_cnt  # number of unmatched '(' left
        for ch in reversed(filtered):
            if ch == '(' and to_remove > 0:
                to_remove -= 1
                continue  # skip this '('
            result.append(ch)

        return ''.join(reversed(result))
```

## Python3

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        stack = []
        for i, ch in enumerate(chars):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    chars[i] = ''
        while stack:
            idx = stack.pop()
            chars[idx] = ''
        return ''.join(chars)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* minRemoveToMakeValid(char* s) {
    int n = strlen(s);
    char *keep = (char*)calloc(n, sizeof(char));
    int *stack = (int*)malloc(n * sizeof(int));
    int top = -1;

    for (int i = 0; i < n; ++i) {
        if (s[i] == '(') {
            stack[++top] = i;
        } else if (s[i] == ')') {
            if (top >= 0) {
                keep[stack[top--]] = 1;   // matched '('
                keep[i] = 1;               // matched ')'
            }
        } else {
            keep[i] = 1; // letters are always kept
        }
    }

    char *res = (char*)malloc((n + 1) * sizeof(char));
    int idx = 0;
    for (int i = 0; i < n; ++i) {
        if (keep[i]) {
            res[idx++] = s[i];
        }
    }
    res[idx] = '\0';

    free(keep);
    free(stack);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string MinRemoveToMakeValid(string s) {
        var firstPass = new System.Text.StringBuilder();
        int balance = 0;
        foreach (char c in s) {
            if (c == '(') {
                balance++;
                firstPass.Append(c);
            } else if (c == ')') {
                if (balance > 0) {
                    balance--;
                    firstPass.Append(c);
                }
            } else {
                firstPass.Append(c);
            }
        }

        var secondPass = new System.Text.StringBuilder();
        int needed = 0;
        for (int i = firstPass.Length - 1; i >= 0; i--) {
            char c = firstPass[i];
            if (c == ')') {
                needed++;
                secondPass.Append(c);
            } else if (c == '(') {
                if (needed > 0) {
                    needed--;
                    secondPass.Append(c);
                }
            } else {
                secondPass.Append(c);
            }
        }

        var arr = secondPass.ToString().ToCharArray();
        System.Array.Reverse(arr);
        return new string(arr);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var minRemoveToMakeValid = function(s) {
    const chars = s.split('');
    const stack = [];
    for (let i = 0; i < chars.length; i++) {
        if (chars[i] === '(') {
            stack.push(i);
        } else if (chars[i] === ')') {
            if (stack.length) {
                stack.pop();
            } else {
                chars[i] = '';
            }
        }
    }
    while (stack.length) {
        const idx = stack.pop();
        chars[idx] = '';
    }
    return chars.join('');
};
```

## Typescript

```typescript
function minRemoveToMakeValid(s: string): string {
    const n = s.length;
    const keep = new Array<boolean>(n).fill(true);
    let open = 0;

    for (let i = 0; i < n; i++) {
        const ch = s[i];
        if (ch === '(') {
            open++;
        } else if (ch === ')') {
            if (open > 0) {
                open--;
            } else {
                keep[i] = false;
            }
        }
    }

    for (let i = n - 1; i >= 0 && open > 0; i--) {
        if (s[i] === '(') {
            keep[i] = false;
            open--;
        }
    }

    const result: string[] = [];
    for (let i = 0; i < n; i++) {
        if (keep[i]) result.push(s[i]);
    }
    return result.join('');
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return String
     */
    function minRemoveToMakeValid($s) {
        $n = strlen($s);
        $stack = [];
        $remove = array_fill(0, $n, false);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if ($ch === '(') {
                $stack[] = $i;
            } elseif ($ch === ')') {
                if (!empty($stack)) {
                    array_pop($stack);
                } else {
                    $remove[$i] = true;
                }
            }
        }
        foreach ($stack as $idx) {
            $remove[$idx] = true;
        }
        $result = '';
        for ($i = 0; $i < $n; $i++) {
            if (!$remove[$i]) {
                $result .= $s[$i];
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func minRemoveToMakeValid(_ s: String) -> String {
        var chars = Array(s)
        var stack = [Int]()
        for i in 0..<chars.count {
            if chars[i] == "(" {
                stack.append(i)
            } else if chars[i] == ")" {
                if !stack.isEmpty {
                    stack.removeLast()
                } else {
                    chars[i] = "#"
                }
            }
        }
        for idx in stack {
            chars[idx] = "#"
        }
        return String(chars.filter { $0 != "#" })
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minRemoveToMakeValid(s: String): String {
        val n = s.length
        val remove = BooleanArray(n)
        val stack = java.util.ArrayDeque<Int>()
        for (i in 0 until n) {
            when (s[i]) {
                '(' -> stack.push(i)
                ')' -> {
                    if (stack.isEmpty()) {
                        remove[i] = true
                    } else {
                        stack.pop()
                    }
                }
            }
        }
        while (!stack.isEmpty()) {
            remove[stack.pop()] = true
        }
        val sb = StringBuilder()
        for (i in 0 until n) {
            if (!remove[i]) sb.append(s[i])
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String minRemoveToMakeValid(String s) {
    List<int> stack = [];
    List<bool> keep = List.filled(s.length, true);
    for (int i = 0; i < s.length; i++) {
      var ch = s[i];
      if (ch == '(') {
        stack.add(i);
      } else if (ch == ')') {
        if (stack.isNotEmpty) {
          stack.removeLast();
        } else {
          keep[i] = false;
        }
      }
    }
    for (int idx in stack) {
      keep[idx] = false;
    }
    StringBuffer sb = StringBuffer();
    for (int i = 0; i < s.length; i++) {
      if (keep[i]) sb.write(s[i]);
    }
    return sb.toString();
  }
}
```

## Golang

```go
func minRemoveToMakeValid(s string) string {
    runes := []rune(s)
    n := len(runes)
    keep := make([]bool, n)
    for i := 0; i < n; i++ {
        keep[i] = true
    }

    open := 0
    // Left to right: remove unmatched ')'
    for i, ch := range runes {
        if ch == '(' {
            open++
        } else if ch == ')' {
            if open == 0 {
                keep[i] = false
            } else {
                open--
            }
        }
    }

    closeCnt := 0
    // Right to left: remove unmatched '('
    for i := n - 1; i >= 0; i-- {
        ch := runes[i]
        if ch == ')' {
            closeCnt++
        } else if ch == '(' {
            if closeCnt == 0 {
                keep[i] = false
            } else {
                closeCnt--
            }
        }
    }

    var sb strings.Builder
    for i, ch := range runes {
        if keep[i] {
            sb.WriteRune(ch)
        }
    }
    return sb.String()
}
```

## Ruby

```ruby
def min_remove_to_make_valid(s)
  n = s.length
  remove = Array.new(n, false)
  stack = []

  s.each_char.with_index do |ch, i|
    if ch == '('
      stack << i
    elsif ch == ')'
      if stack.empty?
        remove[i] = true
      else
        stack.pop
      end
    end
  end

  stack.each { |idx| remove[idx] = true }

  result = []
  s.each_char.with_index do |ch, i|
    result << ch unless remove[i]
  end

  result.join
end
```

## Scala

```scala
object Solution {
    def minRemoveToMakeValid(s: String): String = {
        val firstPass = new StringBuilder
        var open = 0
        for (c <- s) {
            c match {
                case '(' =>
                    open += 1
                    firstPass.append(c)
                case ')' =>
                    if (open > 0) {
                        open -= 1
                        firstPass.append(c)
                    }
                case _ => firstPass.append(c)
            }
        }

        val result = new StringBuilder
        var toRemove = open
        for (i <- firstPass.length - 1 to 0 by -1) {
            val c = firstPass.charAt(i)
            if (c == '(' && toRemove > 0) {
                toRemove -= 1 // skip this '('
            } else {
                result.append(c)
            }
        }

        result.reverse.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_remove_to_make_valid(s: String) -> String {
        let chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        let mut stack: Vec<usize> = Vec::new();
        let mut remove = vec![false; n];

        for (i, &c) in chars.iter().enumerate() {
            if c == '(' {
                stack.push(i);
            } else if c == ')' {
                if stack.pop().is_none() {
                    remove[i] = true;
                }
            }
        }

        while let Some(idx) = stack.pop() {
            remove[idx] = true;
        }

        let mut result = String::with_capacity(n);
        for (i, &c) in chars.iter().enumerate() {
            if !remove[i] {
                result.push(c);
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (min-remove-to-make-valid s)
  (-> string? string?)
  (let* ((n (string-length s))
         (keep (make-vector n #f))
         (stack '()))
    ;; First pass: left to right, mark characters to keep
    (for ([i (in-range n)])
      (let ((c (string-ref s i)))
        (cond [(char=? c #\()
               (set! stack (cons i stack))
               (vector-set! keep i #t)]
              [(char=? c #\))
               (if (null? stack)
                   (vector-set! keep i #f) ; unmatched ')'
                   (begin
                     (set! stack (cdr stack))
                     (vector-set! keep i #t)))]
              [else
               (vector-set! keep i #t)])))
    ;; Second pass: remove any remaining unmatched '('
    (for ([idx stack])
      (vector-set! keep idx #f))
    ;; Build the resulting string
    (list->string
     (for/list ([i (in-range n)] #:when (vector-ref keep i))
       (string-ref s i)))))
```

## Erlang

```erlang
-module(solution).
-export([min_remove_to_make_valid/1]).
-spec min_remove_to_make_valid(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
min_remove_to_make_valid(S) ->
    Chars = unicode:characters_to_list(S),
    {Rev1, _Open} = left_pass(Chars, 0, []),
    Rev2 = right_pass(Rev1, 0, []),
    list_to_binary(lists:reverse(Rev2)).

left_pass([], Open, Acc) ->
    {Acc, Open};
left_pass([C|Rest], Open, Acc) ->
    case C of
        $( ->
            left_pass(Rest, Open + 1, [C | Acc]);
        $) ->
            if Open > 0 ->
                    left_pass(Rest, Open - 1, [C | Acc]);
               true ->
                    left_pass(Rest, Open, Acc)
            end;
        _ ->
            left_pass(Rest, Open, [C | Acc])
    end.

right_pass([], _Close, Acc) ->
    Acc;
right_pass([C|Rest], Close, Acc) ->
    case C of
        $) ->
            right_pass(Rest, Close + 1, [C | Acc]);
        $( ->
            if Close > 0 ->
                    right_pass(Rest, Close - 1, [C | Acc]);
               true ->
                    right_pass(Rest, Close, Acc)
            end;
        _ ->
            right_pass(Rest, Close, [C | Acc])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_remove_to_make_valid(s :: String.t()) :: String.t()
  def min_remove_to_make_valid(s) do
    {rev_chars, open_cnt} =
      s
      |> String.to_charlist()
      |> Enum.reduce({[], 0}, fn
        ?(, {acc, cnt} -> {[?( | acc], cnt + 1}
        ?), {acc, cnt} ->
          if cnt > 0 do
            {[?) | acc], cnt - 1}
          else
            {acc, cnt}
          end
        ch, {acc, cnt} -> {[ch | acc], cnt}
      end)

    {clean_rev, _} =
      Enum.reduce(rev_chars, {[], open_cnt}, fn
        ?(, {acc, to_remove}) when to_remove > 0 ->
          {acc, to_remove - 1}
        ch, {acc, to_remove} ->
          {[ch | acc], to_remove}
      end)

    clean_rev
    |> :lists.reverse()
    |> List.to_string()
  end
end
```
